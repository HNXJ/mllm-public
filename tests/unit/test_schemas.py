from mllm.schemas import FactorScoringResponse, HpcEvaluationResponse


def test_factor_scoring_response_validates():
    payload = {
        "scores": [
            {"factor_name": "clarity", "score": 1.0, "rationale": "Clear writing"}
        ]
    }
    validated = FactorScoringResponse.model_validate(payload)
    assert len(validated.scores) == 1
    assert validated.scores[0].factor_name == "clarity"

def test_hpc_evaluation_response_accepts_null_scores():
    payload = {
        "lo_evaluations": {"Factor1": None},
        "go_evaluations": {"Factor1": 0.5},
        "first_author": None,
        "publication_year": "2012",
        "study_type": "Empirical",
        "agent_name": "model",
        "reasoning_log_text": "Concise rationale.",
    }
    validated = HpcEvaluationResponse.model_validate(payload)
    assert validated.lo_evaluations["Factor1"] is None
    assert validated.go_evaluations["Factor1"] == 0.5
