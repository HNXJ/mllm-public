from mllm.data.preprocessors import parse_llm_output_as_json

def test_parse_json_response_smoke():
    payload = parse_llm_output_as_json('{"scores": []}')
    assert payload == {"scores": []}

def test_parse_json_response_with_markdown_in_compatibility_mode():
    raw = """Here is the result:
```json
{"scores": [{"factor_name": "test", "score": 1.0}]}
```"""
    payload = parse_llm_output_as_json(raw, compatibility_mode=True)
    assert payload["scores"][0]["factor_name"] == "test"
