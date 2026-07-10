import json
import logging
import requests
from typing import Any, Dict, List, Optional, Type
from pydantic import BaseModel
from jmllm.util.config.model_config import ModelProfile, InferenceConfig
from jmllm.util.schemas import HpcEvaluationResponse
from jmllm.util.helpers import parse_llm_output_as_json
from jmllm.util.logging import setup_logger
logger = setup_logger(__name__)

class InferenceError(Exception):
    pass

import time

def _call_llm_api_raw(prompt, profile, timeout=300):
    provider = getattr(profile, "provider", "mlx").lower()
    headers = {"Content-Type": "application/json"}
    payload = {}
    
    import os
    api_key = profile.api_key
    if api_key == "none" or api_key == "none":
        if provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY", "none")
        elif provider == "google":
            api_key = os.getenv("GEMINI_API_KEY", "none")
        elif provider == "anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY", "none")

    if provider == "anthropic":
        headers["x-api-key"] = api_key
        headers["anthropic-version"] = "2023-06-01"
        payload = {
            "model": profile.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": profile.max_tokens,
            "temperature": profile.temperature
        }
    elif provider == "ollama":
        payload = {
            "model": profile.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {
                "temperature": profile.temperature,
                "num_predict": profile.max_tokens
            }
        }
        if profile.top_p is not None:
            payload["options"]["top_p"] = profile.top_p
    else:
        # Default MLX / LM Studio / OpenAI / Google (OpenAI compatible)
        headers["Authorization"] = f"Bearer {api_key}"
        payload = {
            "model": profile.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": profile.temperature,
            "max_tokens": profile.max_tokens
        }
        if getattr(profile, 'top_p', None) is not None:
            payload['top_p'] = profile.top_p
        if getattr(profile, 'min_p', None) is not None:
            payload['min_p'] = profile.min_p
        if getattr(profile, 'response_format', None) is not None:
            payload['response_format'] = profile.response_format

    url = profile.api_url
    print(f"[VERBOSITY] Executing API request to {url} for provider {provider}...")
    response = requests.post(url, timeout=timeout, headers=headers, json=payload)
    
    if response.status_code != 200:
        logger.error(f'❌ API Error ({response.status_code}) for model {profile.model_name}: {response.text}')
        response.raise_for_status()
        
    result_json = response.json()
    
    if provider == "anthropic":
        content = result_json.get("content", [{}])[0].get("text")
        if content:
            return content
    elif provider == "ollama":
        content = result_json.get("message", {}).get("content")
        if content:
            return content
    else:
        if 'choices' not in result_json or not result_json['choices']:
            raise InferenceError(f'Unexpected LLM response format: {result_json}')
        choice = result_json['choices'][0]
        content = choice.get('message', {}).get('content') or choice.get('content') or choice.get('text')
        if content:
            return content
            
    raise InferenceError(f'LLM response missing content field. JSON: {result_json}')

def _call_llm_api(prompt, profile, timeout=300):
    max_retries = 3
    backoff_factor = 2
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return _call_llm_api_raw(prompt, profile, timeout)
        except (requests.exceptions.RequestException, InferenceError) as e:
            last_exception = e
            logger.warning(f"⚠️ API call attempt {attempt+1} failed: {e}. Retrying in {backoff_factor ** attempt}s...")
            time.sleep(backoff_factor ** attempt)
            
    raise InferenceError(f"API call failed after {max_retries} attempts. Last error: {last_exception}")

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