import argparse
import os
from pathlib import Path
from jmllm.pipeline.controller import PipelineController

REPO_ROOT = Path(__file__).resolve().parents[3]

def main():
    parser = argparse.ArgumentParser(description='JMLLM HPC Evaluation Pipeline')
    parser.add_argument('--pdfs_to_process', nargs='+', default=[])
    parser.add_argument('--reasoning_model_names', nargs='+', default=['gpt-oss-20b-claude-4.5'])
    parser.add_argument('--glossary_path', default=str(REPO_ROOT / 'ontology/glossary/HPC/hpc-36-reference.md'))
    parser.add_argument('--instructions_path', default=str(REPO_ROOT / 'ontology/instructions/hpc_eval_prompt.md'))
    parser.add_argument('--mllm_input_path', default=os.environ.get('MLLM_INPUT_PATH', 'content/inputs'))
    parser.add_argument('--mllm_output_path', default=os.environ.get('MLLM_OUTPUT_PATH', 'content/outputs'))
    parser.add_argument('--mllm_log_path', default=os.environ.get('MLLM_LOG_PATH', './logs/pipeline.log'))
    parser.add_argument('--engine_url', default=os.environ.get('ENGINE_URL', 'http://localhost:4474'))
    parser.add_argument('--mode', default='mlx')
    parser.add_argument('--deepread_vlm', default='qwen3.5-vl-4b-mlx-crack')
    parser.add_argument('--deepread_only', action='store_true')
    parser.add_argument('--test_profile', action='store_true')
    parser.add_argument('--repair', action='store_true')
    parser.add_argument('--no_vlm', action='store_true')
    parser.add_argument('--no_load', action='store_true')
    parser.add_argument('--timeout', type=int, default=120)
    parser.add_argument('--temperature', type=float, default=0.7)
    parser.add_argument('--top_p', type=float, default=0.9)
    parser.add_argument('--min_p', type=float, default=None)
    parser.add_argument('--parallel_workers', type=int, default=1)
    parser.add_argument('--context_window', type=int, default=131072)
    
    args = parser.parse_args()
    PipelineController(args).run_pipeline()

if __name__ == '__main__':
    main()
