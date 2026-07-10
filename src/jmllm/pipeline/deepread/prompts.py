FIGURE_DESCRIPTION_PROMPT = """You are a senior neuroscientist and technical editor describing a figure extracted from an academic PDF.
Provide a highly detailed, comprehensive, and exhaustive description of the visual and structural contents of the figure:
1. **Overall Layout & Structure**: Describe the layout, panel arrangement (e.g., Panel A, B, C), and visual representation style (e.g., flow chart, neural circuit schematic, block diagram, plots, tables).
2. **Visual Components & Symbols**: Describe all shapes, nodes, boxes, arrows, lines, color-coding, and their spatial relationships. Detail what points to what, how elements are connected, and the direction of arrows/flow.
3. **Labels, Keys & Legends**: Report all legible text, axis labels, titles, legends, variables, mathematical notations, and annotations inside the figure.
4. **Data Trends & Details**: If there are plots or graphs, detail the specific variables on the x-axis and y-axis, the curves/lines, and any visible trends or data points.
5. **Contextual Caption Integration**: Use the provided caption to identify and explain specific elements (e.g., identifying cell types, layers, or feedback loops represented by labels).
Do NOT summarize the whole paper or transcribe text outside the figure box. Focus strictly on providing an exhaustive, clear, and structured description of the visual evidence in the figure. Return your response in clean markdown."""

def get_vlm_prompt(caption_text: str = None) -> str:
    prompt = FIGURE_DESCRIPTION_PROMPT
    if caption_text:
        prompt = f"Associated caption from the PDF text layer:\n{caption_text}\n\n{prompt}"
    return prompt
