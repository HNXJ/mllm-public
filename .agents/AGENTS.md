# Project-Scoped Rules — jmllm

## Command Workflow Actions
When the user triggers a workflow action, execute the corresponding protocol steps:
- **proceed with brainstorm**: Update design spec (Section 1) of `plan.json`.
- **proceed with plan**: Expand brainstorm into file rows and task columns in Section 2 of `plan.json`.
- **proceed with review**: Evaluate code, score health (X/100), and optimize plan in `review.json`.
- **proceed with progress**: Perform edits sequentially, logging tasks in `progress.json`.
- **inspect**: Check layout, align file rows, run `jn2md.py`, and run tests.

## PRP System — Compulsory Developer Protocol
Every repository must contain a standardized Plan-Review-Progress (PRP) tracking module under `artifacts/developer/`.
- **Directory Layout**: Restrict strictly to `plan.json`, `review.json`, `progress.json` (sources of truth), `plan.md`, `review.md`, `progress.md` (rendered markdown views), and `misc/jn2md.py` with `misc/archive/`.
- **Synchronization**: File tables across all three JSON files must contain identical file row structures and order. The `inspect` action compiles and renders Markdown views.
- **Scoring**: health/completeness score out of 100 per file (100/100 denotes fully verified standalone code).

## Domain & Project Context
- **User**: Hamm (hamednejat7@gmail.com). Computational biophysics.
- **Dargold Style**: Gamma "Aurum" theme — black background, gold accents, minimal text, figure placeholders only, equations rendered larger than body text, body text slightly reduced. Default style for technical/tutorial decks.
- **JAX Numerics**: Watch for recompilation, in-place mutation, dtype/shape drift; test with jit on AND off. Compose `jit(vmap(scan))` pure kernels.
- **jmllm (mllm-public)**: Literature evaluation pipeline. Uses sequential VLM extraction (DeepRead) and concurrent ThreadPoolExecutor LLM reasoning. Uses `gemma-4-e4b-it-mxfp8` local server on port 1234.

## Omission / Predictive Routing Analysis Rules
- **Skepticism & Rigor**: Statistical significance is mandatory for all multi-trial operations and trial-averaged plots.
- **Dual-Engine Validation**: Always provide both parametric (e.g., t-test, ANOVA) and nonparametric (e.g., Wilcoxon, Mann-Whitney) statistics.
- **False Positive Control**: Always apply multiple-comparisons corrections (e.g., Benjamini-Hochberg FDR, Bonferroni). Do not plot or report significance unless both parametric and nonparametric engines agree at the corrected threshold ($q < 0.05$).
