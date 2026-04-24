import os
import json
import csv
from pathlib import Path

# --- Portable Path Resolution ---
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent.parent
MLLM_ROOT = REPO_DIR.parent if REPO_DIR.name == "mllm" else REPO_DIR

JSON_DIR = MLLM_ROOT / "outputs" / "jsons"
CSV_OUTPUT = MLLM_ROOT / "outputs" / "hpc_evaluations.csv"

def parse_results():
    if not JSON_DIR.exists():
        print(f"❌ JSON directory {JSON_DIR} does not exist.")
        return
    json_files = list(JSON_DIR.glob('*.json'))
    if not json_files:
        print("ℹ️ No JSON files found.")
        return
    factors = set()
    rows = []
    for jf in sorted(json_files):
        try:
            with open(jf, 'r') as f:
                data = json.load(f)
            paper_name = jf.stem
            agent = data.get('agent_name', 'Unknown')
            meta = data.get('metadata', {})
            author = meta.get('first_author', 'Unknown')
            year = meta.get('year', 'Unknown')
            study = f'{author} ({year})'
            
            scores = data.get('scores', {})
            for context in ['lo', 'go']:
                evals = scores.get(context, {})
                if not evals: continue
                row = {'Study': study, 'Paper': paper_name, 'Agent': agent, 'Context': context.upper()}
                for factor, score in evals.items():
                    factors.add(factor)
                    row[factor] = score
                rows.append(row)
        except Exception as e:
            print(f'Error parsing {jf.name}: {e}')
            
    if not rows:
        print("ℹ️ No valid rows extracted.")
        return
        
    fieldnames = ['Study', 'Paper', 'Agent', 'Context'] + sorted(list(factors))
    CSV_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_OUTPUT, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f'📊 CSV results saved to {CSV_OUTPUT}')

if __name__ == '__main__':
    parse_results()
