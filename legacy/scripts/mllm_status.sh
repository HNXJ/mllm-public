#!/bin/bash

# Status Check Configuration
MLLM_REMOTE_USER="${MLLM_REMOTE_USER:-user}"
MLLM_REMOTE_HOST="${MLLM_REMOTE_HOST:-localhost}"
MLLM_OUTPUT_PATH="${MLLM_OUTPUT_PATH:-./outputs/HPC}"
MLLM_LOG_PATH="${MLLM_LOG_PATH:-./logs}"
ENGINE_PORT="${ENGINE_PORT:-4474}"
MONITOR_PORT="${MONITOR_PORT:-8081}"
ENGINE_URL="${ENGINE_URL:-http://localhost:$ENGINE_PORT}"

SSH_CMD="ssh $MLLM_REMOTE_USER@$MLLM_REMOTE_HOST"

echo "🔍 MLLM PIPELINE STATUS SNAPSHOT"
echo "=========================================================="

# 1. Check Local Trigger
if pgrep -f overnight_queue.sh > /dev/null; then
    echo "✅ Local Orchestrator: ACTIVE (overnight_queue.sh)"
else
    echo "❌ Local Orchestrator: INACTIVE"
fi

# 2. Check Remote Engine (configurable port)
$SSH_CMD "lsof -iTCP:$ENGINE_PORT -sTCP:LISTEN > /dev/null 2>&1"
if [ $? -eq 0 ]; then
    echo "✅ Remote Engine:      ACTIVE (Port $ENGINE_PORT)"
else
    echo "❌ Remote Engine:      DOWN"
fi

# 3. Check Remote Monitor (configurable port)
$SSH_CMD "lsof -iTCP:$MONITOR_PORT -sTCP:LISTEN > /dev/null 2>&1"
if [ $? -eq 0 ]; then
    echo "✅ Remote Monitor:     ACTIVE (Port $MONITOR_PORT)"
else
    echo "❌ Remote Monitor:     DOWN"
fi

# 4. Check Current Model (if endpoint available)
current_model=$($SSH_CMD "curl -s $ENGINE_URL/status 2>/dev/null" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('current_model', 'Unknown'))" 2>/dev/null || echo "Unavailable")
echo "🤖 Active Model:       $current_model"

# 5. Progress Audit
done_count=$($SSH_CMD "find $MLLM_OUTPUT_PATH -name '*_eval.json' 2>/dev/null | wc -l" | tr -d ' ')
echo "📊 Evaluation Files:   $done_count"

# 6. Last Activity
last_log=$($SSH_CMD "tail -n 1 $MLLM_LOG_PATH/pipeline.log 2>/dev/null" || echo "No log available")
echo "🕒 Last Log Entry:     $last_log"
echo "=========================================================="
