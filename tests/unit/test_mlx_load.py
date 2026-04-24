import pytest

pytestmark = pytest.mark.hardware
pytest.skip("Manual hardware-specific MLX load test", allow_module_level=True)
