## 

Article

Visuomotor Coupling Shapes the Functional
Development of Mouse Visual Cortex

Graphical Abstract

Highlights

d The development of mismatch responses depends on

visuomotor experience

d Mismatch neurons balance excitatory motor-related input

against visual inhibition

d Visual inhibition onto mismatch neurons is mediated by

somatostatin interneurons

d Normal visuomotor experience rapidly restores normal visual

processing

Authors

Alexander Attinger, Bo Wang,
Georg B. Keller

### Upper Schematic Diagram (Sensorimotor Loop)

The upper section is a block diagram illustrating a closed-loop system involving motor control and sensory processing.

**Components and Flow:**
1.  **Motor Output:** Represented by a purple rectangular box labeled "Motor output." An arrow points from this box towards the central processing area.
2.  **Sensory Feedback:** Represented by a green rectangular box labeled "Sensory feedback." An arrow points from the central processing area towards this box.
3.  **Sensory Input:** Represented by a green rectangular box labeled "Sensory input." An arrow points from this box towards the central processing area.
4.  **Central Processing Area:** This is a large, light gray shaded region containing the core interaction:
    *   **Visual Flow Prediction:** A rounded rectangular node labeled "Visual flow prediction" is located in the lower-left portion of this gray area. An arrow originates from "Motor output" and points towards "Visual flow prediction."
    *   **Inhibition/Modulation Node:** A central, white rectangular box containing a red minus sign ($\ominus$) is positioned centrally. This node receives input from "Visual flow prediction" and sends an arrow towards the connection between "Sensory feedback" and "Sensory input."
    *   **Layer Specification:** Above the central processing area, text indicates: "Layer 2/3 of visual cortex."

**Interconnections:**
*   An arrow flows from "Visual flow prediction" towards the central inhibition node ($\ominus$).
*   Arrows connect the system components: "Motor output" $\rightarrow$ (Central Area) $\leftarrow$ "Visual flow prediction."
*   The central inhibition node ($\ominus$) is positioned to modulate the interaction between "Sensory feedback" and "Sensory input."
*   Arrows indicate a loop: "Sensory feedback" $\rightarrow$ (Central Area) $\leftarrow$ "Sensory input."

### Lower Schematic Diagram (Before vs. After State)

The lower section is a comparative schematic detailing the underlying neural mechanisms, divided into two distinct states: "Before" and "After."

**1. "Before" State (Left Side):**
*   This section is labeled "Before."
*   It depicts a simplified neural circuit involving three elements:
    *   **Motor-related input:** Represented by a small, light blue node/circle.
    *   **Visual input:** Represented by a small, orange-ish node/circle.
    *   **SST:** Represented by a small, light green node/circle labeled "SST."
*   **Connections:**
    *   An arrow flows from "Motor-related input" towards the central interaction area.
    *   A line labeled "inh." (inhibition) connects from the central interaction area towards "Visual input."
    *   A line labeled "MM" (likely Motor Modulation or similar) connects from the central interaction area towards "Motor-related input."
    *   The overall state is described by the text: "Motor-related excitation and visual inhibition are not matched, no mismatch signal."

**2. "After" State (Right Side):**
*   This section is labeled "After."
*   It depicts a similar neural circuit structure as the "Before" state, but with altered dynamics.
*   **Connections:** The elements ("Motor-related input," "Visual input," "SST") are present.
    *   The inhibitory line ("inh.") and the modulation line ("MM") remain, but their context implies a change in balance.
    *   The overall state is described by the text: "A balance between motor-related excitation and visual inhibition is established."

**Overall Structure:**
The figure uses a combination of high-level block diagrams (top) and detailed circuit schematics (bottom) to illustrate the transition from a state of mismatch ("Before") to a balanced, integrated state ("After") within the sensorimotor loop.

Correspondence
georg.keller@fmi.ch

In Brief

The coupling of sensory and motor
experience during development shapes
visual perception by tuning a cortical
circuit that compares inhibitory visual
input and excitatory motor input and is
able to detect mismatches between
actual and expected sensory experience.

Attinger et al., 2017, Cell 169, 1291-1302
June 15, 2017 ª 2017 Elsevier Inc.

---

## 

Article

Visuomotor Coupling Shapes the Functional
Development of Mouse Visual Cortex

Alexander Attinger,1,2,3 Bo Wang,1,2,3 and Georg B. Keller1,2,4,*
1Friedrich Miescher Institute for Biomedical Research, Maulbeerstrasse 66, 4058 Basel, Switzerland
2Faculty of Natural Sciences, University of Basel, Klingelbergstrasse 50/70, 4056 Basel, Switzerland
3These authors contributed equally
4Lead Contact
*Correspondence: georg.keller@fmi.ch

SUMMARY

The emergence of sensory-guided behavior depends
on sensorimotor coupling during development. How
sensorimotor experience shapes neural processing
is unclear. Here, we show that the coupling between
motor output and visual feedback is necessary for
the functional development of visual processing in
layer 2/3 (L2/3) of primary visual cortex (V1) of the
mouse. Using a virtual reality system, we reared
mice in conditions of normal or random visuomotor
coupling. We recorded the activity of identified excit-
atory and inhibitory L2/3 neurons in response to tran-
sient visuomotor mismatches in both groups of mice.
Mismatch responses in excitatory neurons were
strongly experience dependent and driven by a tran-
sient release from inhibition mediated by somato-
statin-positive interneurons. These data are consis-
tent with a model in which L2/3 of V1 computes a
difference between an inhibitory visual input and an
excitatory locomotion-related input, where the bal-
ance between these two inputs is finely tuned by
visuomotor experience.

INTRODUCTION

Sensory feedback is inherently coupled to movement, and
sensorimotor coupling is necessary for both the development
(Held and Hein, 1963; Hein and Held, 1967) and the maintenance
(Leonardo and Konishi, 1999; Nordeen and Nordeen, 1992) of
sensory-guided behaviors. In classical experiments, Held and
Hein demonstrated that cats reared with normal visual experi-
ence but without visuomotor coupling fail to perform simple visu-
ally guided behaviors (Held and Hein, 1963). This behavioral
impairment is restricted to the movements that are decoupled
from sensory feedback during development (Hein and Held,
1967). Thus, sensory-guided behaviors rely on a mechanism to
integrate sensory input and motor output that is instructed by
experience. It is still unclear what the neural circuits are that
underlie this type of sensorimotor integration and how they are
shaped by sensorimotor experience during development.

Visual responses in primary visual cortex (V1) are known to
depend on visual experience during development (Blakemore
and Cooper, 1970; Hirsch and Spinelli, 1970; Hubel and Wiesel,
1970). In anesthetized or immobile animals, neural activity in V1
is known to closely reflect visual stimuli presented to the animal
(Hubel and Wiesel, 1962; Niell and Stryker, 2008). Based on this,
activity in V1 is classically interpreted in a representational
framework (Marr, 1982), where neural responses are described
in terms of receptive fields and signal the presence of a specific
visual stimulus in the environment. However, it is becoming
increasingly clear that this interpretation of the function of visual
cortex is incomplete. In monkeys freely moving their eyes,
response patterns of neurons in V1 give surprisingly poor reflec-
tions of what an animal is viewing (Livingstone et al., 1996). One
possible cause for this are motor-related signals. Self-generated
locomotion has been shown to modulate visual responses (Fu
et al., 2014; Niell and Stryker, 2010; Polack et al., 2013), and to
even drive activity in V1 independent of visual input (Keller
et al., 2012; Saleem et al., 2013). Thus, activity in V1 cannot be
explained by visual input alone and is likely the result of an inte-
gration of sensory and motor-related signals.

An alternate framework within which the activity in visual cor-
tex can be explained is that of predictive coding. It posits that the
brain continuously predicts sensory feedback based on an inter-
nal model of the environment (Friston, 2005; Gregory, 1980; Rao
and Ballard, 1999; Wolpert et al., 1995). Evidence for this inter-
pretation comes from the finding that a subset of neurons in V1
selectively responds to a mismatch between predicted and
actual visual feedback (Keller et al., 2012; Saleem et al., 2013).
Similar feedback mismatch responses have also been described
in primate primary auditory cortex (Eliades and Wang, 2008) and
primary auditory pallium of songbirds (Keller and Hahnloser,
2009). If such feedback mismatch responses signal a deviation
from a prediction that is based on a learned relationship between
motor output and sensory feedback, then they should depend on
sensorimotor experience.

To test this, we reared mice in a virtual reality system either un-
der coupled or non-coupled (yoked) visuomotor conditions and
subsequently probed neural activity in layer 2/3 of V1. We found
that responses to a mismatch between actual and expected
visual input occurred only in mice that experienced normal visuo-
motor coupling. Using a simple model, in which an excitatory
neuron computes a difference between an inhibitory visual input
and an excitatory prediction of visual input, we show that

Cell 169, 1291-1302, June 15, 2017 ª 2017 Elsevier Inc.

---

## 

