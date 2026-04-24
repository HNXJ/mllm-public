from typing import List
from mllm.deepread.models import TextBlock, FigureRegion

class Interleaver:
    """Assembles the final Markdown by interleaving text blocks and figure descriptions."""

    def interleave_page(self, page_index: int, text_blocks: List[TextBlock], figures: List[FigureRegion]) -> str:
        """Assembles Markdown for a single page."""
        
        # 1. Identify insertion points for figures
        # Map: block_no -> List[FigureRegion] to insert *after* this block
        insert_after = {}
        top_figures = []

        for fig in figures:
            if fig.caption_block_no is not None:
                # Insert after the caption block
                block_no = fig.caption_block_no
                if block_no not in insert_after:
                    insert_after[block_no] = []
                insert_after[block_no].append(fig)
            else:
                # Find nearest preceding text block
                # Figures are often near the top, middle or bottom.
                # If above all text, add to top_figures.
                preceding = [tb for tb in text_blocks if tb.bbox[1] < fig.bbox[1]]
                if not preceding:
                    top_figures.append(fig)
                else:
                    # Sort by block_no and pick the highest one
                    last_tb = max(preceding, key=lambda tb: tb.block_no)
                    if last_tb.block_no not in insert_after:
                        insert_after[last_tb.block_no] = []
                    insert_after[last_tb.block_no].append(fig)

        # 2. Build Markdown
        lines = [f"## Page {page_index + 1}", ""]
        
        # Add top figures
        for fig in top_figures:
            lines.append(self._format_figure_block(fig))
            lines.append("")

        # Add text blocks and their following figures
        for tb in sorted(text_blocks, key=lambda b: b.block_no):
            lines.append(tb.text.strip())
            lines.append("")
            
            if tb.block_no in insert_after:
                for fig in insert_after[tb.block_no]:
                    lines.append(self._format_figure_block(fig))
                    lines.append("")

        return "\n".join(lines)

    def _format_figure_block(self, fig: FigureRegion) -> str:
        content = []
        if fig.caption_text:
            content.append(f"> Figure caption (from PDF text): {fig.caption_text}")
        
        desc = fig.description if fig.description else "No description provided."
        content.append(f"> Figure description (generated): {desc}")
        
        return "\n".join(content)
