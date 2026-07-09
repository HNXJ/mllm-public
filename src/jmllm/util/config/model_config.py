"""Configuration models for the MLLM HPC evaluation platform (Pydantic V2).

HPC Pipeline Role — Contract Definitions
=========================================
This module defines the machine-readable contracts that govern the entire
HPC evaluation pipeline.  In Predictive Coding terms:

- ``ModelProfile``    — specifies the *generative model identity* (which LLM
  produces top-down predictions).
- ``InferenceConfig`` — controls the *precision weighting* (timeout, token
  minimums, JSON strictness) applied to each inference run.
- ``PipelineConfig``  — defines the *experimental protocol* (input/output
  directories, parallel workers).
- ``ModelManifest``   — the *model passport* declaring backend support,
  quantisation status, and context-window constraints.
- ``ReleaseManifest`` — the *reproducibility snapshot* capturing exact commit,
  toolchain, and environment at execution time.

All configs inherit from ``BaseConfig`` which provides YAML serialisation.
"""

from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Dict, Any
from pathlib import Path
import yaml

class BaseConfig(BaseModel):
    """Base configuration with YAML support."""
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True
    )
    
    @classmethod
    def from_yaml(cls, path: Path) -> 'BaseConfig':
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)
    
    def to_yaml(self, path: Path) -> None:
        with open(path, 'w') as f:
            yaml.dump(self.model_dump(), f, default_flow_style=False)

class BackendSupport(BaseConfig):
    """Configuration for backend-specific support and quantization."""
    backend_name: str = Field(..., description="Name of the backend (mlx, lms, vulkan, cuda)")
    is_production: bool = Field(False, description="Whether this backend is production-ready for the model")
    supported_quantizations: List[str] = Field(default_factory=lambda: ["fp16"], description="Supported quantization levels")
    max_batch_size: int = Field(1, ge=1)
    performance_tier: str = Field("experimental", description="Performance tier (high, medium, low, experimental)")

class ModelManifest(BaseConfig):
    """The authoritative machine-readable contract for a model in the MLLM platform."""
    model_id: str = Field(..., description="Unique identifier for the model (e.g., phi-4-neuro)")
    display_name: str = Field(..., description="Human-readable name")
    version: str = Field("1.0.0", description="Model version")
    
    # Model Components
    tokenizer_type: str = Field("auto", description="Tokenizer class/type required")
    processor_type: Optional[str] = Field(None, description="Vision/Multimodal processor type")
    
    # Contracts & Constraints
    context_window: int = Field(131072, ge=512)
    input_shape_constraints: Dict[str, Any] = Field(default_factory=dict, description="Constraints on input tensors/text")
    
    # Multi-backend Support Matrix
    backends: List[BackendSupport] = Field(..., description="List of supported backends and their status")
    
    # Metadata
    author: str = Field("Unknown")
    license: str = Field("Proprietary")
    tags: List[str] = Field(default_factory=list)

class ReleaseManifest(BaseConfig):
    """Authoritative reproducibility snapshot for a specific build or run."""
    commit_hash: str = Field(..., description="Commit ID of the source code")
    timestamp: str = Field(..., description="ISO 8601 timestamp of execution/build")
    python_version: str = Field(..., description="Version of the Python interpreter")
    environment_tags: List[str] = Field(default_factory=list, description="Environment tags (macOS, CUDA, MLX, etc.)")
    
    # Toolchain & Backend
    toolchain_version: str = Field("unknown", description="Compiler/Toolchain version (e.g., clang-16)")
    quantization_mode: Optional[str] = Field(None, description="Global quantization setting applied")
    
    # Model Status
    active_manifest: Optional[ModelManifest] = Field(None, description="The manifest of the model being run")
    compatibility_score: float = Field(0.0, ge=0.0, le=1.0)

class ModelProfile(BaseConfig):
    """Configuration for a specific LLM model profile."""
    model_name: str = Field(..., description="The name of the model")
    api_url: str = Field(..., description="The API endpoint URL")
    api_key: str = Field("none", description="The API key if required")
    max_tokens: int = Field(32768, description="Maximum tokens for generation")
    temperature: float = Field(0.8, ge=0.0, le=2.0)
    context_window: int = Field(131072, description="Maximum context window size")
    engine_type: str = Field("lms", description="Engine type (lms, vlm, mlx)")

class InferenceConfig(BaseConfig):
    """Configuration for an inference run."""
    prompt_role: str = Field("Expert Neuroscientist", description="System prompt role")
    min_tokens_requested: int = Field(1000, description="Minimum tokens for reasoning output")
    glossary_path: Optional[Path] = Field(None, description="Path to the scoring glossary")
    rules_path: Optional[Path] = Field(None, description="Path to the scoring rules")
    output_format_example: Optional[str] = Field(None, description="Example of expected output")
    request_timeout_seconds: int = Field(900, ge=1, description="HTTP timeout for inference requests")
    strict_json_parsing: bool = Field(False, description="Require strict JSON-only model output")

class PipelineConfig(BaseConfig):
    """Global configuration for the MLLM pipeline."""
    input_dir: Path = Field(..., description="Directory for input studies")
    output_dir: Path = Field(..., description="Directory for evaluation results")
    log_dir: Path = Field(Path("./logs"), description="Directory for logs")
    models: List[ModelProfile] = Field(default_factory=list, description="List of configured models")
    parallel_workers: int = Field(1, ge=1, description="Number of parallel processing workers")
    
    @field_validator('output_dir', 'log_dir', mode='before')
    @classmethod
    def ensure_path(cls, v: Any) -> Path:
        p = Path(v)
        p.mkdir(parents=True, exist_ok=True)
        return p