mismatch responses can be explained by a relief from visually
driven inhibition. By recording the activity of genetically identified
interneurons in visual cortex, we show that this visual inhibition is
likely mediated by somatostatin (SST) interneurons. Finally, we
show that normal visuomotor experience restores sensorimotor
integration. Together, our data are consistent with a predictive-
coding interpretation of the function of visual cortex, where the
balance between feedforward and top-down input underlying
the computation of visuomotor mismatch is finely tuned by
visuomotor experience. In this way, visuomotor experience
fundamentally shapes the functional development of visual pro-
cessing in primary visual cortex.

RESULTS

To experimentally control the visuomotor experience of mice,
they were dark-reared from birth and only exposed to visual
stimulation in six separate 2-hr training sessions spaced by
48 hr over the course of 12 days, starting on postnatal day 32
(Figure 1A). During these sessions each mouse was trained
either in a coupled visuomotor condition (coupled trained [CT]),
in which the visual flow feedback was coupled to the locomotion
of the mouse in a virtual environment, or in a non-coupled condi-
tion (non-coupled trained [NT]) in which visual flow was indepen-
dent of the mouse's locomotion (Figure 1B; Movie S1). Mice
were head-fixed on a spherical treadmill (Dombeck et al.,
2007) surrounded by a toroidal screen that provided visual flow
feedback in the form of full-field vertical gratings on the walls
of a virtual corridor. To match the visual experience of both
groups, mice were trained in pairs (one CT and one NT mouse)
in two separate virtual environments such that the locomotion
of the CT mouse was used to control the visual flow of both vir-
tual environments. In this way, both CT and NT mice experienced
identical visual flow. Both groups of mice were exposed to light
only in this virtual reality environment during the six training ses-
sions, every other day for 2 hr, and were otherwise fully dark-
reared. A third group of mice was reared and trained in complete
darkness (dark trained [DT]). After the six training sessions, we
recorded neural activity in V1 of all three groups of mice by
two-photon imaging of a genetically encoded calcium indicator
GCaMP5 (Akerboom et al., 2012) or GCaMP6f (Chen et al.,
2013) during different visual flow feedback conditions in two im-
aging sessions spaced by 2 days, starting on postnatal day 44.
Subsequently, mice were exposed to a normal light/dark cycle
and imaged for an additional three sessions, again spaced by
2 days (Figure 1A). Imaging sessions for all groups of mice con-
sisted of one or two repetitions of approximately 8 min of loco-
motion coupled to visual flow feedback (closed-loop session)
and two replays of the same visual flow patterns during an
open-loop session to quantify visual responses (Movie S2). To
probe for feedback mismatch responses, we briefly halted visual
flow for 1 s at random times during the closed-loop session
(referred to as mismatch). Open-loop sessions consisted of a
playback of the visual flow that the mouse had generated during
the closed-loop session including brief visual flow halts, which
we refer to as playback halts. Note that analysis of playback halts
was restricted to times when the mouse was not running (see
STAR Methods). Mice were free to run during the entire experi-

ment, including open-loop sessions and did so spontaneously.
In early sessions, mice that exhibited low locomotor activity
were prompted to run using air-puffs to the neck. CT and NT
mice exhibited similar locomotion behavior during both training
and imaging sessions (Figures S1A and S1B).

Mismatch Responses in Excitatory Neurons Depend on
Visuomotor Experience
To test whether mismatch responses in layer 2/3 excitatory neu-
rons in V1 depend on coupled sensorimotor experience, we ex-
pressed GCaMP5 in C57BL/6 mice (three CT and three NT) and
GCaMP6f in vesicular GABA transporter (vGAT)-Cre (Vong et al.,
2011) 3 Ai14 (Madisen et al., 2010) mice (six CT and six NT) using
an adeno-associated virus (AAV) vector (AAV2/1-EF1a-GCaMP,
see STAR Methods). In vGAT-Cre 3 Ai14 mice, inhibitory
neurons express the red fluorescent protein tdTomato, which
allowed us to restrict analysis to identified excitatory neurons.
In these mice, we found that 96.8% ± 0.7% (mean ± SEM) of
GCaMP6f labeled neurons were excitatory (Figures S1C and
S1D). Thus, for all following analysis we pooled putative excit-
atory neurons of the C57BL/6 mice and the identified excitatory
neurons of the vGAT-Cre 3 Ai14 mice. In total, we recorded from
2,259 excitatory neurons in CT mice (996 putative excitatory and
1,263 identified excitatory neurons) and 2,104 excitatory neu-
rons in NT mice (764 putative excitatory and 1,340 identified
excitatory neurons).

We found that in CT mice, a considerable fraction of excitatory
neurons responded to mismatch (865 of 2,259 neurons or 38.3%;
Figures 1C and 1D) resulting in a large population mismatch
response (Figure 1E). In CT mice, mismatch responses cannot
be explained by visual input alone as there was no population
response to playback halt (Figures 1C and 1E; note, mismatch
and playback halt are identical visual stimuli). This is consistent
with what we previously found in normally reared mice (Keller
et al., 2012). In NT mice, the fraction of neurons that responded
to mismatch was smaller (425 of 2,104 neurons or 20.2%), and
the population response to mismatch was weaker than in CT
mice (Figures 1E and S1E). Interestingly, in NT mice the response
to mismatch was of similar magnitude as the response to play-
back halt (Figure 1E), and individual neurons often responded
to both mismatch and playback halt (Figures S1F and S1G).
With increasing mismatch response, neurons in CT, but not NT,
mice became increasingly selective for mismatch (Figure S1H).
Thus, whereas in CT mice, mismatch responses were strongly
dependent on motor-related inputs, mismatch responses in NT
mice were only weakly modulated by motor-related signals. In
both CT and NT mice, the response reliability of mismatch
responsive neurons increased with average amplitude of the
mismatch response. On average mismatch neurons responded
to 37.5% of mismatches in CT mice and to 33.8% in NT mice
(Figure S1I). A subset of neurons responded with a decrease in
activity to mismatch as well as playback halts (Figures 1D and
S1J). This type of response possibly reflects a visual response
driven by visual flow: upon cessation of the visual flow, these
neurons decrease their response.

The differences in mismatch responses between CT and NT
mice could not be explained by differences in average visual or
motor-related input to V1. Both the running-onset activity during

Cell 169, 1291-1302, June 15, 2017

---

## 

the closed-loop session (referred to as running-onset response)
as well as the visual flow onset responses during open-loop
sessions (referred to as playback-onset response) were similar
when comparing responses in CT and NT mice (Figure 1F). In
dark-trained mice, running-onset responses were normal, but
mismatch and playback halt responses were smaller (Figure S2).
This suggests that visual and motor-related inputs are main-
tained independently, and that visuomotor coupling is necessary

for the development of normal integration of visual and motor-
related inputs.

Mismatch Responses Can Be Explained as a Difference
between an Excitatory Prediction and an Inhibitory
Visual Input
Motor-related inputs have been shown to drive activity in mouse
V1 (Keller et al., 2012; Saleem et al., 2013). One simple model to

Figure 1. Mismatch Responses in Excitatory Neurons Depend on Visuomotor Experience
(A) Experimental timeline. Mice were dark-reared from birth. AAV injection and imaging window implantation occurred on postnatal day 30 (P30). From P32 to
P42, mice had six training sessions in coupled (coupled trained [CT]), non-coupled (non-coupled trained [NT]), or dark (dark trained [DT]) conditions, followed by
two to five imaging sessions beginning at P44 and spaced by 2 days. Some of the mice were put on a normal 12-hr/12-hr light/dark cycle after the second imaging
session.
(B) Schematic of the training setup. Mice were trained in pairs; visual flow (black arrows) on both training setups was coupled to the locomotion of the CT mouse
(blue arrows). The NT mouse was free to run but had no influence on the visual flow it was seeing.
(C) Sample fluorescence traces (DF/F, black lines) of an excitatory neuron in a CT (left) and a NT (right) mouse, during a closed-loop (top traces) and an open-loop
session (open-loop sessions consisted of a replay of the visual flow generated during the preceding closed-loop session, bottom traces). Vertical bars indicate
mismatch (orange) and playback halt (green) events. Binarized visual flow (green) and running speed (purple) are indicated below the fluorescence traces. In CT
mice, we found neurons that selectively respond to mismatch, whereas in NT mice, neurons that responded to mismatch also responded to corresponding
playback halts in open-loop sessions. Note that all data presented in this and the following panels are from the first imaging day.
(D) Average mismatch response (DF/F) of all neurons in CT mice (left, nine mice, 2,259 neurons) and NT mice (right, nine mice, 2,104 neurons), sorted by amplitude
of mismatch response. Black and gray shading to the right indicates significance of responses (gray: p R 0.05, black: p < 0.05, Mann-Whitney U test; see STAR
Methods). Orange bar marks the duration of mismatch. In CT mice, the fraction of neurons with a significant mismatch response was larger than in NT mice
(CT: 40% ± 5%; NT: 26% ± 5%, p = 0.03, Mann-Whitney U test; see STAR Methods).
(E) The average population response (DF/F) to mismatch (solid) was stronger in CT (blue) than in NT (red) mice. Population response to playback halt was
negligible in CT mice, but was as large as the mismatch response in NT mice (dashed lines). Orange area indicates duration of mismatch; shading indicates SEM.
The data in the different curves are compared bin-by-bin (100-ms bins) using a Student's t test. Bins with a significant difference (p < 0.01) are marked by a black
line above the curves; those without are marked as light gray (see STAR Methods). Each comparison is marked by a pair of line segments to the left, corre-
sponding in color and line style to the data plotted, indicating which two curves are being compared.
(F) Same as in (E), but for running onset in closed-loop sessions (solid lines) and playback onset in open-loop sessions (dashed lines, see STAR Methods). Shading
indicates SEM.
See also Figures S1 and S2 and Movies S1 and S2.

