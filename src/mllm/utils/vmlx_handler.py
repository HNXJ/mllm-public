import sys
import subprocess
import importlib.util

def detect_vmlx():
    """Checks if vMLX and its core dependencies are installed."""
    print("[gemmy-cli] Scanning environment for vMLX dependencies...")
    packages = ['vMLX', 'mlx_lm', 'mlx_vlm']
    missing = []
    for pkg in packages:
        # pip show is more reliable for checking vMLX since it might not be directly importable as 'vMLX'
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", pkg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            missing.append(pkg)
    if not missing:
        print("[gemmy-cli] SUCCESS: vMLX environment is fully primed.")
        return True
    else:
        print(f"[gemmy-cli] MISSING: Required packages not found: {missing}")
        return False

def install_vmlx():
    """Forces installation of vMLX and required MLX wrappers."""
    print("[gemmy-cli] Initiating autonomous installation of vMLX and MLX frameworks...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "vMLX", "mlx-lm", "mlx-vlm"
        ])
        print("[gemmy-cli] SUCCESS: Installation complete.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[gemmy-cli] CRITICAL ERROR: Failed to install vMLX. {e}")
        return False

def run_vmlx_terminal(model_path, prompt, max_tokens=500):
    """Executes the model natively using the standard MLX terminal command."""
    print(f"[gemmy-cli] Routing execution to native MLX engine for model: {model_path}")
    # Standard MLX generation command. vMLX hooks into this automatically.
    command = [
        "mlx_lm.generate", "--model", model_path, "--prompt", prompt, "--max-tokens", str(max_tokens)
    ]
    try:
        # Stream the output directly to the terminal as it generates
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[gemmy-cli] EXECUTION FAILED: Ensure the model path is correct and vMLX supports the architecture. {e}")

# --- Agent Execution Logic ---
if __name__ == "__main__":
    # 1. Detect if not primed
    if not detect_vmlx():
        # 2. Install if missing
        install_success = install_vmlx()
        if not install_success:
            sys.exit(1)
    # 3. Ready for execution (Example usage)
    # run_vmlx_terminal("path/to/your/gemma4-mxfp8-folder", "Explain predictive coding in spiking networks.")
