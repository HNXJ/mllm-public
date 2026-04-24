import os
import sys
from pathlib import Path
import subprocess

# --- Portable Path Resolution ---
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent.parent
MLLM_ROOT = REPO_DIR.parent if REPO_DIR.name == "mllm" else REPO_DIR

# --- Configuration ---
VL_MODEL = os.getenv("VL_MODEL", str(MLLM_ROOT / "mlx_models" / "Qwen2.5-VL-7B-Instruct-8bit"))
PAPERS_BASE = MLLM_ROOT / "inputs" / "HPC"
VISUAL_DIR = MLLM_ROOT / "outputs" / "visual_descriptions"
VISUAL_DIR.mkdir(parents=True, exist_ok=True)

def describe_pdf_visuals(pdf_path):
    paper_name = Path(pdf_path).stem
    print(f"🎨 Analyzing Visuals for {paper_name}...")
    
    prompt = "Scan this neuroscience paper and identify all figures. For each figure, provide a detailed description of the data, axes, and how it supports or rejects Predictive Coding (Local/Global Oddball) hypotheses."
    
    cmd = [
        "python3", "-m", "mlx_lm.generate",
        "--model", VL_MODEL,
        "--prompt", prompt,
        "--max-tokens", "2048",
        "--temp", "0.1"
    ]
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        return res.stdout.strip()
    except Exception as e:
        print(f"  ❌ Error analyzing {paper_name}: {e}")
        return ""

def main():
    pdfs = sorted(list(PAPERS_BASE.glob('*.pdf')))
    for pdf in pdfs:
        paper_name = pdf.stem
        out_path = VISUAL_DIR / f"{paper_name}_visuals.md"
        if out_path.exists(): continue
            
        desc = describe_pdf_visuals(str(pdf))
        if desc:
            with open(out_path, 'w') as f: f.write(desc)
            print(f"  ✅ Saved to {out_path}")

if __name__ == "__main__":
    main()
