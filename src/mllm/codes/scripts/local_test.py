import os
import sys
import json
import time
import requests
import subprocess
from pathlib import Path
import re
import argparse

# --- Configuration ---
ENGINE_URL = 'http://127.0.0.1:4474'
API_KEY = 'hnxj-m3max-key'
REASONING_AGENT_URL = f'{ENGINE_URL}/v1/chat/completions'
INPUT_LIMIT_TOKENS = 64000
TIMEOUT_SEC = 3600

# --- Dynamic Path Resolution (Local) ---
REPO_DIR = Path("./workspace/Warehouse/Repositories/mllm")
INPUT_DIR = Path("./workspace/misc/papers/CorticalCircuitContext/markdowns")
OUTPUT_DIR = Path("./workspace/results/mllm")
LOG_DIR = Path("./workspace/logs")
LOG_FILE = LOG_DIR / "monitor_local.txt"

def log(msg):
    timestamp = time.ctime()
    line = f'[{timestamp}] {msg}'
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a') as f: f.write(line + '\n')

def run_engine_load(model_name):
    log(f"📡 Requesting load for {model_name} via local mlxEngine...")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        res = requests.post(f"{ENGINE_URL}/load_model", json={"model": model_name}, headers=headers, timeout=300)
        if res.status_code == 200:
            log(f"✅ {model_name} loaded successfully.")
            return True
        else:
            log(f"❌ Load failed: {res.text}")
            return False
    except Exception as e:
        log(f"❌ Engine Connection Error: {e}")
        return False

def query_agent(prompt, model):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 4096,
        "stream": False
    }
    try:
        res = requests.post(REASONING_AGENT_URL, json=payload, headers=headers, timeout=TIMEOUT_SEC)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        else:
            log(f"  ⚠️ Query failed: {res.text}")
            return None
    except Exception as e:
        log(f"  ⚠️ Query failed: {e}. Retrying...")
        time.sleep(10)
        return None

def extract_python_vars(text):
    if not text: return None
    def get_dict(var_name):
        match = re.search(fr'{var_name}\s*=\s*({{.*?}})', text, re.DOTALL)
        if match:
            try:
                raw_dict = match.group(1).replace("np.nan", "null")
                raw_dict = re.sub(r',\s*}', '}', raw_dict)
                return json.loads(raw_dict)
            except:
                d = {}
                kv_pairs = re.findall(r'"(.*?)\":\s*([\d\.\-]+|null|"np.nan")', raw_dict)
                for k, v in kv_pairs:
                    d[k] = None if v in ["null", "np.nan"] else float(v)
                return d
        return None

    def get_str(var_name):
        match = re.search(fr'{var_name}\s*=\s*\"(.*?)\"', text, re.DOTALL)
        return match.group(1) if match else "Unknown"

    res = {
        "lo_evaluations": get_dict("lo_evaluations"),
        "go_evaluations": get_dict("go_evaluations"),
        "first_author": get_str("first_author"),
        "publication_year": get_str("publication_year"),
        "study_type": get_str("study_type"),
        "agent_name": get_str("agent_name"),
        "reasoning_log_text": get_str("reasoning_log_text")
    }
    return res if res['lo_evaluations'] else None

def build_prompt(paper_text, visual_text, glossary, glossary_keys, model_name):
    role = "You are a senior neuroscientist and biophysicist."
    logic = "Evaluate the study against the glossary provided. Focus on spectral-laminar motifs and LO/GO contexts."
    task = f"""<task>
Analyze the study below and output the required Python variables.

**Study Text**:
{paper_text}

**Visual Descriptions of Figures**:
{visual_text}

Glossary Keys to Score:
{glossary_keys}

**REQUIRED OUTPUT FORMAT**:
lo_evaluations = {{ "Factor Name": 0.8, ... }}
go_evaluations = {{ "Factor Name": 0.5, ... }}
first_author = "Name"
publication_year = "YYYY"
study_type = "Empirical"
agent_name = "{model_name}"
reasoning_log_text = \"\"\"Your detailed reasoning citing figures and text\"\"\"
</task>"""
    return f"{role}\n{logic}\n{task}"

def run_pipeline(subject='CCC', model='Qwen3.5-9B-8bit'):
    log(f'🚀 Starting Local MLLM Test (Subject: {subject}, Model: {model})')
    
    # Adjust local glossary path
    gloss_subj = 'HPC'
    gloss_path = REPO_DIR / 'glossary' / gloss_subj / 'hpc-36-reference.md'
    if not gloss_path.exists():
        log(f"❌ Glossary not found at {gloss_path}")
        return
        
    with open(gloss_path, 'r') as f: glossary_md = f.read()

    # Just one paper for test
    papers = ["Sterzer2024ccc"]
    
    if not run_engine_load(model):
        log(f"❌ Failed to load {model} via local mlxEngine")
        return

    for paper_name in papers:
        out_path = OUTPUT_DIR / 'jsons' / f"{paper_name}_mllm.json"
        if out_path.exists():
            log(f"⏩ Skipping {paper_name}: Output already exists.")
            #continue

        log(f"📖 Processing Paper: {paper_name}")
        
        # Local paths for CCC papers
        text_path = INPUT_DIR / f"{paper_name}_text.md"
        visual_path = INPUT_DIR / f"{paper_name}_visuals.md"
        
        if not text_path.exists():
            log(f"  ⚠️ Skipping {paper_name}: Text not found at {text_path}")
            continue
            
        with open(text_path, 'r') as f: paper_text = f.read()
        visual_text = ""
        if visual_path.exists():
            with open(visual_path, 'r') as f: visual_text = f.read()
        
        definitions = []
        keys = []
        for line in glossary_md.split('\n'):
            match = re.search(r'\|\s*\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|', line)
            if match:
                f_name = match.group(1).strip()
                f_def = match.group(2).strip()
                if f_name and f_name != "Factor Name":
                    definitions.append(f"{f_name}: {f_def}")
                    keys.append(f_name)
        
        full_glossary = "\n".join(definitions)
        glossary_keys = ", ".join([f'"{k}"' for k in keys])
        
        prompt = build_prompt(paper_text, visual_text, full_glossary, glossary_keys, model)
        log(f"    📡 Querying Unified Context (~{len(prompt)//4} tokens)... ")
        
        raw_output = query_agent(prompt, model)
        parsed = extract_python_vars(raw_output)
        
        if parsed:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, 'w') as f:
                json.dump(parsed, f, indent=4)
            log(f"✅ Success! saved to {out_path}")
        else:
            log(f"❌ Failed to parse response for {paper_name}")

if __name__ == "__main__":
    run_pipeline()
