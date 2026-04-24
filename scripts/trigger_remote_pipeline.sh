#!/bin/bash

# Configuration
REMOTE_USER="HN"
REMOTE_HOST="100.69.184.42"
REMOTE_PASS="apple"
REMOTE_PYTHON="/Users/HN/miniconda3/envs/mllm/bin/python"
REMOTE_SCRIPT="/Users/HN/MLLM/mllm-pipeline.py"
REMOTE_WORK_DIR="/Users/HN/MLLM"
REMOTE_PYTHONPATH="/Users/HN/MLLM/mllm/src"

SSH_CMD="sshpass -p '$REMOTE_PASS' ssh"

# Function to run pipeline remotely and WAIT for it to finish
run_remote_sync() {
    local agent=$1
    local pdfs=$2
    echo "🚀 Triggering remote evaluation for agent: $agent"
    echo "📄 Papers: $pdfs"
    
    # Using absolute paths for mllm_input_path and mllm_output_path
    $SSH_CMD "$REMOTE_USER@$REMOTE_HOST" "cd $REMOTE_WORK_DIR && export PYTHONPATH=$REMOTE_PYTHONPATH && $REMOTE_PYTHON $REMOTE_SCRIPT --repair --backend mlx --engine_url http://localhost:4474 --mllm_input_path /Users/HN/MLLM/inputs/HPC --mllm_output_path /Users/HN/MLLM/outputs/HPC --reasoning_model_names $agent --pdfs_to_process $pdfs"
    
    echo "✅ Finished batch for agent: $agent"
    echo "--------------------------------------------------------"
}

# START SEQUENTIAL RUNS
run_remote_sync "qwen3.5-40b-claude-4.5-opus" "Sacramento2018"
run_remote_sync "deepseek-r1-70b-mlx" "Bakhtiari2021 Greedy2022 JiangRao2024 Payeur2021 Sacramento2018 Yamins2014"
run_remote_sync "qwen3-14b-sonnet-4.5" "Bakhtiari2021 Friston2010 Furutachi2024 Greedy2022 Payeur2021 Rao2024 Sacramento2018 Yamins2014"
run_remote_sync "gemma-3-27b-it-mlx" "Bakhtiari2021 Bekinschtein2009 Chao2019 Greedy2022 Keller2012 Kiebel2008 Nejad2025 Payeur2021 Sacramento2018 Wacogne2012 Yamins2014"
run_remote_sync "qwen3-14b-gemini-3" "Attinger2017 Bakhtiari2021 Bekinschtein2009 Chao2019 Friston2010 Greedy2022 Mikulasch2023 Payeur2021 Sacramento2018 Wacogne2012 Yamins2014"
run_remote_sync "phi-4-reasoning-plus-mlx" "Bakhtiari2021 Bekinschtein2009 Furutachi2024 Garret2020 Greedy2022 Hertag2020 JiangRao2024 Keller2012 Kiebel2008 Payeur2021 Sacramento2018 Spratling2008 Yamins2014"
run_remote_sync "mistral-nemo-12b-thinking-mlx" "Bakhtiari2021 Bastos2020 Bekinschtein2009 Furutachi2024 Greedy2022 JiangRao2024 Keller2012 LaoRodriguez2023 LeeMejias2025 Mikulasch2023 Nejad2025 Payeur2021 Rao2024 Sacramento2018 Spratling2008 Spratling2010 Wacogne2012 Yamins2014"
run_remote_sync "gpt-oss-20b-claude-4.5-mlx" "Attinger2017 Bakhtiari2021 Bastos2012 Bastos2020 Bekinschtein2009 Chao2019 Friston2010 Furutachi2024 Garret2020 Greedy2022 Hertag2020 JiangRao2024 Keller2012 Keller2018 Kiebel2008 LaoRodriguez2023 LeeMejias2025 Mikulasch2023 Nejad2025 Payeur2021 Rao2024 RaoBallard1999 Sacramento2018 Spratling2008 Spratling2010 Srinivasan1982 VanDerveer2021 Wacogne2012 Wacongne2011 Westerberg2025 Yamins2014"

echo "🎯 All pending evaluations complete."
