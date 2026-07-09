# PRP — mllm-public
## Current Plan
- Awaiting next user requests for jmllm API or custom ontologies (e.g. SCZ, ADB).
## Last Review
- 2026-07-09: Verified programmatic API execution with smoke test. Unit test suite passes successfully.
## Progress Log
- 2026-07-09: Repository cloned to /Users/hamednejat/workspace/main/mllm-public.
- 2026-07-09: Created progress.json.
- 2026-07-09: Fixed compatibility mode JSON parsing test failure.
- 2026-07-09: Completed package refactoring (`mllm.vis`, `mllm.pipeline`, `mllm.util`), directory restructuring (`content/`, `ontology/`), and updated all imports and test suites.
- 2026-07-09: Ran end-to-end pipeline using `gemma-4-e4b-it-mxfp8` model on Bastos2012 and RaoBallard1999 papers, verifying correct output format, CSV consolidation, and visualization generation.
- 2026-07-09: Packaged repository as `jmllm`, exposed high-level programmatic API, removed root file clutter, and successfully ran API smoke test.

