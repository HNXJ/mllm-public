"""Human Evaluation Validation and Concordance Analysis Harness.

Dedicated module for ingesting, validating, and analyzing independent human domain expert ratings
and computing multi-rater reliability and human-vs-council agreement for the Scientific Reports revision.

Core Principles:
1. Strict schema and domain validation (no silent coercion).
2. Strict missingness semantics: null = unaddressed/unevaluable, 0.0 = neutral evidence.
3. Zero-imputation is strictly prohibited.
4. Descriptive cell concordance is distinguished from population-level study inference.
"""

from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import numpy as np
import pandas as pd
from scipy import stats

REPO_ROOT = Path(__file__).resolve().parents[3]

CANONICAL_PAPERS = [
    "Attinger2017", "Bakhtiari2021", "Bastos2012", "Bastos2020", "Bekinschtein2009",
    "Chao2018", "Friston2010", "Furutachi2024", "Garret2020", "Greedy2022",
    "Hertag2020", "Jiang&Rao2024", "Keller2012", "Keller2018", "Kiebel2008",
    "LaoRodriguez2023", "LeeMejias2025", "Mikulasch2023", "Nejad2025", "Payeur2021",
    "Rao&Ballard1999", "Rao2024", "Sacramento2018", "Spratling2008", "Spratling2010",
    "Srinivasan1982", "VanDerveer2021", "Wacongne2011", "Wacongne2012", "Westerberg&Xiong2025",
    "Yamins2014"
]

FACTOR_COLS_LO = [f"LO-F{i:02d}" for i in range(1, 37)]
FACTOR_COLS_GO = [f"GO-F{i:02d}" for i in range(1, 37)]
ALL_FACTOR_COLS = FACTOR_COLS_LO + FACTOR_COLS_GO

SUMMARY_COLS = [
    "LO-count", "GO-count",
    "LO-H1-avg", "LO-H1-std", "LO-H2-avg", "LO-H2-std", "LO-H3-avg", "LO-H3-std",
    "GO-H1-avg", "GO-H1-std", "GO-H2-avg", "GO-H2-std", "GO-H3-avg", "GO-H3-std"
]

METADATA_COLS = ["study_name", "agent_", "year_", "type_"]
FULL_90_COLS = METADATA_COLS + SUMMARY_COLS[:2] + SUMMARY_COLS[2:] + FACTOR_COLS_LO + FACTOR_COLS_GO


def compute_derived_summaries(df_factors: pd.DataFrame) -> pd.DataFrame:
    """Deterministically computes derived counts, averages, and standard deviations from 72 factor scores."""
    df_out = df_factors.copy()
    
    # LO summaries
    lo_scores = df_out[FACTOR_COLS_LO]
    df_out["LO-count"] = lo_scores.notna().sum(axis=1)
    
    lo_h1 = df_out[[f"LO-F{i:02d}" for i in range(1, 13)]]
    lo_h2 = df_out[[f"LO-F{i:02d}" for i in range(13, 25)]]
    lo_h3 = df_out[[f"LO-F{i:02d}" for i in range(25, 37)]]
    
    df_out["LO-H1-avg"] = lo_h1.mean(axis=1)
    df_out["LO-H1-std"] = lo_h1.std(axis=1, ddof=1)
    df_out["LO-H2-avg"] = lo_h2.mean(axis=1)
    df_out["LO-H2-std"] = lo_h2.std(axis=1, ddof=1)
    df_out["LO-H3-avg"] = lo_h3.mean(axis=1)
    df_out["LO-H3-std"] = lo_h3.std(axis=1, ddof=1)
    
    # GO summaries
    go_scores = df_out[FACTOR_COLS_GO]
    df_out["GO-count"] = go_scores.notna().sum(axis=1)
    
    go_h1 = df_out[[f"GO-F{i:02d}" for i in range(1, 13)]]
    go_h2 = df_out[[f"GO-F{i:02d}" for i in range(13, 25)]]
    go_h3 = df_out[[f"GO-F{i:02d}" for i in range(25, 37)]]
    
    df_out["GO-H1-avg"] = go_h1.mean(axis=1)
    df_out["GO-H1-std"] = go_h1.std(axis=1, ddof=1)
    df_out["GO-H2-avg"] = go_h2.mean(axis=1)
    df_out["GO-H2-std"] = go_h2.std(axis=1, ddof=1)
    df_out["GO-H3-avg"] = go_h3.mean(axis=1)
    df_out["GO-H3-std"] = go_h3.std(axis=1, ddof=1)
    
    return df_out


