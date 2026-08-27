# Neuroscience Analog-Digital Theories -- Glossary Reference
# Role: neuroscientist

This document provides a human-readable reference of all 60 factors related to Analog-Digital theories of the brain (ADB), organized by hypothesis group. Each factor is evaluated on a symmetric scale from **+1.0 (Supporting Analog Pole)** to **-1.0 (Supporting Digital Pole)**.

**Tag Legend**

- **Quantitative** -- Factor is measured with continuous or numerical evidence.
- **Qualitative** -- Factor is assessed by presence/absence or categorical judgment.
- **Methodological** -- Factor relates to the method of observation rather than the mechanism itself.

**Context Legend**

- **LFP/Fields** -- Primary focus on extracellular fields and LFPs.
- **Spiking** -- Primary focus on discrete action potentials and binary events.
- **Hybrid** -- Focus on the interaction between continuous and discrete signaling.

---

## H1: Carrier Identity (IDs 1--20)

Factors in this group address the physical infrastructure of neuronal communication, adjudicating whether the signal carrier is a continuous field (+1) or a discrete spike train (-1).

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 1 | LFP Causality (Ephaptic) | (+) Subthreshold fields causally shift Vmem; (-) Fields are passive epiphenomena of spiking. | Quantitative | LFP/Fields |
| 2 | Wave Propagation | (+) Information flows via continuous traveling waves; (-) Information flows via discrete axonal spikes. | Quantitative | Hybrid |
| 3 | Carrier Stability | (+) Subthreshold oscillations persist across spiking silence; (-) Carrier resets/terminates between spikes. | Quantitative | Hybrid |
| 4 | ECS Resistivity | (+) Changes in medium (glia/edema) modulate signaling; (-) Signaling is invariant to the Analog medium. | Quantitative | LFP/Fields |
| 5 | Dendritic Summation | (+) Continuous, linear/non-linear graded summation; (-) Digital all-or-none dendritic spikes. | Quantitative | Hybrid |
| 6 | Glial-Field Coupling | (+) Astrocytes directly modulate the extracellular field; (-) Glia strictly support Digital metabolic demands. | Qualitative | LFP/Fields |
| 7 | Subthreshold Gain | (+) LFP amplitude sets the Analog gain of a population; (-) Gain is set by discrete Digital synaptic weights. | Quantitative | Hybrid |
| 8 | Pacing Hierarchy | (+) Slow Analog rhythms drive Fast Digital units; (-) Fast Digital units generate the rhythm. | Quantitative | Hybrid |
| 9 | Network Resonance | (+) Circuit is tuned to a specific Analog frequency; (-) Circuit is frequency-agnostic and relies on Digital addresses. | Quantitative | LFP/Fields |
| 10 | Signal Continuity | (+) Signal value is valid at any time point t; (-) Signal is only valid during a Digital (spike) event. | Quantitative | Hybrid |
| 11 | Ephaptic Sync Gating | (+) Extracellular fields gate population synchrony; (-) Synchrony is a purely Digital network property. | Quantitative | LFP/Fields |
| 12 | Dendritic Gain Gradient | (+) Analog gradients along dendrites determine gain; (-) Digital backpropagating spikes determine gain. | Quantitative | Hybrid |
| 13 | Local Field Attenuation | (+) Decay of fields over space dictates circuit reach; (-) Axonal length of Digital tracts dictates reach. | Quantitative | LFP/Fields |
| 14 | Subthreshold Coherence | (+) Information is shared via subthreshold phase coherence; (-) Information is shared via Digital spike coherence. | Quantitative | Hybrid |
| 15 | Gap Junction Modulation | (+) Electrical Analog synapses are the primary carrier; (-) Chemical Digital synapses are the primary carrier. | Qualitative | Hybrid |
| 16 | Membrane Time Constant | (+) Slow Analog integration (tau_m) is the bottleneck; (-) Fast Digital refractory period is the bottleneck. | Quantitative | Hybrid |
| 17 | Frequency-Specific Res | (+) Carrier identity is tied to a specific LFP band; (-) Carrier is frequency-agnostic; relies on Digital addresses. | Quantitative | LFP/Fields |
| 18 | Ephaptic Crosstalk | (+) Circuit uses Analog Interference for computation; (-) Circuit uses Digital Isolation to prevent crosstalk. | Qualitative | LFP/Fields |
| 19 | Signal Regeneration | (+) Continuous signal is filtered but never reset; (-) Signal is regenerated as a bit at each node. | Quantitative | Hybrid |
| 20 | Infra Continuity | (+) Analog carrier is a global network property; (-) Carrier is a set of discrete Digital nodes. | Qualitative | Hybrid |

