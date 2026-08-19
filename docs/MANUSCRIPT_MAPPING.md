# Manuscript Traceability Matrix

This document provides the definitive mapping between the manuscript components:

> Nejat, H., Maier, A., Spencer-Smith, J., Bastos, A.M. (2026).  
> "Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature."  
> *arXiv:2606.05206 [q-bio.NC]* | [DOI: 10.48550/arXiv.2606.05206](https://doi.org/10.48550/arXiv.2606.05206)

and the concrete implementation in this repository.

---

## 1. Ontology & Glossary Layer

| Manuscript Component | Implementation Status | Repository Artifact |
|---|---|---|
| **36-Factor HPC Ontology** (H1 Predictive Suppression, H2 Feedforward Error, H3 Ubiquity) | Implemented & Verified | [`ontology/glossary/HPC/hpc-36-reference.md`](../ontology/glossary/HPC/hpc-36-reference.md) — Canonical 36-factor reference with operational definitions and experimental contexts (LO/GO). |
| **Evaluation Prompt & Rubric** | Implemented & Verified | [`ontology/instructions/hpc_eval_prompt.md`](../ontology/instructions/hpc_eval_prompt.md) — Role definition, scoring scale ($[-1.0, +1.0]$ and null), and JSON schema instructions. |

---

## 2. Ingestion & Preprocessing Layer (DeepRead)

| Manuscript Component | Implementation Status | Repository Artifact |
|---|---|---|
| **PDF Extraction & Layout Analysis** | Implemented & Verified | [`src/jmllm/pipeline/deepread/loaders.py`](../src/jmllm/pipeline/deepread/loaders.py) (`DeepReadLoader` using PyMuPDF). CLI: `jmllm-deepread`. |
| **Figure Caption & Vision Association** | Implemented & Verified | [`src/jmllm/pipeline/deepread/operators.py`](../src/jmllm/pipeline/deepread/operators.py) & [`src/jmllm/pipeline/deepread/preprocessors.py`](../src/jmllm/pipeline/deepread/preprocessors.py). |
| **Unified Markdown Representations** | Implemented & Verified | `content/markdowns/*-vllm-deepread_compressed.md` — 31 canonical study markdowns with figure descriptions. |

---

## 3. Inference, Extraction, and Schema Enforcement

| Manuscript Component | Implementation Status | Repository Artifact |
|---|---|---|
| **Pydantic Response Schema** | Implemented & Verified | [`src/jmllm/util/schemas.py`](../src/jmllm/util/schemas.py) (`HpcEvaluationResponse`) — Validates JSON output structure and bounds factor scores to $[-1.0, +1.0]$. |
| **JSON Extraction Resilience** | Implemented & Verified | [`src/jmllm/util/helpers.py`](../src/jmllm/util/helpers.py) (`parse_llm_output_as_json`) — Balanced curly-brace recovery engine. |
| **OpenAI / LM Studio Client** | Implemented & Verified | [`src/jmllm/pipeline/models/local_llm_wrapper.py`](../src/jmllm/pipeline/models/local_llm_wrapper.py) & [`src/jmllm/pipeline/robustness_runner.py`](../src/jmllm/pipeline/robustness_runner.py). |

---

## 4. Council Aggregation, Analytics & Visualizations

| Manuscript Component | Implementation Status | Repository Artifact |
|---|---|---|
| **Council Aggregation** | Implemented & Verified | [`src/jmllm/util/helpers.py`](../src/jmllm/util/helpers.py) (`aggregate_scores_from_json`) — Computes H1, H2, and H3 means and standard deviations. |
| **3D Hypothesis-Space Projections** | Implemented & Verified | [`src/jmllm/vis/plotting.py`](../src/jmllm/vis/plotting.py) (`plot_3d_scatter`) — Generates interactive 3D scatter plots for LO and GO contexts. CLI: `jmllm-vis`. |
| **Pairwise MSD Heatmaps** | Implemented & Verified | [`src/jmllm/vis/plotting.py`](../src/jmllm/vis/plotting.py) (`agent_compare_summary_ordered`, `study_compare_summary_ordered`). |
| **Figure Notebook** | Implemented & Verified | [`examples/MLLM_HPCA_ORG.ipynb`](../examples/MLLM_HPCA_ORG.ipynb) — Self-contained figure generation suite executing against `examples/hpc_table_final.csv`. |

---

## 5. Reviewer Robustness & Multi-Strata Data Layer

| Manuscript Component | Implementation Status | Repository Artifact |
|---|---|---|
| **837-Sweep Robustness Dataset** | Implemented & Verified | [`content/tables/robustness_202608/`](../content/tables/robustness_202608/) — Authoritative scores (`scores_31x3x3x3_primary.csv`) and execution ledger (`calls_ledger_837.csv`). |
| **Original 10-Model Council Table** | Implemented & Verified | [`content/tables/original_council/hpc_table_original_council.csv`](../content/tables/original_council/hpc_table_original_council.csv) (and [`examples/hpc_table_final.csv`](../examples/hpc_table_final.csv)). |
| **Human+AI Procedural Robustness** | Implemented & Verified | [`content/tables/experts/human_ai/`](../content/tables/experts/human_ai/) (`hpchai_01.csv`, `hpchai_02.csv`, `hpchai_all.csv`). |
| **Expert Registry & Human Strata** | Implemented & Verified | [`content/tables/experts/expert_registry.csv`](../content/tables/experts/expert_registry.csv) — Tracks validation strata (`hpch_01..03` pending, `hpchai_01..02` verified). |
| **Corpus Metadata Registry** | Implemented & Verified | [`content/tables/canonical_31_paper_corpus_registry.csv`](../content/tables/canonical_31_paper_corpus_registry.csv). |
| **Master Dataset Registry** | Implemented & Verified | [`content/tables/master_dataset_registry.csv`](../content/tables/master_dataset_registry.csv). |
