"""Complete Pipeline Script for Human Evaluation Ingestion and Concordance Analysis.

Supports:
1. Single-Human Mode (K=1, Interim Readiness): Evaluates H1 vs Council, generates descriptive agreement and candidate source-audit list.
2. Multi-Human Mode (K>=2, Final Resubmission): Computes inter-rater reliability (H1 vs H2), builds consensus, evaluates consensus vs Council on n>=1 and n>=2 strata.

All outputs and provenance records are saved deterministically.
"""

import shutil
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import numpy as np
import pandas as pd

from jmllm.analysis.human_evaluation import (
    validate_human_score_table,
    compute_pairwise_agreement,
    build_human_consensus,
    load_council_consensus,
    compute_human_council_agreement,
    generate_disagreement_report,
    CANONICAL_PAPERS,
    ALL_FACTOR_COLS
)

REPO_ROOT = Path(__file__).resolve().parents[3]
EXPERTS_DIR = REPO_ROOT / "content" / "tables" / "experts"
RAW_EXPERTS_DIR = EXPERTS_DIR / "raw"
TABLES_DIR = REPO_ROOT / "content" / "tables"


def ingest_human_evaluation_file(
    source_file_path: Path,
    evaluator_id: str = "hpch_01"
) -> Tuple[bool, str, pd.DataFrame]:
    """Preserves raw file, validates schema, and writes canonical normalized table."""
    if not source_file_path.exists():
        raise FileNotFoundError(f"Source file missing at {source_file_path}")

    # 1. Compute SHA-256 of raw input
    raw_bytes = source_file_path.read_bytes()
    raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()

    # 2. Archive raw file
    RAW_EXPERTS_DIR.mkdir(parents=True, exist_ok=True)
    raw_archive_path = RAW_EXPERTS_DIR / f"{evaluator_id}_raw.csv"
    shutil.copy2(source_file_path, raw_archive_path)

    # 3. Validate and recompute derived summaries
    df_raw = pd.read_csv(source_file_path)
    is_valid, errors, validated_df = validate_human_score_table(df_raw, expected_agent=None)

    if not is_valid:
        raise ValueError(f"Human evaluation validation failed for {evaluator_id}: {errors}")

    # Set canonical agent_ column
    validated_df["agent_"] = evaluator_id

    # 4. Save canonical validated table
    canonical_dest = EXPERTS_DIR / f"{evaluator_id}.csv"
    validated_df.to_csv(canonical_dest, index=False)

    return is_valid, raw_sha256, validated_df


