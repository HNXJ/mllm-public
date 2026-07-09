# DEPRECATED: LLM interaction and orchestration logic has been migrated to canonical modules in src/mllm/models/llm_wrapper.py and src/mllm/prompts.py.
# This file is retained for legacy compatibility and will be removed in a future release.

import logging
from typing import List, Dict, Any

logger = logging.getLogger("mllm-llm-ops")

# NOTE: The functions get_study_glossary_instructions, get_llm_thinking,
# score_factors_batch, and parallel_scoring_orchestrator have been migrated or
# replaced by more robust implementations in src/mllm/models/llm_wrapper.py
# and src/mllm/prompts.py.
# This file is retained for backward compatibility. Ensure code is updated to use
# the canonical functions.

# If specific backward compatibility wrappers are needed, they can be added here.
# For now, we assume the removal of the actual function code.