> Figure caption (from PDF text): Figure 1. Mismatch Responses in Excitatory Neurons Depend on Visuomotor Experience
(A) Experimental timeline. Mice were dark-reared from birth. AAV injection and imaging window implantation occurred on postnatal day 30 (P30). From P32 to
P42, mice had six training sessions in coupled (coupled trained [CT]), non-coupled (non-coupled trained [NT]), or dark (dark trained [DT]) conditions, followed by
two to five imaging sessions beginning at P44 and spaced by 2 days. Some of the mice were put on a normal 12-hr/12-hr light/dark cycle after the second imaging
session.
(B) Schematic of the training setup. Mice were trained in pairs; visual flow (black arrows) on both training setups was coupled to the locomotion of the CT mouse
(blue arrows). The NT mouse was free to run but had no influence on the visual flow it was seeing.
(C) Sample fluorescence traces (DF/F, black lines) of an excitatory neuron in a CT (left) and a NT (right) mouse, during a closed-loop (top traces) and an open-loop
session (open-loop sessions consisted of a replay of the visual flow generated during the preceding closed-loop session, bottom traces). Vertical bars indicate
mismatch (orange) and playback halt (green) events. Binarized visual flow (green) and running speed (purple) are indicated below the fluorescence traces. In CT
mice, we found neurons that selectively respond to mismatch, whereas in NT mice, neurons that responded to mismatch also responded to corresponding
playback halts in open-loop sessions. Note that all data presented in this and the following panels are from the first imaging day.
(D) Average mismatch response (DF/F) of all neurons in CT mice (left, nine mice, 2,259 neurons) and NT mice (right, nine mice, 2,104 neurons), sorted by amplitude
of mismatch response. Black and gray shading to the right indicates significance of responses (gray: p R 0.05, black: p < 0.05, Mann-Whitney U test; see STAR
Methods). Orange bar marks the duration of mismatch. In CT mice, the fraction of neurons with a significant mismatch response was larger than in NT mice
(CT: 40% ± 5%; NT: 26% ± 5%, p = 0.03, Mann-Whitney U test; see STAR Methods).
(E) The average population response (DF/F) to mismatch (solid) was stronger in CT (blue) than in NT (red) mice. Population response to playback halt was
negligible in CT mice, but was as large as the mismatch response in NT mice (dashed lines). Orange area indicates duration of mismatch; shading indicates SEM.
The data in the different curves are compared bin-by-bin (100-ms bins) using a Student's t test. Bins with a significant difference (p < 0.01) are marked by a black
line above the curves; those without are marked as light gray (see STAR Methods). Each comparison is marked by a pair of line segments to the left, corre-
sponding in color and line style to the data plotted, indicating which two curves are being compared.
(F) Same as in (E), but for running onset in closed-loop sessions (solid lines) and playback onset in open-loop sessions (dashed lines, see STAR Methods). Shading
indicates SEM.
See also Figures S1 and S2 and Movies S1 and S2.

This figure is composed of six panels (A through F) illustrating the experimental timeline, training setup, single-neuron traces, and population response data comparing two conditions: Coupled Training (CT) and Non-coupled Training (NT).

## 

explain mismatch responses in a layer 2/3 excitatory neuron
would be that such a neuron integrates an excitatory motor-
related input, in this case a prediction of visual flow based on
motor output and an inhibitory input that conveys feedforward
visual flow input (Figure 2A). In this model, inhibitory and excit-
atory inputs are balanced when predictions match feedforward
input. At mismatch onset, a decrease in visual inhibition would
then allow the excitatory motor-related input to activate the
neuron. If this is correct, mismatch neurons should receive excit-
atory motor-related input and inhibitory visual input. To test this,
we computed the correlation of the activity of each neuron with
visual flow and with running speed during the open-loop ses-

sions. As running and visual flow are independent in open-loop
sessions, the activity of a neuron that receives net inhibitory
visual input and net excitatory motor-related input would have
a negative correlation with visual flow and a positive correlation
with running speed and vice versa. Plotting the distribution of the
correlations of all neurons revealed that neurons with a strong
mismatch response had a negative correlation with visual flow
and a positive correlation with running speed, on average (Fig-
ure 2B). When comparing the entire population of neurons, we
found that, in CT mice, neurons with a positive correlation with
running speed tended to have a negative correlation with visual
flow, whereas in NT mice neurons with a positive correlation

Figure 2. Mismatch Responses Can Be Explained as a Difference between an Excitatory Motor-Related Input and an Inhibitory Visual Input
(A) Circuit model in which an excitatory mismatch neuron (MM, gray) integrates excitatory motor-related input and inhibitory visual input relayed by a local
inhibitory interneuron (orange) to compute the difference between predicted and actual visual flow.
(B) Correlation coefficients between neural activity (DF/F) of layer 2/3 excitatory neurons with running speed and with visual flow in CT (left; nine mice) and NT
(right; nine mice) mice during open-loop sessions. Each dot represents a single neuron (CT: 2,259 neurons; NT: 2,104 neurons). Dot color indicates the amplitude
of the mismatch response. Black circles indicate the mean correlation values. The angle A indicated by the solid black line is the average angle between the first
principle component of the distribution and the y axis (see STAR Methods). Note that all data presented in this and the following panels are from the first
imaging day.
(C) Mean angle of the first principle component relative to the y axis of the distribution of correlation coefficients as in (B) for CT (n = 9) and NT mice (n = 9). Error
bars indicate SEM. Mann-Whitney U test, p = 0.04.
(D) Spiking output of a simple conductance-based leaky integrate-and-fire neuron (LIF) was convolved with a unitary calcium-kernel to simulate neuronal activity
during closed-loop and open-loop sessions. Excitatory and inhibitory inputs were approximated by running speed (aR) and visual flow (bV); e.g., for scaling
factors a > 0 and b < 0, excitatory input is proportional to running speed, and inhibitory input is proportional to visual flow. By varying a and b systematically, we
calculated correlation maps with data from open-loop sessions. The scaling factors maximizing the correlation map were used to simulate activity during closed-
loop sessions (Figure 2E).
(E) Sample fluorescence (DF/F) traces of two neurons responding to mismatch from two mice during a closed-loop session (black traces) and the corresponding
simulated traces (pink traces). Note that the simulation parameters are based on optimization during open-loop sessions. Running speed, visual flow, and
mismatch are labeled as in (Figure 1C). Also shown is the FEV: fraction of explained variance (see STAR Methods) for each example neuron.
(F) Lower left: distribution of the fraction of variance explained (2,259 neurons), estimated as the squared correlation (R2) coefficient between model output and
calcium activity during the closed-loop session. Top right: average correlation map and average location of maxima (black crosses) for neurons with significant
positive responses to mismatch, averaged over mice (nine mice, top 50% of significant neurons per mouse).
See also Figures S2 and S3.

> Figure caption (from PDF text): Figure 2. Mismatch Responses Can Be Explained as a Difference between an Excitatory Motor-Related Input and an Inhibitory Visual Input
(A) Circuit model in which an excitatory mismatch neuron (MM, gray) integrates excitatory motor-related input and inhibitory visual input relayed by a local
inhibitory interneuron (orange) to compute the difference between predicted and actual visual flow.
(B) Correlation coefficients between neural activity (DF/F) of layer 2/3 excitatory neurons with running speed and with visual flow in CT (left; nine mice) and NT
(right; nine mice) mice during open-loop sessions. Each dot represents a single neuron (CT: 2,259 neurons; NT: 2,104 neurons). Dot color indicates the amplitude
of the mismatch response. Black circles indicate the mean correlation values. The angle A indicated by the solid black line is the average angle between the first
principle component of the distribution and the y axis (see STAR Methods). Note that all data presented in this and the following panels are from the first
imaging day.
(C) Mean angle of the first principle component relative to the y axis of the distribution of correlation coefficients as in (B) for CT (n = 9) and NT mice (n = 9). Error
bars indicate SEM. Mann-Whitney U test, p = 0.04.
(D) Spiking output of a simple conductance-based leaky integrate-and-fire neuron (LIF) was convolved with a unitary calcium-kernel to simulate neuronal activity
during closed-loop and open-loop sessions. Excitatory and inhibitory inputs were approximated by running speed (aR) and visual flow (bV); e.g., for scaling
factors a > 0 and b < 0, excitatory input is proportional to running speed, and inhibitory input is proportional to visual flow. By varying a and b systematically, we
calculated correlation maps with data from open-loop sessions. The scaling factors maximizing the correlation map were used to simulate activity during closed-
loop sessions (Figure 2E).
(E) Sample fluorescence (DF/F) traces of two neurons responding to mismatch from two mice during a closed-loop session (black traces) and the corresponding
simulated traces (pink traces). Note that the simulation parameters are based on optimization during open-loop sessions. Running speed, visual flow, and
mismatch are labeled as in (Figure 1C). Also shown is the FEV: fraction of explained variance (see STAR Methods) for each example neuron.
(F) Lower left: distribution of the fraction of variance explained (2,259 neurons), estimated as the squared correlation (R2) coefficient between model output and
calcium activity during the closed-loop session. Top right: average correlation map and average location of maxima (black crosses) for neurons with significant
positive responses to mismatch, averaged over mice (nine mice, top 50% of significant neurons per mouse).
See also Figures S2 and S3.

