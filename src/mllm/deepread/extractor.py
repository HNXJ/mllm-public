import fitz
from typing import List, Tuple
from mllm.deepread.models import TextBlock

class PDFExtractor:
    """Extracts text blocks and identifies visual content regions using PyMuPDF."""

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)

    def extract_page_data(self, page_index: int) -> Tuple[str, List[TextBlock], List[dict], List[Tuple[float, float, float, float]]]:
        """
        Extracts raw text, structured text blocks, and all visual region bboxes.
        
        Returns:
            Tuple of (raw_page_text, text_blocks, all_raw_blocks, visual_bboxes)
        """
        page = self.doc[page_index]
        raw_page_text = page.get_text("text")
        
        # block_type 0: text, 1: image, 2: ? (rare), 3: vector
        # Returns tuples: (x0, y0, x1, y1, "text", block_no, block_type)
        all_raw_blocks = page.get_text("blocks", sort=True)
        
        text_blocks = []
        for b in all_raw_blocks:
            if b[6] == 0:  # Text block
                text_blocks.append(TextBlock(
                    page_index=page_index,
                    block_no=b[5],
                    bbox=(b[0], b[1], b[2], b[3]),
                    text=b[4]
                ))
        
        # Collect ALL visual bboxes (images and drawings)
        visual_bboxes = []
        # Images
        for img_info in page.get_image_info():
            visual_bboxes.append(img_info["bbox"])
        # Drawings (vectors)
        for drawing in page.get_drawings():
            visual_bboxes.append(drawing["rect"])
        # Blocks (if any images/vectors are reported there)
        for b in all_raw_blocks:
            if b[6] in (1, 3):
                visual_bboxes.append((b[0], b[1], b[2], b[3]))
        
        return raw_page_text, text_blocks, all_raw_blocks, visual_bboxes

    def close(self):
        self.doc.close()

    @property
    def page_count(self) -> int:
        return len(self.doc)
