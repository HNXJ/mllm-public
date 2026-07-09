import mlx.core as mx
from mlx_lm import load, generate
import argparse

def test_model(model_path, prompt, max_tokens=1000):
    print(f"🚀 Loading model from: {model_path}")
    model, tokenizer = load(model_path)
    
    print(f"🧠 Prompt: {prompt}")
    print("-" * 30)
    
    response = generate(model, tokenizer, prompt=prompt, max_tokens=max_tokens, verbose=True)
    
    print("-" * 30)
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Qwen-Opus-Reasoning model")
    parser.add_argument("--model", type=str, default="./workspace/mlx_models/Qwen3.5-27B-Opus-Reasoning-6bit", help="Path to the MLX model")
    parser.add_argument("--prompt", type=str, default="Explain the biophysical basis of the mismatch negativity (MMN) in the context of hierarchical predictive coding.", help="Test prompt")
    parser.add_argument("--max-tokens", type=int, default=1000, help="Maximum tokens to generate")
    
    args = parser.parse_args()
    test_model(args.model, args.prompt, args.max_tokens)
