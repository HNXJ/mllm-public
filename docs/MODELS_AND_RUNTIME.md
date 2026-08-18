# Models, Councils, and Runtime Configurations

## Overview

This repository provides an ontology-constrained literature scoring pipeline for Hierarchical Predictive Coding (HPC-36) across local (LO) and global (GO) oddball experimental contexts.

It supports inference via:
1. **Local LM Studio Server (`lms`)**: OpenAI-compatible REST endpoint (`http://localhost:1234/v1` or custom host/port), portable to any Mac or Linux/Windows workstation.
2. **Apple Silicon / MLX-LM**: Native MLX acceleration for local Apple Silicon execution.

---

## 1. Model Registry & Evaluation Strata

To ensure rigorous validation without methodological contamination, evaluations are organized into **three distinct validation strata**:

```
                                 [ Scientific Literature Corpus ]
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
[ Strata 1: Human-Only Experts ]    [ Strata 2: Human+AI Experts ]       [ Strata 3: Autonomous Council ]
   (`content/tables/experts/human/`)   (`content/tables/experts/human_ai/`)   (`content/tables/original_council/`)
```

---

### A. Strata 1: Human-Only Domain Experts (`hpch_XX`)
Reserved exclusively for independent human-only domain expert evaluations:

| Expert ID | Expert Class | Source / Provenance | Protocol / Order | Description |
| :---: | :---: | :--- | :---: | :--- |
| **`hpch_01`** | `human` | Original Human Expert 1 Benchmark | Canonical | Ground-truth expert scoring from manuscript baseline. |
| *`hpch_02`* | `human` | *Pending Reviewer Panel 2* | *Independent* | *Reserved for upcoming independent human expert.* |
| *`hpch_03`* | `human` | *Pending Reviewer Panel 3* | *Independent* | *Reserved for upcoming independent human expert.* |

---

### B. Strata 2: Human + AI Collaborative Experts (`hpchai_XX`)
Evaluations conducted by human domain experts utilizing assistive LLM/VLM reasoning workflows:

| Expert ID | Expert Class | AI Model / Tooling | Protocol / Pass Order | Description |
| :---: | :---: | :--- | :---: | :--- |
| **`hpchai_01`** | `human_ai` | Gemini 2.5 Pro (`HT1g37f`) | $1 \longrightarrow 31$ (Forward Pass) | Initial context forward-pass literature evaluation. |
| **`hpchai_02`** | `human_ai` | Gemini 2.5 Pro (`HT2g37f`) | $31 \longrightarrow 1$ (Reverse Pass) | Cumulative synthesis reverse-pass literature evaluation. |
| *`hpchai_03+`* | `human_ai` | *Assisted Panels* | *Custom* | *Reserved for future assisted expert evaluations.* |

---

### C. Strata 3: Autonomous Multi-LLM Council & Robustness Sweeps
Autonomous LLM evaluations evaluated across the 31-paper corpus:

1. **Original 10-Model Council (Baseline Reference)**:
   - `gemma-3-27b-it`, `gemma-4-31b-it`, `deepseek-r1-distill-llama-70b`, `gpt-oss-claude-4.5-sonnet`, `mistral-nemo-12b-thinking`, `olmo-3-32b-think`, `phi-4-reasoning-plus`, `qwen3-14b-gemini-3-pro`, `gpt-oss-safeguard-120b`, `qwen3.5-40b-claude-4.5-opus`.
2. **202608 Robustness Sweep (837-Call Factorial Experiment)**:
   - 31 papers $\times$ 3 models (`gemma-4-31b-it`, `phi-4-reasoning-plus`, `olmo-3-32b-think`) $\times$ 3 temperatures ($T \in \{0.00, 0.35, 0.70\}$) $\times$ 3 repeats.

---

## 2. Directory Structure of Score Tables

All tables are organized under [`content/tables/`](../content/tables/):

```
content/tables/
├── experts/
│   ├── human/
│   │   ├── hpch_01.csv                        # Human Expert 1 (Ground-truth baseline)
│   │   └── hpch_all.csv                       # Combined human-only expert table
│   └── human_ai/
│       ├── hpchai_01.csv                      # Human+AI Expert 1 (HT1g37f forward pass)
│       ├── hpchai_02.csv                      # Human+AI Expert 2 (HT2g37f reverse pass)
│       └── hpchai_all.csv                     # Combined human+AI expert table
├── original_council/
│   ├── hpc_table_original_council.csv         # Full 10-model council wide table (304 rows)
│   └── aggregated_scores_baseline.csv         # Council aggregated baseline (31 rows)
└── robustness_202608/
    ├── scores_31x3x3x3_primary.csv            # 837-attempt authoritative structured scores (31,536 rows)
    ├── scores_analysis_provenance.csv         # Multi-tier provenance layer with completeness ratios
    └── calls_ledger_837.csv                   # Atomic runtime call ledger (837 rows)
```

---

## 3. Running with LM Studio (`lms`)

The pipeline runs seamlessly against any local or remote LM Studio instance:

```bash
# 1. Start your local model in LM Studio (or via CLI)
lms load gemma-4-31b-it --gpu=max

# 2. Run the robustness pipeline using the Python CLI
python -m jmllm.pipeline.robustness_runner \
  --base-url "http://localhost:1234/v1" \
  --api-key "lm-studio" \
  --model "gemma-4-31b-it" \
  --temperature 0.35 \
  --repeats 3
```
