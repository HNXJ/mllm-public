## Page 1

*For correspondence:
loreen.hertaeg@tu-berlin.de (LHa¨);
h.sprekeler@tu-berlin.de (HS)

Competing interests: The
authors declare that no
competing interests exist.

Funding: See page 18

Received: 03 April 2020
Accepted: 28 July 2020
Published: 21 August 2020

Reviewing editor: Srdjan
Ostojic, Ecole Normale
Superieure Paris, France

Copyright Herta¨g and
Sprekeler. This article is
distributed under the terms of
the Creative Commons
Attribution License, which
permits unrestricted use and
redistribution provided that the
original author and source are
credited.

Learning prediction error neurons in a
canonical interneuron circuit

Loreen Herta¨g1,2*, Henning Sprekeler1,2*

1Modelling of Cognitive Processes, Institute of Software Engineering and
Theoretical Computer Science, Berlin Institute of Technology, Berlin, Germany;
2Bernstein Center for Computational Neuroscience, Berlin, Germany

Abstract Sensory systems constantly compare external sensory information with internally
generated predictions. While neural hallmarks of prediction errors have been found throughout the
brain, the circuit-level mechanisms that underlie their computation are still largely unknown. Here,
we show that a well-orchestrated interplay of three interneuron types shapes the development and
refinement of negative prediction-error neurons in a computational model of mouse primary visual
cortex. By balancing excitation and inhibition in multiple pathways, experience-dependent
inhibitory plasticity can generate different variants of prediction-error circuits, which can be
distinguished by simulated optogenetic experiments. The experience-dependence of the model
circuit is consistent with that of negative prediction-error circuits in layer 2/3 of mouse primary
visual cortex. Our model makes a range of testable predictions that may shed light on the circuitry
underlying the neural computation of prediction errors.

Introduction
Changes in sensory inputs can arise from changes in our environment, but also from our own move-
ments. When you walk through a room full of people, your perspective changes over time, and you
will experience a global visual flow. Superimposed on this global change are local changes gener-
ated by the movements of the people around you. An essential task of sensory perception is to dis-
entangle these different origins of sensory inputs, because the appropriate behavioral responses to
environmental and to self-generated changes are often different. Am I approaching a person or is
she approaching me?

A common assumption is that perceptual systems subtract from the sensory data an internal pre-
diction (Bell, 1981; Rao and Ballard, 1999; Friston, 2005; Spratling, 2010; Franklin and Wolpert,
2011; den Ouden et al., 2012; Kennedy et al., 2014; Keller and Mrsic-Flogel, 2018), which is cal-
culated from an efference copy of the motor signals our brain has issued. Changes in the external
world then take the form of mismatches – or prediction errors – between internal predictions and
sensory data (Wolpert et al., 1995). This comparison requires an accurate prediction system that
adapts to ongoing changes in the environment or in behavior. An efficient way to ensure a flexible
adaptation is to render the prediction circuits experience-dependent by minimizing prediction errors
(Wolpert et al., 2011).

Neural hallmarks of prediction errors are found throughout the brain. Dopaminergic neurons in
the basal ganglia and the striatum (Schultz and Dickinson, 2000) encode a reward prediction error
(mismatch between expected and received reward), and subsets of neurons in visual cortex
(Keller et al., 2012; Zmarz and Keller, 2016; Attinger et al., 2017), auditory cortex (Eliades and
Wang, 2008; Keller and Hahnloser, 2009) and barrel cortex (Ayaz et al., 2019) code for a mis-
match between feedback and feedforward information.

While neural correlates of prediction errors have been found broadly, the circuit level mechanisms
that underlie their computation are poorly understood. Given that prediction errors involve a

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
1 of 30

RESEARCH ARTICLE


---

## Page 2

subtraction of expectations from sensory data (for an alternative implementation employing divisive
inhibition, see Spratling, 2008; Spratling, 2017; Spratling, 2019), the relevant circuits likely involve
both excitatory and inhibitory pathways (Attinger et al., 2017). Negative prediction-error (nPE) neu-
rons, which are activated only when sensory signals are weaker than predicted, are likely to receive
excitatory predictions counterbalanced by inhibitory sensory signals. Conversely, positive prediction-
error (pPE) neurons, which respond only when sensory signals exceed the internal prediction, may
receive excitatory sensory signals counterbalanced by inhibitory predictions (Rao and Ballard, 1999;
Keller and Mrsic-Flogel, 2018). How the complex inhibitory circuits of the cortex (Markram et al.,
2004; Rudy et al., 2011; Pfeffer et al., 2013; Jiang et al., 2015; Tremblay et al., 2016;
Wamsley and Fishell, 2017) support the computations of these prediction errors is not resolved
and neither are the activity-dependent forms of plasticity that would allow these circuits to refine the
prediction machine.

For prediction-error neurons, fully predicted sensory signals should cancel with the internal pre-
diction and hence trigger no response. We therefore hypothesized that an experience-dependent
formation and refinement of prediction-error circuits can be achieved by balancing excitation and
inhibition in an activity-dependent manner. Using a computational model comprised of excitatory
pyramidal cells and three types of inhibitory interneurons, we show that nPE neurons can be learned
by inhibitory synaptic plasticity rules that balance excitation and inhibition in principal cells. We find
that the circuit shows a similar experience dependence as observed in V1 (Attinger et al., 2017).
Depending on which interneuron classes receive motor predictions and which receive sensory sig-
nals, the plasticity rules shape different, fully functional variants of the prediction circuit. Using simu-
lated optogenetic experiments, we show that these variants have identifiable fingerprints in their
reaction to optogenetic activation or inactivation of different interneuron classes. Finally, we demon-
strate that the inhibitory prediction circuits can be learned by biologically plausible forms of homeo-
static inhibitory synaptic plasticity, which only rely on local information available at the synapses.

Results
We studied a rate-based network model of layer 2/3 of rodent V1 to investigate how prediction-
error (PE) neurons develop. In the following, we will focus primarily on negative prediction-error
(nPE) neurons. In V1, nPE neurons have been studied more extensively, which allows us to compare
our results with experimental findings. However, the same approaches and principles derived for
nPE neurons can also be applied to positive prediction-error (pPE) neurons (see Appendix 2—fig-
ures 1 and 2). The network model includes excitatory pyramidal cells (PCs) as well as inhibitory par-
valbumin-expressing
(PV),
somatostatin-expressing
(SOM)
and
vasoactive
intestinal
peptide-
expressing (VIP) interneurons (Figure 1a). The relative abundance of the four cell types and the
probability of the respective synaptic connections are chosen in line with electrophysiological studies
(see Materials and methods). While all inhibitory neurons are modeled as point neurons (Wilson and
Cowan, 1972), we used a two-compartment model for PCs with a rectifying active dendritic process
that allowed nonlinear dynamics akin to dendritic calcium spikes (Murayama et al., 2009) (see Mate-
rials and methods and Appendix 1).

A subset of inhibitory synapses – chosen based on a mathematical analysis (see Materials and
methods, or Appendix 1) – are subject to experience-dependent plasticity, which aims at minimizing
deviations of the PC firing rate from a baseline rate. These deviations can be interpreted as predic-
tion errors. Learning hence strives to adapt the inhibitory circuit such as to reduce these errors.
While the synapses onto both the somatic and dendritic compartments of PCs follow an inhibitory
plasticity rule akin to Vogels et al., 2011, the inhibitory synapses onto PV neurons follow an approxi-
mated backpropagation of error rule akin to Rumelhart et al., 1986. Specifically, the former rule
changes the synapses onto PCs in proportion to the presynaptic interneuron activity and the devia-
tion of PC activity from a baseline rate (see Materials and methods, Equation 14). The latter rule
changes the synapses onto PV neurons in proportion to the presynaptic interneuron activity and the
averaged deviation of the postsynaptic PCs from their baseline rate (see Materials and methods,
Equation 16). Earlier work has shown that such forms of plasticity establish a balance of excitation
and inhibition (Vogels et al., 2011; Mackwood et al., 2020).

All neurons in the model receive excitatory background input that ensures reasonable baseline
activities in the absence of visual input and motor-related internal predictions (‘baseline’). In

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
2 of 30

Research article
Neuroscience


---

## Page 3

a

b

c

d

e

V
V

*

PC

PV

SOM
VIP

*

*
*

Visual input (V)
Motor-related input (M)

b

Figure 1. Balancing excitation and inhibition gives rise to negative prediction-error neurons. (a) Network model
with excitatory PCs and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of
clarity. Somatic compartment of PCs, SOM and PV neurons receive visual input, apical dendrites of PCs and VIP
neurons receive a motor-related prediction thereof. Connections marked with an asterisk undergo experience-
dependent plasticity. (b) During plasticity, the network is exposed to a sequence of feedback (coupled
sensorimotor experience) and playback phases (black square, visual input not predicted by motor commands).
Stimuli last for 1 s and are alternated with baseline phases (absence of visual input and motor predictions). (c) Left:
Before plasticity, somatic excitation (light red) and inhibition (light blue) in PCs are not balanced. Excitatory and
inhibitory currents shifted by ±20 pA for visualization. The varying net excitatory current (gray) causes the PC
population rate to deviate from baseline. Right: Response relative to baseline (DR=R) of all PCs in feedback (FB),
mismatch (MM) and playback (PB) phase, sorted by amplitude of mismatch response. None of the PCs are
classified as nPE neurons (indicated by gray shading to the right). (d) Same as in (c) after plasticity. Somatic
excitation and inhibition are balanced. PC population rate remains at baseline. All PCs classified as nPE neurons
(also indicated by black shading to the right). (e) Left: Mismatch response increases with the difference between
visual and motor input. Right: nPE neuron response during playback does not change with the difference between
visual and motor input but remains at baseline.
The online version of this article includes the following figure supplement(s) for figure 1:

> Figure caption (from PDF text): Figure 1. Balancing excitation and inhibition gives rise to negative prediction-error neurons. (a) Network model
with excitatory PCs and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of
clarity. Somatic compartment of PCs, SOM and PV neurons receive visual input, apical dendrites of PCs and VIP
neurons receive a motor-related prediction thereof. Connections marked with an asterisk undergo experience-
dependent plasticity. (b) During plasticity, the network is exposed to a sequence of feedback (coupled
sensorimotor experience) and playback phases (black square, visual input not predicted by motor commands).
Stimuli last for 1 s and are alternated with baseline phases (absence of visual input and motor predictions). (c) Left:
Before plasticity, somatic excitation (light red) and inhibition (light blue) in PCs are not balanced. Excitatory and
inhibitory currents shifted by ±20 pA for visualization. The varying net excitatory current (gray) causes the PC
population rate to deviate from baseline. Right: Response relative to baseline (DR=R) of all PCs in feedback (FB),
mismatch (MM) and playback (PB) phase, sorted by amplitude of mismatch response. None of the PCs are
classified as nPE neurons (indicated by gray shading to the right). (d) Same as in (c) after plasticity. Somatic
excitation and inhibition are balanced. PC population rate remains at baseline. All PCs classified as nPE neurons
(also indicated by black shading to the right). (e) Left: Mismatch response increases with the difference between
visual and motor input. Right: nPE neuron response during playback does not change with the difference between
visual and motor input but remains at baseline.
The online version of this article includes the following figure supplement(s) for figure 1:
> Figure description (generated): This figure, Figure 1, illustrates a network model demonstrating how balancing excitation and inhibition leads to the emergence of negative prediction-error (nPE) neurons. It is composed of five panels: (a), (b), (c), (d), and (e).

### Panel (a): Network Model Schematic
Panel (a) is a schematic diagram of the neural network model. It shows several neuronal types: PC, SOM, VIP, and PV neurons.
*   **Nodes:** The nodes represent the neuronal compartments: Somatic Compartment (SOM), Apical Dendrites, and Soma.
*   **Inputs:** Arrows indicate inputs:
    *   Visual input (V) targets the Somatic Compartment of PC, SOM, and PV neurons.
    *   Motor-related prediction targets the Apical Dendrites of PC and VIP neurons.
*   **Connections:** Connections are shown between the compartments, although connections from PCs are noted as not being fully shown for clarity.
*   **Plasticity:** Connections marked with an asterisk ($\text{*}$) indicate synapses that undergo experience-dependent plasticity.

### Panel (b): Plasticity Protocol Diagram
Panel (b) illustrates the experimental protocol during plasticity. It is a timeline diagram showing alternating phases:
*   **Visual Input:** A waveform representing visual input is shown at the top.
*   **Motor Prediction:** A corresponding waveform representing motor prediction is shown below the visual input.
*   **Phases:** The diagram indicates two types of phases:
    *   Feedback (FB): Represented by a solid black square, where visual input is predicted by motor commands.
    *   Playback (PB): Represented by a black square, where visual input is *not* predicted by motor commands.
*   **Timing:** Stimuli last for 1 second and are alternated with baseline phases (absence of visual input and motor predictions).

### Panel (c): Before Plasticity
Panel (c) presents data "Before plasticity." It consists of two sub-plots:

**Left Plot (Currents):**
*   **Y-axis:** Current in pA.
*   **X-axis:** Time (s), ranging from 0 to 20 seconds.
*   **Traces:** Three colored traces show somatic excitation and inhibition in PCs:
    *   Light red trace (Somatic Excitation).
    *   Light blue trace (Somatic Inhibition).
    *   Gray trace (Net current), which shows the net excitatory current.
*   **Annotation:** The caption notes that currents are shifted by $\pm 20 \text{ pA}$ for visualization. The gray net current trace shows fluctuations, causing the PC population rate to deviate from baseline.

**Right Plot (Response Sorting):**
*   This plot shows the response relative to baseline ($\Delta R/R$) of all PCs, sorted by amplitude of mismatch response.
*   **X-axis:** Categorical labels: FB (Feedback), MM (Mismatch), and PB (Playback).
*   **Y-axis:** $\Delta R/R$ (Response relative to baseline).
*   **Neurons:** A bar chart representation shows the distribution of PCs across these phases. Gray shading indicates that none of the PCs are classified as nPE neurons.

### Panel (d): After Plasticity
Panel (d) presents data "After plasticity," mirroring the structure of Panel (c).

**Left Plot (Currents):**
*   **Y-axis:** Current in pA.
*   **X-axis:** Time (s), ranging from 0 to 20 seconds.
*   **Traces:** Similar traces for somatic excitation (light red), inhibition (light blue), and net current (gray).
*   **Observation:** The caption notes that somatic excitation and inhibition are balanced, and the PC population rate remains at baseline.

