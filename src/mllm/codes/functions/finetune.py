import os
import argparse
import time
import subprocess
import sys

try:
    from mlx_lm import lora
except ImportError:
    print("❌ mlx_lm not found. Please install: pip install mlx-lm")

def run_neuro_finetune(model_path, data_dir, adapter_path="adapters", iters=500, batch_size=4, lr=1e-5, type="dora"):
    """
    Triggers the MLX LoRA/DoRA fine-tuning pipeline using the CLI.
    Optimized for high-fidelity neurophysiology data.
    """
    print(f"🚀 Starting Neuro-LLM Fine-Tuning ({type.upper()} CLI)")
    print(f"🧠 Base Model: {model_path}")
    print(f"📂 Training Data: {data_dir}")
    print(f"🛠  Adapter Path: {adapter_path}")
    print(f"⚙️ Config: Type={type}, Iters={iters}")

    cmd = [
        "python3", "-m", "mlx_lm.lora",
        "--model", model_path,
        "--train",
        "--data", data_dir,
        "--iters", str(iters),
        "--batch-size", str(batch_size),
        "--learning-rate", str(lr),
        "--adapter-path", adapter_path,
        "--fine-tune-type", type,
        "--num-layers", "16"
    ]

    print(f"⚙️ Running command: {' '.join(cmd)}")
    
    start_time = time.time()
    try:
        subprocess.run(cmd, check=True)
        elapsed = time.time() - start_time
        print(f"✅ Fine-Tuning complete in {elapsed/60:.2f} minutes.")
    except Exception as e:
        print(f"❌ Fine-Tuning failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neuro-LLM Fine-Tuning (DoRA)")
    parser.add_argument("--model", type=str, required=True, help="Base model path")
    parser.add_argument("--data", type=str, default="./data", help="Directory for JSONL files")
    parser.add_argument("--adapter", type=str, default="adapters", help="Output adapter path")
    parser.add_argument("--iters", type=int, default=500, help="Number of iterations")
    parser.add_argument("--batch", type=int, default=4, help="Batch size")
    parser.add_argument("--lr", type=float, default=1e-5, help="Learning rate")
    parser.add_argument("--type", type=str, choices=["lora", "dora"], default="dora", help="Fine-tuning type (lora or dora)")
    args = parser.parse_args()

    run_neuro_finetune(args.model, args.data, adapter_path=args.adapter, iters=args.iters, batch_size=args.batch, lr=args.lr, type=args.type)
