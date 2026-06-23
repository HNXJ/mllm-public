# Reproducibility Guide

This document explains how to reproduce the multi-LLM evidence-mapping pipeline from the manuscript "Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature."

---

## Start Here: Minimal Reproducible Path (no models, no GPU)

If you have never seen this repository before, are not an MLX expert,
and do not have access to the 10-model council described below, start
with the **offline demo** instead of the full pipeline:

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public
pip install -e .
python demo/run_demo.py
```

This exercises the real `mllm.data.preprocessors.aggregate_scores_from_json`
and `parse_llm_output_as_json` functions — the same code that builds
the manuscript's result tables — on small synthetic data, in under a
second, with no network access, no GPU, and no model weights. See
[`demo/README.md`](../demo/README.md) for the exact expected output
and a diff-based correctness check against [`demo/expected_output/`](../demo/expected_output/).

The rest of this document describes the **full** manuscript pipeline,
which additionally requires Apple Silicon hardware and a local MLX
model council (see [docs/MODELS_AND_RUNTIME.md](MODELS_AND_RUNTIME.md)).

---

## Manuscript ↔ Repository Mapping

This repository accompanies Nejat, Maier, Spencer-Smith & Bastos (2026),
[arXiv:2606.05206](https://arxiv.org/abs/2606.05206). The table below maps
each major manuscript component to the concrete repository artifact that
implements it. A row marked **not in this repository** means the
manuscript-reported result depends on inputs (the 31-paper corpus,
downloaded model weights, or post-hoc analysis notebooks) that are not
shipped here, even though the code that *would* process them is. See
[docs/MANUSCRIPT_MAPPING.md](MANUSCRIPT_MAPPING.md) for the figure-by-figure
traceability matrix.

| Manuscript Component | Repository Component | Evidence |
|---|---|---|
| Ontology definition (HPC-36, 3 hypotheses × 12 factors) | [`src/mllm/skills/glossary/HPC/hpc-36-reference.md`](../src/mllm/skills/glossary/HPC/hpc-36-reference.md) | File present; full 36-row factor table verified by direct read |
| Evidence extraction (PDF → text + figure-aware markdown) | [`src/mllm/data/loaders.py`](../src/mllm/data/loaders.py) (`DeepReadLoader`) | Class present and importable; **requires a live VLM engine to execute — not run in this pass** |
| Figure processing (figure detection / description) | `src/mllm/deepread/` (VLM-based figure extraction invoked via `--deepread_vlm` / `--deepread_only` in `mllm-pipeline.py`) | Flag present in [`mllm-pipeline.py`](../mllm-pipeline.py) CLI; **VLM execution not independently re-verified this pass — requires Apple Silicon + model weights, see [docs/TESTED_ENVIRONMENTS.md](TESTED_ENVIRONMENTS.md) §2** |
| Multi-LLM council (10-model ensemble inference) | [`docs/MODELS_AND_RUNTIME.md`](MODELS_AND_RUNTIME.md) (model list + decoding params) + `--reasoning_model_names` in `mllm-pipeline.py` | Model list and decoding parameters documented; **live inference not run this pass (no MLX hardware in verification environment)** |
| Agreement analysis (cross-model consensus, agreement-bucket counts, mean-square-distance heatmaps) | [`src/mllm/data/preprocessors.py`](../src/mllm/data/preprocessors.py) (`aggregate_scores_from_json`) for consensus tables, **plus** [`src/mllm-visualization.py`](../src/mllm-visualization.py) (`agent_compare_summary_ordered`, `study_compare_summary_ordered`) and [`examples/MLLM_HPCA_ORG.ipynb`](../examples/MLLM_HPCA_ORG.ipynb) for the pairwise mean-square-distance ("MSD") agreement heatmaps referenced in `src/mllm/skills/README.md` as Agent/Literature/Literature-Agent Consistency | `preprocessors.py` path exercised end-to-end by [`demo/run_demo.py`](../demo/run_demo.py), output byte-identical to [`demo/expected_output/consensus_summary.csv`](../demo/expected_output/consensus_summary.csv). The result table that `mllm-visualization.py` and the notebook depend on now ships at [`examples/hpc_table_final.csv`](../examples/hpc_table_final.csv) (previously missing); the script's hardcoded path was fixed to point at it, and both the script and the notebook were re-run end-to-end in a clean venv producing all of their figures with no errors — see [`examples/README.md`](../examples/README.md) and [docs/MANUSCRIPT_MAPPING.md §5](MANUSCRIPT_MAPPING.md#5-output-validation--score-table-construction) for the run receipts |
| Hypothesis-space mapping (score tables and 3D scatter across H1/H2/H3 × LO/GO) | `lo_evaluations` / `go_evaluations` schema in [`src/mllm/schemas.py`](../src/mllm/schemas.py) (`HpcEvaluationResponse`) for score tables; [`src/mllm-visualization.py`](../src/mllm-visualization.py) (`plot_3d_scatter`, `plot_2d_h_comparison`) and [`examples/MLLM_HPCA_ORG.ipynb`](../examples/MLLM_HPCA_ORG.ipynb) for the "HPC Hypothesis Space" 3D/2D plots | Schema validated by [`tests/unit/test_schemas.py`](../tests/unit/test_schemas.py); demo produces a real aggregated score table. The 3D/2D plotting functions in `mllm-visualization.py` were re-run against the now-shipped `examples/hpc_table_final.csv`, producing all figures with no errors; the notebook required one pandas-compatibility bug fix (see [`examples/README.md`](../examples/README.md#known-issue-fixed-during-integration)) before it also produced all 14 figures — see [docs/MANUSCRIPT_MAPPING.md §6](MANUSCRIPT_MAPPING.md#6-hypothesis-space-mapping--visualization) |
| Hypothesis-space "temperature" metric (geometric dispersion of council scores) | **Not located in this repository as a named function or script** | Grepped for `temperature`, `dispersion`, and related terms in `src/mllm/`; no implementing code found in the current snapshot. The manuscript abstract describes this as a geometric metric over the council's score distribution — it is **not shipped in this repository as of this audit**. See [docs/MANUSCRIPT_MAPPING.md](MANUSCRIPT_MAPPING.md) for the explicit gap entry. |

---

## Pipeline Overview

The MLLM (Multi-LLM) pipeline is a **seven-stage ontology-constrained evidence-mapping system**. In the manuscript, it maps a 31-study predictive-processing corpus onto the HPC-36 ontology across local and global oddball contexts:

```
┌─────────────────────────────────────────────────────────────────┐
│ STAGE 1: PDF/Text Ingestion & Figure Extraction                 │
│ └─ Input: Neuroscience PDFs                                     │
│ └─ Output: Interleaved markdown (text + figure descriptions)    │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 2: Study Text Preparation                                 │
│ └─ Tokenize manuscript                                          │
│ └─ Format metadata (author, year, study design)                │
│ └─ Validate token count against context window                 │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 3: Ontology-Constrained Prompt Assembly                   │
│ └─ Load HPC-36 factor glossary                                 │
│ └─ Load scoring methodology rules                              │
│ └─ Construct unified evaluation prompt                         │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 4: Multi-Model Council Inference                          │
│ └─ Query all 10 reasoning models in parallel (or serial)       │
│ └─ Decoding params: temp=0.70, top-p=0.9, min-p=0.1           │
│ └─ Collect structured JSON outputs                            │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 5: Output Validation & Score-Table Construction                  │
│ └─ Validate JSON structure (all 36 factors present)            │
│ └─ Validate score ranges [-1.0, +1.0] and null                │
│ └─ Compute model aggregates and agreement metrics across council   │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 6: Result Serialization                                   │
│ └─ Write per-model scores (JSON)                               │
│ └─ Write consensus aggregates                                  │
│ └─ Preserve reasoning logs and evidence citations              │
├─────────────────────────────────────────────────────────────────┤
│ STAGE 7: Visualization & Reporting (Optional)                   │
│ └─ Generate score distributions, agreement matrices, and hypothesis-space visualizations │
│ └─ Export statistics tables (mean, std, n-sample per factor)   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core Public Artifacts

