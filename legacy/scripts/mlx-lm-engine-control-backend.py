import os
import gc
import json
import time
import asyncio
import logging
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import mlx.core as mx
from mlx_lm.utils import load as mlx_load
from mlx_lm.generate import generate
from mlx_lm.sample_utils import make_sampler

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mlx-engine")

app = FastAPI(title="mlxEngine: Backend Unified Manager")
security = HTTPBearer()

# Configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "engine-config.json")
# Status file is now in the same directory as logs, relative to the script
DEFAULT_LOGS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "logs")
STATUS_FILE = os.environ.get("MLLM_STATUS_FILE", os.path.join(DEFAULT_LOGS_DIR, "engine-status.md"))

class EngineManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.current_model_name = None
        self.status = "idle"
        self.config = self.load_config()
        # Use env for API key, fallback to config
        self.api_key = os.environ.get("ENGINE_API_KEY") or self.config.get("defaults", {}).get("api_key")
        if not self.api_key:
            logger.warning("No ENGINE_API_KEY set. Defaulting to 'none'.")
            self.api_key = "none"
            
        self.model_root = os.environ.get("MLX_MODEL_ROOT") or self.config.get("defaults", {}).get("model_root", "/tmp/mlx_models")

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        return {"defaults": {}, "models": []}

    def log_status(self, message: str):
        try:
            os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
            with open(STATUS_FILE, "a") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
        except Exception as e:
            logger.error(f"Failed to log status: {e}")

    def get_vram_usage_gb(self):
        try: return mx.get_active_memory() / (1024**3) # type: ignore
        except: return 0.0

    def unload_model(self):
        if self.model is not None:
            logger.info(f"Unloading: {self.current_model_name}")
            del self.model
            del self.tokenizer
            self.model = None
            self.tokenizer = None
            self.current_model_name = None
            gc.collect()
            mx.metal.clear_cache() # type: ignore

    async def load_model(self, model_name: str):
        if self.current_model_name == model_name and self.status == "ready":
            return

        model_info = next((m for m in self.config["models"] if m["name"] == model_name), None)
        if not model_info:
            raise HTTPException(status_code=404, detail=f"Model {model_name} not in config.")

        if model_info["type"] == "lms":
             self.log_status(f"LMS Model requested: {model_name}. Ensure LM Studio is running on 4474.")
             self.current_model_name = model_name
             self.status = "ready"
             return

        model_path = os.path.join(self.model_root, model_info["path"])
        self.status = "loading"
        self.unload_model()
        
        try:
            loop = asyncio.get_event_loop()
            self.model, self.tokenizer = await loop.run_in_executor(None, lambda: mlx_load(model_path))
            self.current_model_name = model_name
            self.status = "ready"
            self.log_status(f"Loaded MLX {model_name}")
        except Exception as e:
            self.status = "error"
            logger.error(f"Load failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))

manager = EngineManager()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != manager.api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return credentials.credentials

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Dict[str, str]]
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    max_tokens: Optional[int] = 2048

@app.get("/status")
async def get_status():
    return {
        "status": manager.status,
        "current_model": manager.current_model_name,
        "vram_gb": f"{manager.get_vram_usage_gb():.2f}",
        "config_models": [m["name"] for m in manager.config["models"]]
    }

@app.post("/load_model")
async def load_model_endpoint(request: Dict[str, str], token: str = Depends(verify_token)):
    await manager.load_model(request.get("model"))
    return {"status": "success", "model": manager.current_model_name}

@app.post("/unload_all")
async def unload_all_endpoint(token: str = Depends(verify_token)):
    manager.unload_model()
    return {"status": "success", "message": "All models unloaded"}

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest, token: str = Depends(verify_token)):
    if manager.current_model_name != request.model:
         await manager.load_model(request.model)

    if manager.model is None or manager.tokenizer is None:
        raise HTTPException(status_code=400, detail="No MLX model loaded for inference.")
    
    prompt = manager.tokenizer.apply_chat_template(request.messages, tokenize=False, add_generation_prompt=True)
    sampler = make_sampler(request.temperature, request.top_p)

    def generate_response():
        response = generate(manager.model, manager.tokenizer, prompt=prompt, 
                            max_tokens=request.max_tokens, sampler=sampler)
        return {
            "choices": [{"message": {"role": "assistant", "content": response}}],
            "model": manager.current_model_name
        }

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, generate_response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4474)
