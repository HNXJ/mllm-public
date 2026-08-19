# Reproducibility Guide

This document provides exact instructions to reproduce the multi-LLM evidence-mapping pipeline using the `jmllm` package.

---

## 1. Minimal Installation & Offline Demo

To verify the installation and core analytical pipeline offline:

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public

# Install in editable mode with test and viz dependencies
pip install -e ".[dev,viz]"

# Run full test suite
pytest
```

---

## 2. End-to-End Pipeline Execution

The `jmllm` pipeline evaluates scientific literature against the 36-factor Hierarchical Predictive Coding (HPC-36) ontology.

### Step 1: DeepRead Multimodal Ingestion
Extract text and VLM figure descriptions from a source PDF:
```bash
jmllm-deepread content/inputs/Bastos2012.pdf -o content/markdowns/Bastos2012-vllm-deepread.md
```

### Step 2: Multi-LLM Council Inference
Run inference against a local OpenAI-compatible engine (such as LM Studio at `http://localhost:1234`):
```bash
jmllm-run \
  --pdfs_to_process Bastos2012 Attinger2017 \
  --reasoning_model_names gemma-4-31b-it \
  --engine_url http://localhost:1234 \
  --temperature 0.0
```

### Step 3: Council Score Aggregation
Aggregate JSON model outputs into consensus score tables:
```python
from pathlib import Path
from jmllm.util.helpers import aggregate_scores_from_json

df = aggregate_scores_from_json(Path("content/outputs"))
df.to_csv("content/tables/aggregated_scores.csv", index=False)
```

### Step 4: Consensus Analytics & Visualizations
Generate 3D hypothesis-space projections and pairwise MSD heatmaps:
```bash
jmllm-vis \
  --csv_path content/tables/aggregated_scores.csv \
  --reports_dir content/reports
```

---

## 3. Shipped Publication Datasets

All authoritative evaluation datasets ship under [`content/tables/`](../content/tables/):

| Dataset Path | Stratum / Description | Rows | Schema |
| :--- | :--- | :---: | :--- |
| [`original_council/hpc_table_original_council.csv`](../content/tables/original_council/hpc_table_original_council.csv) | Original 10-Model Council Wide Table | 304 | Wide 90-column |
| [`original_council/aggregated_scores_baseline.csv`](../content/tables/original_council/aggregated_scores_baseline.csv) | Original Baseline Aggregated Table | 31 | Wide 90-column |
| [`robustness_202608/scores_31x3x3x3_primary.csv`](../content/tables/robustness_202608/scores_31x3x3x3_primary.csv) | 837-Sweep Authoritative Factor Scores | 31,536 | Long format |
| [`robustness_202608/calls_ledger_837.csv`](../content/tables/robustness_202608/calls_ledger_837.csv) | 837-Sweep Runtime Execution Ledger | 837 | Execution ledger |
| [`experts/expert_registry.csv`](../content/tables/experts/expert_registry.csv) | Metadata Registry for Validation Strata | 5 | Metadata registry |
| [`experts/human_ai/hpchai_all.csv`](../content/tables/experts/human_ai/hpchai_all.csv) | Dual-Pass Human+AI Expert Table | 62 | Wide 90-column |
| [`canonical_31_paper_corpus_registry.csv`](../content/tables/canonical_31_paper_corpus_registry.csv) | Canonical 31-Paper Corpus Metadata | 31 | Corpus metadata |
| [`master_dataset_registry.csv`](../content/tables/master_dataset_registry.csv) | Complete Dataset Catalog & SHA-256 Hashes | 10 | Master registry |

---

## 4. Python API Usage

```python
import jmllm

# Configure paths and ontology
jmllm.set_instructions("ontology/instructions/hpc_eval_prompt.md")
jmllm.set_glossary("ontology/glossary/HPC/hpc-36-reference.md")
jmllm.set_path("content")

# Register reasoning model
jmllm.add_model(
    name="gemma-4-31b-it",
    url="http://localhost:1234",
    temperature=0.0
)

# Run evaluation and generate visualizations
jmllm.run(inputs=["Bastos2012.pdf", "Attinger2017.pdf"])
jmllm.visualize()
```