**Right Plot (Response Sorting):**
*   This plot shows the response relative to baseline ($\Delta R/R$) of all PCs, sorted by amplitude of mismatch response.
*   **X-axis:** Categorical labels: FB, MM, and PB.
*   **Y-axis:** $\Delta R/R$.
*   **Neurons:** A bar chart representation shows the distribution of PCs. Black shading indicates that all PCs are classified as nPE neurons.

### Panel (e): Response Characteristics
Panel (e) contains two separate scatter/line plots illustrating the functional properties of nPE neurons.

**Left Plot (Mismatch Response):**
*   **Title:** Mismatch (MM).
*   **Y-axis:** $\Delta R/R$ (%).
*   **X-axis:** $(\text{motor-visual})/\text{motor}$.
*   **Trend:** The plot shows a positive, increasing trend: the mismatch response increases as the ratio of visual to motor input difference increases.

**Right Plot (Playback Response):**
*   **Title:** Playback (PB).
*   **Y-axis:** $\Delta R/R$ (%).
*   **X-axis:** $(\text{visual-motor})/\text{visual}$.
*   **Trend:** The plot shows that the nPE neuron response during playback remains near baseline (around 0%) and does not change significantly with the ratio of visual to motor input difference.

Figure supplement 1. Learning prediction-error circuits with different forms of homeostatic plasticity.
Figure supplement 2. VIP!PV synapses are not required for the formation of nPE neurons.
Figure 1 continued on next page

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
3 of 30

Research article
Neuroscience


---

## Page 4

addition, we stimulated the network with time-varying external inputs representing actual and pre-
dicted visual stimuli (Figure 1a,b). We reasoned that during natural conditions, movements lead to
sensory
inputs
that
are
fully
predicted
by
internal
motor
commands
(‘feedback
phase’,
Attinger et al., 2017), while unexpected external changes in the environment should generate
unpredicted sensory signals (‘playback phase’, Attinger et al., 2017). Situations in which internal
motor commands are not accompanied by corresponding sensory signals should be rare (‘feedback
mismatch phase’, Attinger et al., 2017). During plasticity, we therefore stimulated the circuit with a
sequence consisting of feedback and playback phases (‘quasi-natural training’, Figure 1b).

Figure 1 continued

Figure supplement 3. Balancing excitation, somatic and dendritic inhibition gives rise to nPE neurons in a model
in which an excess of dendritic inhibition is forwarded to the soma.

Excitation

Inhibition

Exc

Inh

Input pathway
Visual input (V)

Motor input (M)

?

?
?

PC
PV

SOM

VIP

M
V

PC
PV
PC

M
V

PV

M
V

PC
PV

M
V

PC
PV

VIPĺPVĺ3&

SOMĺPVĺ3&

PVĺ3&

SOMĺVIPĺ39ĺ3& 
VIPĺSOMĺ39ĺ3&

a

b

c

e

d

f

Figure 2. Multi-pathway balance of excitation and inhibition in different nPE neuron circuits. (a) Excitatory,
inhibitory, disinhibitory and dis-disinhibitory pathways onto PCs that need to be balanced in nPE neuron circuits.
Input to the soma of PCs and PV neurons is varied (c–f). SOM neurons receive visual input, VIP neurons receive a
motor-related prediction. (b) Test stimuli: Feedback (FB), mismatch (MM) and playback (PB) phases of 1 s each. (c)
PCs and PV neurons receive visual input (left, top). When all visual (V) and motor (M) pathways are balanced (left,
bottom), PCs act as nPE neurons (right). PV neuron activity increases in both feedback and playback phases.
Responses normalized between  1 and 1 such that baseline is zero. (d) Same as in (c) but PV neurons receive
motor predictions. (e) Same as in (c) but PCs receive no visual input. PV neurons remain at baseline in the absence
of visual input to the soma of PCs. (f) Same as in (c) but PCs receive no visual input and PV neurons receive motor
predictions. PV neurons remain at baseline in the absence of visual input to the soma of PCs.
The online version of this article includes the following figure supplement(s) for figure 2:

> Figure caption (from PDF text): Figure 2. Multi-pathway balance of excitation and inhibition in different nPE neuron circuits. (a) Excitatory,
inhibitory, disinhibitory and dis-disinhibitory pathways onto PCs that need to be balanced in nPE neuron circuits.
Input to the soma of PCs and PV neurons is varied (c–f). SOM neurons receive visual input, VIP neurons receive a
motor-related prediction. (b) Test stimuli: Feedback (FB), mismatch (MM) and playback (PB) phases of 1 s each. (c)
PCs and PV neurons receive visual input (left, top). When all visual (V) and motor (M) pathways are balanced (left,
bottom), PCs act as nPE neurons (right). PV neuron activity increases in both feedback and playback phases.
Responses normalized between  1 and 1 such that baseline is zero. (d) Same as in (c) but PV neurons receive
motor predictions. (e) Same as in (c) but PCs receive no visual input. PV neurons remain at baseline in the absence
of visual input to the soma of PCs. (f) Same as in (c) but PCs receive no visual input and PV neurons receive motor
predictions. PV neurons remain at baseline in the absence of visual input to the soma of PCs.
The online version of this article includes the following figure supplement(s) for figure 2:
> Figure description (generated): This figure, Figure 2, illustrates the multi-pathway balance of excitation and inhibition in different nPE neuron circuits. It is composed of several panels: (a), (b), (c), (d), (e), and (f).

### Panel (a)
Panel (a) is a schematic diagram illustrating different pathways onto PCs. It lists several pathway types:
*   Excitatory ($\text{V} \to \text{PC}$)
*   Inhibitory ($\text{PV} \to \text{PC}$)
*   Disinhibitory ($\text{C} \to \text{PC}$, where C likely refers to a control or context pathway)
*   Dis-disinhibitory ($\text{VIP} \to \text{PV} \to \text{PC}$)
*   $\text{OM} \to \text{PV} \to \text{PC}$

### Panel (b)
Panel (b) is a schematic representing test stimuli phases, depicted as horizontal bars over time. The stimulus types are labeled above the timeline:
*   **FB**: Feedback phase (1 s duration)
*   **MM**: Mismatch phase (1 s duration)
*   **PB**: Playback phase (1 s duration)

Below the timeline, there are two input lines:
*   **Motor prediction (M)**: Represented by an orange line.
*   **Visual input (V)**: Represented by a teal/cyan line.

### Panel (c)
Panel (c) shows the neural circuit activity when all visual ($\text{V}$) and motor ($\text{M}$) pathways are balanced, resulting in PCs acting as nPE neurons.
*   **Circuit Schematic (Left):** A schematic shows three nodes: PC, PV, and a third node (implied context/input). Arrows indicate connections.
*   **Time Course Plots (Right):** Three time-series plots are shown, corresponding to the stimulus phases in Panel (b).
    *   **PC:** Shows activity over time, with distinct patterns during FB, MM, and PB.
    *   **PV:** Shows activity over time, with distinct patterns during FB, MM, and PB.
    *   **SOM:** Shows activity over time (likely related to SOM neurons).
    *   **VIP:** Shows activity over time.

### Panel (d)
Panel (d) presents a comparison of pathway strength when PV neurons receive motor predictions ($\text{M}$).
*   **Circuit Schematic (Left):** A schematic shows PC and PV nodes connected. An arrow points from an external source labeled 'M' towards the PV node, and another input (implied visual) points to PC.
*   **Bar Graph (Bottom Left):** A bar graph titled "Pathway stgth" is displayed.
    *   The x-axis shows two conditions: 'V' and 'M'.
    *   The y-axis is labeled "Pathway stgth" (ranging from 0 to 2).
    *   For condition 'V', there are two bars: one brown (PC input) and one orange (PV input).
    *   For condition 'M', there are two bars: one red (PC input) and one dark blue (PV input).
*   **Time Course Plots (Right):** Four time-series plots are shown, corresponding to the stimulus phases:
    *   **PC:** Shows activity over time.
    *   **PV:** Shows activity over time.
    *   **SOM:** Shows activity over time.
    *   **VIP:** Shows activity over time.

### Panel (e)
Panel (e) shows the scenario where PCs receive no visual input.
*   **Circuit Schematic (Left):** A schematic shows PC and PV nodes connected, similar to Panel (d).
*   **Bar Graph (Bottom Left):** A bar graph titled "Pathway stgth" is displayed.
    *   The x-axis shows two conditions: 'V' and 'M'.
    *   The y-axis is labeled "Pathway stgth" (ranging from 0 to 2).
    *   For condition 'V', there is one brown bar.
    *   For condition 'M', there are two bars: one red and one dark blue.
*   **Time Course Plots (Right):** Four time-series plots are shown: PC, PV, SOM, and VIP activity over the stimulus phases.

### Panel (f)
Panel (f) shows the scenario where PCs receive no visual input AND PV neurons receive motor predictions.
*   **Circuit Schematic (Left):** A schematic shows PC and PV nodes connected, similar to Panel (d).
*   **Bar Graph (Bottom Left):** A bar graph titled "Pathway stgth" is displayed.
    *   The x-axis shows two conditions: 'V' and 'M'.
    *   The y-axis is labeled "Pathway stgth" (ranging from 0 to 2).
    *   For condition 'V', there is one brown bar.
    *   For condition 'M', there are two bars: one red and one dark blue.
*   **Time Course Plots (Right):** Four time-series plots are shown: PC, PV, SOM, and VIP activity over the stimulus phases.

> Figure caption (from PDF text): Figure 2. Multi-pathway balance of excitation and inhibition in different nPE neuron circuits. (a) Excitatory,
inhibitory, disinhibitory and dis-disinhibitory pathways onto PCs that need to be balanced in nPE neuron circuits.
Input to the soma of PCs and PV neurons is varied (c–f). SOM neurons receive visual input, VIP neurons receive a
motor-related prediction. (b) Test stimuli: Feedback (FB), mismatch (MM) and playback (PB) phases of 1 s each. (c)
PCs and PV neurons receive visual input (left, top). When all visual (V) and motor (M) pathways are balanced (left,
bottom), PCs act as nPE neurons (right). PV neuron activity increases in both feedback and playback phases.
Responses normalized between  1 and 1 such that baseline is zero. (d) Same as in (c) but PV neurons receive
motor predictions. (e) Same as in (c) but PCs receive no visual input. PV neurons remain at baseline in the absence
of visual input to the soma of PCs. (f) Same as in (c) but PCs receive no visual input and PV neurons receive motor
predictions. PV neurons remain at baseline in the absence of visual input to the soma of PCs.
The online version of this article includes the following figure supplement(s) for figure 2:
> Figure description (generated): This figure, labeled as Figure 2, illustrates the multi-pathway balance of excitation and inhibition in different nPE neuron circuits. It is divided into several panels, specifically focusing on panel (c) and panel (e).

### Overall Layout & Structure
The figure is structured into two main sections, corresponding to panels (c) and (e). Each panel combines a schematic diagram of neural pathways with corresponding raster plots or time-series activity traces.

### Panel (c) Description
**Schematic Diagram (Left Side):**
This section depicts a circuit diagram showing inputs to two types of neurons: PC and PV.
1.  **Nodes:** There are three main nodes represented by triangles/circles: PC, PV, and a general input node (implied or associated with the pathways).
2.  **Pathways:** Arrows indicate connections:
    *   An arrow points from a source (implied input) to PC.
    *   A separate pathway shows an arrow originating from a source and pointing towards PV, which is connected to PC.
3.  **Pathway Balance Bar Chart (Below Schematic):** Below the schematic, there is a bar chart illustrating pathway balance:
    *   The x-axis labels are **V** and **M**.
    *   For **V**, there is a red bar labeled "Excitation" and a blue bar labeled "Inhibition."
    *   For **M**, there is a red bar labeled "Excitation" and a blue bar labeled "Inhibition."
    *   The y-axis is labeled **Pathway stgth** (Strength), ranging from 0 to 3.

**Activity Traces (Right Side):**
This section displays time-series activity traces for several neuron types across a temporal sequence (implied by the caption to be Feedback, Mismatch, and Playback phases).
1.  **Neurons Traced:** PC, PV, SOM, and VIP neurons are shown.
2.  **Activity Plotting:** Each neuron has a corresponding trace showing activity over time, segmented into distinct phases (indicated by shaded vertical bars).
    *   The traces show fluctuating activity levels, normalized between 0 and 1 (as per the caption).
    *   The shaded regions appear to delineate specific experimental phases.

### Panel (e) Description
**Schematic Diagram (Left Side):**
This section mirrors the structure of panel (c) but represents a modified circuit.
1.  **Nodes:** PC and PV nodes are present, similar to panel (c).
2.  **Pathway Balance Bar Chart (Below Schematic):** A bar chart is present, structured identically to panel (c)'s balance chart:
    *   The x-axis labels are **V** and **M**.
    *   For **V**, there is a red bar labeled "Excitation" and a blue bar labeled "Inhibition."
    *   For **M**, there is a red bar labeled "Excitation" and a blue bar labeled "Inhibition."
    *   The y-axis is labeled **Pathway stgth** (Strength), ranging from 0 to 3.

**Activity Traces (Right Side):**
This section displays time-series activity traces for the same neuron types: PC, PV, SOM, and VIP.
1.  **Activity Plotting:** Similar to panel (c), the traces show activity over time, segmented by shaded phases.
2.  **Observed Trend:** The traces in panel (e) show a distinct pattern compared to panel (c), particularly noting the baseline activity of PV neurons.

### Summary of Key Elements and Labels
*   **Neuron Types:** PC (Principal Cells), PV, SOM, VIP.
*   **Pathway Components:** Excitation (Exc), Inhibition (Inh).
*   **Inputs/Conditions:** V (Visual input) and M (Motor prediction).
*   **Axes:** Pathway stgth (Strength), Normalized activity traces (0 to 1).
*   **Contextual Interpretation (from caption):** Panel (c) represents the case where PCs and PV neurons receive visual input, and all pathways are balanced. Panel (e) represents the case where PCs receive no visual input.

> Figure caption (from PDF text): Figure 2. Multi-pathway balance of excitation and inhibition in different nPE neuron circuits. (a) Excitatory,
inhibitory, disinhibitory and dis-disinhibitory pathways onto PCs that need to be balanced in nPE neuron circuits.
Input to the soma of PCs and PV neurons is varied (c–f). SOM neurons receive visual input, VIP neurons receive a
motor-related prediction. (b) Test stimuli: Feedback (FB), mismatch (MM) and playback (PB) phases of 1 s each. (c)
PCs and PV neurons receive visual input (left, top). When all visual (V) and motor (M) pathways are balanced (left,
bottom), PCs act as nPE neurons (right). PV neuron activity increases in both feedback and playback phases.
Responses normalized between  1 and 1 such that baseline is zero. (d) Same as in (c) but PV neurons receive
motor predictions. (e) Same as in (c) but PCs receive no visual input. PV neurons remain at baseline in the absence
of visual input to the soma of PCs. (f) Same as in (c) but PCs receive no visual input and PV neurons receive motor
predictions. PV neurons remain at baseline in the absence of visual input to the soma of PCs.
The online version of this article includes the following figure supplement(s) for figure 2:
> Figure description (generated): Based on the provided information, which includes a DOI and an associated caption but no actual image of Figure 2, I must rely entirely on the detailed description provided in the caption to construct a comprehensive structural and functional description.

