"""Unit tests for the MLLM Reviewer Robustness Experiment Harness.
"""

import json
import pytest
import pandas as pd
from pathlib import Path
from typing import Dict, Any

from jmllm.pipeline.robustness_runner import (
    generate_condition_id,
    get_temp_code,
    get_repeat_code,
    validate_response,
    validate_response_schema,
    parse_and_recover_generation,
    generate_manifest,
    generate_tabular_datasets,
    reparse_raw_artifacts,
    write_file_atomically,
    execute_cell_inference,
    CANONICAL_FACTORS,
    SCIENTIFIC_MODELS,
    TEMPERATURES,
    REPEATS,
    TOP_P,
    MIN_P,
    EXP_DIR,
    RAW_DIR,
    MANIFEST_PATH,
    CALLS_CSV_PATH,
    SCORES_CSV_PATH,
)


def test_factorial_manifest_dimensions(tmp_path, monkeypatch):
    """Verify that the manifest generates exactly 837 unique primary cells."""
    dummy_mapping = {
        "olmo-3-32b-think": "olmo-3-32b-think-mlx",
        "gemma-4-31b-it": "gemma-4-31b-it",
        "phi-4-reasoning-plus": "phi-4-reasoning-plus",
    }

    monkeypatch.setattr("jmllm.pipeline.robustness_runner.EXP_DIR", tmp_path)
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.RAW_DIR", tmp_path / "raw")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.LOGS_DIR", tmp_path / "logs")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.CONFIG_DIR", tmp_path / "config")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.MANIFEST_PATH", tmp_path / "manifest.csv")

    df = generate_manifest(dummy_mapping)

    assert len(df) == 837
    assert df["condition_id"].nunique() == 837
    assert df["paper_id"].nunique() == 31
    assert df["scientific_model"].nunique() == 3
    assert set(df["scientific_model"].unique()) == {"olmo-3-32b-think", "gemma-4-31b-it", "phi-4-reasoning-plus"}
    assert df["repeat"].nunique() == 3
    assert set(df["temperature"].unique()) == {"0.00", "0.35", "0.70"}


def test_temperature_repeat_encoding_collision_free():
    """Verify that T and R codes produce distinct, collision-free condition IDs."""
    c1 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.00, 1)
    c2 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.35, 1)
    c3 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.70, 1)
    c4 = generate_condition_id("Attinger2017", "phi-4-reasoning-plus", 0.00, 2)

    assert c1 == "Attinger2017__gemma-4-31b-it__T000__R01"
    assert c2 == "Attinger2017__gemma-4-31b-it__T035__R01"
    assert c3 == "Attinger2017__gemma-4-31b-it__T070__R01"
    assert c4 == "Attinger2017__phi-4-reasoning-plus__T000__R02"

    assert len({c1, c2, c3, c4}) == 4


def test_sampler_metadata_constants():
    """Verify sampler defaults top_p=0.90 and min_p=0.10 are explicit."""
    assert TOP_P == 0.90
    assert MIN_P == 0.10


def test_temperature_zero_payload_serialization():
    """Verify that T=0.00 is serialized as numeric 0.0 and never evaluated as falsy."""
    temp = 0.00
    payload = {
        "model": "gemma-4-31b-it",
        "messages": [{"role": "user", "content": "prompt"}],
        "temperature": temp,
        "top_p": TOP_P,
        "min_p": MIN_P,
    }

    serialized = json.dumps(payload)
    deserialized = json.loads(serialized)

    assert deserialized["temperature"] == 0.0
    assert type(deserialized["temperature"]) in (int, float)
    assert deserialized["temperature"] is not None


