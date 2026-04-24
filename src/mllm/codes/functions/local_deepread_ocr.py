import os
import sys
import json
import time
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import mlx.core as mx
from mlx_vlm import load, generate

def pdf_to_images(pdf_path, temp_dir):
    """Converts PDF pages to temporary images for OCR."""
    pdf_path = Path(pdf_path)
    temp_dir = Path(temp_dir)
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    image_paths = []
    
    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # 2x zoom for better OCR
        img_path = temp_dir / f"{pdf_path.stem}_p{i+1}.png"
        pix.save(str(img_path))
        image_paths.append(img_path)
        
    doc.close()
    return image_paths

def run_local_ocr(model_path, pdf_path, output_dir):
    """Runs OCR on each page using a local MLX vision model."""
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    temp_dir = Path("misc/papers/temp_images")
    image_paths = pdf_to_images(pdf_path, temp_dir)
    
    print(f"🚀 Loading Vision Model: {model_path}")
    model, processor = load(model_path)
    
    full_markdown = f"# OCR Analysis: {pdf_path.stem}\n\n"
    
    # SYSTEM PROMPT to enforce strict OCR
    system_prompt = "You are a professional OCR engine. Your task is to transcribe the provided image of a scientific paper into high-fidelity Markdown. Output ONLY the Markdown content. Do not include any commentary, thoughts, or explanations. Start immediately with the transcription."

    for i, img_path in enumerate(image_paths):
        print(f"📸 Processing Page {i+1}/{len(image_paths)}...")
        
        # User prompt
        user_content = [
            {"type": "image"},
            {"type": "text", "text": "Transcribe this page into Markdown exactly as it appears. No meta-commentary."}
        ]
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
        
        # Apply chat template
        prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        try:
            # Manually process inputs and convert to MLX
            img = Image.open(img_path)
            inputs = processor(text=prompt, images=img, return_tensors="pt")
            
            # Convert torch tensors to mlx arrays
            mlx_inputs = {
                "input_ids": mx.array(inputs["input_ids"].numpy()),
                "pixel_values": mx.array(inputs["pixel_values"].numpy()),
                "attention_mask": mx.array(inputs["attention_mask"].numpy())
            }
            if "image_grid_thw" in inputs:
                mlx_inputs["image_grid_thw"] = mx.array(inputs["image_grid_thw"].numpy())

            response = generate(
                model, 
                processor, 
                prompt,
                str(img_path), 
                max_tokens=2048, 
                verbose=False,
                **mlx_inputs
            )
            text_out = response.text if hasattr(response, 'text') else str(response)
            
            # Simple cleanup if it still produces "The user wants..."
            if "wants me to" in text_out[:100].lower() or "analyze the image" in text_out[:100].lower():
                # Try to extract the markdown part if it's trapped in a code block or something
                # But usually, it just outputs text. Let's just append and check.
                pass

            full_markdown += f"## Page {i+1}\n\n{text_out}\n\n---\n\n"
        except Exception as e:
            print(f"❌ Error on page {i+1}: {e}")
            full_markdown += f"## Page {i+1}\n\n[OCR Failed for this page: {e}]\n\n---\n\n"

    output_path = output_dir / f"{pdf_path.stem}_ocr.md"
    with open(output_path, "w") as f:
        f.write(full_markdown)
        
    print(f"✅ OCR Complete! Saved to {output_path}")
    return output_path

if __name__ == "__main__":
    MODEL = "./workspace/mlx_models/Qwen3.5-9B-8bit"
    PDF = "misc/papers/queue_papers/Nitzan2025Omission.pdf"
    OUT = "misc/papers/markdowns"
    
    run_local_ocr(MODEL, PDF, OUT)
