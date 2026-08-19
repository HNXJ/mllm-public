# jmllm

A lightweight toolkit for ontology-constrained literature evaluation and evidence mapping using local and remote reasoning models.

---

## Installation

```bash
git clone https://github.com/HNXJ/mllm-public.git
cd mllm-public
pip install -e ".[dev,viz]"
```

---

## Quickstart

### 1. Command Line Interface

```bash
# Run pipeline against local LM Studio server
jmllm-run \
  --pdfs_to_process Bastos2012 Attinger2017 \
  --reasoning_model_names gemma-4-31b-it \
  --engine_url http://localhost:1234 \
  --temperature 0.0

# Generate consensus visualizations
jmllm-vis \
  --csv_path content/tables/aggregated_scores.csv \
  --reports_dir content/reports

# DeepRead PDF extraction
jmllm-deepread content/inputs/Bastos2012.pdf -o content/markdowns/Bastos2012-vllm-deepread.md
```

### 2. Python API

```python
import jmllm

jmllm.set_instructions("ontology/instructions/hpc_eval_prompt.md")
jmllm.set_glossary("ontology/glossary/HPC/hpc-36-reference.md")
jmllm.set_path("content")

jmllm.add_model(
    name="gemma-4-31b-it",
    url="http://localhost:1234",
    temperature=0.0
)

jmllm.run(inputs=["Bastos2012.pdf", "Attinger2017.pdf"])
jmllm.visualize()
```

---

## Repository Layout

```
jmllm/
├── ontology/           # Ontology definitions and prompt instructions
├── content/            # Inputs, markdowns, outputs, tables, and reports
├── src/jmllm/          # Package source code
├── tests/              # Test suite
└── docs/               # Technical references and tested environments
```

---

## Testing

```bash
pytest
```

---

## Citation

```bibtex
@article{nejat2026jmllm,
  title={Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature},
  author={Nejat, Hamed and Maier, Alexander and Spencer-Smith, Jesse and Bastos, Andr{\'e} M.},
  journal={arXiv preprint arXiv:2606.05206},
  year={2026}
}
```