---

## H2: Data Representation (IDs 21--40)

Factors in this group address the encoding scheme, adjudicating whether the "Message" is a continuous magnitude (+1) or a discrete binary code (-1).

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 21 | Amplitude Modulation | (+) Stimulus intensity in continuous LFP power; (-) Stimulus intensity in discrete spike rates. | Quantitative | Hybrid |
| 22 | Phase Shift Keying | (+) Info is in relative phase offsets of oscillations; (-) Info is in absolute timing of Digital events. | Quantitative | Hybrid |
| 23 | Frequency Modulation | (+) Info is in shifting frequency peaks (Gamma); (-) Info is in discrete inter-spike interval bins. | Quantitative | Hybrid |
| 24 | Pulse Width Modulation | (+) Info is in the duration of an Analog burst; (-) Info is in the number of spikes per window. | Quantitative | Hybrid |
| 25 | Phase Precession | (+) Info is in spike latency relative to Analog phase; (-) Info is in latency relative to Digital trigger. | Quantitative | Hybrid |
| 26 | Quadrature Modulation | (+) Simultaneous encoding in phase AND amplitude; (-) Single-variable, independent Digital codes. | Quantitative | Hybrid |
| 27 | Spectral Efficiency | (+) Maximizes info density per Analog Hertz; (-) Maximizes info density per Digital Spike. | Quantitative | Hybrid |
| 28 | Cross-Frequency PAC | (+) The coupling coefficient itself is the message; (-) Coupling is a structural/clocking byproduct. | Quantitative | Hybrid |
| 29 | Field-Spike Precision | (+) High-precision locking to Analog phase required; (-) Spikes are stochastic/independent of phase. | Quantitative | Hybrid |
| 30 | Info Smearing | (+) Info is smeared across many Analog frequencies; (-) Info is localized in specific Digital channels. | Quantitative | Hybrid |
| 31 | Error Correction | (+) Continuous Analog feedback corrects signal drift; (-) Discrete Digital parity/checks are used. | Qualitative | Hybrid |
| 32 | Continuous Readout | (+) Info is readable at any point in the Analog cycle; (-) Info is only valid during Digital phase window. | Quantitative | Hybrid |
| 33 | Dynamic Resolution | (+) High-res details preserved in Analog magnitude; (-) Details quantized into binary Digital rate steps. | Quantitative | Hybrid |
| 34 | State Persistence | (+) Info persists in continuous Analog state; (-) Info requires Digital refreshment via spiking. | Qualitative | Hybrid |
| 35 | Signal Multiplexing | (+) Multiple messages overlapped in one carrier; (-) Messages separated into distinct fiber tracts. | Quantitative | Hybrid |
| 36 | Modulation Depth | (+) Variations in Analog mod depth carry data; (-) Presence/Absence of Digital events is the data. | Quantitative | Hybrid |
| 37 | Channel Capacity | (+) Transfer limited by Analog SNR of the field; (-) Transfer limited by Digital bandwidth of axon. | Quantitative | Hybrid |
| 38 | Metabolic Scaling | (+) Energy consumption scales with field volume; (-) Energy consumption scales with spike count. | Quantitative | Hybrid |
| 39 | Noise Adjudication | (+) High-fidelity data extracted from noisy field; (-) Data quantized into bits to ignore noise. | Quantitative | Hybrid |
| 40 | Symbolic vs Graded | (+) Stimuli represented as graded magnitudes; (-) Stimuli represented as discrete symbols/bits. | Qualitative | Hybrid |

---

## H3: Modulatory & Chemical Interface (IDs 41--60)

Factors in this group address how neurochemicals control the signal, adjudicating whether they act as "Analog" field-tuners (+1) or "Digital" threshold-shifters (-1).