This figure, titled "Mismatch Responses Can Be Explained as a Difference between an Excitatory Motor-Related Input and an Inhibitory Visual Input," is composed of six panels (A through F) presenting a combination of circuit diagrams, scatter plots, correlation maps, and time-series traces.

## 

with running speed tended to also have a positive correlation
with visual flow. We quantified this interaction for every mouse
as the angle (A) of the first principal component of the correlation
scatterplot and found that, in CT mice, this angle was on average
negative (41 ± 10, mean ± SEM), whereas in NT mice it was
on average positive (9 ± 13, mean ± SEM; Figures 2B and
2C). This suggests that visuomotor coupling establishes a
balance between inhibition and excitation, such that those
layer 2/3 excitatory neurons that are strongly activated by
running also are also strongly inhibited by visual flow.

To test this model further, we implemented a conductance
based leaky-integrate-and-fire (LIF) model (Salinas and Sejnow-
ski, 2001) with two free parameters: a scaling factor for the
running-related input (a) and a scaling factor for the visual input
(b),whichwereused tomodulatetheexcitatoryandinhibitorycon-
ductances. The spiking output of the LIF model was convolved
with a calcium kernel to generate a simulated calcium response
(Figures 2D and 2E; see STAR Methods). Using data from open-
loop sessions, we optimized the correlation between the model
output and neural activity with a grid search over a and b for every
excitatory neuron. We then predicted the activity of each excit-
atory neuron during the closed-loop session by using visual flow
and running speed of that session as inputs to the LIF model opti-
mized for the particular neuron (Figure 2E). We found that the
average fraction of explained variance, estimated by a cross vali-
dation approach on the open-loop session data (see STAR
Methods), was twice as large when using a model based on visual
flow and running speed as when using a model based on just vi-
sual flow or just running speed (full model R2 = 0.06; just visual
flow R2 = 0.02;just running speed R2 = 0.03; p < 0.01 for both com-
parisons, Mann-Whitney U test; Figure 2F). We then averaged the
correlation maps generated by the grid search (see STAR
Methods) for excitatory neurons with a significantly positive

response to mismatch and found that activity of these neurons
could be best approximated when the motor-related conduc-
tance is positive (a > 0) and the visual conductance is negative
(b < 0) (Figure 2F). This shows that mismatch responses in excit-
atory neurons can be explained by a combination of an excitatory
motor-related input and inhibition by visual flow. Consistent with a
visually driven inhibition of mismatch neurons, mismatch respon-
sive neurons exhibited a decrease of activity in response to the
onset of visual flow in open-loop conditions (Figures S3A-S3C).

SST Interneurons Decrease Activity during Mismatch
As most long-range inputs to V1 are excitatory, feedforward vi-
sual inhibition would need to be relayed by local inhibitory neu-
rons. These neurons would have to be strongly driven by visual
flow and, as a consequence, decrease activity in response to a
brief stop in visual flow during mismatch and playback halt. To
probe the responses of different inhibitory neuron subtypes,
we repeated the training and imaging protocol using four
different Cre driver lines to selectively express GCaMP6f
(AAV2/1-EF1a-DIO-GCaMP6f-WPRE) in SST (Taniguchi et al.,
2011), vasoactive intestinal polypeptide (VIP) (Taniguchi et al.,
2011), parvalbumin (PV) (Hippenmeyer et al., 2005), or neuropep-
tide-Y (NPY) (Gong et al., 2007) interneurons. The SST-Cre, VIP-
Cre, and PV-Cre lines collectively target approximately 80% of
interneurons in mouse V1 and the labeled populations are largely
non-overlapping (Pfeffer et al., 2013).

We found that SST interneurons exhibited a higher correlation
with visual flow than other interneuron subtypes or excitatory
neurons (Figure 3). Moreover, of the four interneuron subtypes,
only SST interneurons responded, on average, with a drop in
activity to a brief stop in visual flow both during mismatch and
playback halt (Figure 4A). Notably, this decrease in average
activity on visual flow halt was independent of visuomotor expe-
rience, as it was present in both CT (five mice, 118 neurons) and
NT mice (five mice, 157 neurons), indicating that the visual input
onto SST neurons is established independently of motor-related
input. Locomotion strongly increased visual responses in SST
interneurons (Figure 4B), but running-onset responses were
almost completely absent in darkness (Figure S3D), consistent
with a predominantly visual drive to SST interneurons. Overall,
the responses of SST interneurons to mismatch were diverse
(Figure S3E), indicating that SST expression does not mark
one homogeneous functional class of interneurons.

The mismatch and playback halt responses of VIP interneu-
rons were independent of visuomotor experience. In both CT
and NT mice, they responded with an increase of activity to
mismatch but not to playback halt (Figure 4C; CT: three mice,
189 neurons; NT: three mice, 137 neurons). Given that VIP inter-
neurons receive direct inhibitory input from SST interneurons
(Pfeffer et al., 2013), mismatch responses may result from the
combination of a running-related excitatory input to VIP interneu-
rons (Fu et al., 2014) and a relief from SST interneuron-mediated
inhibition. Interestingly, running-related input to VIP interneurons
was strongly experience dependent. VIP interneurons were
driven only by running onset during closed-loop sessions in CT
but not in NT mice (Figure 4D). Consistent with the strong reduc-
tion of running-onset responses in SST interneurons in darkness,
a running-related input to VIP interneurons in NT mice was

Figure 3. SST Interneurons Are Strongly Driven by Visual Flow
Average correlation of neural activity with visual flow during open-loop ses-
sions for excitatory neurons (average correlations: CT: 0.00, NT: 0.01) and
SST (CT: 0.13, NT: 0.04), VIP (CT: 0.01, NT: 0.03), PV (CT: 0.01, NT: 0.00),
and NPY (CT: 0.02, NT: 0.02) interneurons in CT and NT mice. Average cor-
relation of activity with visual flow was highest for SST interneurons. Error bars
indicates SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not significant, p R 0.05,
Student's t test.

> Figure caption (from PDF text): Figure 3. SST Interneurons Are Strongly Driven by Visual Flow
Average correlation of neural activity with visual flow during open-loop ses-
sions for excitatory neurons (average correlations: CT: 0.00, NT: 0.01) and
SST (CT: 0.13, NT: 0.04), VIP (CT: 0.01, NT: 0.03), PV (CT: 0.01, NT: 0.00),
and NPY (CT: 0.02, NT: 0.02) interneurons in CT and NT mice. Average cor-
relation of activity with visual flow was highest for SST interneurons. Error bars
indicates SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not significant, p R 0.05,
Student's t test.

This figure is a set of comparative bar/point plots illustrating the average correlation between neural activity and visual flow across different types of interneurons in two experimental conditions, CT and NT.

**1. Overall Layout & Structure:**
The figure is structured as a single, multi-series scatter plot with error bars. The x-axis represents different types of neural populations (interneurons and excitatory neurons), while the y-axis quantifies the correlation coefficient. The data points are differentiated by color and shape to represent the two experimental conditions (CT and NT).

**2. Visual Components & Symbols:**
*   **Axes:** The vertical axis (Y-axis) is labeled "Correlation of activity with visual flow" and ranges from approximately -0.1 to 0.15, marked in increments of 0.05. The horizontal axis (X-axis) lists the different neural populations being tested.
*   **Data Points:** Two distinct markers are used:
    *   Blue circles ($\circ$): Represent the CT condition.
    *   Red circles ($\bullet$): Represent the NT condition.
*   **Error Bars:** Vertical lines extending from each data point indicate the Standard Error of the Mean (SEM).
*   **Significance Markers:** Above and below the data points, asterisks ($\text{*}$, $\text{**}$, $\text{***}$) and text annotations ("n.s.") are used to denote statistical significance based on a Student's t-test.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** "Correlation of activity with visual flow"
*   **X-Axis Labels (from left to right):** "SST", "Excitatory", "VIP", "PV", and "NPY".
*   **Legend:** A legend in the upper right corner identifies the symbols:
    *   Blue circle ($\circ$): CT
    *   Red circle ($\bullet$): NT

**4. Data Trends & Details:**
The plot displays the following specific data trends:

*   **SST Interneurons:**
    *   CT (Blue): Shows a high positive correlation, approximately 0.13. This point is marked with "***" (p < 0.001).
    *   NT (Red): Shows a lower positive correlation, approximately 0.04. This point is marked with "***" (p < 0.001).
*   **Excitatory Neurons:**
    *   CT (Blue): Shows a correlation near 0.00, marked with "***" (p < 0.001).
    *   NT (Red): Shows a small negative correlation, approximately -0.01, marked with "***" (p < 0.001).
