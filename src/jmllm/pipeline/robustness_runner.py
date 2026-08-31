"""Robustness Experiment Harness for MLLM/HPC-36 Literature Scoring Pipeline.

Dedicated harness for the Scientific Reports reviewer robustness analysis.
Factorial Design: 31 papers x 3 models x 3 temperatures x 3 repeats = 837 primary cells.
"""

import os
import sys
import json
import time
import glob
import re
import hashlib
import subprocess
import requests
import concurrent.futures
import pandas as pd
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

REPO_ROOT = Path(__file__).resolve().parents[3]
PAPERS_DIR = REPO_ROOT / "content" / "markdowns"
GLOSSARY_PATH = (REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md") if (REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md").exists() else (REPO_ROOT / "src" / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md")
INSTRUCTIONS_PATH = (REPO_ROOT / "ontology" / "instructions" / "hpc_eval_prompt.md") if (REPO_ROOT / "ontology" / "instructions" / "hpc_eval_prompt.md").exists() else (REPO_ROOT / "src" / "ontology" / "instructions" / "hpc_eval_prompt.md")

EXP_DIR = REPO_ROOT / "content" / "202608_temp"
RAW_DIR = EXP_DIR / "raw"
LOGS_DIR = EXP_DIR / "logs"
CONFIG_DIR = EXP_DIR / "config"
MANIFEST_PATH = EXP_DIR / "manifest.csv"
CALLS_CSV_PATH = EXP_DIR / "calls.csv"
SCORES_CSV_PATH = EXP_DIR / "scores.csv"

# Experimental Factorial Specifications
SCIENTIFIC_MODELS = [
    "olmo-3-32b-think",
    "gemma-4-31b-it",
    "phi-4-reasoning-plus",
]

TEMPERATURES = [0.00, 0.35, 0.70]
REPEATS = [1, 2, 3]
TOP_P = 0.90
MIN_P = 0.10

# Expected Served Model Mapping Rules
DEFAULT_MODEL_MAPPING = {
    "olmo-3-32b-think": ["olmo-3-32b-think", "olmo-3-32b-think-gguf", "allenai/olmo-3-32b-think"],
    "gemma-4-31b-it": ["gemma-4-31b-it", "gemma-4-31b-it-mxfp4-mlx"],
    "phi-4-reasoning-plus": ["phi-4-reasoning-plus", "phi-4-reasoning-plus-mlx"],
}

# Parse 36 Canonical Factors from hpc-36-reference.md
def load_canonical_factors() -> List[str]:
    if not GLOSSARY_PATH.exists():
        raise FileNotFoundError(f"Glossary missing at {GLOSSARY_PATH}")
    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    factors = []
    for line in text.splitlines():
        if line.strip().startswith("|") and "Factor Name" not in line and "----" not in line and "Total" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1].isdigit():
                factors.append(parts[2])
    if len(factors) != 36:
        raise ValueError(f"Expected 36 canonical factors, parsed {len(factors)}")
    return factors

CANONICAL_FACTORS = load_canonical_factors()

def get_paper_files() -> List[Path]:
    papers = sorted(list(PAPERS_DIR.glob("*-vllm-deepread_compressed.md")))
    if not papers:
        # Fallback to uncompressed if compressed versions not found
        papers = sorted(list(PAPERS_DIR.glob("*-vllm-deepread.md")))
    return [p for p in papers if p.name != "HPC-prompt-Bastos2012.md"]

def extract_paper_id(filepath: Path) -> str:
    name = filepath.name
    name = name.replace("-vllm-deepread_compressed.md", "")
    return name.replace("-vllm-deepread.md", "")

def compute_sha256(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def compute_string_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def get_temp_code(temp: float) -> str:
    val = int(round(temp * 100))
    return f"T{val:03d}"

def get_repeat_code(repeat: int) -> str:
    return f"R{repeat:02d}"

def generate_condition_id(paper_id: str, scientific_model: str, temp: float, repeat: int) -> str:
    t_str = get_temp_code(temp)
    r_str = get_repeat_code(repeat)
    return f"{paper_id}__{scientific_model}__{t_str}__{r_str}"

def get_git_info() -> Tuple[str, str, bool]:
    try:
        branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=REPO_ROOT).decode().strip()
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT).decode().strip()
        status = subprocess.check_output(["git", "status", "--short"], cwd=REPO_ROOT).decode().strip()
        is_clean = len(status) == 0
        return branch, commit, is_clean
    except Exception:
        return "unknown", "unknown", False

