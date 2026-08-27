"""Figure-Text Ablation Experiment Runner (31-Paper NO_FIGURE_TEXT Sensitivity).

Dedicated minimal adapter for the Scientific Reports reviewer figure-text sensitivity analysis.
Ensures 100% Request, Prompt, Sampler, and Parser Equivalence with the frozen T=0.00 / R=01 baseline.
"""

import os
import sys
import json
import time
import hashlib
import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import pandas as pd
import requests

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "content" / "tables" / "figure_text_ablation_input_manifest.csv"
LEDGER_PATH = REPO_ROOT / "content" / "tables" / "figure_text_ablation_calls_ledger_31.csv"
SCORES_PATH = REPO_ROOT / "content" / "tables" / "figure_text_ablation_scores.csv"
RAW_DIR = REPO_ROOT / "content" / "raw_responses" / "figure_text_ablation_202608"

GLOSSARY_PATH = REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md"
INSTRUCTIONS_PATH = REPO_ROOT / "ontology" / "instructions" / "hpc_eval_prompt.md"

BASE_URL = "http://localhost:1234/v1"
SCIENTIFIC_MODEL = "gemma-4-31b-it"
TEMPERATURE = 0.00
TOP_P = 0.90
MIN_P = 0.10
REPEAT = 1


def load_canonical_glossary() -> Tuple[str, List[str]]:
    """Loads and parses the exact 36 canonical factors from the reference glossary."""
    if not GLOSSARY_PATH.exists():
        raise FileNotFoundError(f"Glossary missing at {GLOSSARY_PATH}")
    text = GLOSSARY_PATH.read_text(encoding="utf-8")
    factors = []
    for line in text.splitlines():
        if line.strip().startswith("|") and "Factor Name" not in line and "----" not in line and "Total" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1].isdigit():
                factors.append(parts[2])
    if len(factors) != 36:
        raise ValueError(f"Expected 36 canonical factors, parsed {len(factors)}")
    return text, factors


# Load canonical factor keys once at module level
_, CANONICAL_FACTORS = load_canonical_glossary()


def build_canonical_hpc_prompt(study_text: str, glossary_text: str, glossary_keys: List[str], model_name: str) -> str:
    """Exact byte-for-byte prompt construction from historical pipeline (src/jmllm/util/prompts.py)."""
    keys_json = json.dumps(glossary_keys, ensure_ascii=False)
    return f"""
You are a senior neuroscientist and biophysicist evaluating predictive-coding mechanisms in a neuroscience study.

Evaluate the study against the supplied glossary.

Definitions:
- LO (Local Oddball): short-term sensory deviance or immediate stimulus violation.
- GO (Global Oddball): long-term or sequence-level deviance over a broader temporal pattern.

Scoring semantics:
- +1.0: strong evidence supporting the factor
- +0.5: moderate evidence supporting the factor
- 0.0: explicitly addressed but neutral, mixed, or inconclusive
- -0.5: moderate evidence against the factor
- -1.0: strong evidence against the factor
- null: factor cannot be meaningfully evaluated from the study

Requirements:
1. Return exactly one valid JSON object and nothing else.
2. Do not wrap the JSON in markdown fences.
3. Include every glossary key exactly once in both `lo_evaluations` and `go_evaluations`.
4. Use exact glossary key strings.
5. Do not add extra keys inside `lo_evaluations` or `go_evaluations`.
6. Use `null` when a factor is not meaningfully addressed.
7. Use `0.0` only when the factor is discussed but neutral or inconclusive.
8. Do not guess metadata. Use null if uncertain.
9. Keep `reasoning_log_text` concise and evidence-based.

Glossary Definitions:
{glossary_text}

Glossary Keys:
{keys_json}

Study Text:
{study_text}

Required output shape:
{{
  "lo_evaluations": {{ "Factor Name": 0.8 }},
  "go_evaluations": {{ "Factor Name": 0.5 }},
  "first_author": "Name or null",
  "publication_year": "YYYY or null",
  "study_type": "Empirical or Review or null",
  "agent_name": "{model_name}",
  "reasoning_log_text": "Concise evidence-based rationale."
}}
""".strip()