Here is the exhaustive description based on the provided text:

***

## Figure 2 Description: Multi-pathway balance of excitation and inhibition in different nPE neuron circuits

**1. Overall Layout & Structure:**
The figure is structured into multiple distinct panels, labeled (a) through (f), suggesting a multi-part schematic or set of experimental results illustrating the balance between excitation and inhibition in nPE (presumably "neuronal population encoding" or similar) neuron circuits. The structure appears to combine schematic representations of neural pathways with functional plots/graphs showing activity changes under different conditions.

**2. Visual Components & Symbols (Inferred from Caption):**
*   **Neural Circuit Schematic (Panel a):** This panel likely depicts the fundamental connectivity. It illustrates various pathways onto "PCs" (presumably Principal Cells) that require balancing. These pathways are categorized as:
    *   Excitatory pathways
    *   Inhibitory pathways
    *   Disinhibitory pathways
    *   Dis-disinhibitory pathways
    *   The schematic shows inputs directed towards PCs.
*   **Input/Stimulus Representation (Panel b):** This panel likely illustrates the experimental timing or stimulus structure. It mentions three test stimuli phases: Feedback (FB), Mismatch (MM), and Playback (PB), each lasting 1 second.
*   **Functional Plots/Conditions (Panels c–f):** These panels appear to be time-series plots or comparative graphs showing neural activity.
    *   **Cell Types:** PCs and PV neurons are central components being measured. SOM neurons receive visual input, and VIP neurons receive a motor-related prediction.
    *   **Inputs:** Visual (V) and Motor (M) pathways are explicitly mentioned as inputs.
    *   **Activity Representation:** The activity is normalized between 0 and 1, with a baseline set at zero.

**3. Labels, Keys & Legends:**
*   **Cell Types/Nodes:** PCs (Principal Cells), PV neurons, SOM neurons, VIP neurons.
*   **Inputs/Pathways:** Visual input (V), Motor prediction (M).
*   **Experimental Phases:** Feedback (FB), Mismatch (MM), Playback (PB).
*   **Conditions/States:** Balanced state (when all V and M pathways are balanced), absence of visual input.
*   **Normalization:** Responses are normalized between 0 and 1, with baseline set to zero.

**4. Data Trends & Details (Specific Panel Descriptions):**
*   **(Panel c):** Shows the state when PCs and PV neurons receive visual input (indicated as "left, top"). When all V and M pathways are balanced ("left, bottom"), PCs function as nPE neurons (indicated as "right"). A key finding noted is that PV neuron activity *increases* in both the feedback (FB) and playback (PB) phases under these balanced conditions.
*   **(Panel d):** This panel is identical to (c) in structure but specifies that PV neurons receive motor predictions instead of the general conditions described in (c).
*   **(Panel e):** This panel shows a condition where PCs receive *no visual input*. The result observed is that PV neurons remain at baseline activity.
*   **(Panel f):** This panel combines two conditions: PCs receive *no visual input*, AND PV neurons receive motor predictions. The result observed is that PV neurons remain at baseline activity.

**5. Contextual Caption Integration Summary:**
Figure 2 comprehensively maps the functional requirements for nPE neuron operation. Panel (a) defines the necessary balance of excitatory, inhibitory, disinhibitory, and dis-disinhibitory inputs onto PCs. Panels (c) through (f) test this balance by systematically varying the presence of visual input to PCs and motor predictions to PV neurons, demonstrating that functional nPE behavior (as seen in Panel c) requires the coordinated input of both visual and motor pathways, as deviations (Panels e and f) lead to a loss of activity in PV neurons.

Figure supplement 1. Multi-pathway balance of excitation and inhibition in different nPE neuron circuits with both
visual and motor input onto PV neurons.

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
4 of 30

Research article
Neuroscience


---

## Page 5

Negative prediction-error neurons emerge by balancing excitation and
inhibition
Before the onset of plasticity, synaptic connections were randomly initialized, leading to PCs receiv-
ing unbalanced excitation and inhibition. Therefore, all PCs change their firing rate in response to
both feedback and playback stimuli, indicating the absence of nPE neurons (Figure 1c). During
quasi-natural sensorimotor experience, inhibitory plasticity strengthens or weakens inhibitory synap-
ses to diminish the firing rate deviations of PCs from their baseline firing rate (Figure 1—figure sup-
plement 1). At the same time, dendritic inhibition mediated by SOM interneurons was sufficiently
strengthened to suppress the motor prediction arriving at the apical dendrite. After synaptic plastic-
ity, somatic excitation and inhibition are balanced on a stimulus-by-stimulus basis (Figure 1d–e). PCs
merely show small and transient onset/offset responses to feedback and playback stimuli. In con-
trast, all PCs show an increase in activity for feedback mismatch stimuli (Figure 1d), which scales
with the size of the difference between actual and predicted visual input (Figure 1e). Hence, inhibi-
tory synaptic plasticity generates nPE neurons by balancing excitation and inhibition in PCs for
quasi-natural conditions.

Balance of excitation, inhibition and disinhibition in different functional
prediction circuits
The circuit we studied so far was motivated by the widely accepted view that PCs and SOM and PV
interneurons show visual responses (Ko et al., 2011; Yang et al., 2013; Larkum, 2013a; Xue et al.,
2014; Harris and Shepherd, 2015; Lee et al., 2016; Attinger et al., 2017), while long-range
(motor) predictions arrive in the superficial layers of V1 and target VIP neurons (Fu et al., 2014;
Harris and Shepherd, 2015; Tremblay et al., 2016; Attinger et al., 2017) and the apical and distal
compartments of PCs (Larkum, 2013a; Leinweber et al., 2017; Attinger et al., 2017). Because this
view is not uncontested (Fu et al., 2014) and it has been shown that interneuron types can receive
both feedforward and feedback inputs (Wall et al., 2016), we systematically varied the inputs to the
different neuron classes. We first studied circuit variations in which PCs and PV neurons receive visual
and/or motor signals (Figure 2, see also Figure 2—figure supplement 1).

We found that inhibitory plasticity establishes nPE neurons independent of the input configura-
tion onto PCs and PV neurons (Figure 2c–f, right). The emerging connectivity of the interneuron cir-
cuits varied, however. For PCs not to respond above baseline in feedback and playback phase,
various excitatory, inhibitory, disinhibitory and dis-disinhibitory pathways need to be balanced. An
informative example is the input configuration in which PCs receive visual input and PV neurons
receive motor predictions (Figure 2d). In this case, visual inputs arrive at the PCs as direct excitation,
as disinhibition through the SOM-PV pathway, and as dis-disinhibition via the SOM-VIP-PV pathway
(Figure 2a). To keep the PCs at their baseline during the playback phase, these three pathways
need to be balanced (Figure 2d, left). Similarly, motor signals arrive at the PCs as inhibition from PV
neurons, dis-inhibition via the VIP-PV pathway, dis-dis-inhibition via the VIP-SOM-PV pathway and as
direct excitation to the dendrite that is canceled by SOM-mediated inhibition. Again, all these path-
ways need to be balanced to keep the PCs at their baseline for fully predicted visual stimuli
(Figure 2d, left). Analog balancing arguments hold for other input configurations (Figure 2c–f, left).
Note that this multi-pathway balance applies primarily to somatic inputs to PCs. During feedback
and playback phases, this provides a complete picture, because the dendrites are deactivated by
inhibition. During mismatch phases, this dendritic inhibition is withdrawn and the dendrites provide
additional excitatory input to the soma that can drive mismatch responses.

While the flow of visual and motor information in the learned inhibitory microcircuit is different
for different input configurations, the neural responses of the different interneuron classes provide
limited information about the input configuration. PV neuron activity reflects whether PCs receive
visual input: If PCs receive visual input, PV responses increase during feedback and playback phases
to balance the sensory input at the soma of PCs (Figure 2c–d, right). If PCs receive no visual input,
PV neurons remain at their baseline firing rate (Figure 2e–f, right), which is in contradiction to the
experimentally observed increase of PV neurons during feedback (see Attinger et al., 2017). The
activity of SOM and VIP neurons varies between playback, feedback and mismatch phases (in line
with experimental results, see Attinger et al., 2017), but is independent of the input configuration
for PCs and PV interneurons (Figure 2c–f, right).

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
5 of 30

Research article
Neuroscience


---

## Page 6

In summary, inhibitory plasticity can establish functional nPE circuits irrespective of the inputs
onto the soma of PCs and PV neurons. Although the underlying circuits vary substantially in the spe-
cific balance of pathways, the neural activity patterns only weakly reflect the underlying information
flow.

Simulated optogenetic manipulations disambiguate prediction-error
circuits
We hypothesized that the need to simultaneously balance several pathways offers a way to disam-
biguate the different prediction-error circuits by optogenetic manipulations. To test this, we system-
atically suppressed or activated PV, SOM and VIP interneurons in each input configuration after
inhibitory plasticity had established the respective nPE circuit.

We found that in our model, such simulated optogenetic experiments are highly informative
about the underlying input configuration (Figure 3). For example, PV neuron inactivation changes
the response of nPE neurons during feedback, playback and mismatch phases if and only if the PCs
receive visual inputs. VIP inactivation renders nPE neurons silent unless PV neurons receive motor
predictions, in which case they are transformed into positive prediction-error (pPE) neurons. Since

Figure 3. Simulated optogenetic manipulations of PV, SOM and VIP neurons disambiguate prediction-error
circuits. (a) Left: nPE neuron circuit in which PCs and PV neurons receive visual input. Inactivation (middle) or
activation (right) of PV (first row), SOM (second row) or VIP neurons (third row). Optogenetic manipulations change
responses of nPE neurons (Ctrl) in feedback, mismatch and playback phases. Responses normalized between  1
and 1 such that baseline is zero. Inactivation input is -8 s 1. Activation input is 5 s 1. (b) Same as in (a) but PV
neurons receive motor-related prediction. (c) Same as in (a) but PCs receive no visual input. (d) Same as in (a) but
PCs receive no visual input and PV neurons receive a motor-related prediction.
The online version of this article includes the following figure supplement(s) for figure 3:

> Figure caption (from PDF text): Figure 3. Simulated optogenetic manipulations of PV, SOM and VIP neurons disambiguate prediction-error
circuits. (a) Left: nPE neuron circuit in which PCs and PV neurons receive visual input. Inactivation (middle) or
activation (right) of PV (first row), SOM (second row) or VIP neurons (third row). Optogenetic manipulations change
responses of nPE neurons (Ctrl) in feedback, mismatch and playback phases. Responses normalized between  1
and 1 such that baseline is zero. Inactivation input is -8 s 1. Activation input is 5 s 1. (b) Same as in (a) but PV
neurons receive motor-related prediction. (c) Same as in (a) but PCs receive no visual input. (d) Same as in (a) but
PCs receive no visual input and PV neurons receive a motor-related prediction.
The online version of this article includes the following figure supplement(s) for figure 3:
> Figure description (generated): ## Figure 3 Description: Simulated Optogenetic Manipulations of PV, SOM, and VIP Neurons

This figure presents a set of four panels (a, b, c, d) illustrating simulated optogenetic manipulations within different neural circuit contexts. Each panel combines a schematic diagram of the neuronal circuitry with corresponding heatmaps representing changes in PC activity following these manipulations.

### Overall Layout and Structure
The figure is structured into four main sections, labeled (a), (b), (c), and (d). Each section follows a consistent structure:
1. **Circuit Schematic:** A small diagram illustrating the connectivity of key neuronal types (PC, PV, SOM, VIP, V, M).
2. **Activity Heatmaps:** Three rows of heatmaps corresponding to the manipulation of PV, SOM, and VIP neurons, respectively.
3. **Activity Trace Plots:** A final row of line plots showing the normalized PC rate over time, corresponding to the circuit context.

### Visual Components & Symbols (Circuit Schematics)
The schematics use stylized shapes to represent different neuronal populations:
* **PC (Pyramidal Cells):** Represented by a triangle.
* **PV, SOM, VIP:** These are shown as nodes connected to the PC and other elements.
* **V (Visual Input):** Represented by a small, light-colored shape (likely an input source).
* **M (Motor Output):** Represented by a small, dark-colored shape (likely an output target).

Arrows indicate directional flow or influence between these nodes. The specific connectivity changes across panels (a) through (d) define the experimental context:

* **Panel (a):** PC and PV neurons receive visual input ($\text{V}$).
* **Panel (b):** PV neurons receive motor-related prediction, while PC receives visual input.
* **Panel (c):** PCs receive no visual input ($\text{V}$ is absent or disconnected from PC).
* **Panel (d):** PCs receive no visual input, and PV neurons receive a motor-related prediction.

### Visual Components & Symbols (Heatmaps)
Each panel contains three rows of heatmaps, representing the effect of manipulating specific interneuron types:

1. **Top Row (PV Manipulation):** Shows the effect of manipulating PV neurons.
2. **Middle Row (SOM Manipulation):** Shows the effect of manipulating SOM neurons.
3. **Bottom Row (VIP Manipulation):** Shows the effect of manipulating VIP neurons.

The heatmaps display activity changes over time (implied x-axis, though not explicitly labeled with units) and are color-coded based on the **Normalized PC rate**.
* **Color Scale:** A horizontal bar below the heatmaps indicates the normalization scale: $-1$ (darkest color, representing strong decrease) to $0$ (white/light gray, baseline) to $+1$ (darkest color, representing strong increase).

The heatmaps are further divided into three distinct temporal phases: **Feedback**, **Mismatch**, and **Playback**. These phases are visually separated within the heatmap structure.

### Data Trends & Details (Activity Trace Plots)
Below the heatmaps in each panel, there is a single line plot showing the **Normalized PC rate** over time. This trace appears to be segmented into temporal phases corresponding to the heatmap structure (Feedback, Mismatch, Playback).

* **X-axis:** Represents time progression across the phases.
* **Y-axis:** Represents the Normalized PC rate (ranging from approximately -1 to +1).
* **Lines/Traces:** The plots show distinct temporal patterns, often exhibiting characteristic shapes (e.g., sustained activity or transient bursts) across the different phases for each circuit configuration.

