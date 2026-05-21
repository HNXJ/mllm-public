import argparse, os, sys, json, time, requests, re, subprocess
from pathlib import Path
from typing import Optional, List

# MLLM Package Imports
from mllm.config.model_config import ModelProfile, InferenceConfig
from mllm.config.profiles import get_model_manifest
from mllm.data.loaders import DeepReadLoader
from mllm.models.llm_wrapper import get_llm_thinking
from mllm.utils.global_logger import generate_global_log

REPO_ROOT = Path(__file__).parent.resolve()

class PipelineController:
    def __init__(self, args):
        self.args = args
        self.mllm_input_path = Path(args.mllm_input_path)
        self.mllm_output_path = Path(args.mllm_output_path)
        self.mllm_log_path = Path(args.mllm_log_path)
        self.engine_url = args.engine_url
        self.active_model_id = args.reasoning_model_names[0]
        self.vlm_model_id = args.deepread_vlm
        
        # Paths verification
        self.mllm_output_path.mkdir(parents=True, exist_ok=True)
        self.mllm_log_path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, message: str, is_error: bool = False):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        level = "ERROR" if is_error else "INFO"
        formatted_msg = f"[{timestamp}] [{level}] {message}"
        print(formatted_msg)
        with open(self.mllm_log_path, 'a') as f:
            f.write(formatted_msg + '\n')

    def ensure_monitor_running(self):
        """Verify or start the mllm monitor on port 8081."""
        monitor_path = REPO_ROOT / "mllm-monitor.py"
        python_bin = sys.executable
        try:
            requests.get("http://localhost:8081", timeout=2)
            self.log("Dashboard monitor is already active on port 8081.")
        except:
            self.log("Dashboard monitor not responding. Spawning mllm-monitor.py...")
            subprocess.Popen([python_bin, str(monitor_path)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def get_mlx_key(self, model_id: str) -> str:
        # Mapping from profile name to MLX-LM model identifier.
        # For local paths, users should configure via MLX_MODEL_ROOT env var.
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
        mlx_key = self.get_mlx_key(model_id)
        self.log(f"🚀 Requesting MLX load for {mlx_key} (from {model_id})...")
        url = f"{self.engine_url}/load_model"
        headers = {"Authorization": "Bearer mlx-server"}
        try:
            res = requests.post(url, json={"model": mlx_key}, headers=headers, timeout=600)
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
            
            # Minimal verification query
            res = get_llm_thinking("say hi", config, profile, response_model=None)
            if res:
                self.log(f"✅ Heartbeat success for {model_id}")
                # Update local profile
                profile_path = REPO_ROOT / "src/mllm/config/profiles" / f"{model_id}-full-profile.json"
                if not profile_path.exists():
                    profile_path = REPO_ROOT / "src/mllm/config/profiles" / f"{model_id}.json"
                
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
        
        # Initial Load
        if not self.load_model(self.active_model_id):
            return

        for pdf_name in self.args.pdfs_to_process:
            # Handle glob or direct name
            base_name = Path(pdf_name).stem
            pdf_path = self.mllm_input_path / f'{base_name}.pdf'
            
            # Fuzzy match fallback
            if not pdf_path.exists():
                possible = list(self.mllm_input_path.glob(f'{base_name}*.pdf'))
                if possible:
                    pdf_path = possible[0]
                    self.log(f"Fuzzy matched {base_name} to {pdf_path.name}")
            
            if not pdf_path.exists():
                self.log(f"Paper not found: {base_name} in {self.mllm_input_path}", is_error=True)
                continue

            out_md_path = self.mllm_output_path / f'{base_name}-vllm-deepread.md'
            safe_model_id = self.active_model_id.replace("/", "_")
            out_eval_path = self.mllm_output_path / f'{base_name}_{safe_model_id}_eval.json'

            # 1. Check if reasoning already exists
            if out_eval_path.exists():
                self.log(f"⏩ Evaluation already exists for {base_name} with {self.active_model_id}. Skipping.")
                continue

            # 2. DeepRead Phase
            study_text = ""
            if out_md_path.exists():
                self.log(f"✅ Using cached DeepRead: {out_md_path.name}")
                with open(out_md_path, 'r') as f: study_text = f.read()
            elif self.args.repair:
                self.log(f"⏩ Repair mode: skipping {base_name} (no DeepRead cache).")
                continue
            else:
                # Load VLM
                if not self.load_model(self.vlm_model_id): continue
                self.log(f"📥 Extracting: {base_name}")
                try:
                    loader = DeepReadLoader(
                        engine_url=self.engine_url,
                        vlm_model=self.get_mlx_key(self.vlm_model_id),
                        api_key="mlx-server",
                        vlm_engine="mlx"
                    )
                    artifact = loader.extract_parallel(str(pdf_path))
                    study_text = artifact.study_text
                    with open(out_md_path, 'w') as f: f.write(study_text)
                    self.log(f"✅ DeepRead complete: {out_md_path.name}")
                    # Reload Reasoning Model
                    if not self.load_model(self.active_model_id): continue
                except Exception as e:
                    self.log(f"DeepRead failed for {base_name}: {e}", is_error=True)
                    continue

            if self.args.deepread_only: 
                generate_global_log()
                continue

            # 3. Reasoning Phase
            try:
                self.log(f"🧠 Reasoning: {base_name} via {self.active_model_id}")
                with open(self.args.glossary_path, 'r') as f: glossary = f.read()
                with open(self.args.instructions_path, 'r') as f: instructions = f.read()
                
                manifest = get_model_manifest(self.active_model_id) or {}
                profile_data = {
                    "model_name": self.get_mlx_key(self.active_model_id),
                    "api_url": f"{self.engine_url}/v1/chat/completions",
                    "api_key": "mlx-server",
                    "max_tokens": 16384,
                    "engine_type": "mlx"
                }
                profile_data.update(manifest)
                profile_data["model_name"] = self.get_mlx_key(self.active_model_id)
                profile_data["api_key"] = "mlx-server"
                profile = ModelProfile(**profile_data)
                
                config = InferenceConfig(request_timeout_seconds=2400)
                full_prompt = f'{instructions}\n\n**GLOSSARY:**\n{glossary}\n\n**DOCUMENT:**\n{study_text}\n\n**FILL IN THE SCORES:**'
                
                eval_json_text = get_llm_thinking(unified_prompt=full_prompt, config=config, profile=profile, response_model=None)
                with open(out_eval_path, 'w') as f: f.write(eval_json_text)
                self.log(f'✅ Evaluation complete: {out_eval_path.name}')
            except Exception as e:
                self.log(f'Reasoning failed for {base_name}: {e}', is_error=True)
            
            # Refresh global log
            generate_global_log()

        self.log("🎯 Pipeline run complete. Final cleanup...")
        self.unload_all()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MLLM HPC Evaluation Pipeline')
    parser.add_argument('--pdfs_to_process', nargs='+', default=[])
    parser.add_argument('--reasoning_model_names', nargs='+', default=['gpt-oss-20b-claude-4.5'])
    parser.add_argument('--glossary_path', default=str(REPO_ROOT / 'src/mllm/skills/glossary/HPC/hpc-36-reference.md'))
    parser.add_argument('--instructions_path', default=str(REPO_ROOT / 'src/mllm/skills/instructions/hpc_eval_prompt.md'))
    parser.add_argument('--mllm_input_path', default=os.environ.get('MLLM_INPUT_PATH', './inputs'))
    parser.add_argument('--mllm_output_path', default=os.environ.get('MLLM_OUTPUT_PATH', './outputs'))
    parser.add_argument('--mllm_log_path', default=os.environ.get('MLLM_LOG_PATH', './logs/pipeline.log'))
    parser.add_argument('--engine_url', default=os.environ.get('ENGINE_URL', 'http://localhost:4474'))
    parser.add_argument('--mode', default='mlx')
    parser.add_argument('--deepread_vlm', default='qwen3.5-vl-4b-mlx-crack')
    parser.add_argument('--deepread_only', action='store_true')
    parser.add_argument('--test_profile', action='store_true')
    parser.add_argument('--repair', action='store_true')
    args = parser.parse_args()
    PipelineController(args).run_pipeline()
