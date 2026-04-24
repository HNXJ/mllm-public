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
    print("[VERBOSITY] Executing: payload = {'model': profile.model_name, 'messages': [{'ro...")
    payload = {'model': profile.model_name, 'messages': [{'role': 'user', 'content': prompt}], 'temperature': profile.temperature, 'max_tokens': profile.max_tokens, 'top_p': 0.9}
    print("[VERBOSITY] Executing: headers = {'Authorization': f'Bearer {profile.api_key}', ...")
    headers = {'Authorization': f'Bearer {profile.api_key}', 'Content-Type': 'application/json'}
    print('[VERBOSITY] Executing: response = requests.post(profile.api_url, timeout=(10, 36...')
    response = requests.post(profile.api_url, timeout=(10, 3600), headers=headers, json=payload)
    print('[VERBOSITY] Executing: if response.status_code != 200:')
    if response.status_code != 200:
        logger.error(f'❌ API Error ({response.status_code}) for model {profile.model_name}: {response.text}')
    print('[VERBOSITY] Executing: response.raise_for_status()')
    response.raise_for_status()
    print('[VERBOSITY] Executing: result_json = response.json()')
    result_json = response.json()
    print("[VERBOSITY] Executing: if 'choices' not in result_json or not result_json['choic...")
    if 'choices' not in result_json or not result_json['choices']:
        raise InferenceError(f'Unexpected LLM response format: {result_json}')
    print("[VERBOSITY] Executing: choice = result_json['choices'][0]")
    choice = result_json['choices'][0]
    print("[VERBOSITY] Executing: content = choice.get('message', {}).get('content') or cho...")
    content = choice.get('message', {}).get('content') or choice.get('content') or choice.get('text')
    print('[VERBOSITY] Executing: if content:')
    if content:
        return content
    raise InferenceError(f'LLM response missing content field. JSON: {result_json}')

def get_llm_thinking(unified_prompt, config, profile, response_model=HpcEvaluationResponse):
    print("[VERBOSITY] Executing: prompt = f'{unified_prompt}\\n\\nReturn exactly one valid J...")
    prompt = f'{unified_prompt}\n\nReturn exactly one valid JSON object and nothing else.'
    print('[VERBOSITY] Executing: try:')
    try:
        result_content = _call_llm_api(prompt, profile, timeout=config.request_timeout_seconds)
        parsed_data = parse_llm_output_as_json(result_content, compatibility_mode=not config.strict_json_parsing)
        if parsed_data.get('REPAIR_REQUIRED'):
            return json.dumps(parsed_data, indent=2)
        if response_model is not None:
            validated = response_model.model_validate(parsed_data)
            return json.dumps(validated.model_dump(), indent=2)
        return json.dumps(parsed_data, indent=2)
    except Exception as exc:
        logger.error(f'❌ Reasoning error: {exc}')
        raise InferenceError(f'LLM reasoning phase failed: {exc}') from exc