### Contextual Caption Integration
The caption clarifies several elements:
* **Manipulation:** The heatmaps show the effect of *inactivation* (middle column/state) or *activation* (right column/state) of PV, SOM, and VIP neurons.
* **Normalization:** Responses are normalized between $-1$ and $+1$, with the baseline set to zero.
* **Input Values:** The specific input values used for manipulation are provided: Inactivation input is $-8 \text{ s}^{-1}$, and Activation input is $5 \text{ s}^{-1}$.
* **Circuit Contexts:** The panels correspond to specific circuit configurations:
    * (a): nPE neuron circuit where PCs and PV neurons receive visual input.
    * (b): Same as (a), but PV neurons receive motor-related prediction.
    * (c): Same as (a), but PCs receive no visual input.
    * (d): Same as (a), but PCs receive no visual input and PV neurons receive a motor-related prediction.

> Figure caption (from PDF text): Figure 3. Simulated optogenetic manipulations of PV, SOM and VIP neurons disambiguate prediction-error
circuits. (a) Left: nPE neuron circuit in which PCs and PV neurons receive visual input. Inactivation (middle) or
activation (right) of PV (first row), SOM (second row) or VIP neurons (third row). Optogenetic manipulations change
responses of nPE neurons (Ctrl) in feedback, mismatch and playback phases. Responses normalized between  1
and 1 such that baseline is zero. Inactivation input is -8 s 1. Activation input is 5 s 1. (b) Same as in (a) but PV
neurons receive motor-related prediction. (c) Same as in (a) but PCs receive no visual input. (d) Same as in (a) but
PCs receive no visual input and PV neurons receive a motor-related prediction.
The online version of this article includes the following figure supplement(s) for figure 3:
> Figure description (generated): Based on the provided information, which includes a DOI and an associated caption but no actual image of Figure 3, I must rely entirely on the detailed description provided in the caption to construct a comprehensive structural and functional description of what the figure *represents*.

Since I cannot see the visual elements (plots, schematics, etc.), this description will detail the *intended structure* based on the caption's narrative.

---

## Exhaustive Description of Figure 3 (Inferred from Caption)

**Figure Title/Context:** Simulated optogenetic manipulations of PV, SOM and VIP neurons disambiguate prediction-error circuits.

**Overall Layout & Structure:**
The figure is structured into four distinct sub-panels: (a), (b), (c), and (d). These panels appear to be comparative schematics or sets of plots illustrating the effects of specific experimental manipulations on neural circuit responses. The structure suggests a comparison across different input conditions and cell types being manipulated.

**Visual Components & Symbols (Inferred):**
The figure likely utilizes schematic representations of neural circuits, possibly combined with time-series plots to show neuronal responses.

*   **Neural Components:** The caption explicitly mentions several cell types: **PV neurons**, **SOM neurons**, **VIP neurons**, and **nPE neurons** (the target of the response measurement).
*   **Inputs/Stimuli:** The circuits involve different types of input: **visual input**, **motor-related prediction**, and the absence of certain inputs (e.g., "PCs receive no visual input").
*   **Manipulations:** The core manipulation involves **optogenetic manipulations**, which are categorized as:
    *   **Inactivation:** Represented by a specific input value of **$-8 \text{ s}\sigma_1$**.
    *   **Activation:** Represented by a specific input value of **$+5 \text{ s}\sigma_1$**.
*   **Phases:** The responses are analyzed across three distinct temporal phases: **feedback**, **mismatch**, and **playback**.
*   **Normalization:** Responses are normalized between $0$ and $1$, with the baseline set to zero.

**Panel-Specific Configurations (Based on Caption):**

*   **Panel (a): Baseline Circuit:**
    *   **Circuit Description:** The nPE neuron circuit where **PCs and PV neurons receive visual input**.
    *   **Manipulations Shown:** The panel compares three conditions across the rows:
        1.  Inactivation of **PV** neurons (First row).
        2.  Manipulation of **SOM** neurons (Second row).
        3.  Manipulation of **VIP** neurons (Third row).
    *   **Measurement:** The figure shows how these manipulations change the responses of **nPE neurons (Ctrl)** across the feedback, mismatch, and playback phases.

*   **Panel (b): Motor Prediction Input:**
    *   **Circuit Description:** Identical to Panel (a), but with a critical change: **PV neurons receive motor-related prediction** instead of or in addition to visual input.

*   **Panel (c): Visual Input Removal:**
    *   **Circuit Description:** Identical to Panel (a), but with the condition that **PCs receive no visual input**.

*   **Panel (d): Combined Input Change:**
    *   **Circuit Description:** A combination of changes: **PCs receive no visual input AND PV neurons receive a motor-related prediction**.

**Labels, Keys & Legends:**
*   **Cell Types:** PV, SOM, VIP, nPE (and PCs).
*   **Input Modalities:** Visual input, Motor-related prediction.
*   **Experimental Conditions/Manipulations:** Inactivation ($-8 \text{ s}\sigma_1$), Activation ($+5 \text{ s}\sigma_1$).
*   **Temporal Phases:** Feedback, Mismatch, Playback.
*   **Normalization Scale:** Responses normalized between $0$ and $1$.

**Data Trends & Details (Inferred from Description):**
The figure's primary function is to demonstrate how the specific optogenetic manipulations (inactivation/activation of PV, SOM, or VIP) alter the temporal response patterns (feedback, mismatch, playback) of nPE neurons under various input conditions (visual vs. motor prediction). The visual data would show the magnitude and timing of these changes relative to the normalized baseline.

Figure supplement 1. Net currents in PCs after in/activation of PV, SOM or VIP neurons elucidate prediction-error
circuits.

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
6 of 30

Research article
Neuroscience


---

## Page 7

SOM and VIP neurons are mutually inhibiting (see e.g. Pfeffer et al., 2013), the same information
can be gained by an over-activation of SOM neurons that effectively silences VIP neurons.

Changes in neuronal activity due to optogenetic manipulations depend on a variety of factors
such as baseline firing rates and saturation effects (Phillips and Hasenstaub, 2016). For instance,
while an excess of inhibition is not observable when PCs exhibit vanishingly small baseline activity, it
leads to a firing rate decrease otherwise. Moreover, in/activation of interneuron types within a recur-
rent network may also have ambiguous consequences contingent on potential saturation effects in
other cell types. These ambiguities can be partially resolved by measuring currents rather than firing
rates, during baseline, feedback, mismatch and playback phases. Indeed, we found that the net cur-
rents in PCs after in/activation of PV, SOM or VIP neurons are highly informative about the underly-
ing input configuration (Figure 3—figure supplement 1).

When we compared our results with optogenetic experiments in which SOM or VIP neurons are
either inactivated or activated during mismatch or running (Attinger et al., 2017), it shows that a
homogeneous input configuration in which all PCs receive visual input while all PV neurons receive a
motor-related prediction thereof is unlikely (Figure 3b). All other variants of nPE circuits exhibit mis-
match responses during SOM/VIP neuron manipulation that are in line with the ones observed
experimentally. However, the responses observed in the feedback phase (when compared with ‘dur-
ing running’, see Attinger et al., 2017) deviate from all the conditions we simulated, indicating that
the interneurons do not receive exclusively sensory or motor inputs, but rather a combination of
actual and predicted visual input.

In summary, our model predicts that optogenetic experiments may unveil a unique fingerprint for
nPE circuits that differ in their inputs onto PCs and PV neurons.

Fraction of nPE neurons is modulated by inputs to SOM and VIP
interneurons
In the model considered so far, all PCs developed into nPE neurons during learning, irrespective of
the inputs to PCs and PV interneurons. However, nPE neurons represent only a small fraction of neu-
rons in mouse V1 (Keller et al., 2012; Saleem et al., 2013; Zmarz and Keller, 2016;
Attinger et al., 2017). Given that in our model, motor predictions arriving at the apical dendrites
are canceled by SOM neuron-mediated inhibition, we hypothesized that the fraction of PCs that
develop into nPE neurons depends on the distribution of visual and motor input onto SOM and VIP
neurons.

To test this, we allow neurons of both SOM and VIP populations to receive either visual input or a
motor prediction thereof. A fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive

a
b
M

V
V

*

PC

PV

SOM
VIP

*

*
*

M
V

f
f
(1-f)

b

Neurons

nPE
non-nPE

Figure 4. Fraction of nPE neurons depends on SOM and VIP neuron inputs. (a) Network model with excitatory PCs
and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of clarity. Somatic
compartment of PCs, PV neurons, a fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive visual
input. The remaining SOM and VIP neurons receive motor predictions. (b) Response relative to baseline (DR=R) of
all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response. The fraction of
nPE neurons that develop during learning decreases with f (also indicated by black and gray shading to the right).
The increasing fraction of non-nPE neurons comprises neurons that remain at their baseline in all three phases,
show a suppression during mismatch or develop into positive prediction-error neurons that respond only during
playback.

> Figure caption (from PDF text): Figure 4. Fraction of nPE neurons depends on SOM and VIP neuron inputs. (a) Network model with excitatory PCs
and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of clarity. Somatic
compartment of PCs, PV neurons, a fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive visual
input. The remaining SOM and VIP neurons receive motor predictions. (b) Response relative to baseline (DR=R) of
all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response. The fraction of
nPE neurons that develop during learning decreases with f (also indicated by black and gray shading to the right).
The increasing fraction of non-nPE neurons comprises neurons that remain at their baseline in all three phases,
show a suppression during mismatch or develop into positive prediction-error neurons that respond only during
playback.
> Figure description (generated): ## Figure Description: Fraction of nPE Neurons Depends on SOM and VIP Neuron Inputs

This figure, labeled with the letter 'b', presents a visualization of neural responses across different conditions.

**1. Overall Layout & Structure:**
The figure is divided into two main conceptual sections, though they are presented sequentially: a schematic representation at the top and a heatmap/response plot below it.

**2. Visual Components & Symbols:**
*   **Top Section (Schematic/Context):** This section is dominated by a large, rectangular heatmap-like structure.
    *   The vertical axis is labeled "Neurons," indicating that the rows represent individual neurons being analyzed.
    *   The horizontal axis is labeled "$\Delta R/R (\%)$," representing the relative change in response.
    *   A prominent vertical bar, colored deep red/maroon, is centered in the heatmap area. This bar corresponds to a specific condition indicated by the label "$f = 90\%$".
    *   To the right of the main heatmap, there are two vertical shading elements: a black bar and a gray bar.
*   **Bottom Section (Response Plot):** Below the heatmap, there is a small graphical representation showing temporal activity.
    *   This plot features three distinct horizontal lines/traces, suggesting different phases of neural activity.
    *   A color gradient bar is positioned beneath these traces, spanning the range from dark green/black on the left to deep red on the right. This gradient likely corresponds to the $\Delta R/R (\%)$ scale shown above.

**3. Labels, Keys & Legends:**
*   **Main Title/Annotation:** "$f = 90\%$" is displayed above the main heatmap.
*   **Y-Axis Label:** "Neurons" (on the left side of the heatmap).
*   **X-Axis Label:** "$\Delta R/R (\%)$" (below the heatmap).
*   **Temporal Traces:** Three distinct horizontal traces are visible below the main plot, suggesting different phases (as detailed in the caption).
*   **Color Gradient:** A horizontal color bar spans the bottom, ranging from a dark/cool color (left) to a warm/red color (right).

**4. Data Trends & Details:**
*   **Heatmap Response:** The heatmap displays a distribution of responses across neurons. The central red bar ($f=90\%$) shows a concentrated area of high response amplitude (indicated by the deep red color) centered around $\Delta R/R = 0\%$.
*   **Shading Trend:** The caption notes that the fraction of nPE neurons decreases with $f$. This is visually suggested by the black and gray shading to the right of the main plot, indicating a change in population characteristics as $f$ varies.
*   **Temporal Activity:** The three traces below the heatmap show distinct patterns of activity across time (implied by their sequential arrangement):
    *   The first trace shows a pattern of activity followed by quiescence.
    *   The second trace shows a similar, perhaps slightly different, pattern.
    *   The third trace shows another distinct temporal profile.

**5. Contextual Caption Integration:**
The caption clarifies that the heatmap represents the "Response relative to baseline ($\Delta R=R$) of all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response." The vertical bar at $f=90\%$ specifically relates to the fraction ($f$) of SOM neurons receiving visual input, while $(1-f)$ of VIP neurons receive visual input. The black and gray shading to the right corresponds to changes in the fraction of nPE neurons as $f$ varies.

> Figure caption (from PDF text): Figure 4. Fraction of nPE neurons depends on SOM and VIP neuron inputs. (a) Network model with excitatory PCs
and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of clarity. Somatic
compartment of PCs, PV neurons, a fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive visual
input. The remaining SOM and VIP neurons receive motor predictions. (b) Response relative to baseline (DR=R) of
all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response. The fraction of
nPE neurons that develop during learning decreases with f (also indicated by black and gray shading to the right).
The increasing fraction of non-nPE neurons comprises neurons that remain at their baseline in all three phases,
show a suppression during mismatch or develop into positive prediction-error neurons that respond only during
playback.
> Figure description (generated): This figure, labeled as Figure 4, presents a visualization related to the fraction of nPE neurons depending on SOM and VIP neuron inputs. The figure is divided into two main conceptual parts, though the provided image snippet focuses heavily on a single panel structure.

### Overall Layout & Structure
The visible portion of the figure appears to be a combination of schematic representations and heatmaps/plots. The structure is organized vertically, featuring labels indicating different neuron types or states on the right side, and a central plot area displaying response data.

### Visual Components & Symbols
1. **Right-Side Labels (Neuron States):** On the far right, there are two distinct labels stacked vertically:
    * **nPE:** Indicating a specific type of neuron (likely "novel prediction error" or similar, based on the caption).
    * **non-nPE:** Indicating neurons that do not fit the nPE classification.
2. **Central Plot Area (Heatmap/Response Map):** The main body of the figure is dominated by a large, rectangular plot area.
    * **Color Gradient:** This area displays a color gradient ranging from deep red/maroon on the left to lighter pinks and whites towards the center-right. This suggests a quantitative measure, likely related to response magnitude or activity level.
    * **Horizontal Banding:** Within this plot, there are horizontal bands of color intensity that appear to change across the x-axis.
3. **Bottom Plot (Response Profile):** Below the main heatmap, there is a secondary plot showing response profiles.
    * **Line Graph:** A fluctuating line graph is visible, suggesting temporal or phase-dependent activity.
    * **Color Bar/Gradient:** Beneath this line graph is a horizontal color bar transitioning from dark (left) to light (right), likely representing the range of $\Delta R/R$ values.

