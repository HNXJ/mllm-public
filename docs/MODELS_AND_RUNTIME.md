# Models and Runtime Configuration

## Overview

This document describes the large language models (LLMs) used in the manuscript "Ontology-constrained multi-LLM scoring of hypothesis support in the predictive processing literature" and the runtime environment required to reproduce the evaluation pipeline.

**Runtime Platform:** MLX-LM (Apple Silicon optimized)  
**Inference Engine:** MLX (Machine Learning Accelerated)  
**Deployment Pattern:** Local multi-model council with ontology-constrained prompting

---

## Model Council (10 Models)

The manuscript evaluates predictive coding hypotheses using a council of 10 diverse reasoning models, each selected for different reasoning and quantitative capabilities:

| Model ID | Model Name | Hugging Face ID | Size | Family | Quantization | Context Window | Paper Alias |
|----------|-----------|-----------------|------|--------|--------------|----------------|----|
| 1 | GPT-OSS-20B-Claude-4.5 | gpt-oss-20b-claude-4.5-mlx | 20B | OpenAI OSS | MLX-native | 131,072 | M1 |
| 2 | DeepSeek-R1-70B | deepseek-r1-distill-llama-70b-6bit-mlx | 70B | DeepSeek | MXFP6 | 131,072 | M2 |
| 3 | Gemma-3-27B-IT | gemma-3-27b-it-8bit-mlx | 27B | Google Gemma | MXFP8 | 131,072 | M3 |
| 4 | Phi-4-Reasoning-Plus-8bit | phi-4-reasoning-plus-8bit | 14B | Microsoft Phi | MXFP8 | 131,072 | M4 |
| 5 | Qwen3.5-40B-Opus-4.5 | qwen3.5-40b-opus-4.5-mlx | 40B | Alibaba Qwen | MLX-native | 131,072 | M5 |
| 6 | Mistral-Nemo-12B-Thinking | mistral-nemo-12b-thinking-mlx | 12B | Mistral AI | MLX-native | 128,000 | M6 |
| 7 | Olmo-3-32B-Think | olmo-3-32b-think-mlx | 32B | Allen Institute | MLX-native | 128,000 | M7 |
| 8 | Ministral-3-14B-Instruct | ministral-3-14b-instruct-2512-mxfp8-mlx | 14B | Mistral AI | MXFP8 | 131,072 | M8 |
| 9 | Qwen2.5-32B-Instruct-8bit | qwen2.5-32b-instruct-8bit-mlx | 32B | Alibaba Qwen | MXFP8 | 131,072 | M9 |
| 10 | Gemma-4-31B-IT-8bit | gemma-4-31b-8bit-mlx | 31B | Google Gemma | MXFP8 | 131,072 | M10 |

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