def execute_human_analysis_pipeline(
    rater_files: List[Tuple[str, Path]] = None,
    output_dir: Path = TABLES_DIR
) -> Dict[str, Any]:
    """Executes the complete single-human or multi-human analysis workflow."""
    if rater_files is None:
        # Auto-discover available human evaluations in content/tables/experts/
        rater_files = []
        for r_id in ["hpch_01", "hpch_02", "hpch_03"]:
            r_path = EXPERTS_DIR / f"{r_id}.csv"
            if r_path.exists():
                rater_files.append((r_id, r_path))

    if not rater_files:
        raise FileNotFoundError("No valid human evaluator files found in content/tables/experts/")

    # 1. Load validated tables
    loaded_raters = {}
    coverage_records = []
    total_slots = len(CANONICAL_PAPERS) * len(ALL_FACTOR_COLS)

    for r_id, r_path in rater_files:
        df_r = pd.read_csv(r_path)
        is_valid, errors, v_df = validate_human_score_table(df_r)
        if not is_valid:
            raise ValueError(f"Validation error in {r_id}: {errors}")
        loaded_raters[r_id] = v_df
        
        # Coverage statistics
        numeric_scores = v_df[ALL_FACTOR_COLS].apply(pd.to_numeric, errors="coerce")
        n_valid = int(numeric_scores.notna().sum().sum())
        n_null = int(numeric_scores.isna().sum().sum())
        coverage_records.append({
            "evaluator_id": r_id,
            "source_file": str(r_path.name),
            "papers_covered": len(v_df["study_name"].unique()),
            "total_slots": total_slots,
            "valid_scores": n_valid,
            "missing_nulls": n_null,
            "coverage_percentage": round(float(n_valid / total_slots * 100), 2)
        })

    coverage_df = pd.DataFrame(coverage_records)
    coverage_df.to_csv(output_dir / "supplement_human_coverage.csv", index=False)

    # 2. Build consensus & counts
    consensus_df, counts_df = build_human_consensus(list(loaded_raters.values()))
    consensus_df.to_csv(output_dir / "human_consensus_scores.csv", index=False)
    counts_df.to_csv(output_dir / "human_rater_counts.csv", index=False)

    # 3. Inter-rater pairwise agreement (if K >= 2)
    human_human_records = []
    r_ids = list(loaded_raters.keys())
    if len(r_ids) >= 2:
        for i, id1 in enumerate(r_ids):
            for id2 in r_ids[i+1:]:
                res = compute_pairwise_agreement(loaded_raters[id1], loaded_raters[id2], id1, id2)
                human_human_records.append({
                    "evaluator_A": id1,
                    "evaluator_B": id2,
                    "overlapping_cells_N": res["overlapping_n"],
                    "pearson_r": res["pearson_r"],
                    "mae": res["mae"],
                    "mean_signed_difference": res["mean_signed_difference"],  # rater A - rater B
                    "directional_eligible_N": res["eligible_directional_n"],
                    "excluded_zero_N": res["excluded_zero_n"],
                    "concordant_N": res["concordant_directional_n"],
                    "directional_concordance_pct": round(res["directional_concordance_proportion"] * 100, 2) if pd.notna(res["directional_concordance_proportion"]) else np.nan
                })
    else:
        # K=1 placeholder schema
        human_human_records.append({
            "evaluator_A": r_ids[0],
            "evaluator_B": "N/A (Single Evaluator Mode)",
            "overlapping_cells_N": np.nan,
            "pearson_r": np.nan,
            "mae": np.nan,
            "mean_signed_difference": np.nan,
            "directional_eligible_N": np.nan,
            "excluded_zero_N": np.nan,
            "concordant_N": np.nan,
            "directional_concordance_pct": np.nan
        })

    human_human_df = pd.DataFrame(human_human_records)
    human_human_df.to_csv(output_dir / "supplement_human_human_agreement.csv", index=False)

    # 4. Load Council Consensus and evaluate Human-vs-Council Agreement
    council_df = load_council_consensus()
    human_council_res = compute_human_council_agreement(
        human_consensus_df=consensus_df,
        council_df=council_df,
        coverage_counts_df=counts_df,
        min_raters=1
    )

    council_agreement_records = [
        {
            "stratum": "All Scored Cells (n_human_raters >= 1)",
            "evaluator_count_K": len(loaded_raters),
            "sample_size_N": human_council_res["n_valid_cells"],
            "observational_unit": "Factor Cell (Descriptive)",
            "pearson_r": human_council_res["pearson_r"],
            "mae": human_council_res["mae"],
            "paper_sample_N": human_council_res["paper_n"],
            "paper_spearman_rho": human_council_res["paper_spearman_rho"],
            "paper_spearman_p": human_council_res["paper_spearman_p"]
        }
    ]

    # If K >= 2, also evaluate n >= 2 stratum
    if len(loaded_raters) >= 2:
        hc_n2 = compute_human_council_agreement(
            human_consensus_df=consensus_df,
            council_df=council_df,
            coverage_counts_df=counts_df,
            min_raters=2
        )
        council_agreement_records.append({
            "stratum": "Consensus Cells (n_human_raters >= 2)",
            "evaluator_count_K": len(loaded_raters),
            "sample_size_N": hc_n2["n_valid_cells"],
            "observational_unit": "Factor Cell (Descriptive)",
            "pearson_r": hc_n2["pearson_r"],
            "mae": hc_n2["mae"],
            "paper_sample_N": hc_n2["paper_n"],
            "paper_spearman_rho": hc_n2["paper_spearman_rho"],
            "paper_spearman_p": hc_n2["paper_spearman_p"]
        })

    council_agreement_df = pd.DataFrame(council_agreement_records)
    council_agreement_df.to_csv(output_dir / "supplement_human_council_agreement.csv", index=False)

    # 5. Generate Disagreement Report and Source-Passage Audit Candidate Sheet
    disagreements_df = generate_disagreement_report(consensus_df, council_df)
    disagreements_df.to_csv(output_dir / "human_council_disagreements.csv", index=False)

    # Prepare blank source-passage audit sheet
    audit_records = []
    for _, row in disagreements_df.iterrows():
        audit_records.append({
            "paper_id": row["study_name"],
            "context": row["context"],
            "factor": row["factor_column"],
            "human_score": row["human_score"],
            "council_score": row["council_score"],
            "absolute_difference": row["absolute_difference"],
            "audit_priority": "High (|diff| >= 0.50)" if row["is_diagnostic_divergence"] else "Standard",
            "source_markdown": f"{row['study_name']}-vllm-deepread_compressed.md",
            "source_location": "",
            "source_evidence_summary": "",
            "supports_human_direction": "",
            "supports_council_direction": "",
            "ambiguous_or_insufficient": "",
            "adjudicator_id": "",
            "adjudication_note": ""
        })

    audit_df = pd.DataFrame(audit_records)
    audit_df.to_csv(output_dir / "source_passage_audit_sheet.csv", index=False)

    return {
        "coverage": coverage_df,
        "human_human": human_human_df,
        "human_council": council_agreement_df,
        "disagreements": disagreements_df,
        "audit_candidates": audit_df
    }


if __name__ == "__main__":
    # Ingest H1 from Downloads if available
    h1_raw = Path("/Users/hamednejat/Downloads/hpc_table_inprogress - HumanExpert1.csv")
    if h1_raw.exists():
        is_val, sha, v_df = ingest_human_evaluation_file(h1_raw, "hpch_01")
        print(f"H1 Ingestion Success: SHA-256 = {sha}")
    
    res = execute_human_analysis_pipeline()
    print("Human evaluation pipeline executed successfully.")
