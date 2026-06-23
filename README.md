# MLLM: Multi-LLM Ontology-Constrained Evidence-Mapping Pipeline

A local ontology-constrained pipeline for mapping heterogeneous neuroscience literatures into auditable model-derived evidence spaces using a council of large language models.

## Overview

This repository provides an **ontology-constrained multi-LLM pipeline** for evidence mapping in scientific literature, with particular application to predictive coding hypothesis evaluation. It includes:

- **Pipeline Controller** (`mllm-pipeline.py`): Orchestrates document ingestion, multimodal extraction, model-council inference, output validation, and result serialization
- **HPC-36 Glossary** (`src/mllm/skills/glossary/HPC/hpc-36-reference.md`): 36-factor ontology for hierarchical predictive coding, organized into predictive suppression, feedforward error propagation, and ubiquity
- **Unified Evaluation Prompt** (`src/mllm/skills/instructions/hpc_eval_prompt.md`): Structured scoring instructions for local and global oddball contexts
- **DeepRead Extraction** (`src/mllm/data/loaders.py`): PDF text extraction with figure-aware document consolidation
- **Model Profiles** (`src/mllm/config/profiles/`): Configuration templates for local MLX-LM model execution
- **Agreement and Geometry Metrics**: Agent Consistency, Literature Consistency, Literature-Agent Consistency, and hypothesis-space dispersion analysis

## Associated Publication

This repository contains the software implementation used in:

