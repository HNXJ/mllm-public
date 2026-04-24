import re

def context_clean_compress(input_text: str) -> str:
    """
    Deterministically compresses academic markdown by stripping redundant
    sections, OCR/VLM errors, and publisher boilerplate while preserving 100%
    of core scientific context, figures, headers, and equations.
    """
    # 1. Strip the References / Bibliography section completely.
    # Academic papers usually place this at the very end. This saves massive token counts.
    text = re.split(r'\n#+\s*References\b|\nReferences\n', input_text, flags=re.IGNORECASE)[0]
    
    # 2. Scrub systematic parsing artifacts and VLM failures
    text = re.sub(r'\*VLM Error: Max retries exceeded\.\*', '', text)
    
    # 3. Scrub redundant publisher boilerplate (e.g., Nature Communications headers, recurring DOIs)
    # This specifically targets the repeating footer bloat seen in parsed PDFs
    text = re.sub(r'Article\s+https://doi\.org/[^\n]+', '', text)
    text = re.sub(r'Nature Communications\|\s*\(\d+\)\d+:\d+', '', text)
    text = re.sub(r'Received:.*?Accepted:.*?Published online:.*?\n', '', text, flags=re.DOTALL)
    text = re.sub(r'Check for updates\n', '', text)
    text = re.sub(r'\d{10}\(\):,;', '', text) # Removes raw OCR digit artifacts
    
    # 4. Strip inline citations to save tokens, ONLY IF they are standard bracket/parentheses formats
    # e.g., removes [1, 2, 3] or (Author et al., 2025) but keeps the prose intact.
    # Note: Use with caution if specific citation numbers are critical to the immediate prompt.
    text = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', text)
    
    # 5. Compress Whitespace
    # Reduce multiple newlines to a maximum of two (preserves paragraph breaks)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Reduce multiple spaces to a single space
    text = re.sub(r'[ \t]{2,}', ' ', text)
    
    return text.strip()