# Schema Validation (Stage A - Strict)
def validate_response_schema(parsed_data: Any) -> Tuple[bool, List[str], Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    errors = []
    if not isinstance(parsed_data, dict):
        return False, ["Parsed data is not a JSON dictionary"], None, None
    
    required_top = ["lo_evaluations", "go_evaluations", "first_author", "publication_year", "study_type", "agent_name", "reasoning_log_text"]
    for field in required_top:
        if field not in parsed_data:
            errors.append(f"Missing required top-level field: '{field}'")
            
    lo_evals = parsed_data.get("lo_evaluations")
    go_evals = parsed_data.get("go_evaluations")
    
    if not isinstance(lo_evals, dict):
        errors.append("'lo_evaluations' is not a dictionary")
        lo_evals = None
    if not isinstance(go_evals, dict):
        errors.append("'go_evaluations' is not a dictionary")
        go_evals = None
        
    if lo_evals is not None:
        lo_keys = list(lo_evals.keys())
        if len(lo_keys) != 36:
            errors.append(f"'lo_evaluations' has {len(lo_keys)} keys, expected 36")
        missing_lo = set(CANONICAL_FACTORS) - set(lo_keys)
        if missing_lo:
            errors.append(f"'lo_evaluations' missing canonical factors: {sorted(list(missing_lo))}")
        extra_lo = set(lo_keys) - set(CANONICAL_FACTORS)
        if extra_lo:
            errors.append(f"'lo_evaluations' has unknown factor keys: {sorted(list(extra_lo))}")
            
        for k, v in lo_evals.items():
            if v is not None:
                if not isinstance(v, (int, float)):
                    errors.append(f"'lo_evaluations' factor '{k}' value '{v}' is not numeric or null")
                elif not (-1.0 <= float(v) <= 1.0):
                    errors.append(f"'lo_evaluations' factor '{k}' score {v} out of range [-1.0, 1.0]")

    if go_evals is not None:
        go_keys = list(go_evals.keys())
        if len(go_keys) != 36:
            errors.append(f"'go_evaluations' has {len(go_keys)} keys, expected 36")
        missing_go = set(CANONICAL_FACTORS) - set(go_keys)
        if missing_go:
            errors.append(f"'go_evaluations' missing canonical factors: {sorted(list(missing_go))}")
        extra_go = set(go_keys) - set(CANONICAL_FACTORS)
        if extra_go:
            errors.append(f"'go_evaluations' has unknown factor keys: {sorted(list(extra_go))}")
            
        for k, v in go_evals.items():
            if v is not None:
                if not isinstance(v, (int, float)):
                    errors.append(f"'go_evaluations' factor '{k}' value '{v}' is not numeric or null")
                elif not (-1.0 <= float(v) <= 1.0):
                    errors.append(f"'go_evaluations' factor '{k}' score {v} out of range [-1.0, 1.0]")
                    
    is_valid = len(errors) == 0
    return is_valid, errors, lo_evals, go_evals

# Legacy alias for test backwards compatibility
validate_response = validate_response_schema

# Stage B - Recovery Parser
def parse_and_recover_generation(
    raw_generation: str
) -> Tuple[str, str, Optional[Dict[str, Any]], Optional[Dict[str, Any]], Optional[Dict[str, Any]], List[str], str]:
    """Two-Stage Parser for LLM Generations.
    Returns:
       parse_status: "valid" | "recovered" | "unrecoverable"
       parser_method: "strict_json" | "cleaned_json" | "extracted_json_block" | "regex_fallback" | "failed"
       parsed_data: Dict or None
       lo_evaluations: Dict or None
       go_evaluations: Dict or None
       errors: List[str]
       notes: str
    """
    if not raw_generation or not raw_generation.strip():
        return "unrecoverable", "failed", None, None, None, ["Empty generation text"], "Generation text was empty"

    # 1. Try direct strict parsing
    try:
        data = json.loads(raw_generation)
        is_valid, errs, lo, go = validate_response_schema(data)
        if is_valid:
            return "valid", "strict_json", data, lo, go, [], "Schema strict valid"
    except Exception:
        pass

    # 2. Try helpers.parse_llm_output_as_json with compatibility mode
    from jmllm.util.helpers import parse_llm_output_as_json, extract_json_block
    parsed = parse_llm_output_as_json(raw_generation, compatibility_mode=True)
    if isinstance(parsed, dict) and not parsed.get("REPAIR_REQUIRED"):
        is_valid, errs, lo, go = validate_response_schema(parsed)
        if is_valid:
            return "valid", "cleaned_json", parsed, lo, go, [], "Cleaned JSON strictly valid"
        else:
            # If structure has lo/go evaluations, recover valid factor subset
            lo_raw = parsed.get("lo_evaluations")
            go_raw = parsed.get("go_evaluations")
            if isinstance(lo_raw, dict) or isinstance(go_raw, dict):
                lo_rec = {}
                go_rec = {}
                if isinstance(lo_raw, dict):
                    for factor in CANONICAL_FACTORS:
                        v = lo_raw.get(factor)
                        if v is not None and isinstance(v, (int, float)) and -1.0 <= float(v) <= 1.0:
                            lo_rec[factor] = float(v)
                        else:
                            lo_rec[factor] = None
                if isinstance(go_raw, dict):
                    for factor in CANONICAL_FACTORS:
                        v = go_raw.get(factor)
                        if v is not None and isinstance(v, (int, float)) and -1.0 <= float(v) <= 1.0:
                            go_rec[factor] = float(v)
                        else:
                            go_rec[factor] = None
                notes = f"Recovered scores from JSON structure. Strict schema errors: {'; '.join(errs)}"
                return "recovered", "extracted_json_block", parsed, lo_rec, go_rec, errs, notes

    # 3. Fallback: Extraction of json block via brace regex
    json_block = extract_json_block(raw_generation)
    if json_block:
        try:
            data = json.loads(json_block, strict=False)
            lo_raw = data.get("lo_evaluations")
            go_raw = data.get("go_evaluations")
            if isinstance(lo_raw, dict) or isinstance(go_raw, dict):
                lo_rec = {f: (float(lo_raw[f]) if isinstance(lo_raw, dict) and f in lo_raw and isinstance(lo_raw[f], (int, float)) and -1.0 <= float(lo_raw[f]) <= 1.0 else None) for f in CANONICAL_FACTORS}
                go_rec = {f: (float(go_raw[f]) if isinstance(go_raw, dict) and f in go_raw and isinstance(go_raw[f], (int, float)) and -1.0 <= float(go_raw[f]) <= 1.0 else None) for f in CANONICAL_FACTORS}
                return "recovered", "extracted_json_block", data, lo_rec, go_rec, [], "Recovered via balanced brace extraction"
        except Exception:
            pass

    # 4. Fallback: Key-Value / Numbered factor regex extraction from reasoning trace
    extracted = {}
    # Pattern A: "Factor Name" = score or "Factor Name": score
    for k, v in re.findall(r'\"([^\"]+)\"\s*(?:=|:)\s*([+-]?\d+\.?\d*|null)', raw_generation, re.IGNORECASE):
        k_clean = k.strip()
        if k_clean in CANONICAL_FACTORS and k_clean not in extracted:
            extracted[k_clean] = float(v) if v.lower() != 'null' else None

    # Pattern B: 1: Subtractive Inhibition (SST): null / "1": Factor Name: score
    for k, v in re.findall(r'\"?\d+\"?:\s*([^:\n]+?):\s*([+-]?\d+\.?\d*|null)', raw_generation, re.IGNORECASE):
        k_clean = k.strip().strip('"').strip("'")
        if k_clean in CANONICAL_FACTORS and k_clean not in extracted:
            extracted[k_clean] = float(v) if v.lower() != 'null' else None

    # Pattern C: Factor Name -> null / Factor Name: score
    for f in CANONICAL_FACTORS:
        if f not in extracted:
            m = re.search(re.escape(f) + r'\s*(?:=|:|\->)\s*([+-]?\d+\.?\d*|null)', raw_generation, re.IGNORECASE)
            if m:
                v = m.group(1)
                extracted[f] = float(v) if v.lower() != 'null' else None

    if len(extracted) >= 18:  # At least half the canonical factors recovered
        lo_rec = {f: extracted.get(f) for f in CANONICAL_FACTORS}
        go_rec = {f: extracted.get(f) for f in CANONICAL_FACTORS}
        synth_data = {
            "lo_evaluations": lo_rec,
            "go_evaluations": go_rec,
            "reasoning_log_text": "Extracted from comprehensive reasoning trace"
        }
        return "recovered", "regex_trace_extraction", synth_data, lo_rec, go_rec, [], f"Recovered {len(extracted)} factors from reasoning trace"

    return "unrecoverable", "failed", None, None, None, ["Failed all rescue parser stages"], "No valid JSON structure recovered"

# Model Server & Discovery
def query_served_models(engine_url: str = "http://localhost:1234") -> List[str]:
    try:
        url = f"{engine_url.rstrip('/')}/v1/models"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return [m["id"] for m in data.get("data", [])]
    except Exception:
        pass
    return []

def resolve_model_mapping(served_models: List[str]) -> Dict[str, Optional[str]]:
    mapping = {}
    for sc_model in SCIENTIFIC_MODELS:
        candidates = DEFAULT_MODEL_MAPPING.get(sc_model, [sc_model])
        matched = None
        for cand in candidates:
            if cand in served_models:
                matched = cand
                break
        if matched is None:
            for sm in served_models:
                if sc_model.lower() in sm.lower():
                    matched = sm
                    break
        mapping[sc_model] = matched
    return mapping

# Atomic file writer
def write_file_atomically(target_path: Path, data_str: str):
    tmp_path = target_path.with_suffix(f".tmp.{os.getpid()}_{time.time_ns()}")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(data_str)
    tmp_path.replace(target_path)

# Manifest Generation & Management
def generate_manifest(model_mapping: Dict[str, Optional[str]]) -> pd.DataFrame:
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    paper_files = get_paper_files()
    rows = []
    
    for pf in paper_files:
        paper_id = extract_paper_id(pf)
        for sc_model in SCIENTIFIC_MODELS:
            served_id = model_mapping.get(sc_model) or "UNRESOLVED"
            for temp in TEMPERATURES:
                for rep in REPEATS:
                    cid = generate_condition_id(paper_id, sc_model, temp, rep)
                    raw_file = RAW_DIR / f"{cid}.json"
                    
                    status = "PENDING"
                    attempts = 0
                    parse_status = "UNTESTED"
                    err_msg = ""
                    lat_sec = ""
                    
                    if raw_file.exists():
                        try:
                            with open(raw_file, "r", encoding="utf-8") as rf:
                                rdata = json.load(rf)
                                parse_status = rdata.get("parse_status") or rdata.get("validation_status", "UNKNOWN")
                                attempts = rdata.get("attempts", 1)
                                lat_sec = rdata.get("latency_seconds", "")
                                err_msg = "; ".join(rdata.get("parse_errors", rdata.get("validation_errors", [])))
                                if parse_status in ["valid", "VALID"]:
                                    status = "COMPLETE"
                                elif parse_status in ["recovered", "RECOVERED"]:
                                    status = "RECOVERED"
                                elif parse_status in ["unrecoverable", "INVALID", "UNRECOVERABLE"]:
                                    status = "UNRECOVERABLE"
                                else:
                                    status = "ERROR"
                        except Exception:
                            status = "ERROR"
                            
                    try:
                        rel_path = str(raw_file.relative_to(REPO_ROOT))
                    except ValueError:
                        rel_path = str(raw_file)

                    rows.append({
                        "condition_id": cid,
                        "paper_id": paper_id,
                        "scientific_model": sc_model,
                        "served_model_id": served_id,
                        "temperature": f"{temp:.2f}",
                        "top_p": f"{TOP_P:.2f}",
                        "min_p": f"{MIN_P:.2f}",
                        "repeat": rep,
                        "status": status,
                        "attempts": attempts,
                        "raw_result_path": rel_path,
                        "parse_status": parse_status,
                        "error": err_msg,
                        "latency_seconds": lat_sec,
                    })
                    
    df = pd.DataFrame(rows)
    df.to_csv(MANIFEST_PATH, index=False)
    return df

# Tabular Generators: calls.csv and scores.csv
def generate_tabular_datasets() -> Tuple[pd.DataFrame, pd.DataFrame]:
    raw_files = sorted(list(RAW_DIR.glob("*.json")))
    call_records = []
    score_records = []
    
    for rf in raw_files:
        try:
            with open(rf, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            p_stat = data.get("parse_status") or data.get("validation_status", "unknown").lower()
            if p_stat == "valid":
                is_valid = True
                is_recovered = False
            elif p_stat == "recovered":
                is_valid = False
                is_recovered = True
            else:
                is_valid = False
                is_recovered = False
                
            call_records.append({
                "condition_id": data.get("condition_id"),
                "paper_id": data.get("paper_id"),
                "scientific_model": data.get("scientific_model"),
                "served_model_id": data.get("served_model_id"),
                "temperature": data.get("temperature"),
                "top_p": data.get("top_p"),
                "min_p": data.get("min_p"),
                "repeat": data.get("repeat"),
                "concurrency": data.get("concurrency", 1),
                "http_status": data.get("http_status"),
                "latency_seconds": data.get("latency_seconds"),
                "attempts": data.get("attempts"),
                "parse_status": p_stat,
                "parser_method": data.get("parser_method", "unknown"),
                "parser_version": data.get("parser_version", "v1.0"),
                "is_valid": is_valid,
                "is_recovered": is_recovered,
                "git_commit": data.get("git_commit"),
                "request_start_timestamp": data.get("request_start_timestamp"),
                "request_end_timestamp": data.get("request_end_timestamp"),
            })
            
            lo_evals = data.get("lo_evaluations") or {}
            go_evals = data.get("go_evaluations") or {}
            
            if lo_evals or go_evals:
                for factor_name, score in lo_evals.items():
                    score_records.append({
                        "paper_id": data.get("paper_id"),
                        "scientific_model": data.get("scientific_model"),
                        "served_model_id": data.get("served_model_id"),
                        "temperature": data.get("temperature"),
                        "repeat": data.get("repeat"),
                        "context": "LO",
                        "factor": factor_name,
                        "score": score if score is not None else "",
                        "condition_id": data.get("condition_id"),
                        "parse_status": p_stat,
                        "is_recovered": is_recovered,
                        "parser_method": data.get("parser_method", "unknown"),
                    })
                    
                for factor_name, score in go_evals.items():
                    score_records.append({
                        "paper_id": data.get("paper_id"),
                        "scientific_model": data.get("scientific_model"),
                        "served_model_id": data.get("served_model_id"),
                        "temperature": data.get("temperature"),
                        "repeat": data.get("repeat"),
                        "context": "GO",
                        "factor": factor_name,
                        "score": score if score is not None else "",
                        "condition_id": data.get("condition_id"),
                        "parse_status": p_stat,
                        "is_recovered": is_recovered,
                        "parser_method": data.get("parser_method", "unknown"),
                    })
        except Exception as e:
            print(f"Error parsing raw file {rf}: {e}")
            continue

    df_calls = pd.DataFrame(call_records)
    df_calls.to_csv(CALLS_CSV_PATH, index=False)
    
    df_scores = pd.DataFrame(score_records)
    df_scores.to_csv(SCORES_CSV_PATH, index=False)
    
    print(f"Generated {CALLS_CSV_PATH.name} ({len(df_calls)} call records) and {SCORES_CSV_PATH.name} ({len(df_scores)} score records).")
    return df_calls, df_scores

# Backwards compatibility alias
def generate_long_csv() -> pd.DataFrame:
    _, df_scores = generate_tabular_datasets()
    return df_scores

# Offline Re-Parsing Engine (Zero Inference Calls)
def reparse_raw_artifacts() -> Tuple[pd.DataFrame, pd.DataFrame]:
    print("🔄 Running Offline Re-Parser on raw artifacts...")
    raw_files = sorted(list(RAW_DIR.glob("*.json")))
    reparsed_count = 0
    valid_count = 0
    recovered_count = 0
    unrecoverable_count = 0
    
    for rf in raw_files:
        with open(rf, "r", encoding="utf-8") as f:
            rec = json.load(f)
            
        raw_gen = rec.get("raw_assistant_response") or rec.get("raw_generation") or ""
        p_status, p_method, p_data, lo, go, errs, notes = parse_and_recover_generation(raw_gen)
        
        rec["parse_status"] = p_status
        rec["parser_method"] = p_method
        rec["parser_version"] = "v2.0_offline"
        rec["parsed_response"] = p_data
        rec["lo_evaluations"] = lo
        rec["go_evaluations"] = go
        rec["parse_errors"] = errs
        rec["recovery_notes"] = notes
        rec["validation_status"] = p_status.upper()
        rec["validation_errors"] = errs
        
        write_file_atomically(rf, json.dumps(rec, indent=2))
        reparsed_count += 1
        if p_status == "valid":
            valid_count += 1
        elif p_status == "recovered":
            recovered_count += 1
        else:
            unrecoverable_count += 1
            
    print(f"✅ Offline Re-parsing complete across {reparsed_count} artifacts.")
    print(f"   Valid: {valid_count} | Recovered: {recovered_count} | Unrecoverable: {unrecoverable_count}")
    return generate_tabular_datasets()

# Preflight Check Command
def run_preflight(engine_url: str = "http://localhost:1234") -> bool:
    print("=" * 65)
    print("      MLLM REVIEWER ROBUSTNESS EXPERIMENT — PREFLIGHT")
    print("=" * 65)
    
    branch, commit, is_clean = get_git_info()
    print(f"Git Branch         : {branch}")
    print(f"Git Commit         : {commit}")
    print(f"Working Tree Clean : {'YES' if is_clean else 'NO'}")
    
    paper_files = get_paper_files()
    print(f"\nPaper Inputs Count : {len(paper_files)} / 31 expected")
    if len(paper_files) != 31:
        print(f"❌ ERROR: Expected 31 paper files, found {len(paper_files)}")
        return False
        
    glossary_sha = compute_sha256(GLOSSARY_PATH)
    instructions_sha = compute_sha256(INSTRUCTIONS_PATH)
    print(f"Glossary SHA-256   : {glossary_sha[:16]}...")
    print(f"Instruction SHA-256: {instructions_sha[:16]}...")
    
    served_models = query_served_models(engine_url)
    print(f"\nLM Studio Endpoint : {engine_url}")
    print(f"LM Studio Reachable: {'YES' if served_models else 'NO (Unreachable)'}")
    print(f"Discovered Models  : {served_models}")
    
    mapping = resolve_model_mapping(served_models)
    print("\nScientific -> Served Model Mapping:")
    all_resolved = True
    for sc_model, served_id in mapping.items():
        if served_id:
            print(f"  ✅ {sc_model:<30} -> {served_id}")
        else:
            print(f"  ❌ {sc_model:<30} -> UNRESOLVED / MISSING")
            all_resolved = False
            
    print(f"\nSampler Settings   : top_p = {TOP_P:.2f}, min_p = {MIN_P:.2f}")
    print(f"Temperatures       : {TEMPERATURES}")
    print(f"Repeats            : {REPEATS}")
    
    manifest_df = generate_manifest(mapping)
    total_cells = len(manifest_df)
    unique_cids = manifest_df["condition_id"].nunique()
    print(f"\nExpected Total Cells: {total_cells} (Unique condition IDs: {unique_cids})")
    
    if total_cells != 837 or unique_cids != 837:
        print("❌ ERROR: Cell count does not equal 837 unique cells!")
        return False
        
    if not all_resolved:
        print("\n⚠️ PREFLIGHT WARNING: One or more models are not currently served in LM Studio.")
        print("   Ensure models are loaded prior to launching inference.")
        return False
        
    print("\n✅ PREFLIGHT PASSED: Environment ready for inference.")
    return True

# Graceful Stop / Signal Handling State
GLOBAL_STOP_REQUESTED = False
GLOBAL_STOP_COUNTER = 0

def setup_signal_handlers():
    import signal
    def handle_sigint(sig, frame):
        global GLOBAL_STOP_REQUESTED, GLOBAL_STOP_COUNTER
        GLOBAL_STOP_COUNTER += 1
        if GLOBAL_STOP_COUNTER == 1:
            GLOBAL_STOP_REQUESTED = True
            print("\n\n⚠️ SIGINT received (Ctrl-C once). Gracefully stopping sweep after in-flight calls complete...")
            print("   Press Ctrl-C again to force immediate termination.")
        else:
            print("\n\n💥 SIGINT received twice (Ctrl-C twice). Terminating immediately!")
            sys.exit(130)
            
    signal.signal(signal.SIGINT, handle_sigint)
    try:
        signal.signal(signal.SIGTERM, handle_sigint)
    except Exception:
        pass

def select_median_length_paper() -> Path:
    paper_files = get_paper_files()
    paper_lengths = [(pf, len(pf.read_text(encoding="utf-8"))) for pf in paper_files]
    paper_lengths.sort(key=lambda x: x[1])
    median_idx = len(paper_lengths) // 2
    return paper_lengths[median_idx][0]

def select_max_length_paper() -> Path:
    paper_files = get_paper_files()
    paper_lengths = [(pf, len(pf.read_text(encoding="utf-8"))) for pf in paper_files]
    paper_lengths.sort(key=lambda x: x[1])
    return paper_lengths[-1][0]

# Single Cell Inference Execution Helper
def execute_cell_inference(
    paper_path: Path,
    scientific_model: str,
    served_model_id: str,
    temp: float,
    repeat: int,
    concurrency: int = 1,
    engine_url: str = "http://localhost:1234",
    max_retries: int = 3,
) -> Dict[str, Any]:
    paper_id = extract_paper_id(paper_path)
    cid = generate_condition_id(paper_id, scientific_model, temp, repeat)
    raw_file = RAW_DIR / f"{cid}.json"
    
    # Resumability check
    if raw_file.exists():
        try:
            with open(raw_file, "r", encoding="utf-8") as rf:
                existing = json.load(rf)
                if existing.get("parse_status") in ["valid", "recovered"] or existing.get("validation_status") == "VALID":
                    return existing
        except Exception:
            pass
    
    with open(paper_path, "r", encoding="utf-8") as f:
        study_text = f.read()
    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        glossary_text = f.read()
    with open(INSTRUCTIONS_PATH, "r", encoding="utf-8") as f:
        instructions_text = f.read()
        
    paper_sha = compute_sha256(paper_path)
    glossary_sha = compute_sha256(GLOSSARY_PATH)
    instruction_sha = compute_sha256(INSTRUCTIONS_PATH)
    _, git_commit, _ = get_git_info()
    
    full_prompt = (
        f"{instructions_text}\n\n"
        f"**GLOSSARY:**\n{glossary_text}\n\n"
        f"**DOCUMENT:**\n{study_text}\n\n"
        f"**TASK REINFORCEMENT & OUTPUT FORMAT:**\n"
        f"Based on the document and glossary above, evaluate all 36 canonical HPC factors for both Local Oddball (LO) and Global Oddball (GO).\n"
        f"- Use scores in [-1.0, 1.0], or null if unaddressed.\n"
        f"- Output exactly one valid JSON object with keys: "
        f"\"lo_evaluations\", \"go_evaluations\", \"first_author\", \"publication_year\", \"study_type\", \"agent_name\", \"reasoning_log_text\".\n\n"
        f"**FILL IN THE SCORES:**\n\nReturn directly the single valid JSON object with the factor scores and concise reasoning_log_text. Do not output unneeded conversational preamble."
    )
    prompt_sha = compute_string_sha256(full_prompt)
    
    # Dynamic max_tokens budgeting: guarantee prompt_tokens + max_tokens <= 32,000 (safe headroom within 32,768)
    estimated_prompt_tokens = len(full_prompt) // 4
    dynamic_max_tokens = max(2048, min(8192, 32000 - estimated_prompt_tokens))
    
    headers = {"Content-Type": "application/json", "Authorization": "Bearer mlx-server"}
    url = f"{engine_url.rstrip('/')}/v1/chat/completions"
    
    payload = {
        "model": served_model_id,
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": temp,
        "top_p": TOP_P,
        "min_p": MIN_P,
        "max_tokens": dynamic_max_tokens,
    }
    
    attempts = 0
    raw_assistant_response = ""
    http_status = None
    latency = 0.0
    token_usage = None
    raw_http_payload = None
    prompt_tokens = 0
    completion_tokens = 0
    tokens_per_second = 0.0
    
    for attempt in range(1, max_retries + 1):
        attempts = attempt
        start_monotonic = time.monotonic()
        start_time = time.time()
        start_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start_time))
        
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=1800)
            end_monotonic = time.monotonic()
            end_time = time.time()
            end_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(end_time))
            latency = round(end_monotonic - start_monotonic, 3)
            http_status = resp.status_code
            
            if resp.status_code == 200:
                res_json = resp.json()
                raw_http_payload = res_json
                choices = res_json.get("choices", [])
                if choices:
                    msg = choices[0].get("message", {})
                    raw_assistant_response = msg.get("content") or choices[0].get("text") or ""
                    raw_reasoning_content = msg.get("reasoning_content") or ""
                token_usage = res_json.get("usage") or {}
                prompt_tokens = token_usage.get("prompt_tokens") or (len(full_prompt) // 4)
                completion_tokens = token_usage.get("completion_tokens") or (len(raw_assistant_response) // 4)
                if latency > 0 and completion_tokens > 0:
                    tokens_per_second = round(completion_tokens / latency, 2)
                break
            else:
                raw_assistant_response = f"HTTP Error {resp.status_code}: {resp.text}"
        except Exception as e:
            end_monotonic = time.monotonic()
            end_time = time.time()
            end_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(end_time))
            latency = round(end_monotonic - start_monotonic, 3)
            raw_assistant_response = f"Network Exception: {str(e)}"
            
        time.sleep(2 ** (attempt - 1))

    # Stage A / Stage B Parsing
    p_status, p_method, p_data, lo_evals, go_evals, parse_errors, notes = parse_and_recover_generation(raw_assistant_response)
    
    reasoning_log = ""
    if p_data and isinstance(p_data, dict):
        reasoning_log = p_data.get("reasoning_log_text", "")
        
    result_record = {
        "condition_id": cid,
        "paper_id": paper_id,
        "input_filename": paper_path.name,
        "input_sha256": paper_sha,
        "scientific_model": scientific_model,
        "served_model_id": served_model_id,
        "temperature": temp,
        "top_p": TOP_P,
        "min_p": MIN_P,
        "repeat": repeat,
        "concurrency": concurrency,
        "prompt_sha256": prompt_sha,
        "glossary_sha256": glossary_sha,
        "instruction_sha256": instruction_sha,
        "git_commit": git_commit,
        "started_at": start_ts if 'start_ts' in locals() else "",
        "finished_at": end_ts if 'end_ts' in locals() else "",
        "latency_s": latency,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "tokens_per_second": tokens_per_second,
        "http_status": http_status,
        "attempts": attempts,
        "token_usage": token_usage,
        "raw_assistant_response": raw_assistant_response,
        "raw_reasoning_content": raw_reasoning_content if 'raw_reasoning_content' in locals() else "",
        "raw_http_payload": raw_http_payload,
        "parse_status": p_status,
        "parser_method": p_method,
        "parser_version": "v1.0",
        "parsed_response": p_data,
        "parse_errors": parse_errors,
        "recovery_notes": notes,
        "validation_status": p_status.upper(),
        "validation_errors": parse_errors,
        "lo_evaluations": lo_evals,
        "go_evaluations": go_evals,
        "reasoning_log_text": reasoning_log,
    }
    
    # Write RAW Artifact ATOMICALLY before returning/marking complete
    write_file_atomically(raw_file, json.dumps(result_record, indent=2))
    return result_record

# Model Lifecycle Helper
def ensure_model_loaded(served_model_id: str, concurrency: int = 1, context_length: int = 32768, manage_models: bool = True):
    if not manage_models:
        print(f"\n🔄 Using pre-loaded model on server: {served_model_id}")
        return
    print(f"\n🔄 Ensuring resident model is loaded in LM Studio: {served_model_id} (context: {context_length}, parallel: {concurrency})")
    subprocess.run(["lms", "unload", "--all"], capture_output=True)
    res = subprocess.run(
        ["lms", "load", served_model_id, "--context-length", str(context_length), "--parallel", str(concurrency), "-y"],
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        print(f"⚠️ Warning loading {served_model_id}: {res.stderr or res.stdout}")
    else:
        print(f"✅ Resident model {served_model_id} loaded successfully (context: {context_length}, parallel: {concurrency}).")

def unload_all_models(manage_models: bool = True):
    if not manage_models:
        return
    print("\n🧹 Unloading all resident models from LM Studio memory...")
    subprocess.run(["lms", "unload", "--all"], capture_output=True)

def print_block_telemetry(
    scientific_model: str,
    temperature: float,
    block_completed: int,
    block_total: int,
    active_count: int,
    sweep_completed: int,
    sweep_total: int,
    latencies: List[float],
    block_start_mono: float,
):
    import numpy as np
    remaining = block_total - block_completed
    p50 = float(np.median(latencies)) if latencies else 0.0
    p90 = float(np.percentile(latencies, 90)) if latencies else 0.0
    
    elapsed_sec = time.monotonic() - block_start_mono
    evals_per_sec = (block_completed / elapsed_sec) if elapsed_sec > 0 else 0.0
    
    block_eta_sec = (remaining / evals_per_sec) if evals_per_sec > 0 else 0.0
    sweep_eta_sec = ((sweep_total - sweep_completed) / evals_per_sec) if evals_per_sec > 0 else 0.0
    
    b_eta_str = time.strftime("%Hh %Mm %Ss", time.gmtime(block_eta_sec))
    s_eta_str = time.strftime("%Hh %Mm %Ss", time.gmtime(sweep_eta_sec))
    
    print(
        f"[{scientific_model} | T={temperature:.2f}] "
        f"completed: {block_completed}/{block_total} | active: {active_count} | remaining: {remaining} | "
        f"p50: {p50:.1f}s | p90: {p90:.1f}s | throughput: {evals_per_sec:.3f} eval/s | "
        f"block ETA: {b_eta_str} | sweep: {sweep_completed}/{sweep_total} | sweep ETA: {s_eta_str}"
    )

# Concurrent Temperature Block Execution Engine with Bounded Executor Submission
def run_temperature_block(
    scientific_model: str,
    served_model_id: str,
    temperature: float,
    concurrency: int = 1,
    engine_url: str = "http://localhost:1234",
    sweep_completed_counter: int = 0,
    sweep_total: int = 837,
) -> Tuple[List[Dict[str, Any]], int]:
    global GLOBAL_STOP_REQUESTED
    print(f"\n--- Starting Block: Model={scientific_model} | Temperature={temperature:.2f} | Concurrency={concurrency} ---")
    paper_files = get_paper_files()
    
    jobs = []
    for pf in paper_files:
        for rep in REPEATS:
            jobs.append((pf, scientific_model, served_model_id, temperature, rep, concurrency, engine_url))

    # Filter out already complete jobs
    pending_jobs = []
    already_complete = []
    for job in jobs:
        pf, sc_m, s_id, t, r, c, url = job
        paper_id = extract_paper_id(pf)
        cid = generate_condition_id(paper_id, sc_m, t, r)
        raw_file = RAW_DIR / f"{cid}.json"
        if raw_file.exists():
            try:
                with open(raw_file, "r", encoding="utf-8") as rf:
                    existing = json.load(rf)
                    if existing.get("parse_status") in ["valid", "recovered"] or existing.get("validation_status") == "VALID":
                        already_complete.append(existing)
                        continue
            except Exception:
                pass
        pending_jobs.append(job)

    results = list(already_complete)
    block_completed = len(already_complete)
    sweep_completed = sweep_completed_counter + block_completed
    latencies = [r.get("latency_s", r.get("latency_seconds", 0.0)) for r in already_complete if r.get("latency_s") or r.get("latency_seconds")]
    
    block_start_mono = time.monotonic()
    
    if pending_jobs and not GLOBAL_STOP_REQUESTED:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            active_futures: Dict[concurrent.futures.Future, Tuple] = {}
            job_iter = iter(pending_jobs)
            
            # Initial bounded submission up to concurrency limit C
            for _ in range(min(concurrency, len(pending_jobs))):
                if GLOBAL_STOP_REQUESTED:
                    break
                job = next(job_iter)
                fut = executor.submit(execute_cell_inference, *job)
                active_futures[fut] = job
                
            while active_futures:
                done_set, _ = concurrent.futures.wait(
                    active_futures.keys(), return_when=concurrent.futures.FIRST_COMPLETED
                )
                for fut in done_set:
                    del active_futures[fut]
                    try:
                        res = fut.result()
                        results.append(res)
                        block_completed += 1
                        sweep_completed += 1
                        if res.get("latency_s"):
                            latencies.append(res["latency_s"])
                        print_block_telemetry(
                            scientific_model, temperature, block_completed, len(jobs),
                            len(active_futures), sweep_completed, sweep_total, latencies, block_start_mono
                        )
                    except Exception as exc:
                        print(f"  [EXCEPTION] Job failed: {exc}")
                        
                    # Submit next job only if stop is not requested
                    if not GLOBAL_STOP_REQUESTED:
                        try:
                            next_job = next(job_iter)
                            new_fut = executor.submit(execute_cell_inference, *next_job)
                            active_futures[new_fut] = next_job
                        except StopIteration:
                            pass
                            
    return results, sweep_completed

# Production Sweep Topology Implementation
def run_full_production_sweep(
    concurrency: int = 1,
    target_models: Optional[List[str]] = None,
    engine_url: str = "http://localhost:1234",
    manage_models: bool = True
) -> bool:
    global GLOBAL_STOP_REQUESTED
    setup_signal_handlers()
    
    active_models = target_models if target_models else SCIENTIFIC_MODELS
    total_expected = len(get_paper_files()) * len(active_models) * len(TEMPERATURES) * len(REPEATS)
    
    print("=" * 65)
    print("   FULL PRODUCTION EXPERIMENT SWEEP — EXPLICIT TOPOLOGY")
    print(f"   Target Models: {active_models}")
    print("   Topology: [ Model -> Temperature Block -> Concurrent Jobs ]")
    print(f"   Concurrency (Throughput Setting C) = {concurrency}")
    print(f"   Planned Primary Evaluations = {total_expected}")
    print("=" * 65)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    
    missing = [m for m in active_models if not mapping.get(m)]
    if missing:
        print(f"❌ SWEEP ABORTED: Missing served model mappings for {missing}")
        return False

    sweep_completed_counter = 0
    for sc_model in active_models:
        if GLOBAL_STOP_REQUESTED:
            break
        served_id = mapping[sc_model]
        ensure_model_loaded(served_id, concurrency=concurrency, manage_models=manage_models)
        
        for temp in TEMPERATURES:
            if GLOBAL_STOP_REQUESTED:
                break
            block_results, sweep_completed_counter = run_temperature_block(
                scientific_model=sc_model,
                served_model_id=served_id,
                temperature=temp,
                concurrency=concurrency,
                engine_url=engine_url,
                sweep_completed_counter=sweep_completed_counter,
                sweep_total=total_expected,
            )
            
        unload_all_models(manage_models=manage_models)

    generate_manifest(mapping)
    generate_tabular_datasets()
    
    if GLOBAL_STOP_REQUESTED:
        print("\n" + "=" * 65)
        print("⚠️ SWEEP GRACEFULLY STOPPED BY USER. State safely persisted. Resume anytime.")
        print("=" * 65)
        return False

    print("\n" + "=" * 65)
    print(f"PRODUCTION EXPERIMENT SWEEP COMPLETE ({sweep_completed_counter} calls processed).")
    print("=" * 65)
    return True

# Timing & Resumability Benchmark
def run_timing_benchmark(
    concurrency: int = 1,
    include_largest_paper: bool = True,
    engine_url: str = "http://localhost:1234",
) -> bool:
    import numpy as np
    print("=" * 65)
    print("      TIMING & THROUGHPUT BENCHMARK (3-6 REPRESENTATIVE CALLS)")
    print("=" * 65)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    
    median_paper = select_median_length_paper()
    max_paper = select_max_length_paper()
    
    benchmark_papers = [median_paper]
    if include_largest_paper:
        benchmark_papers.append(max_paper)
        
    print(f"Median Paper Selected: {median_paper.name} ({len(median_paper.read_text(encoding='utf-8'))} bytes)")
    if include_largest_paper:
        print(f"Max Paper Selected   : {max_paper.name} ({len(max_paper.read_text(encoding='utf-8'))} bytes)")
    print(f"Concurrency Setting C: {concurrency}")
    print("-" * 65)

    benchmark_records = []
    
    for sc_model in SCIENTIFIC_MODELS:
        served_id = mapping[sc_model]
        ensure_model_loaded(served_id, concurrency=concurrency)
        
        for paper in benchmark_papers:
            print(f"\n⏱️ Benchmarking Model={sc_model} | Paper={paper.name} | Temp=0.35 | Rep=1...")
            start_mono = time.monotonic()
            rec = execute_cell_inference(
                paper_path=paper,
                scientific_model=sc_model,
                served_model_id=served_id,
                temp=0.35,
                repeat=1,
                concurrency=concurrency,
                engine_url=engine_url,
            )
            wall_sec = round(time.monotonic() - start_mono, 3)
            rec["wall_clock_s"] = wall_sec
            benchmark_records.append(rec)
            print(f"   Finished in {wall_sec}s | Tokens/s: {rec.get('tokens_per_second', 0.0)} | Completion Tokens: {rec.get('completion_tokens', 0)}")
            
        unload_all_models()

    # Telemetry Summary & ETAs
    print("\n" + "=" * 65)
    print("               BENCHMARK RESULTS & SWEEP ETA ESTIMATES")
    print("=" * 65)
    
    latencies = [r["latency_s"] for r in benchmark_records]
    p50 = float(np.median(latencies))
    p90 = float(np.percentile(latencies, 90))
    pmax = float(np.max(latencies))
    
    optimistic_sweep_hrs = round((837 * p50) / (3600 * max(1, concurrency)), 2)
    p90_sweep_hrs = round((837 * p90) / (3600 * max(1, concurrency)), 2)
    conservative_sweep_hrs = round((837 * pmax) / (3600 * max(1, concurrency)), 2)
    
    print(f"Observed Latencies : Median P50 = {p50:.1f}s | P90 = {p90:.1f}s | Max = {pmax:.1f}s")
    print(f"Optimistic Sweep ETA (P50, C={concurrency}): ~{optimistic_sweep_hrs} hours")
    print(f"P90 Sweep ETA        (P90, C={concurrency}): ~{p90_sweep_hrs} hours")
    print(f"Conservative ETA     (Max, C={concurrency}): ~{conservative_sweep_hrs} hours")
    print("=" * 65)
    return True

# Stop / Resume Fault Test
def run_fault_test(engine_url: str = "http://localhost:1234") -> bool:
    print("=" * 65)
    print("      RESUMABILITY & STOP/RESUME FAULT TEST")
    print("=" * 65)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    sc_model = SCIENTIFIC_MODELS[0]
    served_id = mapping[sc_model]
    
    ensure_model_loaded(served_id, concurrency=2)
    paper_files = get_paper_files()[:2]
    
    print(f"\n1. Executing 2 initial cells for model {sc_model}...")
    for pf in paper_files:
        execute_cell_inference(pf, sc_model, served_id, 0.00, 1, concurrency=2, engine_url=engine_url)
        
    manifest_df1 = generate_manifest(mapping)
    completed_cids1 = set(manifest_df1[manifest_df1["status"] == "COMPLETE"]["condition_id"].tolist())
    print(f"   Completed Condition IDs: {completed_cids1}")
    
    print("\n2. Simulating resume call (re-running block with same paper files)...")
    start_mono = time.monotonic()
    for pf in paper_files:
        execute_cell_inference(pf, sc_model, served_id, 0.00, 1, concurrency=2, engine_url=engine_url)
    duration = time.monotonic() - start_mono
    
    print(f"   Resume execution completed in {duration:.3f}s (should be near 0.0s due to cached skipping).")
    
    manifest_df2 = generate_manifest(mapping)
    completed_cids2 = set(manifest_df2[manifest_df2["status"] == "COMPLETE"]["condition_id"].tolist())
    
    assert completed_cids1 == completed_cids2
    assert duration < 1.0, "Resume took longer than expected; completed cells were re-executed!"
    
    unload_all_models()
    print("\n✅ FAULT TEST PASSED: Completed conditions were durably preserved and skipped upon resume.")
    return True

# Concurrency Scaling Benchmark (C=1 -> C=2 -> C=4)
def run_concurrency_scaling_benchmark(engine_url: str = "http://localhost:1234") -> bool:
    import numpy as np
    print("=" * 80)
    print("      CONCURRENCY SCALING BENCHMARK (C ∈ {1, 2, 4})")
    print("=" * 80)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    median_paper = select_median_length_paper()
    print(f"Representative Paper: {median_paper.name} ({len(median_paper.read_text(encoding='utf-8'))} bytes)")
    print("-" * 80)

    concurrencies = [1, 2, 4]
    scaling_results = []

    for sc_model in SCIENTIFIC_MODELS:
        served_id = mapping[sc_model]
        r1_rate = None
        
        for C in concurrencies:
            ensure_model_loaded(served_id, concurrency=C)
            print(f"\n🚀 Benchmarking Model={sc_model} | Concurrency C={C} | Paper={median_paper.name}...")
            
            # Execute C concurrent calls of the representative workload
            start_wall = time.monotonic()
            
            jobs = [(median_paper, sc_model, served_id, 0.35, rep, C, engine_url) for rep in range(1, C + 1)]
            call_results = []
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=C) as executor:
                futures = [executor.submit(execute_cell_inference, *j) for j in jobs]
                for fut in concurrent.futures.as_completed(futures):
                    try:
                        res = fut.result()
                        call_results.append(res)
                    except Exception as e:
                        print(f"  [ERROR] Call failed: {e}")
                        
            wall_time = time.monotonic() - start_wall
            completed_count = len(call_results)
            
            # Compute R(C) = completed_evals / wall_time_hrs
            wall_hrs = wall_time / 3600.0
            r_c = completed_count / wall_hrs if wall_hrs > 0 else 0.0
            
            if C == 1:
                r1_rate = r_c
                eta_c = 1.0
            else:
                eta_c = round(r_c / (C * r1_rate), 3) if (r1_rate and r1_rate > 0) else 0.0

            latencies = [r["latency_s"] for r in call_results if "latency_s" in r]
            p50_lat = float(np.median(latencies)) if latencies else 0.0
            p90_lat = float(np.percentile(latencies, 90)) if latencies else p50_lat
            
            total_tokens = sum([r.get("completion_tokens", 0) for r in call_results])
            tok_per_sec = round(total_tokens / wall_time, 2) if wall_time > 0 else 0.0
            
            # Projected 837 sweep hours = 837 / R(C)
            projected_sweep_hrs = round(837.0 / r_c, 2) if r_c > 0 else 0.0
            
            scaling_results.append({
                "model": sc_model,
                "C": C,
                "completed": completed_count,
                "wall_time_s": round(wall_time, 2),
                "p50_latency_s": round(p50_lat, 1),
                "p90_latency_s": round(p90_lat, 1),
                "eval_per_hr": round(r_c, 2),
                "tok_per_sec": tok_per_sec,
                "efficiency_eta": eta_c,
                "projected_sweep_hrs": projected_sweep_hrs,
            })
            
            print(f"   [C={C}] Wall: {wall_time:.1f}s | R(C): {r_c:.2f} eval/hr | Tok/s: {tok_per_sec} | Eff η(C): {eta_c} | Est Sweep: {projected_sweep_hrs} hrs")
            
        unload_all_models()

    # Format Scaling Summary Table
    print("\n" + "=" * 95)
    print("                     CONCURRENCY SCALING BENCHMARK SUMMARY TABLE")
    print("=" * 95)
    print(f"{'Model':<22} | {'C':<3} | {'P50 (s)':<8} | {'P90 (s)':<8} | {'Eval/Hr':<8} | {'Tok/s':<7} | {'Efficiency η(C)':<15} | {'Est Sweep (hrs)':<15}")
    print("-" * 95)
    for row in scaling_results:
        print(
            f"{row['model']:<22} | {row['C']:<3} | {row['p50_latency_s']:<8.1f} | {row['p90_latency_s']:<8.1f} | "
            f"{row['eval_per_hr']:<8.2f} | {row['tok_per_sec']:<7.2f} | {row['efficiency_eta']:<15.3f} | {row['projected_sweep_hrs']:<15.2f}"
        )
    print("=" * 95)
    return True

# Smoke Test (9 calls) using resident topology
def run_smoke_test(engine_url: str = "http://localhost:1234") -> bool:
    print("=" * 65)
    print("      MLLM REVIEWER ROBUSTNESS EXPERIMENT — 9-CALL SMOKE TEST")
    print("=" * 65)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    
    missing = [m for m, sm in mapping.items() if not sm]
    if missing:
        print(f"❌ SMOKE TEST ABORTED: Missing served models for {missing}")
        return False
        
    paper_files = get_paper_files()
    if not paper_files:
        print("❌ SMOKE TEST ABORTED: No paper files found.")
        return False
        
    target_paper = paper_files[0]
    paper_id = extract_paper_id(target_paper)
    print(f"Target Paper       : {target_paper.name} ({paper_id})")
    print(f"Models (3)         : {SCIENTIFIC_MODELS}")
    print(f"Temperatures (3)   : {TEMPERATURES}")
    print("Repeat             : 1")
    print("Total Smoke Calls  : 9")
    print("-" * 65)
    
    executed = 0
    valid_count = 0
    
    for sc_model in SCIENTIFIC_MODELS:
        served_id = mapping[sc_model]
        ensure_model_loaded(served_id, concurrency=1)
        for temp in TEMPERATURES:
            cid = generate_condition_id(paper_id, sc_model, temp, 1)
            print(f"\n🚀 Executing Call {executed+1}/9: {cid}")
            rec = execute_cell_inference(target_paper, sc_model, served_id, temp, 1, concurrency=1, engine_url=engine_url)
            executed += 1
            p_stat = rec["parse_status"]
            print(f"   Status: {p_stat} | Method: {rec['parser_method']} | Latency: {rec['latency_seconds'] if 'latency_seconds' in rec else rec.get('latency_s')}s")
            if p_stat in ["valid", "recovered"]:
                valid_count += 1
            else:
                print(f"   Errors: {rec['parse_errors']}")
        unload_all_models()
                
    generate_manifest(mapping)
    generate_tabular_datasets()
    
    print("\n" + "=" * 65)
    print(f"SMOKE TEST COMPLETE: {valid_count}/9 calls marked valid/recovered.")
    print("=" * 65)
    return valid_count == 9

# Main CLI Entry Point
def main():
    import argparse
    parser = argparse.ArgumentParser(description="MLLM Reviewer Robustness Experiment Harness")
    parser.add_argument("--preflight", action="store_true", help="Run preflight diagnostics and exit")
    parser.add_argument("--test", action="store_true", help="Run unit test suite")
    parser.add_argument("--timing-benchmark", action="store_true", help="Run timing & throughput benchmark")
    parser.add_argument("--concurrency-benchmark", action="store_true", help="Run C=1 -> C=2 -> C=4 concurrency scaling benchmark")
    parser.add_argument("--fault-test", action="store_true", help="Run stop/resume fault test")
    parser.add_argument("--smoke-test", action="store_true", help="Run 9-call smoke test")
    parser.add_argument("--full-experiment", action="store_true", help="Run full 837-call experiment")
    parser.add_argument("--concurrency", type=int, default=1, help="Throughput concurrency setting (C)")
    parser.add_argument("--model", type=str, default=None, help="Target scientific model name (e.g. gemma-4-31b-it)")
    parser.add_argument("--reparse-offline", action="store_true", help="Run offline re-parser on raw artifacts without LLM calls")
    parser.add_argument("--confirm-full-run", action="store_true", help="Required confirmation flag for full experiment")
    parser.add_argument("--generate-csv", action="store_true", help="Compile calls.csv and scores.csv from raw outputs")
    parser.add_argument("--engine-url", type=str, default="http://localhost:1234", help="LM Studio server base URL")
    parser.add_argument("--no-manage-models", action="store_true", help="Do not unload/load models via local CLI (for remote servers)")
    
    args = parser.parse_args()
    
    if args.preflight:
        success = run_preflight(args.engine_url)
        sys.exit(0 if success else 1)
    elif args.test:
        print("Running pytest on test_robustness_runner.py...")
        res = subprocess.run([sys.executable, "-m", "pytest", str(REPO_ROOT / "tests" / "test_robustness_runner.py")])
        sys.exit(res.returncode)
    elif args.timing_benchmark:
        run_timing_benchmark(concurrency=args.concurrency, engine_url=args.engine_url)
        sys.exit(0)
    elif args.concurrency_benchmark:
        run_concurrency_scaling_benchmark(engine_url=args.engine_url)
        sys.exit(0)
    elif args.fault_test:
        run_fault_test(engine_url=args.engine_url)
        sys.exit(0)
    elif args.reparse_offline:
        reparse_raw_artifacts()
        sys.exit(0)
    elif args.generate_csv:
        generate_tabular_datasets()
        sys.exit(0)
    elif args.smoke_test:
        print("Smoke test mode selected.")
        success = run_smoke_test(args.engine_url)
        sys.exit(0 if success else 1)
    elif args.full_experiment:
        if not args.confirm_full_run:
            print("❌ Full experiment requires --confirm-full-run flag.")
            sys.exit(1)
        target_m = [args.model] if args.model else None
        success = run_full_production_sweep(
            concurrency=args.concurrency,
            target_models=target_m,
            engine_url=args.engine_url,
            manage_models=(not args.no_manage_models)
        )
        sys.exit(0 if success else 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