# Canonical Parsing and Recovery Logic (Exact port from robustness_runner.py)
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
            errors.append(f"'lo_evaluations' missing {len(missing_lo)} keys: {list(missing_lo)[:3]}")
            
    if go_evals is not None:
        go_keys = list(go_evals.keys())
        if len(go_keys) != 36:
            errors.append(f"'go_evaluations' has {len(go_keys)} keys, expected 36")
        missing_go = set(CANONICAL_FACTORS) - set(go_keys)
        if missing_go:
            errors.append(f"'go_evaluations' missing {len(missing_go)} keys: {list(missing_go)[:3]}")
            
    return (len(errors) == 0), errors, lo_evals, go_evals


def extract_json_block(text: str) -> Optional[str]:
    cleaned = re.sub(r'//.*?\n|/\*.*?\*/', '', text, flags=re.S)
    match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', cleaned, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r'\{.*\}', cleaned, re.DOTALL)
    if match:
        candidate = match.group(0).strip()
        stack = []
        start_idx = candidate.find('{')
        for idx in range(start_idx, len(candidate)):
            char = candidate[idx]
            if char == '{':
                stack.append('{')
            elif char == '}':
                if stack:
                    stack.pop()
                    if not stack:
                        return candidate[start_idx:idx+1]
        return candidate
    return None


def parse_and_recover_generation(raw_generation: str) -> Tuple[str, str, Optional[Dict[str, Any]], Optional[Dict[str, Any]], Optional[Dict[str, Any]], List[str], str]:
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

    # 2. Try JSON extraction via balanced brace extraction
    json_block = extract_json_block(raw_generation)
    if json_block:
        try:
            data = json.loads(json_block, strict=False)
            is_valid, errs, lo, go = validate_response_schema(data)
            if is_valid:
                return "valid", "cleaned_json", data, lo, go, [], "Cleaned JSON strictly valid"
            else:
                lo_raw = data.get("lo_evaluations")
                go_raw = data.get("go_evaluations")
                if isinstance(lo_raw, dict) or isinstance(go_raw, dict):
                    lo_rec = {f: (float(lo_raw[f]) if isinstance(lo_raw, dict) and f in lo_raw and isinstance(lo_raw[f], (int, float)) and -1.0 <= float(lo_raw[f]) <= 1.0 else None) for f in CANONICAL_FACTORS}
                    go_rec = {f: (float(go_raw[f]) if isinstance(go_raw, dict) and f in go_raw and isinstance(go_raw[f], (int, float)) and -1.0 <= float(go_raw[f]) <= 1.0 else None) for f in CANONICAL_FACTORS}
                    return "recovered", "extracted_json_block", data, lo_rec, go_rec, errs, f"Recovered scores from JSON structure. Errors: {'; '.join(errs)}"
        except Exception:
            pass

    # 3. Fallback: Key-Value regex extraction
    extracted = {}
    for k, v in re.findall(r'\"([^\"]+)\"\s*(?:=|:)\s*([+-]?\d+\.?\d*|null)', raw_generation, re.IGNORECASE):
        k_clean = k.strip()
        if k_clean in CANONICAL_FACTORS and k_clean not in extracted:
            extracted[k_clean] = float(v) if v.lower() != 'null' else None

    if len(extracted) >= 18:
        lo_rec = {f: extracted.get(f) for f in CANONICAL_FACTORS}
        go_rec = {f: extracted.get(f) for f in CANONICAL_FACTORS}
        return "recovered", "regex_fallback", {"lo_evaluations": lo_rec, "go_evaluations": go_rec}, lo_rec, go_rec, ["Recovered via regex"], f"Extracted {len(extracted)} factors"

    return "unrecoverable", "failed", None, None, None, ["Could not parse JSON structure"], "Failed to extract valid factor scores"


def validate_manifest(manifest_path: Path = MANIFEST_PATH) -> pd.DataFrame:
    """Strict preflight validation of the 31-paper input manifest and input SHA-256 hashes."""
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest missing at {manifest_path}")
    
    df = pd.read_csv(manifest_path)
    if len(df) != 31:
        raise ValueError(f"Manifest must contain exactly 31 rows, found {len(df)}")
    
    if df["paper_id"].nunique() != 31:
        raise ValueError(f"Manifest contains duplicate paper IDs: {df['paper_id'].duplicated().sum()} duplicates")
        
    for idx, row in df.iterrows():
        p_id = row["paper_id"]
        in_path = REPO_ROOT / row["nofigure_input_path"]
        expected_sha = row["nofigure_input_sha256"]
        
        if not in_path.exists():
            raise FileNotFoundError(f"Staged no-figure input missing for {p_id} at {in_path}")
            
        actual_sha = hashlib.sha256(in_path.read_bytes()).hexdigest()
        if actual_sha != expected_sha:
            raise ValueError(f"SHA-256 mismatch for {p_id}: Expected {expected_sha}, Actual {actual_sha}")
            
    return df


