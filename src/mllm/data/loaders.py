import os
import re
import base64
import json
import tempfile
import time
import requests
import fitz
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from mllm.utils.logging_utils import setup_logger
logger = setup_logger(__name__)
from mllm.deepread.extractor import PDFExtractor
from mllm.deepread.figure_detector import FigureDetector
from mllm.deepread.vlm_client import VLMClient
from mllm.deepread.interleave import Interleaver
from mllm.deepread.io_utils import save_figure_crop
from mllm.schemas import ExtractedDocumentArtifact

class DeepReadLoader:
    """Canonical loader for 'DeepRead' PDF extraction.

    Provides concurrent extraction of text and visual data from PDFs using
    a VLM-driven sensory pathway. Now powered by mllm.deepread for targeted
    figure analysis.
    """

    def __init__(self, engine_url: str, vlm_model: str, api_key: str='lm-studio', max_workers: int=4, vlm_deepread: bool=True, vlm_engine: str='lms'):
        print('[VERBOSITY] Executing: self.engine_url = engine_url')
        self.engine_url = engine_url
        print('[VERBOSITY] Executing: self.vlm_model = vlm_model')
        self.vlm_model = vlm_model
        print('[VERBOSITY] Executing: self.api_key = api_key')
        self.api_key = api_key
        print('[VERBOSITY] Executing: self.max_workers = max_workers')
        self.max_workers = max_workers
        print('[VERBOSITY] Executing: self.vlm_deepread = vlm_deepread')
        self.vlm_deepread = vlm_deepread
        print('[VERBOSITY] Executing: self.vlm_engine = vlm_engine')
        self.vlm_engine = vlm_engine
        print("[VERBOSITY] Executing: clean_url = engine_url.replace('/v1/chat/completions', ''...")
        clean_url = engine_url.replace('/v1/chat/completions', '').rstrip('/')
        print('[VERBOSITY] Executing: self.detector = FigureDetector(max_figures_per_page=8)')
        self.detector = FigureDetector(max_figures_per_page=8)
        print("[VERBOSITY] Executing: vlm_base_url = f'{clean_url}/v1'")
        vlm_base_url = f'{clean_url}/v1'
        print('[VERBOSITY] Executing: self.vlm_client = VLMClient(base_url=vlm_base_url, api_ke...')
        self.vlm_client = VLMClient(base_url=vlm_base_url, api_key=api_key, model=vlm_model, engine=vlm_engine)
        print('[VERBOSITY] Executing: self.interleaver = Interleaver()')
        self.interleaver = Interleaver()
        print("[VERBOSITY] Executing: if vlm_engine == 'mlx':")
        if vlm_engine == 'mlx':
            self._ensure_vlm_loaded()

    def _ensure_vlm_loaded(self):
        print("[VERBOSITY] Executing: 'Send a load request to the MLLM engine control API.'")
        'Send a load request to the MLLM engine control API.'
        print('[VERBOSITY] Executing: try:')
        try:
            logger.info(f'Sensory Pathway: Requesting load for VLM {self.vlm_model}...')
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.post(f'{self.engine_url}/load_model', json={'model': self.vlm_model}, headers=headers, timeout=300)
            if response.status_code == 200:
                logger.info(f'✅ VLM {self.vlm_model} reported READY by engine.')
            else:
                logger.warning(f'⚠️ VLM load request returned {response.status_code}: {response.text}')
        except Exception as e:
            logger.error(f'❌ Failed to communicate with engine control: {e}')

    def extract_parallel(self, pdf_path: str) -> ExtractedDocumentArtifact:
        print("[VERBOSITY] Executing: 'Perform text and targeted visual extraction for the whol...")
        'Perform text and targeted visual extraction for the whole PDF.'
        print("[VERBOSITY] Executing: logger.info(f'Starting high-fidelity DeepRead extraction ...")
        logger.info(f'Starting high-fidelity DeepRead extraction for: {pdf_path}')
        print('[VERBOSITY] Executing: extractor = PDFExtractor(pdf_path)')
        extractor = PDFExtractor(pdf_path)
        print('[VERBOSITY] Executing: total_pages = extractor.page_count')
        total_pages = extractor.page_count
        print('[VERBOSITY] Executing: all_visual_bboxes = []')
        all_visual_bboxes = []
        print('[VERBOSITY] Executing: for i in range(total_pages):')
        for i in range(total_pages):
            (_, _, _, visual_bboxes) = extractor.extract_page_data(i)
            all_visual_bboxes.append(visual_bboxes)
        print('[VERBOSITY] Executing: known_logos = self._detect_repetitive_bboxes(all_visual_b...')
        known_logos = self._detect_repetitive_bboxes(all_visual_bboxes)
        print('[VERBOSITY] Executing: if known_logos:')
        if known_logos:
            logger.info(f'Detected {len(known_logos)} repetitive visual regions (logos/watermarks) to skip.')
        print('[VERBOSITY] Executing: page_markdowns = []')
        page_markdowns = []
        print('[VERBOSITY] Executing: all_descriptions = []')
        all_descriptions = []
        print('[VERBOSITY] Executing: with tempfile.TemporaryDirectory() as temp_dir:')
        with tempfile.TemporaryDirectory() as temp_dir:
            for i in range(total_pages):
                logger.info(f'Processing page {i + 1}/{total_pages}...')
                (raw_text, text_blocks, all_raw_blocks, visual_bboxes) = extractor.extract_page_data(i)
                figures = []
                if self.vlm_deepread:
                    figures = self.detector.detect_figures(i, all_raw_blocks, visual_bboxes, known_logos=known_logos)
                    for fig in figures:
                        crop_path = os.path.join(temp_dir, f'{fig.figure_id}.png')
                        save_figure_crop(extractor.doc, i, fig.bbox, crop_path)
                        logger.info(f'  Describing figure: {fig.figure_id}')
                        try:
                            fig.description = self.vlm_client.describe_figure(crop_path, fig.caption_text, max_retries=3)
                            all_descriptions.append(fig.description)
                        except Exception as e:
                            logger.error(f'  VLM Error for {fig.figure_id}: {e}')
                            fig.description = f'VLM Error: {e}'
                page_md = self.interleaver.interleave_page(i, text_blocks, figures)
                page_markdowns.append(page_md)
        print('[VERBOSITY] Executing: extractor.close()')
        extractor.close()
        print("[VERBOSITY] Executing: study_text = '\\n\\n---\\n\\n'.join(page_markdowns)")
        study_text = '\n\n---\n\n'.join(page_markdowns)
        print('[VERBOSITY] Executing: word_count = len(study_text.split())')
        word_count = len(study_text.split())
        print('[VERBOSITY] Executing: return ExtractedDocumentArtifact(study_text=study_text, p...')
        return ExtractedDocumentArtifact(study_text=study_text, page_segments=all_descriptions, word_count=word_count, token_count=int(word_count * 1.3), metadata={'source': Path(pdf_path).name, 'pages': total_pages, 'engine': 'mllm.deepread.v2.1'})

    def _detect_repetitive_bboxes(self, all_page_bboxes: List[List[Tuple[float, float, float, float]]]) -> List[Tuple[float, float, float, float]]:
        print("[VERBOSITY] Executing: 'Identifies bboxes that appear at the same coordinates on...")
        'Identifies bboxes that appear at the same coordinates on many pages.'
        print('[VERBOSITY] Executing: if not all_page_bboxes:')
        if not all_page_bboxes:
            return []

        def round_bbox(b):
            print('[VERBOSITY] Executing: return (round(b[0]), round(b[1]), round(b[2]), round(b[3]))')
            return (round(b[0]), round(b[1]), round(b[2]), round(b[3]))
        print('[VERBOSITY] Executing: counts = {}')
        counts = {}
        print('[VERBOSITY] Executing: for page_bboxes in all_page_bboxes:')
        for page_bboxes in all_page_bboxes:
            unique_page_bboxes = set((round_bbox(b) for b in page_bboxes))
            for b in unique_page_bboxes:
                counts[b] = counts.get(b, 0) + 1
        print('[VERBOSITY] Executing: threshold = max(2, len(all_page_bboxes) * 0.2)')
        threshold = max(2, len(all_page_bboxes) * 0.2)
        print('[VERBOSITY] Executing: return [b for (b, count) in counts.items() if count > thr...')
        return [b for (b, count) in counts.items() if count > threshold]