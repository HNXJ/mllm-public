#!/bin/bash

# Overnight Queue Configuration (use environment variables or defaults)
MLLM_REMOTE_USER="${MLLM_REMOTE_USER:-user}"
MLLM_REMOTE_HOST="${MLLM_REMOTE_HOST:-localhost}"
MLLM_REMOTE_ROOT="${MLLM_REMOTE_ROOT:-.}"
MLLM_REMOTE_PYTHON="${MLLM_REMOTE_PYTHON:-python}"
MLLM_INPUT_PATH="${MLLM_INPUT_PATH:-./inputs/HPC}"
MLLM_OUTPUT_PATH="${MLLM_OUTPUT_PATH:-./outputs/HPC}"
ENGINE_URL="${ENGINE_URL:-http://localhost:4474}"

REMOTE_PYTHONPATH="$MLLM_REMOTE_ROOT/src"
REMOTE_SCRIPT="$MLLM_REMOTE_ROOT/mllm-pipeline.py"
SSH_CMD="ssh"

PAPERS="Attinger2017 Bakhtiari2021 Bastos2012 Bastos2020 Bekinschtein2009 Chao2019 Friston2010 Furutachi2024 Garret2020 Greedy2022 Hertag2020 JiangRao2024 Keller2012 Keller2018 Kiebel2008 LaoRodriguez2023 LeeMejias2025 Mikulasch2023 Nejad2025 Payeur2021 Rao2024 RaoBallard1999 Sacramento2018 Spratling2008 Spratling2010 Srinivasan1982 VanDerveer2021 Wacogne2012 Wacongne2011 Westerberg2025 Yamins2014"

AGENTS=(
    "gpt-oss-20b-claude-4.5-mlx"
    "qwen3.5-40b-opus-4.5-mlx"
    "gemma-3-27b-it-mlx"
    "deepseek-r1-70b-mlx"
    "phi-4-reasoning-plus-mlx"
    "mistral-nemo-12b-thinking-mlx"
    "qwen3-14b-sonnet-4.5-mlx"
    "qwen3-14b-gemini-3-mlx"
    "phi-4-8bit-mlx"
    "olmo-3-32b-think-mlx"
    "ministral-3-14b-instruct-2512-mxfp8-mlx"
    "mixtral-8x22b-instruct-v0.1-4bit-mlx"
    "nemotron-3-nano-30b-mlx"
    "qwen3-coder-next-6bit-mlx"
    "qwen3-vl-30b-a3b-instruct-mlx-8bit-mlx"
)

echo "🌕 Starting MLLM Overnight Queue: 465 Evaluations (15 Agents * 31 Papers)"
echo "--------------------------------------------------------------------------"

for agent in "${AGENTS[@]}"; do
    echo "🚀 [$(date)] Processing Agent: $agent"
    
    # 1. Verification Step (Load-Test-Unload)
    echo "🧪 Verifying profile functionality..."
    $SSH_CMD "$MLLM_REMOTE_USER@$MLLM_REMOTE_HOST" \
        "cd $MLLM_REMOTE_ROOT && \
         export PYTHONPATH=$REMOTE_PYTHONPATH && \
         $MLLM_REMOTE_PYTHON $REMOTE_SCRIPT \
         --mode mlx --test_profile --reasoning_model_names $agent"

    # 2. Sequential Evaluation Step
    echo "🧠 Running batch evaluations for all papers..."
    $SSH_CMD "$MLLM_REMOTE_USER@$MLLM_REMOTE_HOST" \
        "cd $MLLM_REMOTE_ROOT && \
         export PYTHONPATH=$REMOTE_PYTHONPATH && \
         $MLLM_REMOTE_PYTHON $REMOTE_SCRIPT \
         --mode mlx --engine_url $ENGINE_URL \
         --mllm_input_path $MLLM_INPUT_PATH \
         --mllm_output_path $MLLM_OUTPUT_PATH \
         --reasoning_model_names $agent --pdfs_to_process $PAPERS"
    
    echo "✅ [$(date)] Agent $agent complete."
    echo "--------------------------------------------------------------------------"
done

echo "🎯 MLLM Overnight Queue Complete."
