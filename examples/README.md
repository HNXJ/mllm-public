# Manuscript Result-Table Analysis & Figures

This directory contains the post-hoc analysis artifacts used to generate the
manuscript's hypothesis-space figures: the aggregated council result table
and the notebook/script that turn it into plots.

## Contents

| File | Description |
|---|---|
| [`hpc_table_final.csv`](hpc_table_final.csv) | The "HPC Grand Table" — 304 rows covering 31 literature studies × up to 10 council models, with per-context (`LO`/`GO`) per-hypothesis (`H1`/`H2`/`H3`) averages/std-devs and the 72 individual factor scores (`LO-F01`…`LO-F36`, `GO-F01`…`GO-F36`). This is the downstream consensus table the manuscript's figures are built from — distinct from, and built on top of, the per-model per-paper JSON files produced by the live pipeline (see [`src/jmllm/util/helpers.py`](../src/jmllm/util/helpers.py)). |
| [`MLLM_HPCA_ORG.ipynb`](MLLM_HPCA_ORG.ipynb) | The figure-generation notebook. Already sanitized for public release (no hardcoded Drive path); resolves its CSV via a candidate-path search that includes a plain relative `hpc_table_final.csv` — which is exactly this directory's layout. Produces 3D hypothesis-space scatter plots, pairwise mean-square-distance (MSD) agreement analysis, literature-vs-"this work" statistical comparisons (Wilcoxon/t-test), and shift-vector plots. |

The CLI command `jmllm-vis` (or `python -m jmllm.vis.cli`) is the canonical package implementation of these figures (3D scatter, agent-agent MSD heatmap, study-study MSD heatmap) and reads `hpc_table_final.csv` by default.

## Provenance

`hpc_table_final.csv` was added to this directory so the result table and
the notebook that visualizes it ship together, rather than the notebook
silently depending on a CSV that didn't exist anywhere in the repo.

## How to run

Both the notebook and the script require `pandas`, `numpy`, `plotly`, and
`scipy`. Install with:

```bash
pip install -e ".[viz]"
```

**Script / CLI:**

```bash
jmllm-vis --csv_path examples/hpc_table_final.csv --reports_dir examples/reports/
```

Writes HTML + SVG figures to `examples/reports/` (git-ignored — regenerate
locally rather than committing rendered output).

**Notebook:** open `MLLM_HPCA_ORG.ipynb` in Jupyter/JupyterLab and run all
cells. Outside Colab, it automatically falls back to the local
`hpc_table_final.csv` in this directory (see `_find_csv_path()` in the
function-library cell) and writes outputs to `./hpc_figures/` (also
git-ignored).

**Verified (2026-06-23):** the notebook's core function-library and run-all
cells were extracted and executed end-to-end against this exact
`hpc_table_final.csv` in a clean virtual environment, after one bug fix
(below) — all 14 figure handles generated with no errors. The script
(`jmllm-vis`) was previously verified against an equivalent
copy of this CSV under a different path and has since been repointed here.

## Known issue fixed during integration

`calculate_msd_matrix()` (notebook, function-library cell) originally called
`np.fill_diagonal(mat.values, np.nan)`. Under pandas's copy-on-write
behavior (default in recent pandas releases, including the 3.0.3 used in
this audit's verification environment — see
[`docs/TESTED_ENVIRONMENTS.md`](../docs/TESTED_ENVIRONMENTS.md)),
`DataFrame.values` can return a read-only array, so this raised
`ValueError: underlying array is read-only` and crashed every figure that
depends on `calculate_msd_matrix`. Fixed by setting the diagonal via `.loc`
instead of mutating `.values` directly. This is a pandas-version
compatibility fix, not a change to the statistics or figures themselves.

## Known data/documentation discrepancy (flagged, not silently resolved)

The model names (`agent_` column) in `hpc_table_final.csv` are:

```
deepseek-r1-distill-llama-70b, gemma-3-27b, gemma-4-31b,
gpt-oss-claude-4.5-sonnet, gpt-oss-safeguard-120b, mistral-nemo-12b-thinking,
olmo-3-32b-think, phi-4-reasoning-plus, qwen3-14b-gemini-3-pro,
qwen3.5-40b-claude-4.5-opus
```

[`docs/MODELS_AND_RUNTIME.md`](../docs/MODELS_AND_RUNTIME.md) lists the
10-model council with `qwen3-14b-claude-4.5-sonnet` in the 9th slot instead
of `gpt-oss-safeguard-120b`. This audit did not have enough information to
determine whether this reflects a model substitution made after
`MODELS_AND_RUNTIME.md` was last updated, a typo in one of the two sources,
or an intentional difference between the documented "intended" council and
the actual council used to produce this specific result table. **This is
reported as an open discrepancy for the maintainer to resolve** — see
[`docs/MANUSCRIPT_MAPPING.md`](../docs/MANUSCRIPT_MAPPING.md) §4.