### Labels, Keys & Legends
**Titles and Variables:**
* **Top Center Label:** $f = 50\%$ (This indicates a specific parameter value being illustrated).
* **X-Axis Label:** $\Delta R/R (\%)$ (This denotes the relative change in response, measured as a percentage). The scale ranges from $-30$ to $30$.
* **Bottom Color Bar Label:** $\Delta R/R (\%)$ (This reiterates the x-axis variable).

**Annotations:**
* The caption mentions "Somatic compartment of PCs, PV neurons, a fraction $f$ of SOM neurons and a fraction $(1-f)$ of VIP neurons receive visual input." This context explains the parameters being varied.

### Data Trends & Details
**Main Plot ($\Delta R/R$ vs. Activity):**
* The color intensity in the main plot shows a distinct vertical band of high activity (darker red) centered near $\Delta R/R = 0$.
* The shading on the right side, corresponding to the nPE and non-nPE labels, shows a gradient:
    * The area corresponding to **nPE** neurons appears to be associated with the central, high-activity region.
    * The area corresponding to **non-nPE** neurons shows a transition, with the caption noting that the fraction of non-nPE neurons increases as $f$ changes.

**Bottom Plot (Response Profile):**
* The fluctuating line graph shows activity that rises and falls across the $\Delta R/R$ range.
* The caption specifies this plot shows "Response relative to baseline ($\Delta R=R$) of all PCs in feedback, mismatch and playback phases." The shape suggests distinct patterns across these three phases.

### Contextual Caption Integration
The caption clarifies the meaning of the visual elements:
* **$f=50\%$:** This specific value sets the fraction of SOM neurons receiving visual input, while $(1-f)$ dictates the fraction of VIP neurons.
* **nPE vs. non-nPE:** The right-side labels correspond to the classification of neurons based on their response characteristics during learning.
* **Data Interpretation:** The caption explains that the fraction of nPE neurons decreases as $f$ changes, and non-nPE neurons include those that remain at baseline or develop into specific types of prediction-error neurons.

> Figure caption (from PDF text): Figure 4. Fraction of nPE neurons depends on SOM and VIP neuron inputs. (a) Network model with excitatory PCs
and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of clarity. Somatic
compartment of PCs, PV neurons, a fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive visual
input. The remaining SOM and VIP neurons receive motor predictions. (b) Response relative to baseline (DR=R) of
all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response. The fraction of
nPE neurons that develop during learning decreases with f (also indicated by black and gray shading to the right).
The increasing fraction of non-nPE neurons comprises neurons that remain at their baseline in all three phases,
show a suppression during mismatch or develop into positive prediction-error neurons that respond only during
playback.
> Figure description (generated): This figure, labeled with a specific condition $f=10\%$, presents a combination of schematic representations and data plots, likely illustrating the functional characteristics of different neuron types within a neural network model.

### 1. Overall Layout & Structure
The figure is structured vertically, containing several distinct visual components stacked one above the other. The top section appears to be a schematic or representation of neuron populations, while the bottom section is a quantitative plot showing response characteristics.

### 2. Visual Components & Symbols
**Top Section (Neuron Population Representation):**
*   On the far left, there is a vertical axis labeled "nPE" and "non-nPE," suggesting a classification of neurons.
*   To the right of this axis, there is a large rectangular area representing the network activity or population response. This area is colored in shades of red/pink, indicating a gradient or distribution.
*   Within this large area, there are multiple horizontal bars stacked vertically on the right side. These bars appear to represent individual neurons or groups of neurons, and their vertical positioning corresponds to the classification on the left (nPE vs. non-nPE).
*   A gray vertical bar is present on the far right edge, possibly indicating a boundary or normalization point.

**Bottom Section (Response Plot):**
*   This section is a 2D plot.
    *   The **x-axis** is labeled $\Delta R/R (\%)$, ranging from approximately $-30$ to $30$.
    *   The **y-axis** is not explicitly labeled with units but represents the response magnitude.
    *   There are several horizontal, stepped lines or curves plotted across this range:
        *   A dark teal/green line is visible near the top of the plot area.
        *   An orange/brownish line is visible below the teal line.
    *   Below these lines, there is a horizontal color bar gradient spanning the width of the plot area. This gradient transitions from dark (left) to light/reddish (right), corresponding to the $\Delta R/R (\%)$ scale.

### 3. Labels, Keys & Legends
*   **Title/Condition:** $f = 10\%$ is prominently displayed above the main visual area.
*   **Y-axis Labels (Left):** "nPE" and "non-nPE".
*   **X-axis Label (Bottom):** $\Delta R/R (\%)$.
*   **Color Bar Gradient:** The gradient below the plot corresponds to $\Delta R/R (\%)$.

### 4. Data Trends & Details
**Top Section:**
*   The stacked horizontal bars show a distribution of responses. The caption indicates that the fraction of nPE neurons decreases with $f$, and the shading (black/gray) on the right side of the top section likely illustrates this trend, showing a shift in population characteristics.

**Bottom Section (Plot):**
*   The plot displays responses across different phases (implied by the caption: feedback, mismatch, playback).
*   The teal and orange lines show distinct response profiles across the $\Delta R/R (\%)$ range. The stepped nature suggests discrete states or phases of response measurement.

### 5. Contextual Caption Integration
The caption provides critical context for interpreting the visual elements:
*   **Neuron Types:** The model involves excitatory PCs, inhibitory PV, SOM, and VIP neurons.
*   **Input Distribution:** The somatic compartment of PCs, PV neurons, a fraction $f$ of SOM neurons, and a fraction $(1-f)$ of VIP neurons receive visual input. The remaining SOM and VIP neurons receive motor predictions.
*   **Plot Interpretation:** Panel (b) (which corresponds to the bottom plot shown here) displays the "Response relative to baseline ($\Delta R=R$) of all PCs in feedback, mismatch and playback phases."
*   **Trend Interpretation:** The caption explicitly states that "The fraction of nPE neurons that develop during learning decreases with $f$ (also indicated by black and gray shading to the right)," linking the visual shading in the top panel to this functional outcome.
*   **Non-nPE Neurons:** The increasing fraction of non-nPE neurons comprises those that remain at baseline, show suppression during mismatch, or develop into positive prediction-error neurons responding only during playback.

> Figure caption (from PDF text): Figure 4. Fraction of nPE neurons depends on SOM and VIP neuron inputs. (a) Network model with excitatory PCs
and inhibitory PV, SOM and VIP neurons. Connections from PCs not shown for the sake of clarity. Somatic
compartment of PCs, PV neurons, a fraction f of SOM neurons and a fraction ð1   f Þ of VIP neurons receive visual
input. The remaining SOM and VIP neurons receive motor predictions. (b) Response relative to baseline (DR=R) of
all PCs in feedback, mismatch and playback phases, sorted by amplitude of mismatch response. The fraction of
nPE neurons that develop during learning decreases with f (also indicated by black and gray shading to the right).
The increasing fraction of non-nPE neurons comprises neurons that remain at their baseline in all three phases,
show a suppression during mismatch or develop into positive prediction-error neurons that respond only during
playback.
> Figure description (generated): ## Figure 4 Description: Fraction of nPE Neurons Depends on SOM and VIP Neuron Inputs

This figure is divided into two main panels, (a) and (b), presenting a combination of a neural circuit schematic and quantitative response plots.

### Panel (a): Network Model Schematic
Panel (a) displays a schematic representation of the neural network model.

*   **Structure:** It illustrates connections between different neuronal populations, including PCs (presumably Principal Cells), PV neurons, SOM neurons, and VIP neurons.
*   **Inputs:** The schematic indicates the sources of input:
    *   Visual input is shown to be received by the Somatic compartment of PCs, PV neurons, a fraction $f$ of SOM neurons, and a fraction $(1-f)$ of VIP neurons.
    *   Motor predictions are shown to be received by the remaining SOM and VIP neurons (i.e., those not receiving visual input).
*   **Connections:** The connections between these components are depicted using lines and arrows, indicating signal flow.
*   **Annotation:** A note states: "Connections from PCs not shown for the sake of clarity."

### Panel (b): Response Plots
Panel (b) presents quantitative data showing neuronal responses across different phases of learning.

*   **Type:** This panel consists of plots displaying neural response relative to baseline.
*   **Axes:** The description indicates the plot shows "Response relative to baseline ($\text{DR}=R$)" across three distinct phases: **feedback**, **mismatch**, and **playback**.
*   **Data Organization:** The responses are sorted by the amplitude of the mismatch response.
*   **Visual Elements & Trends:**
    *   The plot displays data points or distributions representing the response of PCs.
    *   There is a visual representation showing how the fraction of nPE neurons changes as $f$ varies. This change is indicated by **black and gray shading** to the right of the main response data.
    *   The caption specifies that "The fraction of nPE neurons that develop during learning decreases with $f$."
    *   Furthermore, the caption describes an increase in the fraction of non-nPE neurons, which are characterized as:
        1.  Neurons that remain at their baseline in all three phases.
        2.  Neurons that show a suppression during mismatch or develop into positive prediction-error neurons that respond only during playback.

**Summary of Variables and Relationships:**
The figure visually links the parameter $f$ (the fraction of SOM neurons receiving visual input) to the resulting functional properties of the PCs, specifically the development and fraction of nPE neurons across different learning phases (feedback, mismatch, playback).

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
7 of 30

Research article
Neuroscience


---

## Page 8

visual input. The remaining SOM and VIP neurons receive a motor-related prediction (Figure 4a).
When the majority of SOM neurons receive visual inputs and the majority of VIP neurons receive
motor predictions (f » 1), all PCs develop into nPE neurons (Figure 4b, left). Reducing the proportion
of SOM neurons that receive visual input (and, equivalently, the proportion of VIP neurons that
receive the motor prediction), the fraction of nPE neurons decreases (Figure 4b, middle). Non-nPE
neurons remain at their baseline in all three phases, show a suppression during mismatch or develop
into pPE neurons that respond only during playback. pPE neurons only emerge when the inputs to
SOM and VIP neurons are reversed such that most SOM neurons receive motor predictions
(Figure 4b, right).

In summary, the fraction of nPE neurons that develop during learning depends on the distribution
of visual input and motor predictions onto both SOM and VIP neurons.

Experience-dependence of mismatch and interneuron responses
Attinger et al., 2017 showed that the number of nPE neurons and the strength of their mismatch
responses decreases when mice are trained in artificial conditions, during which a mouse was shown
the visual information of a different mouse, such that motor predictions and visual flow were uncor-
related (‘non-coupled training’). We reasoned that this training paradigm should include baseline
phases where both animals sit still and phases, during which the speeds of the two animals differ. To
test whether the model shows the same experience-dependence, we generated a modified training
paradigm, which includes baseline phases and phases during which the visual inputs and motor-
related predictions are statistically independent (‘random gain training’, Figure 5a). We found that
the number of nPE neurons and their mismatch responses also decrease for random gain trained rel-
ative to quasi-natural trained networks (Figure 5b). This decrease is primarily due to changes in PCs
and PV neurons, while the responses of SOM and VIP neurons during the mismatch phase are largely
independent of the training paradigm (Figure 5c). Hence, the experience-dependence of the model
circuit is in line with that of nPE neurons in rodent V1 (Attinger et al., 2017).

During learning, we exposed the network to sensory inputs and motor-related predictions
designed to reflect coupled sensorimotor experience. To account for changes in the external world
that do not arise from the animal’s own movements, we included ‘playback’ phases in which the
visual input is stronger than predicted by the motor-related input. Consistent with the experimental
setup of Attinger et al., 2017, we deliberately excluded feedback mismatch phases. In the model,
the stimuli experienced during learning have a strong impact on the response structure of the PCs,
because the learning rules aim to keep the PCs at a given baseline rate at all times. The inclusion of
feedback and playback phases during learning therefore leads to neurons that remain at their base-
line during those phases, in line with nPE neurons. In mouse V1, nPE neurons exhibit an average rate
decrease during playback when the animals were only exposed to perfectly coupled sensorimotor
experience (Attinger et al., 2017). When our network was trained in the same way, we also
observed that PCs reduced their firing rate during playback phases (Figure 5d and Figure 5—figure
supplement 1). This can be a result of an excess of somatic inhibition, dendritic inhibition or both.
The
model
hence
predicts
that
the
rate
reduction
during
playback
phases
observed
by
Attinger et al., 2017 vanishes when playback phases are included during training.

nPE circuits can also be learned by biologically plausible learning rules
In our model, nPE neurons developed through inhibitory plasticity that establishes an excitation-inhi-
bition (E/I) balance in PCs. So far, we used learning rules that approximate a backpropagation of
error (Rumelhart et al., 1986), which changed SOM!PV and VIP!PV connections such as to mini-
mize the difference between the PC firing rate and a baseline rate (see Equation 16 in Materials and
methods). The biological plausibility of such backpropagation rules, which are broadly used in artifi-
cial intelligence, is still debated, because they rely on information that is not locally available at the
synapse in question (Crick, 1989; Richards and Lillicrap, 2019). We therefore wondered whether
prediction-error circuits can also be established by biologically plausible local learning rules.

We found that nPE neurons also emerged when the backpropagation rules were replaced by a
form of plasticity that changes SOM!PV and VIP!PV synapses in proportion to the difference
between the excitatory recurrent drive onto PV neurons and a target value (see Mackwood et al.,
2020, and Equations 17 and 18 in Materials and methods). This local form of learning was also able

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
8 of 30

Research article
Neuroscience


---

## Page 9

to balance excitation and inhibition sufficiently (Figure 6b,c and Figure 1—figure supplement 1c)
so that all PCs developed into nPE neurons (Figure 6c).

The plasticity rules can be further simplified when PCs do not receive visual information. In this
case, PV neurons also remain at their baseline firing rate in feedback and playback phases
(Figure 2e–f, right). Hence, the strength of SOM!PV and VIP!PV synapses can be learned accord-
ing to a homeostatic rule (Vogels et al., 2011) that aims to sustain a target rate in the PV neurons
(Figure 6—figure supplement 1 and Figure 1—figure supplement 1d, Equations 19 and 20 in
Materials and methods). In summary, the backpropagation-like learning rules for the synapses onto
PV neurons can be approximated by biologically plausible rules that exploit local information avail-
able at the respective synapses.

