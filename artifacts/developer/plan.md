# Developer Plan

## Section 1: Brainstorm
Achieved: core package migrations, programmatic APIs, concurrency stability, thread-safe logger/api locks, multi-provider mappings, and sqlite exports. Next steps: 1. Explicitly decouple Local Mode (local load parameters via MLX/LM Studio CLI) from Remote Mode (API-key + URL gateway). 2. Generalize jmllm.run() inputs to accept direct absolute PDF file paths from anywhere on the filesystem. 3. Simplify installation and environment configurations to make jmllm a professional, lightweight standard package for ontology-constrained literature evaluations.

## Section 2: Execution Plan Table

File | Purpose | Score | Actions | Rules | Edits | Notes | Cautions
--- | --- | --- | --- | --- | --- | --- | ---
src/jmllm/__init__.py | Package programmatic entry points, pathing, and model configurations setup. | 95/100 | 1. Update run() to accept a list of absolute file paths. 2. Handle environment-based API keys dynamically. | Preserve simple module-level stateless interface. | Planned: support absolute PDF paths ingestion. | Bypasses strict copy step into content/inputs. | None
src/jmllm/pipeline/controller.py | Core orchestrator running sequential DeepRead and parallel ThreadPoolExecutor evaluations. | 90/100 | 1. Decouple loading steps: skip load_model() and unload_all() if provider is remote. 2. Resolve target directories dynamically if absolute input paths are provided. | Thread-safe logging and model loading locks must be preserved. | Planned: skip model load calls if provider != 'mlx'. | Prevents redundant HTTP posts to localhost:1234 when running remote models. | None
src/jmllm/pipeline/models/llm_wrapper.py | Wrapper communicating with LMS API via HTTP completions request payload. | 95/100 | 1. Fallback to API keys from standard environment variables (OPENAI_API_KEY, GEMINI_API_KEY, ANTHROPIC_API_KEY) if profile key is 'none'. | Must remain thread-safe. | Planned: update header configuration payload inside _call_llm_api_raw. | Ensures out-of-the-box authentication configuration. | None
src/jmllm/util/helpers.py | Support helpers, JSON parsing, output aggregation, and global log compilation. | 100/100 | None | Preserve thread-safe logging. | None | Optimal state. | None
src/jmllm/vis/plotting.py | Consensus visualizations of evaluations. | 100/100 | None | Follow dargold black/gold theme options where requested. | None | Fully optimal state, no edits planned. | None