CANONICAL_STUDY_MAP = {
    "Chao2019": "Chao2018",
    "JiangRao2024": "Jiang&Rao2024",
    "RaoBallard1999": "Rao&Ballard1999",
    "Wacogne2012": "Wacongne2012",
    "Westerberg2025": "Westerberg&Xiong2025",
}


def validate_human_score_table(
    df: pd.DataFrame,
    expected_agent: Optional[str] = None,
    normalize_study_aliases: bool = True
) -> Tuple[bool, List[str], Optional[pd.DataFrame]]:
    """Strict schema, canonical identifier, and domain validator for raw/formatted human evaluation CSVs."""
    errors = []
    
    if not isinstance(df, pd.DataFrame):
        return False, ["Input is not a valid pandas DataFrame"], None

    # Check study_name column
    if "study_name" not in df.columns:
        errors.append("Missing required primary key column: 'study_name'")
        return False, errors, None

    cleaned_df = df.copy()
    if normalize_study_aliases:
        cleaned_df["study_name"] = cleaned_df["study_name"].replace(CANONICAL_STUDY_MAP)

    # Validate paper count and uniqueness
    studies_present = cleaned_df["study_name"].tolist()
    if len(studies_present) != len(CANONICAL_PAPERS):
        errors.append(f"Expected exactly {len(CANONICAL_PAPERS)} rows, found {len(studies_present)}")
        
    missing_studies = set(CANONICAL_PAPERS) - set(studies_present)
    if missing_studies:
        errors.append(f"Missing canonical studies: {sorted(list(missing_studies))}")
        
    unknown_studies = set(studies_present) - set(CANONICAL_PAPERS)
    if unknown_studies:
        errors.append(f"Unknown or non-canonical study names: {sorted(list(unknown_studies))}")
        
    duplicates = cleaned_df[cleaned_df.duplicated(subset=["study_name"])]["study_name"].tolist()
    if duplicates:
        errors.append(f"Duplicate study entries found: {duplicates}")

    # Validate agent_ if specified
    if expected_agent and "agent_" in cleaned_df.columns:
        agents = cleaned_df["agent_"].dropna().unique()
        if len(agents) > 0 and (len(agents) > 1 or agents[0] != expected_agent):
            errors.append(f"Expected agent '{expected_agent}', found: {list(agents)}")

    # Validate 72 factor score columns
    missing_factors = set(ALL_FACTOR_COLS) - set(cleaned_df.columns)
    if missing_factors:
        errors.append(f"Missing factor columns: {sorted(list(missing_factors))}")
        return False, errors, None

    # Validate factor score values (must be float in [-1.0, 1.0] or null/NaN)
    cleaned_df = df.copy()
    for col in ALL_FACTOR_COLS:
        raw_vals = cleaned_df[col]
        numeric_vals = pd.to_numeric(raw_vals, errors="coerce")
        
        # Check for invalid non-null non-numeric strings
        invalid_mask = raw_vals.notna() & numeric_vals.isna()
        if invalid_mask.any():
            bad_tokens = raw_vals[invalid_mask].unique().tolist()
            errors.append(f"Column '{col}' contains non-numeric invalid values: {bad_tokens}")
            
        # Check range [-1.0, 1.0]
        out_of_bounds = (numeric_vals < -1.0) | (numeric_vals > 1.0)
        if out_of_bounds.any():
            bad_scores = numeric_vals[out_of_bounds].tolist()
            errors.append(f"Column '{col}' contains out-of-bounds scores outside [-1.0, 1.0]: {bad_scores}")
            
        cleaned_df[col] = numeric_vals

    if errors:
        return False, errors, None

    # Deterministically re-compute derived summaries to guarantee mathematical integrity
    canonical_order_df = cleaned_df.set_index("study_name").reindex(CANONICAL_PAPERS).reset_index()
    if "agent_" not in canonical_order_df.columns:
        canonical_order_df["agent_"] = expected_agent or "human_evaluator"
    if "year_" not in canonical_order_df.columns:
        canonical_order_df["year_"] = 2020.0
    if "type_" not in canonical_order_df.columns:
        canonical_order_df["type_"] = "empirical"

    recomputed = compute_derived_summaries(canonical_order_df)
    
    ordered_cols = [
        "study_name", "agent_", "year_", "type_",
        "LO-count", "GO-count",
        "LO-H1-avg", "LO-H1-std", "LO-H2-avg", "LO-H2-std", "LO-H3-avg", "LO-H3-std",
        "GO-H1-avg", "GO-H1-std", "GO-H2-avg", "GO-H2-std", "GO-H3-avg", "GO-H3-std"
    ] + ALL_FACTOR_COLS
    
    recomputed = recomputed[ordered_cols]
    return True, [], recomputed