*   **VIP Interneurons:**
    *   CT (Blue): Shows a correlation near 0.00, marked with "***" (p < 0.001).
    *   NT (Red): Shows a small negative correlation, approximately -0.03, marked with "***" (p < 0.001).
*   **PV Interneurons:**
    *   CT (Blue): Shows a correlation near 0.00, marked with "**" (p < 0.01).
    *   NT (Red): Shows a correlation near 0.00, marked with "*" (p < 0.05).
*   **NPY Interneurons:**
    *   CT (Blue): Shows a correlation near 0.02.
    *   NT (Red): Shows a correlation near 0.02. This pair is marked "n.s." (not significant, p > 0.05).

**5. Contextual Caption Integration:**
The caption confirms the identity of the plotted populations: SST, Excitatory neurons, VIP, PV, and NPY interneurons. It specifies that the correlations shown are for "open-loop sessions." The caption further clarifies the specific average correlation values:
*   Excitatory neurons (CT: 0.00, NT: $\approx -0.01$)
*   SST (CT: 0.13, NT: 0.04)
*   VIP (CT: $\approx -0.01$, NT: $\approx -0.03$)
*   PV (CT: $\approx -0.01$, NT: 0.00)
*   NPY (CT: 0.02, NT: 0.02)

The caption also notes that the correlation was highest for SST interneurons, which is visually supported by the highest positive value (CT: 0.13). The statistical notations ($\text{*}$, $\text{**}$, $\text{***}$) correspond to $p < 0.05$, $p < 0.01$, and $p < 0.001$, respectively, based on a Student's t test.

Cell 169, 1291-1302, June 15, 2017

---

## 

unmasked in darkness (Figure S3F). Taken together, our findings
suggest that the inhibitory connection from SST interneurons
onto VIP interneurons is stronger in absence of visuomotor
experience.

Finally, responses in both PV interneurons (CT: five mice, 498
neurons; NT: six mice, 344 neurons) and NPY interneurons
(CT: three mice, 189 neurons; NT: three mice, 137 neurons)
were behavioral state and visuomotor-experience dependent.
These two interneuron subtypes were activated by mismatch
in CT mice but unresponsive to mismatch in NT mice and unre-
sponsive to playback halt in both CT and NT mice (Figures 4E
and S3G-S3I). This highly selective response to mismatch in
CT mice could be a direct consequence of the stronger activa-
tion of the excitatory neuron population in CT mice in response
to mismatch (Figure 1E). Either excitatory neurons recruit PV
and NPY interneurons only above a given activity level or the cal-
cium dynamics in PV and NPY interneurons are such that we are
unable to measure activity changes below a given threshold.
Note, however, that such a simple measurement threshold
cannot account for the observation that in CT mice the popula-
tion response of excitatory neurons to running onset is smaller
than that to mismatch (Figures 1E and 1F), but the running-onset
response of PV interneurons is larger than that to mismatch (Fig-
ures 4E and 4F). One potential consequence of a selective acti-
vation of PV interneurons in CT mice is that the PV activation
could lead to a response normalization in excitatory neurons
(Wilson et al., 2012) that narrows the population response to
mismatch. Consistent with this, we found that the distribution
of mismatch responses is narrower in CT mice (Figure S3J).
This narrowing of the distribution of mismatch responses could
function to make mismatch responses more selective to one
particular type of mismatch.

Our data indicate that layer 2/3 excitatory mismatch neurons
and a subset of VIP interneurons receive excitatory, motor-
related input, while a subset of SST interneurons is more strongly
driven by visual flow. Consistent with the finding that SST inter-
neurons receive strong input from surrounding excitatory neu-
rons (Adesnik et al., 2012; Fino and Yuste, 2011; Jiang et al.,
2015), we found that excitatory neurons whose activity corre-
lates positively with visual flow (CT: 24% or 539 of 2,259 of neu-
rons; NT: 24% or 513 of 2,104 neurons) exhibit a decrease in
activity on mismatch similar to SST interneurons (Figure S1J).
Based on the connectivity motif of excitatory neurons, SST and
VIP interneurons (Pfeffer et al., 2013; Pi et al., 2013), we propose
a schematic model circuit to explain mismatch responses in
layer 2/3 excitatory neurons (Figure 5A). SST interneurons target
the apical dendrites of layer 2/3 excitatory neurons (Markram
et al., 2004). A reduction of visual input onto SST interneurons
during mismatch thus relieves the apical dendrite of inhibition
and would allow excitatory motor-related input to activate the
neuron. Based on this model, we predict that both SST inter-
neuron activation and inhibition should lead to a decrease of
the mismatch response in excitatory neurons but should have
opposing effects on running-related activity in excitatory neu-
rons (Figure 5B). To test this, we pharmacogenetically manipu-
lated the activity of SST interneurons using designer receptors
exclusively activated by designer drugs (DREADDs) (Armbruster
et al., 2007). We injected either AAV-EF1a-DIO-hM4D(Gi)-
mCherry or AAV-EF1a-DIO-hM3D(Gq)-mCherry into V1 of nor-
mally reared SST-Cre mice. In addition, we unconditionally
transfected neurons with GCaMP6f to record mismatch and
running related activity in putative excitatory neurons. Note
that in these experiments we cannot exclude the possibility
that some of these putative excitatory neurons are non-SST

Figure 4. Experience-Dependent Visuomo-
tor Integration in Inhibitory Interneurons
(A) Average population responses to mismatch
(solid line) and playback halt (dashed line) for SST
interneurons from CT (blue, five mice, 118 neu-
rons) and NT (red, five mice, 157 neurons) mice.
For both CT and NT mice, SST interneurons re-
sponded with a decrease in activity to mismatch
and playback halt. Orange area indicates duration
of mismatch; shading indicates SEM. Note that all
data presented in (A)-(F) are from the first imaging
day. The data in the different curves are compared
bin-by-bin (100-ms bins) using a Student's t test.
Bins with a significant difference (p < 0.01) are
marked by a black line above the curves; those
without are marked as light gray (see STAR
Methods). Each of the four comparisons is marked
by a pair of line segments to the left, corre-
sponding in color and line style to the data plotted,
indicating which two curves are being compared.
(B) Same as in (A), but for running onset in closed-
loop sessions (solid lines) and playback onset in
open-loop sessions (dashed lines).
(C and D) Same as in (A and B), but for VIP in-
terneurons (CT: three mice, 189 neurons; NT: three
mice, 137 neurons). VIP interneurons responded with an increase in activity independent of experience but did not respond to playback halt.
(E and F) Same as in (A and B) but for PV interneurons (CT: five mice, 498 neurons; NT: six mice, 344 neurons). The mismatch response in PV interneurons was
strongly experience dependent.
See also Figure S3.

## 

interneurons. We found that DREADD inhibition of SST interneu-
rons led to an increase in running-related activity in excitatory
neurons, while DREADD activation of SST interneurons led to a
decrease in running-related activity (Figure 5C). In addition,
both inhibition and activation of SST interneurons led to a
decrease in the mismatch response of excitatory neurons (Fig-
ures 5D and 5E). These results are consistent with a model of
mismatch computation in which mismatch responses in layer
2/3 neurons are the result of a relief of SST interneuron-mediated
inhibition. To test the effect of a transient manipulation of
SST and VIP activity on mismatch responses, we injected
AAV-EF1a-GCaMP6f and either AAV-EF1a-DIO-ChrimsonR-
tdTomato (Klapoetke et al., 2014) or AAV-CAG-FLEX-ArchT-
tdTomato (Han et al., 2011) into V1 of normally reared SST-Cre
mice and VIP-Cre mice. We then identified putative excitatory

mismatch neurons based on their responses to mismatch events
in closed-loop sessions (in the following simply referred to as
mismatch neurons) and measured the responses of these neu-
rons to brief (1 s) activation or inhibition of SST or VIP interneu-
rons (see STAR Methods). We found that activation of SST
interneurons resulted in an inhibition of mismatch neurons that
was strong enough to fully suppress mismatch responses in
mismatch neurons when SST interneurons were activated
concurrently with a mismatch event (Figure 6A). Consistent
with this, inhibition of SST neurons resulted in an activation of
mismatch neurons and concurrent inhibition of SST interneurons
with a mismatch event resulted in increased mismatch re-
sponses (Figure 6B). Conversely, activation of VIP interneurons
resulted in an activation of mismatch neurons and an increase
of the mismatch response when VIP interneurons were activated

