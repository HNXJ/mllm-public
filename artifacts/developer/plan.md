# Developer Plan

## Section 1: Brainstorm
1. Universal Model Adapter Interface: Generalize llm_wrapper.py to support multiple providers (LM Studio, OpenAI, Anthropic, Google Gemini, Ollama) via unified configurations. 2. Decoupled VLM Preprocessor: Abstract the DeepRead preprocessing phase to cleanly separate text extraction from optional VLM figure-to-text operations. 3. Structured JSON Schema Enforcement: Integrate standard response_format payload mapping or schema validation. 4. Flexible Input and Output Formats: Support custom target paths, recursive directories, and sqlite/dataframe exports.

## Section 2: Execution Plan Table

File | Purpose | Score | Actions | Rules | Edits | Notes | Cautions
--- | --- | --- | --- | --- | --- | --- | ---
src/jmllm/__init__.py | Package programmatic entry points, pathing, and model configurations setup. | 95/100 | 1. Expand add_model() to support specifying remote provider types (openai, google, anthropic, ollama). 2. Add SQL/sqlite target configuration parameters. | Preserve simple module-level stateless interface. | Planned: support dynamic provider mapping inside configuration registers. | Ensures backward compatibility with local LMS setups. | None
src/jmllm/pipeline/controller.py | Core orchestrator running sequential DeepRead and parallel ThreadPoolExecutor evaluations. | 90/100 | 1. Implement context window limit token guard check. 2. Decouple DeepRead text parser and support optional VLM execution. | Thread-safe logging and model loading locks must be preserved. | Planned: insert check_context_window helper call before starting worker threads. | Protects against context overflow API errors. | Check VRAM limits during concurrent model runs.
src/jmllm/pipeline/models/llm_wrapper.py | Wrapper communicating with LMS API via HTTP completions request payload. | 80/100 | 1. Generalize HTTP request builder to support provider-specific authorization, headers, and endpoints. 2. Implement exponential backoff retry handler for robust network recovery. 3. Propagate response_format JSON options. | Must remain thread-safe. Fallback to local server defaults. | Planned: refactor _call_llm_api into provider-specific request wrappers. | Handles rate limiting (HTTP 429) gracefully. | None
src/jmllm/util/helpers.py | Support helpers, JSON parsing, output aggregation, and global log compilation. | 95/100 | 1. Add character-to-token count estimation helper. 2. Support database exports. | Preserve thread-safe logging and splits. | Planned: create estimate_tokens function. | Used by controller to enforce context bounds. | None
src/jmllm/vis/plotting.py | Consensus visualizations of evaluations. | 100/100 | None | Follow dargold black/gold theme options where requested. | None | Fully optimal state, no edits planned. | None
