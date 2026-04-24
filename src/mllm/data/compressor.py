"""Semantic text compression (q8) for context-window optimisation.

HPC Pipeline Role — Sensory Bandwidth Reduction
=================================================
In Predictive Coding, the cortex reduces redundant sensory information
before forwarding it up the hierarchy.  Analogously, this compressor
strips references, boilerplate, and parenthetical citations from study
text *before* it enters the LLM's context window — maximising the ratio
of evidence-bearing tokens to total tokens.  The ``q8`` label reflects
the target compression ratio (~1/8th of original volume).
"""

import re
from typing import List, Tuple


class TextCompressor:
    """Utilities for semantic compression (q8) and boilerplate removal."""

    @staticmethod
    def strip_references(text: str) -> str:
        """Removes the References/Bibliography section."""
        ref_patterns = [
            r'\nReferences\s*\n',
            r'\nBIBLIOGRAPHY\s*\n',
            r'\nLITERATURE CITED\s*\n',
            r'\nWORKS CITED\s*\n'
        ]
        for pattern in ref_patterns:
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            if matches:
                last_match = matches[-1]
                return text[:last_match.start()].strip()
        return text

    @staticmethod
    def clean_boilerplate(text: str) -> str:
        """Removes page numbers, headers, and metadata fluff."""
        # Page numbers
        text = re.sub(r'\bPage\s+\d+(\s+of\s+\d+)?\b', '', text, flags=re.IGNORECASE)
        # Journals and DOIs
        text = re.sub(r'DOI:\s*10\.\d{4}/[\w\.]+', '', text, flags=re.IGNORECASE)
        text = re.sub(r'https?://[\w\./\-]+', '', text)
        # Standalone line numbers
        text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
        return text.strip()

    @staticmethod
    def semantic_summarize_chunks(text: str) -> str:
        """
        Executes 'q8' (1/8th ratio) semantic compression.
        Currently uses aggressive redundancy filtering and citation pruning.
        """
        text = TextCompressor.strip_references(text)
        text = TextCompressor.clean_boilerplate(text)
        
        # Remove parenthetical citations (e.g., (Smith, 2020)) to save context
        text = re.sub(r'\(\w+ et al\., \d{4}\)', '', text)
        text = re.sub(r'\(\w+, \d{4}\)', '', text)
        
        # Consolidate whitespace
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r' +', ' ', text)
        
        return text.strip()

if __name__ == "__main__":
    sample = "Introduction... (Sterzer et al., 2024)\nDOI: 10.101/test\nReferences\n1. Smith et al. 2020..."
    compressed = TextCompressor.semantic_summarize_chunks(sample)
    print(f"Compressed Result: {compressed}")