### 1. **Glossary: HPC-36 Reference**

**File:** `src/mllm/skills/glossary/HPC/hpc-36-reference.md`

**Content:** 36-factor neuroscience ontology for Hierarchical Predictive Coding, organized into 3 hypothesis groups:

- **H1: Predictive Suppression** (12 factors) — Neural mechanisms suppressing expected stimuli
- **H2: Feedforward Error Propagation** (12 factors) — Ascending prediction-error signals
- **H3: Ubiquity** (12 factors) — Cross-cortical, cross-modal, cross-species conservation

**Format:** Markdown table with columns:
- Factor ID (1–36)
- Factor Name
- Definition
- Measurement Tag (Quantitative / Qualitative / Methodological)
- Experimental Context (LO = Local Oddball; GO = Global Oddball; LO+GO = Both)

**Usage:** Loaded as input to every model evaluation; all outputs must include exactly these 36 keys.

---

### 2. **Evaluation Prompt & Scoring Methodology**

**File:** `src/mllm/skills/instructions/hpc_eval_prompt.md`

**Content:** Multi-part instruction set for all 10 models:

#### Role Definition
Models are prompted as "senior neuroscientist and biophysicist" evaluating predictive-coding mechanisms.

#### Scoring Methodology

| Score | Meaning | Example |
|-------|---------|---------|
| **+1.0** | Strong quantitative evidence **SUPPORTS** the factor | "Figure 3 shows inhibitory firing rate reduction of 35% for predictable stimuli" |
| **+0.6** | Moderate evidence **SUPPORTS** the factor | "Text reports reduced pyramidal activity in expected conditions (p < 0.05)" |
| **+0.2** | Weak evidence **SUPPORTS** the factor | "Qualitative description of suppressed responses in method section" |
| **0.0** | Factor is **ADDRESSED BUT NEUTRAL/CONTRADICTORY** | Study tested the factor but found no significant effect or mixed results |
| **−0.2** | Weak evidence **AGAINST** the factor | "Methods section suggests control condition had similar firing rates" |
| **−0.6** | Moderate evidence **AGAINST** the factor | "Quantitative analysis reports 15% increase instead of expected decrease" |
| **−1.0** | Strong quantitative evidence **CONTRADICTS** the factor | "Statistical test (p < 0.001) shows opposite effect" |
| **null** | Factor is **NOT MENTIONED or CANNOT BE EVALUATED** | Study does not address VIP-mediated disinhibition at all |