Figure 5. A Drop in SST Activity Leads to a Mismatch Response in Excitatory Neurons
(A) Schematic of a model circuit describing the computation of mismatch responses in layer 2/3 of V1. Excitatory neurons and VIP interneurons receive excitatory
motor-related input (purple arrow; dashed purple line depicts idealized running profile around a mismatch, indicated by orange shading). SST interneurons
receive visual flow input (green arrow; dashed green line depicts idealized visual flow around a mismatch, indicated by orange shading). Blue lines next to neurons
depict average mismatch responses of excitatory neurons (Figure 1E), SST (Figure 4A), and VIP (Figure 4C) interneurons from CT mice. During mismatch, visual
flow is halted and the activity of SST interneurons decreases, thereby disinhibiting the apical dendrites of mismatch neurons and allowing the excitatory motor-
related input to activate the neuron. VIP interneurons amplify this effect by further suppressing SST interneuron activity.
(B) Predicted effects of pharmacogenetic manipulation of SST interneurons on excitatory neurons. Idealized activity profiles of excitatory motor-related activity
(purple line) and SST interneuron activity for a short period of running during a closed-loop session including a mismatch (onset marked by vertical line). In normal
conditions (top), SST interneuron activity balances the motor-related input and the mismatch response of excitatory neurons is maximal (mismatch-triggered
difference between excitatory and inhibitory input, orange shading). Inhibition of SST interneurons (middle) should result in a smaller mismatch-induced dif-
ference in inhibition and therefore a smaller mismatch response as well as increased running-related activity. Excitation of SST interneurons (bottom) should also
result in smaller mismatch responses due to an over-inhibition of excitatory neurons but decreased running-related activity.
(C) Mean running related activity before and 30 min after injection of DREADD activator Clozapine-N-oxide (CNO) (5 mg/kg i.p.) in mice expressing an inhibitory
(left; 829 neurons, ***p < 0.001, Wilcoxon signed-rank test) or an excitatory (right; 411 neurons, ***p < 0.001, Wilcoxon signed-rank test) DREADD in SST
interneurons. Error bars indicate SEM.
(D) Average population mismatch responses of excitatory neurons before (green trace) and 30 min after (yellow trace) the injection of CNO in mice expressing an
inhibitory DREADD in SST interneurons (four mice, 829 neurons). Orange bar indicates duration of mismatch; shading indicates SEM. Statistical comparisons as
in Figure 1E.
(E) Same as in (D), but for mice expressing an excitatory DREADD in SST interneurons (two mice, 411 neurons).
See also Figure S7.

> Figure caption (from PDF text): Figure 5. A Drop in SST Activity Leads to a Mismatch Response in Excitatory Neurons
(A) Schematic of a model circuit describing the computation of mismatch responses in layer 2/3 of V1. Excitatory neurons and VIP interneurons receive excitatory
motor-related input (purple arrow; dashed purple line depicts idealized running profile around a mismatch, indicated by orange shading). SST interneurons
receive visual flow input (green arrow; dashed green line depicts idealized visual flow around a mismatch, indicated by orange shading). Blue lines next to neurons
depict average mismatch responses of excitatory neurons (Figure 1E), SST (Figure 4A), and VIP (Figure 4C) interneurons from CT mice. During mismatch, visual
flow is halted and the activity of SST interneurons decreases, thereby disinhibiting the apical dendrites of mismatch neurons and allowing the excitatory motor-
related input to activate the neuron. VIP interneurons amplify this effect by further suppressing SST interneuron activity.
(B) Predicted effects of pharmacogenetic manipulation of SST interneurons on excitatory neurons. Idealized activity profiles of excitatory motor-related activity
(purple line) and SST interneuron activity for a short period of running during a closed-loop session including a mismatch (onset marked by vertical line). In normal
conditions (top), SST interneuron activity balances the motor-related input and the mismatch response of excitatory neurons is maximal (mismatch-triggered
difference between excitatory and inhibitory input, orange shading). Inhibition of SST interneurons (middle) should result in a smaller mismatch-induced dif-
ference in inhibition and therefore a smaller mismatch response as well as increased running-related activity. Excitation of SST interneurons (bottom) should also
result in smaller mismatch responses due to an over-inhibition of excitatory neurons but decreased running-related activity.
(C) Mean running related activity before and 30 min after injection of DREADD activator Clozapine-N-oxide (CNO) (5 mg/kg i.p.) in mice expressing an inhibitory
(left; 829 neurons, ***p < 0.001, Wilcoxon signed-rank test) or an excitatory (right; 411 neurons, ***p < 0.001, Wilcoxon signed-rank test) DREADD in SST
interneurons. Error bars indicate SEM.
(D) Average population mismatch responses of excitatory neurons before (green trace) and 30 min after (yellow trace) the injection of CNO in mice expressing an
inhibitory DREADD in SST interneurons (four mice, 829 neurons). Orange bar indicates duration of mismatch; shading indicates SEM. Statistical comparisons as
in Figure 1E.
(E) Same as in (D), but for mice expressing an excitatory DREADD in SST interneurons (two mice, 411 neurons).
See also Figure S7.

This figure, titled "A Drop in SST Activity Leads to a Mismatch Response in Excitatory Neurons," is composed of five distinct panels (A, B, C, D, and E), illustrating a computational model and experimental results related to mismatch responses in V1.

## 

concurrently with a mismatch event (Figure 6C). Finally, inhibition
of VIP interneurons resulted in an inhibition of mismatch neurons
that was strong enough to suppress mismatch responses (Fig-
ure 6D). Note that even though these effects were stronger for
mismatch neurons than for putative excitatory neurons that did
not respond to mismatch (Figure S4), it is very likely only a subset
of SST and VIP interneurons that are part of the circuit involved in
mismatch responses in excitatory neurons. In summary, these
results are consistent with the classical cortical SST-VIP disinhi-
bitory circuit (Pfeffer et al., 2013; Pi et al., 2013) and suggest that
this circuit plays a central role in mismatch computation with
mismatch neurons under inhibitory control of SST interneurons.
Thus, the relief of SST-mediated visual inhibition combined with
a top-down motor-related excitatory drive can account for visuo-
motor mismatch responses in layer 2/3 excitatory neurons.

To test whether both CT and NT mice learn to perform visuo-
motor tasks after exposure to visuomotor coupling, we repeated
the training protocol with a separate cohort of mice. Instead of
going through the imaging paradigm after coupled or non-
coupled training, these mice were trained either to navigate a
2-dimensional (2D) virtual environment or to detect mismatch
(see STAR Methods). Both CT and NT mice learned to perform
the 2D virtual locomotion task over the course of six training ses-

sions of 1 hr each (Figures S5A and S5B). Also, both CT and NT
mice learned to report the occurrence of mismatch over the
course of three to five training sessions of 1 hr each (Figure S5C).
These findings suggest that visuomotor coupling rapidly estab-
lishes normal visuomotor processing even after prolonged
absence of coupling in NT mice.

