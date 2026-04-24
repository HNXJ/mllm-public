---
name: mllm-orchestrator
description: MLLM-orchestrator for the unified DeepRead (VLM/Port 4475) + Evaluation (Agent-E/Port 4474) pipeline. Use when the user says "mllm" or when managing high-fidelity literature synthesis, multimodal figure parsing, or multi-agent consensus evaluations on the Backend LLM engine (e.g., mlx-lm) (or locally on this Mac as a fallback).
---

# MLLM Orchestrator

Unified control for the DeepRead (VLM) + Evaluation (Agent-E) pipeline.

## 1. Backend Connectivity
- **Primary Node**: `HN@100.69.184.42` (Tailscale).
- **Control Interface**: `mlxEngine` (FastAPI).
- **Main API (Port 4474)**: Reasoning and text-based evaluation.
- **VLM API (Port 4475)**: Figure parsing and multimodal synthesis.

## 2. Model Management
- **Default Context Window**: 131,072 tokens (128K).
- **Unload**: GET `/unload` (clears VRAM on current backend).
- **Load**: POST `/load` with `{"model": "REPO_NAME", "backend": "lms"}`.
- **2026 Models (Preferred)**:
  - `Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-6bit` (Logic/Reasoning).
  - `Qwen3-30B-Thinking-6bit` (Complex Chain-of-Thought).
  - `DeepSeek-R1-Distill-Qwen-32B-6bit` (Mathematical/Code Verification).

## 3. Core Workflows

### Phase 1: DeepRead (Multimodal)
1. **Target**: Port 4475 (`vlm_engine`).
2. **Action**: Parse figures and tables from publications using VLLMs (e.g., `Qwen2.5-VL`).
3. **Synthesis**: Combine text and visual descriptions into a **Unified Context**.

### Phase 2: Evaluation (Reasoning)
1. **Target**: Port 4474 (`main_engine`).
2. **Action**: Run structured evaluation scripts against the **Glossary: H1-H3 Factors**.
3. **Consensus**: Parallelize calls to 7+ models (Llama-3, Mistral, Gemini) via the `/v1/chat/completions` endpoint.
4. **Validation**: Check for ontological grounding (Mapping to factors 1-12).

## 4. API Reference
See [ENGINE_API.md](references/ENGINE_API.md) for endpoint details and payload schemas.
