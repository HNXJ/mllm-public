"""Pydantic schemas for HPC evaluation pipeline data contracts.

HPC Pipeline Role — Output Contracts
=====================================
These schemas define the *shape* of every data artefact flowing through
the pipeline.  In Predictive Coding terms:

- ``ExtractedDocumentArtifact`` — the raw sensory input (study text + visuals).
- ``FactorScore`` / ``FactorScoringResponse`` — individual factor predictions
  and their aggregation.
- ``HpcEvaluationResponse`` — the complete hierarchical evaluation with
  separate Local Oddball (LO) and Global Oddball (GO) factor maps.
- ``ReasoningResponse`` — intermediate reasoning chain output.
- ``FinalEvaluationArtifact`` — the fully validated end-product.
- ``ErrorPayload`` — structured error representation.

All schemas use ``ConfigDict(extra='forbid')`` where appropriate to enforce
strict contract adherence — the LLM cannot inject unexpected keys.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ConfigDict

class ExtractedDocumentArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid")
    study_text: str = Field(..., description="The main text content of the study.")
    page_segments: List[str] = Field(default_factory=list, description="Descriptions of visual elements in the study.")
    word_count: int = Field(0, description="Total word count of the extracted text.")
    token_count: int = Field(0, description="Estimated token count (words * 1.3).")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata extracted from the PDF (title, author, etc.).")

class FactorScore(BaseModel):
    factor_name: str = Field(..., description="The name of the factor.")
    score: float = Field(..., description="The score assigned to the factor (typically -1.0 to 1.0).")
    rationale: Optional[str] = Field(None, description="Detailed rationale for the score.")
    evidence: List[str] = Field(default_factory=list, description="Citations or specific text segments as evidence.")

class FactorScoringResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    scores: List[FactorScore] = Field(default_factory=list, description="List of factor scores.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional scoring metadata.")

class HpcEvaluationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    lo_evaluations: Dict[str, Optional[float]] = Field(default_factory=dict)
    go_evaluations: Dict[str, Optional[float]] = Field(default_factory=dict)
    first_author: Optional[str] = None
    publication_year: Optional[str] = None
    study_type: Optional[str] = None
    agent_name: Optional[str] = None
    reasoning_log_text: Optional[str] = None

class ReasoningResponse(BaseModel):
    summary: Optional[str] = Field(None, description="Concise summary of the reasoning.")
    findings: List[Dict[str, Any]] = Field(default_factory=list, description="Structured findings or claims.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Contextual metadata.")

class FinalEvaluationArtifact(BaseModel):
    study_identifier: str = Field(..., description="Identifier for the study being evaluated.")
    overall_assessment: str = Field("N/A", description="A summary assessment of the study based on all factors.")
    detailed_scores: FactorScoringResponse = Field(..., description="The detailed scoring results.")

class ErrorPayload(BaseModel):
    error_code: str = Field(..., description="A unique code identifying the type of error.")
    message: str = Field(..., description="A human-readable description of the error.")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional details about the error.")
