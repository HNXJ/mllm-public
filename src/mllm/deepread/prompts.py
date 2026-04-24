FIGURE_DESCRIPTION_PROMPT = """You are describing a figure extracted from an academic PDF.
Describe only the visible figure content.
Do not transcribe surrounding page text.
Do not summarize the whole paper.
If there is a chart, mention axes, legends, trends, and comparisons only if visible.
If there are panels, mention panel layout.
If text inside the figure is partially legible, report only what is clearly visible.
Return a detailed markdown response."""

def get_vlm_prompt(caption_text: str = None) -> str:
    prompt = FIGURE_DESCRIPTION_PROMPT
    if caption_text:
        prompt = f"Associated caption from the PDF text layer:\n{caption_text}\n\n{prompt}"
    return prompt
