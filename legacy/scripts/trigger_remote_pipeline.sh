#!/bin/bash

# Remote Execution Configuration (use environment variables or defaults)
MLLM_REMOTE_USER="${MLLM_REMOTE_USER:-user}"
MLLM_REMOTE_HOST="${MLLM_REMOTE_HOST:-localhost}"
MLLM_REMOTE_ROOT="${MLLM_REMOTE_ROOT:-.}"
MLLM_REMOTE_PYTHON="${MLLM_REMOTE_PYTHON:-python}"
MLLM_INPUT_PATH="${MLLM_INPUT_PATH:-./inputs/HPC}"
MLLM_OUTPUT_PATH="${MLLM_OUTPUT_PATH:-./outputs/HPC}"
ENGINE_URL="${ENGINE_URL:-http://localhost:4474}"

# Derive remote paths from remote root
REMOTE_SCRIPT="$MLLM_REMOTE_ROOT/mllm-pipeline.py"
REMOTE_PYTHONPATH="$MLLM_REMOTE_ROOT/src"

SSH_CMD="ssh"

# Function to run pipeline remotely and WAIT for it to finish
run_remote_sync() {
    local agent=$1
    local pdfs=$2
    echo "🚀 Triggering remote evaluation for agent: $agent"
    echo "📄 Papers: $pdfs"

    # Run with environment variables; paths use configured defaults
    $SSH_CMD "$MLLM_REMOTE_USER@$MLLM_REMOTE_HOST" \
        "cd $MLLM_REMOTE_ROOT && \
         export PYTHONPATH=$REMOTE_PYTHONPATH && \
         $MLLM_REMOTE_PYTHON $REMOTE_SCRIPT \
         --repair --backend mlx --engine_url $ENGINE_URL \
         --mllm_input_path $MLLM_INPUT_PATH \
         --mllm_output_path $MLLM_OUTPUT_PATH \
         --reasoning_model_names $agent \
         --pdfs_to_process $pdfs"

    echo "✅ Finished batch for agent: $agent"
    echo "--------------------------------------------------------"
}

# Example: Uncomment and configure environment variables to run:
# export MLLM_REMOTE_USER="user"
# export MLLM_REMOTE_HOST="your.server.com"
# export MLLM_REMOTE_ROOT="/path/to/mllm"
# export MLLM_REMOTE_PYTHON="python3"
# export MLLM_INPUT_PATH="/path/to/inputs"
# export MLLM_OUTPUT_PATH="/path/to/outputs"
# export ENGINE_URL="http://localhost:4474"
#
# Then run:
# run_remote_sync "gpt-oss-20b-claude-4.5-mlx" "paper1 paper2 paper3"
