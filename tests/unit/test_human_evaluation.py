"""Unit tests for the frozen human evaluation validation and analysis harness."""

import pytest
import numpy as np
import pandas as pd
from pathlib import Path

from jmllm.analysis.human_evaluation import (
    CANONICAL_PAPERS,
    FACTOR_COLS_LO,
    FACTOR_COLS_GO,
    ALL_FACTOR_COLS,
    validate_human_score_table,
    compute_pairwise_agreement,
    build_human_consensus,
    load_council_consensus,
    compute_human_council_agreement,
    generate_disagreement_report,
    compute_derived_summaries,
)


@pytest.fixture
def valid_human_df():
    """Generates a valid 31-paper human evaluation dataframe with sparse scores."""
    rows = []
    np.random.seed(123)
    for study in CANONICAL_PAPERS:
        row = {
            "study_name": study,
            "agent_": "hpch_test1",
            "year_": 2020.0,
            "type_": "empirical"
        }
        for col in ALL_FACTOR_COLS:
            # 20% chance of being scored
            if np.random.rand() < 0.20:
                row[col] = round(float(np.random.uniform(-1.0, 1.0)), 2)
            else:
                row[col] = np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    return compute_derived_summaries(df)


@pytest.fixture
def valid_human_df2():
    """Generates a second valid 31-paper human evaluation dataframe."""
    rows = []
    np.random.seed(456)
    for study in CANONICAL_PAPERS:
        row = {
            "study_name": study,
            "agent_": "hpch_test2",
            "year_": 2020.0,
            "type_": "empirical"
        }
        for col in ALL_FACTOR_COLS:
            if np.random.rand() < 0.25:
                row[col] = round(float(np.random.uniform(-1.0, 1.0)), 2)
            else:
                row[col] = np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    return compute_derived_summaries(df)


def test_validation_valid_table(valid_human_df):
    is_valid, errors, recomputed = validate_human_score_table(valid_human_df, expected_agent="hpch_test1")
    assert is_valid is True
    assert len(errors) == 0
    assert recomputed.shape == (31, 90)
    assert list(recomputed["study_name"]) == CANONICAL_PAPERS


def test_validation_missing_study(valid_human_df):
    bad_df = valid_human_df.iloc[:-1]  # 30 rows
    is_valid, errors, _ = validate_human_score_table(bad_df)
    assert is_valid is False
    assert any("Expected exactly 31 rows" in e for e in errors)


def test_validation_unknown_study(valid_human_df):
    bad_df = valid_human_df.copy()
    bad_df.loc[0, "study_name"] = "UnknownAuthor2099"
    is_valid, errors, _ = validate_human_score_table(bad_df)
    assert is_valid is False
    assert any("Unknown or non-canonical" in e for e in errors)


def test_validation_duplicate_study(valid_human_df):
    bad_df = valid_human_df.copy()
    bad_df.loc[1, "study_name"] = bad_df.loc[0, "study_name"]
    is_valid, errors, _ = validate_human_score_table(bad_df)
    assert is_valid is False
    assert any("Duplicate study entries" in e for e in errors)


def test_validation_out_of_bounds_score(valid_human_df):
    bad_df = valid_human_df.copy()
    bad_df.loc[0, "LO-F01"] = 1.5
    is_valid, errors, _ = validate_human_score_table(bad_df)
    assert is_valid is False
    assert any("outside [-1.0, 1.0]" in e for e in errors)


def test_validation_non_numeric_token(valid_human_df):
    bad_df = valid_human_df.copy()
    bad_df["LO-F01"] = bad_df["LO-F01"].astype(object)
    bad_df.loc[0, "LO-F01"] = "invalid_string"
    is_valid, errors, _ = validate_human_score_table(bad_df)
    assert is_valid is False
    assert any("non-numeric invalid values" in e for e in errors)


def test_validation_agent_mismatch(valid_human_df):
    is_valid, errors, _ = validate_human_score_table(valid_human_df, expected_agent="hpch_different")
    assert is_valid is False
    assert any("Expected agent 'hpch_different'" in e for e in errors)


