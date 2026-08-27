"""Evidence vs. Prior Control Experiment Harness (54-Call Factorial Ablation).

Prespecified Factorial Design:
6 Prespecified Papers x 3 Conditions x 3 Repeats = 54 Calls (Gemma-4-31B-IT at T=0.35, top_p=0.90, min_p=0.10)

Conditions:
- Condition A: Full-Text DeepRead (Baseline with complete text + visual descriptions)
- Condition B: Abstract-Only (Constrained evidence)
- Condition C: De-identified / Masked Text (Redacted title, author names, institutions, journal names, DOIs)
"""

import re
from pathlib import Path
from typing import Dict, Any, List, Tuple
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[3]
INPUTS_DIR = REPO_ROOT / "content" / "markdowns"
EXP_DIR = REPO_ROOT / "content" / "202608_temp" / "evidence_prior_inputs"

PRESPECIFIED_PAPERS = [
    "Garret2020", "Attinger2017",
    "Keller2012", "Furutachi2024",
    "Chao2018", "Bastos2020"
]

# Specific Redaction Dictionaries for Condition C
REDACTION_PATTERNS = {
    "Garret2020": [
        (r"Garrett et al\.", "[MASKED_AUTHORS]"),
        (r"Garrett", "[MASKED_AUTHOR]"),
        (r"Marina Garrett", "[MASKED_AUTHOR]"),
        (r"Allen Institute for Brain Science", "[MASKED_INSTITUTION]"),
        (r"eLife", "[MASKED_JOURNAL]"),
        (r"10\.7554/eLife\.50340", "[MASKED_DOI]"),
        (r"Experience shapes the organization of neural circuits", "[MASKED_TITLE]"),
    ],
    "Attinger2017": [
        (r"Attinger et al\.", "[MASKED_AUTHORS]"),
        (r"Attinger", "[MASKED_AUTHOR]"),
        (r"Alexander Attinger", "[MASKED_AUTHOR]"),
        (r"Georg B\. Keller", "[MASKED_AUTHOR]"),
        (r"Keller, G\.B\.", "[MASKED_AUTHOR]"),
        (r"Friedrich Miescher Institute for Biomedical Research", "[MASKED_INSTITUTION]"),
        (r"Neuron", "[MASKED_JOURNAL]"),
        (r"10\.1016/j\.neuron\.2017\.01\.031", "[MASKED_DOI]"),
        (r"Visuomotor Experience Shapes the Representation of Mismatch", "[MASKED_TITLE]"),
    ],
    "Keller2012": [
        (r"Keller et al\.", "[MASKED_AUTHORS]"),
        (r"Keller, G\.B\.", "[MASKED_AUTHOR]"),
        (r"Bonhoeffer, T\.", "[MASKED_AUTHOR]"),
        (r"Hübener, M\.", "[MASKED_AUTHOR]"),
        (r"Max Planck Institute of Neurobiology", "[MASKED_INSTITUTION]"),
        (r"Neuron", "[MASKED_JOURNAL]"),
        (r"10\.1016/j\.neuron\.2012\.02\.023", "[MASKED_DOI]"),
        (r"Sensorimotor Mismatch Signals in Primary Visual Cortex", "[MASKED_TITLE]"),
    ],
    "Furutachi2024": [
        (r"Furutachi et al\.", "[MASKED_AUTHORS]"),
        (r"Furutachi", "[MASKED_AUTHOR]"),
        (r"Shohei Furutachi", "[MASKED_AUTHOR]"),
        (r"University of Basel", "[MASKED_INSTITUTION]"),
        (r"Neuron", "[MASKED_JOURNAL]"),
        (r"10\.1016/j\.neuron\.2024\.[0-9]+", "[MASKED_DOI]"),
        (r"Disinhibitory microcircuits implement predictive routing", "[MASKED_TITLE]"),
    ],
    "Chao2018": [
        (r"Chao et al\.", "[MASKED_AUTHORS]"),
        (r"Chao, Z\.C\.", "[MASKED_AUTHOR]"),
        (r"Takaura, K\.", "[MASKED_AUTHOR]"),
        (r"RIKEN Brain Science Institute", "[MASKED_INSTITUTION]"),
        (r"Nature Communications", "[MASKED_JOURNAL]"),
        (r"10\.1038/s41467-018-05188-7", "[MASKED_DOI]"),
        (r"Large-scale cortical networks for predictive coding", "[MASKED_TITLE]"),
    ],
    "Bastos2020": [
        (r"Bastos et al\.", "[MASKED_AUTHORS]"),
        (r"Bastos, A\.M\.", "[MASKED_AUTHOR]"),
        (r"Andre M\. Bastos", "[MASKED_AUTHOR]"),
        (r"Earl K\. Miller", "[MASKED_AUTHOR]"),
        (r"Miller, E\.K\.", "[MASKED_AUTHOR]"),
        (r"Massachusetts Institute of Technology", "[MASKED_INSTITUTION]"),
        (r"Neuron", "[MASKED_JOURNAL]"),
        (r"10\.1016/j\.neuron\.2020\.09\.018", "[MASKED_DOI]"),
        (r"Laminar-Specific Rhythms in Primates", "[MASKED_TITLE]"),
    ]
}


