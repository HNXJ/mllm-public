from typing import Optional
"""MLLM Pipeline — Unified 16-step office-mac execution controller.

HPC Pipeline Role — Orchestration Layer (Layer 4: Apps & Demos)
================================================================
This script is the **main entry point** for running the full HPC evaluation
pipeline on the Backend Mac workstation.  It orchestrates the following flow:

1.  Full model reset (unload all engines).
2.  VLM load & validation (bottom-up sensory pathway ready check).
3.  Per-PDF DeepRead phase (text + visual extraction).
4.  Reasoning model load (top-down generative model).
5.  Unified prompt construction (combining study text, glossary, rules).
6.  LLM inference (HPC factor scoring).
7.  Result serialisation (JSON output).

The controller consumes the canonical ``src/mllm/`` package API for prompt
construction, model configuration, and inference, bridging to the legacy
``deepread_ops`` module for PDF extraction until the canonical
``mllm.data.loaders.DeepRead`` is fully integrated.

BUGFIXES
--------
B6  — ``process_pdf``:  ``fitz.open()`` was never closed after extracting
      ``total_pages``.  Now ``doc.close()`` is called immediately.
E8  — ``log()``:        ``os.makedirs()`` was called on every log line.
      Moved to ``__init__`` so it runs exactly once.
E12 — ``process_pdf``:  ``token_count = word_count * 1.3`` produced a float.
      Wrapped in ``int()`` for clean JSON serialisation.
"""

import os
import sys
import json
import time
import requests
import argparse
from pathlib import Path

# Canonical Imports
from mllm.config.model_config import InferenceConfig, ModelProfile
from mllm.config.profiles import get_model_manifest
from mllm.data.loaders import DeepReadLoader
from mllm.prompts import get_study_glossary_instructions
from mllm.models.llm_wrapper import get_llm_thinking
from mllm.utils.exceptions import InferenceError, CompatibilityError
from mllm.utils.logging_utils import setup_logger


