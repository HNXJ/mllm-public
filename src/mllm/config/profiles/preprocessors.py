"""Data preprocessors for LLM output parsing and score aggregation.

HPC Pipeline Role — Precision Weighting & Normalisation
========================================================
In Hierarchical Predictive Coding, raw prediction signals must be
normalised and validated before they can inform higher-level inference.
This module performs that role for the MLLM pipeline:

- ``clean_json_string``         — Strips markdown fencing and whitespace
  artefacts from LLM responses (analogous to removing sensory noise).
- ``parse_llm_output_as_json``  — Parses the cleaned string into a Python
  dict, enforcing the JSON contract.
- ``aggregate_scores_from_json`` — Collects scores from multiple evaluation
  JSON files into a DataFrame for cross-model analysis.
"""

import re
import json
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Optional
from mllm.utils.logging_utils import setup_logger
from mllm.utils.exceptions import DataProcessingError

logger = setup_logger(__name__)

# --- Canonical JSON Parsing Logic ---

def clean_json_string(text: str, compatibility_mode: bool = False) -> str:
    """Strip markdown fencing and whitespace from an LLM JSON response.

    In ``compatibility_mode``, attempts to salvage a JSON object embedded
    in surrounding prose by locating the outermost ``{...}`` boundaries.
    This handles models that prepend explanatory text before their JSON.

    Args:
        text:               Raw LLM output string.
        compatibility_mode: If ``True``, attempt brace-bounded extraction.

    Returns:
        Cleaned string suitable for ``json.loads()``.
    """
    if text is None:
        return ""

    # Strip <think>...</think> tags if present (common in reasoning models)
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    cleaned = text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:].strip()
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:].strip()

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3].strip()

    if compatibility_mode and not (cleaned.startswith("{") and cleaned.endswith("}")):
        try:
            start_idx = cleaned.index("{")
            end_idx = cleaned.rindex("}") + 1
            cleaned = cleaned[start_idx:end_idx]
        except ValueError:
            pass

    # AXIOMATIC PATCH (E11):  Convert common non-JSON strings to null/valid JSON.
    cleaned = re.sub(r':\s*"null"', ': null', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r':\s*"None"', ': null', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r':\s*"nan"', ': null', cleaned, flags=re.IGNORECASE)

    return cleaned


def ultra_clean_json(text: str) -> str:
    """Aggressively strip non-printable characters to rescue malformed JSON.

    Used as a last resort when standard cleaning and strict=False both fail.
    Strips everything except standard ASCII printables and basic whitespace.
    """
    # Keep only printable characters (32-126) and basic whitespace (\n, \r, \t)
    return "".join(c for c in text if 32 <= ord(c) <= 126 or c in "\n\r\t")


def parse_llm_output_as_json(
    text: str, compatibility_mode: bool = False
) -> Dict[str, Any]:
    """Parse an LLM response string into a Python dictionary.

    Implements a multi-stage rescue for noisy model outputs:
    1. Standard clean + json.loads(strict=True)
    2. Standard clean + json.loads(strict=False)
    3. Brace-Bounded extraction (Stage 2.5) + json.loads(strict=False)
    4. Ultra-clean (strip non-printables) + json.loads(strict=False)

    If all fails, returns a 'REPAIR_REQUIRED' dict instead of raising.

    Args:
        text:               Raw LLM output.
        compatibility_mode: Passed through to ``clean_json_string``.

    Returns:
        Parsed dictionary or a special repair-flagged dictionary.
    """
    cleaned = clean_json_string(text, compatibility_mode=compatibility_mode)

    if not cleaned:
        return {
            "REPAIR_REQUIRED": True,
            "error": "Model output was empty after cleaning",
            "raw_output": text
        }

    # Stage 1: Attempt standard parse (strict)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Stage 2: Attempt robust parse (non-strict control characters)
    try:
        return json.loads(cleaned, strict=False)
    except json.JSONDecodeError:
        pass

    # Stage 2.5: Forced Brace-Bounded extraction (Rescue for reasoning prose)
    if not (cleaned.startswith("{") and cleaned.endswith("}")):
        try:
            start_idx = cleaned.index("{")
            end_idx = cleaned.rindex("}") + 1
            braced = cleaned[start_idx:end_idx]
            return json.loads(braced, strict=False)
        except (ValueError, json.JSONDecodeError):
            pass

    # Stage 3: Attempt Ultra-Clean parse (strip junk)
    try:
        ultra = ultra_clean_json(cleaned)
        return json.loads(ultra, strict=False)
    except json.JSONDecodeError as exc:
        last_exception = exc

    # FAILURE: Return repair-flagged object
    logger.warning("⚠️ JSON parsing failed all rescue stages. Returning REPAIR_REQUIRED flag.")
    return {
        "REPAIR_REQUIRED": True,
        "error": str(last_exception),
        "raw_output": text
    }


def aggregate_scores_from_json(json_dir: Path) -> pd.DataFrame:
    """Aggregates scores from multiple JSON evaluation files into a single DataFrame."""
    all_results = []
    
    if not json_dir.exists():
        logger.warning(f"JSON directory {json_dir} does not exist.")
        return pd.DataFrame()

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            # Extract basic metadata
            # OPTIMISATION: use stem (no extension) and split more
            # robustly.  Previous code split on '_' which failed for
            # filenames like 'Sterzer2024ccc_Mistral-Nemo-12B_HPC.json'.
            name_parts = json_file.stem.split('_')
            study = name_parts[0]
            model = name_parts[1] if len(name_parts) > 1 else "unknown"
            
            # Handle both schema types (flat scores or grouped lo/go)
            if "lo_evaluations" in data and "go_evaluations" in data:
                # Grouped schema (HPC evaluation)
                for context in ["lo", "go"]:
                    evals = data.get(f"{context}_evaluations", {})
                    for factor, val in evals.items():
                        score_val = val if isinstance(val, (int, float)) else None
                        all_results.append({
                            "Study": study, "Model": model, "Context": context.upper(),
                            "Factor": factor, "Score": score_val
                        })
            elif "scores" in data:
                # Generic scores schema
                scores = data.get("scores", [])
                if isinstance(scores, list):
                    # List of factor objects
                    for item in scores:
                        all_results.append({
                            "Study": study, "Model": model, "Context": "GENERAL",
                            "Factor": item.get("factor_name", "Unknown"),
                            "Score": item.get("score")
                        })
                elif isinstance(scores, dict):
                    # Dict of factors
                    for factor, val in scores.items():
                        score_val = val if isinstance(val, (int, float)) else None
                        all_results.append({
                            "Study": study, "Model": model, "Context": "GENERAL",
                            "Factor": factor, "Score": score_val
                        })
        except Exception as e:
            logger.error(f"❌ Error processing {json_file.name}: {e}")
            
    return pd.DataFrame(all_results)
