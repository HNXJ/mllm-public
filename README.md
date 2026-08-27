# Ontology-Constrained Multi-LLM Literature Scoring

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14920268.svg)](https://doi.org/10.5281/zenodo.14920268)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Authoritative code, data, and publication artifacts for **"Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature"** (*Scientific Reports*, 2026).

---

## 1. Canonical Evaluator Data

All evaluator scores across the 31-study predictive processing literature corpus are consolidated into:
- [`artifacts/csvs/hpc_ag_table.csv`](artifacts/csvs/hpc_ag_table.csv): 10 open-weight local LLMs evaluated across 31 papers.
- [`artifacts/csvs/hpc_hexp_table.csv`](artifacts/csvs/hpc_hexp_table.csv): Independent human domain experts ($K=2$ plus consensus).
- [`artifacts/csvs/hpc_grand_table.csv`](artifacts/csvs/hpc_grand_table.csv): Grand union table ($N=397$ rows, $N_{\mathrm{grand}} = N_{\mathrm{agent}} + N_{\mathrm{human}}$).

Full token-level model reasoning logs are archived in `artifacts/data/reasoning_logs/` with exact SHA-256 hashes in `manifest.csv`.

---

## 2. Publication Materials

All publication-facing documents are hosted in [`artifacts/publication/`](artifacts/publication/):
- **Clean Manuscript PDF**: [`main-render.pdf`](artifacts/publication/main-render.pdf)
- **Clean Supplementary Information PDF**: [`supp-render.pdf`](artifacts/publication/supp-render.pdf)
- **Tracked Revision Manuscript PDF**: [`main-diff.pdf`](artifacts/publication/main-diff.pdf)
- **Tracked Revision Supplementary Information PDF**: [`supp-diff.pdf`](artifacts/publication/supp-diff.pdf)
- **Point-by-Point Rebuttal**: [`assets/misc/response_to_reviewers.pdf`](artifacts/publication/assets/misc/response_to_reviewers.pdf)
- **Final Resubmission Archive**: [`scientific_reports_resubmission_final.zip`](artifacts/publication/scientific_reports_resubmission_final.zip)

---

## 3. Documentation & Ontology

- **Data Layout & Specification**: [`docs/DATA_LAYOUT.md`](docs/DATA_LAYOUT.md)
- **Reproducibility & Execution Guide**: [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md)
- **Models & Hardware Setup**: [`docs/MODELS_AND_RUNTIME.md`](docs/MODELS_AND_RUNTIME.md)
- **HPC-36 Reference Glossary**: [`src/ontology/glossary/HPC/hpc-36-reference.md`](src/ontology/glossary/HPC/hpc-36-reference.md)
- **Evaluation Prompt**: [`src/ontology/instructions/hpc_eval_prompt.md`](src/ontology/instructions/hpc_eval_prompt.md)

---

## 4. Permanent Archive & Citation

- **Zenodo DOI**: [10.5281/zenodo.14920268](https://doi.org/10.5281/zenodo.14920268)
- **License**: MIT (see [`LICENSE`](LICENSE)).
- **Citation**: See [`CITATION.cff`](CITATION.cff).
