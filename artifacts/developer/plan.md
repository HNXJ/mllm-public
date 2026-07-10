# Developer Plan

## Section 1: Brainstorm
Achieved: Batch visual and layout extraction of all 31 study PDFs with non-standard character cleaning, automated reference stripping, and high-fidelity VLM-generated figure descriptions. Next steps: 1. Set up the evaluation loop processing the 31 unified markdowns through selected LLMs. 2. Implement the prompt compilation step merging the unified markdown with the target instruction and glossary templates. 3. Manage model cards (Ollama/LMS/Cloud endpoints) and save output evaluations to JSON. 4. Populate evaluation tables with NaN placeholders for missing parameters to avoid false zeros.

## Section 2: Execution Plan Table

File | Purpose | Score | Actions | Rules | Edits | Notes | Cautions
--- | --- | --- | --- | --- | --- | --- | ---
src/jmllm/util/helpers.py | Support helpers, character cleaning, and bibliography/references stripping. | 100/100 | 1. Implement remove_references() to parse and strip literature sections. 2. Add robust clean_text() mapping mathematical brackets, typography ligatures, and quote characters to standard ASCII. | Must remain stateless and highly robust. | Completed: reference stripping and character maps. | Ensures clean output layout text without references. | None
src/jmllm/pipeline/loaders.py | PDF layouter and DeepRead extraction loader integrating visual detection. | 100/100 | 1. Apply remove_references and clean_text to layouts. 2. Enable VLM-based deepread figure detection and parallel page extraction. | Handle visual region watermarks dynamically. | Completed: layout cleaning hooks integrated in DeepReadLoader. | Verified end-to-end VLM integration. | None
src/jmllm/pipeline/deepread/vlm_client.py | Encodes image crops and sends visual description requests to active VLM. | 100/100 | 1. Allow 'mlx' alias engine type. 2. Configure OpenAI client endpoints for LMS API. | Provide robust timeouts and retry logic. | Completed: alias resolution and completions client setup. | Verified against local server VLM endpoints. | None
src/jmllm/pipeline/deepread/prompts.py | Prompts configuration template for the visual descriptions. | 100/100 | 1. Enrich prompts to request detailed visual breakdowns, legends, flow directions, and data trends. | Avoid summarizing paper context. | Completed: structured neuroscientific breakdown prompt. | Output descriptions successfully verified on Bastos2012. | None
