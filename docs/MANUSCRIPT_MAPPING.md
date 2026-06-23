# Manuscript Traceability Matrix

This document is a detailed, evidence-checked mapping between the components
of the manuscript

> Nejat, H., Maier, A., Spencer-Smith, J., Bastos, A.M. (2026).
> "Ontology-constrained multi-LLM scoring of hypothesis support in the
> predictive processing literature." [arXiv:2606.05206](https://arxiv.org/abs/2606.05206)

and the concrete code, configuration, scripts, and outputs in this
repository. For the high-level component map see
[docs/REPRODUCIBILITY.md → Manuscript ↔ Repository Mapping](REPRODUCIBILITY.md#manuscript--repository-mapping).

**Evidence standard for this document:** a row is marked **Implemented &
Verified** only if the cited file exists *and* was exercised in this
audit pass with an observed output. A row is marked **Implemented, Not
Re-run** if the code exists and is plausibly the right component, but
executing it requires resources unavailable in this audit (model weights,
Apple Silicon, or an external data file not shipped in the repo). A row is
marked **Not Found** if no implementing code was located after an explicit
search — this is reported as a gap, not glossed over.

The manuscript's exact figure/table numbering was **not available** to this
audit (no PDF/HTML rendering of the manuscript body was fetched, only the
arXiv abstract page and metadata API — see verification note at the end of
this document). Rows are therefore organized by **named component**, as
described in the abstract and corroborated by in-repo documentation, rather
than by a `Figure N` / `Table N` label. If the maintainer can supply the
manuscript's exact figure/table numbers, this document should be updated to
add that mapping explicitly.

---

## 1. Ontology / Glossary Layer

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| 36-factor HPC ontology (3 hypothesis families × 12 factors each) | **Implemented & Verified** | [`src/mllm/skills/glossary/HPC/hpc-36-reference.md`](../src/mllm/skills/glossary/HPC/hpc-36-reference.md) — full 36-row table read and confirmed: H1 Predictive Suppression (IDs 1–12), H2 Feedforward Error Propagation (IDs 13–24), H3 Ubiquity (IDs 25–36), each with Factor Name / Definition / Measurement Tag / Experimental Context (LO/GO/LO+GO) |
| HPC-Ontogram (3D visualization of ontology structure) | **Implemented, Not Re-run** | Referenced in [`src/mllm/skills/README.md`](../src/mllm/skills/README.md) ("HPC-Ontogram: A high-fidelity 3D visualization... created March 28, 2026"); the generating script was not located by name in this audit — **TODO: maintainer to confirm the exact script/notebook path** |

## 2. Evidence Extraction (PDF / Figure Ingestion)

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| PDF text extraction | **Implemented, Not Re-run** | [`src/mllm/data/loaders.py`](../src/mllm/data/loaders.py) (`DeepReadLoader`); uses PyMuPDF per [`pyproject.toml`](../pyproject.toml) dependency list. Class imports successfully; full extraction was not exercised this pass (no PDF corpus shipped, by design — see [docs/NATURE_COMPLIANCE_REPORT.md](NATURE_COMPLIANCE_REPORT.md)) |
| Figure-aware extraction / VLM figure description ("DeepRead") | **Implemented, Not Re-run** | `--deepread_vlm`, `--deepread_only`, `--repair` flags in [`mllm-pipeline.py`](../mllm-pipeline.py); default VLM `qwen3.5-vl-4b-mlx-crack`. Requires a running MLX VLM engine — not available in this audit environment (see [docs/TESTED_ENVIRONMENTS.md](TESTED_ENVIRONMENTS.md) §2) |
| Parallel multi-instance vision dispatch (4× Qwen2.5-VL workers) | **Implemented, Not Re-run** | [`src/mllm/codes/scripts/visualize_pipeline_3d.py`](../src/mllm/codes/scripts/visualize_pipeline_3d.py) documents this architecture as a flowchart (`ThreadPoolExecutor`, 4 parallel `Qwen2.5-VL` nodes) but is a **visualization-only** script, not the dispatch implementation itself; the actual dispatch logic was not located by this name search and is presumed to live in the DeepRead/loader code path — **TODO: maintainer to confirm exact dispatch module** |

## 3. Ontology-Constrained Prompt Assembly

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| Evaluation prompt template (role definition, scoring rubric, output schema) | **Implemented & Verified** | [`src/mllm/skills/instructions/hpc_eval_prompt.md`](../src/mllm/skills/instructions/hpc_eval_prompt.md) — full content confirmed via direct read, matches the scoring scale (+1.0…−1.0, null) and `lo_evaluations`/`go_evaluations` output schema documented in [docs/REPRODUCIBILITY.md §2](REPRODUCIBILITY.md#2-evaluation-prompt--scoring-methodology) |
| Output schema enforcement | **Implemented & Verified** | [`src/mllm/schemas.py`](../src/mllm/schemas.py) — `HpcEvaluationResponse` Pydantic model with `lo_evaluations`/`go_evaluations` dict fields; validated by [`tests/unit/test_schemas.py`](../tests/unit/test_schemas.py) (part of the 17-passed unit test run, see [docs/TESTED_ENVIRONMENTS.md](TESTED_ENVIRONMENTS.md) §1) |

## 4. Multi-LLM Council Inference

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| 10-model reasoning council | **Implemented, Not Re-run; ⚠️ documentation/data discrepancy found** | [`docs/MODELS_AND_RUNTIME.md`](MODELS_AND_RUNTIME.md) lists 10 models (gemma-3-27b-it, gemma-4-31b-it, deepseek-r1-distill-llama-70b, gpt-oss-claude-4.5-sonnet, mistral-nemo-12b-thinking, olmo-3-32b-think, phi-4-reasoning-plus, qwen3-14b-gemini-3-pro, **qwen3-14b-claude-4.5-sonnet**, qwen3.5-40b-claude-4.5-opus) with matching profile JSONs in [`src/mllm/config/profiles/`](../src/mllm/config/profiles/). The shipped result table [`examples/hpc_table_final.csv`](../examples/hpc_table_final.csv) instead has **`gpt-oss-safeguard-120b`** in that 9th slot, not `qwen3-14b-claude-4.5-sonnet` — confirmed by listing the `agent_` column's 10 unique values. **This is an unresolved discrepancy between the documented council and the council that actually produced this result table; reported here rather than silently reconciled** — see [`examples/README.md`](../examples/README.md#known-datadocumentation-discrepancy-flagged-not-silently-resolved). Live inference requires MLX hardware not available in this audit |
| Decoding parameters (temp=0.70, top-p=0.90, min-p=0.1, max_tokens=4096, context=131072) | **Implemented & Verified (as configuration)** | Confirmed present in [`docs/MODELS_AND_RUNTIME.md`](MODELS_AND_RUNTIME.md) and individual profile JSONs under `src/mllm/config/profiles/`; this is a configuration-correctness check (the values are recorded), not a runtime re-verification |
| Pipeline orchestration / model loading / unloading | **Implemented, Not Re-run** | [`mllm-pipeline.py`](../mllm-pipeline.py) `PipelineController` class (`load_model`, `unload_all`, `test_model_profile`, `run_pipeline`); imports successfully, full run not exercised (requires MLX engine) |

## 5. Output Validation & Score-Table Construction

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| JSON structure / score-range validation | **Implemented & Verified** | `HpcEvaluationResponse` Pydantic validation (`src/mllm/schemas.py`) + `parse_llm_output_as_json` JSON-rescue logic (`src/mllm/data/preprocessors.py`); exercised directly by [`demo/run_demo.py`](../demo/run_demo.py) step `step_json_rescue()` on [`demo/sample_input/raw_model_output_example.txt`](../demo/sample_input/raw_model_output_example.txt), output observed and matches [`demo/expected_output/`](../demo/expected_output/) |
| Council aggregation (mean / median / variance / agreement-bucket counts) | **Implemented & Verified** | `aggregate_scores_from_json` in [`src/mllm/data/preprocessors.py`](../src/mllm/data/preprocessors.py); exercised by `demo/run_demo.py` steps `step_aggregate()` / `step_consensus()`; output diffed byte-identical against [`demo/expected_output/aggregated_scores.csv`](../demo/expected_output/aggregated_scores.csv) and [`consensus_summary.csv`](../demo/expected_output/consensus_summary.csv)/[`.json`](../demo/expected_output/consensus_summary.json) across repeated runs |
| Pairwise mean-square-distance (MSD) agreement heatmaps (Agent Consistency / Literature Consistency / Literature-Agent Consistency, per [`src/mllm/skills/README.md`](../src/mllm/skills/README.md)) | **Implemented & Verified (re-run 2026-06-23)** | [`src/mllm-visualization.py`](../src/mllm-visualization.py) functions `agent_compare_summary_ordered` (Agent-Agent MSD heatmap), `study_compare_summary_ordered` (Study-Study MSD), `one_to_other_summary_plot`; defines comparison benchmarks `Ground LAC = 0.07`, `Hypothesis-Shuffle = 0.5`, `Random-Shuffle = 0.67`. The required `hpc_table_final.csv` is now shipped at [`examples/hpc_table_final.csv`](../examples/hpc_table_final.csv) and `CSV_PATH`/`REPORTS_DIR` were repointed at it (previously hardcoded to a non-shipped `./workspace/analysis/hpc/...` path). Re-run end-to-end in a clean venv with `pip install -e ".[viz]"` — all 6 figure outputs (`agent_agent_compare`, `hpc_3d_lo/go`, `hpc_h2h_comparison`, `literature_consensus_comparison`, `study_study_compare`) generated without error. A pre-existing default-value bug was also found and fixed in passing: `one_to_other_summary_plot`'s default `paper_selected="Westerberg2025"` did not match any study ID in the real data (`Westerberg&Xiong2025`), so the per-paper comparison subplot silently never populated; corrected to the real study ID |
| Legacy/alternate CSV export | **Implemented, Not Re-run (and not the canonical path)** | [`src/mllm/codes/scripts/results_to_csv.py`](../src/mllm/codes/scripts/results_to_csv.py) — an older aggregation script using a `scores: {lo, go}` schema rather than the canonical `lo_evaluations`/`go_evaluations` schema used elsewhere; do not use this as the demo's reference implementation (the demo correctly uses `aggregate_scores_from_json` instead) |

## 6. Hypothesis-Space Mapping & Visualization

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| 3D hypothesis-space scatter plot (H1/H2/H3 axes, LO/GO contexts) | **Implemented & Verified (re-run 2026-06-23)** | [`src/mllm-visualization.py`](../src/mllm-visualization.py) `plot_3d_scatter()` — builds a Plotly `Scatter3d` titled `"HPC Hypothesis Space ({context} Context)"`; executed against [`examples/hpc_table_final.csv`](../examples/hpc_table_final.csv), `hpc_3d_lo.html`/`.svg` and `hpc_3d_go.html`/`.svg` confirmed generated |
| 2D hypothesis-pair comparison plots | **Implemented & Verified (re-run 2026-06-23)** | `plot_2d_h_comparison()` in the same file; `hpc_h2h_comparison.html`/`.svg` confirmed generated |
| Score-table melting / per-study, per-model, per-context records | **Implemented & Verified** | `prepare_hpc_plot_data()` in the same file — converts the wide `hpc_table_final.csv` (columns like `LO-H1-avg`, `GO-H2-avg`, `study_name`, `agent_`, `type_`) into 608 long-format context-agent records on a real run. This wide-CSV format is **not the same schema** as the demo's per-model JSON files — it is a downstream/post-hoc analysis table, now shipped alongside the code that consumes it in [`examples/`](../examples/) |
| Full notebook figure suite (3D scatter, 2D overlays, MSD heatmaps, literature-vs-"this work" Wilcoxon/t-tests, shift vectors) | **Implemented & Verified (re-run 2026-06-23)** | [`examples/MLLM_HPCA_ORG.ipynb`](../examples/MLLM_HPCA_ORG.ipynb) — the original Colab-authored notebook (falls back to a local CSV outside Colab), now shipped with its data file. Its function-library and run-all cells were extracted and executed end-to-end against `examples/hpc_table_final.csv` in a clean venv: produced all 14 figure handles with zero errors, after fixing one pandas copy-on-write incompatibility in `calculate_msd_matrix()` (`np.fill_diagonal(mat.values, ...)` raised `ValueError: underlying array is read-only` under pandas 3.0.3; fixed via `.loc` assignment) — see [`examples/README.md`](../examples/README.md#known-issue-fixed-during-integration) for the exact fix |
| Pipeline architecture flowchart (3D) | **Implemented, Not Re-run** | [`src/mllm/codes/scripts/visualize_pipeline_3d.py`](../src/mllm/codes/scripts/visualize_pipeline_3d.py) `create_mllm_v3_flowchart()` — a presentation/documentation visualization of the pipeline graph itself, not a results figure |

## 7. Hypothesis-Space "Temperature" Metric

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| Geometric dispersion ("temperature") metric over council score distributions, per the arXiv abstract | **Not Found** | Searched `src/`, `docs/`, `scripts/` for `temperature` (excluding LLM decoding-temperature hits), `dispersion`, `hypothesis.space`, and `geometr*` — see command and full output preserved in the audit trail. All `temperature` hits are LLM decoding parameters (`config/profiles/*.json`, `model_config.py`); no function, class, or script implementing a geometric/statistical dispersion metric was found. `src/mllm/skills/README.md` mentions "hypothesis-space geometry analyses" in prose but does not point to a specific implementing file. **This is a confirmed gap as of this audit** — the metric described in the manuscript abstract is not present in this repository's current snapshot. If it exists in a private/unreleased analysis notebook, that should be stated explicitly in the README rather than implied present. |

## 8. Multi-Agent Consensus Protocol (Documentation Layer)

| Manuscript Component | Status | Repository Evidence |
|---|---|---|
| "Multi-Agent Consensus" protocol description (mean-square-distance references, council-level agreement) | **Implemented & Verified (as documentation); partially Implemented in code (see §5–6)** | Described in [`src/mllm/skills/instructions/`](../src/mllm/skills/instructions/) per [`src/mllm/skills/README.md`](../src/mllm/skills/README.md) §2; the MSD computation itself is implemented in `src/mllm-visualization.py` (§5–6 above, not independently re-run) and in `aggregate_scores_from_json`'s agreement-bucket counts (§5, verified) |

---

## Verification Note

This matrix was produced by:
1. Direct `Read` of the cited source files (`hpc-36-reference.md`, `hpc_eval_prompt.md`, `schemas.py`, `preprocessors.py`, `mllm-pipeline.py`, `mllm-visualization.py`, `skills/README.md`, `visualize_pipeline_3d.py`, `results_to_csv.py`).
2. An explicit `grep -rniE` search across `src/`, `docs/`, `scripts/` for `temperature|dispersion|hypothesis.space|geometr` to check for the "temperature metric," with decoding-parameter false positives manually filtered out.
3. A `find` check confirming `hpc_table_final.csv` and the `workspace/` directory `mllm-visualization.py` depends on are **not** present in this repository.
4. Cross-reference against [`demo/expected_output/`](../demo/expected_output/) for the rows marked **Implemented & Verified**, where a real command was run and its output diffed.

No manuscript figure/table numbers were available to this audit (only the arXiv abstract and metadata API were fetched, not the manuscript PDF body). **TODO for maintainer:** if exact figure/table numbers are wanted in this matrix, supply the manuscript PDF or HTML render and this document should be revised to add a `Figure N` / `Table N` column.

---

**Related documents:** [docs/REPRODUCIBILITY.md](REPRODUCIBILITY.md) (pipeline-level mapping and reproduction instructions), [docs/NATURE_COMPLIANCE_REPORT.md](NATURE_COMPLIANCE_REPORT.md) (Nature checklist compliance), [docs/TESTED_ENVIRONMENTS.md](TESTED_ENVIRONMENTS.md) (what was and wasn't independently re-run).
