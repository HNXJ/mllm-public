import os
import json
from pathlib import Path

PROFILES_DIR = Path("computational/mllm_local/mllm/src/mllm/config/profiles/")

def update_profiles():
    for p in PROFILES_DIR.glob("*.json"):
        try:
            with open(p, "r") as f:
                data = json.load(f)
            
            # Update fields
            data["engine_type"] = "mlx"
            data["api_key"] = "mlx-server"
            if "api_url" in data and "1234" in data["api_url"]:
                data["api_url"] = data["api_url"].replace("1234", "4474")
            
            with open(p, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Updated {p.name}")
        except Exception as e:
            print(f"Failed to update {p.name}: {e}")

if __name__ == "__main__":
    update_profiles()
