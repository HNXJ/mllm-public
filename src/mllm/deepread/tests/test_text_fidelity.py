import pytest
from mllm.deepread.models import TextBlock
from mllm.deepread.verify import verify_text_fidelity

def test_verify_text_fidelity_success():
    blocks = [
        TextBlock(page_index=0, block_no=0, bbox=(0, 0, 100, 20), text="Hello World"),
        TextBlock(page_index=0, block_no=1, bbox=(0, 30, 100, 50), text="This is a test.")
    ]
    md = "## Page 1\n\nHello World\n\nThis is a test.\n"
    assert verify_text_fidelity(blocks, md) is True

def test_verify_text_fidelity_with_figures():
    blocks = [
        TextBlock(page_index=0, block_no=0, bbox=(0, 0, 100, 20), text="Hello World"),
        TextBlock(page_index=0, block_no=1, bbox=(0, 30, 100, 50), text="This is a test.")
    ]
    md = "## Page 1\n\nHello World\n\n> Figure caption (from PDF text): Fig 1.\n> Figure description (generated): Some description.\n\nThis is a test.\n"
    assert verify_text_fidelity(blocks, md) is True

def test_verify_text_fidelity_failure():
    blocks = [
        TextBlock(page_index=0, block_no=0, bbox=(0, 0, 100, 20), text="Hello World"),
        TextBlock(page_index=0, block_no=1, bbox=(0, 30, 100, 50), text="This is a test.")
    ]
    md = "## Page 1\n\nHello World\n\nChanged text.\n"
    assert verify_text_fidelity(blocks, md) is False
