# 🧠 FINETUNE_CORE: Closing the Causal Loop

## 1. 📂 Architecture Overview
This project aims to transform LLMs from passive readers of neuroscience to active participants in scientific discovery. The "Closed Loop" approach ensures that the model's internal causal reasoning matches the reality of empirical data.

### Aim 1: Language-to-Logic (Causal Reasoning)
- **Input**: Literature (e.g., GLO/Omission papers), Glossaries (HPC-36, SCZ-51, ADB-60).
- **Process**: LLM evaluates the text, extracts variables (e.g., SST activity, Gamma power), and constructs a directed causal graph: `SST -> (-) -> PV -> (+) -> Gamma`.
- **Validation**: Compare this graph against human expert consensus.

### Aim 2: Logic-to-Data (Empirical Validation)
- **Input**: Spiking data (NWB), LFP recordings, behavior.
- **Process**: The model generates a specific, testable prediction: *"Based on the GLO causal graph, SST neurons should be suppressed during omission trials."*
- **Action**: Run the empirical analysis on the data.
- **Output**: Confirmation (Data matches Reasoning) or Refutation (Data contradicts Reasoning).

---

## 2. 🛠 Fine-Tuning Protocols

### LoRA vs. DoRA: Why it Matters
| Feature | LoRA (Low-Rank Adaptation) | DoRA (Weight-Decomposed LoRA) |
| :--- | :--- | :--- |
| **Method** | Adds small trainable matrices. | Separates weight into Magnitude and Direction. |
| **Accuracy** | Good for broad task adaptation. | **High-Fidelity**; better at capturing nuanced physics/causality. |
| **Stability** | Faster to train. | More stable; avoids "over-fitting" to linguistic noise. |

**Application**: We use **DoRA** for Aim 1 because scientific reasoning requires precision in "directional" weight updates (modeling causal directions).

### Hyperparameter Discipline
- **Iterations**: 1000-2000 (standard), 5000+ for deep causal fine-tuning.
- **Rank (r)**: 16 (balanced), 32 (high capacity for complex glossaries).
- **Alpha**: 2x Rank (standard).
- **LR**: 1e-5 (cautious) to 2e-4 (aggressive).

---

## 3. 🚦 Data Consistency Monitoring
The critical innovation is the "Consistency Score." We tag each training pair with a `consistency_index`:
- `{"messages": [...], "metadata": {"consistency": "HIGH", "source": "GLO_HPC_2025"}}`

### If Inconsistent:
- The model must perform a "Correction Phase."
- **Prompt**: *"Your causal reasoning predicted X, but the spiking data shows Y. Analyze why the literature reasoning failed to capture the empirical reality."*
- **Outcome**: A "Revised Causal Graph" that integrates the empirical data into the model's world-view.

---

## 4. 🚀 Implementation Roadmap
1. **Pre-train**: On broad neuroscience literature (Aim 1).
2. **Fine-tune**: On specific GLO/HPC causal reasoning tasks (Aim 1 + DoRA).
3. **Validate**: Run the "Empirical Loop" script on NWB data (Aim 2).
4. **Iterate**: Feed validation results back into the fine-tuning set.
