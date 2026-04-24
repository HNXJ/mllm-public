import os
import json
import argparse
from pathlib import Path
from rich import print
from typing import Optional

from mllm.deepread.extractor import PDFExtractor
from mllm.deepread.figure_detector import FigureDetector
from mllm.deepread.vlm_client import VLMClient
from mllm.deepread.interleave import Interleaver
from mllm.deepread.io_utils import save_figure_crop
from mllm.deepread.verify import verify_text_fidelity
from mllm.deepread.models import PageAssembly

def main():
    parser = argparse.ArgumentParser(description="DeepRead: PDF to Markdown extraction with VLM-based figure description.")
    parser.add_argument("pdf_path", help="Path to input PDF")
    parser.add_argument("--output", "-o", required=True, help="Path to output Markdown")
    parser.add_argument("--model", default="qwen3.5-vl-4b", help="VLM model ID")
    parser.add_argument("--base-url", default="http://localhost:1234/v1", help="VLM API base URL")
    parser.add_argument("--api-key", default="lm-studio", help="VLM API key")
    parser.add_argument("--dpi", type=int, default=200, help="DPI for figure crops")
    parser.add_argument("--max-figures-per-page", type=int, default=8, help="Max figures per page")
    parser.add_argument("--dump-debug-dir", help="Directory to save crops and manifests")
    parser.add_argument("--emit-json-manifest", help="Path for JSON sidecar manifest")
    parser.add_argument("--strict", action="store_true", help="Fail if model doesn't match qwen3.5-vl prefix")

    args = parser.parse_args()

    pdf_path_obj = Path(args.pdf_path)
    output_obj = Path(args.output)
    dump_debug_dir_obj = Path(args.dump_debug_dir) if args.dump_debug_dir else None
    emit_json_manifest_obj = Path(args.emit_json_manifest) if args.emit_json_manifest else None

    if not pdf_path_obj.exists():
        print(f"[bold red]Error:[/bold red] PDF not found: {args.pdf_path}")
        return

    extractor = PDFExtractor(str(args.pdf_path))
    detector = FigureDetector(max_figures_per_page=args.max_figures_per_page)
    vlm = VLMClient(base_url=args.base_url, api_key=args.api_key, model=args.model, strict=args.strict)
    interleaver = Interleaver()
    
    page_assemblies = []
    full_markdown = []

    print(f"[bold blue]DeepRead Processing:[/bold blue] {pdf_path_obj.name} ({extractor.page_count} pages)")

    for i in range(extractor.page_count):
        print(f"  [cyan]Page {i+1}/{extractor.page_count}...[/cyan]")
        
        # 1. Extract
        raw_text, text_blocks, all_raw_blocks, visual_bboxes = extractor.extract_page_data(i)
        
        # 2. Detect figures
        figures = detector.detect_figures(i, all_raw_blocks, visual_bboxes)
        
        # 3. Crop and Describe figures
        for fig in figures:
            fig_path = f"{fig.figure_id}.png"
            if dump_debug_dir_obj:
                os.makedirs(dump_debug_dir_obj, exist_ok=True)
                fig_path = str(dump_debug_dir_obj / fig_path)
            else:
                os.makedirs(".deepread_tmp", exist_ok=True)
                fig_path = str(Path(".deepread_tmp") / fig_path)
            
            save_figure_crop(extractor.doc, i, fig.bbox, fig_path, dpi=args.dpi)
            fig.image_path = fig_path
            
            print(f"    [dim]Describing figure: {fig.figure_id}[/dim]")
            try:
                fig.description = vlm.describe_figure(fig_path, fig.caption_text)
            except Exception as e:
                print(f"    [red]VLM Error for {fig.figure_id}: {e}[/red]")
                fig.description = f"VLM Error: {e}"

        # 4. Interleave
        page_md = interleaver.interleave_page(i, text_blocks, figures)
        
        # 5. Verify page
        if not verify_text_fidelity(text_blocks, page_md):
            print(f"    [bold red]Warning:[/bold red] Text fidelity verification failed for page {i+1}!")

        # Save for manifest
        page_assemblies.append(PageAssembly(
            page_index=i,
            raw_page_text=raw_text,
            text_blocks=text_blocks,
            figures=figures,
            markdown=page_md
        ))
        full_markdown.append(page_md)

    # Final Save
    os.makedirs(output_obj.parent, exist_ok=True)
    with open(output_obj, "w") as f:
        f.write("\n\n---\n\n".join(full_markdown))
    
    print(f"[bold green]Done![/bold green] Output saved to: {output_obj}")

    if emit_json_manifest_obj:
        manifest = {
            "input_pdf": str(args.pdf_path),
            "model_name": args.model,
            "page_count": extractor.page_count,
            "pages": [pa.model_dump() for pa in page_assemblies]
        }
        os.makedirs(emit_json_manifest_obj.parent, exist_ok=True)
        with open(emit_json_manifest_obj, "w") as f:
            json.dump(manifest, f, indent=2)
        print(f"[dim]Manifest saved to: {emit_json_manifest_obj}[/dim]")

    extractor.close()

if __name__ == "__main__":
    main()
