# Ontology-Constrained Multi-LLM Literature Scoring

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14920268.svg)](https://doi.org/10.5281/zenodo.14920268)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Authoritative code, data, and publication artifacts for **"Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature"** (*Scientific Reports*, 2026).

---

## 1. Repository Structure

```
.
├── artifacts/
│   ├── publication/          # Authoritative manuscript workspace (TeX, PDFs, diffs, figures)
│   │   ├── main.tex          # Clean revised manuscript LaTeX source
│   │   ├── supp.tex          # Clean revised Supplementary Information LaTeX source
│   │   ├── main-render.pdf   # Clean compiled manuscript PDF
│   │   ├── supp-render.pdf   # Clean compiled Supplementary Information PDF
│   │   ├── main-diff.tex     # Tracked-change manuscript LaTeX source (latexdiff)
│   │   ├── main-diff.pdf     # Tracked-change manuscript PDF
│   │   ├── supp-diff.tex     # Tracked-change Supplementary Information LaTeX source
│   │   ├── supp-diff.pdf     # Tracked-change Supplementary Information PDF
│   │   ├── assets/           # Embedded figures, tables, and response to reviewers
│   │   └── scientific_reports_resubmission_final.zip
│   ├── csvs/                 # Consolidated evaluator score tables
│   │   ├── hpc_ag_table.csv  # Autonomous LLM council evaluations (N=304)
│   │   ├── hpc_hexp_table.csv# Independent human expert evaluations (N=93)
│   │   └── hpc_grand_table.csv# Grand union matrix (N=397)
│   ├── data/                 # Raw inputs, markdowns, outputs, and reasoning logs
│   │   └── reasoning_logs/   # Full model reasoning JSON logs & manifest
│   └── other/                # Supplementary reports and legacy assets
├── docs/                     # Documentation, data layout, and reproducibility guides
├── src/
│   ├── jmllm/                # Python package for pipeline, scoring, and analysis
│   └── ontology/             # Canonical HPC-36 glossary and prompt instructions
├── CITATION.cff
├── LICENSE
├── pyproject.toml
└── README.md
```

---

## 2. Canonical Evaluator Data

All evaluator scores across the 31-study predictive processing literature corpus are consolidated into:
- [`artifacts/csvs/hpc_ag_table.csv`](artifacts/csvs/hpc_ag_table.csv): 10 open-weight local LLMs evaluated across 31 papers.
- [`artifacts/csvs/hpc_hexp_table.csv`](artifacts/csvs/hpc_hexp_table.csv): Independent human domain experts ($K=2$ plus consensus).
- [`artifacts/csvs/hpc_grand_table.csv`](artifacts/csvs/hpc_grand_table.csv): Grand union table ($N=397$ rows, $N_{\mathrm{grand}} = N_{\mathrm{agent}} + N_{\mathrm{human}}$).

Full token-level model reasoning logs are archived in `artifacts/data/reasoning_logs/` with exact SHA-256 hashes in `manifest.csv`.

---

## 3. Publication Materials

All publication-facing documents are hosted in [`artifacts/publication/`](artifacts/publication/):
- **Clean Manuscript PDF**: [`main-render.pdf`](artifacts/publication/main-render.pdf)
- **Clean Supplementary Information PDF**: [`supp-render.pdf`](artifacts/publication/supp-render.pdf)
- **Tracked Revision Manuscript PDF**: [`main-diff.pdf`](artifacts/publication/main-diff.pdf)
- **Tracked Revision Supplementary Information PDF**: [`supp-diff.pdf`](artifacts/publication/supp-diff.pdf)
- **Point-by-Point Rebuttal**: [`assets/misc/response_to_reviewers.pdf`](artifacts/publication/assets/misc/response_to_reviewers.pdf)
- **Final Resubmission Archive**: [`scientific_reports_resubmission_final.zip`](artifacts/publication/scientific_reports_resubmission_final.zip)

---

## 4. Permanent Archive & Citation

- **Zenodo DOI**: [10.5281/zenodo.14920268](https://doi.org/10.5281/zenodo.14920268)
- **License**: MIT (see [`LICENSE`](LICENSE)).
- **Citation**: See [`CITATION.cff`](CITATION.cff).
