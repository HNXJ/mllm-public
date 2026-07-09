import os
import gc
import json
import time
import logging
import asyncio
import subprocess
import requests
import numpy as np
from typing import List, Optional, Union, Dict, Any
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("engine-control")

app = FastAPI(title="MLLM Engine Control")
security = HTTPBearer()

# Default configuration from environment variables
DEFAULT_CONFIG = {
    "api_key": os.environ.get("ENGINE_API_KEY"),
    "port": int(os.environ.get("ENGINE_PORT", 4474)),
    "model_root": os.environ.get("MLX_MODEL_ROOT", "/tmp/mlx_models")
}

class EngineManager:
    def __init__(self):
        self.config = DEFAULT_CONFIG.copy()
        self.status = "idle"
        self.current_model = None
        
        if not self.config["api_key"]:
            logger.warning("ENGINE_API_KEY is not set. API calls requiring authentication will fail.")

    def unload_all(self):
        """Graceful shutdown followed by forceful termination of mlx_lm servers."""
        logger.info("Initiating model unload and server shutdown...")
        # Graceful attempt
        subprocess.run(["pkill", "-f", "mlx_lm.server"], check=False)
        time.sleep(2)
        # Forceful cleanup
        subprocess.run(["pkill", "-9", "-f", "mlx_lm.server"], check=False)
        
        self.current_model = None
        self.status = "idle"
        gc.collect()
        # Note: mx.metal.clear_cache() would require mlx import
        try:
            import mlx.core as mx
            mx.metal.clear_cache()
        except ImportError:
            pass

manager = EngineManager()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not manager.config["api_key"]:
         raise HTTPException(status_code=500, detail="ENGINE_API_KEY not configured on server.")
    if credentials.credentials != manager.config["api_key"]:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return credentials.credentials

@app.get("/status")
async def get_status(token: str = Depends(verify_token)):
    return {
        "status": manager.status,
        "current_model": manager.current_model,
        "api_key_configured": manager.config["api_key"] is not None
    }

@app.post("/unload_all")
async def unload_all_endpoint(token: str = Depends(verify_token)):
    manager.unload_all()
    return {"status": "success", "message": "All models unloaded and servers stopped."}

@app.post("/load_model")
async def load_model(request: Dict[str, str], token: str = Depends(verify_token)):
    model_name = request.get("model")
    if not model_name:
        raise HTTPException(status_code=400, detail="Model name is required.")
    
    manager.status = "loading"
    # In a real implementation, this would trigger a subprocess to start the server
    logger.info(f"Loading model: {model_name}")
    manager.current_model = model_name
    manager.status = "ready"
    return {"status": "success", "model": model_name}

if __name__ == "__main__":
    import uvicorn
    if not manager.config["api_key"]:
        logger.error("CRITICAL: ENGINE_API_KEY environment variable is missing.")
    
    uvicorn.run(app, host="0.0.0.0", port=manager.config["port"])
