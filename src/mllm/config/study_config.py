from pydantic import Field
from pathlib import Path
from typing import Optional
from datetime import datetime
from mllm.config.model_config import BaseConfig

class StudyProfile(BaseConfig):
    """Canonical contract for a scientific study evaluation status."""
    study_id: str = Field(..., description="Unique ID (e.g. Sacramento2018)")
    pdf_path: Path = Field(..., description="Source PDF location")
    
    # Artifact Status
    deepread_path: Optional[Path] = None
    evaluation_path: Optional[Path] = None
    
    # Metadata
    last_updated: datetime = Field(default_factory=datetime.now)
    status: str = Field("pending", description="pending, deepread_done, evaluated, failed")
    error_log: Optional[str] = None

    def update_status(self, new_status: str, error: Optional[str] = None):
        self.status = new_status
        self.error_log = error
        self.last_updated = datetime.now()
