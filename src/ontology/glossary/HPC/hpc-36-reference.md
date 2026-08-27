# Hierarchical Predictive Coding Factors - HPC -- Glossary Reference
# Role: computational neuroscientist

This document provides a human-readable reference of all 36 neuroscience predictive coding factors, organized by hypothesis group. Each factor includes its unique ID, name, definition, measurement tag, and the experimental contexts in which it applies.

**Tag Legend**

- **Quantitative** -- Factor is measured with continuous or numerical evidence.
- **Qualitative** -- Factor is assessed by presence/absence or categorical judgment.
- **Methodological** -- Factor relates to the method of observation rather than the mechanism itself.

**Context Legend**

- **LO** -- Local Oddball paradigm only.
- **LO+GO** -- Both Local Oddball and Global Oddball paradigms.

---

## H1: Predictive Suppression (IDs 1--12)

Factors in this group address the mechanisms by which the brain suppresses neural responses to expected or predictable stimuli.

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 1 | Subtractive Inhibition (SST) | Linear suppression of input via somatic inhibition (Somatostatin-mediated). | Quantitative | LO+GO |
| 2 | Divisive Inhibition (PV) | Multiplicative gain reduction (Parvalbumin-mediated). | Quantitative | LO+GO |
| 3 | Inhibition (GABA) | Chloride-mediated inhibition for suppression of prediction. | Quantitative | LO+GO |
| 4 | Habituation to Sequence | Habituation suppresses local oddball response relative to a novel local oddball. | Quantitative | LO |
| 5 | Synaptic Depression (Adaptation) | Passive fatigue of synaptic efficacy due to repetition of stimulus. | Quantitative | LO |
| 6 | Activity Suppression | Reduction in firing rates for expected (predictable) stimuli. | Quantitative | LO+GO |
| 7 | Selective Sharpening | Signal-to-noise increase for predictable stimuli, where noise is selectively suppressed to highlight relevant information. | Quantitative | LO+GO |
| 8 | Alpha/Beta Mediated Suppression | Desynchronization in low-frequency bands (8-30Hz) as a result of disinhibited prediction error signals. | Quantitative | LO+GO |
| 9 | VIP-Mediated Disinhibition | VIP-mediated inhibition of SST/PV neurons, leading to disinhibited pyramidal activity during prediction error. | Qualitative | LO+GO |
| 10 | Precision Weighting (Gain) | Top-down amplification of error units, leading to disinhibited gain in response to attended or highly precise stimuli. | Qualitative | LO+GO |
| 11 | E/I Balance Shift | Dynamic adjustment toward higher inhibition for predictable stimuli, leading to suppressed neural firing. | Quantitative | LO+GO |
| 12 | Omission Response | A top-down generated internal signal in the absence of prediction-mediated suppression, revealing the raw expectation. | Quantitative | LO+GO |

---

## H2: Feedforward Error Propagation (IDs 13--24)

Factors in this group address how prediction-error signals are generated and transmitted in the feedforward (ascending) direction through the cortical hierarchy.

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 13 | Feedforward Deviance Detection | Detection of mismatch signals that explicitly propagate in the feedforward (ascending) direction to higher cortical areas. | Quantitative | LO+GO |
| 14 | Feedforward AMPA | Fast excitatory drive mediated by AMPA receptors, specifically conveying prediction-error signals in the feedforward direction. | Quantitative | LO+GO |
| 15 | Feedforward NMDA | Voltage-dependent amplification (bursting) of error signals, facilitating their robust feedforward propagation through the hierarchy. | Quantitative | LO+GO |
| 16 | Feedforward Ascending Gamma | Rhythmic synchronization (30-90Hz) that temporally packages prediction-error signals for efficient feedforward transmission. | Quantitative | LO+GO |
| 17 | Absence of Feedback Error | The functional requirement that the prediction-error signal must be strictly feedforward-directed, distinguishing it from local or feedback signals. | Quantitative | LO+GO |
| 18 | Feedforward Non-local Supragranular Activity (L2/3) | Error-signaling neurons in Layers 2/3 projecting strictly into the next area, and NOT projecting inside the column serving as the primary anatomical source for feedforward signal propagation. | Quantitative | LO+GO |
| 19 | Feedforward Non-local Granular Activity (L4) | The arrival of prediction error signals in Layer 4, from PREVIOUS area and non-local representing the canonical entry point for feedforward propagation into the cortical column. | Quantitative | LO+GO |
| 20 | Feedforward Non-local Directed Connectivity | Directional measures (Granger Causality/Transfer Entropy) confirming the directed feedforward propagation of prediction error from lower to higher areas. | Quantitative | LO+GO |
| 21 | Feedforward Non-local Activation | Functional activation patterns specifically tracing the feedforward propagation path through the hierarchy. | Quantitative | LO+GO |
| 22 | Ascending Latency Shift | Systematic increases in response latency that characterize the feedforward propagation of prediction error through successive levels of the hierarchy. | Quantitative | LO+GO |
| 23 | Feedforward Error Propagation | Explicit experimental evidence that the prediction error signal is transmitted primarily via feedforward propagation pathways. | Qualitative | LO+GO |
| 24 | Subcortical Feedforward Relaying | Relaying or generation of prediction error signals by subcortical structures (Thalamus/BG), initiating or sustaining their feedforward propagation to the cortex. | Quantitative | LO+GO |


