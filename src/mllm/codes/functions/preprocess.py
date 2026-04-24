import json
import os
import glob
import argparse
from sklearn.model_selection import train_test_split

def prepare_neuro_dataset(input_dir, output_dir, mode="instruction", test_size=0.1):
    """
    Scans a directory for .txt or .md files and generates JSONL formats for MLX fine-tuning.
    """
    print(f"📂 Scanning for neurophysiology data in: {input_dir}")
    files = glob.glob(os.path.join(input_dir, "**/*.md"), recursive=True) + \
            glob.glob(os.path.join(input_dir, "**/*.txt"), recursive=True)
    
    if not files:
        print("❌ No files found in input directory.")
        return

    data = []
    for f_path in files:
        try:
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            if not content: continue
            
            if mode == "continual":
                data.append({"text": content})
            elif mode == "completion":
                # Heuristic: use first line as prompt, rest as completion
                parts = content.split('\n', 1)
                if len(parts) > 1:
                    data.append({"prompt": parts[0], "completion": parts[1]})
            elif mode == "instruction":
                # Instruction-tuning format with paper name as prompt
                data.append({
                    "messages": [
                        {"role": "user", "content": f"Summarize or explain the neuroscientific findings in: {os.path.basename(f_path)}"},
                        {"role": "assistant", "content": content}
                    ]
                })
            elif mode == "causal_consistency":
                # Aim 1 (Reasoning) -> Aim 2 (Empirical Validation)
                # Expected format: Reasoning: <text> | Empirical: <text> | Consistency: <text>
                if "|" in content:
                    parts = content.split("|")
                    reasoning = parts[0].replace("Reasoning:", "").strip()
                    empirical = parts[1].replace("Empirical:", "").strip()
                    consistency = parts[2].replace("Consistency:", "").strip() if len(parts) > 2 else "Unknown"
                    
                    data.append({
                        "messages": [
                            {"role": "user", "content": f"Analyze the consistency between this causal reasoning and empirical spiking data:\n\nREASONING: {reasoning}\nEMPIRICAL DATA: {empirical}"},
                            {"role": "assistant", "content": f"The reasoning is {consistency} with the empirical data. Explanation: {content}"}
                        ]
                    })
        except Exception as e:
            print(f"  ⚠️ Error processing {f_path}: {e}")

    if not data:
        print("❌ No data successfully processed.")
        return

    train, test = train_test_split(data, test_size=test_size)
    os.makedirs(output_dir, exist_ok=True)
    
    for name, subset in [("train", train), ("valid", test)]:
        output_path = os.path.join(output_dir, f"{name}.jsonl")
        with open(output_path, 'w', encoding='utf-8') as f:
            for entry in subset:
                f.write(json.dumps(entry) + '\n')
    
    print(f"✅ Preprocessing complete. Generated {len(train)} train and {len(test)} valid entries.")
    print(f"📂 Output location: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neuro-LLM Data Preprocessing")
    parser.add_argument("--input", type=str, required=True, help="Input directory for .md/.txt files")
    parser.add_argument("--output", type=str, default="./data", help="Output directory for .jsonl files")
    parser.add_argument("--mode", type=str, choices=["instruction", "continual", "completion", "causal_consistency"], default="instruction")
    args = parser.parse_args()
    
    prepare_neuro_dataset(args.input, args.output, mode=args.mode)
