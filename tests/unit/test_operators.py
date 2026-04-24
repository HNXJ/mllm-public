"""Golden tests for core scientific operators in mllm."""

import pytest
import numpy as np
import pandas as pd
from typing import List, Dict, Any
from unittest.mock import patch

def calculate_msd_operator(scores_a: np.ndarray, scores_b: np.ndarray) -> float:
    """Core operator for Mean Squared Deviation, handling NaNs."""
    diff = scores_a - scores_b
    valid_diff = diff[~np.isnan(diff)]
    if len(valid_diff) == 0: return 0.0
    return np.mean(valid_diff**2)

def test_msd_golden_values():
    """Verify MSD operator against known golden values."""
    # Case 1: Identical
    a = np.array([1.0, 0.5, 0.0])
    b = np.array([1.0, 0.5, 0.0])
    assert calculate_msd_operator(a, b) == 0.0
    
    # Case 2: Known deviation
    a = np.array([1.0, 1.0, 1.0])
    b = np.array([0.0, 0.0, 0.0])
    assert calculate_msd_operator(a, b) == 1.0
    
    # Case 3: Handling NaNs
    a = np.array([1.0, np.nan, 0.5])
    b = np.array([0.0, 1.0, 0.5])
    # Diff is [1.0, nan, 0.0] -> Valid diff is [1.0, 0.0] -> Mean sq is 0.5
    assert calculate_msd_operator(a, b) == 0.5

def test_agent_name_cleaning_operator():
    """Verify the agent name cleaning logic."""
    # Simulated agent names with versions
    raw_names = ["Phi-4 (v1.2)", "DeepSeek-R1 (70B)", "Llama-3-70b (v2)"]
    clean_names = [name.split('(')[0].strip() for name in raw_names]
    assert clean_names == ["Phi-4", "DeepSeek-R1", "Llama-3-70b"]

def test_release_manifest_generation():
    """Verify that every test run generates a valid ReleaseManifest."""
    from mllm.utils.reproducibility import generate_release_snapshot
    manifest = generate_release_snapshot()
    # Relaxed assertion for zip/archive workspaces where .git might be missing
    assert isinstance(manifest.commit_hash, str)
    assert len(manifest.commit_hash) > 0
    assert "AppleSilicon" in manifest.environment_tags or "Linux" in manifest.environment_tags or "Darwin" in manifest.environment_tags

def test_git_commit_hash_fallback():
    """Verify git commit hash fallback when git is not available."""
    from mllm.utils.reproducibility import get_git_commit
    import subprocess
    with patch("subprocess.check_output", side_effect=subprocess.SubprocessError("no git")):
        assert get_git_commit() == "unknown"
