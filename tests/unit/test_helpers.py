import tempfile
import json
import pytest
from pathlib import Path
from jmllm.util.helpers import (
    parse_llm_output_as_json,
    extract_json_block,
    calculate_pdf_hash,
    clean_text,
    compress_prompt
)

def test_extract_json_block():
    text_with_json = 'Here is the raw response: {\n  "scores": [1, 2, 3]\n} Hope this is helpful.'
    assert extract_json_block(text_with_json) == '{\n  "scores": [1, 2, 3]\n}'

    text_with_nested = 'Pre {"outer": {"inner": [1, 2]}} Post'
    assert extract_json_block(text_with_nested) == '{"outer": {"inner": [1, 2]}}'

    # Tricky brackets in string
    tricky_brackets = 'Some text {"msg": "this is a {test}"} suffix'
    assert extract_json_block(tricky_brackets) == '{"msg": "this is a {test}"}'

    # Invalid brace matching
    assert extract_json_block("No json here") == ""

def test_parse_llm_output_as_json():
    # Surrounding text rescue
    text = 'Some intro text.\n{\n  "scores": {"LO": 10, "GO": 20}\n}\nSome outro text.'
    parsed = parse_llm_output_as_json(text, compatibility_mode=True)
    assert parsed == {"scores": {"LO": 10, "GO": 20}}

def test_calculate_pdf_hash():
    with tempfile.NamedTemporaryFile("wb", delete=False) as tmp:
        tmp.write(b"Hello PDF Content")
        tmp_name = tmp.name
        
    try:
        pdf_hash = calculate_pdf_hash(tmp_name)
        assert len(pdf_hash) == 32
        # Verify it computes same hash
        assert calculate_pdf_hash(tmp_name) == pdf_hash
    finally:
        Path(tmp_name).unlink()

def test_clean_text():
    raw_text = "ð10Þ ﬁrst ﬂow – en-dash — em-dash ’smart’ ”quotes”"
    cleaned = clean_text(raw_text)
    assert cleaned == '(10) first flow - en-dash - em-dash \'smart\' "quotes"'

def test_compress_prompt():
    prompt = (
        "Role: R\n"
        "## Methods\n"
        + "Detailed methods text " * 50 + "\n"
        "## Discussion\n"
        + "Detailed discussion text " * 50 + "\n"
        "## Results\n"
        "Keep this results text intact.\n"
    )
    # Original prompt has >300 tokens. Setting limit to 100 should compress Methods/Discussion
    # but preserve the rest, without triggering hard truncation.
    compressed = compress_prompt(prompt, max_tokens=100)
    assert "truncated" in compressed
    assert "Results" in compressed
    assert "Keep this results text intact." in compressed

def test_deepread_loader_caching():
    from unittest.mock import patch, MagicMock
    from jmllm.pipeline.loaders import DeepReadLoader
    from jmllm.util.schemas import ExtractedDocumentArtifact

    with tempfile.TemporaryDirectory() as tmp_dir:
        mock_hash = "abc123mockhash"
        
        # Override the path resolution by patching Path inside loaders.py
        with patch("jmllm.pipeline.loaders.calculate_pdf_hash", return_value=mock_hash), \
             patch("jmllm.pipeline.loaders.Path") as mock_path_cls:
             
            real_path = Path(tmp_dir)
            mock_path_cls.return_value = real_path
            
            mock_extractor = MagicMock()
            mock_extractor.page_count = 1
            mock_extractor.extract_page_data.return_value = (
                "Page text",
                [],
                [],
                []
            )
            
            with patch("jmllm.pipeline.loaders.PDFExtractor", return_value=mock_extractor):
                loader = DeepReadLoader(
                    engine_url="http://localhost:1234",
                    vlm_model="mock-vlm",
                    vlm_deepread=False
                )
                
                # First run: cache miss, extracts via PDFExtractor
                art = loader.extract_parallel("mock.pdf")
                assert "Page 1" in art.study_text
                assert mock_extractor.extract_page_data.called
                
                # Reset mock
                mock_extractor.extract_page_data.reset_mock()
                
                # Second run: cache hit, should load from cache directly without calling extractor
                art_cached = loader.extract_parallel("mock.pdf")
                assert "Page 1" in art_cached.study_text
                assert not mock_extractor.extract_page_data.called

