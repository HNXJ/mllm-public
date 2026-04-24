import re
from typing import List, Optional, Tuple
from mllm.deepread.models import TextBlock, FigureRegion

class FigureDetector:
    """Detects figure regions and matching captions on a page."""

    CAPTION_PATTERNS = [
        re.compile(r"^(?:Figure|Fig\.?|Supplementary Figure)\s+\d+", re.IGNORECASE)
    ]

    def __init__(self, max_figures_per_page: int = 8):
        self.max_figures_per_page = max_figures_per_page

    def detect_figures(self, page_index: int, all_raw_blocks: List[tuple], visual_bboxes: List[Tuple[float, float, float, float]], known_logos: List[Tuple[float, float, float, float]] = None) -> List[FigureRegion]:
        """
        Uses image/vector bboxes as anchors and identifies captions to define figure regions.
        """
        text_blocks = [b for b in all_raw_blocks if b[6] == 0]

        if not visual_bboxes:
            return []

        # Filter out tiny visual regions (logos, icons, artifacts)
        # 50x50 area threshold (2500)
        significant_bboxes = [b for b in visual_bboxes if (b[2]-b[0]) * (b[3]-b[1]) > 2500]
        
        # Filter out known logos/watermarks (repetitive regions)
        if known_logos:
            filtered = []
            for b in significant_bboxes:
                is_logo = False
                for logo_bbox in known_logos:
                    if self._calculate_iou(b, logo_bbox) > 0.8:
                        is_logo = True
                        break
                if not is_logo:
                    filtered.append(b)
            significant_bboxes = filtered

        if not significant_bboxes:
            return []

        # Merge overlapping/adjacent visual blocks
        merged_regions = self._merge_visual_blocks(significant_bboxes)
        
        figures = []
        for i, region in enumerate(merged_regions[:self.max_figures_per_page]):
            figure_id = f"page_{page_index:04d}_fig_{i+1:02d}"
            
            # Find caption
            caption_block = self._find_nearest_caption(region['bbox'], text_blocks)
            
            fig_region = FigureRegion(
                page_index=page_index,
                figure_id=figure_id,
                bbox=region['bbox'],
                block_nos=region['block_nos']
            )
            
            if caption_block:
                fig_region.caption_block_no = caption_block[5]
                fig_region.caption_text = caption_block[4].strip()
                
            figures.append(fig_region)
            
        return figures

    def _calculate_iou(self, box1: Tuple[float, float, float, float], box2: Tuple[float, float, float, float]) -> float:
        """Calculates Intersection over Union for two bboxes."""
        x0 = max(box1[0], box2[0])
        y0 = max(box1[1], box2[1])
        x1 = min(box1[2], box2[2])
        y1 = min(box1[3], box2[3])
        
        intersection = max(0, x1 - x0) * max(0, y1 - y0)
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        
        union = area1 + area2 - intersection
        if union <= 0: return 0
        return intersection / union

    def _merge_visual_blocks(self, visual_bboxes: List[Tuple[float, float, float, float]]) -> List[dict]:
        """Simple merging of visual blocks that are vertically close or overlapping."""
        if not visual_bboxes:
            return []

        # Start with individual bboxes
        regions = []
        for i, b in enumerate(visual_bboxes):
            regions.append({
                'bbox': b,
                'block_nos': [i] # These are now indices of significant_bboxes or dummy
            })

        # Basic merge loop: if bboxes overlap or are within 20pt vertically
        changed = True
        while changed:
            changed = False
            new_regions = []
            while regions:
                curr = regions.pop(0)
                merged = False
                for i, other in enumerate(new_regions):
                    if self._should_merge(curr['bbox'], other['bbox']):
                        other['bbox'] = self._union_bbox(curr['bbox'], other['bbox'])
                        other['block_nos'].extend(curr['block_nos'])
                        merged = True
                        changed = True
                        break
                if not merged:
                    new_regions.append(curr)
            regions = new_regions
            
        return regions

    def _should_merge(self, bbox1: Tuple[float, float, float, float], bbox2: Tuple[float, float, float, float]) -> bool:
        # Check for overlap or vertical proximity (within 30 points)
        # (x0, y0, x1, y1)
        # horizontal overlap?
        h_overlap = max(0, min(bbox1[2], bbox2[2]) - max(bbox1[0], bbox2[0])) > 0
        v_dist = min(abs(bbox1[1] - bbox2[3]), abs(bbox2[1] - bbox1[3]))
        
        if h_overlap and v_dist < 30:
            return True
        
        # Simple intersection check
        if (bbox1[0] < bbox2[2] and bbox1[2] > bbox2[0] and
            bbox1[1] < bbox2[3] and bbox1[3] > bbox2[1]):
            return True
            
        return False

    def _union_bbox(self, b1: Tuple[float, float, float, float], b2: Tuple[float, float, float, float]) -> Tuple[float, float, float, float]:
        return (min(b1[0], b2[0]), min(b1[1], b2[1]), max(b1[2], b2[2]), max(b1[3], b2[3]))

    def _find_nearest_caption(self, fig_bbox: Tuple[float, float, float, float], text_blocks: List[tuple]) -> Optional[tuple]:
        """Finds the nearest text block matching caption patterns."""
        captions = []
        for tb in text_blocks:
            text = tb[4].strip()
            if any(p.match(text) for p in self.CAPTION_PATTERNS):
                captions.append(tb)

        if not captions:
            return None

        # Prefer below, then above
        best_cap = None
        min_dist = float('inf')

        for cap in captions:
            cap_bbox = (cap[0], cap[1], cap[2], cap[3])
            
            # Vertical distance from figure bbox
            # If caption is below: cap[1] - fig[3]
            # If caption is above: fig[1] - cap[3]
            
            dist_below = cap_bbox[1] - fig_bbox[3]
            dist_above = fig_bbox[1] - cap_bbox[3]
            
            # Penalize horizontal misalignment
            h_offset = abs((cap_bbox[0] + cap_bbox[2])/2 - (fig_bbox[0] + fig_bbox[2])/2)
            
            if 0 <= dist_below < 100:
                score = dist_below + h_offset * 0.5
                if score < min_dist:
                    min_dist = score
                    best_cap = cap
            elif 0 <= dist_above < 100:
                score = dist_above + 50 + h_offset * 0.5 # Preference for below
                if score < min_dist:
                    min_dist = score
                    best_cap = cap
                    
        return best_cap
