"""Reproducibility snapshot utilities for the MLLM HPC pipeline.

HPC Pipeline Role — Experimental Logbook
==========================================
In scientific computing, every evaluation must be reproducible.  This module
captures the exact execution context — git commit, Python version, toolchain
version, and hardware accelerators — into a ``ReleaseManifest`` that is
saved alongside evaluation results.  This is the computational equivalent
of recording electrode impedances and amplifier settings in a
neurophysiology experiment.
"""

import sys
import platform
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, List

from mllm.config.model_config import ReleaseManifest, ModelManifest

def get_git_commit() -> str:
    """Get the current git commit hash."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], 
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except (subprocess.SubprocessError, Exception):
        return "unknown"

def get_toolchain_info() -> str:
    """Get system compiler/toolchain information."""
    if platform.system() == "Darwin":
        try:
            return subprocess.check_output(["clang", "--version"], stderr=subprocess.DEVNULL).decode().split('\n')[0]
        except (subprocess.SubprocessError, Exception): pass
    elif platform.system() == "Linux":
        try:
            return subprocess.check_output(["gcc", "--version"], stderr=subprocess.DEVNULL).decode().split('\n')[0]
        except (subprocess.SubprocessError, Exception): pass
    return "unknown"

def get_environment_tags() -> List[str]:
    """Capture environment tags (OS, Architecture, Accelerators)."""
    tags = [platform.system(), platform.machine()]
    
    # Check for MLX (Apple Silicon)
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        tags.append("AppleSilicon")
        try:
            import mlx.core
            tags.append("MLX")
        except ImportError: pass
        
    # Check for CUDA
    try:
        import torch
        if torch.cuda.is_available():
            tags.append("CUDA")
    except ImportError: pass
    
    return tags

def generate_release_snapshot(active_model: Optional[ModelManifest] = None) -> ReleaseManifest:
    """Generates a full ReleaseManifest for the current execution."""
    return ReleaseManifest(
        commit_hash=get_git_commit(),
        timestamp=datetime.now().isoformat(),
        python_version=sys.version.split(' ')[0],
        environment_tags=get_environment_tags(),
        toolchain_version=get_toolchain_info(),
        active_manifest=active_model
    )

def save_release_snapshot(manifest: ReleaseManifest, output_path: Path):
    """Saves the release manifest to a JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(manifest.model_dump_json(indent=2))
