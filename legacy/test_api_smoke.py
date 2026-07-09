import jmllm

print("1. Setting up paths...")
jmllm.set_instructions("ontology/instructions/hpc_eval_prompt.md")
jmllm.set_glossary("ontology/glossary/HPC/hpc-36-reference.md")
jmllm.set_path("content")

print("2. Registering model...")
jmllm.add_model(
    name="gemma-4-e4b-it-mxfp8",
    url="http://localhost:1234",
    temperature=0.7,
    context_window=128000,
    top_p=0.95,
    min_p=0.05
)

# Clean outputs to force concurrent re-evaluation
import pathlib
for paper in ["Bastos2012", "RaoBallard1999"]:
    out_eval = pathlib.Path(f"content/outputs/{paper}_gemma-4-e4b-it-mxfp8_HPC_run1.json")
    if out_eval.exists():
        out_eval.unlink()
        print(f"Cleaned {paper} JSON output to force re-evaluation.")

print("3. Running pipeline concurrently...")
jmllm.run(inputs=["Bastos2012.pdf", "RaoBallard1999.pdf"], parallel_workers=2)

print("4. Running visualizations...")
jmllm.visualize()

print("🎉 API Smoke test completed successfully!")
