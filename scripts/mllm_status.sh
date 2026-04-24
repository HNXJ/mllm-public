#!/bin/bash

REMOTE_USER="HN"
REMOTE_HOST="100.69.184.42"
REMOTE_PASS="apple"
SSH_CMD="sshpass -p '$REMOTE_PASS' ssh $REMOTE_USER@$REMOTE_HOST"

echo "🔍 MLLM PIPELINE STATUS SNAPSHOT"
echo "=========================================================="

# 1. Check Local Trigger
if pgrep -f overnight_queue.sh > /dev/null; then
    echo "✅ Local Orchestrator: ACTIVE (overnight_queue.sh)"
else
    echo "❌ Local Orchestrator: INACTIVE"
fi

# 2. Check Remote Engine (Port 4474)
$SSH_CMD "lsof -iTCP:4474 -sTCP:LISTEN > /dev/null"
if [ $? -eq 0 ]; then
    echo "✅ Remote Engine:      ACTIVE (Port 4474)"
else
    echo "❌ Remote Engine:      DOWN"
fi

# 3. Check Remote Monitor (Port 8081)
$SSH_CMD "lsof -iTCP:8081 -sTCP:LISTEN > /dev/null"
if [ $? -eq 0 ]; then
    echo "✅ Remote Monitor:     ACTIVE (Port 8081)"
else
    echo "❌ Remote Monitor:     DOWN"
fi

# 4. Check Current Model
current_model=$($SSH_CMD "curl -s http://localhost:4474/status" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('current_model', 'None'))")
echo "🤖 Active Model:       $current_model"

# 5. Progress Audit
done_count=$($SSH_CMD "find /Users/HN/MLLM/outputs/HPC -name '*_eval.json' | wc -l" | tr -d ' ')
echo "📊 Total Evaluations:  $done_count / 465"

# 6. Last Activity
last_log=$($SSH_CMD "tail -n 1 /Users/HN/MLLM/logs/pipeline.log")
echo "🕒 Last Log Entry:     $last_log"
echo "=========================================================="
