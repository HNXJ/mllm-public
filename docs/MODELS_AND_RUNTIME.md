# Models and Runtime Configuration

## Overview

This document records the model-council and runtime assumptions used by the manuscript "Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature." The manuscript evaluates a 31-study predictive-processing corpus using a 36-factor ontology across local and global oddball contexts.

**Runtime Platform:** MLX-LM (Apple Silicon optimized)  
**Inference Engine:** MLX (Machine Learning Accelerated)  
**Deployment Pattern:** Local multi-model council with ontology-constrained prompting

---

## Model Council (10 Models)

The manuscript evaluates predictive coding hypotheses using a council of 10 diverse reasoning models, each selected for different reasoning and quantitative capabilities:

| Model ID | Manuscript Handle | Size | Family / Source | Runtime Notes |
|----------|-------------------|------|-----------------|---------------|
| 1 | `gemma-3-27b-it` | 27B | Google DeepMind | Local MLX-LM profile |
| 2 | `gemma-4-31b-it` | 31B | Google DeepMind | Local MLX-LM profile |
| 3 | `deepseek-r1-distill-llama-70b` | 70B | DeepSeek-AI / Meta Llama base | Local MLX-LM profile |
| 4 | `gpt-oss-claude-4.5-sonnet` | 20B | Community distillation | Local MLX-LM profile |
| 5 | `mistral-nemo-12b-thinking` | 12B | Mistral AI / NVIDIA | Local MLX-LM profile |
| 6 | `olmo-3-32b-think` | 32B | Allen AI | Local MLX-LM profile |
| 7 | `phi-4-reasoning-plus` | 14B | Microsoft | Local MLX-LM profile |
| 8 | `qwen3-14b-gemini-3-pro` | 14B | Qwen community fine-tune | Local MLX-LM profile |
| 9 | `qwen3-14b-claude-4.5-sonnet` | 14B | Qwen community fine-tune | Local MLX-LM profile |
| 10 | `qwen3.5-40b-claude-4.5-opus` | 40B | Qwen community fine-tune | Local MLX-LM profile |

---

## Decoding Configuration

All models are evaluated using **fixed decoding parameters** to ensure reproducibility:

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Temperature** | 0.70 | Controlled randomness; balances exploration/exploitation |
| **Top-p (nucleus sampling)** | 0.90 | Filters low-probability tokens; limits output diversity |
| **Min-p** | 0.1 | Ensures baseline probability floor for rare tokens |
| **Maximum Tokens** | 4,096 | Sufficient for detailed evidence extraction; prevents runaway inference |
| **Context Window** | 131,072 | Full manuscript text + glossary + instructions in single pass |
| **KV-Cache Format** | MXFP8 | Memory-efficient quantization (where available) |

---

## MLX-LM Runtime

### System Requirements

- **Hardware:** Apple Silicon (M1, M2, M3, M4, etc.) or compatible MLX-enabled architecture
- **Memory:** ≥32 GB unified memory (16GB minimum with aggressive offloading)
- **Python:** 3.10+
- **MLX Version:** Latest compatible with MLX-LM (`mlx>=0.4.0`)

### Installation

```bash
pip install mlx-lm>=0.15.0
pip install mlx>=0.4.0
export MLX_MODEL_ROOT=./mlx_models  # or your local model directory
```

### Model Loading

Models are loaded dynamically at inference time via:

```python
from mlx_lm import load, generate

model, tokenizer = load(model_id)
output = generate(model, tokenizer, prompt, max_tokens=4096, temp=0.70)
```

Where `model_id` is either:
1. A local filesystem path (if `MLX_MODEL_ROOT` is set)
2. A Hugging Face model ID (auto-downloaded to cache)
3. A profile-mapped identifier (see `src/mllm/config/profiles/`)

---

## Model Profile Metadata

Each model's configuration is stored in a **profile JSON** file:

```
src/mllm/config/profiles/{model-id}-full-profile.json
```

Example profile structure:

```json
{
  "model_name": "gpt-oss-20b-claude-4.5-mlx",
  "context_window": 131072,
  "api_url": "http://localhost:4474/v1/chat/completions",
  "api_key": "[REDACTED_SECRET_LIKE_VALUE]",
  "temperature": 0.70,
  "max_tokens": 4096,
  "engine_type": "mlx",
  "availability": "verified"
}
```

**Fields:**
- `model_name`: MLX-LM or Hugging Face model identifier
- `context_window`: Maximum input tokens (including prompt + study text)
- `engine_type`: Runtime backend (`mlx`, `lms`, or `vmlx`)
- `temperature`, `max_tokens`: Decoding hyperparameters
- `availability`: Verification status (`verified`, `untested`, or `failed`)

---

## Important Caveats

### 1. Model Cards and Licensing

Users **must consult the official Hugging Face model cards** for:
- Exact model version and revision
- License terms (MIT, OpenRAIL, commercial restrictions, etc.)
- Training data provenance
- Known biases and limitations
- Citation requirements

**This repository does NOT assert model licensing or correctness.** Consult https://huggingface.co/ for each model ID.

### 2. Scores Are Model-Rated Evidence Assignments, Not Biological Truth

The output scores from this pipeline represent:

- **What the models predict** about evidence for predictive coding factors
- **Ontology-constrained structured predictions** based on learned patterns
- **Useful proxies** for literature mapping and hypothesis synthesis

The scores **do NOT represent:**

- Biological ground truth
- Validated neuroscience claims
- Causal mechanisms or mechanistic proof
- Replacement for domain expert review

**Interpretation:** Scores should be treated as evidence-mapping summaries for rapid literature synthesis, requiring validation by neuroscientists and biophysicists before biological claims.

### 3. Profile Names Are Reproducibility Handles

- Profile filenames (e.g., `gpt-oss-20b-claude-4.5-mlx-full-profile.json`) are **internal reproducibility identifiers**
- They do **NOT** imply association, endorsement, or naming rights by the original model creators
- Model identifiers are based on public Hugging Face registry names and quantization variants

---

## Environment Variables

Users can configure runtime paths via environment variables:

```bash
# Model storage root
export MLX_MODEL_ROOT=/path/to/mlx_models

# Inference engine URL (for OpenAI-compatible servers)
export ENGINE_URL=http://localhost:4474

# API authentication (if required by your server)
export ENGINE_API_KEY=your-key-here

# Pipeline I/O paths
export MLLM_INPUT_PATH=./inputs
export MLLM_OUTPUT_PATH=./outputs
export MLLM_LOG_PATH=./logs
```

---

## Inference Engine Integration

The pipeline can interface with two engine backends:

### 1. MLX-LM (Local, Recommended)

Direct inference via MLX:

```bash
python mllm-pipeline.py \
  --reasoning_model_names gpt-oss-20b-claude-4.5-mlx \
  --mllm_input_path ./inputs \
  --mllm_output_path ./outputs \
  --engine_url http://localhost:4474
```

### 2. OpenAI-Compatible API Server

If running an MLX server (e.g., `mlx-lm serve`):

```bash
mlx_lm serve --model gpt-oss-20b-claude-4.5-mlx --port 4474
# Then:
python mllm-pipeline.py \
  --engine_url http://localhost:4474 \
  --reasoning_model_names gpt-oss-20b-claude-4.5
```

---

## References

- MLX Documentation: https://ml-explore.github.io/mlx/
- MLX-LM Repository: https://github.com/ml-explore/mlx-lm
- Hugging Face Model Hub: https://huggingface.co/models
- OpenAI Chat Completions API: https://platform.openai.com/docs/api-reference

---

**Last Updated:** 2026-05-21  
**Manuscript Alias:** Multi-LLM HPC Council (10 Models)
