# MLLM Reviewer Demo

A minimal, **offline, model-free** demonstration of the MLLM pipeline's
data-handling and consensus-aggregation logic. It exercises real
package code (`mllm.data.preprocessors`) — not a reimplementation — so
a reviewer can verify end-to-end correctness without:

- Apple Silicon / MLX hardware
- Downloading any LLM weights
- Running a local inference server
- Network access of any kind

This demo intentionally does **not** invoke the full multi-model
council described in the manuscript (that requires the local MLX
runtime documented in [docs/MODELS_AND_RUNTIME.md](../docs/MODELS_AND_RUNTIME.md)).
Instead, it demonstrates the parts of the pipeline that are
deterministic and runnable on any machine: parsing/rescuing raw model
JSON output and aggregating per-model evaluation files into consensus
statistics — the same code path used to build the manuscript's result
tables.

## What's here

```
demo/
├── README.md                          this file
├── run_demo.py                        runnable, self-contained demo script
├── sample_input/                      synthetic input data (see Data Provenance below)
│   ├── DemoStudyA_demo-model-alpha_eval.json
│   ├── DemoStudyA_demo-model-beta_eval.json
│   ├── DemoStudyB_demo-model-alpha_eval.json
│   └── raw_model_output_example.txt   noisy raw LLM-style output (markdown fences, stray prose)
└── expected_output/                   reference outputs to diff against
    ├── aggregated_scores.csv
    ├── consensus_summary.csv
    └── consensus_summary.json
```

### Data provenance (important)

Every file under `sample_input/` is **synthetic placeholder data**
authored for this demo. It uses real factor names from the HPC-36
ontology (`src/mllm/skills/glossary/HPC/hpc-36-reference.md`) so the
schema is realistic, but the studies (`DemoStudyA`, `DemoStudyB`), the
model names (`demo-model-alpha`/`beta`/`gamma`), and every score are
invented for illustration only. **No manuscript data, no real model
output, and no scientific claim is contained in this demo.**

## Requirements

- Python 3.10–3.13 (tested with 3.13.7; see [docs/TESTED_ENVIRONMENTS.md](../docs/TESTED_ENVIRONMENTS.md))
- The `mllm` package installed (`pip install -e .` from the repo root — see the main [README.md](../README.md#installation-guide))
- No GPU, no MLX, no network access

## How to run

From the repository root, after completing the [Installation Guide](../README.md#installation-guide):

```bash
python demo/run_demo.py
```

## Expected output

The script prints 3 progress lines and writes 3 files to a new
`demo/demo_output/` directory:

```
[1/3] Rescued raw model output -> agent_name='demo-model-gamma'
[2/3] Aggregated 24 factor-score rows from 3 evaluation files
[3/3] Computed consensus statistics for 16 (study, context, factor) groups

Done in 0.0Xs. Wrote:
  - demo/demo_output/aggregated_scores.csv
  - demo/demo_output/consensus_summary.csv
  - demo/demo_output/consensus_summary.json

Compare against demo/expected_output/ to verify correctness.
```

Generated files:

| File | Contents |
|---|---|
| `aggregated_scores.csv` | Long-form table: one row per (Study, Model, Context, Factor, Score) — the direct output of `mllm.data.preprocessors.aggregate_scores_from_json` |
| `consensus_summary.csv` | One row per (Study, Context, Factor) with `n_models`, `mean_score`, `median_score`, `std_score` — the council-consensus statistics described in [docs/REPRODUCIBILITY.md](../docs/REPRODUCIBILITY.md#2-council-aggregation) |
| `consensus_summary.json` | Same consensus table as JSON records |

`demo/demo_output/` is the script's working output directory and is
git-ignored; `demo/expected_output/` is the **committed reference**
produced by the same script and verified by the maintainers — diff
your run against it to confirm a correct installation:

```bash
diff demo/demo_output/consensus_summary.csv demo/expected_output/consensus_summary.csv
# no output = identical = your installation reproduces the demo exactly
```

## Expected runtime

**Under 1 second** on any normal desktop or laptop computer (measured:
~0.01–0.3s on a 2021 MacBook Pro, Apple M1 Max, see
[docs/TESTED_ENVIRONMENTS.md](../docs/TESTED_ENVIRONMENTS.md)). There is no model
inference in this demo — only JSON parsing and pandas aggregation over
3 small files.

## Running on your own data

To aggregate your own per-model evaluation JSON files instead of the
synthetic demo data, point the same functions at your own directory:

```bash
python -c "
from pathlib import Path
from mllm.data.preprocessors import aggregate_scores_from_json
df = aggregate_scores_from_json(Path('./outputs'))
df.to_csv('my_aggregated_scores.csv', index=False)
print(df.head())
"
```

Input files must match the schema documented in
[docs/REPRODUCIBILITY.md](../docs/REPRODUCIBILITY.md#output-schema) (either
`lo_evaluations`/`go_evaluations` keys, or a generic `scores` list/dict)
— this is exactly the schema produced by `mllm-pipeline.py` for real
papers and real models. See the main
[README.md → Instructions for Use](../README.md#instructions-for-use)
for the full, real (non-demo) pipeline invocation.
