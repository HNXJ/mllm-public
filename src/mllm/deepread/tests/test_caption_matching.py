import pytest
from mllm.deepread.figure_detector import FigureDetector

def test_caption_matching_below():
    detector = FigureDetector()
    # (x0, y0, x1, y1, text, block_no, block_type)
    all_raw_blocks = [
        (100, 100, 200, 200, "Figure 1: Title", 0, 0),
        (100, 10, 200, 100, "", 1, 1) # Figure is above caption
    ]
    visual_bboxes = [(100, 10, 200, 100)]
    figures = detector.detect_figures(0, all_raw_blocks, visual_bboxes)
    assert len(figures) == 1
    assert figures[0].caption_text == "Figure 1: Title"
    assert figures[0].caption_block_no == 0

def test_caption_matching_above():
    detector = FigureDetector()
    all_raw_blocks = [
        (100, 10, 200, 30, "Figure 2. Title", 0, 0), # Caption above
        (100, 40, 200, 140, "", 1, 1)
    ]
    visual_bboxes = [(100, 40, 200, 140)]
    figures = detector.detect_figures(0, all_raw_blocks, visual_bboxes)
    assert len(figures) == 1
    assert figures[0].caption_text == "Figure 2. Title"
    assert figures[0].caption_block_no == 0

def test_merge_visual_blocks():
    detector = FigureDetector()
    all_raw_blocks = [
        (100, 10, 200, 50, "", 0, 1),
        (105, 55, 195, 100, "", 1, 3) # Vector block close to image
    ]
    visual_bboxes = [
        (100, 10, 200, 50),
        (105, 55, 195, 100)
    ]
    figures = detector.detect_figures(0, all_raw_blocks, visual_bboxes)
    assert len(figures) == 1
    assert figures[0].bbox == (100, 10, 200, 100)