Discussion
How the nervous system disentangles self-generated and external sensory stimuli is a long-standing
question (Bell, 1981; Franklin and Wolpert, 2011; Keller and Mrsic-Flogel, 2018). Here, we investi-
gated the circuit level mechanisms that underlie the computation of negative prediction errors and
how different types of inhibitory neurons shape these prediction circuits. We used computational
modeling to show that nPE neurons can be learned by balancing excitation and inhibition in cortical
microcircuits with three types of interneurons. We show that the required E/I balance can be

a
b

c
d

Figure 5. Experience-dependence of nPE and PV neurons. (a) The network is either exposed to a sequence of
baseline, feedback and playback phases (quasi-natural training, QT), to baseline phases and phases during which
the visual inputs and motor-related predictions are statistically independent (random gain training, RT) or perfectly
coupled sensorimotor experience (coupled training, CT) (b) The number of nPE neurons that develop during
learning (top) and their mismatch responses (bottom) are smaller for RT than for QT networks. 90% of SOM and
50% of VIP neurons receive visual input. (c) Population response (DR=R) of PCs, PV, SOM and VIP neurons during
mismatch phase. SOM and VIP neurons show the same mismatch response for QT and RT, PCs and PV neurons
show stronger responses in QT than in RT. 90% of SOM and 50% of VIP neurons receive visual input. (d)
Responses during mismatch (top) and playback (bottom) for QT and CT networks. CT networks can exhibit a
decrease in activity during playback phase. Connections from VIP to PV neurons are non-plastic and fixed to  0.3.
The online version of this article includes the following figure supplement(s) for figure 5:

> Figure caption (from PDF text): Figure 5. Experience-dependence of nPE and PV neurons. (a) The network is either exposed to a sequence of
baseline, feedback and playback phases (quasi-natural training, QT), to baseline phases and phases during which
the visual inputs and motor-related predictions are statistically independent (random gain training, RT) or perfectly
coupled sensorimotor experience (coupled training, CT) (b) The number of nPE neurons that develop during
learning (top) and their mismatch responses (bottom) are smaller for RT than for QT networks. 90% of SOM and
50% of VIP neurons receive visual input. (c) Population response (DR=R) of PCs, PV, SOM and VIP neurons during
mismatch phase. SOM and VIP neurons show the same mismatch response for QT and RT, PCs and PV neurons
show stronger responses in QT than in RT. 90% of SOM and 50% of VIP neurons receive visual input. (d)
Responses during mismatch (top) and playback (bottom) for QT and CT networks. CT networks can exhibit a
decrease in activity during playback phase. Connections from VIP to PV neurons are non-plastic and fixed to  0.3.
The online version of this article includes the following figure supplement(s) for figure 5:
> Figure description (generated): ## Figure 5 Description: Experience-dependence of nPE and PV neurons

This figure, labeled as Figure 5, is composed of four distinct panels (a, b, c, and d), presenting schematic diagrams and time-series plots related to neural network training paradigms.

### Panel (a): Training Paradigms Schematic
Panel (a) is a schematic diagram illustrating three different training protocols: Quasi-natural training (QT), Random gain training (RT), and Coupled training (CT).

*   **Structure:** The panel displays three horizontal rows, each representing a different training type.
*   **Visual Elements:** Each row contains two distinct oscillating waveforms, representing "Motor prediction" and "Visual input."
    *   The **Motor prediction** waveform is shown in a teal/cyan color.
    *   The **Visual input** waveform is shown in an orange/brown color.
*   **Training Types:**
    *   The top row is labeled **"Quasi-natural training (QT)"**. In this configuration, the motor prediction and visual input waveforms appear to be synchronized or correlated.
    *   The middle row is labeled **"Random gain training (RT)"**. In this configuration, the motor prediction and visual input waveforms appear statistically independent.
    *   The bottom row is labeled **"Coupled training (CT)"**. In this configuration, the motor prediction and visual input waveforms are shown as perfectly coupled.

### Panel (b): Neuron Counts and Mismatch Responses
Panel (b) consists of two bar graphs stacked vertically, comparing RT and QT networks.

*   **Top Graph (nPE neurons):**
    *   **Y-axis:** Labeled "\# nPE neurons (%)". The scale ranges from 0 to approximately 35%.
    *   **X-axis:** Shows two categories: "RT" and "QT".
    *   **Data:** Two bars are present. The bar for RT is shorter, and the bar for QT is significantly taller, indicating a higher percentage of nPE neurons developing in QT compared to RT.
*   **Bottom Graph ($\Delta$R/R mismatch):**
    *   **Y-axis:** Labeled "$\Delta$R/R mismatch (%)". The scale ranges from 0 to approximately 35%.
    *   **X-axis:** Shows two categories: "RT" and "QT".
    *   **Data:** Two bars are present. The bar for RT is shorter, and the bar for QT is significantly taller, indicating a larger mismatch response in QT compared to RT.

### Panel (c): Population Response During Mismatch Phase
Panel (c) displays four separate time-series plots, showing the $\Delta$R/R response for different neuronal populations during a mismatch phase.

*   **Structure:** Four plots are arranged in a 2x2 grid.
*   **X-axis (Common):** Labeled "Time (s)", ranging from 0 to 1 second.
*   **Y-axis (Common):** Labeled "$\Delta$R/R (%)".
*   **Plots:**
    1.  **Top Left (PC population):** Shows a response curve for the PC population. The QT trace (teal/cyan) shows a higher peak response than the RT trace (orange/brown).
    2.  **Top Right (PV population):** Shows a response curve for the PV population. The QT and RT traces appear very similar in magnitude during the mismatch phase (0 to 1s).
    3.  **Bottom Left (SOM population):** Shows a response curve for the SOM population. The QT and RT traces overlap closely, showing similar responses.
    4.  **Bottom Right (VIP population):** Shows a response curve for the VIP population. The QT and RT traces overlap closely, showing similar responses.

### Panel (d): Responses During Mismatch and Playback
Panel (d) displays two time-series plots, comparing QT and CT networks across mismatch and playback phases.

*   **Structure:** Two stacked plots are presented.
*   **X-axis (Common):** Labeled "Time (s)", ranging from 0 to 1 second.
*   **Y-axis (Common):** Labeled "$\Delta$R/R (%)".
*   **Top Plot (Mismatch):**
    *   Shows the response during mismatch. The QT trace (teal/cyan) shows a clear positive deflection, while the CT trace (orange/brown) also shows a response.
*   **Bottom Plot (Playback):**
    *   Shows the response during playback. The QT trace shows a positive deflection, while the CT trace exhibits a noticeable decrease in activity (a dip below zero) during this phase.

Figure supplement 1. Coupled-trained networks can produce nPE neurons that decrease their activity in playback
phase.

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
9 of 30

Research article
Neuroscience


---

## Page 10

achieved by biologically plausible forms of synaptic plasticity. Furthermore, the experience-depen-
dence of the circuit is similar to that of nPE circuits in mouse V1 (Attinger et al., 2017).

Our model makes a number of predictions. Firstly, the multi-pathway balance of excitation and
inhibition suggests that the input configuration of the prediction circuit could be disambiguated
using cell type-specific modulations of neural activity. This could be achieved by optogenetic or
pharmacogenetic manipulations, or by exploiting the differential sensitivity of interneuron classes to
neuromodulators. The precarious nature of an exact multi-pathway balance also suggests that nPE
neurons might change their response characteristics in a context-dependent way, for example by
neuromodulatory effects.

a

b

c

(M)

(V)

M

V
V

PV

SOM
VIP

M
V

PC

Ⴃ

႑

Ⴃ

႑

Excrec
ႣΔw ~ (post - ρ0) x pre
႑Δw ~ (ρ0 - Excrec) x pre

(M)

(V)

Figure 6. Learning nPE neurons by biologically plausible learning rules. (a) Left: Network model as in Figure 1.
Connections marked with symbols undergo experience-dependent plasticity. Connections onto PCs follow an
inhibitory plasticity rule akin to Vogels et al., 2011 (triangle). SOM!PV and VIP!PV synapses change in
proportion to the difference between the excitatory recurrent drive onto PV neurons and a target value (square).
Right: During plasticity, the network is exposed to a sequence of feedback (coupled sensorimotor experience) and
playback phases (black square, visual input not predicted by motor commands). Stimuli last for 1 s and are
alternated with baseline phases (absence of visual input and motor predictions). (b) Left: Before plasticity, somatic
excitation (light red) and inhibition (light blue) in PCs are not balanced. Excitatory and inhibitory currents shifted
by ±20 pA for visualization. The varying net excitatory current (gray) causes the PC population rate to deviate from
baseline. Right: Response relative to baseline (DR=R) of all PCs in feedback, mismatch and playback phases, sorted
by amplitude of mismatch response. None of the PCs are classified as nPE neurons (indicated by gray shading to
the right). (c) Same as in (b) after plasticity. Somatic excitation and inhibition are balanced. PC population rate
remains at baseline. All PCs classified as nPE neurons (also indicated by black shading to the right).
The online version of this article includes the following figure supplement(s) for figure 6:

> Figure caption (from PDF text): Figure 6. Learning nPE neurons by biologically plausible learning rules. (a) Left: Network model as in Figure 1.
Connections marked with symbols undergo experience-dependent plasticity. Connections onto PCs follow an
inhibitory plasticity rule akin to Vogels et al., 2011 (triangle). SOM!PV and VIP!PV synapses change in
proportion to the difference between the excitatory recurrent drive onto PV neurons and a target value (square).
Right: During plasticity, the network is exposed to a sequence of feedback (coupled sensorimotor experience) and
playback phases (black square, visual input not predicted by motor commands). Stimuli last for 1 s and are
alternated with baseline phases (absence of visual input and motor predictions). (b) Left: Before plasticity, somatic
excitation (light red) and inhibition (light blue) in PCs are not balanced. Excitatory and inhibitory currents shifted
by ±20 pA for visualization. The varying net excitatory current (gray) causes the PC population rate to deviate from
baseline. Right: Response relative to baseline (DR=R) of all PCs in feedback, mismatch and playback phases, sorted
by amplitude of mismatch response. None of the PCs are classified as nPE neurons (indicated by gray shading to
the right). (c) Same as in (b) after plasticity. Somatic excitation and inhibition are balanced. PC population rate
remains at baseline. All PCs classified as nPE neurons (also indicated by black shading to the right).
The online version of this article includes the following figure supplement(s) for figure 6:
> Figure description (generated): ## Figure 6 Description: Learning nPE Neurons by Biologically Plausible Learning Rules

This figure, Figure 6, is divided into three main panels: (a), (b), and (c). Panel (a) presents a schematic of the network model, while Panels (b) and (c) display time-series plots illustrating neural activity before and after plasticity, respectively.

---

### Panel (a): Network Model Schematic

Panel (a) is a schematic diagram illustrating the network structure and plasticity rules. It is divided into two parts: a left-hand circuit diagram and a right-hand block diagram representing the experimental phases.

**Left Circuit Diagram:**
This schematic shows interconnected neural populations: PC (Parietal Cortex), SOM, VIP, and PV.
*   **Nodes:** The nodes are represented by circles containing abbreviations (PC, SOM, VIP, PV).
*   **Connections:** Synaptic connections are shown between these nodes.
    *   An arrow points from SOM to PV, labeled with a triangle ($\blacktriangle$). The caption specifies this represents an inhibitory plasticity rule akin to Vogels et al., 2011.
    *   An arrow points from VIP to PV, labeled with a square ($\blacksquare$). The caption states this synapse changes in proportion to the difference between excitatory recurrent drive onto PV neurons and a target value.
    *   An arrow points from SOM to PV, labeled with a square ($\blacksquare$). This synapse also changes based on the difference between excitatory recurrent drive onto PV neurons and a target value.
    *   Connections involving PC are also shown, receiving input from SOM and VIP.

**Right Block Diagram (Plasticity Phases):**
This diagram illustrates the experimental sequence during plasticity.
*   It shows two inputs: "Motor prediction (M)" and "Visual input (V)".
*   The sequence alternates between phases:
    *   A phase where the network is exposed to feedback (implied by the structure).
    *   A "playback phase" indicated by a black square, where visual input is *not* predicted by motor commands.
*   The stimuli duration is noted as 1 s, alternating with baseline phases (absence of visual input and motor predictions).

**Annotations in Panel (a):**
*   The plasticity rules are detailed using symbols:
    *   $\blacktriangle$: Represents connections onto PCs following an inhibitory plasticity rule.
    *   $\blacksquare$: Represents SOM!PV and VIP!PV synapses changing based on the difference between excitatory recurrent drive onto PV neurons and a target value.

---

### Panel (b): Before Plasticity

Panel (b) displays time-series data comparing neural activity before plasticity. It is divided into two subplots: a left plot showing current traces and a right heatmap showing response relative to baseline.

**Left Plot (Current Traces):**
*   **X-axis:** Time (s), ranging from 0 to 20 seconds.
*   **Y-axis:** Current (pA), ranging from -50 pA to 50 pA.
*   **Traces:**
    *   Somatic excitation (light red line) and inhibition (light blue line) in PCs are plotted. The caption notes these currents were shifted by $\pm 20 \text{ pA}$ for visualization.
    *   A gray line represents the "Net" current, and a dark gray line represents the overall PC population rate.
*   **Trend:** The caption states that before plasticity, somatic excitation and inhibition in PCs are *not* balanced. The varying net excitatory current (gray line) causes the PC population rate to deviate from baseline.

**Right Heatmap ($\Delta R/R$):**
*   This heatmap shows the "Response relative to baseline ($\Delta R/R$) of all PCs" across different phases.
*   **Y-axis:** Neurons (representing individual PC neurons).
*   **X-axis:** Phases, categorized into "feedback," "mismatch," and "playback."
*   **Color Coding:** The color intensity represents the magnitude of $\Delta R/R$ (ranging from dark red to dark blue, though the scale is not explicitly labeled on the axis).
*   **Annotation:** The caption notes that "None of the PCs are classified as nPE neurons (indicated by gray shading to the right)."

---

### Panel (c): After Plasticity

Panel (c) displays time-series data comparing neural activity after plasticity, mirroring the structure of Panel (b).

**Left Plot (Current Traces):**
*   **X-axis:** Time (s), ranging from 0 to 20 seconds.
*   **Y-axis:** Current (pA), ranging from -50 pA to 50 pA.
*   **Traces:** Somatic excitation (light red line) and inhibition (light blue line) in PCs are plotted.
*   **Trend:** The caption states that after plasticity, "Somatic excitation and inhibition are balanced," and the "PC population rate remains at baseline."

**Right Heatmap ($\Delta R/R$):**
*   This heatmap shows the "Response relative to baseline ($\Delta R/R$) of all PCs."
*   **Y-axis:** Neurons.
*   **X-axis:** Phases (feedback, mismatch, playback).
*   **Color Coding:** The color intensity represents $\Delta R/R$.
*   **Annotation:** The caption notes that "All PCs classified as nPE neurons (also indicated by black shading to the right)."

