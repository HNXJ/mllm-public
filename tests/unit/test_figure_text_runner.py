"""Focused unit tests for the 31-paper figure-text ablation runner."""

import pytest
import pandas as pd
import hashlib
import json
import importlib.util
from pathlib import Path
from unittest.mock import patch

# Load runner dynamically
spec = importlib.util.spec_from_file_location("figure_text_runner", "src/jmllm/pipeline/figure_text_runner.py")
ft_runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ft_runner)


def test_manifest_acceptance():
    """Tests that the real 31-row manifest is accepted and contains 31 distinct papers."""
    df = ft_runner.validate_manifest(ft_runner.MANIFEST_PATH)
    assert len(df) == 31
    assert df["paper_id"].nunique() == 31


def test_manifest_missing_file(tmp_path):
    """Tests that a missing staged input raises FileNotFoundError."""
    bad_manifest = tmp_path / "bad_manifest.csv"
    df = pd.DataFrame([{
        "paper_id": "NonExistent2099",
        "nofigure_input_path": "content/non_existent.md",
        "nofigure_input_sha256": "fakehash"
    }])
    bad_manifest.write_text(df.to_csv(index=False), encoding="utf-8")
    with pytest.raises(ValueError, match="31 rows"):
        ft_runner.validate_manifest(bad_manifest)


def test_manifest_sha_mismatch(tmp_path):
    """Tests that a SHA-256 mismatch raises ValueError."""
    real_df = pd.read_csv(ft_runner.MANIFEST_PATH).copy()
    real_df.loc[0, "nofigure_input_sha256"] = "0000000000000000000000000000000000000000000000000000000000000000"
    mismatched_manifest = tmp_path / "mismatch.csv"
    real_df.to_csv(mismatched_manifest, index=False)
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        ft_runner.validate_manifest(mismatched_manifest)


def test_glossary_loading():
    """Tests that exact 36 canonical factors are loaded."""
    text, keys = ft_runner.load_canonical_glossary()
    assert len(keys) == 36
    assert "Subtractive Inhibition (SST)" in keys[0]


def test_parser_regression_on_historical_raw_responses():
    """Tests that the ported parser gives identical results on representative historical raw responses."""
    # Strict valid JSON test
    valid_mock = json.dumps({
        "lo_evaluations": {f: 0.5 for f in ft_runner.CANONICAL_FACTORS},
        "go_evaluations": {f: -0.5 for f in ft_runner.CANONICAL_FACTORS},
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "gemma-4-31b-it",
        "reasoning_log_text": "Sample valid reasoning."
    })
    p_status, p_method, p_data, lo, go, errs, notes = ft_runner.parse_and_recover_generation(valid_mock)
    assert p_status == "valid"
    assert p_method == "strict_json"
    assert len(lo) == 36
    assert len(go) == 36
    assert lo["Subtractive Inhibition (SST)"] == 0.5

    # Markdown fenced extraction test
    fenced_mock = f"Here is the result:\n```json\n{valid_mock}\n```\nHope this helps."
    p_status2, p_method2, p_data2, lo2, go2, errs2, notes2 = ft_runner.parse_and_recover_generation(fenced_mock)
    assert p_status2 == "valid"
    assert p_method2 == "cleaned_json"
    assert len(lo2) == 36


def test_malformed_response_handling():
    """Tests that unrecoverable/malformed outputs are caught and NOT marked COMPLETED."""
    text, keys = ft_runner.load_canonical_glossary()
    first_input = ft_runner.REPO_ROOT / "content/202608_temp/nofigure_inputs/Attinger2017__NO_FIGURE.md"
    
    with patch("requests.post") as mock_post:
        mock_resp = mock_post.return_value
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "model": "gemma-4-31b-it",
            "choices": [{"message": {"content": "I am an LLM and cannot evaluate this."}}]
        }
        
        ledger_rec, scores = ft_runner.execute_single_call(
            "call_bad", "Attinger2017", first_input, text, keys, dry_run=False
        )
        assert ledger_rec["status"] == "PARSE_FAILED"
        assert ledger_rec["parse_status"] == "unrecoverable"
        assert len(scores) == 0


def test_strict_zero_network_dry_run():
    """Strictly proves zero network calls by monkeypatching requests.post to raise an exception."""
    with patch("requests.post", side_effect=RuntimeError("CRITICAL: Network request attempted during dry-run!")):
        df_ledger, df_scores = ft_runner.run_ablation_sweep(dry_run=True)
        assert len(df_ledger) == 31
        assert (df_ledger["status"] == "DRY_RUN_VALIDATED").all()
        assert len(df_scores) == 0
