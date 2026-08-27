# Manuscript Revision Integration: Stochastic Decoding & Temperature Robustness

This document contains the exact manuscript prose and LaTeX text ready for insertion into the **Methods** and **Results / Discussion** sections of the *Scientific Reports* submission.

---

## 1. Results Section: Robustness to Stochastic Decoding & Temperature

### Markdown Format:
> **Robustness of HPC Evaluations to Stochastic Sampling and Temperature**
>
> To assess whether the literature-derived HPC representations are sensitive to stochastic decoding perturbations or sampling temperature, we conducted a systematic factorial robustness experiment across 31 papers, three reviewer models (`Gemma-4-31B-IT`, `Phi-4-Reasoning-Plus`, `OLMo-3-32B-Think`), three decoding temperatures ($T \in \{0.00, 0.35, 0.70\}$), and three independent stochastic repeated evaluations per condition ($N = 837$ inference attempts). 
>
> Because model architectures differed in their ability to serialize complete factor matrices within fixed token allowances, we distinguish overall inference attempts from complete 72-slot evaluations and base our primary robustness inference on `Gemma-4-31B-IT`, which completed all 279/279 experimental conditions ($100.0\%$).
>
> For `Gemma-4-31B-IT`, the literature-derived HPC scoring geometry demonstrated high stability across decoding temperatures. When averaging across the three repeated evaluations within each paper $\times$ factor $\times$ context $\times$ temperature cell, scores obtained at $T=0.00$ correlated strongly with scores at $T=0.35$ ($r = 0.9900$, $\text{MAE} = 0.0266$) and with scores at $T=0.70$ ($r = 0.9760$, $\text{MAE} = 0.0421$) on the $[-1.0, +1.0]$ score scale. Replicate reliability across independent stochastic runs under identical temperatures was similarly high ($\bar{r}_{\text{rep}} = 0.9905$ at $T=0.00$; $\bar{r}_{\text{rep}} = 0.9724$ at $T=0.35$; $\bar{r}_{\text{rep}} = 0.9444$ at $T=0.70$).
>
> Furthermore, Gemma-derived scores preserved moderate concordance with independent human expert annotation ($r = 0.5160$; mean paper-clustered $r = 0.4412$) and with the original baseline evaluation ($r = 0.4015$; mean paper-clustered $r = 0.3244$). 
>
> In auxiliary sensitivity analyses, `Phi-4-Reasoning-Plus` exhibited moderate agreement among its completed evaluations ($r = 0.6505$ for $T=0.00$ vs. $T=0.70$), though its completion rate was bounded ($46.6\%$, 130/279 conditions) due to long-form reasoning trajectories exhausting fixed generation budgets prior to final serialization. `OLMo-3-32B-Think` completed 30/279 evaluations ($10.8\%$), precluding a reliable temperature-stability estimate under the tested local serving environment. Consequently, we do not generalize the primary Gemma stability result across all reasoning architectures.

---

### LaTeX Format:
```latex
\subsection*{Robustness of HPC Evaluations to Stochastic Sampling and Temperature}
To assess whether the literature-derived HPC representations are sensitive to stochastic decoding perturbations or sampling temperature, we conducted a systematic factorial robustness experiment across 31 papers, three reviewer models (\texttt{Gemma-4-31B-IT}, \texttt{Phi-4-Reasoning-Plus}, \texttt{OLMo-3-32B-Think}), three decoding temperatures ($T \in \{0.00, 0.35, 0.70\}$), and three independent stochastic repeated evaluations per condition ($N = 837$ inference attempts). 

Because model architectures differed substantially in their ability to serialize complete factor matrices within fixed token allowances, we distinguish overall inference attempts from complete 72-slot evaluations and base our primary robustness inference on \texttt{Gemma-4-31B-IT}, which completed all 279/279 experimental conditions (100.0\%).

For \texttt{Gemma-4-31B-IT}, the literature-derived HPC scoring geometry demonstrated high stability across decoding temperatures. When averaging across the three repeated evaluations within each paper $\times$ factor $\times$ context $\times$ temperature cell, scores obtained at $T=0.00$ correlated strongly with scores at $T=0.35$ ($r = 0.9900$, $\text{MAE} = 0.0266$) and with scores at $T=0.70$ ($r = 0.9760$, $\text{MAE} = 0.0421$) on the $[-1.0, +1.0]$ score scale. Replicate reliability across independent stochastic runs under identical temperatures was similarly high ($\bar{r}_{\text{rep}} = 0.9905$ at $T=0.00$; $\bar{r}_{\text{rep}} = 0.9724$ at $T=0.35$; $\bar{r}_{\text{rep}} = 0.9444$ at $T=0.70$).

Furthermore, Gemma-derived scores preserved moderate concordance with independent human expert annotation ($r = 0.5160$; mean paper-clustered $r = 0.4412$) and with the original baseline evaluation ($r = 0.4015$; mean paper-clustered $r = 0.3244$). 

In auxiliary sensitivity analyses, \texttt{Phi-4-Reasoning-Plus} exhibited moderate agreement among its completed evaluations ($r = 0.6505$ for $T=0.00$ vs. $T=0.70$), though its completion rate was bounded ($46.6\%$, 130/279 conditions) due to long-form reasoning trajectories exhausting fixed generation budgets prior to final serialization. \texttt{OLMo-3-32B-Think} completed 30/279 evaluations ($10.8\%$), precluding a reliable temperature-stability estimate under the tested local serving environment. Consequently, we do not generalize the primary Gemma stability result across all reasoning architectures.
```

---

## 2. Methods Section: Robustness Protocol & Experimental Design

### Markdown Format:
> **Factorial Robustness Protocol**
>
> The robustness sweep followed a full factorial design: 31 papers $\times$ 3 models $\times$ 3 temperatures ($T \in \{0.00, 0.35, 0.70\}$, with top-$p=0.90$, min-$p=0.10$) $\times$ 3 independent stochastic repeats, yielding 837 planned attempts.
>
> Each condition evaluated all 36 canonical HPC ontology factors across Local Oddball (LO) and Global Oddball (GO) contexts (72 slots total). Explicit `null` assignments were recorded when papers did not address specific factors. Full evaluation completeness was defined as $C_i = N_{\text{evaluated slots}} / 72 = 1.0$. All raw inference outputs, prompt SHA-256 hashes, timestamps, and model identifiers were permanently logged in an atomic call ledger (`calls.csv`) and raw JSON store.

---

### LaTeX Format:
```latex
\subsection*{Factorial Robustness Protocol}
The robustness sweep followed a full factorial design: 31 papers $\times$ 3 models $\times$ 3 temperatures ($T \in \{0.00, 0.35, 0.70\}$, with $\text{top-}p=0.90$, $\text{min-}p=0.10$) $\times$ 3 independent stochastic repeats, yielding 837 planned attempts.

Each condition evaluated all 36 canonical HPC ontology factors across Local Oddball (LO) and Global Oddball (GO) contexts (72 slots total). Explicit \texttt{null} assignments were recorded when papers did not address specific factors. Full evaluation completeness was defined as $C_i = N_{\text{evaluated slots}} / 72 = 1.0$. All raw inference outputs, prompt SHA-256 hashes, timestamps, and model identifiers were permanently logged in an atomic call ledger (\texttt{calls.csv}) and raw JSON store.
```