def execute_single_call(
    call_id: str,
    paper_id: str,
    input_file: Path,
    glossary_text: str,
    glossary_keys: List[str],
    dry_run: bool = False,
    endpoint_url: str = BASE_URL
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Executes a single scoring inference call with exact payload equivalence."""
    input_text = input_file.read_text(encoding="utf-8")
    input_sha256 = hashlib.sha256(input_text.encode("utf-8")).hexdigest()

    prompt = build_canonical_hpc_prompt(input_text, glossary_text, glossary_keys, SCIENTIFIC_MODEL)
    
    # Exact payload structure matching robustness_runner.py (single user message, no system message)
    payload = {
        "model": SCIENTIFIC_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "min_p": MIN_P,
        "max_tokens": 4096
    }

    if dry_run:
        ledger_rec = {
            "call_id": call_id,
            "paper_id": paper_id,
            "condition": "NO_FIGURE_TEXT",
            "repeat": REPEAT,
            "scientific_model": SCIENTIFIC_MODEL,
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "min_p": MIN_P,
            "input_file": str(input_file.relative_to(REPO_ROOT)),
            "input_sha256": input_sha256,
            "status": "DRY_RUN_VALIDATED",
            "prompt_length_chars": len(prompt),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        return ledger_rec, []

    start_time = time.time()
    url = f"{endpoint_url}/chat/completions" if endpoint_url.endswith("/v1") else f"{endpoint_url}/v1/chat/completions"
    resp = requests.post(url, json=payload, timeout=1800)
    latency = time.time() - start_time

    if resp.status_code != 200:
        raise RuntimeError(f"HTTP Error {resp.status_code} from endpoint: {resp.text}")

    resp_json = resp.json()
    choices = resp_json.get("choices", [])
    raw_content = choices[0].get("message", {}).get("content") or "" if choices else ""
    
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_file = RAW_DIR / f"{call_id}.json"
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump({
            "call_id": call_id,
            "paper_id": paper_id,
            "condition": "NO_FIGURE_TEXT",
            "repeat": REPEAT,
            "scientific_model": SCIENTIFIC_MODEL,
            "served_model_id": resp_json.get("model", SCIENTIFIC_MODEL),
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "min_p": MIN_P,
            "latency_seconds": latency,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "raw_assistant_response": raw_content,
            "raw_response": resp_json
        }, f, indent=2)

    p_status, p_method, p_data, lo_evals, go_evals, errs, notes = parse_and_recover_generation(raw_content)

    if p_status == "unrecoverable" or not lo_evals or not go_evals:
        # Completeness guard: do not mark as COMPLETED if unrecoverable
        ledger_rec = {
            "call_id": call_id,
            "paper_id": paper_id,
            "condition": "NO_FIGURE_TEXT",
            "repeat": REPEAT,
            "scientific_model": SCIENTIFIC_MODEL,
            "served_model_id": resp_json.get("model", SCIENTIFIC_MODEL),
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "min_p": MIN_P,
            "input_file": str(input_file.relative_to(REPO_ROOT)),
            "input_sha256": input_sha256,
            "latency_seconds": latency,
            "parse_status": p_status,
            "parser_method": p_method,
            "status": "PARSE_FAILED",
            "parse_errors": "; ".join(errs),
            "raw_file": str(raw_file.relative_to(REPO_ROOT)),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        return ledger_rec, []

    score_rows = []
    for factor in glossary_keys:
        lo_val = lo_evals.get(factor)
        go_val = go_evals.get(factor)
        
        score_rows.append({
            "paper_id": paper_id,
            "condition": "NO_FIGURE_TEXT",
            "repeat": REPEAT,
            "context": "LO",
            "factor": factor,
            "score": lo_val if lo_val is not None else "",
            "call_id": call_id,
            "scientific_model": SCIENTIFIC_MODEL,
            "temperature": TEMPERATURE,
            "parse_status": p_status,
            "parser_method": p_method
        })
        score_rows.append({
            "paper_id": paper_id,
            "condition": "NO_FIGURE_TEXT",
            "repeat": REPEAT,
            "context": "GO",
            "factor": factor,
            "score": go_val if go_val is not None else "",
            "call_id": call_id,
            "scientific_model": SCIENTIFIC_MODEL,
            "temperature": TEMPERATURE,
            "parse_status": p_status,
            "parser_method": p_method
        })

    ledger_rec = {
        "call_id": call_id,
        "paper_id": paper_id,
        "condition": "NO_FIGURE_TEXT",
        "repeat": REPEAT,
        "scientific_model": SCIENTIFIC_MODEL,
        "served_model_id": resp_json.get("model", SCIENTIFIC_MODEL),
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "min_p": MIN_P,
        "input_file": str(input_file.relative_to(REPO_ROOT)),
        "input_sha256": input_sha256,
        "latency_seconds": latency,
        "parse_status": p_status,
        "parser_method": p_method,
        "status": "COMPLETED",
        "raw_file": str(raw_file.relative_to(REPO_ROOT)),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    return ledger_rec, score_rows


def run_ablation_sweep(
    manifest_path: Path = MANIFEST_PATH,
    dry_run: bool = False,
    endpoint_url: str = BASE_URL
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Executes the 31-paper ablation sweep with atomic updates and safe resume semantics."""
    df_manifest = validate_manifest(manifest_path)
    glossary_text, glossary_keys = load_canonical_glossary()

    existing_completed_calls = set()
    ledger_records = []
    all_scores = []
    
    if LEDGER_PATH.exists() and not dry_run:
        try:
            prev_ledger = pd.read_csv(LEDGER_PATH)
            completed = prev_ledger[prev_ledger["status"] == "COMPLETED"]
            existing_completed_calls = set(completed["call_id"].tolist())
            ledger_records = prev_ledger.to_dict("records")
            if SCORES_PATH.exists():
                all_scores = pd.read_csv(SCORES_PATH).to_dict("records")
            print(f"Resuming: found {len(existing_completed_calls)} previously completed calls.")
        except Exception as e:
            print(f"Warning: could not parse existing ledger ({e}). Starting fresh.")

    mode_str = "DRY-RUN (No Network)" if dry_run else f"LIVE INFERENCE against {endpoint_url}"
    print(f"Starting 31-Paper NO_FIGURE_TEXT Sweep [{mode_str}]...", flush=True)

    for idx, row in df_manifest.iterrows():
        p_id = row["paper_id"]
        call_id = f"NOFIG__{p_id}__gemma-4-31b-it__T000__R01"
        in_file = REPO_ROOT / row["nofigure_input_path"]

        if call_id in existing_completed_calls:
            print(f"[{idx+1}/31] Skipping {call_id} (already completed).")
            continue

        print(f"[{idx+1}/31] Processing {call_id} ({p_id})...", flush=True)
        l_rec, s_rows = execute_single_call(
            call_id, p_id, in_file, glossary_text, glossary_keys,
            dry_run=dry_run, endpoint_url=endpoint_url
        )
        ledger_records.append(l_rec)
        all_scores.extend(s_rows)

        if not dry_run:
            pd.DataFrame(ledger_records).to_csv(LEDGER_PATH, index=False)
            if all_scores:
                pd.DataFrame(all_scores).to_csv(SCORES_PATH, index=False)

    df_ledger = pd.DataFrame(ledger_records)
    df_scores = pd.DataFrame(all_scores)
    
    if not dry_run:
        df_ledger.to_csv(LEDGER_PATH, index=False)
        df_scores.to_csv(SCORES_PATH, index=False)
        print("Sweep complete. Ledger and scores written.", flush=True)
    else:
        print("Dry run completed successfully. All 31 inputs validated.", flush=True)
        
    return df_ledger, df_scores


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="31-Paper NO_FIGURE_TEXT Ablation Runner")
    parser.add_argument("--dry-run", action="store_true", help="Validate manifest and requests without network calls")
    parser.add_argument("--engine-url", type=str, default=BASE_URL, help="LM Studio server base URL")
    args = parser.parse_args()

    run_ablation_sweep(dry_run=args.dry_run, endpoint_url=args.engine_url)
