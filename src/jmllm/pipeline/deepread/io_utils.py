import os
import fitz
from PIL import Image
from typing import Tuple
from pathlib import Path

def save_figure_crop(doc: fitz.Document, page_index: int, bbox: Tuple[float, float, float, float], output_path: str, dpi: int = 200):
    """Renders a page, crops to the bbox, and saves the image."""
    page = doc[page_index]
    
    # Scale factor for DPI
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    
    # Define the crop area with a small padding
    padding = 12
    x0, y0, x1, y1 = bbox
    crop_bbox = fitz.Rect(
        max(0, x0 - padding),
        max(0, y0 - padding),
        min(page.rect.width, x1 + padding),
        min(page.rect.height, y1 + padding)
    )
    
    # Render the cropped area
    pix = page.get_pixmap(matrix=mat, clip=crop_bbox)
    
    # Save using PIL for better control/format
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    
    return output_path
