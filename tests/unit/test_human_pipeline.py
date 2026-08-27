"""Unit tests for the complete single-human and multi-human analysis pipeline."""

import pytest
import pandas as pd
from pathlib import Path

from jmllm.analysis.run_human_analysis_pipeline import (
    ingest_human_evaluation_file,
    execute_human_analysis_pipeline,
)
from jmllm.analysis.human_evaluation import (
    validate_human_score_table,
    CANONICAL_PAPERS,
    ALL_FACTOR_COLS,
    compute_derived_summaries,
)


@pytest.fixture
def sample_h1_df():
    data = {"study_name": CANONICAL_PAPERS, "agent_": ["hpch_01"] * len(CANONICAL_PAPERS), "year_": [2020.0] * len(CANONICAL_PAPERS), "type_": ["empirical"] * len(CANONICAL_PAPERS)}
    for f in ALL_FACTOR_COLS:
        data[f] = [0.5 if i % 2 == 0 else None for i in range(len(CANONICAL_PAPERS))]
    df = pd.DataFrame(data)
    return compute_derived_summaries(df)


@pytest.fixture
def sample_h2_df():
    data = {"study_name": CANONICAL_PAPERS, "agent_": ["hpch_02"] * len(CANONICAL_PAPERS), "year_": [2020.0] * len(CANONICAL_PAPERS), "type_": ["empirical"] * len(CANONICAL_PAPERS)}
    for f in ALL_FACTOR_COLS:
        data[f] = [0.5 if i % 3 == 0 else None for i in range(len(CANONICAL_PAPERS))]
    df = pd.DataFrame(data)
    return compute_derived_summaries(df)


def test_single_human_pipeline_execution(tmp_path, sample_h1_df):
    h1_path = tmp_path / "hpch_01.csv"
    sample_h1_df.to_csv(h1_path, index=False)
    
    out_dir = tmp_path / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    res = execute_human_analysis_pipeline(
        rater_files=[("hpch_01", h1_path)],
        output_dir=out_dir
    )
    
    assert "coverage" in res
    assert "human_council" in res
    assert "audit_candidates" in res
    assert (out_dir / "supplement_human_coverage.csv").exists()
    assert (out_dir / "source_passage_audit_sheet.csv").exists()
    assert (out_dir / "supplement_human_council_agreement.csv").exists()


def test_multi_human_pipeline_execution(tmp_path, sample_h1_df, sample_h2_df):
    h1_path = tmp_path / "hpch_01.csv"
    h2_path = tmp_path / "hpch_02.csv"
    sample_h1_df.to_csv(h1_path, index=False)
    sample_h2_df.to_csv(h2_path, index=False)
    
    out_dir = tmp_path / "outputs_multi"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    res = execute_human_analysis_pipeline(
        rater_files=[("hpch_01", h1_path), ("hpch_02", h2_path)],
        output_dir=out_dir
    )
    
    assert "human_human" in res
    hh_df = res["human_human"]
    assert len(hh_df) == 1
    assert hh_df.iloc[0]["evaluator_A"] == "hpch_01"
    assert hh_df.iloc[0]["evaluator_B"] == "hpch_02"
    assert hh_df.iloc[0]["overlapping_cells_N"] > 0
    assert (out_dir / "supplement_human_human_agreement.csv").exists()
