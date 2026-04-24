#!/bin/bash

REMOTE_USER="HN"
REMOTE_HOST="100.69.184.42"
REMOTE_PASS="apple"
REMOTE_WORK_DIR="/Users/HN/MLLM"
REMOTE_PYTHONPATH="/Users/HN/MLLM/mllm/src"
REMOTE_PYTHON="/Users/HN/miniconda3/envs/mllm/bin/python"
REMOTE_SCRIPT="/Users/HN/MLLM/mllm-pipeline.py"
SSH_CMD="sshpass -p '$REMOTE_PASS' ssh"

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
    $SSH_CMD "$REMOTE_USER@$REMOTE_HOST" "cd $REMOTE_WORK_DIR && export PYTHONPATH=$REMOTE_PYTHONPATH && $REMOTE_PYTHON $REMOTE_SCRIPT --mode mlx --test_profile --reasoning_model_names $agent"
    
    # 2. Sequential Evaluation Step
    echo "🧠 Running batch evaluations for all 31 papers..."
    $SSH_CMD "$REMOTE_USER@$REMOTE_HOST" "cd $REMOTE_WORK_DIR && export PYTHONPATH=$REMOTE_PYTHONPATH && $REMOTE_PYTHON $REMOTE_SCRIPT --mode mlx --engine_url http://localhost:4474 --mllm_input_path /Users/HN/MLLM/inputs/HPC --mllm_output_path /Users/HN/MLLM/outputs/HPC --reasoning_model_names $agent --pdfs_to_process $PAPERS"
    
    echo "✅ [$(date)] Agent $agent complete."
    echo "--------------------------------------------------------------------------"
done

echo "🎯 MLLM Overnight Queue Complete."
