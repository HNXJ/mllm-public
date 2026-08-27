"""Reusable Visual Templates Matching Submitted Manuscript Figures 3-8.

Design Principles:
- Exact visual grammar matching submitted manuscript PDF (2026_mllm_arxiv_post_sub.pdf).
- Zero embedded scientific values (all arrays/metrics passed dynamically from frozen CSVs).
- Deterministic 300 DPI PNG + vector SVG dual exports.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Centralized Style Constants (Direct from Manuscript PDF)
LO_COLOR = '#EF553B'       # Local Oddball Context (Crimson / Vermilion)
GO_COLOR = '#636EFA'       # Global Oddball Context (Periwinkle / Royal Blue)
PALE_BLUE = '#85C1E9'      # Score cloud scatter points
RED_DIAMOND = '#C0392B'    # Category Mean marker
PURPLE_SQUARE = '#8E44AD'  # Category Median marker
EMPIRICAL_GREEN = '#27ae60'# Empirical study markers
COMPUTATIONAL_BLUE = '#2980b9' # Computational / Theory study markers
MUTED_GRAY = '#95a5a6'     # Null baseline / other

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['axes.labelsize'] = 9
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 8
plt.rcParams['figure.titlesize'] = 11
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

def save_publication_figure(fig: plt.Figure, output_stem: Path) -> Tuple[Path, Path]:
    output_stem.parent.mkdir(parents=True, exist_ok=True)
    png_path = output_stem.with_suffix('.png')
    svg_path = output_stem.with_suffix('.svg')
    fig.savefig(png_path, dpi=300)
    fig.savefig(svg_path)
    plt.close(fig)
    return png_path, svg_path

# 1. Figure 3 Family: Score-Distribution / Global Score Cloud
def render_score_distribution(
    categories: List[str],
    data_points: List[np.ndarray],
    means: List[float],
    medians: List[float],
    title: str = 'Score Distribution',
    y_label: str = 'Score [-1.0, +1.0]',
    output_stem: Optional[Path] = None
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(6.8, 3.6), dpi=300)
    ax.axhline(0.0, color='black', linewidth=0.8, linestyle='-', zorder=1)
    for y_ref in [-1.0, -0.5, 0.5, 1.0]:
        ax.axhline(y_ref, color='lightgray', linewidth=0.5, linestyle='--', zorder=1)

    np.random.seed(42)
    x_positions = np.arange(len(categories))
    for i, (vals, m_val, med_val) in enumerate(zip(data_points, means, medians)):
        jitter = np.random.uniform(-0.18, 0.18, size=len(vals))
        ax.scatter(i + jitter, vals, color=PALE_BLUE, s=14, alpha=0.55, edgecolors='none', zorder=2)
        ax.scatter(i, m_val, color=RED_DIAMOND, s=42, marker='D', edgecolors='black', linewidth=0.6, zorder=3, label='Mean' if i == 0 else '')
        ax.scatter(i, med_val, color=PURPLE_SQUARE, s=36, marker='s', edgecolors='black', linewidth=0.6, zorder=3, label='Median' if i == 0 else '')

    ax.set_xticks(x_positions)
    ax.set_xticklabels(categories, fontsize=8.5, fontweight='bold')
    ax.set_ylabel(y_label, fontsize=9, fontweight='bold')
    ax.set_ylim(-1.15, 1.15)
    ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax.set_title(title, fontsize=10.5, fontweight='bold', pad=10)
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False, fontsize=8)
    plt.tight_layout()
    if output_stem:
        save_publication_figure(fig, output_stem)
    return fig

# 2. Figure 4 Family: Multi-Panel Consistency Dashboard
def render_consistency_dashboard(
    matrix_data: np.ndarray,
    matrix_labels: List[str],
    grouped_bars: Dict[str, Tuple[List[float], List[float]]],
    benchmark_line: Optional[float] = None,
    benchmark_label: str = 'Benchmark',
    title: str = 'Consistency Dashboard',
    output_stem: Optional[Path] = None
) -> plt.Figure:
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 6.8), dpi=300)
    im = axes[0, 0].imshow(matrix_data, cmap='coolwarm', vmin=0, vmax=np.nanmax(matrix_data) if np.nanmax(matrix_data) > 0 else 1.0)
    fig.colorbar(im, ax=axes[0, 0], fraction=0.046, pad=0.04, label='Distance / MSD')
    axes[0, 0].set_title('Pairwise Distance Matrix', fontsize=9.5, fontweight='bold')
    axes[0, 0].set_xticks(range(len(matrix_labels)))
    axes[0, 0].set_xticklabels([m[:8] for m in matrix_labels], rotation=45, ha='right', fontsize=7)
    axes[0, 0].set_yticks(range(len(matrix_labels)))
    axes[0, 0].set_yticklabels([m[:8] for m in matrix_labels], fontsize=7)

    panel_positions = [(0, 1), (1, 0), (1, 1)]
    for idx, (h_key, (lo_vals, go_vals)) in enumerate(grouped_bars.items()):
        if idx >= len(panel_positions): break
        r, c = panel_positions[idx]
        ax = axes[r, c]
        x = np.arange(len(matrix_labels))
        w = 0.35
        ax.bar(x - w/2, lo_vals, width=w, color=LO_COLOR, label='LO context' if idx == 0 else '')
        ax.bar(x + w/2, go_vals, width=w, color=GO_COLOR, label='GO context' if idx == 0 else '')
        if benchmark_line is not None:
            ax.axhline(benchmark_line, color='black', linestyle=':', label=benchmark_label if idx == 0 else '')
        ax.set_title(f'{h_key} Disagreement', fontsize=9.5, fontweight='bold')
        ax.set_ylabel(f'Pairwise MSD ({h_key})', fontsize=8.5)
        ax.set_xticks(x)
        ax.set_xticklabels([m[:8] for m in matrix_labels], rotation=45, ha='right', fontsize=7)

    axes[0, 1].legend(loc='upper right', fontsize=7, frameon=True)
    fig.suptitle(title, fontsize=11, fontweight='bold', y=0.98)
    plt.tight_layout()
    if output_stem:
        save_publication_figure(fig, output_stem)
    return fig

# 3. Figure 5 Family: Square Distance Matrix
def render_distance_matrix(
    matrix_data: np.ndarray,
    labels: List[str],
    title: str = 'Pairwise Distance Matrix',
    cbar_label: str = 'MSD',
    vmin: float = 0.0,
    vmax: float = 0.6,
    cmap: str = 'coolwarm',
    output_stem: Optional[Path] = None
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=300)
    im = ax.imshow(matrix_data, cmap=cmap, vmin=vmin, vmax=vmax)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label=cbar_label)
    ax.set_title(title, fontsize=10.5, fontweight='bold', pad=12)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=90, fontsize=6.5)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=6.5)
    plt.tight_layout()
    if output_stem:
        save_publication_figure(fig, output_stem)
    return fig

# 4. Figure 6 Family: Two-Panel Paired Context Trace
def render_paired_context_traces(
    study_labels: List[str],
    lo_values: List[float],
    go_values: List[float],
    lo_mean: float,
    go_mean: float,
    title_lo: str = 'Local Oddball (LO) Context Distance',
    title_go: str = 'Global Oddball (GO) Context Distance',
    y_label: str = 'MSD to Benchmark',
    output_stem: Optional[Path] = None
) -> plt.Figure:
    fig, axes = plt.subplots(2, 1, figsize=(9.5, 6.0), dpi=300, sharex=True)
    x = range(len(study_labels))

    axes[0].scatter(x, lo_values, color=LO_COLOR, s=35, marker='o', edgecolors='black', linewidth=0.4, label='LO Context')
    axes[0].axhline(lo_mean, color=LO_COLOR, linestyle='--', linewidth=0.9, label=f'Mean LO = {lo_mean:.3f}')
    axes[0].set_ylabel(y_label, fontsize=8.5, fontweight='bold')
    axes[0].set_title(title_lo, fontsize=9.5, fontweight='bold', loc='left')
    axes[0].legend(loc='upper right', frameon=True, fontsize=8)
    axes[0].grid(True, color='lightgray', linestyle='--', alpha=0.5)

    axes[1].scatter(x, go_values, color=GO_COLOR, s=35, marker='s', edgecolors='black', linewidth=0.4, label='GO Context')
    axes[1].axhline(go_mean, color=GO_COLOR, linestyle='--', linewidth=0.9, label=f'Mean GO = {go_mean:.3f}')
    axes[1].set_ylabel(y_label, fontsize=8.5, fontweight='bold')
    axes[1].set_title(title_go, fontsize=9.5, fontweight='bold', loc='left')
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(study_labels, rotation=90, fontsize=7)
    axes[1].legend(loc='upper right', frameon=True, fontsize=8)
    axes[1].grid(True, color='lightgray', linestyle='--', alpha=0.5)

    plt.tight_layout()
    if output_stem:
        save_publication_figure(fig, output_stem)
    return fig