---

## H3: Ubiquity (IDs 25--36)

Factors in this group address whether the predictive coding mechanism is a universal, consistent feature across cortical areas, hierarchical levels, modalities, and species.

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 25 | Canonical Microcircuit Ubiquity | The ubiquitous presence of the L2/3 Error and L5/6 Prediction motif repeating across most or all levels of the cortical hierarchy. | Qualitative | LO+GO |
| 26 | Hierarchical Mechanism Invariance | The ubiquitous nature of the predictive coding mechanism, functioning identically in the hierarchy from V1 to PFC. | Qualitative | LO+GO |
| 27 | Hierarchical Activity Ubiquity | The ubiquitous presence of prediction-error activity, detectable across all or most levels of the system's brain hierarchy. | Quantitative | LO+GO |
| 28 | Hierarchical CSD Ubiquity | The ubiquity of current source density profiles, which show consistent laminar patterns across most or all hierarchical levels. | Quantitative | LO+GO |
| 29 | Cross-Scale Hierarchical Ubiquity | The ubiquity of effects observable across scales (single units to LFP) throughout most levels of the cortical hierarchy. | Methodological | LO+GO |
| 30 | Hierarchical Presence (V1-PFC) | The ubiquity of the mechanism across all levels of the hierarchy, specifically including low-level (V1), mid-level (V4), and high-level (PFC) areas. | Qualitative | LO+GO |
| 31 | Cross-Modal Ubiquity | Presence of the mechanism across multiple sensory modalities (visual, auditory, somatosensory) throughout the hierarchy. | Qualitative | LO+GO |
| 32 | Interspecies Hierarchical Ubiquity | Conservation of the hierarchical predictive coding mechanism across different species (e.g., mouse vs. primate). | Qualitative | LO+GO |
| 33 | Temporal Stability of Ubiquity | The consistent and non-transient presence of these mechanisms across the hierarchy over long recording sessions. | Quantitative | LO+GO |
| 34 | Hierarchical Order Stability | Evidence that the predictive mechanism is ubiquitous and not localized to a single hierarchical pole. | Qualitative | LO+GO |
| 35 | Population-Wide Ubiquity | Consistency of the mechanism across diverse neural populations and cell types throughout the hierarchy. | Qualitative | LO+GO |
| 36 | State-Independent Ubiquity | Presence of the mechanism across different brain states (e.g., wakefulness, sleep, anesthesia) throughout the hierarchy. | Qualitative | LO+GO |

---

## Summary Statistics

| Hypothesis Group | ID Range | Total Factors | Quantitative | Qualitative | Methodological |
|------------------|----------|---------------|--------------|-------------|----------------|
| H1: Predictive Suppression | 1--12 | 12 | 10 | 2 | 0 |
| H2: Feedforward Error Propagation | 13--24 | 12 | 10 | 2 | 0 |
| H3: Ubiquity | 25--36 | 12 | 4 | 7 | 1 |
| **Total** | **1--36** | **36** | **24** | **11** | **1** |
