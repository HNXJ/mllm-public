"""Centralised logging configuration for the MLLM HPC pipeline.

HPC Pipeline Role — Audit Trail
=================================
Provides a single ``setup_logger`` factory that every module uses.  This
guarantees a consistent log format across all pipeline stages — from
DeepRead extraction (sensory input) through LLM inference (top-down
prediction) to score aggregation (consensus).  The uniform format makes
it possible to trace a single evaluation run from PDF ingestion to JSON
output across log files and the monitor dashboard.
"""

import logging
import sys
import os
import time
import json
import traceback
from pathlib import Path
from typing import Optional, Any, Dict
from datetime import datetime

def setup_logger(
    name: str,
    level: int = logging.INFO,
    log_file: Optional[Path] = None,
    log_to_console: bool = True,
    format_string: Optional[str] = None
) -> logging.Logger:
    """Set up logger with consistent formatting."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if logger.hasHandlers():
        logger.handlers.clear()
    
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    
    formatter = logging.Formatter(format_string)
    
    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

class StructuredLogger:
    """Hyper-verbose context-aware logger for the MLLM pipeline."""
    
    def __init__(self, name: str, log_path: Path, heartbeat_path: Optional[Path] = None):
        self.logger = setup_logger(name, log_file=log_path)
        self.log_path = log_path
        self.heartbeat_path = heartbeat_path
        self.active_context = {}

    def set_context(self, **kwargs):
        """Set persistent metadata context for subsequent logs."""
        self.active_context.update(kwargs)

    def log_event(self, stage: str, message: str, level: int = logging.INFO, **kwargs):
        """Log a structured event with stage and optional metadata."""
        context = self.active_context.copy()
        context.update(kwargs)
        
        meta_str = " | ".join([f"{k}={v}" for k, v in context.items()])
        full_msg = f"[{stage.upper()}] {message}"
        if meta_str:
            full_msg += f" (Context: {meta_str})"
            
        self.logger.log(level, full_msg)
        self.log_heartbeat()

    def log_failure(self, stage: str, why: str, exception: Optional[Exception] = None, next_action: str = "Continue", **kwargs):
        """Log a structured failure with deep context and traceback."""
        context = self.active_context.copy()
        context.update(kwargs)
        
        exc_type = type(exception).__name__ if exception else "None"
        exc_text = str(exception) if exception else "N/A"
        
        # Build the structured explanation requested by the user
        failure_msg = (
            f"\n"
            f"❌ FAILURE at Stage: `{stage}`\n"
            f"   WHAT: {why}\n"
            f"   WHY: {exc_text} (Type: {exc_type})\n"
            f"   CONTEXT: {json.dumps(context, indent=4, default=str)}\n"
            f"   NEXT ACTION: {next_action}\n"
        )
        
        if exception:
            failure_msg += f"   TRACEBACK:\n{traceback.format_exc()}\n"
            
        self.logger.error(failure_msg)
        self.log_heartbeat()

    def log_heartbeat(self):
        """Update heartbeat file to signal pipeline activity."""
        if self.heartbeat_path:
            try:
                self.heartbeat_path.parent.mkdir(parents=True, exist_ok=True)
                with open(self.heartbeat_path, "w") as f:
                    f.write(str(time.time()))
            except Exception:
                pass

# Example usage:
# logger = setup_logger(__name__)
