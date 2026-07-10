import os, sys, json, time, requests, re, subprocess, threading
from pathlib import Path
from typing import Optional, List

# JMLLM Package Imports
from jmllm.util.config.model_config import ModelProfile, InferenceConfig
from jmllm.util.config.profiles import get_model_manifest
from jmllm.pipeline.loaders import DeepReadLoader
from jmllm.pipeline.models.llm_wrapper import get_llm_thinking
from jmllm.util.helpers import generate_global_log

REPO_ROOT = Path(__file__).resolve().parents[3]

class PipelineController:
    def __init__(self, args):
        self.args = args
        self.mllm_input_path = Path(args.mllm_input_path)
        self.mllm_output_path = Path(args.mllm_output_path)
        self.mllm_log_path = Path(args.mllm_log_path)
        self.engine_url = args.engine_url
        self.active_model_id = args.reasoning_model_names[0]
        self.vlm_model_id = args.deepread_vlm
        
        # Thread locks
        self._log_lock = threading.RLock()
        self._model_api_lock = threading.Lock()
        
        # Paths verification
        self.mllm_markdown_path = REPO_ROOT / 'content' / 'markdowns'
        self.mllm_markdown_path.mkdir(parents=True, exist_ok=True)
        self.mllm_output_path.mkdir(parents=True, exist_ok=True)
        self.mllm_log_path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, message: str, is_error: bool = False):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        level = "ERROR" if is_error else "INFO"
        formatted_msg = f"[{timestamp}] [{level}] {message}"
        print(formatted_msg)
        with self._log_lock:
            with open(self.mllm_log_path, 'a') as f:
                f.write(formatted_msg + '\n')

    def ensure_monitor_running(self):
        """Verify or start the mllm monitor on port 8081."""
        monitor_path = REPO_ROOT / "legacy" / "scripts" / "watchdog.py" # fallback location
        if not monitor_path.exists():
            monitor_path = REPO_ROOT / "mllm-monitor.py" # just in case
        python_bin = sys.executable
        try:
            requests.get("http://localhost:8081", timeout=2)
            self.log("Dashboard monitor is already active on port 8081.")
        except:
            if monitor_path.exists():
                self.log("Dashboard monitor not responding. Spawning watchdog...")
                subprocess.Popen([python_bin, str(monitor_path)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def get_mlx_key(self, model_id: str) -> str:
        mapping = {
            "gpt-oss-20b-claude-4.5-mlx": "gpt-oss-20b-claude-4.5",
            "deepseek-r1-70b-mlx": "DeepSeek-R1-Distill-Llama-70B-6bit",
            "gemma-3-27b-it-mlx": "gemma-3-27b-it-8bit",
            "mistral-nemo-12b-thinking-mlx": "Mistral-Nemo-12B-Thinking",
            "phi-4-reasoning-plus-mlx": "Phi-4-reasoning-plus-8bit",
            "qwen3.5-40b-opus-4.5-mlx": "Qwen3.5-40B-Claude-4.5-Opus",
            "phi-4-reasoning-plus-8bit": "Phi-4-reasoning-plus-8bit",
        }
        return mapping.get(model_id, model_id)

    def load_model(self, model_id: str) -> bool:
        if getattr(self.args, "no_load", False):
            self.log(f"⏩ Skipping model load for {model_id} (no-load mode).")
            return True
        mlx_key = self.get_mlx_key(model_id)
        
        with self._model_api_lock:
            self.log(f"🚀 Requesting MLX load for {mlx_key} (from {model_id})...")
            url = f"{self.engine_url}/load_model"
            headers = {"Authorization": "Bearer mlx-server"}
            payload = {"model": mlx_key}
            
            # Pass context length to LMS if configured
            context_window = getattr(self.args, "context_window", None)
            if context_window:
                payload["context_length"] = context_window
                payload["n_ctx"] = context_window

            try:
                res = requests.post(url, json=payload, headers=headers, timeout=600)
                if res.status_code == 200:
                    self.log(f"✅ Model {mlx_key} is LOADED and READY.")
                    return True
                else:
                    self.log(f"❌ Engine failed to load model: {res.text}", is_error=True)
                    return False
            except Exception as e:
                self.log(f"❌ API Error during load: {e}", is_error=True)
                return False

    def unload_all(self):
        """Unload all models to free VRAM."""
        if getattr(self.args, "no_load", False):
            self.log("⏩ Skipping model unload (no-load mode).")
            return
        
        with self._model_api_lock:
            self.log("🧹 Unloading all models...")
            url = f"{self.engine_url}/unload_all"
            headers = {"Authorization": "Bearer mlx-server"}
            try:
                requests.post(url, headers=headers, timeout=60)
            except: pass

    def test_model_profile(self, model_id: str):
        """Verify model functionality and mark as verified."""
        self.log(f"🧪 Testing profile: {model_id}")
        if not self.load_model(model_id):
            return False
        
        try:
            manifest = get_model_manifest(model_id) or {}
            profile_data = {
                "model_name": self.get_mlx_key(model_id),
                "api_url": f"{self.engine_url}/v1/chat/completions",
                "api_key": "mlx-server",
                "max_tokens": 10,
                "engine_type": "mlx"
            }
            profile = ModelProfile(**profile_data)
            config = InferenceConfig(request_timeout_seconds=60)
            
            res = get_llm_thinking("say hi", config, profile, response_model=None)
            if res:
                self.log(f"✅ Heartbeat success for {model_id}")
                profile_path = REPO_ROOT / "src/jmllm/util/config/profiles" / f"{model_id}-full-profile.json"
                if not profile_path.exists():
                    profile_path = REPO_ROOT / "src/jmllm/util/config/profiles" / f"{model_id}.json"
                
                if profile_path.exists():
                    with open(profile_path, "r") as f: data = json.load(f)
                    data["availability"] = "verified"
                    with open(profile_path, "w") as f: json.dump(data, f, indent=4)
                    self.log(f"📝 Marked {model_id} as verified.")
                return True
        except Exception as e:
            self.log(f"❌ Heartbeat failed for {model_id}: {e}", is_error=True)
        finally:
            self.unload_all()
        return False

    def run_pipeline(self):
        self.ensure_monitor_running()
        
        if self.args.test_profile:
            for m in self.args.reasoning_model_names:
                self.test_model_profile(m)
            return

        self.log(f"🚀 Starting MLLM Pipeline. Mode: {self.args.mode} | Agent: {self.active_model_id}")
        
        # Phase 1: DeepRead / Extraction (Sequential to avoid VRAM thrashing)
        papers_to_evaluate = []
        
        for pdf_name in self.args.pdfs_to_process:
            base_name = Path(pdf_name).stem
            pdf_path = self.mllm_input_path / f'{base_name}.pdf'
            
            if not pdf_path.exists():
                possible = list(self.mllm_input_path.glob(f'{base_name}*.pdf'))
                if possible:
                    pdf_path = possible[0]
                    self.log(f"Fuzzy matched {base_name} to {pdf_path.name}")
            
            if not pdf_path.exists():
                self.log(f"Paper not found: {base_name} in {self.mllm_input_path}", is_error=True)
                continue

            out_md_path = self.mllm_markdown_path / f'{base_name}-vllm-deepread.md'
            safe_model_id = self.active_model_id.replace("/", "_")
            glossary_name = Path(self.args.glossary_path).parent.name
            
            existing_runs = list(self.mllm_output_path.glob(f'{base_name}_{safe_model_id}_{glossary_name}_run*.json'))
            if existing_runs:
                self.log(f"⏩ Evaluation already exists for {base_name} with {self.active_model_id} ({glossary_name}). Skipping.")
                continue
                
            out_eval_path = self.mllm_output_path / f'{base_name}_{safe_model_id}_{glossary_name}_run1.json'

            study_text = ""
            if out_md_path.exists():
                self.log(f"✅ Using cached DeepRead: {out_md_path.name}")
                with open(out_md_path, 'r') as f: study_text = f.read()
            elif self.args.repair:
                self.log(f"⏩ Repair mode: skipping {base_name} (no DeepRead cache).")
                continue
            else:
                if not self.args.no_vlm:
                    if not self.load_model(self.vlm_model_id): continue
                self.log(f"📥 Extracting: {base_name}")
                try:
                    loader = DeepReadLoader(
                        engine_url=self.engine_url,
                        vlm_model=self.get_mlx_key(self.vlm_model_id),
                        api_key="mlx-server",
                        vlm_engine="mlx",
                        vlm_deepread=not self.args.no_vlm
                    )
                    artifact = loader.extract_parallel(str(pdf_path))
                    study_text = artifact.study_text
                    with open(out_md_path, 'w') as f: f.write(study_text)
                    self.log(f"✅ DeepRead complete: {out_md_path.name}")
                except Exception as e:
                    self.log(f"DeepRead failed for {base_name}: {e}", is_error=True)
                    continue

            if self.args.deepread_only: 
                generate_global_log(self.mllm_log_path.parent)
                continue
            
            papers_to_evaluate.append({
                "base_name": base_name,
                "study_text": study_text,
                "out_eval_path": out_eval_path
            })

        if self.args.deepread_only or not papers_to_evaluate:
            self.unload_all()
            return

        # Phase 2: Load Reasoning Model Once
        if not self.load_model(self.active_model_id):
            return

        # Phase 3: Reasoning (Concurrent using ThreadPoolExecutor)
        parallel_workers = getattr(self.args, "parallel_workers", 1) or 1
        self.log(f"🧠 Starting concurrent reasoning phase on {len(papers_to_evaluate)} papers with {parallel_workers} workers...")

        import concurrent.futures
        
        def evaluate_paper(paper_info):
            base_name = paper_info["base_name"]
            study_text = paper_info["study_text"]
            out_eval_path = paper_info["out_eval_path"]
            
            try:
                self.log(f"🧠 Reasoning: {base_name} via {self.active_model_id}")
                with open(self.args.glossary_path, 'r') as f: glossary = f.read()
                with open(self.args.instructions_path, 'r') as f: instructions = f.read()
                
                manifest = get_model_manifest(self.active_model_id) or {}
                
                top_p = getattr(self.args, "top_p", None)
                min_p = getattr(self.args, "min_p", None)

                profile_data = {
                    "model_name": self.get_mlx_key(self.active_model_id),
                    "api_url": f"{self.engine_url}/v1/chat/completions",
                    "api_key": "mlx-server",
                    "max_tokens": 16384,
                    "engine_type": "mlx",
                    "temperature": self.args.temperature,
                    "top_p": top_p,
                    "min_p": min_p,
                    "context_window": getattr(self.args, "context_window", 131072)
                }
                profile_data.update(manifest)
                profile_data["model_name"] = self.get_mlx_key(self.active_model_id)
                profile_data["api_key"] = "mlx-server"
                profile_data["temperature"] = self.args.temperature
                if top_p is not None:
                    profile_data["top_p"] = top_p
                if min_p is not None:
                    profile_data["min_p"] = min_p

                profile = ModelProfile(**profile_data)
                config = InferenceConfig(request_timeout_seconds=self.args.timeout)
                full_prompt = f'{instructions}\n\n**GLOSSARY:**\n{glossary}\n\n**DOCUMENT:**\n{study_text}\n\n**FILL IN THE SCORES:**'
                
                eval_json_text = get_llm_thinking(unified_prompt=full_prompt, config=config, profile=profile, response_model=None)
                with open(out_eval_path, 'w') as f: f.write(eval_json_text)
                self.log(f'✅ Evaluation complete: {out_eval_path.name}')
            except Exception as e:
                self.log(f'Reasoning failed for {base_name}: {e}', is_error=True)
            
            generate_global_log(self.mllm_log_path.parent)

        if parallel_workers > 1 and len(papers_to_evaluate) > 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=parallel_workers) as executor:
                list(executor.map(evaluate_paper, papers_to_evaluate))
        else:
            for p in papers_to_evaluate:
                evaluate_paper(p)

        # Consolidate outputs to CSV table
        self.log("📊 Consolidating scores into CSV table...")
        from jmllm.util.helpers import aggregate_scores_from_json
        df = aggregate_scores_from_json(self.mllm_output_path)
        if not df.empty:
            tables_dir = REPO_ROOT / 'content' / 'tables'
            tables_dir.mkdir(parents=True, exist_ok=True)
            csv_file = tables_dir / 'aggregated_scores.csv'
            df.to_csv(csv_file, index=False)
            self.log(f"✅ Consolidated table written to {csv_file}")
        else:
            self.log("⚠️ No evaluations found to aggregate.", is_error=True)

        self.log("🎯 Pipeline run complete. Final cleanup...")
        self.unload_all()
