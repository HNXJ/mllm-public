"""Robustness Experiment Harness for MLLM/HPC-36 Literature Scoring Pipeline.

Dedicated harness for the Scientific Reports reviewer robustness analysis.
Factorial Design: 31 papers x 3 models x 3 temperatures x 3 repeats = 837 cells.
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
import pandas as pd
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

REPO_ROOT = Path(__file__).resolve().parents[3]
PAPERS_DIR = REPO_ROOT / "content" / "markdowns"
GLOSSARY_PATH = REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md"
INSTRUCTIONS_PATH = REPO_ROOT / "ontology" / "instructions" / "hpc_eval_prompt.md"

EXP_DIR = REPO_ROOT / "content" / "reviewer_robustness_2026"
RAW_DIR = EXP_DIR / "raw"
LOGS_DIR = EXP_DIR / "logs"
CONFIG_DIR = EXP_DIR / "config"
MANIFEST_PATH = EXP_DIR / "manifest.csv"
SCORES_LONG_PATH = EXP_DIR / "scores_long.csv"

# Experimental Factorial Specifications
SCIENTIFIC_MODELS = [
    "olmo-3-32b-think",
    "gemma-4-31b-it",
    "mistral-nemo-12b-thinking",
]

TEMPERATURES = [0.00, 0.35, 0.70]
REPEATS = [1, 2, 3]
TOP_P = 0.90
MIN_P = 0.10

# Expected Served Model Mapping Rules
DEFAULT_MODEL_MAPPING = {
    "olmo-3-32b-think": ["olmo-3-32b-think-mlx", "olmo-3-32b-think"],
    "gemma-4-31b-it": ["gemma-4-31b-it", "gemma-4-31b-it-mxfp4-mlx"],
    "mistral-nemo-12b-thinking": ["mistral-nemo-12b-thinking-mlx", "mistral-nemo-12b-thinking"],
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
    papers = sorted(list(PAPERS_DIR.glob("*-vllm-deepread.md")))
    return [p for p in papers if p.name != "HPC-prompt-Bastos2012.md"]

def extract_paper_id(filepath: Path) -> str:
    name = filepath.name
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

# Response Validation Function
def validate_response(parsed_data: Any) -> Tuple[bool, List[str], Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    errors = []
    if not isinstance(parsed_data, dict):
        return False, ["Parsed data is not a JSON dictionary"], None, None
    
    # Check top-level required fields
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
                    errors.append(f"'lo_evaluations' factor '{k}' value '{v}' is not a numeric score or null")
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
                    errors.append(f"'go_evaluations' factor '{k}' value '{v}' is not a numeric score or null")
                elif not (-1.0 <= float(v) <= 1.0):
                    errors.append(f"'go_evaluations' factor '{k}' score {v} out of range [-1.0, 1.0]")
                    
    is_valid = len(errors) == 0
    return is_valid, errors, lo_evals, go_evals

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
            # Fallback exact substring match
            for sm in served_models:
                if sc_model.lower() in sm.lower():
                    matched = sm
                    break
        mapping[sc_model] = matched
    return mapping

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
                    val_status = "UNTESTED"
                    err_msg = ""
                    lat_sec = ""
                    
                    if raw_file.exists():
                        try:
                            with open(raw_file, "r") as rf:
                                rdata = json.load(rf)
                                val_status = rdata.get("validation_status", "UNKNOWN")
                                attempts = rdata.get("attempts", 1)
                                lat_sec = rdata.get("latency_seconds", "")
                                err_msg = "; ".join(rdata.get("validation_errors", []))
                                if val_status == "VALID":
                                    status = "COMPLETE"
                                elif val_status == "INVALID":
                                    status = "INVALID"
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
                        "validation_status": val_status,
                        "error": err_msg,
                        "latency_seconds": lat_sec,
                    })
                    
    df = pd.DataFrame(rows)
    df.to_csv(MANIFEST_PATH, index=False)
    return df

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
        print("   Load all 3 models in LM Studio before launching inference.")
        return False
        
    print("\n✅ PREFLIGHT PASSED: Environment ready for inference.")
    return True

# Canonical Long CSV Generator
def generate_long_csv() -> pd.DataFrame:
    raw_files = sorted(list(RAW_DIR.glob("*.json")))
    records = []
    
    for rf in raw_files:
        try:
            with open(rf, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data.get("validation_status") != "VALID":
                continue
                
            paper_id = data["paper_id"]
            sc_model = data["scientific_model"]
            served_id = data["served_model_id"]
            temp = float(data["temperature"])
            repeat = int(data["repeat"])
            cid = data["condition_id"]
            
            lo_evals = data.get("lo_evaluations", {})
            go_evals = data.get("go_evaluations", {})
            
            for factor_name, score in lo_evals.items():
                records.append({
                    "paper_id": paper_id,
                    "scientific_model": sc_model,
                    "served_model_id": served_id,
                    "temperature": temp,
                    "repeat": repeat,
                    "context": "LO",
                    "factor": factor_name,
                    "score": score if score is not None else "",
                    "condition_id": cid,
                })
                
            for factor_name, score in go_evals.items():
                records.append({
                    "paper_id": paper_id,
                    "scientific_model": sc_model,
                    "served_model_id": served_id,
                    "temperature": temp,
                    "repeat": repeat,
                    "context": "GO",
                    "factor": factor_name,
                    "score": score if score is not None else "",
                    "condition_id": cid,
                })
        except Exception:
            continue
            
    df = pd.DataFrame(records)
    df.to_csv(SCORES_LONG_PATH, index=False)
    print(f"Generated {SCORES_LONG_PATH.name} with {len(df)} score rows.")
    return df

# Single Cell Inference Execution Helper
def execute_cell_inference(
    paper_path: Path,
    scientific_model: str,
    served_model_id: str,
    temp: float,
    repeat: int,
    engine_url: str = "http://localhost:1234",
    max_retries: int = 3,
) -> Dict[str, Any]:
    paper_id = extract_paper_id(paper_path)
    cid = generate_condition_id(paper_id, scientific_model, temp, repeat)
    raw_file = RAW_DIR / f"{cid}.json"
    
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
    
    full_prompt = f"{instructions_text}\n\n**GLOSSARY:**\n{glossary_text}\n\n**DOCUMENT:**\n{study_text}\n\n**FILL IN THE SCORES:**\n\nReturn exactly one valid JSON object and nothing else."
    prompt_sha = compute_string_sha256(full_prompt)
    
    headers = {"Content-Type": "application/json", "Authorization": "Bearer mlx-server"}
    url = f"{engine_url.rstrip('/')}/v1/chat/completions"
    
    payload = {
        "model": served_model_id,
        "messages": [{"role": "user", "content": full_prompt}],
        "temperature": temp,
        "top_p": TOP_P,
        "min_p": MIN_P,
        "max_tokens": 16384,
    }
    
    attempts = 0
    raw_response_text = ""
    parsed_data = None
    val_status = "ERROR"
    val_errors = []
    lo_evals = None
    go_evals = None
    reasoning_log = ""
    http_status = None
    latency = 0.0
    
    for attempt in range(1, max_retries + 1):
        attempts = attempt
        start_time = time.time()
        start_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start_time))
        
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=300)
            end_time = time.time()
            end_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(end_time))
            latency = round(end_time - start_time, 3)
            http_status = resp.status_code
            
            if resp.status_code == 200:
                res_json = resp.json()
                choices = res_json.get("choices", [])
                if choices:
                    raw_response_text = choices[0].get("message", {}).get("content") or choices[0].get("text") or ""
                    
                # Parse JSON
                from jmllm.util.helpers import parse_llm_output_as_json
                parsed_data = parse_llm_output_as_json(raw_response_text)
                
                # Validate schema
                is_valid, errs, lo, go = validate_response(parsed_data)
                val_errors = errs
                if is_valid:
                    val_status = "VALID"
                    lo_evals = lo
                    go_evals = go
                    reasoning_log = parsed_data.get("reasoning_log_text", "")
                    break
                else:
                    val_status = "INVALID"
            else:
                val_errors = [f"HTTP error {resp.status_code}: {resp.text}"]
                val_status = "ERROR"
        except Exception as e:
            end_time = time.time()
            end_ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(end_time))
            latency = round(end_time - start_time, 3)
            val_errors = [f"Network/Request exception: {str(e)}"]
            val_status = "ERROR"
            
        time.sleep(2 ** (attempt - 1))
        
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
        "prompt_sha256": prompt_sha,
        "glossary_sha256": glossary_sha,
        "instruction_sha256": instruction_sha,
        "git_commit": git_commit,
        "request_start_timestamp": start_ts if 'start_ts' in locals() else "",
        "request_end_timestamp": end_ts if 'end_ts' in locals() else "",
        "latency_seconds": latency,
        "http_status": http_status,
        "attempts": attempts,
        "raw_assistant_response": raw_response_text,
        "parsed_response": parsed_data,
        "validation_status": val_status,
        "validation_errors": val_errors,
        "lo_evaluations": lo_evals,
        "go_evaluations": go_evals,
        "reasoning_log_text": reasoning_log,
    }
    
    with open(raw_file, "w", encoding="utf-8") as rf:
        json.dump(result_record, rf, indent=2)
        
    return result_record

# Smoke Test (9 calls)
def run_smoke_test(engine_url: str = "http://localhost:1234") -> bool:
    print("=" * 65)
    print("      MLLM REVIEWER ROBUSTNESS EXPERIMENT — 9-CALL SMOKE TEST")
    print("=" * 65)
    
    served_models = query_served_models(engine_url)
    mapping = resolve_model_mapping(served_models)
    
    # Check all 3 models mapped
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
        for temp in TEMPERATURES:
            cid = generate_condition_id(paper_id, sc_model, temp, 1)
            print(f"\n🚀 Executing Call {executed+1}/9: {cid}")
            rec = execute_cell_inference(target_paper, sc_model, served_id, temp, 1, engine_url=engine_url)
            executed += 1
            v_stat = rec["validation_status"]
            print(f"   Status: {v_stat} | Latency: {rec['latency_seconds']}s | Attempts: {rec['attempts']}")
            if v_stat == "VALID":
                valid_count += 1
            else:
                print(f"   Errors: {rec['validation_errors']}")
                
    generate_manifest(mapping)
    generate_long_csv()
    
    print("\n" + "=" * 65)
    print(f"SMOKE TEST COMPLETE: {valid_count}/9 calls marked VALID.")
    print("=" * 65)
    return valid_count == 9

# Main CLI Entry Point
def main():
    import argparse
    parser = argparse.ArgumentParser(description="MLLM Reviewer Robustness Experiment Harness")
    parser.add_argument("--preflight", action="store_true", help="Run preflight diagnostics and exit")
    parser.add_argument("--test", action="store_true", help="Run unit test suite")
    parser.add_argument("--smoke-test", action="store_true", help="Run 9-call smoke test (1 paper x 3 models x 3 temps x rep 1)")
    parser.add_argument("--full-experiment", action="store_true", help="Run full 837-call experiment")
    parser.add_argument("--confirm-full-run", action="store_true", help="Required confirmation flag for full experiment")
    parser.add_argument("--generate-csv", action="store_true", help="Compile scores_long.csv from valid raw outputs")
    parser.add_argument("--engine-url", default="http://localhost:1234", help="LM Studio OpenAI-compatible endpoint")
    
    args = parser.parse_args()
    
    if args.preflight:
        success = run_preflight(args.engine_url)
        sys.exit(0 if success else 1)
    elif args.test:
        print("Running pytest on test_robustness_runner.py...")
        res = subprocess.run([sys.executable, "-m", "pytest", str(REPO_ROOT / "tests" / "test_robustness_runner.py")])
        sys.exit(res.returncode)
    elif args.generate_csv:
        generate_long_csv()
        sys.exit(0)
    elif args.smoke_test:
        print("Smoke test mode selected.")
        success = run_smoke_test(args.engine_url)
        sys.exit(0 if success else 1)
    elif args.full_experiment:
        if not args.confirm_full_run:
            print("❌ Full experiment requires --confirm-full-run flag.")
            sys.exit(1)
        print("Full experiment requested.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