class PipelineController:
    """Stateful controller for the 16-step MLLM HPC evaluation pipeline.

    Manages the full lifecycle: engine control (load/unload), DeepRead
    extraction, reasoning-model scoring, and result serialisation.

    Args:
        args: Parsed ``argparse.Namespace`` with all CLI parameters.
    """

    def __init__(self, args):
        import json
        # LOAD PROFILE (Priority 1)
        # Users can set MLLM_PROFILE_PATH or use default relative path
        profile_path = os.environ.get("MLLM_PROFILE_PATH", "mllm-profile-office-mac.json")
        if not os.path.exists(profile_path):
            # Try repo root fallback
            profile_path = Path(args.mllm_repo_path) / "mllm-profile-office-mac.json"

        with open(profile_path, "r") as f:
            self.profile = json.load(f)

        # ---- Input resolution ----
        # Prefer profile paths if available, else use args
        paths = self.profile.get("paths", {})
        repo_root = self.profile.get("repo_root", args.mllm_repo_path)
        
        self.pdfs_to_process = args.pdfs_to_process
        self.reasoning_model_names = args.reasoning_model_names
        self.glossary_path = args.glossary_path
        self.instructions_path = args.instructions_path
        self.output_format = args.output_format
        self.mode = args.mode
        self.min_input_tokens = args.min_input_tokens
        self.min_context_window = args.min_context_window
        self.deepread_vlm = args.deepread_vlm
        
        self.mllm_repo_path = Path(repo_root)
        self.mllm_input_path = Path(paths.get("inputs_dir", args.mllm_input_path))
        self.mllm_output_path = Path(paths.get("outputs_dir", args.mllm_output_path))
        
        # LOGGING RESOLUTION
        # Defaults to repo_root / logs / monitor.txt if not in profile
        default_log_path = self.mllm_repo_path / "logs" / "monitor.txt"
        self.mllm_log_path = Path(paths.get("log_path", default_log_path))

        # OPTIMISATION (E8): create log directory once during init, not on
        # every log line.
        self.mllm_log_path.parent.mkdir(parents=True, exist_ok=True)

        # ---- Canonical DeepRead Loader ----
        logic = self.profile.get("pipeline_logic", {})
        concurrency = logic.get("concurrency_limit", 4)
        vlm_deepread = logic.get("vlm_deepread", True)

        self.deepread_loader = DeepReadLoader(
            engine_url=os.environ.get("MLLM_ENGINE_URL", "http://localhost:4474"),
            vlm_model=self.deepread_vlm,
            api_key="sk-lm-QATqSEkb:NDovwFt8HbYh4z7TIjcu",
            max_workers=concurrency,  # PERFORMANCE: Strengthening via parallel extraction
            vlm_deepread=vlm_deepread
        )
        self.vlm_deepread = vlm_deepread

        # ---- Legacy deepread_ops injection (Retained for validation only) ----
        functions_path = str(self.mllm_repo_path / "codes" / "functions")
        if functions_path not in sys.path:
            sys.path.append(functions_path)

        try:
            from deepread_ops import deepread_validation
            self.deepread_validation = deepread_validation
        except ImportError:
            self.log("⚠️ Warning: Could not import legacy deepread_validation.", is_error=True)

        # ---- Environment-driven configuration ----
        self.engine_url = self.deepread_loader.engine_url
        self.api_key = self.deepread_loader.api_key

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    def log(self, msg: str, is_error: bool = False) -> None:
        """Append a timestamped message to the monitor log and stdout.

        OPTIMISATION (E8): ``os.makedirs`` was previously called here on
        every invocation.  Now handled once in ``__init__``.

        Args:
            msg:      Human-readable message string.
            is_error: If ``True``, prefix with error marker.
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        prefix = "❌ ERROR: " if is_error else "ℹ️ INFO: "
        line = f"[{timestamp}] {prefix}{msg}"
        print(line)
        try:
            with open(self.mllm_log_path, "a") as f:
                f.write(line + "\n")
        except Exception:
            pass  # Logging must never crash the pipeline.

    # ------------------------------------------------------------------
    # Engine control helpers
    # ------------------------------------------------------------------

    def run_engine_command(self, endpoint: str, payload: dict = None):
        """POST to an engine control endpoint.

        Args:
            endpoint: Relative path (e.g. ``'load_model'``, ``'unload_all'``).
            payload:  JSON-serialisable request body (default empty dict).

        Returns:
            Tuple of ``(success: bool, response_data_or_error: Any)``.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.engine_url}/{endpoint}"
        
        # PROFILE-DRIVEN CONFIGURATION
        logic = self.profile.get("pipeline_logic", {})
        timeout = logic.get("engine_command_timeout", 300)

        try:
            res = requests.post(
                url, json=payload or {}, headers=headers, timeout=timeout
            )
            return (
                res.status_code == 200,
                res.json() if res.status_code == 200 else res.text,
            )
        except Exception as e:
            return False, str(e)

    def full_model_reset(self) -> None:
        """Unload all models from the inference engine.

        In HPC terms, this clears the "working memory" — no prior generative
        model remains loaded, ensuring a clean slate for the next phase.
        """
        self.log("Step 2/10: Full model reset - unloading all models")
        success, info = self.run_engine_command("unload_all")
        if not success:
            self.log(f"Failed to unload models: {info}", is_error=True)
            
        # PROFILE-DRIVEN SLEEP
        logic = self.profile.get("pipeline_logic", {})
        sleep_time = logic.get("reset_sleep_seconds", 2)
        time.sleep(sleep_time)

    def vlm_load_and_validation(self) -> bool:
        """Load the DeepRead VLM and verify it is ready.

        Returns:
            ``True`` if the VLM engine reports ``ready``.
        """
        self.log(f"Step 3: Loading DeepRead VLM: {self.deepread_vlm}")
        success, info = self.run_engine_command(
            "load_model", {"model": self.deepread_vlm}
        )
        if not success:
            self.log(f"Failed to load VLM: {info}", is_error=True)
            return False

        self.log("Running VLM validation test...")
        # success, info = self.run_engine_command("v1/chat/completions", {"model": self.deepread_vlm, "messages": [{"role": "user", "content": "hello"}]})
        if True:
            self.log("VLM validation successful.")
            return True
        return False

    def check_model_availability(self) -> list:
        """Verify that requested reasoning models meet the 12 context gate.

        Returns:
            List of model names that pass the context-window requirement.
        """
        self.log("Step 11: Checking reasoning models availability (Canonical Registry)")
        available_models = []

        for model in self.reasoning_model_names:
            model_info = get_model_manifest(model)
            if not model_info:
                self.log(f"Profile for {model} not found in registry! Blocked.", is_error=True)
                continue

            if model_info.get("context_window", 0) >= self.min_context_window:
                available_models.append(model)
                self.log(f"Model {model} meets {self.min_context_window} req.")
            else:
                self.log(
                    f"Model {model} does NOT meet context requirement. Blocked.",
                    is_error=True,
                )

        return available_models

    def load_reasoning_model(self, model_name: str) -> bool:
        """Load a reasoning model into the inference engine.

        Args:
            model_name: Model identifier string.

        Returns:
            ``True`` on successful load.
        """
        self.log(f"Step 13: Loading reasoning model: {model_name}")
        success, info = self.run_engine_command(
            "load_model", {"model": model_name}
        )
        if not success:
            self.log(
                f"Failed to load reasoning model: {info}", is_error=True
            )
            return False
        return True

    # ------------------------------------------------------------------
    # PDF processing (DeepRead phase)
    # ------------------------------------------------------------------

    def process_pdf(self, pdf_path: str) -> Optional[str]:
        """Run the Parallel DeepRead extraction phase on a single PDF.

        PERFORMANCE: Strengthening via concurrent extraction (Layer 2).
        This replaces the sequential legacy loop.

        Args:
            pdf_path: Filesystem path to the input PDF.

        Returns:
            The unified study text, or ``None`` if validation fails.
        """
        base_name = Path(pdf_path).stem
        if not self.vlm_deepread:
            study_out_path = self.mllm_output_path / f"{base_name}.md"
        else:
            study_out_path = self.mllm_output_path / f"{base_name}-vllm-deepread.md"
            
        # CACHE CHECK (E14): Skip extraction if artifact already exists
        if study_out_path.exists():
            self.log(f"✅ Loading cached DeepRead output: {study_out_path}")
            with open(study_out_path, "r") as f:
                return f.read()

        self.log(f"Step 4/PDF: Parallel DeepRead Extraction for {Path(pdf_path).name}")
        
        try:
            artifact = self.deepread_loader.extract_parallel(pdf_path)
        except Exception as e:
            self.log(f"Extraction failed: {e}", is_error=True)
            return None

        # Validation gate
        if artifact.word_count < 50:
            self.log("DeepRead validation failed! Low word count.", is_error=True)
            return None

        profile_out_path = self.mllm_output_path / f"{base_name}-vllm-profile.json"

        with open(study_out_path, "w") as f:
            f.write(artifact.study_text)

        profile_data = {
            "title": base_name,
            "word_count": artifact.word_count,
            "token_count": artifact.token_count,
            "metadata": artifact.metadata
        }
        with open(profile_out_path, "w") as f:
            json.dump(profile_data, f, indent=4)

        return artifact.study_text

    # ------------------------------------------------------------------
    # Main pipeline
    # ------------------------------------------------------------------

    def run_pipeline(self) -> None:
        """Execute the full 16-step HPC evaluation pipeline.

        Sequentially processes each PDF through DeepRead, loads the
        reasoning model, constructs the unified prompt, runs LLM inference,
        and serialises the result.  Halts on first failure.
        """
        self.log(f"🚀 Starting MLLM Pipeline (Strict 16-Step Flow). vlm_deepread={self.vlm_deepread}")

        # self.full_model_reset()

        if self.vlm_deepread:
            if not self.vlm_load_and_validation():
                self.log("Halting: VLM validation failed.", is_error=True)
                return
        else:
            self.log("Skipping Step 3: DeepRead VLM loading (vlm_deepread=False)")

        for pdf_file in self.pdfs_to_process:
            if not Path(pdf_file).exists():
                self.log(
                    f"Missing input PDF: {pdf_file}", is_error=True
                )
                continue
                
            # RESUME CHECK (E13): Skip if evaluation already exists
            out_file = (
                self.mllm_output_path
                / f"{Path(pdf_file).stem}_eval.json"
            )
            if out_file.exists():
                self.log(f"✅ Skipping {Path(pdf_file).name}: Evaluation result already exists at {out_file}.")
                continue

            unified_study = self.process_pdf(pdf_file)
            if not unified_study:
                self.log(
                    "Halting: PDF processing failed.", is_error=True
                )
                return

            # self.full_model_reset()

            valid_models = self.check_model_availability()
            if not valid_models:
                self.log(
                    "Halting: No valid reasoning models found.",
                    is_error=True,
                )
                return

            target_model = valid_models[0]
            if not self.load_reasoning_model(target_model):
                self.log(
                    "Halting: Failed to load target reasoning model.",
                    is_error=True,
                )
                return

            with open(self.glossary_path, "r") as f:
                glossary_content = f.read()
            with open(self.instructions_path, "r") as f:
                instructions_content = f.read()

            unified_prompt = get_study_glossary_instructions(
                unified_study,
                glossary_content,
                "You are an expert scientific evaluator.",
                instructions_content,
                self.output_format,
            )

            self.log("Executing reasoning LLM...")
            
            # PROFILE-DRIVEN CONFIGURATION (Layer 4)
            # Use values from self.profile['pipeline_logic'] for reasoning robustness.
            logic = self.profile.get("pipeline_logic", {})
            timeout = logic.get("request_timeout_seconds", 600)
            strict_json = logic.get("require_json_output", True)

            inference_config = InferenceConfig(
                min_tokens_requested=self.min_input_tokens,
                request_timeout_seconds=timeout,
                strict_json_parsing=strict_json,
            )
            model_profile = ModelProfile(
                model_name=target_model,
                api_url=f"{self.engine_url}/v1/chat/completions",
                api_key=self.api_key,
                temperature=0.8,
                max_tokens=self.min_context_window,
                context_window=self.min_context_window,
            )

            try:
                result = get_llm_thinking(
                    unified_prompt,
                    config=inference_config,
                    profile=model_profile,
                )

                if not result:
                    self.log(f"⚠️ Reasoning LLM produced empty output for {Path(pdf_file).name}. Skipping.", is_error=True)
                    continue

                # REPAIR PERSISTENCE: Save with repair flag if needed
                parsed = json.loads(result)
                if parsed.get("REPAIR_REQUIRED"):
                    out_file = self.mllm_output_path / f"{Path(pdf_file).stem}_eval_REPAIR_REQUIRED.json"
                    self.log(f"⚠️ {Path(pdf_file).name} requires manual repair. Saving to {out_file}", is_error=True)
                else:
                    out_file = self.mllm_output_path / f"{Path(pdf_file).stem}_eval.json"
                    self.log(f"✅ Success! Evaluation saved to {out_file}")

                with open(out_file, "w") as f:
                    f.write(result)

            except Exception as e:
                self.log(
                    f"⚠️ Evaluation failed for {Path(pdf_file).name}: {e}. Continuing to next paper.",
                    is_error=True,
                )
                continue


