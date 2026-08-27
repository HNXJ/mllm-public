"""Unit tests for the revision figures renderer."""

import pytest
from pathlib import Path
from jmllm.vis.render_revision_figures import (
    render_human_concordance_figure,
    render_decoding_robustness_figure,
    render_evidence_prior_figure,
    render_figure4_nulls_figure,
    render_westerberg_sensitivity_figure,
    render_all_revision_figures
)


def test_render_all_revision_figures(tmp_path):
    out_dir = tmp_path / "figs"
    render_all_revision_figures(output_dir=out_dir)

    expected_stems = [
        "figure_S_human_concordance",
        "figure_S_decoding_robustness",
        "figure_S_evidence_prior",
        "figure_S_figure4_nulls",
        "figure_S_westerberg_sensitivity"
    ]

    for stem in expected_stems:
        svg_file = out_dir / f"{stem}.svg"
        png_file = out_dir / f"{stem}.png"
        assert svg_file.exists(), f"Missing SVG for {stem}"
        assert png_file.exists(), f"Missing PNG for {stem}"
        assert svg_file.stat().st_size > 1000
        assert png_file.stat().st_size > 1000