#### Key Rules

1. **0.0 vs null distinction:**
   - **0.0:** Study explicitly addresses the factor but finds neutral or contradictory evidence
   - **null:** Study does not mention the factor; absence of evidence ≠ evidence of absence
   - *When in doubt, prefer null to avoid false negatives*

2. **Evidence Priority:**
   - Direct quantitative results (figures, tables, statistics) — highest weight
   - Qualitative descriptions — acceptable when quantitative unavailable
   - Methodological notes — for "Methodological" tagged factors

3. **Context Independence:**
   - LO (Local Oddball) and GO (Global Oddball) contexts scored separately
   - Never average or conflate scores across contexts
   - If a study uses both paradigms, provide two sets of evaluations

4. **Reasoning Transparency:**
   - For every non-null score: cite specific sections, figures, or tables
   - For null scores on expected factors: explain why the factor was marked missing
   - For 0.0 scores: explain which evidence was considered and why it was neutral

#### Output Schema

```json
{
  "lo_evaluations": {
    "Subtractive Inhibition (SST)": 0.8,
    "Divisive Inhibition (PV)": 0.5,
    "...36 factors...": "null"
  },
  "go_evaluations": {
    "Subtractive Inhibition (SST)": 0.2,
    "...36 factors...": "null"
  },
  "first_author": "Smith",
  "publication_year": "2024",
  "study_type": "Empirical",
  "agent_name": "gpt-oss-20b-claude-4.5-mlx",
  "reasoning_log_text": "Short evidence-based summary of key findings and scoring rationale."
}
```

---

### 3. **Pipeline Entrypoint**

**File:** `mllm-pipeline.py`

**Usage:**

```bash
python mllm-pipeline.py \
  --pdfs_to_process paper1.pdf paper2.pdf \
  --reasoning_model_names gpt-oss-20b-claude-4.5-mlx deepseek-r1-70b-mlx \
  --glossary_path ./src/mllm/skills/glossary/HPC/hpc-36-reference.md \
  --instructions_path ./src/mllm/skills/instructions/hpc_eval_prompt.md \
  --mllm_input_path ./inputs \
  --mllm_output_path ./outputs \
  --engine_url http://localhost:4474
```

