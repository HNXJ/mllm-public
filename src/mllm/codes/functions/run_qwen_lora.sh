#!/bin/bash

# Configuration for Qwen-Opus-Reasoning LoRA
MODEL_PATH="./workspace/mlx_models/Qwen3.5-27B-Opus-Reasoning-6bit"
DATA_DIR="./workspace/Computational/misc/mllm_finetune/data"
ADAPTER_DIR="./workspace/Computational/misc/mllm_finetune/adapters_qwen_opus"

# Hyperparameters from FINETUNE_CORE.md
ITERS=500
RANK=16
ALPHA=32
LR=1e-5
BATCH_SIZE=4

echo "🚀 Starting Qwen-Opus-Reasoning Fine-Tuning..."
echo "🧠 Model: $MODEL_PATH"
echo "📂 Data: $DATA_DIR"

python3 -m mlx_lm.lora \
    --model "$MODEL_PATH" \
    --train \
    --data "$DATA_DIR" \
    --iters "$ITERS" \
    --batch-size "$BATCH_SIZE" \
    --learning-rate "$LR" \
    --adapter-path "$ADAPTER_DIR" \
    --lora-layers 16 \
    --rank "$RANK" \
    --alpha "$ALPHA"

echo "✅ Fine-tuning session finished."
