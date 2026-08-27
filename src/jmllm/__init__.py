import os
from pathlib import Path
from typing import List, Optional

from jmllm.pipeline.controller import PipelineController
from jmllm.util.helpers import get_available_models

def run_all_visualizations(*args, **kwargs):
    from jmllm.vis.plotting import run_all_visualizations as _run_viz
    return _run_viz(*args, **kwargs)

# Global Configuration State
_instructions_path = None
_glossary_path = None
_content_path = None
_sqlite_path = None
_models = []

def set_instructions(path: str):
    """Set the path to the evaluation instructions markdown file."""
    global _instructions_path
    _instructions_path = str(Path(path).resolve())

def set_glossary(path: str):
    """Set the path to the evaluation glossary markdown file."""
    global _glossary_path
    _glossary_path = str(Path(path).resolve())

def set_path(path: str):
    """Set the path to the root content directory (which houses inputs/, outputs/, etc.)."""
    global _content_path
    _content_path = str(Path(path).resolve())

def set_sqlite(path: str):
    """Set the target SQLite database path for exports."""
    global _sqlite_path
    _sqlite_path = str(Path(path).resolve())

def add_model(
    name: str, 
    url: str, 
    provider: str = "mlx", 
    temperature: float = 0.7, 
    context_window: int = 131072, 
    top_p: Optional[float] = None, 
    min_p: Optional[float] = None, 
    response_format: Optional[dict] = None
):
    """Register an LLM model card with its endpoint configuration and provider."""
    global _models
    _models.append({
        "name": name,
        "url": url,
        "provider": provider,
        "temperature": temperature,
        "context_window": context_window,
        "top_p": top_p,
        "min_p": min_p,
        "response_format": response_format
    })

def run(inputs: Optional[List[str]] = None, parallel_workers: Optional[int] = None, no_vlm: bool = True):
    """Run the evaluation pipeline with the current programmatic configuration."""
    global _instructions_path, _glossary_path, _content_path, _sqlite_path, _models
    
    # Resolve project root
    repo_root = Path(__file__).resolve().parents[2]
    
    # Resolve default paths if not set
    content_dir = Path(_content_path) if _content_path else repo_root / "content"
    inputs_dir = content_dir / "inputs"
    outputs_dir = content_dir / "outputs"
    log_file = repo_root / "logs" / "pipeline.log"
    
    instructions = _instructions_path if _instructions_path else str(repo_root / "src/ontology/instructions/hpc_eval_prompt.md")
    glossary = _glossary_path if _glossary_path else str(repo_root / "src/ontology/glossary/HPC/hpc-36-reference.md")
    
    # Determine PDFs to process
    if inputs:
        pdfs = [f if f.endswith(".pdf") else f"{f}.pdf" for f in inputs]
    else:
        # Default to all PDFs in the inputs folder
        if inputs_dir.exists():
            pdfs = [f.name for f in inputs_dir.glob("*.pdf")]
        else:
            pdfs = []
            
    if not pdfs:
        print("⚠️ No PDFs found to process.")
        return
        
    # Use loaded models or default
    reasoning_models = [m["name"] for m in _models] if _models else ["gemma-4-e4b-it-mxfp8"]
    engine_url = _models[0]["url"] if _models else "http://localhost:1234"
    provider = _models[0]["provider"] if _models else "mlx"
    temp = _models[0]["temperature"] if _models else 0.7
    top_p = _models[0].get("top_p") if _models else None
    min_p = _models[0].get("min_p") if _models else None
    c_win = _models[0].get("context_window", 131072) if _models else 131072
    res_fmt = _models[0].get("response_format") if _models else None
    
    # Mock namespace class to emulate parsed argparse arguments
    class ProgrammaticArgs:
        def __init__(self):
            self.pdfs_to_process = pdfs
            self.reasoning_model_names = reasoning_models
            self.glossary_path = glossary
            self.instructions_path = instructions
            self.mllm_input_path = str(inputs_dir)
            self.mllm_output_path = str(outputs_dir)
            self.mllm_log_path = str(log_file)
            self.engine_url = engine_url
            self.mode = "mlx"
            self.deepread_vlm = "qwen3.5-vl-4b-mlx-crack"
            self.deepread_only = False
            self.test_profile = False
            self.repair = False
            self.no_vlm = no_vlm
            self.no_load = True # assume loaded in local server by default
            self.timeout = 600
            self.temperature = temp
            self.top_p = top_p
            self.min_p = min_p
            self.parallel_workers = parallel_workers or 1
            self.context_window = c_win
            self.provider = provider
            self.response_format = res_fmt
            self.sqlite_path = _sqlite_path

    args = ProgrammaticArgs()
    controller = PipelineController(args)
    controller.run_pipeline()

def visualize(csv_path: Optional[str] = None, reports_dir: Optional[str] = None):
    """Run visualizations on the aggregated scores table."""
    repo_root = Path(__file__).resolve().parents[2]
    content_dir = Path(_content_path) if _content_path else repo_root / "content"
    
    c_path = csv_path if csv_path else str(content_dir / "tables/aggregated_scores.csv")
    r_dir = reports_dir if reports_dir else str(content_dir / "reports")
    
    print(f"[*] Running MLLM Visualizations on {c_path}...")
    run_all_visualizations(csv_path=c_path, reports_dir=r_dir)
