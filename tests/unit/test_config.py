"""Unit tests for configuration validation."""

import pytest
from mllm.config.model_config import ModelProfile, PipelineConfig, InferenceConfig

def test_model_profile_validation():
    # Valid profile
    profile = ModelProfile(
        model_name="phi-4",
        api_url="http://localhost:4474/v1"
    )
    assert profile.model_name == "phi-4"
    assert profile.engine_type == "lms"

    # Invalid temperature
    with pytest.raises(ValueError):
        ModelProfile(
            model_name="phi-4",
            api_url="http://localhost:4474/v1",
            temperature=2.5
        )

def test_pipeline_config_path_creation(tmp_path):
    input_dir = tmp_path / "inputs"
    output_dir = tmp_path / "outputs"
    input_dir.mkdir()
    
    # Pydantic should auto-create output_dir via validator if it doesn't exist
    config = PipelineConfig(
        input_dir=input_dir,
        output_dir=output_dir / "new_results"
    )
    assert (output_dir / "new_results").exists()

def test_inference_config_defaults():
    config = InferenceConfig()
    assert config.prompt_role == "Expert Neuroscientist"
    assert config.min_tokens_requested == 1000
