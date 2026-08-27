"""Reproducible Permutation Benchmarks for Council Agreement (Figure 4).

Generates formal revision-parameterized null distributions for:
1. Full-shuffle: Permutes valid factor scores globally across all studies and factors.
2. Hypotheses-shuffle: Permutes valid factor scores strictly within each hypothesis block (H1, H2, H3).

Parameters are explicitly labeled as REVISION REPRODUCTION PARAMETERS (B=10,000, Seed=42).
"""

from pathlib import Path
from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[3]
CANONICAL_COUNCIL_PATH = REPO_ROOT / "content" / "tables" / "original_council" / "hpc_table_original_council.csv"
OUTPUT_NULL_PATH = REPO_ROOT / "content" / "tables" / "figure4_null_distributions.csv"


def run_figure4_permutation_benchmark(
    council_csv_path: Path = CANONICAL_COUNCIL_PATH,
    B: int = 10000,
    seed: int = 42,
    output_csv_path: Path = OUTPUT_NULL_PATH
) -> Tuple[Dict[str, Any], pd.DataFrame]:
    """Executes vectorized permutation benchmarks and exports empirical null summaries."""
    if not council_csv_path.exists():
        raise FileNotFoundError(f"Council file missing at {council_csv_path}")

    df = pd.read_csv(council_csv_path)
    active = df.dropna(subset=["LO-H1-avg"]).copy()
    
    factor_cols = [c for c in active.columns if c.startswith("LO-F") or c.startswith("GO-F")]
    models = sorted(active["agent_"].unique())
    studies = sorted(active["study_name"].unique())

    # Build 3D array: [studies (31), factors (72), models (8)]
    mat_3d = np.full((len(studies), len(factor_cols), len(models)), np.nan)
    study_idx = {s: i for i, s in enumerate(studies)}
    model_idx = {m: i for i, m in enumerate(models)}

    for _, row in active.iterrows():
        s_i = study_idx[row["study_name"]]
        m_i = model_idx[row["agent_"]]
        mat_3d[s_i, :, m_i] = row[factor_cols].values.astype(float)

    def calc_mean_pairwise_msd(m3d: np.ndarray) -> float:
        msds = []
        for i in range(len(models)):
            for j in range(i + 1, len(models)):
                diff = m3d[:, :, i] - m3d[:, :, j]
                valid = ~np.isnan(diff)
                if np.any(valid):
                    msds.append(np.mean(diff[valid] ** 2))
        return float(np.mean(msds))

    obs_msd = calc_mean_pairwise_msd(mat_3d)

    # 1. Full-shuffle
    np.random.seed(seed)
    mask = ~np.isnan(mat_3d)
    valid_vals = mat_3d[mask]

    null_full = np.zeros(B)
    for b in range(B):
        shuf_3d = np.full_like(mat_3d, np.nan)
        shuf_3d[mask] = np.random.permutation(valid_vals)
        null_full[b] = calc_mean_pairwise_msd(shuf_3d)

    # 2. Hypotheses-shuffle (blocks of 12 factors)
    blocks = [slice(0, 12), slice(12, 24), slice(24, 36), slice(36, 48), slice(48, 60), slice(60, 72)]
    null_hyp = np.zeros(B)
    for b in range(B):
        shuf_3d = np.full_like(mat_3d, np.nan)
        for blk in blocks:
            blk_sub = mat_3d[:, blk, :]
            blk_mask = ~np.isnan(blk_sub)
            shuf_blk = np.full_like(blk_sub, np.nan)
            shuf_blk[blk_mask] = np.random.permutation(blk_sub[blk_mask])
            shuf_3d[:, blk, :] = shuf_blk
        null_hyp[b] = calc_mean_pairwise_msd(shuf_3d)

    summary_records = [
        {
            "benchmark_name": "Observed Council Baseline",
            "permutation_type": "None (Empirical)",
            "permutation_count_B": 0,
            "random_seed": "N/A",
            "provenance_status": "FROZEN_OBSERVED",
            "mean_msd": round(obs_msd, 4),
            "sd_msd": 0.0,
            "ci_95_lower": round(obs_msd, 4),
            "ci_95_upper": round(obs_msd, 4),
            "empirical_p_value": "N/A",
            "tail_direction": "N/A"
        },
        {
            "benchmark_name": "Figure 4 Full-Shuffle Null",
            "permutation_type": "Global Factor Permutation",
            "permutation_count_B": B,
            "random_seed": seed,
            "provenance_status": "REVISION_REPRODUCTION_PARAMETERS",
            "mean_msd": round(float(np.mean(null_full)), 4),
            "sd_msd": round(float(np.std(null_full)), 4),
            "ci_95_lower": round(float(np.percentile(null_full, 2.5)), 4),
            "ci_95_upper": round(float(np.percentile(null_full, 97.5)), 4),
            "empirical_p_value": f"{(np.sum(null_full <= obs_msd) + 1) / (B + 1):.6f}",
            "tail_direction": "lower_tail (null_msd <= obs_msd)"
        },
        {
            "benchmark_name": "Figure 4 Hypotheses-Shuffle Null",
            "permutation_type": "Within-Hypothesis Block Permutation",
            "permutation_count_B": B,
            "random_seed": seed,
            "provenance_status": "REVISION_REPRODUCTION_PARAMETERS",
            "mean_msd": round(float(np.mean(null_hyp)), 4),
            "sd_msd": round(float(np.std(null_hyp)), 4),
            "ci_95_lower": round(float(np.percentile(null_hyp, 2.5)), 4),
            "ci_95_upper": round(float(np.percentile(null_hyp, 97.5)), 4),
            "empirical_p_value": f"{(np.sum(null_hyp <= obs_msd) + 1) / (B + 1):.6f}",
            "tail_direction": "lower_tail (null_msd <= obs_msd)"
        }
    ]

    out_df = pd.DataFrame(summary_records)
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(output_csv_path, index=False)
    
    summary_dict = {r["benchmark_name"]: r for r in summary_records}
    return summary_dict, out_df


if __name__ == "__main__":
    res, df_res = run_figure4_permutation_benchmark()
    print(df_res.to_string(index=False))
