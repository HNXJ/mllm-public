"""Legacy DeepRead class — parallel VLM-based PDF analysis.

.. deprecated::
    This module is retained for backward compatibility with scripts that
    directly instantiate ``DeepRead``.  The canonical replacement is
    ``mllm.data.loaders.DeepRead`` (in ``src/mllm/data/loaders.py``).
    New code should import from there.

HPC Pipeline Role — Sensory Evidence Pathway
=============================================
``DeepRead`` implements the *sensory evidence gathering* stage of the
Hierarchical Predictive Coding evaluation pipeline.  It converts a raw PDF
(the "stimulus") into a structured per-page representation containing both
OCR-extracted text and VLM-generated figure descriptions (the "bottom-up
prediction error signals").

The class supports **parallel VLM dispatch** across multiple endpoints,
distributing page-segment analysis tasks across available GPU servers.

BUGFIXES applied in this refactoring
-------------------------------------
B4 — ``extract_text``: fitz ``Document`` was never closed; O(N²) string
     concatenation replaced with ``str.join`` over a list comp.
B5 — ``wait_for_ready``: ``/load_model`` POST was sent on every retry
     iteration, spamming the engine control plane.  A ``load_requested``
     flag now ensures at most one load request per wait cycle.
"""

import os
import requests
import json
import base64
import time
import concurrent.futures
from typing import List, Dict, Union, Any