| ID | Factor Name | Definition | Tag | Contexts |
|----|-------------|------------|-----|----------|
| 41 | Cholinergic SNR Tuning | (+) ACh increases SNR of the Analog field; (-) ACh increases precision of the Digital spike. | Quantitative | Hybrid |
| 42 | Tonic Dopamine State | (+) Tonic levels set Analog gain of the carrier; (-) Phasic bursts act as Digital update triggers. | Quantitative | Hybrid |
| 43 | Ionic Buffer Memory | (+) Extracellular ion clouds store Analog history; (-) Ions strictly support the next Digital trigger. | Quantitative | LFP/Fields |
| 44 | Volume Transmission | (+) Chemicals diffuse to tune Analog fields; (-) Chemicals restricted to Digital synapses. | Qualitative | LFP/Fields |
| 45 | Metabolic Gain Gating | (+) Metabolism scales with Analog field work; (-) Metabolism scales with Digital spike rate. | Quantitative | Hybrid |
| 46 | Glial Noise Cleaning | (+) Astrocytes low-pass filter the Analog field; (-) Glia strictly support Digital metabolic demand. | Qualitative | LFP/Fields |
| 47 | Plasticity Gating | (+) LTP/LTD is gated by Analog carrier phase; (-) Plasticity gated by Digital pre/post timing. | Quantitative | Hybrid |
| 48 | Ionic Conductance Mod | (+) Modulators change continuous Analog conductance; (-) Modulators change discrete Digital thresholds. | Quantitative | Hybrid |
| 49 | Receptor Kinetics | (+) Slow metabotropic receptors integrate Analog data; (-) Fast ionotropic receptors detect Digital events. | Quantitative | Hybrid |
| 50 | SNR Adjudication | (+) Modulators reduce interference in Analog fields; (-) Modulators increase Digital SNR (less noise). | Quantitative | Hybrid |
| 51 | Dopaminergic Gain | (+) DA tunes spatial Analog gain of a column; (-) DA tunes temporal Digital gain of a burst. | Quantitative | Hybrid |
| 52 | Serotonergic State | (+) 5-HT shifts Analog oscillatory baseline; (-) 5-HT shifts Digital firing distribution. | Quantitative | Hybrid |
| 53 | GABAergic Pacing | (+) GABA maintains Analog frequency of carrier; (-) GABA maintains Digital sparsity of the code. | Quantitative | Hybrid |
| 54 | Noradrenergic Arousal | (+) NE increases Analog global field coherence; (-) NE increases Digital local spike precision. | Quantitative | Hybrid |
| 55 | Ion Channel Variability | (+) Stochastic Analog noise used for computation; (-) Channels tuned to minimize Digital bit errors. | Quantitative | Hybrid |
| 56 | Calcium Wave Gating | (+) Analog Ca2+ waves across astrocytes gate field; (-) Calcium transients are triggers for release. | Qualitative | LFP/Fields |
| 57 | Peptidergic Reach | (+) Neuropeptides diffuse across Analog volume; (-) Peptides are restricted to Digital synapses. | Qualitative | LFP/Fields |
| 58 | Extracellular pH | (+) pH shifts continuous Analog field state; (-) pH shifts discrete Digital channel kinetics. | Quantitative | LFP/Fields |
| 59 | Transporter Sequest | (+) Active sequestration cleans Analog fields; (-) Sequestration supports Digital recovery. | Quantitative | Hybrid |
| 60 | Modulator Multiplexing | (+) Different chemicals control different Analog frequencies; (-) Chemicals control different Digital populations. | Quantitative | Hybrid |

---

## Summary Statistics

| Hypothesis Group | ID Range | Total Factors | Quantitative | Qualitative | Methodological |
|------------------|----------|---------------|--------------|-------------|----------------|
| H1: Carrier Identity | 1--20 | 20 | 16 | 4 | 0 |
| H2: Data Representation | 21--40 | 20 | 17 | 3 | 0 |
| H3: Modulatory Interface | 41--60 | 20 | 17 | 3 | 0 |
| **Total** | **1--60** | **60** | **50** | **10** | **0** |
