import os
import time
import subprocess
import requests
import sys
import json
from pathlib import Path

# --- Portable Path Resolution ---
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent.parent.parent # Resolve to repo root
LOG_DIR = REPO_DIR / "logs"
MONITOR_LOG = LOG_DIR / "monitor.txt"
PID_FILE = LOG_DIR / "monitor.pid"
HEARTBEAT_FILE = LOG_DIR / "heartbeat.txt"
RESTART_LOG = LOG_DIR / "pipeline_restart.log"
RUN_CONTEXT_FILE = LOG_DIR / "run_context.json"

def log_to_monitor(message: str, is_error: bool = False):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    prefix = "❌ ERROR" if is_error else "ℹ️ INFO"
    formatted_msg = f'[{timestamp}] {prefix}: {message}'
    print(formatted_msg)
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        with open(MONITOR_LOG, 'a') as f:
            f.write(formatted_msg + '\n')
    except: pass

def get_run_context():
    """Retrieve the arguments used for the last pipeline run."""
    if RUN_CONTEXT_FILE.exists():
        try:
            with open(RUN_CONTEXT_FILE, "r") as f:
                return json.load(f)
        except: return None
    return None

def is_pipeline_running():
    try:
        # Check for the pipeline script in process list
        output = subprocess.check_output(["pgrep", "-f", "mllm-pipeline.py"], stderr=subprocess.DEVNULL)
        return bool(output.strip())
    except: return False

def ensure_single_instance():
    """Check pidfile to ensure only one monitor runs."""
    if PID_FILE.exists():
        try:
            with open(PID_FILE, "r") as f:
                old_pid = int(f.read().strip())
            # Check if process exists
            os.kill(old_pid, 0)
            print(f"Monitor already running (PID {old_pid}). Exiting.")
            sys.exit(0)
        except (ProcessLookupError, ValueError):
            pass # Stale pidfile
            
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

if __name__ == "__main__":
    ensure_single_instance()
    log_to_monitor("Watchdog active. Monitoring MLLM Pipeline + Heartbeat...")
    
    while True:
        pipeline_alive = is_pipeline_running()
        
        # --- HEARTBEAT CHECK ---
        stalled = False
        if HEARTBEAT_FILE.exists():
            try:
                with open(HEARTBEAT_FILE, "r") as f:
                    last_hb = float(f.read().strip())
                diff = time.time() - last_hb
                if diff > 600:
                    log_to_monitor(f"⚠️ PIPELINE STALLED (Last HB: {int(diff)}s ago).")
                    stalled = True
            except: pass

        if not pipeline_alive or stalled:
            context = get_run_context()
            if not context:
                log_to_monitor("⚠️ Pipeline not running and no run context found. Waiting for manual start.")
            else:
                log_to_monitor(f"⚠️ RECOVERING PIPELINE for model: {context.get('model_id')}...")
                # Cleanup
                subprocess.run(["pkill", "-f", "mllm-pipeline.py"], stderr=subprocess.DEVNULL)
                time.sleep(2)
                
                # Restart with original arguments
                args = context.get("args", [])
                cmd = [sys.executable, str(REPO_DIR / "mllm-pipeline.py")] + args
                
                try:
                    with open(RESTART_LOG, "a") as log_file:
                        log_file.write(f"\n--- RESTART AT {time.ctime()} ---\n")
                        subprocess.Popen(cmd, stdout=log_file, stderr=log_file, start_new_session=True)
                    time.sleep(10)
                    if is_pipeline_running():
                        log_to_monitor("✅ PIPELINE RESTARTED SUCCESSFULY.")
                        # Update heartbeat to prevent immediate re-trigger
                        with open(HEARTBEAT_FILE, "w") as f: f.write(str(time.time()))
                    else:
                        log_to_monitor("❌ RESTART FAILED.")
                except Exception as e:
                    log_to_monitor(f"❌ RECOVERY ERROR: {e}", is_error=True)
        
        time.sleep(60) # Check every minute
