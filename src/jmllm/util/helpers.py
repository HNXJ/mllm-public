import os
import re
import sys
import glob
import json
import time
import platform
import subprocess
import threading
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

from jmllm.util.config.model_config import ReleaseManifest, ModelManifest
from jmllm.util.logging import setup_logger

logger = setup_logger(__name__)

# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

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


# =============================================================================
# REPRODUCIBILITY UTILITIES
# =============================================================================

def get_git_commit() -> str:
    """Get the current git commit hash."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], 
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except (subprocess.SubprocessError, Exception):
        return "unknown"

def get_toolchain_info() -> str:
    """Get system compiler/toolchain information."""
    if platform.system() == "Darwin":
        try:
            return subprocess.check_output(["clang", "--version"], stderr=subprocess.DEVNULL).decode().split('\n')[0]
        except (subprocess.SubprocessError, Exception): pass
    elif platform.system() == "Linux":
        try:
            return subprocess.check_output(["gcc", "--version"], stderr=subprocess.DEVNULL).decode().split('\n')[0]
        except (subprocess.SubprocessError, Exception): pass
    return "unknown"

def get_environment_tags() -> List[str]:
    """Capture environment tags (OS, Architecture, Accelerators)."""
    tags = [platform.system(), platform.machine()]
    
    # Check for MLX (Apple Silicon)
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        tags.append("AppleSilicon")
        try:
            import mlx.core
            tags.append("MLX")
        except ImportError: pass
        
    # Check for CUDA
    try:
        import torch
        if torch.cuda.is_available():
            tags.append("CUDA")
    except ImportError: pass
    
    return tags

def generate_release_snapshot(active_model: Optional[ModelManifest] = None) -> ReleaseManifest:
    """Generates a full ReleaseManifest for the current execution."""
    return ReleaseManifest(
        commit_hash=get_git_commit(),
        timestamp=datetime.now().isoformat(),
        python_version=sys.version.split(' ')[0],
        environment_tags=get_environment_tags(),
        toolchain_version=get_toolchain_info(),
        active_manifest=active_model
    )

def save_release_snapshot(manifest: ReleaseManifest, output_path: Path):
    """Saves the release manifest to a JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(manifest.model_dump_json(indent=2))


# =============================================================================
# DATA PREPROCESSORS & PARSING
# =============================================================================

def clean_json_string(text: str, compatibility_mode: bool = False) -> str:
    """Strip markdown fencing and whitespace from an LLM JSON response."""
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

    # Convert common non-JSON strings to null/valid JSON.
    cleaned = re.sub(r':\s*"null"', ': null', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r':\s*"None"', ': null', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r':\s*"nan"', ': null', cleaned, flags=re.IGNORECASE)

    return cleaned

def ultra_clean_json(text: str) -> str:
    """Aggressively strip non-printable characters to rescue malformed JSON."""
    return "".join(c for c in text if 32 <= ord(c) <= 126 or c in "\n\r\t")

