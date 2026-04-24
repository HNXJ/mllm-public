import json
import os
from pathlib import Path

import pytest

from mllm.prompts import parse_glossary, build_hpc_prompt
from mllm.models.llm_wrapper import get_llm_thinking
from mllm.config.model_config import ModelProfile, InferenceConfig
from mllm.schemas import HpcEvaluationResponse

pytestmark = pytest.mark.integration


def test_hpc_eval_roundtrip(tmp_path: Path):
    required_env = ["RUN_HPC_INTEGRATION", "HPC_MODEL_NAME", "HPC_API_URL", "ENGINE_API_KEY"]
    missing = [key for key in required_env if not os.environ.get(key)]
    if missing:
        pytest.skip(f"Missing integration environment variables: {', '.join(missing)}")

    repo_root = Path(__file__).resolve().parents[2]
    glossary_content, glossary_keys = parse_glossary("HPC", repo_root=repo_root)

    study_text = (
        "Bastos et al. tested local and global oddball conditions using auditory sequences. "
        "Mismatch responses were stronger for global violations than for local repetition changes. "
        "Figures 2 and 3 suggest stronger expectation-related responses in higher cortical areas."
    )

    model_name = os.environ["HPC_MODEL_NAME"]
    api_url = os.environ["HPC_API_URL"]
    api_key = os.environ["ENGINE_API_KEY"]

    prompt = build_hpc_prompt(study_text, glossary_content, glossary_keys, model_name)

    config = InferenceConfig(
        min_tokens_requested=1000,
        prompt_role="Expert Neuroscientist",
        request_timeout_seconds=300,
        strict_json_parsing=True,
    )
    profile = ModelProfile(
        model_name=model_name,
        api_url=api_url,
        api_key=api_key,
        max_tokens=8192,
        temperature=0.0,
        context_window=128000,
        engine_type="lms",
    )

    result = get_llm_thinking(prompt, config, profile)
    validated = HpcEvaluationResponse.model_validate(json.loads(result))

    assert isinstance(validated.lo_evaluations, dict)
    assert isinstance(validated.go_evaluations, dict)

    out_file = tmp_path / "hpc_eval.json"
    out_file.write_text(json.dumps(validated.model_dump(), indent=2))
    assert out_file.exists()