**Options:**
- `--pdfs_to_process`: List of PDF filenames to evaluate
- `--reasoning_model_names`: List of model profiles to use (default: ['gpt-oss-20b-claude-4.5'])
- `--glossary_path`: Full path to HPC-36 glossary
- `--instructions_path`: Full path to evaluation prompt
- `--mllm_input_path`: Directory containing input PDFs (default: `./inputs` via env var `MLLM_INPUT_PATH`)
- `--mllm_output_path`: Directory for output JSON files (default: `./outputs` via env var `MLLM_OUTPUT_PATH`)
- `--engine_url`: Engine API endpoint (default: `http://localhost:4474` via env var `ENGINE_URL`)
- `--mode`: Engine type (`mlx` or `lms`; default: `mlx`)
- `--deepread_vlm`: VLM model for figure extraction (default: `qwen3.5-vl-4b-mlx-crack`)
- `--deepread_only`: Run figure extraction only (skip reasoning)
- `--test_profile`: Verify model availability without processing papers
- `--repair`: Skip DeepRead, use cached markdown if available

---

### 4. **Model Profiles**

**Directory:** `src/mllm/config/profiles/`

**Format:** JSON configuration files for each model, specifying:
- Model name / Hugging Face ID
- Context window
- Decoding parameters (temperature, max_tokens)
- Engine type (mlx, lms, vmlx)
- Availability status (verified / untested / failed)

**Profile Mapping:** When you use `--reasoning_model_names gpt-oss-20b-claude-4.5-mlx`, the pipeline:
1. Looks up `gpt-oss-20b-claude-4.5-mlx-full-profile.json`
2. Loads decoding parameters and context window from the profile
3. Maps the profile name to an MLX or Hugging Face model ID
4. Loads the model and runs inference

---

### 5. **Tests & Validation**