class DeepRead:
    """Parallel VLM-based PDF extractor for scientific papers.

    Splits each page into top/bottom halves, dispatches to one or more VLM
    endpoints for visual description, and yields structured per-page data
    combining text + visual analysis.

    Args:
        vlm_urls: A single VLM endpoint URL or a list of URLs for parallel
                  dispatch.  Each URL should point to a chat-completions
                  compatible endpoint (e.g. ``http://host:port/v1/chat/completions``).
        api_key:  Bearer token for VLM authentication.
    """

    def __init__(self, vlm_urls: Union[str, List[str]], api_key: str):
        if isinstance(vlm_urls, str):
            self.vlm_urls = [vlm_urls]
        else:
            self.vlm_urls = vlm_urls
        self.api_key = api_key
        self.num_workers = len(self.vlm_urls)

    def extract_text(self, pdf_path: str) -> str:
        """Extract raw text from all pages of a PDF.

        BUGFIX (B4): The previous implementation
        (a) never closed the fitz ``Document``, leaking a file descriptor, and
        (b) built the result via ``text += page.get_text()`` which is O(N²)
        for N pages because Python strings are immutable — each ``+=``
        allocates a new string of length ``sum(0..N)``.

        Now uses ``str.join`` over a list comprehension for O(N) construction
        and a ``try/finally`` to guarantee handle release.

        Args:
            pdf_path: Filesystem path to the PDF.

        Returns:
            Concatenated text of all pages.
        """
        import fitz  # PyMuPDF — guarded import to match legacy behaviour.

        doc = fitz.open(pdf_path)
        try:
            # BUGFIX: O(N) join instead of O(N²) concatenation.
            text = "".join([page.get_text() for page in doc])
        finally:
            # BUGFIX: guarantee handle release.
            doc.close()
        return text

    def wait_for_ready(
        self,
        vlm_url: str,
        model_name: str,
        max_retries: int = 10,
    ) -> bool:
        """Wait for the VLM engine to be ready with the target model loaded.

        BUGFIX (B5): Previous implementation posted ``/load_model`` on *every*
        retry iteration.  When the engine takes 30+ seconds to load a 7 B
        model, this caused a cascade of overlapping load requests.
        A ``load_requested`` flag now ensures the load POST fires at most
        once per wait cycle.

        Args:
            vlm_url:     Full chat-completions URL (``/v1/chat/completions``).
            model_name:  Expected model identifier.
            max_retries: Number of polling cycles before giving up.

        Returns:
            ``True`` if the engine reported ``ready`` with the correct model;
            ``False`` if max retries were exhausted.
        """
        status_url = vlm_url.replace("/v1/chat/completions", "/status")
        load_url = vlm_url.replace("/v1/chat/completions", "/load_model")
        headers = {"Authorization": f"Bearer {self.api_key}"}
        # BUGFIX: track whether we've already sent a load request.
        load_requested = False

        for i in range(max_retries):
            try:
                response = requests.get(status_url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if (
                        data.get("status") == "ready"
                        and data.get("current_model") == model_name
                    ):
                        return True
                    # Only request load once — avoid spamming the engine.
                    if data.get("status") != "loading" and not load_requested:
                        requests.post(
                            load_url,
                            json={"model": model_name},
                            headers=headers,
                            timeout=5,
                        )
                        load_requested = True
            except Exception:
                pass
            time.sleep(10)
        return False

    def analyze_single_image(
        self,
        vlm_url: str,
        img_path: str,
        model_name: str,
    ) -> str:
        """Send a single image to a VLM endpoint with retry logic.

        In HPC terminology, this produces the *bottom-up sensory evidence*
        for a single page segment.

        Args:
            vlm_url:    Target VLM endpoint URL.
            img_path:   Path to the image file.
            model_name: Model identifier.

        Returns:
            VLM description text, or an error string if all retries fail.
        """
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if not self.wait_for_ready(vlm_url, model_name, max_retries=5):
                    continue

                with open(img_path, "rb") as f:
                    encoded_image = base64.b64encode(f.read()).decode("utf-8")

                prompt = (
                    "Describe the scientific content of this page segment. "
                    "Identify figures, axes, and key trends. "
                    "Note any predictive coding (HPC) relevance."
                )

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
                    "max_tokens": 500,
                }

                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                }
                response = requests.post(
                    vlm_url, headers=headers, json=payload, timeout=120
                )

                if response.status_code == 200:
                    result = response.json()["choices"][0]["message"]["content"]
                    if result and len(result.strip()) > 10:
                        return result

                time.sleep(5)
            except Exception as e:
                if attempt == max_retries - 1:
                    return (
                        f"*VLM Error ({vlm_url}) after {max_retries} "
                        f"attempts: {str(e)}*"
                    )
                time.sleep(10)

        return f"*VLM Error ({vlm_url}): Maximum retries exceeded.*"

    def process_document_pages(self, pdf_path: str, model_name: str):
        """Generator — process a PDF page-by-page with parallel VLM analysis.

        Each page is split into top/bottom halves.  All segments are submitted
        to a thread pool, distributed round-robin across the available VLM
        URLs, and then yielded in page order.

        Args:
            pdf_path:   Filesystem path to the PDF.
            model_name: VLM model identifier.

        Yields:
            ``dict`` per page with keys ``page_num``, ``total_pages``,
            ``top_visual``, ``bot_visual``, ``text``.
        """
        import fitz

        doc = fitz.open(pdf_path)
        try:
            total_pages = len(doc)

            output_dir = os.path.join(
                os.path.dirname(pdf_path), "temp_vlm_images"
            )
            os.makedirs(output_dir, exist_ok=True)

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.num_workers,
            ) as executor:
                segment_tasks = []  # (page_num, type, img_path)

                for i in range(total_pages):
                    page = doc[i]
                    rect = page.rect
                    mid_y = rect.y1 / 2
                    mat = fitz.Matrix(2, 2)

                    # Top half
                    top_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, mid_y)
                    top_pix = page.get_pixmap(matrix=mat, clip=top_rect)
                    top_path = os.path.join(output_dir, f"p{i + 1}_top.png")
                    top_pix.save(top_path)
                    segment_tasks.append((i + 1, "top", top_path))

                    # Bottom half
                    bot_rect = fitz.Rect(rect.x0, mid_y, rect.x1, rect.y1)
                    bot_pix = page.get_pixmap(matrix=mat, clip=bot_rect)
                    bot_path = os.path.join(output_dir, f"p{i + 1}_bot.png")
                    bot_pix.save(bot_path)
                    segment_tasks.append((i + 1, "bot", bot_path))

                # ---- Distribute across VLM URLs ----
                results_map = {}  # (page_num, type) -> text

                def worker_task(task, url_idx):
                    page_num, seg_type, img_path = task
                    url = self.vlm_urls[url_idx % len(self.vlm_urls)]
                    return (
                        (page_num, seg_type),
                        self.analyze_single_image(url, img_path, model_name),
                    )

                future_to_task = {
                    executor.submit(worker_task, task, i): task
                    for i, task in enumerate(segment_tasks)
                }

                for future in concurrent.futures.as_completed(future_to_task):
                    key, result = future.result()
                    results_map[key] = result

                # Yield in page order (not completion order).
                for i in range(total_pages):
                    page_data = {
                        "page_num": i + 1,
                        "total_pages": total_pages,
                        "top_visual": results_map.get((i + 1, "top"), ""),
                        "bot_visual": results_map.get((i + 1, "bot"), ""),
                        "text": doc[i].get_text(),
                    }
                    yield page_data
        finally:
            doc.close()

    def unify(self, text: str, visuals: str) -> str:
        """Merge raw text and visual descriptions into a single Markdown doc.

        Args:
            text:    Raw OCR/text-layer output.
            visuals: VLM-generated visual descriptions.

        Returns:
            Unified Markdown string.
        """
        return f"# Paper Analysis\n\n{text}\n\n{visuals}"
