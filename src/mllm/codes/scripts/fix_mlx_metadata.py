import mlx.core as mx
from safetensors import safe_open

def fix_metadata(file_path):
    print(f"Fixing: {file_path}")
    try:
        # Load the tensors using MLX
        with safe_open(file_path, framework="mlx") as f:
            tensors = {key: f.get_tensor(key) for key in f.keys()}
            metadata = f.metadata() or {}
            
        print(f"Current metadata: {metadata}")
        metadata["format"] = "mlx"
        
        # Save back replacing the original file
        mx.save_safetensors(file_path, tensors, metadata)
        print(f"Successfully updated metadata for {file_path}")
    except Exception as e:
        print(f"Failed to fix {file_path}: {e}")

if __name__ == "__main__":
    file_path = "~/.lmstudio/models/mlx_models_alias/ltx2-phr00t-nsfw-v62-mlx-universal/diffusion_pytorch_model.safetensors"
    fix_metadata(file_path)