> **Nejat, H., Maier, A., Spencer-Smith, J., Bastos, A.M. (2026).**
> **"Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature."**
> arXiv:[2606.05206](https://arxiv.org/abs/2606.05206) [q-bio.NC]

| | |
|---|---|
| **Paper title** | Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature |
| **Authors** | Hamed Nejat, Alexander Maier, Jesse Spencer-Smith, André M. Bastos |
| **arXiv** | [arxiv.org/abs/2606.05206](https://arxiv.org/abs/2606.05206) |
| **arXiv subjects** | q-bio.NC (Neurons and Cognition), cs.AI (Artificial Intelligence), stat.AP (Applications) |
| **Submitted** | 2026-05-23 |
| **DOI** | [10.48550/arXiv.2606.05206](https://doi.org/10.48550/arXiv.2606.05206) (arXiv preprint DOI; no journal DOI on record as of this writing — check the arXiv listing for the current status) |

**How this repository relates to the paper:** the repository implements the ontology-constrained multi-LLM literature-synthesis pipeline described in the manuscript — the HPC-36 glossary, the local/global-oddball evaluation prompt, the 10-model reasoning council, the DeepRead figure-aware PDF extraction, and the consensus/agreement aggregation — and provides the tooling required to reproduce the reported workflow. It also ships the manuscript's aggregated result table and figure-generation notebook under [`examples/`](examples/) (`hpc_table_final.csv` + `MLLM_HPCA_ORG.ipynb`). It does **not** bundle the manuscript's 31-paper corpus or the trained/fine-tuned model weights (those require the corpus and Apple Silicon model council described in [docs/MODELS_AND_RUNTIME.md](docs/MODELS_AND_RUNTIME.md)). See [docs/MANUSCRIPT_MAPPING.md](docs/MANUSCRIPT_MAPPING.md) for a detailed figure-by-figure, stage-by-stage traceability matrix, and [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md#manuscript--repository-mapping) for a high-level component map.

### Citation

If you use this software, please cite the manuscript:

**Plain text:**

> Nejat, H., Maier, A., Spencer-Smith, J., & Bastos, A. M. (2026). Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature. *arXiv preprint* arXiv:2606.05206.

**BibTeX:**

```bibtex
@misc{nejat2026ontology,
  title         = {Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature},
  author        = {Nejat, Hamed and Maier, Alexander and Spencer-Smith, Jesse and Bastos, Andre M.},
  year          = {2026},
  eprint        = {2606.05206},
  archivePrefix = {arXiv},
  primaryClass  = {q-bio.NC},
  url           = {https://arxiv.org/abs/2606.05206},
  doi           = {10.48550/arXiv.2606.05206},
  note          = {Code: \url{https://github.com/HNXJ/mllm-public}}
}
```

**Citing the software itself** (independent of the paper, e.g. for a specific code version): use the metadata in [`CITATION.cff`](CITATION.cff) — GitHub renders a "Cite this repository" button from this file, or run `cffconvert --format bibtex` against it locally.

**Citing the models:** the reasoning-council models retain their own licenses and citation requirements — see [docs/MODELS_AND_RUNTIME.md → Model Cards and Licensing](docs/MODELS_AND_RUNTIME.md#1-model-cards-and-licensing) and cite each model's original paper/card from Hugging Face in addition to the above.

### Resources

- **[Models & Runtime](docs/MODELS_AND_RUNTIME.md)** — 10-model specification, decoding parameters, installation, and model licensing caveats
- **[Reproducibility Guide](docs/REPRODUCIBILITY.md)** — Complete pipeline architecture, ontology, scoring methodology, examples, and interpretation guidelines
- **[Tested Environments](docs/TESTED_ENVIRONMENTS.md)** — Exact OS/Python/package versions and hardware this repository has been verified on
- **[Nature Compliance Report](docs/NATURE_COMPLIANCE_REPORT.md)** — Checklist mapping of this repository against the Nature Code and Software Submission Checklist

### Quick Links

- **New here? Start with the [Demo](#demo)** — a < 1 second, offline, no-GPU walkthrough in `demo/`
- Core Glossary: `src/mllm/skills/glossary/HPC/hpc-36-reference.md`
- Evaluation Prompt: `src/mllm/skills/instructions/hpc_eval_prompt.md`
- Main Entrypoint: `mllm-pipeline.py`
- Unit Tests: `tests/unit/`
- Integration Tests: `tests/integration/test_hpc_eval.py`

## Repository Layout

```
demo/                       Reviewer-friendly, offline, model-free demo (see Demo section below)
├── README.md               Demo-specific instructions, expected output, runtime
├── run_demo.py              Runnable end-to-end demo script (no GPU/network required)
├── sample_input/            Small synthetic input dataset (≈4 KB, 4 files)
└── expected_output/         Reference outputs to diff your run against
docs/                       Manuscript, reproducibility, and runtime documentation
├── MODELS_AND_RUNTIME.md   10-model specifications, decoding params, MLX-LM setup
├── REPRODUCIBILITY.md      7-stage pipeline architecture, scoring methodology, examples
├── TESTED_ENVIRONMENTS.md  Verified OS/Python/package versions and hardware
├── NATURE_COMPLIANCE_REPORT.md  Checklist compliance evidence table
├── examples/               Generated examples and runtime logs
└── runtime/                Runtime guides (e.g., LMS hardening)
examples/                   Manuscript result table + figure-generation notebook (see examples/README.md)
├── MLLM_HPCA_ORG.ipynb     Notebook with HPC-36 analysis and visualization (verified runnable)
├── hpc_table_final.csv     Manuscript's aggregated "HPC Grand Table" council result table
└── README.md               Contents, provenance, how-to-run, and a flagged data/doc discrepancy
scripts/                    Public reusable scripts (queue runners, status checks)
├── maintenance/            Maintenance utilities (profile updates, etc.)
├── overnight_hpc_queue.sh  Example HPC paper evaluation queue
└── mllm_status.sh          Pipeline status monitoring (configurable via env vars)
src/mllm/                   Pipeline package source
├── skills/glossary/HPC/    HPC-36 ontology and factor definitions
├── skills/instructions/    Evaluation prompts and scoring rules
├── data/                   Data loaders, parsers, and score aggregators (PDF extraction, JSON rescue, consensus)
├── codes/scripts/          Internal pipeline scripts
└── config/profiles/        Model configuration profiles
tests/                      Unit and integration tests
config/                     Configuration templates
pyproject.toml              Package metadata and dependencies
mllm-pipeline.py            Public CLI entrypoint for pipeline execution (requires a local MLX engine + model weights)
```

### Directory Notes

- **demo/**: The fastest path to verifying this repository works. Fully offline, no model weights or GPU required, runs in under a second. See [Demo](#demo) below.
- **data/**: Not tracked in this repository (see `.gitignore`); some scripts and notebooks under `examples/` expect a locally-generated `data/` directory of CSV/lookup tables when reproducing full manuscript figures (see [Reproducibility Guide](docs/REPRODUCIBILITY.md)). It is **not** required to run the demo.
- **examples/**: The manuscript's aggregated result table (`hpc_table_final.csv`) and figure-generation notebook (`MLLM_HPCA_ORG.ipynb`), verified runnable end-to-end against the shipped CSV — see [`examples/README.md`](examples/README.md), which also documents a flagged model-name discrepancy between this CSV and `docs/MODELS_AND_RUNTIME.md`.
- **outputs/**: Generated locally when running the real pipeline or notebooks; not tracked by default unless included as examples.

## System Requirements

There are two relevant configurations, depending on what you want to do:

| | **Demo path** (`demo/`) | **Full pipeline** (`mllm-pipeline.py`, real model council) |
|---|---|---|
| **Purpose** | Verify the repository's data/consensus logic works | Reproduce manuscript-style evidence mapping with real LLMs |
| **Operating systems** | Any OS that runs Python 3.10+: Linux, macOS, Windows (incl. WSL) | macOS on Apple Silicon (M1/M2/M3/M4) — required for the MLX runtime |
| **OS actually tested** | macOS 26.5.1 (Build 25F80), Darwin kernel 25.5.0, arm64 | macOS 26.5.1, Apple Silicon (M1 Max). See [docs/TESTED_ENVIRONMENTS.md](docs/TESTED_ENVIRONMENTS.md) |
| **Python version(s)** | 3.10–3.13 (tested with **3.13.7**) | 3.10–3.13 |
| **Key package versions** | `pandas` (tested 3.0.3), `pydantic` (tested 2.13.4) — see `pyproject.toml` for full pinned ranges | Same, plus `mlx`, `mlx-lm` (see [docs/MODELS_AND_RUNTIME.md](docs/MODELS_AND_RUNTIME.md)) |
| **Hardware** | Any laptop/desktop CPU; no GPU/accelerator | Apple Silicon GPU (unified memory architecture); MLX is **not** supported on Intel Mac, Linux, or Windows |
| **Memory** | < 200 MB | ≥32 GB unified memory recommended (16 GB minimum with aggressive model offloading); varies per model, see model profiles in `src/mllm/config/profiles/` |
| **GPU / accelerator** | None required | Apple Silicon integrated GPU via MLX (Metal). No CUDA/ROCm support. |
| **Network access** | None required | Required once, to download model weights from Hugging Face (unless already cached locally) |

Exact dependency versions are pinned as minimums in [`pyproject.toml`](pyproject.toml); see [docs/TESTED_ENVIRONMENTS.md](docs/TESTED_ENVIRONMENTS.md) for the precise versions this repository has been verified against, including any items not yet independently re-verified (marked `TODO`).

## Installation Guide

### Demo path (recommended starting point)

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public
python3 -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -e .
```

**Typical installation time:** **1–3 minutes** on a normal desktop computer with a broadband connection (dominated by downloading `pandas`/`pydantic`/`PyMuPDF` wheels; no model weights are needed for the demo).

### Full pipeline path (real model council, Apple Silicon only)

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
pip install "mlx>=0.4.0" "mlx-lm>=0.15.0"
export MLX_MODEL_ROOT=./mlx_models   # or your model directory
```

Model weights are **not bundled** with this repository (they are large, third-party artifacts hosted on Hugging Face). On first use, `mlx-lm` downloads the requested model into `MLX_MODEL_ROOT`/the Hugging Face cache; see [docs/MODELS_AND_RUNTIME.md](docs/MODELS_AND_RUNTIME.md) for the 10-model manuscript council, sizes, and licensing caveats.

**Typical installation time:** 1–3 minutes for the Python environment (as above), **plus 5–60+ minutes per model** for weight download, depending on model size (12B–70B parameters) and network speed. This step is not required for the demo.

## Demo

A complete, offline, reviewer-friendly demo lives in [`demo/`](demo/) — see [`demo/README.md`](demo/README.md) for full details. Summary:

**Run:**

```bash
python demo/run_demo.py
```

**Demo input:** [`demo/sample_input/`](demo/sample_input/) — 3 small synthetic per-model evaluation JSON files plus 1 raw/noisy LLM-style text response (all placeholder data, not manuscript data; see provenance note in `demo/README.md`).

**Expected output:** 3 files written to `demo/demo_output/` (git-ignored working directory):

```
demo/demo_output/
├── aggregated_scores.csv        # 24 rows: one per (Study, Model, Context, Factor)
├── consensus_summary.csv        # 16 rows: one per (Study, Context, Factor), with mean/median/std/n
└── consensus_summary.json       # same consensus table as JSON records
```

A verified reference copy of these exact files is committed at [`demo/expected_output/`](demo/expected_output/) — diff your run against it:

```bash
diff demo/demo_output/consensus_summary.csv demo/expected_output/consensus_summary.csv
```

No differences means your installation reproduces the demo exactly.

**Expected runtime:** **under 1 second** (measured 0.01–0.3s) on a normal desktop computer. No GPU, no network access, and no LLM inference is involved — only JSON parsing and `pandas` aggregation.

## Instructions for Use

### Running on your own data

**To aggregate your own pre-generated model evaluation JSON files** (no LLM calls, fully offline — same code path as the demo):

```python
from pathlib import Path
from mllm.data.preprocessors import aggregate_scores_from_json

df = aggregate_scores_from_json(Path("./your_outputs_dir"))
df.to_csv("aggregated_scores.csv", index=False)
```

**Input format:** one JSON file per (paper, model) pair, named `{paper_stem}_{model_id}_eval.json`, containing either:
- `lo_evaluations` / `go_evaluations` dicts (factor name → score in `[-1.0, 1.0]` or `null`), or
- a generic `scores` field (list of `{"factor_name", "score"}` objects, or a flat `{factor: score}` dict)

See [docs/REPRODUCIBILITY.md → Output Schema](docs/REPRODUCIBILITY.md#2-evaluation-prompt--scoring-methodology) for the exact contract, and [`src/mllm/schemas.py`](src/mllm/schemas.py) for the enforced Pydantic models.

**Output format:** a long-form CSV/DataFrame with columns `Study, Model, Context, Factor, Score` — directly pivotable for consensus statistics, as shown in [`demo/run_demo.py`](demo/run_demo.py).

**To run the full pipeline on your own PDFs** (requires the full-pipeline installation above and a running MLX engine):

```bash
python mllm-pipeline.py \
  --pdfs_to_process paper1.pdf paper2.pdf \
  --reasoning_model_names gpt-oss-20b-claude-4.5-mlx \
  --mllm_input_path ./inputs \
  --mllm_output_path ./outputs \
  --engine_url http://localhost:4474
```

**Configuration options** (full list in [docs/REPRODUCIBILITY.md → Pipeline Entrypoint](docs/REPRODUCIBILITY.md#3-pipeline-entrypoint)):

| Option | Purpose |
|---|---|
| `--pdfs_to_process` | PDF filenames to evaluate (placed in `--mllm_input_path`) |
| `--reasoning_model_names` | One or more model profile names from `src/mllm/config/profiles/` |
| `--glossary_path` / `--instructions_path` | Override the ontology glossary / scoring instructions |
| `--mllm_input_path` / `--mllm_output_path` | Input PDF directory / output JSON directory |
| `--engine_url` | MLX/OpenAI-compatible engine endpoint |
| `--deepread_vlm` | Vision-language model used for figure extraction |
| `--test_profile` | Verify model availability without processing papers |
| `--repair` | Skip extraction, reuse cached DeepRead markdown if present |

To verify model availability before a full run (optional):

```bash
python mllm-pipeline.py --test_profile --reasoning_model_names gpt-oss-20b-claude-4.5-mlx
```

## Core Public Artifacts

| Artifact | Path | Purpose |
|----------|------|---------|
| **HPC-36 Glossary** | `src/mllm/skills/glossary/HPC/hpc-36-reference.md` | 36-factor ontology for predictive coding research |
| **Evaluation Prompt** | `src/mllm/skills/instructions/hpc_eval_prompt.md` | Structured reasoning prompt + scoring methodology |
| **Pipeline** | `mllm-pipeline.py` | Main entrypoint for PDF → model council → consensus |
| **Model Profiles** | `src/mllm/config/profiles/` | Configuration for 10 reasoning models (MLX-LM) |
| **Data Loaders** | `src/mllm/data/loaders.py` | DeepRead: PDF extraction + figure description |
| **Tests** | `tests/unit/`, `tests/integration/` | Validation & integration tests |

## Important Notes

### Scope and Interpretation

This repository implements the public, reusable components of an ontology-constrained evidence-mapping workflow. It maps papers onto the HPC-36 predictive-coding ontology, preserves local execution where configured, records structured model outputs, and supports downstream agreement and dispersion analyses.

The resulting scores are model-derived evidence annotations. They are intended for auditable literature mapping, corpus comparison, and hypothesis-space analysis; they are not biological ground truth and should be interpreted together with the underlying papers, reasoning logs, and domain expertise.

### Scoring Interpretation

- **Scores range from −1.0 to +1.0**, with **null** for unaddressed factors
- **0.0** = factor explicitly tested but unsupported
- **null** = factor not mentioned (absence of evidence ≠ evidence of absence)
- **Council aggregate** = mean/median across models; reflects model agreement over extracted evidence, not biological truth

See [Reproducibility Guide](docs/REPRODUCIBILITY.md) for detailed scoring methodology.

## License

MIT License. See LICENSE file for details.

Models themselves are subject to their original licenses (check Hugging Face model cards).

---

For detailed reproducibility instructions, model specifications, and interpretation guidance, see **[docs/](docs/)** directory.
