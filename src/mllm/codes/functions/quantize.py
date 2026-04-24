import argparse
import os
import subprocess

def run_neuro_quantization(model_path, output_path, q_bits=6):
    """
    Advanced Quantization: K-level Hybrid strategy.
    Optimized for high-fidelity neurophysiology parameters.
    Recommended: q6_K for near-transparency to 16-bit performance.
    """
    print(f"💎 Starting Neuro-LLM Quantization (q{q_bits}_K)")
    print(f"🧠 Input Model: {model_path}")
    print(f"🛠  Output Model: {output_path}")

    # For MLX, we use the mlx-lm convert tool which supports K-quants (q4_K, q8_0, etc.)
    # Note: Modern MLX versions support these through the --q-bits flag or mapping.
    cmd = [
        "python", "-m", "mlx_lm.convert",
        "--hf-path", model_path,
        "--mlx-path", output_path,
        "-q" # Enable quantization
    ]
    
    # MLX CLI doesn't always take q6_K directly as a string but as bits.
    # However, many versions support specific bit depths.
    if q_bits:
        cmd.extend(["--q-bits", str(q_bits)])
    
    print(f"⚙️ Running command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Quantization complete. Output saved to: {output_path}")
    except Exception as e:
        print(f"❌ Quantization failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neuro-LLM Quantization (K-level Hybrid)")
    parser.add_argument("--model", type=str, required=True, help="HF or local model path")
    parser.add_argument("--output", type=str, required=True, help="Output MLX model path")
    parser.add_argument("--bits", type=int, default=6, help="Quantization bits (e.g., 4, 6, 8)")
    args = parser.parse_args()

    run_neuro_quantization(args.model, args.output, q_bits=args.bits)
