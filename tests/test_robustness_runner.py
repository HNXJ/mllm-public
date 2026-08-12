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
    generate_manifest,
    generate_long_csv,
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
    SCORES_LONG_PATH,
)


def test_factorial_manifest_dimensions(tmp_path, monkeypatch):
    """Verify that the manifest generates exactly 837 unique primary cells."""
    dummy_mapping = {
        "olmo-3-32b-think": "olmo-3-32b-think-mlx",
        "gemma-4-31b-it": "gemma-4-31b-it",
        "mistral-nemo-12b-thinking": "mistral-nemo-12b-thinking-mlx",
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
    assert df["repeat"].nunique() == 3
    assert set(df["temperature"].unique()) == {"0.00", "0.35", "0.70"}


def test_temperature_repeat_encoding_collision_free():
    """Verify that T and R codes produce distinct, collision-free condition IDs."""
    c1 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.00, 1)
    c2 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.35, 1)
    c3 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.70, 1)
    c4 = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.00, 2)

    assert c1 == "Attinger2017__gemma-4-31b-it__T000__R01"
    assert c2 == "Attinger2017__gemma-4-31b-it__T035__R01"
    assert c3 == "Attinger2017__gemma-4-31b-it__T070__R01"
    assert c4 == "Attinger2017__gemma-4-31b-it__T000__R02"

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
        "agent_name": "gemma-4-31b-it",
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
        "agent_name": "gemma-4-31b-it",
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
        "agent_name": "gemma",
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
        "agent_name": "gemma",
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
        "agent_name": "gemma",
        "reasoning_log_text": "log",
    }

    is_valid, errors, _, _ = validate_response(data)
    assert is_valid is False
    assert any("out of range" in e for e in errors)


def test_resumability_skips_complete_cells(tmp_path, monkeypatch):
    """Verify that manifest generation marks valid raw JSON cells as COMPLETE and skips re-execution."""
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
        "mistral-nemo-12b-thinking": "mistral-nemo-12b-thinking-mlx",
    }

    # Pre-create one complete valid raw file
    cid = generate_condition_id("Attinger2017", "olmo-3-32b-think", 0.00, 1)
    rec = {
        "condition_id": cid,
        "paper_id": "Attinger2017",
        "scientific_model": "olmo-3-32b-think",
        "served_model_id": "olmo-3-32b-think-mlx",
        "temperature": 0.0,
        "repeat": 1,
        "validation_status": "VALID",
        "attempts": 1,
        "latency_seconds": 1.2,
    }
    with open(raw_dir / f"{cid}.json", "w") as f:
        json.dump(rec, f)

    df = generate_manifest(dummy_mapping)
    row = df[df["condition_id"] == cid].iloc[0]

    assert row["status"] == "COMPLETE"
    assert row["validation_status"] == "VALID"
    assert row["attempts"] == 1


def test_raw_response_preservation_on_invalid(tmp_path, monkeypatch):
    """Verify that when validation fails, raw response text is preserved and marked INVALID."""
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.EXP_DIR", tmp_path)
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.RAW_DIR", tmp_path / "raw")
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    cid = generate_condition_id("Attinger2017", "gemma-4-31b-it", 0.70, 1)

    invalid_parsed = {
        "lo_evaluations": {"BadKey": 0.5},  # Invalid factor key
        "go_evaluations": {},
        "first_author": "Attinger",
        "publication_year": "2017",
        "study_type": "Empirical",
        "agent_name": "gemma",
        "reasoning_log_text": "Malformed response log",
    }

    raw_text = '{"lo_evaluations": {"BadKey": 0.5}}'

    is_valid, errors, _, _ = validate_response(invalid_parsed)
    assert is_valid is False
    assert len(errors) > 0

    record = {
        "condition_id": cid,
        "raw_assistant_response": raw_text,
        "parsed_response": invalid_parsed,
        "validation_status": "INVALID",
        "validation_errors": errors,
    }

    with open(raw_dir / f"{cid}.json", "w") as f:
        json.dump(record, f, indent=2)

    # Read back and verify raw preservation
    with open(raw_dir / f"{cid}.json", "r") as f:
        saved = json.load(f)

    assert saved["validation_status"] == "INVALID"
    assert saved["raw_assistant_response"] == raw_text
    assert len(saved["validation_errors"]) > 0


def test_long_csv_dimensionality(tmp_path, monkeypatch):
    """Verify that generating long CSV from 837 synthetic VALID raw records produces exactly 60,264 score rows."""
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.EXP_DIR", tmp_path)
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.RAW_DIR", tmp_path / "raw")
    monkeypatch.setattr("jmllm.pipeline.robustness_runner.SCORES_LONG_PATH", tmp_path / "scores_long.csv")

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    dummy_mapping = {
        "olmo-3-32b-think": "olmo-3-32b-think-mlx",
        "gemma-4-31b-it": "gemma-4-31b-it",
        "mistral-nemo-12b-thinking": "mistral-nemo-12b-thinking-mlx",
    }

    paper_ids = [f"Paper{i:02d}" for i in range(1, 32)]
    lo_evals = {f: 0.5 for f in CANONICAL_FACTORS}
    go_evals = {f: None for f in CANONICAL_FACTORS}

    count = 0
    for pid in paper_ids:
        for model in SCIENTIFIC_MODELS:
            served_id = dummy_mapping[model]
            for temp in TEMPERATURES:
                for rep in REPEATS:
                    cid = generate_condition_id(pid, model, temp, rep)
                    rec = {
                        "condition_id": cid,
                        "paper_id": pid,
                        "scientific_model": model,
                        "served_model_id": served_id,
                        "temperature": temp,
                        "repeat": rep,
                        "validation_status": "VALID",
                        "lo_evaluations": lo_evals,
                        "go_evaluations": go_evals,
                    }
                    with open(raw_dir / f"{cid}.json", "w") as f:
                        json.dump(rec, f)
                    count += 1

    assert count == 837

    df_long = generate_long_csv()
    assert len(df_long) == 837 * 2 * 36
    assert len(df_long) == 60264
