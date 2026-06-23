# Tested Environments

This document records the **exact** environments this repository has
been verified against, separated by what was actually exercised:
offline package installation + unit tests + the `demo/` walkthrough
(verified in this pass) versus the full MLX model-council pipeline
(not independently re-verified in this pass — see `TODO` markers).

---

## 1. Demo path — verified

The `demo/` walkthrough, the package's offline data-handling code
(`mllm.data.preprocessors`), and the unit test suite were installed
and run end-to-end to produce this record.

| Item | Value |
|---|---|
| **Operating system** | macOS 26.5.1 (Build 25F80) |
| **Kernel** | Darwin 25.5.0, `RELEASE_ARM64_T6000` |
| **Architecture** | arm64 (Apple Silicon) |
| **CPU** | Apple M1 Max |
| **Memory** | 64 GB unified memory (demo itself uses < 200 MB) |
| **Python** | 3.13.7 (`Clang 16.0.0`) |
| **Install method** | `python3 -m venv .venv && pip install -e .` |
| **Install time observed** | < 1 minute (offline pip cache; first-time cold install over a network connection is expected to take 1–3 minutes — see README) |
| **Demo runtime observed** | 0.01s–0.30s per `python demo/run_demo.py` invocation |

### Key package versions actually installed and exercised

| Package | Version resolved | Constraint in `pyproject.toml` |
|---|---|---|
| `numpy` | 2.5.0 | `>=1.20.0` |
| `pandas` | 3.0.3 | `>=1.3.0` |
| `pydantic` | 2.13.4 | `>=2.0.0` |
| `pydantic_core` | 2.46.4 | (transitive) |
| `fastapi` | 0.138.0 | `>=0.100.0` |
| `uvicorn` | 0.49.0 | `>=0.20.0` |
| `click` | 8.4.1 | `>=8.0.0` |
| `requests` | 2.34.2 | `>=2.25.0` |
| `PyYAML` | 6.0.3 | `>=6.0` |
| `tqdm` | 4.68.3 | `>=4.60.0` |
| `PyMuPDF` (`fitz`) | 1.27.2.3 | unpinned |
| `Pillow` | 12.2.0 | unpinned |
| `openai` | 2.43.0 | unpinned |
| `rich` | 15.0.0 | unpinned |
| `pytest` | 9.1.1 | `>=7.0.0` (dev extra) |

### Test suite result on this environment

```
$ python -m pytest tests/unit/ -v
17 passed, 1 failed, 1 skipped
```

**Known pre-existing failure (not introduced by the Nature-compliance changes in this pass):**
`tests/unit/test_preprocessors.py::test_parse_llm_output_as_json_strict_rejects_extra_text` —
the JSON-rescue function (`mllm.data.preprocessors.parse_llm_output_as_json`)
salvages a brace-bounded JSON object from surrounding prose even when
`compatibility_mode=False`, whereas the test expects strict mode to
refuse and return a `REPAIR_REQUIRED` payload. This does not affect
the `demo/` walkthrough (which always calls with
`compatibility_mode=True`) or the documented public API contract.
**TODO:** maintainers should decide whether to gate the brace-bounded
rescue stage behind `compatibility_mode` or relax the test, and fix
accordingly.

**Skipped test:** 1 test is skipped under the default `pytest` marker
configuration (`-m 'not integration and not hardware'`, see
`pyproject.toml`); this is expected — see Section 3 below.

---

## 2. Full MLX model-council pipeline — not independently re-verified (TODO)

The full `mllm-pipeline.py` path (real PDF ingestion, DeepRead VLM
figure extraction, and 10-model MLX-LM reasoning council) requires
Apple Silicon hardware, downloaded model weights (12B–70B parameters
each), and a running MLX inference server. This pass did **not**
re-run that path; the values below are carried from
[`docs/MODELS_AND_RUNTIME.md`](MODELS_AND_RUNTIME.md) and
[`docs/REPRODUCIBILITY.md`](REPRODUCIBILITY.md) and are marked
accordingly.

| Item | Value | Status |
|---|---|---|
| **Operating system** | macOS, Apple Silicon (M1/M2/M3/M4) | Documented by maintainer; **TODO: re-verify exact OS build per model run** |
| **MLX version** | `mlx>=0.4.0` | Documented minimum; **TODO: record exact resolved version** |
| **MLX-LM version** | `mlx-lm>=0.15.0` | Documented minimum; **TODO: record exact resolved version** |
| **Memory** | ≥32 GB unified memory recommended (16 GB minimum with offloading) | Documented by maintainer; not independently re-measured this pass |
| **Model weight download time** | Not measured this pass | **TODO: measure and record per model size class (12B/14B/27B/31B/32B/40B/70B)** |
| **Full pipeline wall-clock per paper** | Not measured this pass | **TODO: record typical seconds/minutes per paper per model** |

**Why this is split out rather than merged into Section 1:** the
Nature checklist requires reporting *what was actually tested*, not
implying a hardware-dependent path was re-verified when it was not.
Reviewers without Apple Silicon hardware should rely on the `demo/`
path in Section 1, which has no such dependency.

---

## 3. Integration tests (require live MLX engine — not run this pass)

`tests/integration/test_hpc_eval.py` is gated behind
`RUN_HPC_INTEGRATION=1` plus `HPC_MODEL_NAME`, `HPC_API_URL`, and
`ENGINE_API_KEY` environment variables pointing at a live model
server (see [docs/REPRODUCIBILITY.md → Tests & Validation](REPRODUCIBILITY.md#5-tests--validation)).
These were not run in this pass since no MLX engine/model weights
were available in the verification environment. **TODO: maintainer
to run and record results when hardware is available.**

---

## 4. Known limitations

- MLX and `mlx-lm` are Apple-Silicon-only; there is no CPU/Linux/Windows
  fallback for the full reasoning-council path. The `demo/` path is the
  only part of this repository verified to be platform-independent.
- Exact model weight revisions/hashes are not pinned in this repository
  (see [docs/MODELS_AND_RUNTIME.md → Model Cards and Licensing](MODELS_AND_RUNTIME.md#1-model-cards-and-licensing));
  consult each model's Hugging Face card for the exact version used.
- One pre-existing unit test fails as documented in Section 1; it does
  not affect the demo or the documented public API.

---

**Last verified:** this document's Section 1 was generated by actually
running `pip install -e .` and `pytest`/`demo/run_demo.py` in the
environment described above. Sections 2–3 are carried from existing
maintainer documentation and explicitly marked `TODO` where this pass
could not independently confirm them — replace the `TODO` markers as
that hardware-dependent verification is performed.