Normal Visuomotor Experience Restores Normal
Visuomotor Integration in V1
Given that both CT and NT mice learned to perform visuomotor
tasks over the course of a few days, visuomotor coupling should
rapidly restore normal visuomotor processing in V1. To quantify
the change in neural processing in V1 with the exposure to visuo-
motor coupling, we measured mismatch responses in both CT
and NT mice over the course of 8 days following restoration of
visuomotor coupling (exposure to both open-loop and closed-
loop conditions and normal visuomotor experience with the
transfer to rearing in a normal light/dark cycle; Figure 1A). We
found that mismatch responses of excitatory neurons in CT
and NT mice equalized rapidly with normal visuomotor experi-
ence (Figures 7A-7C). The population mismatch responses of
SST and VIP interneurons remained stable throughout the
course of the experiment for both CT and NT mice (Figures 7D

Figure 6. Mismatch Neurons Are Inhibited by SST Activation or VIP Inhibition and Activated by SST Inhibition or VIP Activation
(A) Left: schematic of the experimental design. ChrimsonR was selectively expressed in SST interneurons and GCaMP6f in all neurons. We then locally activated
SST interneurons through the imaging objective while imaging GCaMP6f activity in all neurons. Right: response of putative excitatory mismatch-responsive
neurons (165 neurons, five mice) to mismatch (green line), optogenetic activation of SST interneurons during running (purple line), and concurrent mismatch and
optogenetic activation of SST interneurons (yellow line). Orange area indicates duration of mismatch and duration of optogenetic stimulation respectively;
shading indicates SEM. Statistical comparisons as in Figure 1E, but for 67-ms bins. Upper line marks comparison of manipulation only against baseline; lower line
marks comparison of mismatch only against concurrent mismatch and optogenetic stimulation.
(B) Left: as in (A), but expressing ArchT in SST interneurons. Right: responses of mismatch neurons (236 neurons, four mice) as in (A), but for optogenetic inhibition
of SST interneurons.
(C) Left: as in (A), but expressing ChrimsonR in VIP interneurons. Right: responses of mismatch neurons (114 neurons, four mice) as in (A), but for optogenetic
activation of VIP interneurons.
(D) Left: as in (A), but expressing ArchT in VIP interneurons. Right: responses of mismatch neurons (107 neurons, three mice) as in (A), but for optogenetic inhibition
of VIP interneurons. Error bars indicate SEM.
See also Figure S4.

> Figure caption (from PDF text): Figure 6. Mismatch Neurons Are Inhibited by SST Activation or VIP Inhibition and Activated by SST Inhibition or VIP Activation
(A) Left: schematic of the experimental design. ChrimsonR was selectively expressed in SST interneurons and GCaMP6f in all neurons. We then locally activated
SST interneurons through the imaging objective while imaging GCaMP6f activity in all neurons. Right: response of putative excitatory mismatch-responsive
neurons (165 neurons, five mice) to mismatch (green line), optogenetic activation of SST interneurons during running (purple line), and concurrent mismatch and
optogenetic activation of SST interneurons (yellow line). Orange area indicates duration of mismatch and duration of optogenetic stimulation respectively;
shading indicates SEM. Statistical comparisons as in Figure 1E, but for 67-ms bins. Upper line marks comparison of manipulation only against baseline; lower line
marks comparison of mismatch only against concurrent mismatch and optogenetic stimulation.
(B) Left: as in (A), but expressing ArchT in SST interneurons. Right: responses of mismatch neurons (236 neurons, four mice) as in (A), but for optogenetic inhibition
of SST interneurons.
(C) Left: as in (A), but expressing ChrimsonR in VIP interneurons. Right: responses of mismatch neurons (114 neurons, four mice) as in (A), but for optogenetic
activation of VIP interneurons.
(D) Left: as in (A), but expressing ArchT in VIP interneurons. Right: responses of mismatch neurons (107 neurons, three mice) as in (A), but for optogenetic inhibition
of VIP interneurons. Error bars indicate SEM.
See also Figure S4.

This figure, titled "Mismatch Neurons Are Inhibited by SST Activation or VIP Inhibition and Activated by SST Inhibition or VIP Activation," is composed of four main panels (A, B, C, and D), each presenting a combination of schematic diagrams and corresponding time-course plots.

---

### **Panel A: SST Activation**

**Left Schematic:**
*   This panel shows a schematic diagram illustrating the experimental setup. It depicts two neuronal types: **SST** (Somatostatin-expressing interneurons) and **VIP** (Vasoactive Intestinal Peptide neurons).
*   The SST neuron is shown with a schematic representation of the genetic tools: **SST-Cre mouse**, **AAV-Ef1a-DIO-ChrimsonR** (targeting SST neurons), and **AAV-Ef1a-GCaMP6f**.
*   The diagram shows the SST neuron connected to a general neuronal population (implied by the context of GCaMP6f expression).

**Right Plot:**
*   This is a time-course plot showing $\Delta F/F$ (change in fluorescence over baseline) versus Time [s].
*   **Y-axis:** $\Delta F/F$ [%], ranging from approximately -20% to 20%.
*   **X-axis:** Time [s], ranging from 0 to 3 seconds.
*   **Colored Lines (representing different conditions):**
    *   **Green line:** Labeled "Mismatch (MM)". This line shows a clear increase in $\Delta F/F$ during the initial period.
    *   **Purple line:** Labeled "SST activation". This line shows a sustained increase in $\Delta F/F$ during the stimulation period.
    *   **Yellow line:** Labeled "MM & SST act." (Mismatch and SST activation). This line shows a response that is modulated by the concurrent stimulation.
*   **Annotations:**
    *   An **orange shaded area** indicates the duration of "mismatch."
    *   A second, narrower **orange shaded area** indicates the duration of "optogenetic stimulation."
    *   The plot includes error bars representing SEM.
*   **Legend:** The legend identifies the lines: "Mismatch (MM)" (green), "SST activation" (purple), and "MM & SST act." (yellow).

---

### **Panel B: SST Inhibition**

**Left Schematic:**
*   This schematic is similar to Panel A's left side, showing SST and VIP neurons.
*   The genetic tools are specified as: **SST-Cre mouse**, **AAV-CAG-FLex-ArchT** (targeting SST neurons), and **AAV-Ef1a-GCaMP6f**.
*   The presence of ArchT suggests optogenetic inhibition.

**Right Plot:**
*   This is a time-course plot showing $\Delta F/F$ [%] versus Time [s].
*   **Y-axis:** $\Delta F/F$ [%], ranging from approximately -20% to 20%.
*   **X-axis:** Time [s], ranging from 0 to 3 seconds.
*   **Colored Lines (representing different conditions):**
    *   **Green line:** Labeled "Mismatch (MM)". Shows a typical response profile.
    *   **Purple line:** Labeled "SST inhibition". Shows a different response profile compared to the mismatch alone.
    *   **Yellow line:** Labeled "MM & SST inh." (Mismatch and SST inhibition). Shows the combined effect.
*   **Annotations:** The plot structure mirrors Panel A, with shaded areas indicating the duration of mismatch and optogenetic stimulation.
*   **Legend:** The legend identifies the lines: "Mismatch (MM)" (green), "SST inhibition" (purple), and "MM & SST inh." (yellow).

---

### **Panel C: VIP Activation**

**Left Schematic:**
*   This schematic shows SST and VIP neurons.
*   The genetic tools are specified as: **VIP-Cre mouse**, **AAV-Ef1a-DIO-ChrimsonR** (targeting VIP neurons), and **AAV-Ef1a-GCaMP6f**.
*   The presence of ChrimsonR suggests optogenetic activation.

**Right Plot:**
*   This is a time-course plot showing $\Delta F/F$ [%] versus Time [s].
*   **Y-axis:** $\Delta F/F$ [%], ranging from approximately -20% to 20%.
*   **X-axis:** Time [s], ranging from 0 to 3 seconds.
*   **Colored Lines (representing different conditions):**
    *   **Green line:** Labeled "Mismatch (MM)".
    *   **Purple line:** Labeled "VIP activation".
    *   **Yellow line:** Labeled "MM & VIP act." (Mismatch and VIP activation).
*   **Annotations:** Shaded areas indicate the duration of mismatch and optogenetic stimulation.
*   **Legend:** The legend identifies the lines: "Mismatch (MM)" (green), "VIP activation" (purple), and "MM & VIP act." (yellow).

---

### **Panel D: VIP Inhibition**

**Left Schematic:**
*   This schematic shows SST and VIP neurons.
*   The genetic tools are specified as: **VIP-Cre mouse**, **AAV-CAG-FLex-ArchT** (targeting VIP neurons), and **AAV-Ef1a-GCaMP6f**.
*   The presence of ArchT suggests optogenetic inhibition.

**Right Plot:**
*   This is a time-course plot showing $\Delta F/F$ [%] versus Time [s].
*   **Y-axis:** $\Delta F/F$ [%], ranging from approximately -20% to 20%.
*   **X-axis:** Time [s], ranging from 0 to 3 seconds.
*   **Colored Lines (representing different conditions):**
    *   **Green line:** Labeled "Mismatch (MM)".
    *   **Purple line:** Labeled "VIP inhibition".
    *   **Yellow line:** Labeled "MM & VIP inh." (Mismatch and VIP inhibition).
*   **Annotations:** Shaded areas indicate the duration of mismatch and optogenetic stimulation.
*   **Legend:** The legend identifies the lines: "Mismatch (MM)" (green), "VIP inhibition" (purple), and "MM & VIP inh." (yellow).

---
**General Notes:** All panels utilize a consistent structure: schematic representation of the circuit/manipulation followed by quantitative time-series data ($\Delta F/F$ vs. Time). The caption clarifies that the plots compare manipulation effects against baseline and mismatch-only conditions, with error bars indicating SEM.

Cell 169, 1291-1302, June 15, 2017

---

## 

and 7E). This is consistent with the idea that the mismatch
response of VIP and SST interneurons developed independent
of visuomotor coupling. Similar to excitatory neurons, mismatch

responses in PV and NPY interneurons equalized after restora-
tion of normal visuomotor coupling (Figures 7F and S6A). Inter-
estingly, we found not only an increase of mismatch responses

Figure 7. Normal Visuomotor Experience Restores Normal Visuomotor Integration
(A) Average responses to mismatch (solid lines) and playback halt (dashed lines) of neurons with positive correlation of activity with running speed (running
correlation greater than 0.05) and negative correlation of activity with visual flow (visual correlation smaller than 0.05) on the first imaging day (CT: 12% ± 2% of
neurons per mouse, nine mice; NT: 10% ± 3%, nine mice). Orange area indicates duration of mismatch; shading indicates SEM. Statistical comparison as in
Figure 1E.
(B) Same as (A), but for last imaging day (CT: 10% ± 2% of neurons per mouse, eight mice; NT: 9% ± 1%, seven mice).
(C) Average responses to mismatch and playback halt (see STAR Methods) of excitatory neurons selected as in (A) as a function of imaging days for CT and NT
mice. Mice were dark reared until the second imaging session (indicated by gray area). Error bars indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not
significant, p R 0.05, Mann-Whitney U test.
(D) Average population responses to mismatch of SST interneurons, as a function of imaging days for CT and NT mice (CT, five mice, 118 neurons; NT: five mice,
157 neurons). Statistical test as in (C). Error bars indicate SEM.
(E) As in (D) but for VIP interneurons (CT: three mice, 189 neurons; NT: three mice, 137 neurons).
(F) As in (D) but for PV interneurons (CT: five mice, 498 neurons; NT: six mice, 344 neurons).
(G) Mean angle of first principal component (as in Figures 2B and 2C; see STAR Methods) relative to the y axis for CT and NT mice as a function of imaging days.
Gray area indicates dark rearing; error bars indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not significant, p R 0.05, Mann-Whitney U test.
(H) Average pupil dilation in response to mismatch and playback halt for CT (25 mice) and NT mice (25 mice; see STAR Methods) on the first imaging day. Orange
area indicates duration of mismatch; shading indicates SEM. Statistical comparisons as in Figure 1E, but for p < 0.05.
(I) Average pupil dilation in response to mismatch and playback halt a function of imaging days for CT and NT mice. Gray area indicates dark rearing; error bars
indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, Mann-Whitney U test.
See also Figures S5 and S6.

