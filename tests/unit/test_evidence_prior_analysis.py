"""Unit tests for the Evidence vs. Prior descriptive analysis module."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from jmllm.analysis.evidence_prior_analysis import analyze_evidence_prior_results


def test_evidence_prior_analysis_synthetic(tmp_path):
    # Construct synthetic test scores table
    records = []
    for p in ["Garret2020", "Attinger2017"]:
        for f_idx in range(1, 37):
            f = f"F{f_idx:02d}"
            for c in ["LO", "GO"]:
                for rep in [1, 2, 3]:
                    # Cond A (Full)
                    records.append({
                        "call_id": f"call_A_{p}_{rep}",
                        "paper_id": p,
                        "condition": "Condition A (Full)",
                        "repeat": rep,
                        "factor": f"{c}-{f}",
                        "context": c,
                        "score": 0.5 + 0.01 * f_idx
                    })
                    # Cond B (Abstract) - slightly lower
                    records.append({
                        "call_id": f"call_B_{p}_{rep}",
                        "paper_id": p,
                        "condition": "Condition B (Abstract)",
                        "repeat": rep,
                        "factor": f"{c}-{f}",
                        "context": c,
                        "score": 0.3 + 0.01 * f_idx
                    })
                    # Cond C (Masked) - almost identical to Cond A
                    records.append({
                        "call_id": f"call_C_{p}_{rep}",
                        "paper_id": p,
                        "condition": "Condition C (Masked)",
                        "repeat": rep,
                        "factor": f"{c}-{f}",
                        "context": c,
                        "score": 0.5 + 0.01 * f_idx + 0.001 * rep
                    })

    scores_df = pd.DataFrame(records)
    scores_path = tmp_path / "test_scores.csv"
    out_path = tmp_path / "test_summary.csv"
    scores_df.to_csv(scores_path, index=False)

    summary_dict, df_res = analyze_evidence_prior_results(scores_path, out_path)
    assert len(df_res) == 2
    assert out_path.exists()

    # Check A vs B
    ab_row = df_res[df_res["comparison_name"] == "Full Text (A) vs Abstract Only (B)"].iloc[0]
    assert ab_row["sample_size_N"] == 2 * 72
    assert ab_row["pearson_r"] > 0.99
    assert abs(ab_row["mae"] - 0.2) < 1e-4

    # Check A vs C
    ac_row = df_res[df_res["comparison_name"] == "Full Text (A) vs Masked Text (C)"].iloc[0]
    assert ac_row["sample_size_N"] == 2 * 72
    assert ac_row["pearson_r"] > 0.99
    assert ac_row["mae"] < 0.01