def extract_abstract(text: str) -> str:
    """Extracts abstract text block from markdown."""
    m = re.search(r"(?:#+\s*Abstract|## Summary|### Abstract)(.*?)(?=#+\s*(?:Introduction|Results|Main|Background)|$)", text, flags=re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # Fallback to first 2500 characters
    lines = text.splitlines()[:50]
    return "\n".join(lines)


def mask_deidentify_text(text: str, paper_id: str) -> str:
    """Masks explicit author, title, journal, and affiliation references."""
    masked = text
    # Strip top headers with study name
    masked = re.sub(r"^#\s+.*?\n", "# Scientific Study (De-Identified Text)\n", masked)
    
    # Apply paper-specific patterns
    if paper_id in REDACTION_PATTERNS:
        for pat, repl in REDACTION_PATTERNS[paper_id]:
            masked = re.sub(pat, repl, masked, flags=re.IGNORECASE)
            
    # Generic DOI and email redaction
    masked = re.sub(r"https?://doi\.org/[^\s\)]+", "[MASKED_DOI_URL]", masked)
    masked = re.sub(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", "[MASKED_DOI]", masked)
    masked = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[MASKED_EMAIL]", masked)
    return masked


def generate_18_ablation_inputs() -> Dict[str, Path]:
    """Generates all 18 input markdown files (6 papers x 3 conditions)."""
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    generated = {}
    
    for paper in PRESPECIFIED_PAPERS:
        full_path = INPUTS_DIR / f"{paper}-vllm-deepread_compressed.md"
        if not full_path.exists():
            full_path = INPUTS_DIR / f"{paper}-vllm-deepread.md"
        raw_text = full_path.read_text(encoding="utf-8")
        
        # Condition A: Full text
        cond_a_path = EXP_DIR / f"{paper}__CondA_Full.md"
        cond_a_path.write_text(raw_text, encoding="utf-8")
        generated[f"{paper}__CondA"] = cond_a_path
        
        # Condition B: Abstract only
        abstract_text = f"# {paper} (Abstract Only)\n\n" + extract_abstract(raw_text)
        cond_b_path = EXP_DIR / f"{paper}__CondB_Abstract.md"
        cond_b_path.write_text(abstract_text, encoding="utf-8")
        generated[f"{paper}__CondB"] = cond_b_path
        
        # Condition C: Masked de-identified text
        masked_text = mask_deidentify_text(raw_text, paper)
        cond_c_path = EXP_DIR / f"{paper}__CondC_Masked.md"
        cond_c_path.write_text(masked_text, encoding="utf-8")
        generated[f"{paper}__CondC"] = cond_c_path
        
    return generated


def perform_leakage_audit(generated_inputs: Dict[str, Path]) -> pd.DataFrame:
    """Performs deterministic verification that Condition C has zero explicit publication identity leaks."""
    audit_records = []
    for paper in PRESPECIFIED_PAPERS:
        cond_c_path = generated_inputs[f"{paper}__CondC"]
        text = cond_c_path.read_text(encoding="utf-8")
        
        leaks = []
        # Check against redaction keywords
        if paper in REDACTION_PATTERNS:
            for pat, _ in REDACTION_PATTERNS[paper]:
                found = re.findall(pat, text, flags=re.IGNORECASE)
                if found:
                    leaks.append(f"Found residual match for pattern '{pat}': {set(found)}")
                    
        # Check DOI / Email leaks
        doi_leaks = re.findall(r"10\.\d{4,9}/[^\s\)]+", text)
        if doi_leaks:
            leaks.append(f"Residual DOIs: {doi_leaks[:3]}")
            
        audit_records.append({
            "paper_id": paper,
            "condition": "Condition C (Masked)",
            "file_path": str(cond_c_path.relative_to(REPO_ROOT)),
            "char_count": len(text),
            "leak_count": len(leaks),
            "leak_details": "; ".join(leaks) if leaks else "CLEAN (Zero Leaks)",
            "audit_verdict": "PASSED" if len(leaks) == 0 else "FAILED"
        })
        
    return pd.DataFrame(audit_records)


if __name__ == "__main__":
    inputs = generate_18_ablation_inputs()
    audit_df = perform_leakage_audit(inputs)
    print(audit_df.to_string(index=False))
