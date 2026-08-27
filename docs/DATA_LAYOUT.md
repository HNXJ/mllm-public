# Canonical Data Layout & Evaluator Tables

This document describes the structure and provenance of the consolidated datasets in `artifacts/csvs/` and `artifacts/data/`.

## 1. Canonical Evaluator Score Tables

All evaluator scores across the 31-study predictive processing literature corpus are organized into three canonical tables in `artifacts/csvs/`:

| File Name | Evaluator Stratum | Rows ($) | Columns | Provenance / Description |
| :--- | :--- | :---: | :---: | :--- |
| `hpc_ag_table.csv` | Autonomous LLM Council | 304 | 93 | 10 open-weight local LLMs evaluated across 31 papers (HPC-36 ontology, LO & GO contexts). |
| `hpc_hexp_table.csv` | Independent Human Experts | 93 | 93 | Independent domain expert evaluations (=2$ plus consensus/adjudication) across the 31-paper corpus. |
| `hpc_grand_table.csv` | Grand Union ( \cup HEXP$) | 397 | 93 | Exact union of `hpc_ag_table.csv` and `hpc_hexp_table.csv` ({\mathrm{grand}} = N_{\mathrm{agent}} + N_{\mathrm{human}} = 304 + 93 = 397$). |

### Schema Details
Each row contains:
- `study_name`: Canonical study identifier (e.g., `Attinger2017`, `Bastos2020`, `Westerberg2025`).
- `evaluator_id`: Specific model handle (e.g., `gemma-4-31b-it`, `phi-4-reasoning-plus`) or human expert ID (`hexp01`, `hexp02`).
- `evaluator_type`: Categorical indicator (`agent` vs `human`).
- `year_`, `type_`: Study publication year and methodological categorization.
- `LO-count`, `GO-count`: Number of non-null factor evaluations in Local and Global Oddball contexts.
- `LO-H1-avg` ... `GO-H3-std`: Hypothesis-level summary aggregates.
- `LO-F01` ... `GO-F36`: 72 context-factor scoring columns (scale 1.$, empty/NaN if unaddressed).
- `provenance_source`: Tracking origin identifier.

*Note: Hybrid/assisted Human+AI evaluations are completely excluded from these publication-facing canonical tables.*

---

## 2. Reasoning Logs Archive

Full token-level and section-grounded model reasoning logs are permanently archived in `artifacts/data/reasoning_logs/`:
- **File Format**: Structured JSON.
- **Manifest**: `artifacts/data/reasoning_logs/manifest.csv` cataloging model handle, study identifier, source path, archive path, execution status, and SHA-256 content hashes.
