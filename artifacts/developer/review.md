# Developer Review

## Section 1: Review Summary
Reviewed extraction codebase status. All core files (helpers, loaders, vlm_client, prompts) are fully complete, verified, and test-passed under the batch VLM run.

## Section 2: Codebase Evaluation Table

File | Purpose | Score | Assessment | Warnings | Design Choices | Notes | Cautions
--- | --- | --- | --- | --- | --- | --- | ---
src/jmllm/util/helpers.py | Support helpers, character cleaning, and bibliography/references stripping. | 100/100 | Completed: character cleaning maps and bibliography/references stripping. | Ensure regex patterns remain broad enough to match different references headings. | Decoupled text post-processing from the layout loader. | Verified regex matches and standard-ASCII conversion maps. | None
src/jmllm/pipeline/loaders.py | PDF layouter and DeepRead extraction loader integrating visual detection. | 100/100 | Completed: layout cleaning hooks integrated in DeepReadLoader. | None | Separated text layout and figure descriptions before interleaving them. | Verified end-to-end VLM integration. | None
src/jmllm/pipeline/deepread/vlm_client.py | Encodes image crops and sends visual description requests to active VLM. | 100/100 | Completed: alias resolution and completions client setup. | Ensure timeout matches local generation constraints. | Reuses the LMS OpenAI completions backend under 'mlx' alias. | Verified against local server VLM endpoints. | None
src/jmllm/pipeline/deepread/prompts.py | Prompts configuration template for the visual descriptions. | 100/100 | Completed: structured neuroscientific breakdown prompt. | Avoid adding paper-level summaries in instructions. | Requested layout, symbols, keys, and trends separately. | Output descriptions successfully verified on Bastos2012. | None
