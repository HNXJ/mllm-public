"""Canonical profile management for MLLM models.

HPC Pipeline Role — Configuration Layer (Layer 3: SDK & Bindings)
===============================================================
This module manages model-specific profiles, ensuring that the pipeline
consumes validated context windows, prompt templates, and precision
data from the 'src/mllm/config/profiles/' registry.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from mllm.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

PROFILES_DIR = Path(__file__).parent / "profiles"

def get_model_manifest(model_name: str) -> Optional[Dict[str, Any]]:
    """Retrieve the JSON manifest for a specific model."""
    profile_path = PROFILES_DIR / f"{model_name}-full-profile.json"
    if not profile_path.exists():
        # Try without the full-profile suffix if not found
        profile_path = PROFILES_DIR / f"{model_name}.json"
        
    if not profile_path.exists():
        return None
        
    try:
        with open(profile_path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Malformed JSON in profile {profile_path.name}: {e}")
        return None

def list_available_models() -> List[str]:
    """List all models registered in the canonical profiles directory."""
    models = []
    for p in PROFILES_DIR.glob("*.json"):
        name = p.stem.replace("-full-profile", "")
        models.append(name)
    return sorted(list(set(models)))

def validate_model_profile(model_name: str) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    """Strictly validate a model profile existence and schema."""
    profile_path = PROFILES_DIR / f"{model_name}-full-profile.json"
    if not profile_path.exists():
        profile_path = PROFILES_DIR / f"{model_name}.json"
        
    if not profile_path.exists():
        return False, f"Profile file not found in {PROFILES_DIR}", None
        
    try:
        with open(profile_path, "r") as f:
            data = json.load(f)
            # Basic schema check
            required = ["model_name", "api_url", "engine_type"]
            missing = [f for f in required if f not in data]
            if missing:
                return False, f"Missing required fields: {missing}", data
            return True, "Valid", data
    except json.JSONDecodeError as e:
        return False, f"Malformed JSON: {str(e)}", None
    except Exception as e:
        return False, f"Unexpected error: {str(e)}", None

def get_profiles_summary() -> str:
    """Generate a human-readable summary of all available profiles."""
    models = list_available_models()
    summary = [f"Registry: {PROFILES_DIR}", f"Count: {len(models)} models registered."]
    for m in models:
        valid, msg, _ = validate_model_profile(m)
        status = "✅" if valid else "❌"
        summary.append(f"  {status} {m:<30} | {msg}")
    return "\n".join(summary)