**Demo (no models required, < 1 second):** `demo/run_demo.py` — see [demo/README.md](../demo/README.md) and the [Minimal Reproducible Path](#start-here-minimal-reproducible-path-no-models-no-gpu) above. This is the fastest way to confirm a working installation.

**Unit Tests:** `tests/unit/`

- `test_schemas.py` — Validate output JSON structure against expected schema
- `test_prompts.py` — Verify prompt construction and variable interpolation
- `test_config.py` — Test profile loading and model manifest resolution
- `test_operators.py` — Test data preprocessing and token counting

**Integration Tests:** `tests/integration/`

- `test_hpc_eval.py` — Full pipeline test with a small paper or mock input (requires `RUN_HPC_INTEGRATION=1` and `HPC_MODEL_NAME` env var)

**Running Tests:**

```bash
# Unit tests (no models required)
pytest tests/unit/ -v

# Integration tests (requires MLX models)
export RUN_HPC_INTEGRATION=1
export HPC_MODEL_NAME=gpt-oss-20b-claude-4.5-mlx
export HPC_API_URL=http://localhost:4474
export ENGINE_API_KEY=mlx-server
pytest tests/integration/ -v
```

---

## Validation & Quality Checks

### 1. **Output JSON Validation**

Every model output is validated for:

✓ Valid JSON structure  
✓ All 36 factor keys present in `lo_evaluations`  
✓ All 36 factor keys present in `go_evaluations` (if applicable)  
✓ Score values in range [-1.0, +1.0] or null  
✓ Metadata fields (author, year, study_type, agent_name) present  

If validation fails, the entry is logged but does not halt the pipeline.

### 2. **Council Aggregation**

After all models have evaluated a paper:

- **Mean score:** `sum(scores) / len(scores)` where scores are non-null
- **Median score:** Middle value (robust to outliers)
- **Variance:** `sum((score - mean)^2) / n`
- **Agreement:** Count of models returning same score bucket [+1, +0.6, +0.2, 0, −0.2, −0.6, −1, null]

Consensus output format (example):

```json
{
  "paper_id": "Smith-2024",
  "factor": "Subtractive Inhibition (SST)",
  "context": "LO",
  "n_models": 10,
  "mean_score": 0.68,
  "median_score": 0.7,
  "variance": 0.095,
  "range": [0.2, 1.0],
  "agreement_bucket_counts": {
    "+1.0": 4,
    "+0.6": 3,
    "+0.2": 2,
    "0.0": 1,
    "null": 0
  }
}
```

---

## Null vs. Zero Scoring

**Critical distinction that affects downstream interpretation:**

| Scenario | Score | Reason |
|----------|-------|--------|
| Study measures VIP-mediated disinhibition; finds significant effect | **+0.6** (or similar) | Factor is addressed and supported |
| Study measures VIP disinhibition; finds NO significant effect | **0.0** | Factor is explicitly addressed but unsupported |
| Study never mentions VIP disinhibition | **null** | Factor is not addressed; cannot judge |
| Study measures something related but not identical (e.g., GABAergic inhibition generically) | **null** | VIP-specific mechanism is not addressed |

**Why this matters:**
- A **null** score leaves room for future evidence
- A **0.0** score says the hypothesis was tested and failed
- **Averaging null with 0.0 is misleading** (do not do this)

---

## Ontology-Constrained Prompting

The evaluation prompt uses **explicit schema enforcement**:

1. **Factor enumeration:** All 36 factors listed in the prompt
2. **Schema specification:** Required JSON output format shown in prompt
3. **Context isolation:** LO and GO contexts kept separate in prompt and output
4. **Measurement tags:** Quantitative vs. Qualitative vs. Methodological factors noted in glossary
5. **Rule restatement:** Evidence priority, null vs. 0.0 distinction, context independence all stated in prompt

This design minimizes:
- Factor invention (models introducing keys outside the ontology)
- Schema drift (output structure changes mid-evaluation)
- Context mixing (LO findings misattributed to GO context)
- Unjustified factorization (breaking a single paper result into multiple factor scores)

---

## Results Interpretation

### Per-Model Output

**File format:** `{paper_stem}_{model_id}_eval.json`

Example: `Smith-2024_gpt-oss-20b-claude-4.5-mlx_eval.json`

**Interpretation:** Represents one model-specific annotation of evidence support from the paper. It is one auditable council member output and is interpreted through the accompanying reasoning log.

### Consensus Output

**File format:** `{paper_stem}_consensus_hpc36.json` (or similar)

**Interpretation:**
- **High agreement (agreement ≥ 7/10 models):** The extracted evidence is consistently mapped by the council.
- **Mixed agreement (4–6 models agree):** The paper or factor requires closer inspection because model interpretations diverge.
- **Low agreement (≤ 3 models agree):** The evidence is sparse, indirect, or strongly dependent on model-specific interpretation.

### Interpretation Boundaries

Model outputs are structured annotations over the supplied paper text, figure descriptions, and ontology. Council agreement is evidence about reproducibility of the annotation process, not direct biological validation. Mechanistic conclusions should remain grounded in the source studies and, where relevant, independent empirical validation.

---

## Example Workflow

```bash
# 1. Set up environment
export MLX_MODEL_ROOT=./mlx_models
export MLLM_INPUT_PATH=./papers
export MLLM_OUTPUT_PATH=./results

# 2. Place PDFs in input directory
mkdir -p ./papers
cp Smith-2024.pdf Jones-2023.pdf Chen-2022.pdf ./papers/

# 3. Run pipeline with 2 models
python mllm-pipeline.py \
  --pdfs_to_process Smith-2024.pdf Jones-2023.pdf \
  --reasoning_model_names gpt-oss-20b-claude-4.5-mlx gemma-3-27b-it-8bit-mlx \
  --mllm_input_path ./papers \
  --mllm_output_path ./results

# 4. Check outputs
ls -lh ./results/
# Smith-2024_gpt-oss-20b-claude-4.5-mlx_eval.json
# Smith-2024_gemma-3-27b-it-8bit-mlx_eval.json
# Smith-2024_consensus.json
# Jones-2023_*.json
# ...

# 5. Visualize consensus (optional, via post-processing script)
python scripts/visualize_consensus.py --input_dir ./results
```

---

## Citation

See [README.md → Citation](../README.md#citation) for the canonical BibTeX
entry, plain-text citation, and citation instructions (kept in one place
to avoid drift between copies). Also cite the individual models and their
original papers — see [docs/MODELS_AND_RUNTIME.md → Model Cards and
Licensing](MODELS_AND_RUNTIME.md#1-model-cards-and-licensing).

---

**Last Updated:** 2026-05-23
**Pipeline Version:** 1.0.1 (manuscript-aligned public release)