def parse_llm_output_as_json(
    text: str, compatibility_mode: bool = False
) -> Dict[str, Any]:
    """Parse an LLM response string into a Python dictionary."""
    cleaned = clean_json_string(text, compatibility_mode=compatibility_mode)

    if not cleaned:
        return {
            "REPAIR_REQUIRED": True,
            "error": "Model output was empty after cleaning",
            "raw_output": text
        }

    last_exception = None

    # Stage 1: Attempt standard parse (strict)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        last_exception = exc

    # Stage 2: Attempt robust parse (non-strict control characters)
    try:
        return json.loads(cleaned, strict=False)
    except json.JSONDecodeError as exc:
        last_exception = exc

    # Stage 2.3: Balanced Brace Extraction (Robust rescue for surrounding text)
    if compatibility_mode:
        extracted = extract_json_block(text)
        if extracted:
            try:
                return json.loads(extracted, strict=False)
            except json.JSONDecodeError as exc:
                last_exception = exc

    # Stage 2.5: Markdown Code Block Extraction (Rescue for wrapped output)
    if compatibility_mode and "```" in cleaned:
        try:
            code_blocks = re.findall(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned)
            for block in reversed(code_blocks):
                try:
                    return json.loads(block, strict=False)
                except json.JSONDecodeError:
                    try:
                        b_start = block.index("{")
                        b_end = block.rindex("}") + 1
                        return json.loads(block[b_start:b_end], strict=False)
                    except (ValueError, json.JSONDecodeError):
                        continue
        except Exception:
            pass

    # Stage 2.6: Forced Brace-Bounded extraction (Rescue for reasoning prose)
    if compatibility_mode and not (cleaned.startswith("{") and cleaned.endswith("}")):
        try:
            matches = list(re.finditer(r"\{[\s\S]*\}", cleaned))
            if matches:
                for match in reversed(matches):
                    try:
                        return json.loads(match.group(), strict=False)
                    except json.JSONDecodeError:
                        continue
        except (ValueError, json.JSONDecodeError):
            pass

    # Stage 3: Attempt Ultra-Clean parse (strip junk)
    if compatibility_mode:
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

    hpc_factors = [
        "Subtractive Inhibition (SST)",
        "Divisive Inhibition (PV)",
        "Inhibition (GABA)",
        "Habituation to Sequence",
        "Synaptic Depression (Adaptation)",
        "Activity Suppression",
        "Selective Sharpening",
        "Alpha/Beta Mediated Suppression",
        "VIP-Mediated Disinhibition",
        "Precision Weighting (Gain)",
        "E/I Balance Shift",
        "Omission Response",
        "Feedforward Deviance Detection",
        "Feedforward AMPA",
        "Feedforward NMDA",
        "Feedforward Ascending Gamma",
        "Absence of Feedback Error",
        "Feedforward Non-local Supragranular Activity (L2/3)",
        "Feedforward Non-local Granular Activity (L4)",
        "Feedforward Non-local Directed Connectivity",
        "Feedforward Non-local Activation",
        "Ascending Latency Shift",
        "Feedforward Error Propagation",
        "Subcortical Feedforward Relaying",
        "Canonical Microcircuit Ubiquity",
        "Hierarchical Mechanism Invariance",
        "Hierarchical Activity Ubiquity",
        "Hierarchical CSD Ubiquity",
        "Cross-Scale Hierarchical Ubiquity",
        "Hierarchical Presence (V1-PFC)",
        "Cross-Modal Ubiquity",
        "Interspecies Hierarchical Ubiquity",
        "Temporal Stability of Ubiquity",
        "Hierarchical Order Stability",
        "Population-Wide Ubiquity",
        "State-Independent Ubiquity"
    ]

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            # Extract basic metadata robustly from the right side of the split
            name_parts = json_file.stem.split('_')
            if len(name_parts) >= 4:
                study = "_".join(name_parts[:-3])
                model = name_parts[-3]
            else:
                study = name_parts[0]
                model = name_parts[1] if len(name_parts) > 1 else "unknown"
            
            # Extract year from study name (first 4 digits)
            import re
            year_match = re.search(r'\d{4}', study)
            year = float(year_match.group()) if year_match else None
            
            # Type detection fallback
            study_type = "empirical"
            if "RaoBallard" in study or "Kiebel" in study or "Friston" in study:
                study_type = "computational"

            # Check if this is HPC glossary based on filename or metadata
            is_hpc = "HPC" in json_file.name or ("metadata" in data and "HPC" in str(data.get("metadata", {})))
            lo_data = data.get("lo_evaluations", {})
            go_data = data.get("go_evaluations", {})
            if not is_hpc and lo_data:
                if any(k in hpc_factors for k in lo_data.keys()):
                    is_hpc = True

            if is_hpc:
                # Map to canonical hpc columns
                row = {
                    "study_name": study,
                    "agent_": model,
                    "year_": year,
                    "type_": study_type
                }
                
                # Extract individual factor scores LO-F01 to LO-F36 and GO-F01 to GO-F36
                lo_vals = []
                go_vals = []
                for idx, factor in enumerate(hpc_factors):
                    f_num = f"{idx+1:02d}"
                    
                    # LO
                    val_lo = lo_data.get(factor)
                    row[f"LO-F{f_num}"] = val_lo if val_lo is not None else None
                    if val_lo is not None:
                        lo_vals.append(float(val_lo))
                        
                    # GO
                    val_go = go_data.get(factor)
                    row[f"GO-F{f_num}"] = val_go if val_go is not None else None
                    if val_go is not None:
                        go_vals.append(float(val_go))

                # Counts
                row["LO-count"] = float(len(lo_vals))
                row["GO-count"] = float(len(go_vals))

                # Helper to compute group avg/std
                def get_stats(vals, start_idx, end_idx):
                    sub_vals = []
                    for idx in range(start_idx - 1, end_idx):
                        factor = hpc_factors[idx]
                        v = vals.get(factor)
                        if v is not None:
                            sub_vals.append(float(v))
                    if not sub_vals:
                        return None, None
                    import numpy as np
                    return np.mean(sub_vals), np.std(sub_vals) if len(sub_vals) > 1 else 0.0

                # Calculate H1, H2, H3 for LO
                h1_avg, h1_std = get_stats(lo_data, 1, 12)
                h2_avg, h2_std = get_stats(lo_data, 13, 24)
                h3_avg, h3_std = get_stats(lo_data, 25, 36)
                row["LO-H1-avg"] = h1_avg
                row["LO-H1-std"] = h1_std
                row["LO-H2-avg"] = h2_avg
                row["LO-H2-std"] = h2_std
                row["LO-H3-avg"] = h3_avg
                row["LO-H3-std"] = h3_std

                # Calculate H1, H2, H3 for GO
                h1_avg_go, h1_std_go = get_stats(go_data, 1, 12)
                h2_avg_go, h2_std_go = get_stats(go_data, 13, 24)
                h3_avg_go, h3_std_go = get_stats(go_data, 25, 36)
                row["GO-H1-avg"] = h1_avg_go
                row["GO-H1-std"] = h1_std_go
                row["GO-H2-avg"] = h2_avg_go
                row["GO-H2-std"] = h2_std_go
                row["GO-H3-avg"] = h3_avg_go
                row["GO-H3-std"] = h3_std_go

                all_results.append(row)
            else:
                # Flat or non-HPC schema fallback
                if "lo_evaluations" in data and "go_evaluations" in data:
                    lo_scores = {f"lo_{k}": v for k, v in data["lo_evaluations"].items()}
                    go_scores = {f"go_{k}": v for k, v in data["go_evaluations"].items()}
                    row = {"study_name": study, "agent_": model}
                    row.update(lo_scores)
                    row.update(go_scores)
                    all_results.append(row)
                else:
                    row = {"study_name": study, "agent_": model}
                    for k, v in data.items():
                        if k not in ["study_name", "agent_", "metadata", "ReleaseManifest", "commit_hash"]:
                            row[k] = v
                    all_results.append(row)
        except Exception as e:
            logger.error(f"Error parsing score from {json_file.name}: {e}")

    if not all_results:
        return pd.DataFrame()
        
    df = pd.DataFrame(all_results)
    return df