Figure supplement 1. Learning nPE neurons by biologically plausible learning rules in networks without visual
input at the soma of PCs.

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
10 of 30

Research article
Neuroscience


---

## Page 11

Secondly, the central assumption of the model is that nPE neurons emerge by a self-organized E/
I balance during sensorimotor experience. It therefore predicts that (i) sensorimotor experience an
animal is habituated to should lead to balanced excitation and inhibition in PCs, (ii) E/I balance
should break for sensorimotor experience the animal has rarely encountered, for example for mis-
matches of sensory stimuli and motor predictions and (iii) during altered sensorimotor experience in
a virtual reality setting or when the excitability of specific interneuron types is altered, interneuron
circuits should gradually reconfigure to reestablish the E/I balance.

PCs in L2/3 of V1 have very low spontaneous firing rates (Polack et al., 2013; Xue et al., 2014).
A potential rate decrease during feedback and playback could hence be hard to detect. Whether
the low response of nPE neurons during feedback and playback phases are due to an E/I balance –
as suggested here – or due to an excess of inhibition may hence be difficult to decide, and could for
example be resolved by intracellular recordings (Jordan and Keller, 2020).

We used a mathematical analysis to derive constraints imposed on an interneuron circuit by the
presence of nPE neurons. In particular, the equations unveiled the relation between the strength of
a number of inhibitory synapses, describing a multi-pathway E/I balance in a network comprising PV,
SOM and VIP neurons (see Materials and methods, Equations 8, 9). However, we also performed an
extensive analysis of different subnetworks, to elucidate under which conditions nPE neurons can
emerge (see Appendix 1). By comparing nPE circuits with less cell types, a set of common principles
can be extracted (see Appendix 1 for a detailed description): (I) SOM neurons must be present to
balance feedback predictions at the dendrites of PCs. (II) SOM neurons must receive visual input
unless both PV and VIP neurons are present as well. (III) The connections onto the dendrites must
undergo experience-dependent plasticity. (IV) PV neurons must be present when PCs receive visual
input in their somatic compartment. (V) Dendritic non-linearities are necessary except for a small set
of networks, in which all interneuron types are present and specific constraints for the input configu-
ration apply. While a minimal model that allows nPE neurons to develop comprises SOM neurons
and PCs (Attinger et al., 2017), the network with three inhibitory neuron types appears the most
likely nPE circuit given what is currently known about rodent V1.

The interneuron circuit in our model is motivated by the canonical circuit found in a variety of
brain regions (Pfeffer et al., 2013; Lee et al., 2013; Jiang et al., 2015). In addition to the connec-
tions between interneuron classes that are frequently reported as strong and numerous, we included
VIP!PV synapses in the circuit, because a mathematical analysis reveals that they are required for a
perfect E/I balance during both feedback and playback phases (see Appendix 1). While VIP!PV syn-
apses have been found in visual (Pfeffer et al., 2013), auditory (Pi et al., 2013), somatosensory
(Hioki et al., 2013; Lee et al., 2013) and medial prefrontal cortex (Pi et al., 2013), as well as amyg-
dala (Krabbe et al., 2019), they are less prominent and often weaker than SOM!PV connections
(but see Krabbe et al., 2019). VIP!PV synapses can be excluded when the conditions for nPE neu-
rons during feedback and playback phases are mildly relaxed (Keller and Hahnloser, 2009;
Keller et al., 2012; Attinger et al., 2017) and when PV neurons receive visual, but not motor inputs
(Figure 1—figure supplement 2).

Cortical circuits are complex and contain a large variety of interneuron classes (Rudy et al., 2011;
Jiang et al., 2015; Tremblay et al., 2016). We restricted the model to three of these classes: PV,
SOM and VIP neurons. It is conceivable that several other interneuron types can play a pivotal role in
prediction-error circuits. The dendrites of layer 2/3 neurons reach out to layer 1, the major target for
feedback connections (Felleman and Van Essen, 1991; Cauller, 1995; Larkum, 2013a) and home
to a number of distinct interneuron types (Larkum, 2013b; Schuman et al., 2019), which may con-
tribute to associative learning (Abs et al., 2018). In particular, NDNF neurons unspecifically inhibit
apical dendrites located in the superficial layers, and at the same time receive strong inhibition from
SOM neurons (Abs et al., 2018). Hence, it is possible that these interneurons also shape the proc-
essing of feedback information, including the computation of prediction errors.

Our analysis revealed a number of synapses in the circuit that undergo experience-dependent
changes. While the synapses from PV neurons onto PCs established a baseline firing rate in the
absence of visual input and motor predictions, the synergy between the SOM!PV, VIP!PV and
SOM!PC synapses guaranteed that the baseline is retained in feedback and playback phase. The
multi-pathway balance of excitation and inhibition could also be achieved by synaptic plasticity in
other inhibitory synapses – for example the mutual inhibition between SOM and VIP neurons. How-
ever, the assumption that mainly the inhibitory synapses onto PV neurons are plastic is supported by

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
11 of 30

Research article
Neuroscience


---

## Page 12

the observation that PV neuron activity – in contrast to SOM and VIP neuron activity – is experience-
dependent (Attinger et al., 2017).

In our circuit, the bottom-up and top-down connections conveying actual and predicted visual
input, respectively, were non-plastic. However, this modeling choice is not a pre-requisite for the for-
mation of nPE neurons and can be relaxed. As a matter of fact, nPE neurons can also develop in a
network, in which the excitatory top-down and bottom-up connections undergo experience-depen-
dent plasticity that balances excitation and inhibition in somatic and dendritic compartments of PCs.
For instance, nPE neurons can also be learned by endowing the top-down and bottom-up connec-
tions onto PCs and PV neurons with similar plasticity rules described here. Restricting plasticity to
the excitatory connections onto PCs would, however, require all inhibitory interneurons to exclusively
receive visual input, suggesting that excitatory bottom-up/top-down connections onto interneurons
must also change in an activity-dependent manner.

In the model, the plastic inhibitory synapses onto PV neurons change according to non-local infor-
mation that might not be directly available at the synapse. These synapses therefore implement an
approximation of a backpropagation of error, the biological plausibility of which is debated
(Crick, 1989). We showed that this plasticity rule can be approximated by biologically plausible var-
iants of the plasticity rules. If PCs do not receive direct visual input (Figure 6—figure supplement
1), the backpropagation-like algorithm can be replaced by a simple homeostatic Hebbian plasticity
rule in the synapses onto the PV interneurons. Given that PCs in V1 are known to receive substantial
visual drive (Yang et al., 2013; Xue et al., 2014), this assumption is unlikely to be valid. We there-
fore propose an alternative form of plasticity that changes SOM!PV and VIP!PV synapses in pro-
portion to the difference between the excitatory recurrent drive onto PV neurons and a target value
(Mackwood et al., 2020, see Figure 6). The underlying mechanism is similar to feedback alignment
(Lillicrap et al., 2016) and requires sufficient overlap between the set of postsynaptic PCs a PV neu-
ron inhibits and the set of presynaptic PCs the same PV neuron receives excitation from. This is
likely, given the high connection probability between PCs and PV neurons (Pfeffer et al., 2013;
Pala and Petersen, 2015; Jiang et al., 2015). Given that the main goal of the present paper was to
show that PE circuits can be learned by balancing excitation and inhibition, we used the plasticity
rule implementing a backpropagation of error, to ensure maximal generality.

We modeled the apical dendrite of PCs as a single compartment that integrates excitatory and
inhibitory input currents and has the potential to produce calcium spike-like events (Yuste et al.,
1994; Larkum et al., 1999; Murayama et al., 2009; Herta¨g and Sprekeler, 2019). Moreover, we
assumed that an overshoot of inhibition decouples the apical tuft of the PCs from their soma, by
including a rectifying non-linearity that precludes an excess of dendritic inhibition to influence
somatic activity. However, the presence or nature of these dendritic nonlinearities has a minor influ-
ence on the development of nPE neurons (Figure 1—figure supplement 3). When we allowed den-
dritic inhibition to influence the soma, inhibitory plasticity still established nPE neurons, although the
learned interneuron circuit differs with respect to the synaptic strengths. The additional dendritic
inhibition reduces the required amount of somatic, PV-mediated inhibition. This is primarily the case
during playback phases, when the excitatory motor input to the apical dendrite is absent. PV neu-
rons are therefore less active during the playback phase than during the feedback phase (Figure 1—
figure supplement 3), consistent with recordings in mouse V1 (Attinger et al., 2017).

By modeling the apical dendrite as a single compartment, we also neglected the possibility that
dendritic branches process distinct information. However, we expect that the suggested framework
of generating predictive signals by a compartment-specific E/I balance generalizes to more complex
dendritic configurations, in which local inhibition could contribute by gating different dendritic inputs
(Yang et al., 2016).

A hallmark of neurons in sensory areas is their pronounced feature selectivity (Cardin et al.,
2007; Niell and Stryker, 2008; Harris and Mrsic-Flogel, 2013). This selectivity is also present in
nPE neurons in layer 2/3 of rodent V1 which preferentially signal mismatches in a particular location
of the visual field (Zmarz and Keller, 2016). Here, we did not include feature selectivity, but only
modeled one-dimensional input signals representing actual or expected visual input. However, we
expect that nPE neurons can also develop in networks in which excitatory neurons are equipped
with feature selectivity and receive multi-dimensional inputs, by the same plasticity rules described
here. We conjecture that the presence of feature selectivity imposes further constraints on the net-
work, for instance, regarding feature topography or interneuron tuning properties. For future work,

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
12 of 30

Research article
Neuroscience


---

## Page 13

it would be interesting to study how the presence of feature-selective PE neurons constrains the fea-
ture selectivity in interneurons that tend to be more broadly tuned than excitatory neurons
(Sohya et al., 2007; Cardin et al., 2007; Kerlin et al., 2010; Atallah et al., 2012).

In our model, the excitatory recurrent connections target the apical dendrites of PCs, but given
that PCs comprise a homogeneous population, they serve no specific computational purpose in the
present context. We expect that this would change if the neurons in the circuit were endowed with
stimulus selectivity. For instance, the predictive coding model by Boerlin et al., 2013 assumes sepa-
rate recurrent loops for coding and computation (see also Dene`ve and Machens, 2016). In this
model, the membrane potential represents a prediction error and occasional spiking serves the pur-
pose of reducing a potential mismatch by initiating fast inhibition. The excitatory neurons receive
feedforward inputs, fast feedback inhibition and slow excitatory recurrent connections. While the
fast inhibitory loop balances the excitatory feedforward and the slow feedback inputs, the slower
loop – combined with dendritic nonlinearities – allows for nonlinear computations of the delayed
represented variable (Dene`ve and Machens, 2016). It will be interesting to study how this line of
work is related to the PE circuit model we studied here, but it would require to extend the present
model to perform richer computations, for example by endowing it with stimulus selectivity.

Here, we have mainly focused on the development of nPE neurons because those have been
studied extensively in layer 2/3 of rodent V1, which allowed us to qualitatively compare our model
with experimental findings. In contrast, to the best of our knowledge, less is known for pPE neurons
in the visual system. Moreover, as we assume that excitatory neurons aim to establish an E/I balance
for all stimuli they are regularly exposed to, and as animals experience episodes, in which the change
of visual input is only caused by external factors (playback phases), excitatory neurons are more likely
to develop into nPE than pPE neurons in the sensorimotor paradigm used here. However, it can be
assumed that under different circumstances pPE neurons do play an equally important role in the
processing of information. We expect that the same principles and approaches described here also
hold for the formation of pPE neurons. Indeed, when a network, in which SOM neurons receive
motor-related input and VIP neurons receive visual input, is exposed to baseline, feedback and mis-
match phases, pPE neurons develop (see Appendix 2—figure 2). The inhibitory plasticity establishes
pPE neurons independent of the input configuration onto PCs and PV neurons as long as various
excitatory, inhibitory, disinhibitory and dis-disinhibitory pathways can be balanced (see Appendix 2—
figure 1, Equations 50 and 51).

In the present work, we derived the constraints for separate nPE and pPE neurons and did not
study the parallel development of both in the same neural network. While the formation of nPE neu-
rons requires SOM neurons to receive visual input, the formation of pPE neurons requires SOM neu-
rons to receive a motor-related prediction thereof. Given that SOM neurons constitute a
heterogeneous population (Jiang et al., 2015; Tremblay et al., 2016; Urban-Ciecko and Barth,
2016), it is conceivable that separate sub-circuits enable the parallel existence of nPE and pPE neu-
rons. However, we expect that the presence of both PE types requires refined constraints on the
interneuron circuit and plasticity rules. For instance, the formation of nPE and pPE neurons that only
increase their activity in mismatch and playback phases, respectively, while remaining at baseline
otherwise, introduces constraints for all three phases. Hence, the network must be exposed to all
input phases during learning. In the present framework, this would most likely produce excitatory
neurons that remain at their baseline in all phases and hence do not encode prediction errors at all.
Hence, the plasticity rules must be modified such that they incorporate gating signals that restrict
learning to a subset of input phases or a subset of synapses, for example by controlling the learning
rates. It has been argued that specific neuromodulators that are linked to self-motion may guide
plasticity in prediction-error circuits (Keller and Mrsic-Flogel, 2018). For example, neuromodulators
could restrict learning to feedback phases. In this case, excitatory neurons would show deviations
from baseline during both playback and mismatch phases, that is essentially all neurons would
encode both positive and negative prediction errors. A dichotomy of nPE and pPE neurons could
result from low baseline firing rates. A thorough investigation of these scenarios for the simultaneous
development of nPE and pPE neurons is, however, beyond the scope of the present study.

Our model suggests a well-orchestrated division of labor of PV, SOM and VIP interneurons that is
shaped by experience: While PV neurons balance the sensory input at the somatic compartment of
PCs, SOM neurons cancel feedback signals at the apical dendrites. VIP neurons ensure sufficiently
large mismatch responses by amplifying small differences between feedforward and feedback inputs

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
13 of 30

Research article
Neuroscience


---

## Page 14

(Attinger et al., 2017; Herta¨g and Sprekeler, 2019). Given the relative uniformity of cortex in its
appearance, structure and cell types (Douglas et al., 1989; Mountcastle, 1997), it is conceivable
that the same principles also hold for other regions of the cortex beyond V1. Shedding light on the
mechanisms that constitute the predictive power of neuronal circuits may in the long run contribute
to an understanding of psychiatric disorders that have long been associated with a malfunction of
the brain’s prediction machinery (Fletcher and Frith, 2009; Corlett et al., 2009; Sinha et al., 2014;
Lawson et al., 2017) and specific types of interneurons (Marı´n, 2012; Hattori et al., 2017; Batista-
Brito et al., 2018).

