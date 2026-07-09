from pydantic import BaseModel
from typing import Literal, Optional, List, Tuple

class TextBlock(BaseModel):
    page_index: int
    block_no: int
    bbox: Tuple[float, float, float, float]
    text: str

class FigureRegion(BaseModel):
    page_index: int
    figure_id: str
    bbox: Tuple[float, float, float, float]
    block_nos: List[int]
    caption_block_no: Optional[int] = None
    caption_text: Optional[str] = None
    image_path: Optional[str] = None
    description: Optional[str] = None

class PageAssembly(BaseModel):
    page_index: int
    raw_page_text: str
    text_blocks: List[TextBlock]
    figures: List[FigureRegion]
    markdown: str