def compute_pairwise_agreement(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    rater1_name: str = "Rater1",
    rater2_name: str = "Rater2"
) -> Dict[str, Any]:
    """Computes descriptive pairwise agreement metrics across overlapping factor cells between two raters."""
    d1 = df1.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    d2 = df2.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    
    v1 = d1.values.flatten().astype(float)
    v2 = d2.values.flatten().astype(float)
    
    total_slots = len(v1)  # 31 * 72 = 2,232
    scored_r1 = int(np.sum(~np.isnan(v1)))
    scored_r2 = int(np.sum(~np.isnan(v2)))
    
    overlap_mask = ~np.isnan(v1) & ~np.isnan(v2)
    overlapping_n = int(np.sum(overlap_mask))
    
    if overlapping_n < 2:
        return {
            "rater1": rater1_name,
            "rater2": rater2_name,
            "total_slots": total_slots,
            "scored_r1": scored_r1,
            "scored_r2": scored_r2,
            "overlapping_n": overlapping_n,
            "pearson_r": np.nan,
            "pearson_p": np.nan,
            "mae": np.nan,
            "msd": np.nan,
            "eligible_directional_n": 0,
            "excluded_zero_n": 0,
            "concordant_directional_n": 0,
            "directional_concordance_proportion": np.nan,
            "inferential_warning": "Factor-cell agreement metrics characterize descriptive concordance across scored cells and do not treat the cells as independent biological/study replicates for population-level inference."
        }
        
    v1_ov = v1[overlap_mask]
    v2_ov = v2[overlap_mask]
    
    # Continuous correlation & error metrics
    std1, std2 = np.std(v1_ov), np.std(v2_ov)
    if std1 > 0 and std2 > 0:
        r, p = stats.pearsonr(v1_ov, v2_ov)
    else:
        r, p = np.nan, np.nan
        
    mae = float(np.mean(np.abs(v1_ov - v2_ov)))
    msd = float(np.mean((v1_ov - v2_ov) ** 2))
    
    # Directional concordance with explicit denominators
    nonzero_mask = (v1_ov != 0.0) & (v2_ov != 0.0)
    eligible_directional_n = int(np.sum(nonzero_mask))
    excluded_zero_n = int(overlapping_n - eligible_directional_n)
    
    if eligible_directional_n > 0:
        sign_match = np.sign(v1_ov[nonzero_mask]) == np.sign(v2_ov[nonzero_mask])
        concordant_directional_n = int(np.sum(sign_match))
        directional_prop = float(concordant_directional_n / eligible_directional_n)
    else:
        concordant_directional_n = 0
        directional_prop = np.nan
        
    return {
        "rater1": rater1_name,
        "rater2": rater2_name,
        "total_slots": total_slots,
        "scored_r1": scored_r1,
        "scored_r2": scored_r2,
        "overlapping_n": overlapping_n,
        "pearson_r": round(float(r), 4) if not np.isnan(r) else np.nan,
        "pearson_p": float(p) if not np.isnan(p) else np.nan,
        "mae": round(mae, 4),
        "mean_signed_difference": round(msd, 4),  # rater1 - rater2
        "msd": round(msd, 4),  # legacy alias for backwards compatibility
        "eligible_directional_n": eligible_directional_n,
        "excluded_zero_n": excluded_zero_n,
        "concordant_directional_n": concordant_directional_n,
        "directional_concordance_proportion": round(directional_prop, 4) if not np.isnan(directional_prop) else np.nan,
        "inferential_warning": "Factor-cell agreement metrics characterize descriptive concordance across scored cells and do not treat the cells as independent biological/study replicates for population-level inference."
    }


