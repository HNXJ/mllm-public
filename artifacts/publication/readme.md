# Canonical Publication Workspace: Scientific Reports Resubmission

## 1. Overview & Provenance Contract
- **Manuscript Title**: Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature
- **Authors**: Hamed Nejat, Alexander Maier, Jesse Spencer-Smith, Andr\'e M. Bastos
- **Target Journal**: *Scientific Reports*
- **Persistent Archive DOI**: https://doi.org/10.5281/zenodo.14920268
- **Git Release Tag**: `resubmission-release-v1` (Commit: `db0f1b65a09949480f7b2385bc786f9c3d9256e8`)
- **Original Source Tree**: `content/post-sub-draft/2026_mllm_arxiv_post_sub/`

---

## 2. Data & Verification Scope Separation
- `assets/data/`: Contains publication-local verification contracts and manifests (e.g., `resubmission_sealed_artifacts_manifest.csv`, `revision_statistical_claims.csv`) required to verify reported quantities, captions, and tables without duplicating raw storage.
- `content/tables/`: Authoritative repository location for full sealed output datasets and historical evaluator passes.
- `Zenodo (DOI 10.5281/zenodo.14920268)`: Immutable public release archive.

---

## 3. Workspace Structure
```
artifacts/publication/
├── main.tex                    # Clean revised manuscript source (SciRep template, embedded thebibliography)
├── supp.tex                    # Revised Supplementary Information source (embedded thebibliography)
├── readme.md                   # Build instructions and provenance contract
├── main-render.pdf             # Latest verified clean render of main.tex
├── supp-render.pdf             # Latest verified render of supp.tex
│
└── assets/
    ├── figures/                # Vector SVG & 300 DPI publication figures (Fig 1-9, Fig S1-S5)
    ├── data/                   # Publication-local verification contracts and claims manifests
    └── misc/
        ├── response_to_reviewers.tex   # Rebuttal source document
        └── response_to_reviewers.pdf   # Point-by-point response to Reviewer 1
```

*Note on Bibliography*: Both `main.tex` and `supp.tex` use embedded LaTeX `thebibliography` environments conforming to *Scientific Reports* author guidelines; no separate `assets/ref.bib` is fabricated.

---

## 4. Compilation Commands
```bash
# Main manuscript
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

# Supplementary Information
pdflatex -interaction=nonstopmode supp.tex
pdflatex -interaction=nonstopmode supp.tex
```

---

## 5. Anti-Drift Invariant
$$\Delta_{\mathrm{publication}} = \Delta_{\mathrm{authorized}} + \Delta_{\mathrm{necessary}}, \quad \Delta_{\mathrm{unauthorized}} = 0$$