> Figure caption (from PDF text): Figure 7. Normal Visuomotor Experience Restores Normal Visuomotor Integration
(A) Average responses to mismatch (solid lines) and playback halt (dashed lines) of neurons with positive correlation of activity with running speed (running
correlation greater than 0.05) and negative correlation of activity with visual flow (visual correlation smaller than 0.05) on the first imaging day (CT: 12% ± 2% of
neurons per mouse, nine mice; NT: 10% ± 3%, nine mice). Orange area indicates duration of mismatch; shading indicates SEM. Statistical comparison as in
Figure 1E.
(B) Same as (A), but for last imaging day (CT: 10% ± 2% of neurons per mouse, eight mice; NT: 9% ± 1%, seven mice).
(C) Average responses to mismatch and playback halt (see STAR Methods) of excitatory neurons selected as in (A) as a function of imaging days for CT and NT
mice. Mice were dark reared until the second imaging session (indicated by gray area). Error bars indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not
significant, p R 0.05, Mann-Whitney U test.
(D) Average population responses to mismatch of SST interneurons, as a function of imaging days for CT and NT mice (CT, five mice, 118 neurons; NT: five mice,
157 neurons). Statistical test as in (C). Error bars indicate SEM.
(E) As in (D) but for VIP interneurons (CT: three mice, 189 neurons; NT: three mice, 137 neurons).
(F) As in (D) but for PV interneurons (CT: five mice, 498 neurons; NT: six mice, 344 neurons).
(G) Mean angle of first principal component (as in Figures 2B and 2C; see STAR Methods) relative to the y axis for CT and NT mice as a function of imaging days.
Gray area indicates dark rearing; error bars indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, n.s., not significant, p R 0.05, Mann-Whitney U test.
(H) Average pupil dilation in response to mismatch and playback halt for CT (25 mice) and NT mice (25 mice; see STAR Methods) on the first imaging day. Orange
area indicates duration of mismatch; shading indicates SEM. Statistical comparisons as in Figure 1E, but for p < 0.05.
(I) Average pupil dilation in response to mismatch and playback halt a function of imaging days for CT and NT mice. Gray area indicates dark rearing; error bars
indicate SEM. *p < 0.05, **p < 0.01, ***p < 0.001, Mann-Whitney U test.
See also Figures S5 and S6.

## 

in NT mice with exposure to closed-loop sessions and normal
visuomotor experience, but also a decrease of mismatch re-
sponses in CT mice with exposure to open-loop sessions and
normal visuomotor experience. Similarly, we found that for the
distribution of visual flow and running speed correlations, the
angle of the first principle component (Figures 2B and 2C) equal-
ized and approached zero for both CT and NT mice (Figures 7G
and S6B). To quantify the behavioral response to mismatch on a
timescale similar to that of the equalization of neural dynamics,
we measured pupil dilation in response to mismatch. Mice ex-
hibited a small but measurable pupil dilation response with a
delay of approximately 450 ms after the neural response to a
mismatch (400 ms for CT, 500 ms for NT; see STAR Methods;
Figure 7H). This pupil dilation response was larger in CT mice
and may reflect a startle response. The pupil dilation response
also equalized with restoration of normal visuomotor experience,
with the same time course as neural activity (Figure 7I). Alto-
gether, these results suggest that the artificial restriction of visuo-
motor coupling to only a subset of movements (forward locomo-
tion and eye movements) leads to an overrepresentation of the
visuomotor processing of these movements that needs to be un-
learned for the restoration of normal visuomotor behavior. This is
consistent with the finding that a lack of visuomotor coupling for a
specific range of movements leads to behavioral impairments
that are specific to those movements (Hein and Held, 1967).

DISCUSSION

Here, we have shown that the development of responses to a
mismatch between predicted and actual visual feedback in
mouse V1 critically depends on coupled visuomotor experience.
These mismatch responses are thought to be the consequence
of predictive coding strategies that involve a comparison of
actual and predicted sensory feedback to compute a prediction
error or feedback mismatch. In this framework, predictions of
sensory feedback are based on an internal model of the environ-
ment. Deviations from predictions in the form of mismatch sig-
nals are then used to update the internal model (Bastos et al.,
2012; Rao and Ballard, 1999). As a consequence, it is likely
that predictions are systematically shaped by experience and
can adapt to changes in the coupling between motor output
and sensory feedback.

The mismatch responses we describe here could be the result
of a weak excitatory visual response to the playback halt stim-
ulus that is amplified by a running-related input. As mismatch
is generated simply by halting visual flow, this would mean that
the visual feature driving mismatch responses is either the nega-
tive acceleration of visual flow or simply a stationary grating
viewed while running. However, any model for mismatch re-
sponses based on an excitatory visual drive fails to explain
why mismatch responses scale linearly with the difference be-
tween running speed and visual flow speed in open-loop ses-
sions (Zmarz and Keller, 2016). Additionally, a model for
mismatch responses based on an excitatory visual input cannot
explain why mismatch responses tend to decrease activity on
playback onset (Figures S3A-S3C).

Our results are consistent with a model in which sensorimotor
mismatch signals are computed locally in layer 2/3 by a compar-

ator circuit that is shaped by experience. In this circuit, inhibition
by visual flow is balanced against an excitatory motor-related
input in mismatch neurons. SST interneurons mediate the inhibi-
tion by visual flow, while mutual inhibition between VIP and SST
interneurons (Pfeffer et al., 2013) acts to amplify the responses of
SST interneurons. Even though the average response of SST in-
terneurons to mismatch is a decrease in activity, this effect is
carried by only a subset of SST interneurons. Moreover, although
such a simplified model is sufficient to explain mismatch re-
sponses, the interactions between the different interneuron
subtypes are in all likelihood much richer than schematically
summarized here. PV interneurons, for example, could act to
normalize the mismatch response in excitatory neurons (Hofer
et al., 2011; Kerlin et al., 2010).

Given that SST interneurons provide visual inhibition to excit-
atory mismatch neurons and that mismatch responses in SST in-
terneurons do not depend on visuomotor experience (Figure 4A),
it is likely that visuomotor experience predominantly modifies the
synaptic inputs onto the excitatory neuron. In this way, a balance
of excitation and inhibition is established, possibly via mecha-
nisms similar to those resulting in the establishment of the bal-
ance between feedforward excitation and inhibition mediated
by PV interneurons (Xue et al., 2014). Note that the type of
mismatch neuron we describe here balances an excitatory
top-down input against an inhibition by visual flow and is active
when there is less visual input than predicted. Conversely, if a
neuron balances an inhibitory top-down input against an excit-
atory feedforward input, it would signal a visual input that is
stronger than predicted. Such a neuron would have classic visual
responses in a passively observing animal. Computationally
these two circuits are symmetric and would merely signal
different types of mismatch (Figure S7).

We speculate that the framework of predictive coding can be
used to describe cortical processing of sensory feedback for
every movement that results in a predictable change of sensory
input. We propose that the comparison of sensory input with a
top-down prediction may be a general principle of cortical func-
tion, where predictions from higher areas are continuously
compared to signals from lower areas, and mismatches between
the two are used to refine these predictions (Clark, 2013; Friston,
2010). It is intriguing to speculate that impairments in this com-
parison may underlie cortical dysfunctions where the balance
between predictions and sensory input is systematically per-
turbed (Frith et al., 2000; Sinha et al., 2014).

STAR+METHODS

Detailed methods are provided in the online version of this paper
and include the following:

d KEY RESOURCES TABLE

d CONTACT FOR REAGENT AND RESOURCE SHARING

d EXPERIMENTAL MODEL AND SUBJECT DETAILS

d METHOD DETAILS

B Surgery

B DREADD and optogenetic experiments

B Viral constructs

B Virtual reality environment setup

Cell 169, 1291-1302, June 15, 2017

---

## 

B Two-photon imaging

B Simultaneous two-photon imaging and optogenetic

stimulations

B Experimental design

B Mismatch detection paradigm and 2D virtual locomo-

tion task

d QUANTIFICATION AND STATISTICAL ANALYSIS

B Extraction of neuronal activity

B Data analysis

B Modified leaky integrate-and-fire neuron model

B Pupil dilation analysis

d DATA AND SOFTWARE AVAILABILITY

SUPPLEMENTAL INFORMATION

Supplemental Information includes seven figures and two movies and can be
found with this article online at 

AUTHOR CONTRIBUTIONS

A.A. and B.W. designed and conducted experiments. A.A. designed the model
and simulations. A.A. and B.W. analyzed data. A.A., B.W., and G.B.K. wrote
the manuscript.

ACKNOWLEDGMENTS

We thank Antonia Drinnenberg, Thomas Mrsic-Flogel, and Rainer Friedrich for
comments on earlier versions of the manuscript. We thank Daniela Gerosa-
Erni for production of the AAV vectors and the members of the Keller lab for
discussion, support, and comments on the manuscript. This work was sup-
ported by the Swiss National Science Foundation and the Novartis Research
Foundation.

Received: November 22, 2016
Revised: March 17, 2017
Accepted: May 12, 2017
Published: June 8, 2017