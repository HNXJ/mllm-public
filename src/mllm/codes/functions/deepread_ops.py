"""DeepRead operations for PDF text extraction and VLM-based visual analysis.

HPC Pipeline Role — Sensory Input Layer
========================================
In the Hierarchical Predictive Coding (HPC) architecture, this module serves
as the **bottom-up sensory pathway**.  It converts raw PDF documents (the
"stimulus") into unified markdown representations that combine textual content
with VLM-generated figure descriptions.  The resulting artefact feeds directly
into the reasoning/evaluation phase where LLM agents score HPC factors.

Functions
---------
- ``extract_pdf_to_md``   — Raw text extraction (PyMuPDF).
- ``vision_extraction_orchestrator`` — Page-level VLM figure description.
- ``deepread_validation``  — Word-count sanity gate between raw and unified.
- ``get_pdf_page_text``    — Single-page text retrieval.
- ``get_pdf_page_shot``    — Split-page screenshot generation (top/bottom).
- ``get_vlm_describe``     — Single-image VLM description with retries.

DEPRECATION NOTE
----------------
This module lives in the legacy ``codes/functions/`` directory.  The canonical
replacement is ``mllm.data.loaders.DeepRead``.  New callers should prefer that
API.  This file is retained because ``mllm-pipeline.py`` and
``run_mllm_pipeline_unified_office.py`` still import from here directly.
"""

import os
import re
import fitz  # PyMuPDF
import base64
import json
import time
import tempfile
import requests
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional


# ---------------------------------------------------------------------------
# Single-page helpers
# ---------------------------------------------------------------------------

def get_pdf_page_text(pdf_path: str, page_num: int) -> str:
    """Extract raw text from a single PDF page.

    BUGFIX: Previous implementation leaked the fitz ``Document`` handle on
    every call — one OS file-descriptor per invocation, accumulating to ~40
    leaked handles for a 20-page paper processed via top/bottom splits.

    Args:
        pdf_path: Filesystem path to the PDF.
        page_num: Zero-indexed page number.

    Returns:
        UTF-8 text content of the page, or empty string if ``page_num``
        is out of range.
    """
    doc = fitz.open(pdf_path)
    try:
        if page_num < 0 or page_num >= len(doc):
            return ""
        return doc[page_num].get_text()
    finally:
        # BUGFIX: guarantee handle release regardless of return path.
        doc.close()


def get_pdf_page_shot(
    pdf_path: str,
    page_num: int,
    output_dir: str,
) -> Tuple[str, str]:
    """Render a PDF page as two half-page PNG screenshots (top & bottom).

    The page is split at the vertical midpoint and rendered at 2× resolution
    to preserve figure detail for downstream VLM analysis.

    BUGFIX: Previous implementation never closed the fitz ``Document``.

    Args:
        pdf_path:   Filesystem path to the PDF.
        page_num:   Zero-indexed page number.
        output_dir: Directory to write the PNG files into (created if absent).

    Returns:
        Tuple of (top_image_path, bottom_image_path).
    """
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    try:
        page = doc[page_num]
        rect = page.rect
        mid_y = rect.y1 / 2
        mat = fitz.Matrix(2, 2)  # 2× zoom for VLM-grade resolution

        # --- Top half ---
        top_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, mid_y)
        top_pix = page.get_pixmap(matrix=mat, clip=top_rect)
        top_path = os.path.join(output_dir, f"p{page_num}_top.png")
        top_pix.save(top_path)

        # --- Bottom half ---
        bot_rect = fitz.Rect(rect.x0, mid_y, rect.x1, rect.y1)
        bot_pix = page.get_pixmap(matrix=mat, clip=bot_rect)
        bot_path = os.path.join(output_dir, f"p{page_num}_bot.png")
        bot_pix.save(bot_path)

        return top_path, bot_path
    finally:
        doc.close()


# ---------------------------------------------------------------------------
# VLM communication
# ---------------------------------------------------------------------------

def get_vlm_describe(
    image_path: str,
    prompt: str,
    vlm_url: str,
    model_name: str,
    api_key: str,
    max_retries: int = 5,
    timeout: int = 180,
) -> str:
    """Send an image to a VLM endpoint and retrieve a textual description.

    In HPC terms this is the *bottom-up prediction error signal* — the VLM
    extracts what is actually present in a figure (the "sensory evidence")
    which later gets compared against the LLM's top-down expectations.

    BUGFIX: Bare ``except:`` replaced with ``except Exception:`` so that
    ``KeyboardInterrupt`` and ``SystemExit`` propagate correctly.

    OPTIMISATION: Base64 encoding moved outside the retry loop — the image
    bytes don't change between attempts, so re-encoding was pure waste.

    Args:
        image_path:  Path to the image file (PNG/JPEG).
        prompt:      Natural-language instruction for the VLM.
        vlm_url:     Full URL of the VLM chat-completions endpoint.
        model_name:  Model identifier string for the payload.
        api_key:     Bearer token for authentication.
        max_retries: Maximum number of retry attempts (default 5).
        timeout:     HTTP request timeout in seconds per attempt (default 180).

    Returns:
        VLM response text, or empty string on total failure.
    """
    # OPTIMISATION: encode once, reuse across retries.
    with open(image_path, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}",
                        },
                    },
                ],
            }
        ],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(max_retries):
        try:
            res = requests.post(
                vlm_url, headers=headers, json=payload, timeout=timeout
            )
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
            time.sleep(5)
        except Exception:
            # BUGFIX: was bare ``except:`` which swallowed KeyboardInterrupt.
            time.sleep(10)
    return ""


