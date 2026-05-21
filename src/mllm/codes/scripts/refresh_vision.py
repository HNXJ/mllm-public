import os
import sys
import json
import time
import requests
import subprocess
from pathlib import Path
import re
import fitz  # PyMuPDF
import base64

# --- Constants & Configuration ---
# Users should set MLLM_WORKSPACE_ROOT or use default relative path
BASE_DIR = Path(os.environ.get("MLLM_WORKSPACE_ROOT", "./mllm_workspace"))
SCRIPTS_DIR = BASE_DIR / "scripts"
GLOSSARY_DIR = BASE_DIR / "glossary"
PAPERS_DIR = BASE_DIR / "papers"
MD_DIR = BASE_DIR / "markdowns"
UNIFIED_INPUT_DIR = BASE_DIR / "Unified_article_input"
RESULTS_DIR = BASE_DIR / "results"
THINKING_LOGS = BASE_DIR / "thinking_logs"
REASONING_LOGS = BASE_DIR / "reasoning_logs"

REASONING_AGENT_URL = f"http://127.0.0.1:4474/v1/chat/completions"
VISION_MODEL_URL = f"http://127.0.0.1:4475/v1/chat/completions" # Isolated port
TIMEOUT_SEC = 3600 

MODELS_TO_RUN = ["gemma-3-27b-it-8bit", "Qwen3.5-40B-Claude-4.5-Opus", "Olmo-3-32B-Think", "phi-4-8bit", "Mistral-Nemo-12B-Thinking"]
VISION_MODEL = "Qwen2.5-VL-7B-Instruct-8bit"
SUBJECTS = ["HPC", "SCZ", "ADB"]

SUBJECT_CONFIG = {
    "HPC": {"glossary": GLOSSARY_DIR / "HPC" / "hpc-36-reference.md", "folder": PAPERS_DIR / "hpc_papers"},
    "SCZ": {"glossary": GLOSSARY_DIR / "SCZ" / "scz-51-reference.md", "folder": PAPERS_DIR / "scz_papers"},
    "ADB": {"glossary": GLOSSARY_DIR / "ADB" / "adb-60-reference.md", "folder": PAPERS_DIR / "adb_papers"}
}

# --- Core Functions ---

def run_manager(action, model_name="", port=None):
    # Model manager script path: users should set MODEL_MANAGER_SCRIPT env var
    manager_script = os.environ.get("MODEL_MANAGER_SCRIPT")
    if manager_script and os.path.exists(manager_script):
        cmd = ["bash", manager_script, action]
        if model_name: cmd.append(model_name)
        if port: cmd.append(str(port))
        res = subprocess.run(cmd, capture_output=True, text=True)
        return "✅" in res.stdout
    return True

def query_vlm(prompt, image_path):
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode('utf-8')
    payload = {
        "model": "default_vlm",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "temperature": 0.1
    }
    try:
        response = requests.post(VISION_MODEL_URL, json=payload, timeout=600)
        return response.json()['choices'][0]['message']['content']
    except: return None

def vision_loop(pdf_path):
    paper_name = pdf_path.stem
    vision_md_path = MD_DIR / f"{paper_name}_visuals.md"
    
    # RE-RUN IF FILE IS TOO SMALL (Likely empty header)
    if vision_md_path.exists() and vision_md_path.stat().st_size > 200:
        return True

    print(f"  👁️ Running Robust Vision Loop for {pdf_path.name}...")
    content = "# Visual Data Extraction (Figures & Tables)\n\n"
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            page_text = page.get_text()
            # ROBUST DETECTION: Check for image objects OR "Figure/Table" captions
            has_visuals = len(page.get_images()) > 0 or re.search(r'(Figure|Table|Fig\.)\s+\d+', page_text, re.I)
            
            if has_visuals:
                print(f"    📸 Processing Page {page.number+1}...")
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_path = Path(f"/tmp/p{page.number}.jpg")
                pix.save(str(img_path))
                desc = query_vlm("Describe any figures, charts, or tables on this page in extreme detail for a neuroscience study. Provide markdown tables for quantitative data.", str(img_path))
                if desc:
                    content += f"## Page {page.number+1}\n{desc}\n\n"
                if img_path.exists(): os.remove(img_path)
        doc.close()
        with open(vision_md_path, 'w') as f: f.write(content)
        return True
    except Exception as e:
        print(f"    ⚠️ Vision Error: {e}")
        return False

def organize_unified_input(paper_name):
    text_path = MD_DIR / f"{paper_name}_text.md"
    visual_path = MD_DIR / f"{paper_name}_visuals.md"
    unified_path = UNIFIED_INPUT_DIR / f"{paper_name}_unified.md"
    os.makedirs(UNIFIED_INPUT_DIR, exist_ok=True)
    content = ""
    if text_path.exists():
        with open(text_path, 'r') as f: content += "# MAIN TEXT\n" + f.read()
    if visual_path.exists():
        with open(visual_path, 'r') as f: content += "\n\n# FIGURE & TABLE DESCRIPTIONS\n" + f.read()
    with open(unified_path, 'w') as f: f.write(content)
    return content

def run_pipeline():
    for d in [MD_DIR, UNIFIED_INPUT_DIR, RESULTS_DIR]: os.makedirs(d, exist_ok=True)

    # --- PHASE 1: Robust Vision Extraction ---
    print("\n🚀 PHASE 1: Robust Vision Extraction (Port 4475)")
    run_manager("unload")
    if run_manager("load_vlm", VISION_MODEL, port=4475):
        time.sleep(30)
        for sub in SUBJECTS:
            for pdf in SUBJECT_CONFIG[sub]['folder'].glob("*.pdf"):
                vision_loop(pdf)
        run_manager("unload")

    # --- PHASE 2: Organization Check ---
    print("\n🚀 PHASE 2: Refreshing Unified Inputs")
    for sub in SUBJECTS:
        for pdf in SUBJECT_CONFIG[sub]['folder'].glob("*.pdf"):
            organize_unified_input(pdf.stem)

    print("\n✅ Vision & Organization Refresh Complete!")

if __name__ == "__main__":
    run_pipeline()