def test_pairwise_agreement_exact_correlation(valid_human_df):
    # Pairwise agreement with self should be r=1.0, MAE=0.0
    res = compute_pairwise_agreement(valid_human_df, valid_human_df, "R1", "R1_clone")
    assert res["overlapping_n"] > 0
    assert res["pearson_r"] == 1.0
    assert res["mae"] == 0.0
    assert res["msd"] == 0.0
    assert res["concordant_directional_n"] == res["eligible_directional_n"]
    assert res["directional_concordance_proportion"] == 1.0
    assert "inferential_warning" in res


def test_pairwise_agreement_directional_denominators():
    # Construct small test fixture
    d1 = pd.DataFrame([{"study_name": s, **{c: np.nan for c in ALL_FACTOR_COLS}} for s in CANONICAL_PAPERS])
    d2 = pd.DataFrame([{"study_name": s, **{c: np.nan for c in ALL_FACTOR_COLS}} for s in CANONICAL_PAPERS])
    
    # 4 overlapping slots
    # slot 1: +0.5 vs +0.8 (agree)
    # slot 2: -0.4 vs -0.2 (agree)
    # slot 3: +0.6 vs -0.6 (disagree)
    # slot 4: 0.0 vs +0.5 (one zero -> excluded from directional)
    d1.loc[0, "LO-F01"] = 0.5
    d2.loc[0, "LO-F01"] = 0.8
    
    d1.loc[0, "LO-F02"] = -0.4
    d2.loc[0, "LO-F02"] = -0.2
    
    d1.loc[0, "LO-F03"] = 0.6
    d2.loc[0, "LO-F03"] = -0.6
    
    d1.loc[0, "LO-F04"] = 0.0
    d2.loc[0, "LO-F04"] = 0.5
    
    res = compute_pairwise_agreement(d1, d2)
    assert res["overlapping_n"] == 4
    assert res["eligible_directional_n"] == 3
    assert res["excluded_zero_n"] == 1
    assert res["concordant_directional_n"] == 2
    assert abs(res["directional_concordance_proportion"] - 2 / 3) < 1e-4


def test_build_human_consensus(valid_human_df, valid_human_df2):
    consensus_df, counts_df = build_human_consensus([valid_human_df, valid_human_df2])
    assert consensus_df.shape == (31, 90)
    assert counts_df.shape == (31, 73)  # study_name + 72 factors
    
    # Check that counts reflect valid presence
    v1 = valid_human_df.set_index("study_name")[ALL_FACTOR_COLS]
    v2 = valid_human_df2.set_index("study_name")[ALL_FACTOR_COLS]
    c_vals = consensus_df.set_index("study_name")[ALL_FACTOR_COLS]
    cnts = counts_df.set_index("study_name")[ALL_FACTOR_COLS]
    
    for study in CANONICAL_PAPERS[:5]:
        for col in ALL_FACTOR_COLS[:5]:
            s1 = v1.loc[study, col]
            s2 = v2.loc[study, col]
            c_score = c_vals.loc[study, col]
            count = cnts.loc[study, col]
            
            valid_scores = [s for s in [s1, s2] if pd.notna(s)]
            assert count == len(valid_scores)
            if count == 0:
                assert pd.isna(c_score)
            else:
                assert abs(c_score - np.mean(valid_scores)) < 1e-5


def test_council_agreement_and_disagreements(valid_human_df):
    repo_root = Path(__file__).resolve().parents[2]
    council_path = repo_root / "content" / "tables" / "original_council" / "hpc_table_original_council.csv"
    
    council_df = load_council_consensus(council_path)
    assert council_df.shape == (31, 90)
    assert council_df["agent_"].iloc[0] == "council_consensus_8m"
    
    consensus_df, counts_df = build_human_consensus([valid_human_df])
    
    agr_res = compute_human_council_agreement(consensus_df, council_df, counts_df, min_raters=1)
    assert "pearson_r" in agr_res
    assert "mae" in agr_res
    assert "inferential_warning" in agr_res
    
    dis_report = generate_disagreement_report(consensus_df, council_df, diagnostic_threshold=0.50)
    assert isinstance(dis_report, pd.DataFrame)
    if not dis_report.empty:
        assert "is_diagnostic_divergence" in dis_report.columns
        # Check sorted order
        assert (dis_report["absolute_difference"].diff().dropna() <= 0).all()