# =============================================================================
# GLOBAL LOGGER COMPILATION
# =============================================================================

_global_log_lock = threading.Lock()

def generate_global_log(log_dir: Optional[Path] = None):
    global _global_log_lock
    if log_dir is None:
        log_dir = Path("./logs")
    else:
        log_dir = Path(log_dir)
        
    output_file = log_dir / "global_log.jsonl"
    char_limit = 20000
    
    if not log_dir.exists():
        return
        
    with _global_log_lock:
        log_files = glob.glob(str(log_dir / "*.log")) + glob.glob(str(log_dir / "*.txt"))
        log_files = [f for f in log_files if "global_log.jsonl" not in f]
        log_files.sort(key=os.path.getmtime, reverse=True)
        
        global_entries = []
        
        for log_path in log_files:
            try:
                file_size = os.path.getsize(log_path)
                with open(log_path, "r", errors="ignore") as f:
                    if file_size > char_limit:
                        f.seek(file_size - char_limit)
                    content = f.read()
                
                entry = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(log_path))),
                    "source": os.path.basename(log_path),
                    "content": content
                }
                global_entries.append(entry)
            except Exception as e:
                print(f"Error reading {log_path}: {e}")

        try:
            with open(output_file, "w") as f:
                for entry in global_entries:
                    f.write(json.dumps(entry) + "\n")
            print(f"✅ Global log generated with {len(global_entries)} sources.")
        except Exception as e:
            print(f"Error writing global log: {e}")

