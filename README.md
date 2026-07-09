# jmllm: Multi-LLM Ontology-Constrained Evidence-Mapping Pipeline

A Python package and command-line tool for mapping heterogeneous scientific literature into structured, model-derived evidence spaces using a council of large language models.

---

## Associated Publication

This repository implements the ontology-constrained literature-synthesis pipeline described in:

> **Nejat, H., Maier, A., Spencer-Smith, J., Bastos, A.M. (2026).**  
> **"Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature."**  
> *arXiv:2606.05206 [q-bio.NC]*  
> [arXiv Listing](https://arxiv.org/abs/2606.05206) | [DOI: 10.48550/arXiv.2606.05206](https://doi.org/10.48550/arXiv.2606.05206)

---

## Core Features

- **Programmatic Python API**: Configure ontologies, register reasoning models, run literature evaluations, and generate consensus analytics programmatically.
- **DeepRead Multimodal Ingestion**: Figure-aware PDF text extraction that parses text and targets VLM-based figure descriptions.
- **HPC-36 Ontology**: Built-in 36-factor predictive coding hierarchy spanning Predictive Suppression (H1), Feedforward Error Propagation (H2), and Ubiquity (H3).
- **Consensus Analytics**: Pairwise Mean Square Distance (MSD) geometry, consensus averaging, and 3D scatter plots of hypothesis space support.

---

## Installation

Install the package in editable mode with development and visualization dependencies using `uv` or `pip`:

```bash
# Clone the repository
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public

# Setup virtual environment and install dependencies
uv pip install -e ".[dev,viz]"
# or using standard pip:
# pip install -e ".[dev,viz]"
```

---

## Programmatic Python API Usage

```python
import jmllm

# 1. Configure pathways & ontology templates
jmllm.set_instructions("ontology/instructions/hpc_eval_prompt.md")
jmllm.set_glossary("ontology/glossary/HPC/hpc-36-reference.md")
jmllm.set_path("content")  # Root folder containing inputs/, outputs/, tables/

# 2. Register models (updates profiles dynamically)
jmllm.add_model(
    name="gemma-4-e4b-it-mxfp8",
    url="http://localhost:1234",
    temperature=0.7,
    context_window=128000
)

# 3. Execute evaluation pipeline on inputs
jmllm.run(inputs=["Bastos2012.pdf", "RaoBallard1999.pdf"])

# 4. Generate visual consensus reports
jmllm.visualize()
```

---

## Command Line Interface (CLI)

The package registers three command-line entry points upon installation:

### 1. Run Pipeline
Execute the full multi-LLM scoring pipeline:
```bash
jmllm-run \
  --pdfs_to_process Bastos2012.pdf RaoBallard1999.pdf \
  --reasoning_model_names gemma-4-e4b-it-mxfp8 \
  --engine_url http://localhost:1234 \
  --no_vlm \
  --no_load \
  --timeout 600 \
  --temperature 0.7
```

### 2. Generate Visualizations
Generate heatmaps and 3D scatter projections from the aggregated scores CSV:
```bash
jmllm-vis \
  --csv_path content/tables/aggregated_scores.csv \
  --reports_dir content/reports
```

### 3. DeepRead PDF Extraction Only
Extract interleaved text and VLM-described figures from a PDF:
```bash
jmllm-deepread source_paper.pdf -o output_cached.md
```

---

## Repository Layout

```
├── ontology/           # Core ontologies (glossary/ & evaluation instructions/)
├── content/            # Runtime directories (inputs/, markdowns/, outputs/, tables/, reports/)
├── src/jmllm/          # Package source (pipeline namespaces, vis, and util)
├── tests/              # Unit and integration test suite
├── docs/               # In-depth manuscript mappings and tested environments
└── legacy/             # Refactored queue runner scripts and configs
```

---

## Documentation Index

For detailed explanations of configurations, compliance, and metrics, see:
- [Tested Environments](docs/TESTED_ENVIRONMENTS.md) — OS/Python/package versions.
- [Models & Runtime Specification](docs/MODELS_AND_RUNTIME.md) — Models specification and decoding parameters.
- [Reproducibility Guide](docs/REPRODUCIBILITY.md) — 7-stage pipeline explanation.
- [Nature Compliance Report](docs/NATURE_COMPLIANCE_REPORT.md) — checklist compliance.
