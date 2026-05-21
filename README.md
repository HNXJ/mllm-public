# MLLM: Multi-LLM Ontology-Constrained Evidence-Mapping Pipeline

A local, privacy-preserving pipeline for rapid evidence synthesis in neuroscience literature using a council of reasoning models and ontology-constrained structured scoring.

## Overview

This repository provides an **ontology-constrained multi-LLM pipeline** for evidence mapping in scientific literature, with particular application to predictive coding hypothesis evaluation. It includes:

- **Pipeline Controller** (`mllm-pipeline.py`): Orchestrates document ingestion, multi-model inference, consensus scoring, and result serialization
- **HPC-36 Glossary** (`src/mllm/skills/glossary/HPC/hpc-36-reference.md`): 36-factor neuroscience ontology for Hierarchical Predictive Coding
- **Unified Evaluation Prompt** (`src/mllm/skills/instructions/hpc_eval_prompt.md`): Structured reasoning instructions for 10 reasoning models
- **DeepRead Extraction** (`src/mllm/data/loaders.py`): Parallel text + figure extraction from PDF
- **Model Profiles** (`src/mllm/config/profiles/`): Configuration templates for 10 reasoning models
- **Consensus Aggregation**: Consensus scoring across model council with agreement metrics

## Manuscript

This repository supports the paper:

> **"Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature"**
> *Evaluating evidence for predictive coding mechanisms using a structured multi-model council*

### Reproducibility Resources

- **[Models & Runtime](docs/MODELS_AND_RUNTIME.md)** — 10-model specification, decoding parameters, installation, and model licensing caveats
- **[Reproducibility Guide](docs/REPRODUCIBILITY.md)** — Complete pipeline architecture, ontology, scoring methodology, examples, and interpretation guidelines

### Quick Links

- Core Glossary: `src/mllm/skills/glossary/HPC/hpc-36-reference.md`
- Evaluation Prompt: `src/mllm/skills/instructions/hpc_eval_prompt.md`
- Main Entrypoint: `mllm-pipeline.py`
- Unit Tests: `tests/unit/`
- Integration Tests: `tests/integration/test_hpc_eval.py`

## Repository Layout

```
data/                       Example data files and reference tables
├── hpc_table_final.csv     HPC-36 factor reference table for analysis
docs/                       Manuscript, reproducibility, and runtime documentation
├── MODELS_AND_RUNTIME.md   10-model specifications, decoding params, MLX-LM setup
├── REPRODUCIBILITY.md      7-stage pipeline architecture, scoring methodology, examples
├── examples/               Generated examples and runtime logs
└── runtime/                Runtime guides (e.g., LMS hardening)
examples/                   Reproducibility notebooks and analysis scripts
├── MLLM_HPCA_ORG.ipynb     Colab notebook with HPC-36 analysis and visualization
scripts/                    Public reusable scripts (queue runners, status checks)
├── maintenance/            Maintenance utilities (profile updates, etc.)
├── overnight_hpc_queue.sh  Example HPC paper evaluation queue
└── mllm_status.sh          Pipeline status monitoring (configurable via env vars)
src/mllm/                   Pipeline package source
├── skills/glossary/HPC/    HPC-36 ontology and factor definitions
├── skills/instructions/    Evaluation prompts and scoring rules
├── data/                   Data loaders (PDF extraction, figure handling)
├── codes/scripts/          Internal pipeline scripts
└── config/profiles/        Model configuration profiles
tests/                      Unit and integration tests
config/                     Configuration templates
pyproject.toml              Package metadata and dependencies
mllm-pipeline.py            Public CLI entrypoint for pipeline execution
```

### Directory Notes

- **data/**: Public example/reference files (small CSVs, lookup tables).
- **examples/**: Reproducibility notebooks and analysis scripts. Intended for Colab or Jupyter with relative paths to `data/`.
- **outputs/**: Generated locally when running notebooks; not tracked by default unless included as examples.

## Installation & Setup

### Requirements

- Python 3.10+
- MLX-LM and MLX (Apple Silicon recommended, or compatible hardware)
- 32+ GB unified memory (or 16GB with model offloading)

### Installation

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public
pip install -r requirements.txt  # or use pyproject.toml
export MLX_MODEL_ROOT=./mlx_models  # or your model directory
```

### Quick Test

```bash
# Verify model availability (optional)
python mllm-pipeline.py --test_profile --reasoning_model_names gpt-oss-20b-claude-4.5-mlx

# Run on sample papers
python mllm-pipeline.py \
  --pdfs_to_process paper1.pdf paper2.pdf \
  --mllm_input_path ./inputs \
  --mllm_output_path ./outputs
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

### What This Pipeline Does

✓ Maps neuroscience literature against an ontology of predictive coding mechanisms
✓ Uses local LLMs (privacy-preserving, no data sent to cloud)
✓ Aggregates multi-model perspectives into consensus scores
✓ Provides rapid evidence synthesis for literature triage

### What This Pipeline Does NOT Do

✗ Make biological claims (scores are model-inferred evidence proxies, not ground truth)
✗ Replace domain expert review (use for rapid synthesis, verify findings with subject experts)
✗ Guarantee correctness (models can hallucinate; requires human validation)
✗ Provide licensing or legal advice (consult model cards on Hugging Face for license terms)

### Scoring Interpretation

- **Scores range from −1.0 to +1.0**, with **null** for unaddressed factors
- **0.0** = factor explicitly tested but unsupported
- **null** = factor not mentioned (absence of evidence ≠ evidence of absence)
- **Consensus** = mean/median across 10 models; reflects agreement strength, not truth

See [Reproducibility Guide](docs/REPRODUCIBILITY.md) for detailed scoring methodology.

## License

MIT License. See LICENSE file for details.

Models themselves are subject to their original licenses (check Hugging Face model cards).

---

For detailed reproducibility instructions, model specifications, and interpretation guidance, see **[docs/](docs/)** directory.
