"""Custom exceptions for the MLLM HPC evaluation pipeline.

HPC Pipeline Role — Error Taxonomy
====================================
Maps each failure mode to its architectural origin:

- ``ConfigurationError``  — Contract violation at initialisation (Layer 2).
- ``ModelLoadError``       — Generative model failed to initialise (Layer 1).
- ``InferenceError``       — Top-down prediction generation failed (Layer 3).
- ``DataProcessingError``  — Sensory input preprocessing failed (Layer 2).
- ``APIError``             — Network transport failure (cross-layer).
- ``RateLimitError``       — Engine back-pressure signal (Layer 1).
- ``TokenLimitError``      — Context window overflow (Layer 3).
"""

from typing import Optional

class MLLMError(Exception):
    """Base exception for all mllm errors."""
    pass

class ConfigurationError(MLLMError):
    """Raised when configuration is invalid."""
    pass

class ModelLoadError(MLLMError):
    """Raised when model loading fails."""
    pass

class InferenceError(MLLMError):
    """Raised when inference fails."""
    pass

class DataProcessingError(MLLMError):
    """Raised when data processing fails."""
    pass

class APIError(MLLMError):
    """Raised when API calls fail."""
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code

class RateLimitError(APIError):
    """Raised when API rate limit is exceeded."""
    pass

class TokenLimitError(MLLMError):
    """Raised when token limit is exceeded."""
    def __init__(self, message: str, tokens_used: int, max_tokens: int):
        super().__init__(message)
        self.tokens_used = tokens_used
        self.max_tokens = max_tokens

class CompatibilityError(MLLMError):
    """Raised when a model-backend pair is incompatible."""
    pass