def test_validation_valid_response():
    """Verify that a response with all 36 LO and 36 GO factor scores passes validation."""
    valid_lo = {f: 0.6 if i % 2 == 0 else None for i, f in enumerate(CANONICAL_FACTORS)}
    valid_go = {f: -0.2 if i % 3 == 0 else None for i, f in enumerate(CANONICAL_FACTORS)}

    data = {
        "lo_evaluations": valid_lo,
        "go_evaluations": valid_go,
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4-reasoning-plus",
        "reasoning_log_text": "Valid test reasoning log.",
    }

    is_valid, errors, lo, go = validate_response(data)
    assert is_valid is True
    assert len(errors) == 0
    assert len(lo) == 36
    assert len(go) == 36


def test_null_score_acceptance():
    """Verify that explicit null/None factor scores are accepted without converting to 0.0."""
    lo = {f: None for f in CANONICAL_FACTORS}
    go = {f: None for f in CANONICAL_FACTORS}

    data = {
        "lo_evaluations": lo,
        "go_evaluations": go,
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4-reasoning-plus",
        "reasoning_log_text": "All factors null.",
    }

    is_valid, errors, lo_out, go_out = validate_response(data)
    assert is_valid is True
    assert all(v is None for v in lo_out.values())
    assert all(v is None for v in go_out.values())


def test_validation_missing_factor():
    """Verify that omitting a factor key triggers a validation error."""
    lo = {f: 0.5 for f in CANONICAL_FACTORS[:-1]}  # 35 factors
    go = {f: 0.5 for f in CANONICAL_FACTORS}

    data = {
        "lo_evaluations": lo,
        "go_evaluations": go,
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4-reasoning-plus",
        "reasoning_log_text": "log",
    }

    is_valid, errors, _, _ = validate_response(data)
    assert is_valid is False
    assert any("missing canonical factors" in e for e in errors)


def test_validation_extra_unknown_factor():
    """Verify that introducing an unknown factor key triggers a validation error."""
    lo = {f: 0.5 for f in CANONICAL_FACTORS}
    lo["FakeUnknownFactor"] = 0.8
    go = {f: 0.5 for f in CANONICAL_FACTORS}

    data = {
        "lo_evaluations": lo,
        "go_evaluations": go,
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4-reasoning-plus",
        "reasoning_log_text": "log",
    }

    is_valid, errors, _, _ = validate_response(data)
    assert is_valid is False
    assert any("unknown factor keys" in e for e in errors)


def test_validation_out_of_range_score():
    """Verify that scores outside [-1.0, 1.0] trigger a validation error."""
    lo = {f: 0.5 for f in CANONICAL_FACTORS}
    lo[CANONICAL_FACTORS[0]] = 2.5  # Out of range

    data = {
        "lo_evaluations": lo,
        "go_evaluations": {f: 0.5 for f in CANONICAL_FACTORS},
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4-reasoning-plus",
        "reasoning_log_text": "log",
    }

    is_valid, errors, _, _ = validate_response(data)
    assert is_valid is False
    assert any("out of range" in e for e in errors)


def test_two_stage_recovery_parser():
    """Verify Stage B recovery parser behavior across valid, recovered, and unrecoverable generations."""
    # 1. Valid JSON
    valid_lo = {f: 0.5 for f in CANONICAL_FACTORS}
    valid_go = {f: None for f in CANONICAL_FACTORS}
    valid_json = json.dumps({
        "lo_evaluations": valid_lo,
        "go_evaluations": valid_go,
        "first_author": "Test",
        "publication_year": "2020",
        "study_type": "Empirical",
        "agent_name": "gemma",
        "reasoning_log_text": "Log text"
    })

    p_status, p_method, _, lo, go, _, _ = parse_and_recover_generation(valid_json)
    assert p_status == "valid"
    assert p_method in ["strict_json", "cleaned_json"]
    assert len(lo) == 36

    # 2. Recovered JSON (Markdown wrapped + extra text)
    prose_json = f"Here is my evaluation:\n```json\n{valid_json}\n```\nHope this helps!"
    p_status, p_method, _, lo, go, _, _ = parse_and_recover_generation(prose_json)
    assert p_status in ["valid", "recovered"]
    assert len(lo) == 36

    # 3. Unrecoverable prose
    garbage = "I cannot evaluate this paper as a model."
    p_status, p_method, _, lo, go, errs, _ = parse_and_recover_generation(garbage)
    assert p_status == "unrecoverable"
    assert p_method == "failed"
    assert lo is None