Materials and methods

Network model
We simulated a rate-based network model of excitatory pyramidal cells (NPC = 70) and inhibitory PV,
SOM and VIP neurons (NPV ¼ NSOM ¼ NVIP = 10). All neurons are randomly connected with connec-
tion strengths and probabilities given below (see ‘Connectivity’).

The excitatory pyramidal cells are described by a two-compartment rate model that was intro-
duced by Murayama et al., 2009. The dynamics of the firing rate rE;i of the somatic compartment of
neuron i obeys

t E

drE;i

dt ¼  rE;i þ Ii   Q
½
;
(1)

where t E denotes the excitatory rate time constant (t E = 60 ms), Q terms the rheobase of the neu-
ron (Q ¼ 14 s 1). Firing rates are rectified to ensure positivity. Ii is the total somatic input generated
by somatic and dendritic synaptic events and potential dendritic calcium spikes:

Ii ¼ lD Isyn

D;i þ ci
h
i

þþð1   lEÞIsyn

E;i :
(2)

Here, the function ½xþ ¼ maxðx;0Þ is a rectifying nonlinearity that prohibits an excess of inhibition
at the apical dendrite to reach the soma. Isyn

D;i and Isyn

E;i are the total synaptic inputs into dendrite and

soma, respectively, and ci denotes a dendritic calcium event. lD and lE are the fractions of ‘currents’
leaking away from dendrites and soma, respectively (lD=0.27, lE=0.31). The synaptic input to the
soma Isyn

E;i is given by the sum of external sensory inputs xE and PV neuron-induced (P) inhibition,

Isyn

E;i ¼ xE  

X
NPV

j¼1

wEP;ij  rP;j:
(3)

The dendritic input Isyn

D;i is the sum of motor-related predictions xD, the recurrent, excitatory con-
nections from other PCs and SOM neuron-induced (S) inhibition:

Isyn

D;i ¼ xD  

X
NSOM

j¼1

wDS;ij  rS;j þ

X
NPC

j¼1

wDE;ij  rE;j:
(4)

The weight matrices wEP, wDS and wDE denote the strength of connection between PV neurons
and the soma of PCs (wEP), SOM neurons and the dendrites of PCs (wDS) and the recurrence
between PCs (wDE), respectively. The input generated by a calcium spike is given by

ci ¼ c  HðI0

D;i   QcÞ;
(5)

where c scales the amount of current produced (c ¼ 7s 1), H is the Heaviside step function, Qc repre-
sents a threshold that describes the minimal input needed to produce a Ca2+-spike (Qc ¼ 28 s 1) and
I0

D;i denotes the total, synaptically generated input in the dendrites,

I0

D;i ¼ lEIsyn

E;i þ ð1   lDÞIsyn

D;i :
(6)

Note that we incorporated the gain factor present in Murayama et al., 2009 into the parameters

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
14 of 30

Research article
Neuroscience


---

## Page 15

to achieve unit consistency for all neuron types (when we compared excitatory/inhibitory currents,
the respective activities were divided by this gain factor, g ¼ 0:07 (pA s) 1).

The firing rate dynamics of each interneuron is modeled by a rectified, linear differential equation
(Wilson and Cowan, 1972),

t i

drX;i

dt ¼  rX;i þ

X
NPC

j¼1

wXE;ij  rE;j  

X
NPV

j¼1

wXP;ij  rP;j  

X
NSOM

j¼1

wXS;ij  rS;j  

X
NVIP

j¼1

wXV;ij  rV;j þ xi;
(7)

where rX;i denotes the firing rate of neuron i from neuron type X (X 2 fP;S;Vg) and xi represents
external inputs. The weight matrices wXY denote the strength of connection between the presynap-
tic neuron population Y and the postsynaptic neuron population X. The rate time constant t i was
chosen to resemble a fast GABAA time constant, and set to 2 ms for all interneuron types included.

Negative prediction-error neurons
We define PCs as nPE neurons when they exclusively increase their firing rate during feedback mis-
match (visual input smaller than predicted), while remaining at their baseline during feedback and
playback phases. In a linearized, homogeneous network and under the assumption that the apical
dendrites are sufficiently inhibited during feedback and playback phase, this definition is equivalent
to two constraints on the interneuron network (see Appendix 1 for a detailed analysis and
derivation):

wPS ¼ VP þ wVS MP   ð1 þ wPPÞ

wEP

VE;
(8)

wPV ¼ MP þ wSV VP   wSV

ð1 þ wPPÞ

wEP

VE

¼ wSVwPS þ ð1   wSVwVSÞMP :
(9)

The parameters VX;MX 2 f0;1g indicate whether neuron type X receives visual and motor-related
inputs, respectively, and control the different input configurations. In addition to the conditions
Equations 8 and 9, the synapses from SOM neurons onto the apical dendrites must be sufficiently
strong to cancel potential excitatory inputs during feedback and playback phase.

In practice, we classify PCs as nPE neurons when DR=R is larger than 20% in the mismatch phase
and less than ±10% elsewhere (DR=R ¼ ðr   rBLÞ=rBL, rBL: baseline firing rate). Tolerating small devia-
tions in feedback and playback phase is more in line with experimental approaches. The results do
not rely on the precise thresholds used for the classification.

Connectivity
All neurons are randomly connected with connection probabilities motivated by the experimental lit-
erature (Fino and Yuste, 2011; Packer and Yuste, 2011; Pfeffer et al., 2013; Lee et al., 2013;
Pi et al., 2013; Jiang et al., 2015; Jouhanneau et al., 2015; Pala and Petersen, 2015),

p ¼

pEE
pEP
pES
pEV
pDE pDP pDS pDV
pPE
pPP
pPS
pPV
pSE
pSP
pSS
pSV
pVE pVP pVS pVV

0

B
B
B
B
B
B
@

1

C
C
C
C
C
C
A

¼

 
0:6
 
 
0:1
 
0:55
 
0:45 0:5
0:6
0:5
0:35
 
 
0:5
0:1
 
0:45
 

0

B
B
B
B
B
B
@

1

C
C
C
C
C
C
A

:
(10)

All cells of the same neuron type have the same number of incoming connections. The mean con-
nection strengths are given by

w ¼

wEE
wEP
wES
wEV
wDE wDP wDS wDV
wPE
wPP
wPS
wPV
wSE
wSP
wSS
wSV
wVE wVP wVS wVV

0

B
B
B
B
B
B
@

1

C
C
C
C
C
C
A

¼

 

 
 
0:42  

 





1
 
 
0:6
1
  0:5
 

0

B
B
B
B
B
B
@

1

C
C
C
C
C
C
A

(11)

where the symbol * denotes weights that vary between simulations (e.g., subject to plasticity or

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
15 of 30

Research article
Neuroscience


---

## Page 16

computed from the Equations 8 and 9). For non-plastic networks, these synaptic strengths are given
by wEP ¼ 2:8, wDS ¼ 3:5, wPE ¼ 1:5, wPP ¼ 0:1 (if PCs receive visual input) or wPP ¼ 1:5 (if PCs receive
no visual input), wPS and wPV are computed from the Equations 8 and 9.

For plastic networks, the initial connections between neurons are drawn from uniform distribu-
tions winitial

ij
2 U 0:5 w; 1:5 w
ð
Þ where w denotes the mean connection strengths given in (Equation 11)
and wEP ¼ 1:75, wDS ¼ 0:35, wPE ¼ 2:5 (if PCs receive visual input) or wPE ¼ 1:2 (if PCs receive no
visual input), wPP ¼ 0:5 (if PCs receive visual input) or wPP ¼ 1:5 (if PCs receive no visual input),
wPS ¼ 0:3 and wPV ¼ 0:6. Please note that the system is robust to the choice of connections
strengths. The connection strengths are merely chosen such that the solutions of Equations 8 and 9
comply with Dale’s principle.

All weights are scaled in proportion to the number of existing connections (i.e., the product of
the number of presynaptic neurons and the connection probability), so that the results are indepen-
dent of the population size.

Inputs
All neurons receive constant, external background input that ensures reasonable baseline firing rates
in the absence of visual and motor-related input. In the case of non-plastic networks, these inputs
were set such that the baseline firing rates are rE ¼ 1s 1, rP ¼ 2s 1, rS ¼ 2s 1 and rV ¼ 4s 1. In the
case of plastic networks, we set the external inputs to xE ¼ 28s 1, xD ¼ 0s 1, xP ¼ 2s 1, xS ¼ 2s 1 and
xV ¼ 2s 1 (if not stated otherwise). In addition to the external background inputs, the neurons
receive either visual input (v), a motor-related prediction thereof (m) or both.

In line with the experimental setup of Attinger et al., 2017, we distinguish between baseline
(m ¼ v ¼ 0), feedback (m ¼ v>0), feedback mismatch (m>v) and playback (m<v) phases. During train-
ing, the network is exposed to feedback and playback phases with stimuli drawn from a uniform dis-
tribution from the interval ½0; 7s 1. After learning, the strength of stimuli is set to 7s 1 (plastic
networks) or 3:5s 1 (non-plastic networks).

Plasticity
In plastic networks, a number of connections between neurons are subject to experience-dependent
changes in order to establish an E/I balance for PCs. PV!PC and the PC!PV synapses establish the
target firing rates for PCs and PV neurons, respectively. VIP!PV and SOM!PV synapses and the
synapses from SOM neurons onto the apical dendrites of PCs ensure that PCs remain at their base-
line during feedback and playback phase. The corresponding plasticity rules are of the form

Dw / ðpost   baselineÞ  pre
(12)

Connections onto PCs
In detail, the connections from PV and SOM neurons onto the soma and the apical dendrites,
respectively, obey inhibitory Hebbian plasticity rules akin to Vogels et al., 2011

DwEP;ij / ðrpost

E;i   post

E;0 Þ  rpre

P;j ;
(13)

DwDS;ij / ðApost

i
  Þ  rpre

S;j :
(14)

The parameter post

E;0 denotes the baseline firing rate of the postsynaptic PC, and the dendritic

activity Apost

i
is given by the rectified synaptic events at the dendrites

Apost

i
¼ Isyn

D;i þ ci
h
i

þ:
(15)

The small ‘correction’ term  eases the effect of strong onset responses (here, we used  ¼ 0:1s 1).

Connections onto PV neurons - non-local learning
The connections from both SOM and VIP neurons onto PV neurons implement an approximation of
a backpropagation of error

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
16 of 30

Research article
Neuroscience


---

## Page 17

Dwij / 1

NE;i

X

k2Spost

i

ðpost

E;0   rpost

E;k Þ  rpre

j
:
(16)

Spost

i
denotes the set of postsynaptic PCs a particular PV neuron is connected to, and NE;i is the
number of excitatory neurons in Spost

i
.

Connections onto PV neurons - local approximation to backpropagation of
error
When the connection probability between PCs and PV neurons is large, this backpropagation of
error can be replaced by a biologically plausible learning rule that only relies on local information
available in the PV neurons (Figure 6),

Dwij / DErec;i  rpre

j
;
(17)

where DErec;i denotes the difference between the excitatory recurrent drive onto PV neuron i and a
target value

DErec;i ¼

X

k2Spre

i

wPE;ik  ðpost

E;0   rpost

E;k Þ:
(18)

Spre

i
denotes the set of presynaptic PCs a particular PV neuron receives excitation from.

Connections onto PV neurons - learning with a homeostatic firing rate for
PV neurons
When nPE neurons do not receive direct visual input, the backpropagation rules can be simplified
even further (Figure 6—figure supplement 1). The synapses onto PV neurons can be learned
according to a Hebbian inhibitory plasticity rule (Vogels et al., 2011) that aims to sustain a baseline
rate in the PV neurons

DwPX;ij / ðrpost

P;i   post

P;0 Þ  rpre

X;j
(19)

with X 2 fS;Vg. This baseline rate is established by modifying the connections from PCs onto PV neu-
rons according to an anti-Hebbian plasticity rule

DwPE;ij / ðpost

P;0   rpost

P;i Þ  rpre

E;j :
(20)

Simulation and code availability
All simulations were performed in customized Python code written by LH. Differential equations
were numerically integrated using a 2nd-order Runge-Kutta method with time steps between 0.05
and 2 ms. Neurons were initialized with rið0Þ ¼ 0. Source code and data for all figures will be avail-
able
after
publication
at
Herta¨g,
2020
(https://github.com/sprekelerlab/SourceCode_
Hertaeg20, copy archived at https://github.com/elifesciences-publications/SourceCode_Hertaeg20).

Acknowledgements
We are grateful to Laura Bella Naumann and Joram Keijser for critical reading of the manuscript and
Owen Mackwood for technical guidance during development of the simulator. We also want to
thank all members of the Sprekeler lab for discussion, support and comments on the manuscript.
The project is funded by the German Federal Ministry for Education and Research, FKZ 01GQ1201
and the DFG via the collaborative research center FOR 2143.

Herta¨g and Sprekeler. eLife 2020;9:e57541. DOI: https://doi.org/10.7554/eLife.57541
17 of 30

Research article
Neuroscience


---

## Page 18

Additional information

Funding

Funder
Grant reference number
Author

Bundesministerium fu¨ r Bildung
und Forschung

FKZ 01GQ1201
Henning Sprekeler

Deutsche Forschungsge-
meinschaft

FOR 2143
Henning Sprekeler

The funders had no role in study design, data collection and interpretation, or the
decision to submit the work for publication.

Author contributions
Loreen Herta¨g, Conceptualization, Data curation, Software, Formal analysis, Validation, Investigation,
Visualization, Methodology, Writing - original draft, Writing - review and editing; Henning Sprekeler,
Conceptualization, Resources, Supervision, Funding acquisition, Writing - original draft, Project
administration, Writing - review and editing

Author ORCIDs
Loreen Herta¨g
https://orcid.org/0000-0001-7838-3361
Henning Sprekeler
http://orcid.org/0000-0003-0690-3553

Decision letter and Author response
Decision letter https://doi.org/10.7554/eLife.57541.sa1
Author response https://doi.org/10.7554/eLife.57541.sa2

Additional files
Supplementary files

. Transparent reporting form

Data availability
Source code to reproduce simulated data and figures is publicly available at https://github.com/
sprekelerlab/SourceCode_Hertaeg20 (copy archived at https://github.com/elifesciences-publica-
tions/SourceCode_Hertaeg20).