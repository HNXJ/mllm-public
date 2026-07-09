# DEPRECATED: Prompt building logic has been migrated to src/mllm/prompts.py.
# This file is for legacy compatibility and will be removed in a future release.

import re
from pathlib import Path

# NOTE: The functions parse_glossary and build_hpc_prompt have been moved to src/mllm/prompts.py.
# This file is retained for backward compatibility with existing scripts that may directly import them.
# Ensure that any code directly using these functions is updated to import from the new canonical location.

# If specific backward compatibility wrappers are needed, they can be added here.
# For now, we assume the removal of the actual function code.