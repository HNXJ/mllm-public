"""Runner for the 54-Call Evidence-vs-Prior Factorial Ablation Experiment.

Factorial Design:
6 Papers x 3 Conditions x 3 Repeats = 54 Calls
Model: gemma-4-31b-it
Sampler: T=0.35, top_p=0.90, min_p=0.10
Endpoint: http://localhost:1234/v1

Outputs:
- artifacts/csvs/source_tables/evidence_prior_calls_ledger_54.csv (Call-level runtime provenance)
- artifacts/csvs/source_tables/evidence_prior_scores_54.csv (Parsed factor scores)
- content/raw_responses/evidence_prior_202608/{call_id}.json (Raw JSON completions)
"""

import json
import time
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import pandas as pd
import requests

from jmllm.util.prompts import build_hpc_prompt, get_glossary_instruction_block
from jmllm.util.helpers import parse_llm_output_as_json

REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "content" / "tables" / "evidence_prior_54_calls_manifest.csv"
LEDGER_PATH = REPO_ROOT / "content" / "tables" / "evidence_prior_calls_ledger_54.csv"
SCORES_PATH = REPO_ROOT / "content" / "tables" / "evidence_prior_scores_54.csv"
RAW_DIR = REPO_ROOT / "content" / "raw_responses" / "evidence_prior_202608"

GLOSSARY_PATH = REPO_ROOT / "ontology" / "glossary" / "HPC" / "hpc-36-reference.md"
BASE_URL = "http://localhost:1234/v1"
MODEL_ID = "gemma-4-31b-it"


def load_glossary() -> Tuple[str, List[str]]:
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
    return text, factors


def execute_single_call(
    call_id: str,
    paper_id: str,
    condition: str,
    repeat: int,
    input_file: Path,
    glossary_text: str,
    glossary_keys: List[str]
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Executes a single inference call against LM Studio OpenAI-compatible endpoint."""
    input_text = input_file.read_text(encoding="utf-8")
    input_sha256 = hashlib.sha256(input_text.encode("utf-8")).hexdigest()

    prompt = build_hpc_prompt(input_text, glossary_text, glossary_keys, MODEL_ID)
    payload = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": "You are an expert neuroscientist evaluating scientific literature against the HPC-36 ontology."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.35,
        "top_p": 0.90,
        "min_p": 0.10,
        "max_tokens": 8192
    }

    start_t = time.time()
    iso_start = datetime.now(timezone.utc).isoformat()
    raw_path = RAW_DIR / f"{call_id}.json"
    
    # Check if raw output already exists (resumability)
    if raw_path.exists():
        with open(raw_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        raw_content = raw_data.get("response_text", "")
        status = "COMPLETED_CACHED"
        latency = raw_data.get("latency_seconds", 0.0)
    else:
        try:
            resp = requests.post(f"{BASE_URL}/chat/completions", json=payload, timeout=600)
            latency = time.time() - start_t
            if resp.status_code == 200:
                resp_json = resp.json()
                raw_content = resp_json["choices"][0]["message"]["content"]
                status = "COMPLETED_SUCCESS"
                # Save raw response
                RAW_DIR.mkdir(parents=True, exist_ok=True)
                with open(raw_path, "w", encoding="utf-8") as f:
                    json.dump({
                        "call_id": call_id,
                        "paper_id": paper_id,
                        "condition": condition,
                        "repeat": repeat,
                        "model": MODEL_ID,
                        "temperature": 0.35,
                        "top_p": 0.90,
                        "min_p": 0.10,
                        "input_sha256": input_sha256,
                        "timestamp": iso_start,
                        "latency_seconds": latency,
                        "response_text": raw_content,
                        "full_response": resp_json
                    }, f, indent=2)
            else:
                raw_content = ""
                status = f"HTTP_ERROR_{resp.status_code}: {resp.text[:200]}"
        except Exception as e:
            latency = time.time() - start_t
            raw_content = ""
            status = f"EXCEPTION: {str(e)[:200]}"

    # Ledger record
    ledger_record = {
        "call_id": call_id,
        "paper_id": paper_id,
        "condition": condition,
        "repeat": repeat,
        "model": MODEL_ID,
        "temperature": 0.35,
        "top_p": 0.90,
        "min_p": 0.10,
        "input_sha256": input_sha256,
        "status": status,
        "latency_seconds": round(latency, 2),
        "timestamp": iso_start,
        "raw_response_path": str(raw_path.relative_to(REPO_ROOT)) if raw_path.exists() else "N/A"
    }

    # Parse factor scores if output available
    score_rows = []
    if raw_content:
        parsed = parse_llm_output_as_json(raw_content, compatibility_mode=True)
        if isinstance(parsed, dict):
            lo_dict = parsed.get("lo_evaluations", {})
            go_dict = parsed.get("go_evaluations", {})
            
            # Match factors
            for idx, k in enumerate(glossary_keys, start=1):
                f_id = f"F{idx:02d}"
                lo_s = lo_dict.get(k) if isinstance(lo_dict, dict) else None
                go_s = go_dict.get(k) if isinstance(go_dict, dict) else None
                
                # Check valid bounds [-1.0, 1.0]
                lo_val = float(lo_s) if lo_s is not None and isinstance(lo_s, (int, float)) and -1.0 <= lo_s <= 1.0 else None
                go_val = float(go_s) if go_s is not None and isinstance(go_s, (int, float)) and -1.0 <= go_s <= 1.0 else None
                
                score_rows.append({
                    "call_id": call_id,
                    "paper_id": paper_id,
                    "condition": condition,
                    "repeat": repeat,
                    "factor": f"LO-{f_id}",
                    "context": "LO",
                    "score": lo_val
                })
                score_rows.append({
                    "call_id": call_id,
                    "paper_id": paper_id,
                    "condition": condition,
                    "repeat": repeat,
                    "factor": f"GO-{f_id}",
                    "context": "GO",
                    "score": go_val
                })

    return ledger_record, score_rows


def run_54_call_ablation_sweep() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Runs all 54 calls sequentially with atomic ledger updates."""
    manifest = pd.read_csv(MANIFEST_PATH)
    glossary_text, glossary_keys = load_glossary()

    ledger_records = []
    all_scores = []

    print(f"Starting 54-Call Sweep against {MODEL_ID} at T=0.35...", flush=True)
    for idx, row in manifest.iterrows():
        c_id = row["call_id"]
        p_id = row["paper_id"]
        cond = row["condition"]
        rep = int(row["repeat"])
        in_file = REPO_ROOT / row["input_markdown_file"]

        print(f"[{idx+1}/54] Executing {c_id}: {p_id} | {cond} | R{rep}...", flush=True)
        l_rec, s_rows = execute_single_call(c_id, p_id, cond, rep, in_file, glossary_text, glossary_keys)
        ledger_records.append(l_rec)
        all_scores.extend(s_rows)

        # Atomic periodic save
        pd.DataFrame(ledger_records).to_csv(LEDGER_PATH, index=False)
        if all_scores:
            pd.DataFrame(all_scores).to_csv(SCORES_PATH, index=False)

    df_ledger = pd.DataFrame(ledger_records)
    df_scores = pd.DataFrame(all_scores)
    df_ledger.to_csv(LEDGER_PATH, index=False)
    df_scores.to_csv(SCORES_PATH, index=False)
    print("Sweep complete. Ledger and scores written.", flush=True)
    return df_ledger, df_scores


if __name__ == "__main__":
    run_54_call_ablation_sweep()