# ---------------------------------------------------------------------------
# Full-document extraction
# ---------------------------------------------------------------------------

def extract_pdf_to_md(pdf_path: Path, output_md: Path) -> str:
    """Extract raw text from every page of a PDF and write it as Markdown.

    Each page is delimited with a ``--- PAGE N ---`` separator to preserve
    positional context for downstream HPC factor evaluation.

    OPTIMISATION: Uses a generator expression fed to ``str.join`` instead of
    materialising a full list of page strings.  Memory overhead drops from
    O(pages) to O(1) for the join buffer.

    Args:
        pdf_path:  Path to the source PDF.
        output_md: Path for the output Markdown file.

    Returns:
        The full extracted text as a string.
    """
    doc = fitz.open(pdf_path)
    try:
        # OPTIMISATION: generator avoids intermediate list allocation.
        text = "\n".join(
            f"\n--- PAGE {p.number + 1} ---\n" + p.get_text()
            for p in doc
        )
    finally:
        doc.close()

    text = re.sub(r"\n+", "\n", text)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    with open(output_md, "w") as f:
        f.write(text)
    return text


def vision_extraction_orchestrator(
    pdf_path: Path,
    vlm_url: str,
    model_name: str,
    api_key: str,
    output_md: Path,
) -> str:
    """Orchestrate VLM-based figure/table extraction for an entire PDF.

    Iterates through every page that contains embedded images or references
    to ``Figure``, ``Table``, or ``Fig.`` and sends a full-page 2× render to
    the VLM for description.

    BUGFIX: Replaced hardcoded ``/tmp/vlm_p{n}.jpg`` with ``tempfile.mkstemp``
    for portability and to eliminate name collisions under concurrent runs.
    Cleanup now happens in a ``finally`` block to prevent temp-file leaks.

    Args:
        pdf_path:   Path to the source PDF.
        vlm_url:    Full VLM chat-completions URL.
        model_name: VLM model identifier.
        api_key:    Bearer token.
        output_md:  Path for the output visual-description Markdown.

    Returns:
        The assembled visual-description Markdown as a string.
    """
    content = "# Visual Data Extraction\n\n"
    doc = fitz.open(pdf_path)
    try:
        for page in doc:
            has_images = len(page.get_images()) > 0
            has_fig_ref = re.search(
                r"(Figure|Table|Fig\.)\s+\d+", page.get_text(), re.I
            )
            if not (has_images or has_fig_ref):
                continue

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            # BUGFIX: use tempfile instead of hardcoded /tmp path.
            fd, tmp_img = tempfile.mkstemp(
                suffix=".jpg", prefix=f"vlm_p{page.number}_"
            )
            os.close(fd)  # mkstemp opens the fd; we just need the path.
            try:
                pix.save(tmp_img)
                desc = get_vlm_describe(
                    tmp_img,
                    "Describe any figures or tables on this page.",
                    vlm_url,
                    model_name,
                    api_key,
                )
                if desc:
                    content += f"## Page {page.number + 1}\n{desc}\n\n"
            finally:
                # Guarantee cleanup even if VLM call raises.
                if os.path.exists(tmp_img):
                    os.remove(tmp_img)
    finally:
        doc.close()

    with open(output_md, "w") as f:
        f.write(content)
    return content


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def deepread_validation(unified_text: str, raw_text: str) -> bool:
    """Validate that the DeepRead output is reasonably complete.

    Acts as a *precision gate* in the HPC pipeline: if the unified text
    (raw + VLM descriptions) is significantly shorter than the raw text,
    the VLM extraction likely failed or was truncated.  A minimum absolute
    word count guards against pathologically short papers.

    Args:
        unified_text: The combined raw-text + VLM-description Markdown.
        raw_text:     The raw text-only extraction (baseline).

    Returns:
        ``True`` if the unified text passes both the ratio and absolute
        word-count thresholds; ``False`` otherwise.
    """
    unified_words = len(unified_text.split())
    raw_words = len(raw_text.split())

    # Heuristic: unified (including VLM additions) should retain ≥80 % of
    # the raw content.  Some loss is acceptable from whitespace normalisation.
    if unified_words < raw_words * 0.8:
        return False
    # Absolute floor — a scientific paper should produce ≥500 words of text.
    if unified_words < 500:
        return False
    return True
