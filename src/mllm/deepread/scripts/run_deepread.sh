#!/usr/bin/env bash
set -euo pipefail

# Ensure we are in the mllm source directory to find mllm.deepread.cli
# Assumes this script is in src/mllm/deepread/scripts/
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/../../../../.." && pwd )"
SRC_DIR="$REPO_ROOT/src"

PDF_PATH="$1"
OUT_PATH="$2"

# Ensure src is in PYTHONPATH
export PYTHONPATH="$SRC_DIR:$PYTHONPATH"

# Set default model if not provided (optional, handled by cli.py defaults)
# We can pass additional args if needed

python -m mllm.deepread.cli "$PDF_PATH" -o "$OUT_PATH" --dump-debug-dir .deepread_debug --emit-json-manifest .deepread_debug/manifest.json
