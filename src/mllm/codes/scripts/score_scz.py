import os
import json
import time
import requests
import numpy as np
from pathlib import Path

# --- Configuration ---
REMOTE_IP = "100.69.184.42"
AGENTS = {
    "Qwen-32B": {"url": f"http://{REMOTE_IP}:4474/v1/chat/completions", "port": 4474},
    "DeepSeek-R1-70B": {"url": f"http://{REMOTE_IP}:4475/v1/chat/completions", "port": 4475},
    "Phi-4": {"url": f"http://{REMOTE_IP}:4476/v1/chat/completions", "port": 4476}
}

GLOSSARY_PATH = Path("./workspace/Repositories/mllm/glossary/scz-51-reference.md")
PAPERS_DIR = Path("./workspace/misc/papers/markdowns")
RESULTS_DIR = Path("./workspace/Repositories/mllm/results/scz_scoring")

def parse_glossary(path):
    """Simple parser for the markdown table glossary."""
    with open(path, 'r') as f:
        content = f.read()
    
    factors = []
    # Regex to find | ID | Name | Def | Tag |
    matches = re.findall(r'\| (\d+) \| (.*?) \| (.*?) \| (.*?) \|', content)
    for m in matches:
        factors.append({
            "id": int(m[0]),
            "name": m[1].strip(),
            "definition": m[2].strip(),
            "tag": m[3].strip()
        })
    return factors

def get_agent_score(agent_name, agent_url, paper_text, factor):
    """Queries a single agent for a score on a specific factor."""
    prompt = f"""
    Analyze the following neuroscience paper text and score it against the biophysical factor provided.
    
    PAPER TEXT:
    {paper_text[:15000]} # Context window limit
    
    FACTOR:
    ID: {factor['id']}
    Name: {factor['name']}
    Definition: {factor['definition']}
    
    TASK:
    1. Score: Provide a numerical score between 0.0 and 1.0.
       - 1.0: Paper provides strong direct evidence for this factor.
       - 0.5: Paper mentions this factor or provides indirect evidence.
       - 0.0: Paper does not mention or contradicts this factor.
    2. Evidence: Quote the most relevant sentence (if any).
    3. Reasoning: 1-sentence explanation of your score.
    
    OUTPUT FORMAT (JSON ONLY):
    {{
        "score": float,
        "evidence": "string",
        "reasoning": "string"
    }}
    """
    
    payload = {
        "model": "default_model",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1, # Low temp for consistency
        "response_format": {"type": "json_object"}
    }
    
    try:
        response = requests.post(agent_url, json=payload, timeout=120)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"    ⚠️ Agent {agent_name} Error: {e}")
        return None

def score_paper(paper_path, factors):
    paper_name = paper_path.stem.replace("_analysis", "")
    print(f"📖 Scoring Paper: {paper_name}")
    
    with open(paper_path, 'r') as f:
        text = f.read()
        
    results = {}
    
    # Pilot: Only score first 5 factors for testing
    for factor in factors[:5]:
        print(f"  🔍 Factor {factor['id']}: {factor['name']}...")
        factor_results = {}
        scores = []
        
        for name, info in AGENTS.items():
            raw_res = get_agent_score(name, info['url'], text, factor)
            if raw_res:
                try:
                    data = json.loads(raw_res)
                    factor_results[name] = data
                    scores.append(data.get('score', 0.0))
                except: pass
        
        if scores:
            consensus = np.mean(scores)
            certainty = 1.0 - np.std(scores)
            results[factor['id']] = {
                "factor": factor['name'],
                "consensus": consensus,
                "certainty": certainty,
                "agents": factor_results
            }
            
    # Save results
    output_path = RESULTS_DIR / f"{paper_name}_scores.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"✅ Saved scores to {output_path}")

if __name__ == "__main__":
    import re
    os.makedirs(RESULTS_DIR, exist_ok=True)
    factors = parse_glossary(GLOSSARY_PATH)
    papers = list(PAPERS_DIR.glob("*.md"))
    
    if not papers:
        print("❌ No analyzed papers found in markdowns/ folder.")
    else:
        # Run on the first paper as a pilot
        score_paper(papers[0], factors)
