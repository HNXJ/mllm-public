import mlx.core as mx
from mlx_lm import load, generate
import argparse
from pathlib import Path

def run_g_eval(model_path, ocr_path):
    print(f"🚀 Loading Teacher Model (Qwen-Opus): {model_path}")
    model, tokenizer = load(model_path)
    
    print(f"📖 Reading Student Output (OCR): {ocr_path}")
    with open(ocr_path, 'r') as f:
        ocr_content = f.read()
    
    # Selecting Page 1 for the check
    page_1_start = ocr_content.find("## Page 1")
    page_2_start = ocr_content.find("## Page 2")
    student_sample = ocr_content[page_1_start:page_2_start]

    prompt = f"""<|im_start|>system
You are a 'Teacher' model specializing in neuroscience and biophysical engineering. Your task is to perform a G-Eval validation of a 'Student' model's OCR transcription.
Evaluate the following transcription based on:
1. **Scientific Factualness**: Does the text preserve the technical accuracy of neuroscience terms and citations?
2. **Logical Consistency**: Is the flow of the transcribed argument coherent and free of structural hallucinations?

Output your evaluation in this format:
- **Factualness Score (1-5)**: [Score]
- **Consistency Score (1-5)**: [Score]
- **Justification**: [Brief technical rationale]
<|im_end|>
<|im_start|>user
Student OCR Output Sample:
\"\"\"
{student_sample}
\"\"\"

Please evaluate the sample above.
<|im_end|>
<|im_start|>assistant
"""

    print("🧠 Teacher is evaluating...")
    print("-" * 30)
    response = generate(model, tokenizer, prompt=prompt, max_tokens=1000, verbose=True)
    print("-" * 30)
    
    return response

if __name__ == "__main__":
    MODEL = "./workspace/Warehouse/mlx_models/Qwen3.5-27B-Opus-Reasoning-6bit"
    OCR = "misc/papers/markdowns/Nitzan2025Omission_ocr.md"
    
    run_g_eval(MODEL, OCR)