def build_human_consensus(
    human_dfs: List[pd.DataFrame]
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Constructs human consensus scores by averaging non-null ratings and generates rater coverage counts."""
    aligned_mats = []
    for df in human_dfs:
        aligned = df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
        aligned_mats.append(aligned.values.astype(float))
        
    # Stack into 3D array: [K_raters, 31_papers, 72_factors]
    stack = np.stack(aligned_mats, axis=0)
    
    # Compute counts of valid human ratings per cell
    valid_mask = ~np.isnan(stack)
    rater_counts = np.sum(valid_mask, axis=0)
    
    # Compute mean over valid raters with explicit NaN where count == 0
    with np.errstate(divide="ignore", invalid="ignore"):
        sum_scores = np.nansum(stack, axis=0)
        consensus_values = np.where(rater_counts > 0, sum_scores / rater_counts, np.nan)
        
    consensus_df = pd.DataFrame(consensus_values, index=CANONICAL_PAPERS, columns=ALL_FACTOR_COLS).reset_index()
    consensus_df = consensus_df.rename(columns={"index": "study_name"})
    consensus_df["agent_"] = "human_consensus"
    consensus_df["year_"] = 2026.0
    consensus_df["type_"] = "human_panel"
    
    consensus_df = compute_derived_summaries(consensus_df)
    
    counts_df = pd.DataFrame(rater_counts, index=CANONICAL_PAPERS, columns=ALL_FACTOR_COLS).reset_index()
    counts_df = counts_df.rename(columns={"index": "study_name"})
    
    return consensus_df, counts_df


CANONICAL_COUNCIL_PATH = REPO_ROOT / "content" / "tables" / "original_council" / "hpc_table_original_council.csv"


def load_council_consensus(council_csv_path: Optional[Path] = None) -> pd.DataFrame:
    """Extracts authoritative multi-model council consensus by averaging across active council models."""
    if council_csv_path is None:
        council_csv_path = CANONICAL_COUNCIL_PATH
    if not council_csv_path.exists():
        raise FileNotFoundError(f"Council file missing at {council_csv_path}")
        
    df_raw = pd.read_csv(council_csv_path)
    active = df_raw.dropna(subset=["LO-H1-avg"]).copy()
    
    factor_cols = [c for c in active.columns if c in ALL_FACTOR_COLS]
    council_agg = active.groupby("study_name")[factor_cols].mean().reindex(CANONICAL_PAPERS).reset_index()
    council_agg["agent_"] = "council_consensus_8m"
    council_agg["year_"] = 2026.0
    council_agg["type_"] = "llm_council"
    
    return compute_derived_summaries(council_agg)


def compute_human_council_agreement(
    human_consensus_df: pd.DataFrame,
    council_df: pd.DataFrame,
    coverage_counts_df: Optional[pd.DataFrame] = None,
    min_raters: int = 1
) -> Dict[str, Any]:
    """Computes concordance between human consensus and autonomous LLM council across specified coverage strata."""
    h_aligned = human_consensus_df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    c_aligned = council_df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    
    h_vals = h_aligned.values.flatten().astype(float)
    c_vals = c_aligned.values.flatten().astype(float)
    
    if coverage_counts_df is not None:
        cnt_aligned = coverage_counts_df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
        cnt_vals = cnt_aligned.values.flatten().astype(int)
        rater_filter = cnt_vals >= min_raters
    else:
        rater_filter = np.ones_like(h_vals, dtype=bool)
        
    valid_mask = ~np.isnan(h_vals) & ~np.isnan(c_vals) & rater_filter
    n_valid = int(np.sum(valid_mask))
    
    if n_valid < 2:
        return {
            "stratum": f"min_human_raters_{min_raters}",
            "n_valid_cells": n_valid,
            "pearson_r": np.nan,
            "mae": np.nan,
            "paper_spearman_rho": np.nan,
            "note": "Insufficient valid overlapping factor cells.",
            "inferential_warning": "Factor-cell agreement metrics characterize descriptive concordance across scored cells and do not treat the cells as independent biological/study replicates for population-level inference."
        }
        
    h_sub = h_vals[valid_mask]
    c_sub = c_vals[valid_mask]
    
    r, p_r = stats.pearsonr(h_sub, c_sub)
    mae = float(np.mean(np.abs(h_sub - c_sub)))
    
    h_paper_means = human_consensus_df.set_index("study_name")[ALL_FACTOR_COLS].mean(axis=1)
    c_paper_means = council_df.set_index("study_name")[ALL_FACTOR_COLS].mean(axis=1)
    
    p_df = pd.DataFrame({"human": h_paper_means, "council": c_paper_means}).dropna()
    if len(p_df) >= 3:
        rho, p_rho = stats.spearmanr(p_df["human"], p_df["council"])
    else:
        rho, p_rho = np.nan, np.nan
        
    return {
        "stratum": f"min_human_raters_{min_raters}",
        "n_valid_cells": n_valid,
        "pearson_r": round(float(r), 4),
        "pearson_p": float(p_r),
        "mae": round(mae, 4),
        "paper_n": int(len(p_df)),
        "paper_spearman_rho": round(float(rho), 4) if not np.isnan(rho) else np.nan,
        "paper_spearman_p": float(p_rho) if not np.isnan(p_rho) else np.nan,
        "inferential_warning": "Factor-cell agreement metrics characterize descriptive concordance across scored cells and do not treat the cells as independent biological/study replicates for population-level inference."
    }


def generate_disagreement_report(
    human_df: pd.DataFrame,
    council_df: pd.DataFrame,
    diagnostic_threshold: float = 0.50
) -> pd.DataFrame:
    """Ranks and extracts factor-cell disagreements between human ratings and council consensus."""
    h_aligned = human_df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    c_aligned = council_df.set_index("study_name").reindex(CANONICAL_PAPERS)[ALL_FACTOR_COLS]
    
    records = []
    for study in CANONICAL_PAPERS:
        for factor_col in ALL_FACTOR_COLS:
            context, factor_id = factor_col.split("-")
            h_val = h_aligned.loc[study, factor_col]
            c_val = c_aligned.loc[study, factor_col]
            
            if pd.notna(h_val) and pd.notna(c_val):
                diff = float(h_val - c_val)
                abs_diff = float(abs(diff))
                records.append({
                    "study_name": study,
                    "context": context,
                    "factor_column": factor_col,
                    "human_score": round(float(h_val), 3),
                    "council_score": round(float(c_val), 3),
                    "signed_difference": round(diff, 3),
                    "absolute_difference": round(abs_diff, 3),
                    "is_diagnostic_divergence": abs_diff >= diagnostic_threshold
                })
                
    out_df = pd.DataFrame(records)
    if not out_df.empty:
        out_df = out_df.sort_values(by="absolute_difference", ascending=False).reset_index(drop=True)
    return out_df
