# Developer Plan

## Section 1: Brainstorm
Optimize literature evaluation pipeline for thread safety, dynamic parameters, and robust metadata parsing. Standardize programmatic modules under jmllm package conventions.

## Section 2: Execution Plan Table

File | Purpose | Score | Actions | Rules | Edits | Notes | Cautions
--- | --- | --- | --- | --- | --- | --- | ---
src/jmllm/__init__.py | Package programmatic entry points, pathing, and model configurations setup. | 100/100 | 1. Expose high-level functional APIs. 2. Verify settings propagation. | No state leak, keep methods stateless/global-fallback. | Completed high-level jmllm configuration setters and runner. | Allows simple imports and direct programmatic workflows. | None
src/jmllm/pipeline/controller.py | Core orchestrator running sequential DeepRead and parallel ThreadPoolExecutor evaluations. | 100/100 | 1. Run sequental caption extraction. 2. Load model. 3. Concurrently run reasoning. 4. Compile results. | Thread-safe logs and model loading. Dynamic parameter passing. | Integrated threading.RLock and self._model_api_lock. Dynamic log path resolution. | Verified parallel executions do not cause race conditions. | Check VRAM constraints on local LM Studio servers.
src/jmllm/pipeline/models/llm_wrapper.py | Wrapper communicating with LMS API via HTTP completions request payload. | 100/100 | 1. Map prompt and sampling options to parameters. 2. Handle HTTP errors. | Safely forward top_p and min_p parameters if present. | Added optional top_p and min_p mapping properties. | Passed all integration and mock testing. | None
src/jmllm/util/helpers.py | Support helpers, JSON parsing, output aggregation, and global log compilation. | 100/100 | 1. Parse JSON with robust markdown extraction. 2. Compile thread-safe logs. 3. Aggregates dataframes. | Use threading.Lock for global log updating. Robust right-split stem name parsing. | Implemented thread-safe generate_global_log and right-aligned stem split logic. | Ensures underscore-heavy study names parse correctly. | None
src/jmllm/vis/plotting.py | Consensus visualizations of evaluations. | 100/100 | 1. Parse aggregated CSV. 2. Plot heatmaps, PCA, and 3D scatter projections. | Follow dargold black/gold theme options where requested. | Consolidated visualization layouts. | Verified correct figure output layout. | None
