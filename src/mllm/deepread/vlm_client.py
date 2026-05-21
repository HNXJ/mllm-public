import base64
import os
import time
from openai import OpenAI
from mllm.deepread.prompts import get_vlm_prompt

class VLMClient:
    """Sends figure crops to a local VLM for description."""

    def __init__(self, base_url: str = "http://localhost:1234/v1", api_key: str = "lm-studio", model: str = "qwen3.5-vl-4b", engine: str = "lms", strict: bool = False):
        if strict and not model.lower().startswith("qwen3.5-vl"):
            raise ValueError(f"Strict mode enabled: Model {model} does not start with qwen3.5-vl")
        
        self.engine = engine.lower()
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        
        if self.engine == "lms":
            self.client = OpenAI(base_url=base_url, api_key=api_key)
        elif self.engine == "vmlx":
            self._vmlx_model = None # Lazy load
            self._vmlx_processor = None
            self._mlx_vlm = None

    def describe_figure(self, image_path: str, caption_text: str = None, max_retries: int = 3) -> str:
        """Encodes an image and requests a description from the VLM."""
        if self.engine == "vmlx":
            return self._describe_vmlx(image_path, caption_text)
        
        return self._describe_lms(image_path, caption_text, max_retries)

    def _describe_vmlx(self, image_path: str, caption_text: str = None) -> str:
        """Native vMLX inference."""
        if self._vmlx_model is None:
            print(f"🚀 Loading VLM via mlx_vlm: {self.model}")
            try:
                import mlx_vlm
                # Resolve model path: users should set MLX_MODEL_ROOT env var or use model ID directly
                mlx_model_root = os.environ.get("MLX_MODEL_ROOT", "./mlx_models")
                model_path = f"{mlx_model_root}/{self.model}"
                if not os.path.exists(model_path):
                    model_path = self.model # Try direct model ID if local path doesn't exist
                
                self._vmlx_model, self._vmlx_processor = mlx_vlm.load(model_path)
                self._mlx_vlm = mlx_vlm
            except Exception as e:
                print(f"❌ Failed to load vMLX model {self.model}: {e}")
                raise e
        
        prompt = get_vlm_prompt(caption_text)
        return self._mlx_vlm.generate(self._vmlx_model, self._vmlx_processor, image_path, prompt, max_tokens=4096)

    def _describe_lms(self, image_path: str, caption_text: str, max_retries: int) -> str:
        """OpenAI-compatible inference via LM Studio."""
        base64_image = self._encode_image(image_path)
        prompt = get_vlm_prompt(caption_text)

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{base64_image}"
                                    },
                                },
                            ],
                        }
                    ],
                    max_tokens=4096,
                    timeout=300 # 5 minute timeout per request
                )
                return response.choices[0].message.content
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"      [yellow]VLM attempt {attempt+1} failed: {e}. Retrying in 60s...[/yellow]")
                    time.sleep(60)
                else:
                    raise e

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
