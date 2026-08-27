# Reviewer-Targeted Robustness Analysis (Scientific Reports Revision)

**Experiment Design**: 31 papers $\times$ 3 models (`gemma-4-31b-it`, `phi-4-reasoning-plus`, `olmo-3-32b-think`) $\times$ 3 temperatures ($T \in \{0.00, 0.35, 0.70\}$) $\times$ 3 independent stochastic repeats = **837 total inference attempts**.

---

### 1. Operational Completion & Evaluation Viability

Evaluations are categorized by full-slot canonical completion ($C_i = N_{\text{evaluated slots}} / 72$, where an explicit `null` is a valid scientific assignment for unaddressed factors):

| Model | Total Attempts | Complete ($C_i=1.0$) | Partial ($0.10 \le C_i < 1.0$) | Failed ($C_i < 0.10$) | Primary Usable Factors ($N$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | 279 | **279 (100.0%)** | 0 (0.0%) | 0 (0.0%) | **6,054** |
| **`phi-4-reasoning-plus`** | 279 | **130 (46.6%)** | 54 (19.4%) | 95 (34.1%) | **1,449** |
| **`olmo-3-32b-think`** | 279 | **30 (10.8%)** | 69 (24.7%) | 180 (64.5%) | **48** |

*Methodological Basis*:
- **`gemma-4-31b-it`**: Completed all 279/279 conditions (72 evaluated slots each); provides the primary empirical basis for robustness claims.
- **`phi-4-reasoning-plus`**: High completion at low temperature ($51/93$ at $T=0.00$), but token budget truncation reduces structured yield at higher temperatures ($34/93$ at $T=0.70$).
- **`olmo-3-32b-think`**: Severe token truncation and local server context limits under the tested setup preclude reliable statistical temperature claims.

---

### 2. Core Reviewer-Facing Results Summary

| Dimension | Primary Model (`gemma-4-31b-it`) | Reasoning Sensitivity Model (`phi-4-reasoning-plus`) | Exploratory Model (`olmo-3-32b-think`) | Reviewer Takeaway |
| :--- | :---: | :---: | :---: | :--- |
| **Operational Completion ($C_i=1.0$)** | **100.0%** (279 / 279) | **46.6%** (130 / 279) | **10.8%** (30 / 279) | Primary model evaluated all 72 canonical factor slots across all 279 cells. |
| **Temperature Stability ($\bar{r}_{0,.70}$)** | **$r = 0.9760$** ($\text{MAE} = 0.0421$) | **$r = 0.6505$** ($\text{MAE} = 0.1421$) | *N/A (insufficient cell overlap)* | HPC scoring geometry is highly stable across tested decoding temperatures in the primary model. |
| **Replicate Reliability ($\bar{r}_{\text{rep}} \mid T=0.35$)** | **$r_{\text{rep}} = 0.9724$** ($\text{MAE} = 0.0384$) | *N/A (incomplete triples at .35)* | *N/A* | Variation across independent stochastic runs is small ($\text{MAE} < 0.04$). |
| **Human Expert Concordance ($r_{\text{human}}$)** | **$r = 0.5160$** (Clustered: **$r = 0.4412$**) | **$r = 0.3400$** (Clustered: **$r = 0.2810$**) | *N/A* | Preserves moderate concordance with independent human expert scoring. |
| **Original Manuscript Concordance ($r_{\text{base}}$)** | **$r = 0.4015$** (Clustered: **$r = 0.3244$**) | **$r = 0.3224$** (Clustered: **$r = 0.1778$**) | *N/A* | Preserves moderate concordance with original manuscript baseline scores. |

---

### 3. Temperature Stability (Cell-Mean Scores Across 3 Repeats)

Scores are averaged across the 3 independent stochastic runs within each `(paper, context, factor, temperature)` cell ($\bar{s}_{pfcT} = \frac{1}{3}\sum_{r=1}^3 s_{pfcTr}$):

| Model | Overlapping Factor Cells ($N$) | $T=0.00\text{ vs } T=0.35$ | $T=0.00\text{ vs } T=0.70$ | $T=0.35\text{ vs } T=0.70$ |
| :--- | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | **679** | **$r = 0.9900$** ($\text{MAE} = 0.0266$) | **$r = 0.9760$** ($\text{MAE} = 0.0421$) | **$r = 0.9816$** ($\text{MAE} = 0.0367$) |
| **`phi-4-reasoning-plus`** | **104** | **$r = 0.5231$** ($\text{MAE} = 0.1269$) | **$r = 0.6505$** ($\text{MAE} = 0.1421$) | **$r = 0.3294$** ($\text{MAE} = 0.1761$) |

---

### 4. Within-Temperature Replicate Reliability

Pairwise agreement across independent stochastic generations when temperature is held constant:

| Model | Temperature ($T$) | Complete Triples ($N$) | Mean Replicate Correlation ($\bar{r}_{\text{rep}}$) | Mean Replicate MAE |
| :--- | :---: | :---: | :---: | :---: |
| **`gemma-4-31b-it`** | $0.00$ | 639 | **$r = 0.9905$** | **0.0126** |
| | $0.35$ | 619 | **$r = 0.9724$** | **0.0384** |
| | $0.70$ | 572 | **$r = 0.9444$** | **0.0585** |
| **`phi-4-reasoning-plus`** | $0.00$ | 106 | **$r = 0.8126$** | **0.0755** |
| | $0.70$ | 14 | **$r = 0.3568$** | **0.1333** |

---

### 5. Final Rebuttal & Manuscript Response Text

> **Reviewer Response Draft**:
>
> We thank the reviewer for raising the question of sensitivity to stochastic decoding temperature and repeated sampling. To address this directly, we conducted a systematic robustness experiment across 31 papers, three reviewer models, three temperatures ($T \in \{0.00, 0.35, 0.70\}$), and three repeated evaluations per condition, comprising 837 inference attempts. Because the comparison models differed substantially in their ability to complete the full structured evaluation, we distinguish inference attempts from complete 72-slot evaluations and base our primary robustness inference on Gemma-4-31B, which completed all 279/279 conditions.
>
> For Gemma-4-31B, the literature-derived HPC scores were highly stable across the tested decoding temperatures. After averaging the three repeated evaluations within each paper $\times$ factor $\times$ context $\times$ temperature cell, scores at $T=0.00$ correlated $r=0.9900$ with scores at $T=0.35$ ($\text{MAE}=0.0266$) and $r=0.9760$ with scores at $T=0.70$ ($\text{MAE}=0.0421$) on the $[-1, +1]$ scoring scale. Within-temperature replicate reliability was similarly high and remained strong as stochasticity increased ($\bar{r}_{\text{rep}}=0.9905,\ 0.9724,\ 0.9444$ at $T=0.00,\ 0.35,\ 0.70$, respectively). These results indicate that neither the tested decoding temperatures nor repeated stochastic sampling materially altered the relative HPC scoring structure in the primary evaluation model.
>
> As an external check, Gemma-derived scores retained moderate concordance with the independent human expert annotation (pooled $r=0.5160$; mean within-paper $r=0.4412$) and with the original manuscript baseline scores (pooled $r=0.4015$; mean within-paper $r=0.3244$). Thus, the temperature-stable representation also preserves correspondence with independent expert judgment and the original analysis.
>
> The additional reasoning-model experiments provide sensitivity analyses rather than the primary basis for this conclusion. Phi-4 showed moderate temperature agreement among completed structured evaluations (e.g., $r=0.6505$ for $T=0.00$ versus $T=0.70$), but only 130/279 (46.6%) attempts completed all 72 evaluation slots because long reasoning generations frequently reached the fixed generation budget before final structured serialization. OLMo-3 completed only 30/279 (10.8%) evaluations and therefore provided insufficient coverage for a reliable temperature-robustness estimate. We consequently do not generalize the primary Gemma robustness result across model architectures.
>
> We have revised the manuscript to report these robustness analyses and to distinguish explicitly between stochastic stability of the primary evaluation pipeline and the completion limitations observed in the auxiliary reasoning-model sensitivity analyses.
