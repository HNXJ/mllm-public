"""Unit tests for permutation benchmarks and supplement export modules."""

import pytest
import pandas as pd
from pathlib import Path

from jmllm.analysis.shuffled_baselines import run_figure4_permutation_benchmark
from jmllm.analysis.export_supplement_tables import (
    export_authoritative_robustness_summary,
    export_leave_one_out_summary,
    export_westerberg_sensitivity_summary,
    export_corpus_registry,
    export_claims_ledger,
)


def test_shuffled_baselines_fast(tmp_path):
    out_csv = tmp_path / "test_null.csv"
    summary_dict, df_res = run_figure4_permutation_benchmark(
        B=50,
        seed=42,
        output_csv_path=out_csv
    )
    assert len(df_res) == 3
    assert out_csv.exists()
    assert "Observed Council Baseline" in summary_dict
    assert "Figure 4 Full-Shuffle Null" in summary_dict
    assert "Figure 4 Hypotheses-Shuffle Null" in summary_dict
    
    # Check that observed MSD is lower than null distributions
    obs_msd = summary_dict["Observed Council Baseline"]["mean_msd"]
    full_msd = summary_dict["Figure 4 Full-Shuffle Null"]["mean_msd"]
    assert obs_msd < full_msd


def test_export_robustness_summary(tmp_path):
    out_csv = tmp_path / "test_rob.csv"
    df = export_authoritative_robustness_summary(out_csv)
    assert len(df) == 7
    assert out_csv.exists()
    assert (df["sample_size_N"] > 0).all()
    # Check M2-01 values
    m2_01 = df[df["claim_id"] == "M2-01"].iloc[0]
    assert m2_01["primary_estimate"] == 0.9900
    assert m2_01["secondary_estimate_mae"] == 0.0266
    assert m2_01["sample_size_N"] == 679


def test_export_leave_one_out(tmp_path):
    out_csv = tmp_path / "test_loo.csv"
    df = export_leave_one_out_summary(out_csv)
    assert len(df) == 11  # 1 baseline + 10 council models
    assert out_csv.exists()
    deltas = df[df["omitted_model"] != "None"]["mean_displacement_delta"]
    assert len(deltas) == 10
    # Range of LOO mean displacement deltas across all 10 council models
    assert deltas.min() == -0.0628
    assert deltas.max() == -0.0512


def test_export_westerberg_sensitivity(tmp_path):
    out_csv = tmp_path / "test_west.csv"
    df = export_westerberg_sensitivity_summary(out_csv)
    assert len(df) == 3
    assert out_csv.exists()
    full = df[df["corpus_stratum"] == "Full Paired Corpus"].iloc[0]
    assert full["paper_sample_N"] == 28
    assert full["mean_displacement_delta"] == -0.0177
    assert full["paired_t_p_value"] == 0.7208

    no_west = df[df["corpus_stratum"] == "Excluding Westerberg & Xiong (2025)"].iloc[0]
    assert no_west["paper_sample_N"] == 27
    assert no_west["mean_displacement_delta"] == 0.0297
    assert no_west["paired_t_p_value"] == 0.0296


def test_export_corpus_registry(tmp_path):
    out_csv = tmp_path / "test_reg.csv"
    df = export_corpus_registry(out_csv)
    assert len(df) == 31
    assert out_csv.exists()


def test_export_claims_ledger(tmp_path):
    out_csv = tmp_path / "test_ledger.csv"
    df = export_claims_ledger(out_csv)
    assert len(df) >= 10
    assert out_csv.exists()
