#!/bin/bash
# Trigger HPC evaluations using local mllm-pipeline.
# Configure environment variables before running:
# - MLLM_WORKSPACE_ROOT: workspace root (default: current directory)
# - MLLM_REMOTE_PYTHON: path to Python interpreter (default: python)

MLLM_WORKSPACE_ROOT="${MLLM_WORKSPACE_ROOT:-.}"
PYTHON="${MLLM_REMOTE_PYTHON:-python}"

cd "$MLLM_WORKSPACE_ROOT" || { echo "Error: could not cd to $MLLM_WORKSPACE_ROOT"; exit 1; }

# Full list of verified HPC papers
HPC_PAPERS="Attinger2017 Bakhtiari2021 Bastos2012 Bastos2020 Bekinschtein2009 Chao2019 Friston2010 Furutachi2024 Garret2020 Greedy2022 Hertag2020 JiangRao2024 Keller2012 Keller2018 Kiebel2008 LaoRodriguez2023 LeeMejias2025 Mikulasch2023 Nejad2025 Payeur2021 Rao2024 RaoBallard1999 Sacramento2018 Spratling2008 Spratling2010 Srinivasan1982 VanDerveer2021 Wacogne2012 Wacongne2011 Westerberg2025 Yamins2014"

# List of working agents
AGENTS=(
    "gpt-oss-20b-claude-4.5-mlx"
    "nemotron-3-nano-30b-mlx"
    "deepseek-r1-70b-mlx"
    "gemma-3-27b-it-mlx"
    "mistral-nemo-12b-thinking-mlx"
    "phi-4-reasoning-plus-mlx"
    "olmo-3-32b-think-mlx"
    "qwen3.5-40b-claude-4.5-opus-mlx"
)

echo "🚀 Triggering PENDING HPC evaluations..."

for AGENT in "${AGENTS[@]}"; do
    echo "--------------------------------------------------------"
    echo "🤖 Agent: $AGENT"
    $PYTHON mllm-pipeline.py --reasoning_model_names "$AGENT" --pdfs_to_process $HPC_PAPERS
done

echo "🎯 All pending HPC evaluations triggered."
