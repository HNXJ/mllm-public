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
    context_window=128000
)

# Clean output for Bastos2012 to make sure it runs the reasoning phase programmatically
import pathlib
out_eval = pathlib.Path("content/outputs/Bastos2012_gemma-4-e4b-it-mxfp8_HPC_run1.json")
if out_eval.exists():
    out_eval.unlink()
    print("Cleaned Bastos2012 JSON output to force re-evaluation.")

print("3. Running pipeline...")
jmllm.run(inputs=["Bastos2012.pdf"])

print("4. Running visualizations...")
jmllm.visualize()

print("🎉 API Smoke test completed successfully!")
