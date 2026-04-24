import json
import logging
import requests
from typing import Any, Dict, List, Optional, Type
from pydantic import BaseModel
from mllm.config.model_config import ModelProfile, InferenceConfig
from mllm.schemas import HpcEvaluationResponse
from mllm.data.preprocessors import parse_llm_output_as_json
from mllm.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

class InferenceError(Exception):
    pass

def _call_llm_api(prompt, profile, timeout=300):
    payload = {
        'model': profile.model_name,
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': profile.temperature,
        'max_tokens': profile.max_tokens,
        'stream': False,
    }
    headers = {
        'Authorization': f'Bearer {profile.api_key}',
        'Content-Type': 'application/json',
    }
    response = requests.post(profile.api_url, timeout=(10, 3600), headers=headers, json=payload)
    response.raise_for_status()
    result_json = response.json()
    
    if 'choices' not in result_json or not result_json['choices']:
        raise InferenceError(f'Unexpected LLM response format: {result_json}')

    choice = result_json['choices'][0]
    
    # Defensive content retrieval
    content = choice.get('message', {}).get('content') or choice.get('content') or choice.get('text')
    if content:
        return content, choice.get('finish_reason')
    
    raise InferenceError(f'LLM response missing content field. JSON: {result_json}')

def get_llm_thinking(unified_prompt, config, profile, response_model=HpcEvaluationResponse):
    for attempt in range(2):
        prompt = f'{unified_prompt}\n\nReturn exactly one valid JSON object and nothing else.'
        try:
            result_content, finish_reason = _call_llm_api(prompt, profile, timeout=config.request_timeout_seconds)
            
            # Handle token truncation (length finish reason)
            if finish_reason == 'length' and attempt < 1:
                logger.warning(f'⚠️ Model output truncated. Increasing tokens and retrying...')
                profile.max_tokens = int(profile.max_tokens * 1.5)
                continue

            parsed_data = parse_llm_output_as_json(result_content, compatibility_mode=not config.strict_json_parsing)

            if parsed_data.get('REPAIR_REQUIRED'):
                return json.dumps(parsed_data, indent=2)

            if response_model is not None:
                validated = response_model.model_validate(parsed_data)
                return json.dumps(validated.model_dump(), indent=2)

            return json.dumps(parsed_data, indent=2)
        except Exception as exc:
            logger.error(f'❌ Reasoning error (attempt {attempt+1}): {exc}')
            if attempt == 1:
                raise InferenceError(f'LLM reasoning phase failed after retries: {exc}') from exc
