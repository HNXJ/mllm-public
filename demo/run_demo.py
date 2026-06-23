#!/usr/bin/env python3
"""MLLM reviewer demo: offline, model-free, end-to-end run.

This script exercises the REAL pipeline code (no mocked package
internals) on tiny synthetic data so a reviewer can verify the
repository's claim-aggregation logic without an MLX engine, GPU, or
downloaded model weights:

1. ``mllm.data.preprocessors.parse_llm_output_as_json`` — rescues a
   noisy/markdown-fenced raw LLM response into clean JSON (the same
   function the pipeline uses on real model output).
2. ``mllm.data.preprocessors.aggregate_scores_from_json`` — loads every
   per-model evaluation JSON in ``sample_input/`` into a single
   long-form DataFrame (the same function used to build manuscript
   tables).
3. A consensus aggregation (mean / median / std / n / agreement) over
   that DataFrame, following the methodology described in
   docs/REPRODUCIBILITY.md.

All input data in ``sample_input/`` is SYNTHETIC placeholder data
invented for this demo. It is not drawn from the manuscript corpus and
carries no scientific claim.

Usage:
    python demo/run_demo.py

Expected runtime: a few seconds on a normal desktop computer (no
network access or GPU required).
"""

import json
import sys
import time
from pathlib import Path

import pandas as pd

DEMO_DIR = Path(__file__).parent.resolve()
SAMPLE_INPUT = DEMO_DIR / "sample_input"
OUTPUT_DIR = DEMO_DIR / "demo_output"


def step_json_rescue() -> dict:
    """Demonstrate clean_json_string / parse_llm_output_as_json on a noisy raw response."""
    from mllm.data.preprocessors import parse_llm_output_as_json

    raw_text = (SAMPLE_INPUT / "raw_model_output_example.txt").read_text()
    parsed = parse_llm_output_as_json(raw_text, compatibility_mode=True)
    assert "REPAIR_REQUIRED" not in parsed, "JSON rescue failed on demo input"
    print(f"[1/3] Rescued raw model output -> agent_name={parsed.get('agent_name')!r}")
    return parsed


def step_aggregate() -> pd.DataFrame:
    """Aggregate every *_eval.json file in sample_input/ into one long-form table."""
    from mllm.data.preprocessors import aggregate_scores_from_json

    df = aggregate_scores_from_json(SAMPLE_INPUT)
    if df.empty:
        raise RuntimeError(f"No evaluation rows found in {SAMPLE_INPUT}")
    print(f"[2/3] Aggregated {len(df)} factor-score rows from "
          f"{len(list(SAMPLE_INPUT.glob('*_eval.json')))} evaluation files")
    return df


def step_consensus(df: pd.DataFrame) -> pd.DataFrame:
    """Compute per-study/context/factor consensus statistics across council members."""
    grouped = df.groupby(["Study", "Context", "Factor"])["Score"]
    consensus = grouped.agg(
        n_models="count",
        mean_score="mean",
        median_score="median",
        std_score="std",
    ).reset_index()
    consensus["std_score"] = consensus["std_score"].fillna(0.0)
    consensus = consensus.sort_values(["Study", "Context", "Factor"]).reset_index(drop=True)
    print(f"[3/3] Computed consensus statistics for {len(consensus)} (study, context, factor) groups")
    return consensus


def main() -> int:
    start = time.time()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    step_json_rescue()
    df = step_aggregate()
    consensus = step_consensus(df)

    raw_path = OUTPUT_DIR / "aggregated_scores.csv"
    consensus_csv_path = OUTPUT_DIR / "consensus_summary.csv"
    consensus_json_path = OUTPUT_DIR / "consensus_summary.json"

    df.to_csv(raw_path, index=False)
    consensus.to_csv(consensus_csv_path, index=False)
    consensus_json_path.write_text(
        json.dumps(json.loads(consensus.to_json(orient="records")), indent=2)
    )

    elapsed = time.time() - start
    print(f"\nDone in {elapsed:.2f}s. Wrote:")
    print(f"  - {raw_path.relative_to(DEMO_DIR.parent)}")
    print(f"  - {consensus_csv_path.relative_to(DEMO_DIR.parent)}")
    print(f"  - {consensus_json_path.relative_to(DEMO_DIR.parent)}")
    print("\nCompare against demo/expected_output/ to verify correctness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
