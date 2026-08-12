# Project Rules — MLLM Reviewer Robustness Experiment

## Scope

This branch is dedicated to the Scientific Reports reviewer-requested robustness analysis of the existing MLLM/HPC-36 literature-scoring pipeline.

Preserve the scientific semantics of the existing pipeline unless explicitly instructed otherwise.

## Core principles

* Inspect existing code before modifying it.
* Prefer minimal changes over architectural rewrites.
* Preserve the existing HPC-36 ontology and scoring semantics.
* Preserve the existing 31 paper inputs.
* Preserve raw inference outputs.
* Derived data must be reproducible from raw outputs.
* Experimental conditions must never overwrite one another.
* Long-running inference must be resumable.
* Record exact runtime/model/sampler metadata needed for reproducibility.
* Do not fabricate experimental results.
* Do not silently substitute models, papers, prompts, or parameters.
* Do not regenerate DeepRead inputs unless explicitly requested.
* Do not modify manuscript claims based on results that have not been generated and validated.

## Experiment

Target factorial design:

31 papers × 3 models × 3 temperatures × 3 repeats = 837 inference calls.

Models:

* olmo-3-32b-think
* gemma-4-31b-it
* mistral-nemo-12b-thinking

Temperatures:

* 0.00
* 0.35
* 0.70

Repeats:

* 1
* 2
* 3

The exact locally served LM Studio model identifiers must be discovered and recorded separately from these scientific model names.

## Development discipline

Before launching the full experiment:

1. inspect the existing repository;
2. identify the exact 31 manuscript inputs;
3. identify the existing scoring prompt, glossary, parser, controller, and inference wrapper;
4. resolve model identifiers from LM Studio;
5. implement temperature/repeat-aware experimental identity;
6. implement resumability and manifest tracking;
7. run tests;
8. run a 9-call smoke test:
   1 paper × 3 models × 3 temperatures × repeat 1;
9. inspect the resulting raw outputs and derived CSV;
10. STOP for authorization before the 837-call sweep.

Do not introduce unrelated project-management protocols, JAX requirements, presentation styling rules, Labyrinth integrations, external MCP dependencies, or unrelated statistical doctrines.