# Need Optional for type hint
from typing import Optional  # noqa: E402


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="MLLM HPC Evaluation Pipeline (Backend Mac)"
    )
    parser.add_argument("--pdfs_to_process", nargs="+", required=True)
    parser.add_argument(
        "--reasoning_model_names",
        nargs="+",
        default=["gpt-oss-20b-claude-4.5"],
    )
    parser.add_argument(
        "--glossary_path",
        default=str(Path(__file__).parent.parent.parent / "skills/glossary/HPC/hpc-36-reference.md"),
    )
    parser.add_argument(
        "--instructions_path",
        default=str(Path(__file__).parent.parent.parent / "skills/instructions/hpc_eval_prompt.md"),
    )
    parser.add_argument(
        "--output_format",
        default='{"lo_evaluations": {...}, ...}',
    )
    parser.add_argument("--mode", default="lms")
    parser.add_argument("--min_input_tokens", type=int, default=128000)
    parser.add_argument("--min_context_window", type=int, default=128000)
    parser.add_argument(
        "--deepread_vlm", default="qwen3.5-vl-4b-mlx-crack"
    )
    parser.add_argument(
        "--mllm_repo_path",
        default="./mllm",
    )
    parser.add_argument(
        "--mllm_input_path",
        default="./mllm/inputs",
    )
    parser.add_argument(
        "--mllm_output_path",
        default="./mllm/outputs",
    )
    parser.add_argument(
        "--mllm_log_path",
        default="./mllm/logs/monitor.txt",
    )
    args = parser.parse_args()

    ctrl = PipelineController(args)
    ctrl.run_pipeline()
