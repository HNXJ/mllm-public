"""Descriptive Analysis for the 54-Call Evidence-vs-Prior Experiment.

Calculates prespecified comparisons:
- Condition A (Full-Text) vs Condition B (Abstract-Only): Valid N, Pearson r, MAE
- Condition A (Full-Text) vs Condition C (Masked Text): Valid N, Pearson r, MAE
- Completeness and null rates by condition
- Replicate reliability across repeats R1, R2, R3 by condition
"""

from pathlib import Path
from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd
from scipy import stats

REPO_ROOT = Path(__file__).resolve().parents[3]
SCORES_PATH = REPO_ROOT / "content" / "tables" / "evidence_prior_scores_54.csv"
OUTPUT_SUMMARY_PATH = REPO_ROOT / "content" / "tables" / "evidence_prior_analysis_summary.csv"


def analyze_evidence_prior_results(
    scores_path: Path = SCORES_PATH,
    output_path: Path = OUTPUT_SUMMARY_PATH
) -> Tuple[Dict[str, Any], pd.DataFrame]:
    """Analyzes the 54-call ablation scores table and exports machine-readable summary."""
    if not scores_path.exists():
        raise FileNotFoundError(f"Scores file missing at {scores_path}")

    df = pd.read_csv(scores_path)
    # Simplify condition names
    df["cond_key"] = df["condition"].map({
        "Condition A (Full)": "Cond_A",
        "Condition B (Abstract)": "Cond_B",
        "Condition C (Masked)": "Cond_C"
    })

    # Repeat-averaged scores per paper x factor x context cell
    piv_cell = df.groupby(["paper_id", "factor", "context", "cond_key"])["score"].mean().unstack("cond_key")

    # 1. Condition A vs Condition B (Full vs Abstract)
    sub_ab = piv_cell[["Cond_A", "Cond_B"]].dropna()
    n_ab = len(sub_ab)
    r_ab, p_ab = stats.pearsonr(sub_ab["Cond_A"], sub_ab["Cond_B"]) if n_ab > 1 else (np.nan, np.nan)
    mae_ab = float((sub_ab["Cond_A"] - sub_ab["Cond_B"]).abs().mean()) if n_ab > 0 else np.nan

    # 2. Condition A vs Condition C (Full vs Masked)
    sub_ac = piv_cell[["Cond_A", "Cond_C"]].dropna()
    n_ac = len(sub_ac)
    r_ac, p_ac = stats.pearsonr(sub_ac["Cond_A"], sub_ac["Cond_C"]) if n_ac > 1 else (np.nan, np.nan)
    mae_ac = float((sub_ac["Cond_A"] - sub_ac["Cond_C"]).abs().mean()) if n_ac > 0 else np.nan

    # 3. Completeness & null rates per condition
    total_slots = 6 * 72 * 3  # 6 papers * 72 factor cells * 3 repeats = 1296 possible slots per condition
    comp_stats = {}
    for c_key in ["Cond_A", "Cond_B", "Cond_C"]:
        c_sub = df[df["cond_key"] == c_key]
        n_assigned = c_sub["score"].notna().sum()
        comp_stats[c_key] = {
            "total_slots": len(c_sub),
            "valid_scores": int(n_assigned),
            "missing_nulls": int(len(c_sub) - n_assigned),
            "coverage_pct": round(float(n_assigned / len(c_sub) * 100), 2) if len(c_sub) > 0 else 0.0
        }

    # 4. Repeat reliability per condition (mean pairwise r and MAE across 3 runs)
    rep_stats = {}
    for c_key in ["Cond_A", "Cond_B", "Cond_C"]:
        c_sub = df[df["cond_key"] == c_key]
        piv_rep = c_sub.pivot_table(index=["paper_id", "factor", "context"], columns="repeat", values="score").dropna()
        if len(piv_rep) > 1 and 1 in piv_rep and 2 in piv_rep and 3 in piv_rep:
            rs = [stats.pearsonr(piv_rep[a], piv_rep[b])[0] for a, b in [(1,2), (1,3), (2,3)]]
            maes = [(piv_rep[a] - piv_rep[b]).abs().mean() for a, b in [(1,2), (1,3), (2,3)]]
            rep_stats[c_key] = {
                "n_triples": len(piv_rep),
                "mean_r": round(float(np.mean(rs)), 4),
                "mean_mae": round(float(np.mean(maes)), 4)
            }
        else:
            rep_stats[c_key] = {"n_triples": len(piv_rep), "mean_r": np.nan, "mean_mae": np.nan}

    records = [
        {
            "comparison_name": "Full Text (A) vs Abstract Only (B)",
            "sample_size_N": n_ab,
            "observational_unit": "Repeat-Averaged Factor Cell (Descriptive)",
            "pearson_r": round(float(r_ab), 4) if pd.notna(r_ab) else np.nan,
            "mae": round(float(mae_ab), 4) if pd.notna(mae_ab) else np.nan,
            "scientific_interpretation": "Measures scoring sensitivity to restriction of available paper-specific evidence."
        },
        {
            "comparison_name": "Full Text (A) vs Masked Text (C)",
            "sample_size_N": n_ac,
            "observational_unit": "Repeat-Averaged Factor Cell (Descriptive)",
            "pearson_r": round(float(r_ac), 4) if pd.notna(r_ac) else np.nan,
            "mae": round(float(mae_ac), 4) if pd.notna(mae_ac) else np.nan,
            "scientific_interpretation": "Measures scoring sensitivity to removal of explicit publication identity."
        }
    ]

    out_df = pd.DataFrame(records)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(output_path, index=False)

    summary = {
        "primary_comparisons": records,
        "completeness_by_condition": comp_stats,
        "repeat_reliability_by_condition": rep_stats
    }
    return summary, out_df


if __name__ == "__main__":
    summary, df_summary = analyze_evidence_prior_results()
    print(df_summary.to_string(index=False))
