"""Unit tests for the Evidence vs. Prior ablation input generator and leakage audit."""

import pytest
from pathlib import Path
import pandas as pd

from jmllm.pipeline.evidence_prior_ablation import (
    generate_18_ablation_inputs,
    perform_leakage_audit,
    PRESPECIFIED_PAPERS,
)


def test_18_ablation_inputs_generation():
    inputs = generate_18_ablation_inputs()
    assert len(inputs) == 18
    for p in PRESPECIFIED_PAPERS:
        assert f"{p}__CondA" in inputs
        assert f"{p}__CondB" in inputs
        assert f"{p}__CondC" in inputs
        assert inputs[f"{p}__CondA"].exists()
        assert inputs[f"{p}__CondB"].exists()
        assert inputs[f"{p}__CondC"].exists()


def test_deterministic_leakage_audit():
    inputs = generate_18_ablation_inputs()
    audit_df = perform_leakage_audit(inputs)
    assert len(audit_df) == 6
    assert (audit_df["audit_verdict"] == "PASSED").all()
    assert (audit_df["leak_count"] == 0).all()
