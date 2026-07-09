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
REASONING_AGENT_URL = 'http://127.0.0.1:4474/v1/chat/completions'
INPUT_LIMIT_TOKENS = 64000
TIMEOUT_SEC = 3600

# --- Dynamic Path Resolution ---
# Users should set these environment variables or use relative defaults
REPO_DIR = Path(os.environ.get("MLLM_REPO_PATH", "./mllm"))
INPUT_DIR = Path(os.environ.get("MLLM_INPUT_DIR", "./inputs"))
OUTPUT_DIR = Path(os.environ.get("MLLM_OUTPUT_DIR", "./outputs"))
LOG_DIR = Path(os.environ.get("MLLM_LOG_DIR", "./logs"))
LOG_FILE = LOG_DIR / "monitor.txt"
MODEL_MANAGER = os.environ.get("MODEL_MANAGER_SCRIPT", "./scripts/model_manager.sh")

def log(msg):
    timestamp = time.ctime()
    line = f'[{timestamp}] {msg}'
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a') as f: f.write(line + '\n')

def run_manager(action, model_name=''):
    cmd = ['bash', MODEL_MANAGER, action]
    if model_name: cmd.append(model_name)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        return '✅' in res.stdout
    except Exception as e:
        log(f"❌ Manager Error: {e}")
        return False

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
                kv_pairs = re.findall(r'"(.*?)":\s*([\d\.\-]+|null|"np.nan")', raw_dict)
                for k, v in kv_pairs:
                    d[k] = None if v in ["null", "np.nan"] else float(v)
                return d
        return None

    lo = get_dict("lo_evaluations")
    go = get_dict("go_evaluations")
    
    reasoning_match = re.search(r'reasoning_log_text\s*=\s*"""(.*?)"""', text, re.DOTALL)
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""
    
    first_author_match = re.search(r'first_author\s*=\s*"(.*?)"', text)
    year_match = re.search(r'publication_year\s*=\s*"(.*?)"', text)
    
    if lo or go:
        return {
            'lo_evaluations': lo,
            'go_evaluations': go,
            'first_author': first_author_match.group(1) if first_author_match else "Unknown",
            'publication_year': year_match.group(1) if year_match else "Unknown",
            'study_type': "Empirical",
            'agent_name': "Mixtral-8x22B",
            'reasoning_log_text': reasoning
        }
    return None

def query_agent(prompt):
    payload = {
        'model': 'default_model', 
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 16384,
        'temperature': 0.1,
    }
    for attempt in range(5):
        try:
            response = requests.post(REASONING_AGENT_URL, json=payload, timeout=TIMEOUT_SEC)
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content']
            if content and len(content.strip()) > 100:
                return content
            log(f"  ⚠️ Response too short. Retrying {attempt+1}...")
        except Exception as e:
            log(f"  ⚠️ Query failed: {e}. Retrying...")
            time.sleep(10)
    return None

def build_prompt(study_text, visual_text, full_glossary_definitions, glossary_keys_list, model_name):
    role = """<role>
Assume that as a scientist, your task is to evaluate Predictive Coding mechanisms in Neuroscience studies. 
Your task is to carefully analyze the provided study_text AND the visual_descriptions of figures to quantify 
specific neurophysiological factors based on the provided glossary_definitions.
</role>"""

    logic = f"""<definitions>
1. **Contexts**:
   - **LO (Local Oddball)**: Short-term sensory deviance.
   - **GO (Global Oddball)**: Long-term/Sequence deviance.

2. **Scoring Scale (-1.0 to +1.0)**:
   - +1.0: Strong support | 0.0: Neutral | -1.0: Strong rejection | np.nan: Not mentioned.

3. **Glossary Definitions**:
{full_glossary_definitions}
</definitions>"""

    task = f"""<task>
Analyze the study below and output the required Python variables.

**Study Text**:
{study_text}

**Visual Descriptions of Figures**:
{visual_text}

Glossary Keys to Score:
{glossary_keys_list}

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

def run_pipeline(subject='CCC', model='Mixtral-8x22B-Instruct-v0.1-4bit'):
    log(f'🚀 Starting CCC Pipeline (Subject: {subject}, Model: {model})')
    
    # Glossary
    gloss_subj = 'HPC'
    gloss_path = REPO_DIR / 'core' / 'glossary' / gloss_subj / 'hpc-36-reference.md'
    if not gloss_path.exists():
        log(f"❌ Glossary not found at {gloss_path}")
        return
        
    with open(gloss_path, 'r') as f: glossary_md = f.read()

    # Papers
    papers = ["Feldman2015ccc", "Keller2018ccc", "LeeKopell2013ccc", "Sterzer2024ccc", "Thomas2024ccc"]
    
    # Model Loading
    if not run_manager('load', model):
        log(f"❌ Failed to load {model}")
        return
    time.sleep(30)

    for paper_name in papers:
        log(f"📖 Processing Paper: {paper_name}")
        
        text_path = OUTPUT_DIR / 'score_structures' / f"{paper_name}_text.md"
        visual_path = OUTPUT_DIR / 'score_structures' / f"{paper_name}_visuals.md"
        
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
        
        raw_output = query_agent(prompt)
        parsed = extract_python_vars(raw_output)
        
        if parsed:
            out_dir = OUTPUT_DIR / 'jsons'
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{paper_name}_mllm.json"
            
            with open(out_path, 'w') as f:
                json.dump(parsed, f, indent=4)

            log(f"✅ Success! saved to {out_path}")
        else:
            log(f"❌ Failed to parse response for {paper_name}")

    run_manager('unload')

if __name__ == "__main__":
    run_pipeline()
