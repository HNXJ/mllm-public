import pytest
from mllm.data.preprocessors import clean_json_string, parse_llm_output_as_json


def test_clean_json_string_strips_fences():
    raw = """```json
{"a": 1}
```"""
    assert clean_json_string(raw) == '{"a": 1}'


def test_parse_llm_output_as_json_parses_object():
    raw = """```json
{"scores": []}
```"""
    parsed = parse_llm_output_as_json(raw)
    assert parsed == {"scores": []}

def test_parse_llm_output_as_json_strict_rejects_extra_text():
    raw = 'prefix {"scores": []} suffix'
    parsed = parse_llm_output_as_json(raw, compatibility_mode=False)
    assert isinstance(parsed, dict)
    assert parsed.get("REPAIR_REQUIRED") is True
    assert parsed.get("raw_output") == raw

def test_parse_llm_output_as_json_compatibility_mode_can_salvage():
    raw = 'prefix {"scores": []} suffix'
    parsed = parse_llm_output_as_json(raw, compatibility_mode=True)
    assert parsed == {"scores": []}
