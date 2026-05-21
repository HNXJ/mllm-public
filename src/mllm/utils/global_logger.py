import os
import glob
import json
import time
from pathlib import Path

LOG_DIR = Path(os.environ.get("MLLM_LOG_DIR", "./logs"))
OUTPUT_FILE = LOG_DIR / "global_log.jsonl"
CHAR_LIMIT = 20000

def generate_global_log():
    log_files = glob.glob(str(LOG_DIR / "*.log")) + glob.glob(str(LOG_DIR / "*.txt"))
    # Filter out the global log itself
    log_files = [f for f in log_files if "global_log.jsonl" not in f]
    
    # Sort by modification time to get the most recent first
    log_files.sort(key=os.path.getmtime, reverse=True)
    
    global_entries = []
    
    for log_path in log_files:
        try:
            file_size = os.path.getsize(log_path)
            with open(log_path, "r", errors="ignore") as f:
                if file_size > CHAR_LIMIT:
                    f.seek(file_size - CHAR_LIMIT)
                content = f.read()
            
            entry = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(log_path))),
                "source": os.path.basename(log_path),
                "content": content
            }
            global_entries.append(entry)
        except Exception as e:
            print(f"Error reading {log_path}: {e}")

    with open(OUTPUT_FILE, "w") as f:
        for entry in global_entries:
            f.write(json.dumps(entry) + "\n")
    
    print(f"✅ Global log generated with {len(global_entries)} sources.")

if __name__ == "__main__":
    generate_global_log()
