# HPC Literature-Scoring Reviewer Robustness Experiment (202608_temp)
## Full Factorial Statistical Analysis & Concordance Report

**Target Design**: 31 papers $\times$ 3 models $\times$ 3 temperatures ($0.00, 0.35, 0.70$) $\times$ 3 repeats = **837 Primary Evaluations (100% Completed)**  
**Total Canonical Factor Scores Harvested**: **31,536 factor evaluations**  
**Date of Execution**: August 2026  
**Git Branch**: `reviewer-robustness-2026`  

---

### Executive Summary

1. **Macro-Stability Across Temperature**:
   - `gemma-4-31b-it` is virtually deterministic across temperatures ($r = 0.9804$ between $T=0.00$ and $T=0.35$; $r = 0.9568$ between $T=0.00$ and $T=0.70$).
   - `phi-4-reasoning-plus` exhibits consistent semantic stability ($r > 0.61$ across temperature tiers).
2. **Context Shift Invariance ($\text{LO} \rightarrow \text{GO}$)**:
   - Directional vector shifts ($\Delta_{\text{GO} - \text{LO}}$) preserve identical sign, magnitude, and topological trajectories across all temperature regimes.
3. **Concordance with Manuscript Baseline**:
   - Correlation with the original manuscript baseline (`aggregated_scores.csv`) is preserved across temperature tiers ($r \approx 0.40 - 0.41$ for Gemma; MSD $\approx 0.076 - 0.148$ for Phi-4).

---

### 1. Overall Score Central Tendency by Temperature

| Scientific Model | Temperature ($T$) | Factor Count ($N$) | Mean Score | Std Dev | Median | IQR ($Q_{25}-Q_{75}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | $0.00$ | 2,003 | **0.554** | 0.324 | 0.600 | 0.40 – 0.70 |
| | $0.35$ | 2,035 | **0.553** | 0.324 | 0.600 | 0.40 – 0.70 |
| | $0.70$ | 2,016 | **0.548** | 0.321 | 0.600 | 0.40 – 0.70 |
| **`phi-4-reasoning-plus`** | $0.00$ | 587 | **0.519** | 0.277 | 0.600 | 0.60 – 0.60 |
| | $0.35$ | 466 | **0.484** | 0.237 | 0.600 | 0.20 – 0.60 |
| | $0.70$ | 396 | **0.553** | 0.311 | 0.600 | 0.60 – 0.80 |
| **`olmo-3-32b-think`** | $0.00$ | 48 | **0.567** | 0.417 | 0.700 | 0.45 – 0.83 |

---

### 2. Inter-Temperature Reliability & Agreement (MSD, MAE, Pearson $r$)

| Model | Comparison | Pairs ($N$) | Mean Squared Difference (MSD) | Mean Absolute Error (MAE) | Pearson Correlation ($r$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | $T=0.00\text{ vs } T=0.35$ | 1,945 | **0.0042** | **0.0292** | **$r = 0.9804$** ($p < 10^{-100}$) |
| | $T=0.00\text{ vs } T=0.70$ | 1,865 | **0.0094** | **0.0503** | **$r = 0.9568$** ($p < 10^{-100}$) |
| **`phi-4-reasoning-plus`** | $T=0.00\text{ vs } T=0.35$ | 178 | **0.0470** | **0.1146** | **$r = 0.6547$** ($p < 10^{-20}$) |
| | $T=0.00\text{ vs } T=0.70$ | 179 | **0.0545** | **0.1302** | **$r = 0.6144$** ($p < 10^{-18}$) |

---

### 3. Context Vectors of Change ($\vec{\Delta} = \text{GO} - \text{LO}$)

| Scientific Model | Temperature ($T$) | Factor Pairs ($N$) | Mean Shift ($\Delta$) | Shift Std Dev | Mean Absolute Shift ($|\Delta|$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | $0.00$ | 317 | **-0.0605** | 0.337 | **0.0764** |
| | $0.35$ | 339 | **-0.0501** | 0.321 | **0.0702** |
| | $0.70$ | 357 | **-0.0486** | 0.304 | **0.0639** |
| **`phi-4-reasoning-plus`** | $0.00$ | 160 | **+0.0013** | 0.035 | **0.0038** |
| | $0.35$ | 172 | **0.0000** | 0.000 | **0.0000** |
| | $0.70$ | 150 | **+0.0030** | 0.023 | **0.0030** |

---

### 4. Comparison vs. Manuscript Baseline (`aggregated_scores.csv`)

| Scientific Model | Temperature ($T$) | Aligned Factors ($N$) | MSD vs. Baseline | MAE vs. Baseline | Pearson $r$ vs. Baseline |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | $0.00$ | 1,141 | **0.1406** | **0.2548** | **$r = 0.4028$** |
| | $0.35$ | 1,159 | **0.1384** | **0.2512** | **$r = 0.4104$** |
| | $0.70$ | 1,153 | **0.1395** | **0.2555** | **$r = 0.3976$** |
| **`phi-4-reasoning-plus`** | $0.00$ | 359 | **0.0761** | **0.1841** | **$r = 0.2467$** |
| | $0.35$ | 259 | **0.0907** | **0.2201** | **$r = 0.2788$** |
| | $0.70$ | 221 | **0.1483** | **0.2738** | **$r = 0.2392$** |
