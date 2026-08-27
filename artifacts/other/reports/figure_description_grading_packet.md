# DeepRead Multimodal Figure-Description Manual Grading Packet

**Purpose**: Independent empirical validation of generated VLM figure descriptions against primary source figures and captions (Reviewer 1 Minor Concern #2).

## Evaluation Rubric & Permissibility Rules

1. **Axis A: Numerical & Statistical Extraction Accuracy**
   - `Correct`: Values, sample sizes, units, and statistical tests accurately extracted.
   - `Minor Deviation`: Minor numerical discrepancy (e.g., slight rounding difference) not altering meaning.
   - `Severe Error`: Major error in extracted numerical quantities ($> 10\%$) or incorrect $p$-value.
   - `Not Applicable (N/A)`: **Permitted** if the primary figure/caption contains no quantitative numbers.

2. **Axis B: Empirical Effect Direction / Trend**
   - `Concordant`: Generated description correctly reflects direction of neural activity / modulation.
   - `Inverted`: Generated description reverses the biological direction (e.g., reports suppression instead of enhancement).
   - `Ambiguous`: Description is contradictory or unclear.

3. **Axis C: HPC-36 Biological Glossary Term Mapping**
   - `Accurate`: Correctly maps figure findings to canonical biological terms (e.g., PV vs SST vs VIP interneurons, layers 2/3 vs 4 vs 5/6).
   - `Mismatched`: Conflates cell types, layers, or routing directions.
   - `Not Applicable (N/A)`: **Permitted** if the generated description does not attempt a specific glossary mapping.

---

## Prespecified 10-Figure Sample & Generated Descriptions

### Item 1: Attinger2017 — Figure 2
- **Modality**: 2-Photon Calcium Imaging (Mouse V1)
- **Selection Basis**: Classic Visuomotor Baseline
- **Source Reference**: DOI `10.1016/j.neuron.2017.01.031`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): This figure is a schematic diagram illustrating the relationship between motor output, sensory feedback, and visual input in the context of sensorimotor experience. It is divided into two main conceptual sections: "Before" and "After," which are further detailed in a lower panel.
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 2: Garret2020 — Figure 3
- **Modality**: 2-Photon Calcium Imaging (Mouse Visual Cortex)
- **Selection Basis**: Novelty vs Deviance Baseline
- **Source Reference**: DOI `10.7554/eLife.50340`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): This image displays a line graph titled "mouse M409259," which appears to be an example of behavioral performance data, likely related to the natural image change detection task described in the accompanying caption.
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 3: Bastos2020 — Figure 4
- **Modality**: Laminar ECoG / LFP Recording (Non-Human Primate)
- **Selection Basis**: Laminar Rhythm Specificity
- **Source Reference**: DOI `10.1016/j.neuron.2020.09.018`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): Since no figure image was provided, I cannot generate the detailed description.
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 4: Chao2018 — Figure 3
- **Modality**: High-Density ECoG Grid (Non-Human Primate)
- **Selection Basis**: Large-Scale Cortical Prediction Hierarchy
- **Source Reference**: DOI `10.1038/s41467-018-05188-7`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): ## Figure Description: Electrode Placement Map for Subject 1
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 5: Bekinschtein2009 — Figure 2
- **Modality**: Scalp High-Density EEG (Human)
- **Selection Basis**: Local-Global Oddball Originator
- **Source Reference**: DOI `10.1073/pnas.0809667106`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): ## Figure 2 Description
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 6: LaoRodriguez2023 — Figure 3
- **Modality**: Scalp EEG & Auditory ERPs (Human)
- **Selection Basis**: Mismatch Negativity Hierarchy
- **Source Reference**: DOI `10.1007/s11571-023-09947-6`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): ## Figure Description: Experimental Setup and Neural Recording
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 7: Srinivasan1982 — Figure 1
- **Modality**: Intracellular Recording (Insect / Fly Compound Eye)
- **Selection Basis**: Predictive Redundancy Reduction Baseline
- **Source Reference**: DOI `10.1098/rspb.1982.0085`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): The provided image is a logo, not a scientific figure containing data or schematics. Therefore, the description will focus on its typographical and structural elements as a graphic design element.
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 8: Nejad2025 — Figure 2
- **Modality**: Intracranial Electrophysiology (Non-Human Primate)
- **Selection Basis**: Cortical Laminar Dissociation in Routing
- **Source Reference**: DOI `10.1523/JNEUROSCI.1234-24.2025`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): ## Figure 1: Information Flow in Neocortical Circuits
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 9: Hertag2020 — Figure 2
- **Modality**: Biophysical Spiking Neural Network (In Silico)
- **Selection Basis**: Circuit Model of SST/PV Dynamics
- **Source Reference**: DOI `10.7554/eLife.57051`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): This figure, Figure 1, illustrates a network model demonstrating how balancing excitation and inhibition leads to the emergence of negative prediction-error (nPE) neurons. It is composed of five panels: (a), (b), (c), (d), and (e).
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---

### Item 10: LeeMejias2025 — Figure 4
- **Modality**: Multi-Regional Spiking Network (In Silico)
- **Selection Basis**: Primate Multi-Regional Predictive Oscillations
- **Source Reference**: DOI `10.1371/journal.pcbi.1013469`

**Extracted Generated DeepRead Block**:
```markdown
> Figure description (generated): ## Figure Description
```

| Evaluator ID | Axis A (Numeric) | Axis B (Direction) | Axis C (Mapping) | Adjudicated Grade | Concise Error Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Grader 1 | | | | | |
| Grader 2 | | | | | |

---
