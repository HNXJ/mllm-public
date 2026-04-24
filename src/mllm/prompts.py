"""Prompt construction for the MLLM HPC evaluation pipeline.

HPC Pipeline Role — Prior Definition Layer
==========================================
In Hierarchical Predictive Coding, the "prior" determines what a generative
model expects to find.  This module constructs that prior by assembling:

- **Glossary content** — the factor definitions that define *what* the model
  should predict (e.g. "Laminar Prediction Error", "Top-Down Modulation").
- **Evaluation rules** — the scoring semantics and output-format constraints
  that define *how* the model should respond.
- **Study text** — the sensory evidence against which predictions are scored.

The assembled prompt is the computational equivalent of setting synaptic
weights on the top-down pathway before running a prediction cycle.

Functions
---------
- ``parse_glossary``                 — Load and parse a markdown glossary table.
- ``get_study_glossary_instructions`` — Build the full unified prompt.
- ``get_glossary_instruction_block``  — Build an XML-tagged glossary block.
- ``build_hpc_prompt``               — Build the specialised HPC evaluation prompt.
"""

import re
import json
from pathlib import Path
from typing import List, Any, Optional, Iterable
from mllm.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def parse_glossary(
    subject_name: str,
    repo_root: Optional[Path] = None,
    glossary_path: Optional[Path] = None,
) -> tuple[str, List[str]]:
    """Parse a glossary markdown file into a definition block and a list of keys.

    Searches multiple candidate paths in priority order:
    1. Explicitly provided ``glossary_path``.
    2. Paths relative to ``repo_root``.
    3. Paths relative to this package's install location.

    The glossary markdown is expected to contain a table with columns
    ``| # | Factor Name | Definition |``.

    Args:
        subject_name:  Glossary subject identifier (e.g. ``'HPC'``, ``'SCZ'``).
        repo_root:     Optional path to the repository root for candidate
                       path construction.
        glossary_path: Optional explicit path to the glossary file.

    Returns:
        Tuple of (definitions_text, keys_list) where ``definitions_text``
        is a newline-separated string of ``'Factor: Definition'`` pairs and
        ``keys_list`` is the ordered list of factor names.

    Raises:
        FileNotFoundError: If no glossary file is found at any candidate path.
    """
    subject_upper = subject_name.upper()
    subject_lower = subject_name.lower()

    candidates = []
    if glossary_path is not None:
        candidates.append(glossary_path)
    if repo_root is not None:
        candidates.append(repo_root / "src" / "mllm" / "skills" / "glossary" / subject_upper / f"{subject_lower}-36-reference.md")
        candidates.append(repo_root / "skills" / "glossary" / subject_upper / f"{subject_lower}-36-reference.md")
        candidates.append(repo_root / "skills" / "glossary" / subject_lower / f"{subject_lower}-36-reference.md")

    package_root = Path(__file__).resolve().parent
    candidates.append(package_root / "skills" / "glossary" / subject_upper / f"{subject_lower}-36-reference.md")
    candidates.append(package_root / "skills" / "glossary" / subject_lower / f"{subject_lower}-36-reference.md")

    gloss_path = next((candidate for candidate in candidates if candidate.exists()), None)
    if gloss_path is None:
        searched = "\n".join(str(candidate) for candidate in candidates)
        raise FileNotFoundError(f"Glossary file not found. Searched:\n{searched}")

    glossary_md = gloss_path.read_text()
    definitions: List[str] = []
    keys: List[str] = []

    for line in glossary_md.splitlines():
        match = re.search(r"\|\s*\d+\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", line)
        if match:
            factor_name = match.group(1).strip()
            factor_def = match.group(2).strip()
            if factor_name and factor_name != "Factor Name":
                definitions.append(f"{factor_name}: {factor_def}")
                keys.append(factor_name)

    return "\n".join(definitions), keys

def get_study_glossary_instructions(
    unified_study: str, 
    glossary_content: str, 
    prompt_role: str, 
    rules: str,
    output_format_example: str
) -> str:
    """Constructs the final prompt by combining deepread study text, glossary, role, rules, and output example."""
    unified_prompt = f"""
{prompt_role}

# RULES
{rules}

# GLOSSARY
{glossary_content}

# OUTPUT FORMAT EXAMPLE
{output_format_example}

# STUDY CONTENT
{unified_study}

# FINAL MANDATE
Return exactly one valid JSON object and nothing else.
Do not wrap the JSON in markdown fences.
Do not include commentary before or after the JSON.
"""
    return unified_prompt.strip()

def get_glossary_instruction_block(terms: Iterable[Any]) -> str:
    """
    Build a glossary instruction block for the reasoning prompt.
    """
    if not terms:
        return ""

    if isinstance(terms, dict):
        lines = [f"- {key}: {value}" for key, value in terms.items()]
        glossary_text = "\n".join(lines)
    else:
        glossary_text = "\n".join(f"- {term}" for term in terms)

    return f"""
<glossary>
Use the following study-specific glossary terms and definitions when interpreting the document and generating outputs.
{glossary_text}
</glossary>
""".strip()

def build_hpc_prompt(study_text: str, glossary: str, glossary_keys: list[str], model_name: str) -> str:
    keys_json = json.dumps(glossary_keys, ensure_ascii=False)
    return f"""
You are a senior neuroscientist and biophysicist evaluating predictive-coding mechanisms in a neuroscience study.

Evaluate the study against the supplied glossary.

Definitions:
- LO (Local Oddball): short-term sensory deviance or immediate stimulus violation.
- GO (Global Oddball): long-term or sequence-level deviance over a broader temporal pattern.

Scoring semantics:
- +1.0: strong evidence supporting the factor
- +0.5: moderate evidence supporting the factor
- 0.0: explicitly addressed but neutral, mixed, or inconclusive
- -0.5: moderate evidence against the factor
- -1.0: strong evidence against the factor
- null: factor cannot be meaningfully evaluated from the study

Requirements:
1. Return exactly one valid JSON object and nothing else.
2. Do not wrap the JSON in markdown fences.
3. Include every glossary key exactly once in both `lo_evaluations` and `go_evaluations`.
4. Use exact glossary key strings.
5. Do not add extra keys inside `lo_evaluations` or `go_evaluations`.
6. Use `null` when a factor is not meaningfully addressed.
7. Use `0.0` only when the factor is discussed but neutral or inconclusive.
8. Do not guess metadata. Use null if uncertain.
9. Keep `reasoning_log_text` concise and evidence-based.

Glossary Definitions:
{glossary}

Glossary Keys:
{keys_json}

Study Text:
{study_text}

Required output shape:
{{
  "lo_evaluations": {{ "Factor Name": 0.8 }},
  "go_evaluations": {{ "Factor Name": 0.5 }},
  "first_author": "Name or null",
  "publication_year": "YYYY or null",
  "study_type": "Empirical or Review or null",
  "agent_name": "{model_name}",
  "reasoning_log_text": "Concise evidence-based rationale."
}}
""".strip()
