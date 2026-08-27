# Human+AI Workflow Order & Re-Test Robustness Report

## Summary & Methodological Framing

This report documents the procedural test–retest stability of the **Human+AI evaluation workflow** across two distinct reading passes:
- **`hpchai_01` (Pass 1 - Forward)**: Canonical 1 $\longrightarrow$ 31 order (initial contextual state).
- **`hpchai_02` (Pass 2 - Reverse)**: Reverse 31 $\longrightarrow$ 1 order under cumulative contextual synthesis.

> **Methodological Note on Validation Strata**:
> These passes represent repeated evaluations using the same Human+AI methodology under perturbed reading sequences. They quantify **procedural order robustness**, not inter-rater reliability among independent domain experts (`hpch_01`, `hpch_02`, `hpch_03`).

---

## 1. Measured Procedural Agreement Metrics

Across $N = 239$ jointly scored factor slots (clustered within 31 papers):

| Metric | Measured Value | Descriptive Interpretation |
| :--- | :---: | :--- |
| **Pearson Correlation ($r$)** | **0.7669** | Substantial positive linear alignment across reading directions. |
| **Mean Absolute Error (MAE)** | **0.1305** | Bounded absolute deviation on the $[-1.0, +1.0]$ score scale. |
| **Directional Sign Concordance** | **96.23%** | 230 / 239 jointly scored slots agree in polarity ($+$, $-$, or $0$). |
| **Mean Squared Deviation (MSD)** | **0.1352** | Empirical mean squared difference across paired non-null slots. |

*Note on Inferential Statistics*:
Because factor evaluations are structurally nested within papers and ontology domains, descriptive effect sizes ($r = 0.767$, $\text{MAE} = 0.131$) are reported without assuming independent and identically distributed (IID) observations.

---

## 2. Permutation Benchmark Specifications

For comparison against random assignment:
- **Null Distribution**: Generated via Monte Carlo factor shuffle ($B = 10,000$ permutations) within the $[-1.0, +1.0]$ score domain.
- **Expected Shuffle Distance**: $\text{MSD}_{\text{shuffle}} \approx 0.500$ (with empirical $95\%\text{ CI: } [0.482, 0.518]$).
- **Observed Workflow Distance**: $\text{MSD}_{\text{obs}} = 0.1352$, confirming structured semantic alignment far above chance expectation.

---

## 3. Stratified Registry Status

Recorded in [`content/tables/experts/expert_registry.csv`](file:///Users/hamednejat/workspace/main/mllm-public/content/tables/experts/expert_registry.csv):

| ID | Stratum | Methodology / AI Tooling | Order | Status |
| :---: | :---: | :--- | :---: | :---: |
| **`hpch_01`** | `human` | Human Expert 1 (Baseline reference) | Canonical | `pending_ingestion` |
| **`hpch_02`** | `human` | Human Expert 2 (Independent Panel) | Independent | `pending_ingestion` |
| **`hpch_03`** | `human` | Human Expert 3 (Independent Panel) | Independent | `pending_ingestion` |
| **`hpchai_01`** | `human_ai` | Gemini 2.5 Pro Assisted | Forward $1 \to 31$ | `verified` |
| **`hpchai_02`** | `human_ai` | Gemini 2.5 Pro Assisted | Reverse $31 \to 1$ | `verified` |