def estimate_tokens(text: str) -> int:
    """Estimates the number of tokens in a text string based on character length."""
    if not text:
        return 0
    return len(text) // 4

def get_available_models(engine_url: str = "http://localhost:1234") -> List[str]:
    """Fetch the list of available loaded or loadable models from the local server."""
    try:
        import requests
        url = f"{engine_url.rstrip('/')}/v1/models"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return [m["id"] for m in data.get("data", [])]
    except Exception as e:
        print(f"⚠️ Warning: failed to fetch available models from {engine_url}: {e}")
    return []

def remove_references(text: str) -> str:
    """Removes the References/Bibliography section from the extracted study text."""
    import re
    pattern = re.compile(
        r'(?i)\n(?:##?\s*)?(?:References|Bibliography|Literature\s+Cited|References\s+and\s+Notes)\b'
    )
    match = pattern.search(text)
    if match:
        return text[:match.start()].strip()
    return text

def extract_json_block(text: str) -> str:
    """Finds the first balanced curly-brace bounded JSON object in the text.
    Returns the JSON string or empty string if not found.
    """
    if not text:
        return ""
    
    # Strip <think>...</think> first
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    
    # Find the first occurrence of '{'
    start_idx = text.find("{")
    if start_idx == -1:
        return ""
        
    brace_count = 0
    in_string = False
    escape = False
    
    for i in range(start_idx, len(text)):
        char = text[i]
        
        # Track string literals to avoid counting braces inside string values
        if char == '"' and not escape:
            in_string = not in_string
            
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Found a complete balanced block
                    return text[start_idx:i+1]
        
        # Handle string character escapes
        if char == '\\' and in_string:
            escape = not escape
        else:
            escape = False
            
    return ""

def calculate_pdf_hash(file_path: str) -> str:
    """Calculate the MD5 checksum of a file."""
    import hashlib
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read in 64kb chunks
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def clean_text(text: str) -> str:
    """Cleans non-standard characters from text, mapping them to standard ASCII equivalents."""
    if not text:
        return ""
    
    char_map = {
        "ð": "(",
        "Þ": ")",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "–": "-",  # en-dash
        "—": "-",  # em-dash
        "’": "'",  # curly apostrophe
        "‘": "'",
        "”": '"',  # curly double quotes
        "“": '"',
        "…": "...", # ellipsis
        " ": " ",   # non-breaking space
    }
    
    cleaned = text
    for non_std, std in char_map.items():
        cleaned = cleaned.replace(non_std, std)
        
    return cleaned

def compress_prompt(prompt: str, max_tokens: int) -> str:
    """If prompt length exceeds max_tokens, dynamically compress sections of the prompt."""
    if not prompt:
        return ""
        
    current_tokens = estimate_tokens(prompt)
    if current_tokens <= max_tokens:
        return prompt
        
    logger.info(f"⚠️ Prompt size ({current_tokens} tokens) exceeds limit ({max_tokens}). Compressing sections...")
    
    target_sections = ["Discussion", "Methods", "Materials and Methods", "Materials & Methods"]
    
    compressed_prompt = prompt
    for section_name in target_sections:
        pattern = re.compile(
            r'(##\s*' + re.escape(section_name) + r'\b[\s\S]*?)(?=\n## |\n---|$)'
        )
        match = pattern.search(compressed_prompt)
        if match:
            section_text = match.group(1)
            lines = section_text.split("\n")
            header = lines[0]
            truncated_body = f"\n*[Section truncated to satisfy model context window limits of {max_tokens} tokens]*\n"
            replacement = header + truncated_body
            compressed_prompt = compressed_prompt.replace(section_text, replacement)
            
            if estimate_tokens(compressed_prompt) <= max_tokens:
                logger.info(f"✅ Successfully compressed prompt to {estimate_tokens(compressed_prompt)} tokens.")
                return compressed_prompt

    if estimate_tokens(compressed_prompt) > max_tokens:
        logger.warning(f"⚠️ Prompt still exceeds limit after section truncation. Truncating to {max_tokens} tokens.")
        compressed_prompt = compressed_prompt[:max_tokens * 4]
        
    return compressed_prompt

