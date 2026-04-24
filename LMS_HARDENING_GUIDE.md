# hardening gemmy-cli against LM Studio (LMS) backend bottlenecks

This guide ensures the NeuroPC multi-agent pipeline handles model loading autonomously, efficiently, and with the correct fallback logic.

### 1. Format & Quantization Prioritization Protocol
To maximize the unified memory bandwidth of Apple Silicon and preserve reasoning quality for complex neuro-computational tasks, enforce the following model selection hierarchy:
1. **Primary Target:** Native MLX formats with Microscaling.
   * *Priority 1:* **mxfp8** (Near-lossless fp16 quality, dynamic scaling, identical VRAM footprint to Q8).
   * *Priority 2:* **mxfp4** (Matches Q5/Q6 reasoning, ultra-low VRAM footprint).
2. **Secondary Target:** Standard MLX integer quantization (e.g., q4, q8) for fastest time-to-first-token (pre-fill phase).
3. **Fallback Target:** GGUF formats via llama.cpp. Use only if MLX architecture definitions are completely unsupported and immediate inference is required.

---

### 2. Common LMS Failure Modes & Triage
* **Failure:** `ValueError: [Model] support is not ready yet` or unknown architecture errors.
  * *Diagnosis:* LMS's bundled mlx_lm wrapper is outdated and lacks the tensor graph definitions for bleeding-edge models (e.g., Gemma 4).
  * *Resolution:* Execute the "Surgical Environment Patch" (Section 3) or fall back to native Python inference.
* **Failure:** Immediate crash upon context allocation (often silent or throws a Metal allocation error).
  * *Diagnosis:* Context window size combined with KV-cache data types exceeds available unified memory.
  * *Resolution:* Drastically lower the context length limit in LMS settings, or switch from an mxfp8 to an mxfp4 model to free up VRAM.
* **Failure:** Model loads but generates garbage tokens or hangs infinitely.
  * *Diagnosis:* Incompatible tensor formats clashing with Apple's Metal framework, or a broken GGUF quantization.
  * *Resolution:* Force CPU-only inference by setting GPU Offload to 0. If it runs, the MLX/Metal compilation for that specific model is broken. Discard the model and fetch a different quantization.

---

### 3. The Surgical Environment Patch (Forcing vMLX/mlx-vlm into LMS)
When encountering an MLX architecture that the standard LMS backend rejects, execute the following steps:

**Step A: Locate the LMS Isolated Python Backend**
Path format: `/Users/[USERNAME]/.lmstudio/extensions/backends/vendor/_amphibian/app-mlx-generate-mac14-arm64@[VERSION]/bin/python3`

**Step B: Force-Install Advanced MLX Engines**
```bash
/Users/[USERNAME]/.lmstudio/extensions/backends/vendor/_amphibian/app-mlx-generate-mac14-arm64@[VERSION]/bin/python3 -m pip install --upgrade mlx_lm mlx_vlm vMLX
```

**Step C: Patch the Generator Script**
File: `/Users/[USERNAME]/.lmstudio/extensions/backends/vendor/_amphibian/app-mlx-generate-mac14-arm64@[VERSION]/lib/python3.11/site-packages/mlx_engine/generate.py`
* Add imports at the top:
```python
from mlx_vlm.models.gemma4 import Model as Gemma4Model
```
* Modify `load_model` to catch unsupported architectures and route them through vMLX or mlx_vlm.

---

### 4. The Native Python Fallback (Bypassing LMS UI)
If LMS application updates overwrite the surgical patches, deploy native Python execution.

**Native Loading Script Template:**
```python
import sys
try:
    from mlx_vlm.models.gemma4 import Model
    import mlx.core as mx
except ImportError:
    print(\"CRITICAL: Run 'pip install mlx_vlm vMLX' in your active environment.\")
    sys.exit(1)

def load_native_agent(model_path):
    print(f\"Bypassing LMS wrapper. Loading {model_path} directly via Metal backend...\")
    # Initialize model using pure vMLX/mlx_lm logic
    pass
```