def test_resumability_skips_complete_cells(tmp_path, monkeypatch):
    """Verify that manifest generation marks valid raw JSON cells as COMPLETE."""
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.EXP_DIR", tmp_path)
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.RAW_DIR", tmp_path / "raw")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.LOGS_DIR", tmp_path / "logs")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.CONFIG_DIR", tmp_path / "config")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.MANIFEST_PATH", tmp_path / "manifest.csv")

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    dummy_mapping = {
        "olmo-3-32b-think": "olmo-3-32b-think-mlx",
        "gemma-4-31b-it": "gemma-4-31b-it",
        "phi-4-reasoning-plus": "phi-4-reasoning-plus",
    }

    cid = generate_condition_id("Attinger2017", "phi-4-reasoning-plus", 0.00, 1)
    rec = {
        "condition_id": cid,
        "paper_id": "Attinger2017",
        "scientific_model": "phi-4-reasoning-plus",
        "served_model_id": "phi-4-reasoning-plus",
        "temperature": 0.0,
        "repeat": 1,
        "parse_status": "valid",
        "validation_status": "VALID",
        "attempts": 1,
        "latency_seconds": 1.2,
    }
    with open(raw_dir / f"{cid}.json", "w") as f:
        json.dump(rec, f)

    df = generate_manifest(dummy_mapping)
    row = df[df["condition_id"] == cid].iloc[0]

    assert row["status"] == "COMPLETE"
    assert row["parse_status"] == "valid"
    assert row["attempts"] == 1


def test_raw_response_preservation_and_atomic_write(tmp_path, monkeypatch):
    """Verify atomic write helper and raw assistant response preservation."""
    target_path = tmp_path / "atomic_test.json"
    content = json.dumps({"test": "atomic"})
    
    write_file_atomically(target_path, content)
    assert target_path.exists()
    with open(target_path, "r") as f:
        assert f.read() == content


def test_tabular_datasets_and_offline_reparse(tmp_path, monkeypatch):
    """Verify calls.csv and scores.csv generation and offline re-parser execution."""
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.EXP_DIR", tmp_path)
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.RAW_DIR", tmp_path / "raw")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.CALLS_CSV_PATH", tmp_path / "calls.csv")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.SCORES_CSV_PATH", tmp_path / "scores.csv")

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    cid = generate_condition_id("Attinger2017", "phi-4-reasoning-plus", 0.00, 1)
    lo_evals = {f: 0.5 for f in CANONICAL_FACTORS}
    go_evals = {f: None for f in CANONICAL_FACTORS}
    
    raw_text = json.dumps({
        "lo_evaluations": lo_evals,
        "go_evaluations": go_evals,
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "phi-4",
        "reasoning_log_text": "log text",
    })

    rec = {
        "condition_id": cid,
        "paper_id": "Attinger2017",
        "scientific_model": "phi-4-reasoning-plus",
        "served_model_id": "phi-4-reasoning-plus",
        "temperature": 0.0,
        "repeat": 1,
        "raw_assistant_response": raw_text,
        "parse_status": "valid",
        "parser_method": "strict_json",
        "lo_evaluations": lo_evals,
        "go_evaluations": go_evals,
    }
    with open(raw_dir / f"{cid}.json", "w") as f:
        json.dump(rec, f)

    df_calls, df_scores = generate_tabular_datasets()
    assert len(df_calls) == 1
    assert df_calls.iloc[0]["condition_id"] == cid
    assert len(df_scores) == 72  # 36 LO + 36 GO

    # Test Offline Reparse (zero inference calls)
    df_calls_re, df_scores_re = reparse_raw_artifacts()
    assert len(df_calls_re) == 1
    assert len(df_scores_re) == 72
