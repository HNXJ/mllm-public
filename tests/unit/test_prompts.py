from mllm.prompts import get_glossary_instruction_block, build_hpc_prompt


def test_get_glossary_instruction_block_from_list():
    result = get_glossary_instruction_block(["term1", "term2"])
    assert "<glossary>" in result
    assert "term1" in result
    assert "term2" in result


def test_get_glossary_instruction_block_from_dict():
    result = get_glossary_instruction_block({"term1": "def1", "term2": "def2"})
    assert "<glossary>" in result
    assert "- term1: def1" in result
    assert "- term2: def2" in result

def test_build_hpc_prompt_requires_json_and_exact_keys():
    prompt = build_hpc_prompt(
        study_text="Study text",
        glossary="""Factor A: desc
Factor B: desc""",
        glossary_keys=["Factor A", "Factor B"],
        model_name="test-model",
    )
    assert "Return exactly one valid JSON object" in prompt
    assert "Include every glossary key exactly once" in prompt
    assert "Use `null` when a factor is not meaningfully addressed." in prompt
    assert '"agent_name": "test-model"' in prompt
