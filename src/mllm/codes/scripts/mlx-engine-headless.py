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

app = FastAPI(title="mlxEngine: Headless Unified Manager")
security = HTTPBearer()

class EngineManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.current_model_name = None
        self.status = "idle"
        # Force correct paths for this environment
        self.model_root = os.environ.get("MLX_MODEL_ROOT", "/Users/HN/MLLM/mlx_models")
        self.api_key = os.environ.get("ENGINE_API_KEY", "mlx-server")
        logger.info(f"Engine initialized. Root: {self.model_root}, Key: {self.api_key}")

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

        # Headless bypass: just try to load from root
        model_path = os.path.join(self.model_root, model_name)
        if not os.path.exists(model_path):
            # Try case-insensitive or exact folder names from previous listing
            # E.g. Qwen3.5-40B-Claude-4.5-Opus
            logger.warning(f"Path not found: {model_path}. Trying case-insensitive search...")
            possible = [d for d in os.listdir(self.model_root) if d.lower() == model_name.lower()]
            if possible:
                model_path = os.path.join(self.model_root, possible[0])
            else:
                raise HTTPException(status_code=404, detail=f"Model directory not found: {model_name} in {self.model_root}")

        logger.info(f"🚀 Loading MLX model from: {model_path}")
        self.status = "loading"
        self.unload_model()
        
        try:
            loop = asyncio.get_event_loop()
            # mlx_load is synchronous, run in executor
            self.model, self.tokenizer = await loop.run_in_executor(None, lambda: mlx_load(model_path))
            self.current_model_name = model_name
            self.status = "ready"
            logger.info(f"✅ Loaded MLX {model_name}")
        except Exception as e:
            self.status = "error"
            logger.error(f"❌ Load failed for {model_name}: {e}")
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
        "vram_gb": f"{manager.get_vram_usage_gb():.2f}"
    }

@app.post("/load_model")
async def load_model_endpoint(request: Dict[str, str], token: str = Depends(verify_token)):
    await manager.load_model(request.get("model"))
    return {"status": "success", "model": manager.current_model_name}

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest, token: str = Depends(verify_token)):
    if manager.current_model_name != request.model:
         await manager.load_model(request.model)

    if manager.model is None or manager.tokenizer is None:
        raise HTTPException(status_code=400, detail="No MLX model loaded for inference.")
    
    # Use standard MLX LM generation
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
    # Use port 4474 to reclaim it from LM Studio
    uvicorn.run(app, host="0.0.0.0", port=4474)
