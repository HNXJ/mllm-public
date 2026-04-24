import re
from typing import List
from mllm.deepread.models import TextBlock

def verify_text_fidelity(original_blocks: List[TextBlock], markdown_output: str) -> bool:
    """Verifies that the markdown output preserves the original text blocks."""
    
    # 1. Normalize original text: join sorted blocks
    original_text = "".join(b.text.strip() for b in sorted(original_blocks, key=lambda b: b.block_no))
    original_text = re.sub(r'\s+', '', original_text)
    
    # 2. Extract text from Markdown, ignoring figure blocks and page headers
    # Strip figure blocks
    stripped_md = re.sub(r'> Figure (?:caption|description) .*?\n', '', markdown_output)
    # Strip page headers
    stripped_md = re.sub(r'## Page \d+\n', '', stripped_md)
    # Normalize extracted text
    extracted_text = re.sub(r'\s+', '', stripped_md)
    
    # 3. Compare
    # Note: Exact comparison might be too strict if PyMuPDF handles block concatenation differently.
    # But the brief says "Do not modify the text block strings."
    return original_text == extracted_text
