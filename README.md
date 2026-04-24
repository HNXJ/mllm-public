# MLLM: Multi-modal Large Language Model Pipeline

A streamlined pipeline for processing, reasoning, and analyzing scientific documents using local LLMs via MLX.

## Overview
This repository provides a robust backend for running inference on scientific papers, utilizing local MLX-compatible models. It includes:
- **Pipeline Controller**: Orchestrates ingestion, reasoning, and output extraction.
- **Sentinel API**: A control plane for managing model loading, pipeline queues, and telemetry.
- **DeepRead Module**: Specialized sub-module for interpreting figures, tables, and text from research PDFs.

## Setup
1. Clone the repository.
2. Install requirements from `pyproject.toml`.
3. Configure your paths in the `.env` file.
4. Run the sentinel API to begin processing.

## License
Provided under the MIT License.
