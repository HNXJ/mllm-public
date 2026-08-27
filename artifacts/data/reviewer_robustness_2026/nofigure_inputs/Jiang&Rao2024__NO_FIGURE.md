## Page 1

RESEARCH ARTICLE
Dynamic predictive coding: A model of
hierarchical sequence learning and prediction
in the neocortex

Linxing Preston JiangID1,2,3, Rajesh P. N. RaoID1,2,3*

1 Paul G. Allen School of Computer Science & Engineering, University of Washington, Seattle, Washington,
United States of America, 2 Center for Neurotechnology, University of Washington, Seattle, Washington,
United States of America, 3 Computational Neuroscience Center, University of Washington, Seattle,
Washington, United States of America

* rao@cs.washington.edu

Abstract

We introduce dynamic predictive coding, a hierarchical model of spatiotemporal prediction
and sequence learning in the neocortex. The model assumes that higher cortical levels
modulate the temporal dynamics of lower levels, correcting their predictions of dynamics
using prediction errors. As a result, lower levels form representations that encode
sequences at shorter timescales (e.g., a single step) while higher levels form representa-
tions that encode sequences at longer timescales (e.g., an entire sequence). We tested this
model using a two-level neural network, where the top-down modulation creates low-dimen-
sional combinations of a set of learned temporal dynamics to explain input sequences.
When trained on natural videos, the lower-level model neurons developed space-time
receptive fields similar to those of simple cells in the primary visual cortex while the higher-
level responses spanned longer timescales, mimicking temporal response hierarchies in the
cortex. Additionally, the network’s hierarchical sequence representation exhibited both pre-
dictive and postdictive effects resembling those observed in visual motion processing in
humans (e.g., in the flash-lag illusion). When coupled with an associative memory emulating
the role of the hippocampus, the model allowed episodic memories to be stored and
retrieved, supporting cue-triggered recall of an input sequence similar to activity recall in the
visual cortex. When extended to three hierarchical levels, the model learned progressively
more abstract temporal representations along the hierarchy. Taken together, our results
suggest that cortical processing and learning of sequences can be interpreted as dynamic
predictive coding based on a hierarchical spatiotemporal generative model of the visual
world.

Author summary

The brain is adept at predicting stimuli and events at multiple timescales. How do the neu-
ronal networks in the brain achieve this remarkable capability? We propose that the neo-
cortex employs dynamic predictive coding to learn hierarchical spatiotemporal

PLOS COMPUTATIONAL BIOLOGY



**1. Overall Layout & Structure:**
The primary visual component is a square graphic centered on the page, which functions as an icon or status indicator. Below this icon, there is a horizontal line separator, followed by text indicating access rights.

**2. Visual Components & Symbols:**
*   **Central Icon:** The icon is a square with slightly rounded corners, set against a light gray background. Inside this square is a circular graphic composed of two overlapping elements:
    *   A red, pointed shape resembling a bookmark or flag, positioned centrally.
    *   A blue circular outline surrounding the red shape.
    The overall impression is a stylized notification or update symbol.

**3. Labels, Keys & Legends:**
*   **Text within the Icon:** Directly beneath the central icon, there is text centered in a dark font: "Check for updates".
*   **Text Below the Icon:** Separated by a horizontal line, there is text in capital letters: "OPEN ACCESS".

**4. Data Trends & Details:**
This figure does not contain plots, graphs, or data trends; it is a symbolic indicator.

**5. Contextual Caption Integration:**
No specific contextual caption was provided to integrate with the figure, so the description relies solely on the visual elements present. The icon serves as a general status indicator ("Check for updates"), and the text below confirms the document's accessibility ("OPEN ACCESS").

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
1 / 30

a1111111111
a1111111111
a1111111111
a1111111111
a1111111111

OPEN ACCESS

Citation: Jiang LP, Rao RPN (2024) Dynamic
predictive coding: A model of hierarchical
sequence learning and prediction in the neocortex.
PLoS Comput Biol 20(2): e1011801. https://doi.
org/10.1371/journal.pcbi.1011801

Editor: Jonathan Rubin, University of Pittsburgh,
UNITED STATES

Received: March 5, 2023

Accepted: January 4, 2024

Published: February 8, 2024

Copyright: © 2024 Jiang, Rao. This is an open
access article distributed under the terms of the
Creative Commons Attribution License, which
permits unrestricted use, distribution, and
reproduction in any medium, provided the original
author and source are credited.

Data Availability Statement: Data and code for
reproducing all simulations in the paper are
available at https://github.com/lpjiang97/dynamic-
predictive-coding.

Funding: This work was supported by the National
Institutes of Health (1UF1NS126485-01 to RPNR
as co-PI), National Science Foundation (NSF) EFRI
(2223495 to RPNR as co-PI), Defense Advanced
Research Projects Agency (DARPA) Contract
(HR001120C0021 to RPNR via a subcontract), a
UW + Amazon Science Hub grant, a Weill
Neurohub Investigator grant, a Frameworks grant



Once you provide the image, I will structure my response according to your requirements:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration**


---

## Page 2

representations. Using computer simulations, we show that when exposed to natural vid-
eos, a hierarchical neural network that minimizes prediction errors develops stable and
longer timescale responses at the higher level; lower-level neurons learn space-time recep-
tive fields similar to the receptive fields of primary visual cortical cells. The same network
also exhibits several effects in visual motion processing and supports cue-triggered activity
recall. Our results provide a new framework for understanding the genesis of temporal
response hierarchies and activity recall in the neocortex.

Introduction

The ability to predict future stimuli and event outcomes is critical for perceiving and interact-
ing with a highly dynamic world. At the neural circuit level, predictions could compensate for
neural transmission delays and engage with the world in real-time. At the cognitive level, plan-
ning a sequence of actions to achieve a desired goal relies on predictions of the sensory conse-
quences of motor commands. These abilities are predicated on two requirements: (a) the brain
must infer the dynamics of sensory stimuli to make spatiotemporal predictions based on an
internal model of the world, and (b) the brain’s temporal representations must span different
timescales to support predictions over both short and long horizons.

Many experimental studies have provided evidence for such computations. Predictive rep-
resentations of upcoming stimuli have been found in various open and closed-loop paradigms
where animals developed experience-dependent visual and auditory expectations [1–5]. Other
empirical evidence suggests that cortical representations exhibit a hierarchy of timescales and
an increase in stability from lower-order to higher-order areas across both sensory and cogni-
tive regions [6–9]. We asked the question: could such phenomena be explained by the neocor-
tex learning a spatiotemporal generative model based on a temporal hierarchy of
representations?

Predictive coding provides a unifying framework for understanding perception and predic-
tion in terms of learning hierarchical generative models of the environment [10–14]. Here, we
present dynamic predictive coding (DPC), a new predictive coding model for learning hierar-
chical temporal representations. The central idea of our proposal is that our perceptual system
learns temporally abstracted representations that encode entire sequences rather than single
points at any given time. Specifically, DPC assumes that higher-level model neurons modulate
the transition dynamics of lower-level networks, building on the computational concept of
hypernetworks [15]. Hypernetworks are neural networks that generate the parameters (synap-
tic weights) for another neural network. However, generating an entire set of high-dimen-
sional synaptic weights is not neurally plausible. Instead, DPC models the transition dynamics
at a lower level of a hierarchy using a small set of modulation weights for a group of learned
transition matrices. These weights implement “top-down” gain modulation of the lower-level
synapses [16, 17] and are predicted by the higher level through a feedback network (a hyper-
network) connecting the higher to the lower level. Compared to previous normative models of
video processing that either do not learn the temporal dynamics between images [18–22] or
presume a fixed temporal hierarchy [23, 24] (see Discussion), the DPC model offers a neural
implementation of spatiotemporal prediction that learns the transition dynamics of the input
and adapts its hierarchical temporal representation to the intrinsic timescales of the data.

We tested the DPC model using a two-level neural network trained on natural and artificial
image sequences to minimize spatiotemporal prediction errors. After training, the lower-level
neurons developed space-time receptive fields similar to those found in simple cells in the

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
2 / 30

from the Templeton World Charity Foundation, and
a Cherng Jia and Elizabeth Yun Hwang
Professorship to RPNR. The funders had no role in
study design, data collection and analysis, decision
to publish, or preparation of the manuscript.”



**Please upload the academic PDF figure you would like me to describe.**

Once you provide the image, I will generate a highly detailed, comprehensive, and exhaustive description following all your specified guidelines:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration**

I am ready to act as a senior neuroscientist and technical editor for your figure analysis.

Competing interests: The authors have declared
that no competing interests exist.


---

## Page 3

primary visual cortex (V1) [25]. Neurons in the second level learned to capture input dynamics
on a longer timescale and their responses exhibited greater stability compared to responses in
the first level, similar to the temporal response hierarchies observed in the cortex [6–9]. We
further show that the learned sequence representations in the network can explain both pre-
dictive and postdictive effects seen in visual processing [26–29], reproducing several aspects of
the flash-lag illusion [26, 30, 31]. When linked to an associative memory mimicking the role of
the hippocampus, the network allowed storage of episodic memories and exhibited cue-trig-
gered activity recall after repeated exposure to a fixed input sequence, an effect previously
reported in rodents [1], human V1 [32–34] and monkey V4 [35]. Lastly, when extended to
three levels, the top-level neurons learned to encode the transition dynamics of the second-
level states, which in turn encoded the transition dynamics of the first-level states, thereby
yielding a hierarchical temporal representation of input image sequences. Together, these
results support the hypothesis that the neocortex uses dynamic predictive coding based on a
hierarchical spatiotemporal generative model to learn and interpret input sequences at multi-
ple levels of temporal abstractions. Some of the results presented herein appeared previously in
a conference proceedings [36].

Results
Dynamic predictive coding

The DPC model assumes that spatiotemporal inputs are generated by a hierarchical generative
model (Fig 1a) (see also [37]). We describe here a two-level hierarchical model (see Discussion
for the possibility of extending the model to more levels). The lower level of the model follows
the traditional predictive coding model in generating images using a set of spatial filters U and
a latent state vector rt, which is sparse [38], for each time step t: It = Urt + n where n is zero
mean Gaussian white noise. The temporal dynamics of the state rt is modeled using K learn-
able transition matrices fVkg

K
k¼1 which can be linearly combined using a set of “modulation”
weights given by a K-dimensional vector w. This vector of weights is generated by the higher-
level state vector rh using a function H (Fig 1b), implemented as a neural network (a “hyper-
network” [15]—see “Hypernetworks and neural gain modulation” in S1 Text):

w ¼ HðrhÞ
ð1Þ

V ¼

X
K

k¼1

wkVk:
ð2Þ

Here, wk is the kth component of the vector w. The lower-level state vector at time t + 1 is gen-
erated as rt+1 = ReLU(Vrt) + m where m is zero mean Gaussian white noise. Note that this is
one particular parameterization for top-down modulation of the lower-level transition dynam-
ics, with the hypernetwork formulation allowing other types of parameterizations (see “Hyper-
networks and neural gain modulation” in S1 Text).

The generative model in Fig 1b can be implemented in a hierarchical neural network: the
higher-level state rh, represented by higher-level neurons, generates a top-down modulation w
via a top-down feedback neural network H, and this top-down input w influences the groups
of lower-level neurons representing Vi through gain modulation [16, 17] (see “Hypernetworks
and neural gain modulation” in S1 Text for details). We propose that such a computation
could be implemented by cortical pyramidal neurons receiving top-down modulation via their
apical dendrites (through gain control [17, 39]) and the recurrent state rt (and input prediction
errors) via their basal dendrites, and integrating these to predict the next state (Fig 1c).

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
3 / 30


---

## Page 4

When an input sequence is presented, the model employs a Bayesian filtering approach to
perform online inference on the latent vectors [40] by minimizing a loss function that includes
prediction errors and penalties from prior distributions over the latent variables (see Meth-
ods). Given the model’s estimates ^rt and ^rh at time t, the estimate ^rtþ1 of r at time t + 1 is com-

puted by gradient descent to minimize the sum of the input prediction error kItþ1   U^rtk

2
2 and

the temporal state prediction error krtþ1   ReLUðV^rtÞk

2
2 plus a sparseness penalty. Similarly,
the second level estimates ^rh is updated using the temporal prediction error plus a prior-related
penalty. The model’s parameters are learned by minimizing the same prediction errors across
all time steps and input sequences, further reducing the errors not accounted for by the infer-
ence process above for latent vectors (see Methods).

Hierarchical predictive coding of natural videos

We implemented the DPC model described above using a two-level neural network where
neural responses represent estimates of the latent state vectors and whose synaptic weights rep-
resent the spatial filters and transition parameters. We used K = 5 transition matrices for the
first level (more matrices did not significantly improve performance—see Fig A in S1 Text).
Perception in the DPC network corresponds to estimating the latent vectors by updating neu-
ral responses (through network dynamics) to minimize prediction errors via gradient descent
(see Methods). Updating network parameters to further reduce prediction errors corresponds
to learning (slow changes in synaptic weights through synaptic plasticity).

Fig 1d and 1e illustrate the inference process for both levels of the network. The network
generates top-down and lateral predictions (green) using the current two-level state estimates

Fig 1. Dynamic predictive coding. (a) Generative model for dynamic predictive coding. (b) Parameterization of the model. The higher-
level state modulates the lower-level transition matrices through a top-down network (“hypernetwork”) H. (c) A possible neural
implementation of the generative model using cortical pyramidal neurons. Pyramidal neurons receive the top-down embedding vector
input via synapses at apical dendrites and the current recurrent state vector via basal dendrites, and produce as their output the next state
vector. (d) Schematic depiction of an inference step when the dynamics at the lower level is stable. The higher-level state remains stable
due to minimal prediction errors. (e) Depiction of an inference step when the lower-level dynamics changes. The resulting large prediction
errors drive updates to the higher-level state to account for the new lower-level dynamics.

> Figure caption (from PDF text): Fig 1. Dynamic predictive coding. (a) Generative model for dynamic predictive coding. (b) Parameterization of the model. The higher-
level state modulates the lower-level transition matrices through a top-down network (“hypernetwork”) H. (c) A possible neural
implementation of the generative model using cortical pyramidal neurons. Pyramidal neurons receive the top-down embedding vector
input via synapses at apical dendrites and the current recurrent state vector via basal dendrites, and produce as their output the next state
vector. (d) Schematic depiction of an inference step when the dynamics at the lower level is stable. The higher-level state remains stable
due to minimal prediction errors. (e) Depiction of an inference step when the lower-level dynamics changes. The resulting large prediction
errors drive updates to the higher-level state to account for the new lower-level dynamics.


This figure, labeled "Fig 1. Dynamic predictive coding," is composed of five distinct panels (a through e), illustrating different aspects of a dynamic predictive coding framework, ranging from generative models to neural implementations and inference steps.

---

### Panel (a): Generative Model
*   **Structure:** This panel displays a directed acyclic graph (DAG) structure, representing a generative model.
*   **Nodes:** There are several nodes labeled with time indices: $r_0, r_1, \dots, r_{T-1}$ at the top level, and $I_0, I_1, \dots, I_{T-1}$ at the bottom level.
*   **Connections:** Arrows flow downwards from the top row ($r_t$) to the bottom row ($I_t$). The structure suggests that the state $r_t$ predicts or generates the observation $I_t$.
*   **Annotation:** The panel is labeled: "Input: continuous leftward motion."

### Panel (b): Parameterization of the Model
*   **Structure:** This panel illustrates a hierarchical, recurrent structure involving state vectors and transition matrices.
*   **Nodes:** There are nodes representing higher-level states ($V_1, V_2, V_3, \dots$) and a general state node labeled $r$. There is also a block labeled $\mathcal{H}$ (representing the hypernetwork).
*   **Connections:** Arrows indicate flow. The state $r$ connects to the hypernetwork $\mathcal{H}$. The hypernetwork $\mathcal{H}$ modulates the transition matrices connecting the lower-level states ($V_1, V_2, \dots$) across time steps $t$ to $t+1$.
*   **Flow:** Arrows show transitions between the lower-level states ($V_i \to V_j$) and a general transition flow from $t$ to $t+1$.
*   **Annotation:** The caption notes that the higher-level state modulates the lower-level transition matrices through a top-down network ("hypernetwork") $\mathcal{H}$.

### Panel (c): Neural Implementation
*   **Structure:** This panel depicts a schematic neural circuit, likely representing cortical pyramidal neurons.
*   **Nodes/Elements:** There is a central structure resembling a neuron soma with dendrites branching out.
*   **Inputs:** Two distinct input pathways are shown:
    1.  A top-down pathway labeled with an arrow pointing down, representing the "top-down embedding vector input." This input synapses onto apical dendrites.
    2.  A recurrent pathway labeled with an arrow pointing into the basal dendrites, representing the "current recurrent state vector."
*   **Output:** An arrow exits the neuron structure, representing the "next state vector" output.
*   **Annotation:** The caption specifies that pyramidal neurons receive the top-down input via apical dendrites and the recurrent state via basal dendrites.

### Panel (d): Stable Dynamics Inference Step
*   **Structure:** This panel shows a sequence of time steps ($t$ to $t+1$) illustrating an inference step under stable dynamics.
*   **Components:** It features a block labeled $\mathcal{V}$ (representing the higher-level state) and a sequence of observed data representations ($\hat{r}_t$, $\hat{r}_{t+1}$) alongside corresponding predicted/estimated data (represented by bar graphs).
*   **Dynamics:** The sequence shows the state $\mathcal{V}$ remaining stable. The prediction errors (represented by small, dashed red lines) are minimal.
*   **Data Representation:** Bar graphs represent observations/estimates at time $t$ and $t+1$.
*   **Flow:** Arrows indicate the progression from time $t$ to $t+1$.
*   **Annotation:** The caption describes this as an inference step where the higher-level state remains stable due to minimal prediction errors.

### Panel (e): Changing Dynamics Inference Step
*   **Structure:** This panel mirrors the structure of Panel (d) but illustrates a scenario where the lower-level dynamics change.
*   **Components:** It also features the state block $\mathcal{V}$ and time steps $t$ to $t+1$.
*   **Dynamics:** In contrast to Panel (d), this panel shows a transition where the lower-level dynamics changes. This change results in **large prediction errors** (indicated by prominent, dashed red lines).
*   **State Update:** The large prediction errors drive an update to the higher-level state $\mathcal{V}$ (indicated by a change in the block representation).
*   **Data Representation:** Bar graphs show observations/estimates at time $t$ and $t+1$.
*   **Annotation:** The caption identifies this as an inference step where large prediction errors drive updates to the higher-level state to account for new lower-level dynamics.

---
**Legend:** A legend box is present in the bottom right corner, defining visual elements:
*   **Prediction:** Represented by a solid line/bar.
*   **Estimate:** Represented by a dashed line/bar.
*   **Observation:** Represented by a solid bar graph (in panels d and e).
*   **Error:** Represented by dashed red lines.

https://doi.org/10.1371/journal.pcbi.1011801.g001

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
4 / 30


---

## Page 5

(blue). If the input sequence is predicted well by the top-down-modulated transition matrix V,
the higher-level response rh remains stable due to small prediction errors (Fig 1d). When a
non-smooth transition occurs in the input sequence, the resulting large prediction errors are
sent to the higher level via feedforward connections (red arrows, Fig 1e, driving changes in rh

to predict new dynamics for the lower level.

We trained the network on thousands of natural image sequences extracted from a video
recorded by a person walking on a forest trail (frame size: 16 × 16 pixels, sequence length: 10
frames (*0.35 seconds)). The frames were spatially and temporally whitened to simulate reti-
nal and lateral geniculate nucleus (LGN) processing [38, 41]. The image sequences reserved
for testing did not overlap in space or time with the training sequences. Fig 2a illustrates the
inference process on an example natural image sequence by the network. The first row displays
the ground truth input It for 10 time steps: each frame was shown sequentially to the model.
The next row shows the model’s predictions Urt for each time step t, where rt was predicted
by the previous state estimate ^rt  1: rt ¼ ReLUðV^rt  1Þ. The prediction errors It   Urt are
shown in the third row. The prediction errors were the largest in the first two steps as the
model inferred the spatial features and the transition dynamics from the initial inputs. The
subsequent predictions were more accurate, resulting in minimized prediction errors. Finally,
the last row shows the corrected estimates U^rt after rt has been updated to ^rt through predic-
tion error minimization. Fig 2b shows the lower- (top) and higher-level (middle) neural
responses to the natural video sequence in Fig 2a. The bottom panel of Fig 2b shows the top-
down dynamics modulation generated by the higher level.

We examined the learned spatial receptive fields (RFs) of the model neurons at the first
level and qualitatively compared them with the spatial RFs of simple cells in the primary visual
cortex (V1). A subset of the spatial filters (columns of U) learned by the model from our natu-
ral videos dataset are shown in Fig 2c. These filters resemble oriented Gabor-like edge or bar
detectors, similar to the localized, orientation-selective spatial RFs found in V1 simple cells
[38, 42]. To measure the spatiotemporal receptive fields of the lower-level neurons, we ran a
reverse correlation experiment [43, 44] with a continuous natural video clip ( 47 minutes)
extracted from the same forest trail natural video used for training. This video was not shown
to the model during either training or testing (see Methods). Fig 2d shows the spatiotemporal
receptive fields for four example lower-level model neurons, computed by weighting input
frames from the seven previous time steps It−7, It−6, . . ., It−1 by the response ^rt they caused at
the current time step t (see Methods). The resulting average spatiotemporal receptive fields are
shown as seven-image sequences labeled t −7, t −6, . . ., t −1 (lasting  250 milliseconds in
total). The first column labeled “Spatial” shows the spatial RFs of the example neurons.

To compute the space-time receptive fields (STRFs), we took the spatiotemporal X −Y −T
receptive field cubes and collapsed either the X or Y dimension, depending on which axis had
time-invariant responses. Fig 2e left panel shows the X/Y −T receptive fields of these example
neurons. For comparison, Fig 2e right panel shows the STRFs of simple cells in the primary
visual cortex (V1) of a cat (adapted from DeAngelis et al. [25]).

DeAngelis et al. [25] categorized the receptive fields of simple cells in V1 to be space-time
separable (Fig 2e top row) and inseparable (Fig 2e bottom row). Space-time separable receptive
fields maintain the spatial form of bright/dark-excitatory regions over time but switch their
polarization: the space-time receptive field can thus be obtained by multiplying separate spatial
and temporal receptive fields. Space-time inseparable receptive fields on the other hand exhibit
bright/dark-excitatory regions that shift gradually over time, showing an orientation in the
space-time domain. Neurons with space-time inseparable receptive fields are direction-selec-
tive, responding to motion in only one direction. As seen in Fig 2e left pane, the neurons in
the lower level of our network learned V1-like separable and inseparable STRFs, based on the

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
5 / 30


---

## Page 6

principle of spatiotemporal prediction error minimization. To our knowledge, these results
represent one of the first demonstrations of the emergence of both separable and inseparable
STRFs in a recurrent network model by predictive coding of natural videos presented frame-
by-frame. Previous demonstrations (e.g., [18, 20, 23]) have typically required chunks or all the
frames of a video to be provided as a single input to a network, which is hard to justify biologi-
cally (see Discussion).

Temporal hierarchy through prediction of dynamics

Next, we show that the two-level DPC network learned a hierarchical temporal representation
of input videos. In our formulation of the model, a higher-level state vector predicts the
dynamics of the lower-level states. This implies that the higher-level network neurons will have
stable activation for input sequences with consistent dynamics (Fig 1d). When a change occurs
in input dynamics, we expect the higher-level responses to switch to a different activation pro-
file to minimize prediction errors (Fig 1e). We hypothesize that the different timescales of

Fig 2. Predictive coding of natural videos and learned space-time receptive fields. (a) Inference on an example input image sequence of 10
frames. Top to bottom: Input sequence; model’s prediction of the current input from the previous step (the first step prediction being zero);
prediction error (predicted input subtracted from the actual input); model’s final estimate of the current input after prediction error
minimization. (b) The trained DPC network’s response to the natural image sequence in (a). Each plotted line represents the responses of a
model neuron over 10 time steps. Top: responses of the 20 most active lower-level neurons (some colors are repeated); middle: responses of
seven randomly chosen higher-level neurons; bottom: predicted transition dynamics (each line is the modulation weight for a basis transition
matrix at the lower level). (c) 40 example spatial receptive fields (RFs) learned from natural videos. Each square tile is a column of U reshaped to
a 16 × 16 image. (d) Space-Time RFs (STRFs) of four example lower-level neurons. First column: the spatial RFs of the example neurons. Next
seven columns: the STRFs of the example neurons revealed by reverse correlation mapping. (e) Left panel: space-time plots of the example
neurons in (d). Right panel: space-time plots of the RFs of two simple cells in the primary visual cortex of a cat (adapted from [25]).

> Figure caption (from PDF text): Fig 2. Predictive coding of natural videos and learned space-time receptive fields. (a) Inference on an example input image sequence of 10
frames. Top to bottom: Input sequence; model’s prediction of the current input from the previous step (the first step prediction being zero);
prediction error (predicted input subtracted from the actual input); model’s final estimate of the current input after prediction error
minimization. (b) The trained DPC network’s response to the natural image sequence in (a). Each plotted line represents the responses of a
model neuron over 10 time steps. Top: responses of the 20 most active lower-level neurons (some colors are repeated); middle: responses of
seven randomly chosen higher-level neurons; bottom: predicted transition dynamics (each line is the modulation weight for a basis transition
matrix at the lower level). (c) 40 example spatial receptive fields (RFs) learned from natural videos. Each square tile is a column of U reshaped to
a 16 × 16 image. (d) Space-Time RFs (STRFs) of four example lower-level neurons. First column: the spatial RFs of the example neurons. Next
seven columns: the STRFs of the example neurons revealed by reverse correlation mapping. (e) Left panel: space-time plots of the example
neurons in (d). Right panel: space-time plots of the RFs of two simple cells in the primary visual cortex of a cat (adapted from [25]).


This figure, Figure 2, is divided into five distinct panels (a, b, c, d, and e), illustrating the process of predictive coding applied to natural video sequences and visualizing the learned receptive fields.

### Panel (a): Inference on an Example Input Image Sequence
Panel (a) displays a sequence of 10 frames, showing the results of the predictive coding inference process. The layout is a vertical stack of four rows, each showing 10 sequential frames across the horizontal axis (Time: 0 through 9).

*   **Row 1: Input $I_t$**: This row shows the actual input image sequence ($I_t$).
*   **Row 2: Prediction $\hat{U}_t$**: This row shows the model's prediction ($\hat{U}_t$) of the current input based on previous steps. The caption notes that the first step prediction is zero.
*   **Row 3: Prediction Error $I_t - \hat{U}_t$**: This row displays the prediction error, calculated as the actual input minus the model's prediction.
*   **Row 4: After Correction $\tilde{U}_t$**: This row shows the model's final estimate ($\tilde{U}_t$) of the current input after minimizing the prediction error.

### Panel (b): DPC Network Response
Panel (b) consists of three stacked plots, illustrating the trained Deep Predictive Coding (DPC) network's response to the sequence shown in Panel (a). The x-axis for all three plots is labeled "Time" ranging from 0 to 8. The y-axis for all three plots is labeled "Normalized Response," ranging from 0.0 to 1.0.

*   **Top Plot**: Shows the responses of the "20 most active lower-level neurons." Multiple colored lines are plotted, representing individual neuron responses over time.
*   **Middle Plot**: Shows the responses of "seven randomly chosen higher-level neurons." Again, multiple colored lines track these specific neuron activations over time.
*   **Bottom Plot**: Shows the "predicted transition dynamics." Each line represents the modulation weight for a basis transition matrix at the lower level.

### Panel (c): Spatial Receptive Fields (RFs)
Panel (c) displays 40 example spatial receptive fields (RFs). The layout is a grid structure.
*   The overall panel shows 5 rows and 8 columns of small image tiles.
*   Each tile represents a column of $U$ reshaped into a $16 \times 16$ image, as stated in the caption.
*   The rows are labeled with identifiers: \#13, \#29, \#86, and \#19 (though the grid structure suggests more than four distinct groups might be present).

### Panel (d): Space-Time Receptive Fields (STRFs)
Panel (d) presents the Space-Time Receptive Fields (STRFs) for four example lower-level neurons. The layout is organized into rows corresponding to different neuron identifiers (\#13, \#29, \#86, \#19).
*   Each row contains multiple image tiles representing the receptive fields.
*   The first column of tiles in each row shows the **spatial RFs** of the example neurons.
*   The subsequent seven columns show the **STRFs** revealed by reverse correlation mapping, indicating how these neurons respond across time.

### Panel (e): Space-Time Plots Comparison
Panel (e) is divided into two side-by-side sections, comparing different types of space-time plots.

*   **Left Panel (X - T)**: This section shows the space-time plots of the example neurons detailed in Panel (d). The plot axes are labeled $X$ and $T$.
*   **Right Panel (Separable vs. Inseparable)**: This section compares the space-time plots of two simple cells from the primary visual cortex of a cat (adapted from [25]).
    *   The top plot is labeled "Separable" and shows a characteristic pattern.
    *   The bottom plot is labeled "Inseparable" and shows a different, more complex pattern.

https://doi.org/10.1371/journal.pcbi.1011801.g002

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
6 / 30


---

## Page 7

neural responses observed in the cortex [6–9] could be an emergent property of the cortex
learning a similar hierarchical generative model.

We tested this hypothesis in our DPC network trained on natural videos. As seen in the
inference example in Fig 2b, the lower-level responses change rapidly as the stimulus moves
(top panel). The higher-level responses (middle panel) and the predicted transition dynamics
(right panel) were more stable after the initial adaptation to the motion. Since the stimulus
continued to follow roughly the same dynamics (leftward motion) after the first two steps, the
transition matrix predicted by the higher-level neurons continued to be accurate for the rest of
the steps, leading to small prediction errors and few changes in the responses. Note that we did
not enforce a longer time constant or smoothness constraint for rh during inference—the lon-
ger timescale and more stable responses are entirely a result of the higher-level neurons learn-
ing to predict the lower-level dynamics under the proposed generative model.

To quantify this learned hierarchical temporal representation, we computed the autocorre-
lation of the lower- and higher-level responses to unseen natural videos and fitted an exponen-
tial decay function (see Methods). As Fig 3a shows, the autocorrelation of the higher-level
responses rh is greater than that of the lower-level response r and has a slower decay rate (expo-
nential time constant for rh: 5.49 steps; for r: 2.18 steps). To factor out the effect of the natural
video statistics, we computed the same autocorrelation using Gaussian white noise sequences.
We found that the hierarchy of timescales still exists (rh: 3.11 steps; r: 0.18 steps). Fig 3b shows
the autocorrelation of nonhuman primate neural responses from the medial-temporal (MT)
area in the visual cortex (assumed to be lower in the processing stream) and lateral prefrontal
cortex (LPFC) (assumed to be higher) for time periods preceding a motion task [6]. These neu-
ral responses show a difference in timescales qualitatively similar to the different response
timescales in our hierarchical DPC network.

To further understand the model’s ability to learn hierarchical temporal representations, we
trained a DPC network on the Moving MNIST dataset [45]. Each image sequence in this data-
set contains ten 18 × 18 pixel frames showing a single example of a handwritten digit (chosen
from the original MNIST dataset) moving in a particular direction. The digit’s motion is lim-
ited to up, down, left, or right directions with a fixed speed. Fig 3c illustrates the trained net-
work’s inference process on an example image sequence. Similar to the responses to the
natural video sequence, the lower-level responses displayed fast changes while the higher-level
responses spanned a longer timescale and showed greater stability (Fig 3d). Note that at time
t = 4 and t = 8, the input dynamics changed as the digit “bounced” against the boundaries and
started to move in the opposite motion (Fig 3c red dashed box). The higher-level neurons’ pre-
dictions resulted in large prediction errors at those times (Fig 3c third row). The prediction
errors caused notable changes in the higher-level responses rh (Fig 3d red dashed boxes). For
the rest of the steps, rh remained stable and generated accurate predictions of the stable
dynamics.

Lastly, we confirmed that lower-level transition dynamics are indeed encoded in the
higher-level responses. We performed principal component analysis (PCA) on the higher-level
responses rh for the Moving MNIST sequences in the test set. Fig 3e visualizes these responses
in the space of their first two principal components (PCs), colored by either the motion direc-
tion (left) or digit identities (right). The responses clearly formed clusters according to input
motion direction but not digit identities. We then trained a support vector machine with radial
basis function (RBF) kernel [46] to map r and rh to motion directions and digit identities (Fig
3f). Using the higher-level responses, the classifier yielded 73.9% 10-fold cross-validated classi-
fication accuracy on the four motion directions (chance accuracy: 26.0%, computed as the
number of majority labels in the test set divided by the total number of labels). Using the
lower-level responses resulted in significantly less classification accuracy for motion direction

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
7 / 30


---

## Page 8

(46.5%, p  0.001, t-test). In contrast, decoding accuracy for digit identity was significantly
higher using the lower-level responses (76.1%) compared to using the higher-level responses
(20.9%, p  0.001, t-test). These results show that due to the structure of its generative model,
the DPC network learned to disentangle to a significant extent the motion information in an
input video from image content (here, digit identity), yielding a factored representation of
input image sequences.

Predictive and postdictive effects in visual motion processing

The ability of the DPC model to encode entire sequences at the higher level (cf. the “timeline”
model of perception [29]) leads to new normative and computational interpretations of visual
motion phenomena such as the flash-lag illusion [26, 30, 31], explaining both predictive and

Fig 3. Hierarchical temporal representation with different timescales. (a) Autocorrelation of the lower- and higher-
level responses in the trained network with natural videos. Shaded area denotes ±1 standard deviation. Dotted lines
show fitted exponential decay functions. Left: response recorded during natural video stimuli; right: white noise stimuli.
(b) Autocorrelation of the neural responses recorded from MT and LPFC of monkeys. Adapted from Murray et al. [6]
(c) Inference for an example Moving MNIST sequence in a trained network. The red dashed boxes mark the time steps
when the dynamics of the input changed. (d) The network’s responses to the input Moving MNIST sequence in (c).
Note the changes in the higher-level responses after the input dynamics changed (red dashed boxes); this gradient-based
change helps to minimize prediction errors. (e) Higher-level responses to the Moving MNIST sequences visualized in
the 2D space of the first two principal components. Left: responses colored according to motion direction; right:
responses colored according to digit identities. (f) Comparison of decoding performance for motion direction versus
digit identity using lower- and higher-level neural responses. Error bars: ±1 standard deviation from 10-fold cross
validation. Orange: chance accuracies.

> Figure caption (from PDF text): Fig 3. Hierarchical temporal representation with different timescales. (a) Autocorrelation of the lower- and higher-
level responses in the trained network with natural videos. Shaded area denotes ±1 standard deviation. Dotted lines
show fitted exponential decay functions. Left: response recorded during natural video stimuli; right: white noise stimuli.
(b) Autocorrelation of the neural responses recorded from MT and LPFC of monkeys. Adapted from Murray et al. [6]
(c) Inference for an example Moving MNIST sequence in a trained network. The red dashed boxes mark the time steps
when the dynamics of the input changed. (d) The network’s responses to the input Moving MNIST sequence in (c).
Note the changes in the higher-level responses after the input dynamics changed (red dashed boxes); this gradient-based
change helps to minimize prediction errors. (e) Higher-level responses to the Moving MNIST sequences visualized in
the 2D space of the first two principal components. Left: responses colored according to motion direction; right:
responses colored according to digit identities. (f) Comparison of decoding performance for motion direction versus
digit identity using lower- and higher-level neural responses. Error bars: ±1 standard deviation from 10-fold cross
validation. Orange: chance accuracies.


This figure, titled "Hierarchical temporal representation with different timescales," is composed of six distinct panels (a through f) presenting various types of data visualizations, including autocorrelation plots, sequence representations, and principal component analyses.

### Panel (a): Autocorrelation Plots
Panel (a) consists of two side-by-side line graphs illustrating autocorrelation.

*   **Left Plot (Natural videos):** This plot shows the autocorrelation decay for responses recorded during natural video stimuli.
    *   The x-axis is labeled "Lag (step)" ranging from 0 to 9.
    *   The y-axis is labeled "Autocorrelation" ranging from 0.00 to 1.00.
    *   Two curves are present: one labeled "r: 2.18 steps" and another labeled "r$^b$: 5.49 steps." Both curves show a decay pattern, with the shaded area indicating $\pm 1$ standard deviation. Dotted lines are shown fitting exponential decay functions to the curves.
*   **Right Plot (White noise):** This plot shows the autocorrelation decay for responses recorded during white noise stimuli.
    *   The x-axis is labeled "Lag (step)" ranging from 0 to 9.
    *   The y-axis is labeled "Autocorrelation" ranging from 0.00 to 1.00.
    *   Two curves are present: one labeled "r: 0.18 steps" and another labeled "r$^b$: 3.11 steps." Similar to the left plot, these curves show decay and are accompanied by a shaded area representing $\pm 1$ standard deviation.

### Panel (b): Neural Response Autocorrelation
Panel (b) is a line plot comparing autocorrelation values from specific neural recordings.

*   The y-axis is labeled "Autocorrelation" ranging from 0.0 to 0.25.
*   The x-axis is labeled "ms" (milliseconds), ranging from 0 to 100 ms.
*   Two distinct lines are plotted: one labeled "MT: 77 ms" (in red) and another labeled "LPFC: 127 ms" (in green). Both lines show a decreasing trend as the time lag increases.

### Panel (c): Inference for Moving MNIST Sequence
Panel (c) displays a sequence of image frames representing the inference process.

*   The panel is structured as a vertical stack of four rows, each showing a sequence of 10 frames (Time steps 0 through 9).
*   **Row 1: Input $I$**: Shows the input sequence, which appears to be a moving digit pattern.
*   **Row 2: Prediction $U_{f_t}$**: Shows the predicted state sequence.
*   **Row 3: Prediction Error $I_t - U_{f_t}$**: Shows the difference between input and prediction.
*   **Row 4: After Correction $U_{f_t}$**: Shows the corrected state sequence.
*   Red dashed boxes are overlaid on frames 3 through 5 in the Input ($I$), Prediction ($U_{f_t}$), and Prediction Error ($I_t - U_{f_t}$) rows, indicating time steps where the input dynamics changed.

### Panel (d): Network Responses to Moving MNIST
Panel (d) shows the network's responses corresponding to the sequence in Panel (c). This panel is divided into three sub-plots stacked vertically.

*   **Top Sub-plot:** Shows a sequence of responses (likely activations) over time, corresponding to the input sequence.
*   **Middle Sub-plot:** Shows a second set of responses over time, also corresponding to the input sequence.
*   **Bottom Sub-plot:** Shows a third set of responses over time, also corresponding to the input sequence.
*   In all three sub-plots, changes in the responses are highlighted around the time steps marked by red dashed boxes (corresponding to the input dynamics changes in Panel c).

### Panel (e): Principal Component Analysis Visualization
Panel (e) presents two scatter plots visualizing higher-level responses in a 2D principal component space.

*   **Left Plot:**
    *   The x-axis is labeled "PC1" and the y-axis is labeled "PC2".
    *   The points are colored according to motion direction (indicated by a legend).
    *   The legend shows colors corresponding to directions: Up, Left, Down, and Right.
*   **Right Plot:**
    *   The x-axis is labeled "PC1" and the y-axis is labeled "PC2".
    *   The points are colored according to digit identities (indicated by a legend).
    *   The legend shows colors corresponding to digits 0 through 9.

### Panel (f): Decoding Performance Comparison
Panel (f) is a bar chart comparing decoding accuracy.

*   The x-axis has two main categories: "Motion" and "Digit."
*   For each category, there are two bars: one representing decoding using lower-level responses and another using higher-level responses.
*   The y-axis is labeled "Decoding Accuracy" ranging from 0.0 to 0.6.
*   Error bars are present on top of each bar, representing $\pm 1$ standard deviation from a 10-fold cross-validation.
*   A separate label, "Chance," is shown above the bars for comparison, indicating chance accuracy.

https://doi.org/10.1371/journal.pcbi.1011801.g003

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
8 / 30


---

## Page 9

postdictive effects [27, 29]. The flash-lag illusion refers to the phenomenon that a flashed,
intermittent object is perceived to be “lagged” behind the percept of a continuously moving
object even though the physical locations of the two objects are aligned or the same [30, 31].
Though this illusion is commonly attributed to the predictive nature of the perceptual system
[30], Eagleman and Sejnowski [26] proposed a postdictive mechanism based on psychophysi-
cal results that the motion of the moving object after the flash can change the percept of events
at the time of the flash. The potential interplay between prediction and postdiction in shaping
perception was also studied by Hogendoorn et al. [27, 29]. The authors designed an interfer-
ence paradigm with different reaction-speed tasks and showed that when the trajectory of the
object unexpectedly reverses, predictive effects (extrapolation) are observed at short latencies
but postdictive effects (interpolation) are observed at longer latencies (Fig 4i and 4j).

We propose that prediction error minimization with a hierarchical temporal representa-
tion, as in the DPC model, provides a natural explanation for these predictive and postdictive
effects. In a DPC network, the higher-level state rh predicts entire sequences of lower-level
states following the same dynamics (Fig 3). When the dynamics of observations change (e.g.,
motion reversal), the higher-level state is updated to minimize prediction errors, resulting in a
revised state that represents the motion-reversed sequence spanning both past and future
inputs. This process corresponds to postdiction in visual processing [28]. For the flash-lag
experiment, we predict that the higher-level neurons of a trained DPC network will form a
static sequence percept when presented with a flashed object and a directional sequence per-
cept for a moving object, causing perceived lags between the two objects as observed in the
flash-lag illusion [30].

We first test these predictions of the DPC model on the experimental conditions used by
[26]. In their experiment, the stimuli consisted of a flashed disk and a ring moving in a circle.
Before the flash, the ring could have an initial trajectory (Fig 4a top) or no initial trajectory
(Fig 4a bottom). After the flash, the ring could continue moving on its initial trajectory (“con-
tinuous”), stop moving (“stopped”), or move on the reversed trajectory (“reversed”). A flash
appeared in a seven-degree range that extended above and below the ring on its trajectory. The
participants then indicated whether a flashed white disk occurred above or below the center of
the moving ring. Positive displacements denoted lags along the initial trajectory of the ring,
while negative displacements denoted the reversed direction.

To simulate these testing conditions, we used the Moving MNIST test set and extracted 134
test sequences with consistent leftward or rightward motion. For each of these 134 sequences,
we simulated the two test conditions used by [26] (with or without initial trajectory): the
higher-level state ^rh was either inferred from the first three steps (t = 0, 1, 2) of the input
sequence, or initialized to the zero vector (Fig 4b left). For each of these two test conditions,
we simulated the four test cases used in [26] regarding the motion of the moving object at the
time of the flash (Fig 4b right). Note that flashed stimuli correspond to the “no initial trajec-
tory, terminate” condition. We computed the location of a digit as the center of mass of pixel
values in the 2D image; the perceived location at time t was defined similarly based on the pre-
dicted image at time t. As Fig 4e shows, the perceived location of a flashed object at t = 3
strongly overlapped with the physical flashed location at t = 2, showing that the prediction
errors drove the higher-level state estimates to predict no change in object location for the
flashed object. Fig 4f shows the perceived displacement between the moving object (with initial
trajectories) and the flashed object, computed as the difference in perceived locations at t = 3
between the moving object and the flashed object. Positive displacements followed the original
trajectory direction and negative displacements followed the reversed direction. The perceived
displacements in the model were significantly different in the three test conditions (Fig 4f left
panel, p  0.001, one-way ANOVA test) and were similar to the psychophysical results

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
9 / 30


---

## Page 10

reported by Eagleman & Sejnowski (Fig 4c). Fig 4g confirms that the initial trajectories of the
moving object had no effects on the model’s flash-lag illusion, consistent with the reported
results (Fig 4d) [26]. These results validate the explanation provided by the DPC model on the
flash-lag effect: for a hierarchical generative model with representations of sequences, a flashed
or stopped/terminated moving object leads to inference of a static object sequence (Fig 4e),

Fig 4. Flash-lag illusion and object representations in apparent motion. (a) The flash-lag test conditions used by [26].
The moving ring could have an initial trajectory (top) or no trajectory (bottom). At the time of the flash (bright disk), the
ring could move along the initial trajectory, stop, or reverse its trajectory. Adapted from [26]. (b) Two test conditions
(left) regarding initial trajectories of the moving object (a digit) in the flash-lag experiment with the model, and four test
conditions (right) for the moving object. The flashed object was shown at time t and turned off at time t + 1 (same as the
“Terminate” condition). (c & d) Psychophysical estimates for human subjects reported by [26] when the moving object
had initial trajectories (c) or no initial trajectory (d). (e) Perceived location of the flashed object in the DPC model at
time t + 1. The error bar indicates ±1 standard deviation (measured across presentations of different digits). (f) Perceived
displacement between the moving object (with initial trajectories) and the flashed object in the DPC model for the four
test conditions. (g) Same as (f) but with no initial trajectory for the moving object. (h) Illustration of the prediction-
error-driven dynamics of the perception of the moving object in the model when the trajectory reversed at time t + 1.
Red ellipsis between panels denotes the prediction error minimization process. (i) Interference pattern during human
apparent motion perception with continuous motion (left) and reversed motion (right) at short latency (fast detection
task). Brighter color denotes more interference. Dashed arrows represent object motion direction. Adapted from [29]. (j)
Same as (i) but at long latency (slow discrimination task) [29]. (k) Perceived location of the moving object in the DPC
model at time t + 1 probed at short versus long latency during prediction error minimization. Positive values denote
distance along the original trajectory. Negative values denote distance along the reversed trajectory. Short and long
latency correspond to “Early percept” and “Late percept” respectively in part (h). (l) Perceived location of the digit at all
latencies during the prediction error minimization process in part (h).

> Figure caption (from PDF text): Fig 4. Flash-lag illusion and object representations in apparent motion. (a) The flash-lag test conditions used by [26].
The moving ring could have an initial trajectory (top) or no trajectory (bottom). At the time of the flash (bright disk), the
ring could move along the initial trajectory, stop, or reverse its trajectory. Adapted from [26]. (b) Two test conditions
(left) regarding initial trajectories of the moving object (a digit) in the flash-lag experiment with the model, and four test
conditions (right) for the moving object. The flashed object was shown at time t and turned off at time t + 1 (same as the
“Terminate” condition). (c & d) Psychophysical estimates for human subjects reported by [26] when the moving object
had initial trajectories (c) or no initial trajectory (d). (e) Perceived location of the flashed object in the DPC model at
time t + 1. The error bar indicates ±1 standard deviation (measured across presentations of different digits). (f) Perceived
displacement between the moving object (with initial trajectories) and the flashed object in the DPC model for the four
test conditions. (g) Same as (f) but with no initial trajectory for the moving object. (h) Illustration of the prediction-
error-driven dynamics of the perception of the moving object in the model when the trajectory reversed at time t + 1.
Red ellipsis between panels denotes the prediction error minimization process. (i) Interference pattern during human
apparent motion perception with continuous motion (left) and reversed motion (right) at short latency (fast detection
task). Brighter color denotes more interference. Dashed arrows represent object motion direction. Adapted from [29]. (j)
Same as (i) but at long latency (slow discrimination task) [29]. (k) Perceived location of the moving object in the DPC
model at time t + 1 probed at short versus long latency during prediction error minimization. Positive values denote
distance along the original trajectory. Negative values denote distance along the reversed trajectory. Short and long
latency correspond to “Early percept” and “Late percept” respectively in part (h). (l) Perceived location of the digit at all
latencies during the prediction error minimization process in part (h).


### Overall Layout & Structure
The figure is organized into 12 distinct panels, labeled (a) through (l), arranged in a grid-like fashion across multiple rows. The panels transition from schematic representations of experimental conditions (a, b), to psychophysical results (c, d), model predictions for location and displacement (e-g), dynamic process illustrations (h, k, l), and finally interference pattern visualizations (i, j).

### Detailed Panel Descriptions

**Panels (a) and (b): Experimental Conditions Schematics**
*   **Panel (a):** Shows two scenarios for a moving ring. The top row illustrates the condition "With initial trajectories," showing three states: continuous motion, stopped state, and reversed trajectory. The bottom row illustrates "No initial trajectories," showing the same three states (continuous, stopped, reversed) but without prior trajectory information.
*   **Panel (b):** Presents a flowchart illustrating test conditions involving an initial trajectory and the flash event.
    *   The left side shows two conditions related to "initial trajectories of the moving object (a digit)" in the flash-lag experiment with a model.
    *   The right side shows four test conditions for the moving object, labeled: "Continuous," "Stopped," "Reversal," and "Terminate."
    *   The flow indicates that the flashed object is shown at time $t$ and turned off at time $t+1$.

**Panels (c) and (d): Psychophysical Estimates**
*   These panels display bar graphs representing psychophysical estimates from human subjects.
    *   **Panel (c):** Titled "Psychophysical estimates for human subjects reported by [26] when the moving object had initial trajectories." The y-axis is "Perceived Displacement (deg)," and the x-axis shows categories: "Continuous," "Stopped," and "Reversal."
    *   **Panel (d):** Titled "Psychophysical estimates for human subjects reported by [26] when the moving object had no initial trajectory." It mirrors Panel (c) in structure, with "Perceived Displacement (deg)" on the y-axis and categories "Continuous," "Stopped," and "Reversal" on the x-axis.

**Panels (e), (f), and (g): DPC Model Predictions (Location & Displacement)**
*   **Panel (e):** Shows the "Perceived location of the flashed object in the DPC model at time $t+1$." It features a plot where the y-axis is "Perceived location (pixel)" and the x-axis represents different conditions. An error bar indicates $\pm 1$ standard deviation.
*   **Panel (f):** Shows the "Perceived displacement between the moving object (with initial trajectories) and the flashed object in the DPC model for the four test conditions." The y-axis is "Perceived displacement (pixel)," and the x-axis lists the four conditions from Panel (b) right side: "Continuous," "Stopped," "Reversal," and "Terminate."
*   **Panel (g):** Similar to Panel (f), it shows the "Perceived displacement between the moving object... but with no initial trajectory for the moving object." It uses the same axes as Panel (f).

**Panels (h), (k), and (l): Dynamic Model Illustration**
*   **Panel (h):** An illustration of the "prediction-error-driven dynamics." It shows a sequence of states:
    *   **Left side:** "Previous step ($t=2$)" leading to a state at time $t$.
    *   **Center:** A transition involving the flash event, showing "Perceived" and "Input." An arrow labeled with a red ellipsis indicates the prediction error minimization process.
    *   **Right side:** The state at time $t+1$, labeled "Perceived."
    *   The diagram uses colored blocks (5, 6) to represent states or percepts.
*   **Panel (k):** A plot showing the "Perceived location of the moving object in the DPC model at time $t+1$ probed at short versus long latency."
    *   The y-axis is "Perceived Location (pixel)."
    *   The x-axis shows two conditions: "Revised Trajectory" and "Original Trajectory."
    *   A legend distinguishes between "short latency" (blue) and "long latency" (green). Positive values denote distance along the original trajectory, and negative values denote distance along the reversed trajectory.
*   **Panel (l):** Shows "Perceived location of the digit at all latencies during the prediction error minimization process in part (h)." This is a plot showing location across different latencies.

**Panels (i) and (j): Interference Patterns**
*   These panels illustrate interference patterns observed in human perception.
    *   **Panel (i):** Shows the "Interference pattern during human apparent motion perception with continuous motion (left) and reversed motion (right) at short latency (fast detection task)." Brighter color indicates more interference, and dashed arrows indicate motion direction.
    *   **Panel (j):** Shows the same phenomenon but at "long latency (slow discrimination task)."

### Summary of Key Elements
The figure integrates experimental setup diagrams, quantitative psychophysical data (displacement in degrees), and computational model outputs (location/displacement in pixels) to explain the mechanisms underlying apparent motion perception, particularly focusing on how prior trajectory information influences perception when a flash event occurs.

https://doi.org/10.1371/journal.pcbi.1011801.g004

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
10 / 30


---

## Page 11

while continuous or reversed motion leads to inference of a moving object sequence, resulting
in the perceived lags along the corresponding directions (Fig 4f).

One aspect of motion perception the previous results do not illustrate is the interplay
between postdiction and prediction. Hogendoorn et al. investigated this effect in an experi-
ment on apparent motion perception [27]. Participants were instructed to report the detection
of a visual cue (short latency task) or differentiate between two visual cues (long latency task)
during apparent motion. These visual cues could either be along the apparent motion trajec-
tory or the reversed trajectory. The authors found that upon reversing the apparent motion
trajectory, predictive effects dominated perception at short latency (detection task, Fig 4i),
with the most interference (measured in terms of the participants’ reaction times) along the
original motion trajectory. At longer latency (differentiation task, Fig 4j), most interference
was along the reversed trajectories, indicating that postdictive effects dominated perception.

We hypothesize that the prediction error minimization process of DPC could explain this
interplay between prediction and postdiction, as illustrated by Fig 4h which depicts the gradi-
ent-descent-based optimization process of Fig 1e (and Eq 18). Early percepts of the model are
dominated by the spatiotemporal prediction using the optimal estimates from the previous
step (Fig 4h left). When a motion reversal occurs, feedforward prediction errors gradually cor-
rect the second-level state (Fig 4h middle) until convergence (Fig 4h right). Therefore, late per-
cepts in the model correspond to error-corrected spatiotemporal predictions. Note that due to
the discrete temporal nature of the DPC model (unit time steps), this process is considered to
happen “at” one particular time step (e.g., early versus late percept “at” t = 3 in Fig 4h).

To test this hypothesis, we used the same trained DPC network and probed its percept of
the moving object at the time of reversal under the “with initial trajectory, reversal” condition
(Fig 4b). At short latency (10% of steps into prediction error correction, Fig 4h early percept),
the perceived locations for the moving object in most test sequences were along the original
trajectory, as denoted by positive displacements compared to the final step before reversal
(t = 2) (Fig 4k blue)). At longer latency (90%, Fig 4h late percept), the moving object’s per-
ceived locations were flipped and along the reversed trajectory (negative displacements; Fig 4k
green, p  0.001, t-test). This is consistent with psychophysical findings [27, 29] that when the
motion of the object unexpectedly reversed, prediction effects were observed at short latency
( 350 ms, Fig 4i right panel, bright color denotes locations of interference due to prediction)
while postdictive effects were observed at longer latency ( 620 ms, Fig 4j right panel, bright
color denotes locations of interference due to postdiction). Fig 4l plots the moving object’s per-
ceived location in our model throughout the error correction process: the perceived location
varies smoothly from being along the original direction initially to along the reversed direction
at greater latencies. These results make a testable prediction: if probed at an intermediate level
of latency (between 350 ms and 620 ms), the maximal interference should overlap with the
object’s location at the time of reversal (i.e., at the black dots in Fig 4i and 4j), as suggested by
Fig 4l.

Cue-triggered recall and episodic memory

A number of experiments in rodents have shown that the primary visual cortex (V1) encodes
predictive representations of upcoming stimuli [1–4, 47]. In one of the first such studies, Xu
et al. [1] demonstrated that after exposing rats repeatedly to the same moving dot visual
sequence (Fig 5a), displaying only the starting dot stimulus triggered sequential firing in V1
neurons in the same order as when displaying the complete sequence (Fig 5a). Similar effects
have been reported in monkey [35] and human [32–34, 48] visual cortical areas as well.

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
11 / 30


---

## Page 12

The generative model of DPC provides a highly efficient computational basis for episodic
memories and sequence prediction. DPC assumes sequences are generated by a factorized
representation: a single (lower-level) representation of the content (“what”) provided at the
first step and a single (higher-level) representation of dynamics (motion or “where”). These
two representations are inferred during sequence perception as the explanations (or causes) of
a given input sequence.

It is known that factored information from the visual cortex makes its way, via the medial
and lateral entorhinal cortices, to the hippocampus [50]. The hippocampus has been impli-
cated both in the formation of episodic memories [51–53] and in mediating activity recall in
the neocortex [54–57] through its outputs to the entorhinal cortex, which in turn conveys this
information to downstream areas via feedback connections. Because the DPC model encodes
an entire sequence in terms of a single dynamics vector rh (along with the content r0 at the first
step), it suggests a simple mechanism for storing sequential experiences as episodic memories,
namely, storing the vector rh (along with r0) in an associative memory, mimicking the role of
the hippocampus.

To test this hypothesis, we augmented the DPC model with an associative memory that
uses a vector m to bind the content vector r0 with the dynamics of the sequence rh, thereby
encoding an episodic memory: the new generative model is shown in Fig 5b. Given the initial
cue r0 (inferred from the first image frame in the sequence), the associative memory

Fig 5. Cue-triggered activity recall in the DPC model. (a) The experimental setup of Xu et al. (adapted from [1]). A
bright dot stimulus moved from START to END repeatedly during conditioning. Activities of neurons whose receptive
fields (colored ellipses) were along the dot’s trajectory were recorded. (b) Generative model combining an associative
memory and DPC. The red part denotes the augmented memory component that binds the initial content vector r0
and the dynamics vector rh to encode an episodic memory. (c) Depiction of the memory encoding process. The
presynaptic memory activity and postsynaptic prediction error jointly shape the memory weights G. (d) Depiction of
the recall process. Prediction error on the partial observation ^r0 drives the convergence of the memory estimates ~m
and recalls the higher-level dynamics vector rh as a top-down prediction. The red dotted box depicts the prediction
error between the missing observations for rh and the prediction rh; this error is ignored during recall, implementing a
form of robust predictive coding [49]. (e) The image sequence used to simulate conditioning and testing for our
memory-augmented DPC network. (f) Responses of the lower-level neurons of the network. Colored lines represent
the five most active lower-level neurons at each step. Left to right: neural responses during conditioning, testing the
network with a single start frame, middle frame, and end frame. (g, h) Normalized pairwise cross correlation of (g)
primary visual cortex neurons (adapted from [1]) and (h) the lower-level model neurons. Top: during conditioning;
middle two: testing with the starting stimulus, before and after conditioning; bottom: the differences between cross
correlations, “After” minus “Before” conditioning.

> Figure caption (from PDF text): Fig 5. Cue-triggered activity recall in the DPC model. (a) The experimental setup of Xu et al. (adapted from [1]). A
bright dot stimulus moved from START to END repeatedly during conditioning. Activities of neurons whose receptive
fields (colored ellipses) were along the dot’s trajectory were recorded. (b) Generative model combining an associative
memory and DPC. The red part denotes the augmented memory component that binds the initial content vector r0
and the dynamics vector rh to encode an episodic memory. (c) Depiction of the memory encoding process. The
presynaptic memory activity and postsynaptic prediction error jointly shape the memory weights G. (d) Depiction of
the recall process. Prediction error on the partial observation ^r0 drives the convergence of the memory estimates ~m
and recalls the higher-level dynamics vector rh as a top-down prediction. The red dotted box depicts the prediction
error between the missing observations for rh and the prediction rh; this error is ignored during recall, implementing a
form of robust predictive coding [49]. (e) The image sequence used to simulate conditioning and testing for our
memory-augmented DPC network. (f) Responses of the lower-level neurons of the network. Colored lines represent
the five most active lower-level neurons at each step. Left to right: neural responses during conditioning, testing the
network with a single start frame, middle frame, and end frame. (g, h) Normalized pairwise cross correlation of (g)
primary visual cortex neurons (adapted from [1]) and (h) the lower-level model neurons. Top: during conditioning;
middle two: testing with the starting stimulus, before and after conditioning; bottom: the differences between cross
correlations, “After” minus “Before” conditioning.


### Overall Layout & Structure
The figure is organized into eight distinct panels: (a) through (h). Panels (a) through (d) illustrate the theoretical model components, while panels (e) through (h) present experimental data and simulations. The layout transitions from schematic diagrams to image sequences, and finally to correlation heatmaps/plots.

### Panel Descriptions

**Panel (a): Experimental Setup Schematic**
This panel shows a schematic representation of the experimental setup. A bright dot stimulus is depicted moving along a trajectory from a labeled **START** point to an **END** point. The trajectory is shown as a curved path, and along this path, several colored ellipses are positioned, representing the receptive fields of recorded neurons.

**Panel (b): Generative Model Schematic**
This panel illustrates the generative model structure, combining an associative memory and DPC. It features nodes labeled $r_0$ (initial content vector) and $r_h$ (dynamics vector). An arrow points from the initial state to a sequence of states, indicated by $r_0 \rightarrow r_1 \rightarrow \dots$. A red-shaded region is highlighted, labeled as the "augmented memory component," which binds $r_0$ and $r_h$ to encode an episodic memory.

**Panel (c): Memory Encoding Process Diagram**
This panel depicts the encoding process. It shows a flow involving $\hat{m}$ (likely representing memory state) and $G$ (memory weights). An arrow points from a presynaptic activity representation ($\text{[}r_0; \hat{r}^h\text{]}$) and a postsynaptic prediction error ($\text{[}\hat{r}_0; \hat{r}^h\text{]}$) jointly shaping the memory weights $G$.

**Panel (d): Recall Process Diagram**
This panel illustrates the recall process. It shows a flow starting from $\hat{m}$ and $G$. A prediction error on the partial observation, denoted by a red dotted arrow originating from $\hat{r}_0$, drives the convergence of memory estimates $\tilde{m}$ and recalls the higher-level dynamics vector $\tilde{r}^h$ as a top-down prediction. A red dotted box highlights the prediction error between missing observations for $r_h$ and the prediction $\tilde{r}^h$, which is noted as being ignored during recall.

**Panel (e): Image Sequence Simulation**
This panel displays a sequence of four grayscale images, representing the visual input used for conditioning and testing. The frames are labeled sequentially: **Start**, **Middle**, and **End**.

**Panel (f): Neural Response Plots**
This panel contains three sets of line plots, showing the responses of lower-level neurons across different testing phases.
*   **Left Plot (Conditioning):** Shows responses during conditioning.
*   **Middle Plot (Start Frame Test):** Shows responses when testing with a single start frame.
*   **Right Plot (End Frame Test):** Shows responses when testing with a single end frame.
Each plot shows multiple colored lines, and the caption specifies that these represent the five most active lower-level neurons at each step.

**Panel (g): Cross-Correlation Heatmap (Conditioning)**
This panel is a heatmap displaying the normalized pairwise cross correlation. The axes are labeled **Time** (x-axis) and **RF distance (degrees)** (y-axis). The color scale ranges from dark blue/black to bright yellow, indicating correlation strength. This heatmap is labeled **Conditioning**.

**Panel (h): Cross-Correlation Heatmaps (Testing)**
This panel contains three stacked heatmaps, comparing cross-correlations across different testing conditions:
1.  **Top Heatmap:** Labeled **Conditioning**. (Similar to Panel g).
2.  **Middle Heatmap:** Labeled **Before**, showing correlations before conditioning.
3.  **Bottom Heatmap:** Labeled **After - Before**, showing the difference in correlations between the "After" and "Before" states.

### Legends and Notations
*   **Legend (Top Right):** Defines the meaning of symbols used in the model diagrams:
    *   $\text{Prediction}$ (represented by a solid line/arrow)
    *   $\text{Estimate}$ (represented by a dashed line/arrow)
    *   $\text{Observation}$ (represented by a solid box/node)
    *   $\text{Error}$ (represented by a red dotted line/box)
*   **Variables:** $r_0$, $r_h$, $\hat{m}$, $G$, $\tilde{m}$, $\tilde{r}^h$.
*   **Axes Labels:** In Panels (g) and (h), the y-axis is labeled **RF distance (degrees)**, and the x-axis is labeled **Time**.

### Data Trends & Details
*   **Panel (f):** The colored lines show dynamic activity patterns across the time steps for conditioning and testing.
*   **Panel (g) & (h):** These heatmaps visualize correlation strength across time and spatial distance. The color intensity indicates the magnitude of the cross-correlation, with warmer colors (yellow/red) indicating higher correlation. The bottom heatmap in Panel (h) specifically highlights changes induced by the conditioning process.

https://doi.org/10.1371/journal.pcbi.1011801.g005

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
12 / 30


---

## Page 13

(emulating the hippocampus) recalls the episodic sequence dynamics rh which modulates the
transition dynamics in the DPC network (representing the visual cortex) to complete the
sequence recall. Specifically, we added to the trained DPC network another higher level of pre-
dictive coding to implement associative memory [10, 58]: the memory vector estimate ^m pre-
dicts both the content vector ^r0 and motion dynamics vector ^rh and uses the prediction error
to correct itself (Fig 5c). Upon convergence of ^m, the associative memory network stores this
vector by updating its weights G using Hebbian plasticity based on presynaptic activity ^m and
postsynaptic prediction error [10] (Fig 5c, see Methods). During recall, the memory estimate

~m is driven by the ^r0 inferred from the cue and the prediction error (Fig 5d, dashed boxes
denote the missing input). The dynamics vector rh is then recalled as the top-down prediction
after ~m has converged (Fig 5d, green dashed box). Note that during conditioning, no learning
occurs in the DPC network—only the weights of the memory network G are optimized to
store the episodic memory ^m.

We simulated the experiment of Xu et al. [1] using a moving MNIST sequence from the test
set shown in Fig 5e. After conditioning (5 repetitions of the sequence), the network was tested
with the starting frame only, the middle frame only, and the end frame only. The lower-level
responses ^r0 of the DPC network were used to recall the dynamics component rh from the
memory. The recalled dynamics were then used to predict a sequence of lower-level responses
in the DPC network. We found that the lower-level model neurons exhibited cue-triggered
activity recall given only the start frame of the sequence (Fig 5f Start). Cueing the network with
the middle frame triggered weak recall, consistent with findings by Xu et al. (see Fig 3c in Ref
[1]). The end frame did not trigger recall [1]. We found that the sequence recall is cue-specific
—when trained with sequences that have distinct digits and dynamics, the DPC network suc-
cessfully recalled the correct sequence when cued with different starting digits (Fig B in S1
Text).

Lastly, following the analysis done by Xu et al. [1], we plotted the pairwise cross-correlation
of the lower-level model neurons as a function of their spatial RF distances when tested with
the starting frame of the sequence (see Methods). As Fig 5h shows, the peaks of the correlation
showed a clear rightward slant after conditioning, consistent with the experimental results (Fig
5g). This indicates a strong sequential firing order in the lower-level model neurons elicited by
the starting cue, where neurons farther apart have longer lags in response cross-correlations, a
phenomenon that was nonexistent before conditioning (Fig 5g). These simulation results sup-
port our hypothesis that cue-triggered recall could be the result of the hippocampus, acting as
an associative memory, binding factorized sequence representations of content and dynamics
from the neocortex and recalling the corresponding dynamics component given the content
cue.

Estimating higher-order transition dynamics with a three-level model

Our results thus far involved a two-level DPC model whose second-level states predicted the
first-level state transitions. Since the second-level state is assumed to characterize the entire
sequence (Fig 1), it cannot predict higher-order transitions such as digits bouncing at the
boundaries in the Moving MNIST dataset, which requires different second-level state repre-
sentations (Fig 3). Here we show that adding a third level allows the DPC model to learn and
infer the transition dynamics of second-level states, thus capturing a temporally more abstract
representation of sequences at the third level.

Fig 6a shows the generative model for the three-level DPC model. Just as the second-level
states modulate the transition function of the first-level states in the two-level model (Fig 1),
the third-level states modulate the transitions of the second-level states. During inference (Fig

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
13 / 30


---

## Page 14

Fig 6. Three-level DPC model learns progressively more abstract temporal representations. (a) Generative model
for three-level DPC. (b) Schematic depiction of an inference process. Observation nodes are omitted for clarity. (c)
Inference for an example Moving MNIST sequence with “straight bouncing” dynamics. Red time steps mark the
moments when the first-level prediction error exceeded the threshold, causing the network to transition to a new
second-level state (see Methods). For these time steps, the predictions (second row) are by the second-level neurons,
while the rest are by the first-level neurons as in Fig 3. (d) The network’s responses to the Moving MNIST sequence in
(c). Left to right: first-level responses, second-level responses, third-level responses, first-level modulation weights,
second-level modulation weights. (e) Same as (d) but with “clockwise bouncing” dynamics. (f) Same as (d) but for the
sequence in (e). (g) Third-level responses to the Moving MNIST sequences visualized in the 2D space of the first two
principal components. Left: responses colored according to bouncing type; right: responses colored according to
motion direction. (h) Comparison of decoding performance for bouncing type versus motion direction using the
modulation weights generated by the second and third level. Error bars: ±1 standard deviation from 10-fold cross
validation. Orange: chance accuracies.

> Figure caption (from PDF text): Fig 6. Three-level DPC model learns progressively more abstract temporal representations. (a) Generative model
for three-level DPC. (b) Schematic depiction of an inference process. Observation nodes are omitted for clarity. (c)
Inference for an example Moving MNIST sequence with “straight bouncing” dynamics. Red time steps mark the
moments when the first-level prediction error exceeded the threshold, causing the network to transition to a new
second-level state (see Methods). For these time steps, the predictions (second row) are by the second-level neurons,
while the rest are by the first-level neurons as in Fig 3. (d) The network’s responses to the Moving MNIST sequence in
(c). Left to right: first-level responses, second-level responses, third-level responses, first-level modulation weights,
second-level modulation weights. (e) Same as (d) but with “clockwise bouncing” dynamics. (f) Same as (d) but for the
sequence in (e). (g) Third-level responses to the Moving MNIST sequences visualized in the 2D space of the first two
principal components. Left: responses colored according to bouncing type; right: responses colored according to
motion direction. (h) Comparison of decoding performance for bouncing type versus motion direction using the
modulation weights generated by the second and third level. Error bars: ±1 standard deviation from 10-fold cross
validation. Orange: chance accuracies.


This figure, titled "Three-level DPC model learns progressively more abstract temporal representations," is composed of eight distinct panels (a through h), presenting a combination of schematic diagrams, sequence visualizations, time-series plots, and dimensionality reduction plots.

### Panel (a): Generative Model Schematic
Panel (a) displays a schematic diagram representing the generative model for three-level DPC. It features a hierarchical structure of nodes, suggesting temporal dependencies. The diagram shows multiple layers of interconnected nodes, labeled with indices such as $r_i^{(1)}$, $r_{i-1}^{(1)}$, and $r_i^{(2)}$. Arrows indicate the flow of information, suggesting a predictive or generative process moving across time steps ($i$ to $i+1$).

### Panel (b): Inference Process Schematic
Panel (b) provides a schematic depiction of an inference process. It illustrates the relationship between different levels of representation, specifically showing nodes labeled $r_i^{(1)}$, $r_{i-1}^{(2)}$, and $r_i^{(2)}$. The diagram includes a legend indicating "Prediction," "Estimate," and "Error." Arrows show the flow of information, with a feedback loop indicated by an arrow pointing from $r_i^{(2)}$ back towards the prediction mechanism.

### Panel (c): Inference Visualization for "Straight Bouncing" Dynamics
Panel (c) visualizes the inference process for a sequence exhibiting "straight bouncing" dynamics. It consists of 19 columns, representing time steps (0 through 18). Each column contains two rows of images:
1. **Top Row (Prediction $U_F$):** Shows the network's prediction at each time step.
2. **Bottom Row (Prediction Error $I_F$):** Shows the prediction error at each time step.
The images appear to be frames from a sequence (likely MNIST digits, as per the caption context). Red time steps are marked in both rows, indicating moments when the first-level prediction error exceeded a threshold, triggering a transition to a new second-level state.

### Panel (d): Network Responses for "Straight Bouncing"
Panel (d) presents four time-series plots tracking the network's responses to the sequence shown in Panel (c). The x-axis for all plots is "Time," ranging from 0 to 15.
* **Left Plot:** Labeled $r^{(1)}$, showing the first-level responses over time.
* **Second Plot:** Labeled $r^{(2)}$, showing the second-level responses over time.
* **Third Plot:** Labeled $r^{(3)}$, showing the third-level responses over time.
* **Right Plot:** Labeled $w^{(1)}$, showing the first-level modulation weights over time.
The y-axis for all plots is "Normalized Response," ranging from 0.00 to 1.00.

### Panel (e): Inference Visualization for "Clockwise Bouncing" Dynamics
Panel (e) is structurally identical to Panel (c), visualizing the inference process for a sequence exhibiting "clockwise bouncing" dynamics. It also consists of 19 columns (Time steps 0 through 18), with two rows: "Prediction $U_F$" and "Prediction Error $I_F$." Red time steps mark state transitions.

### Panel (f): Network Responses for "Clockwise Bouncing"
Panel (f) mirrors the structure of Panel (d), showing four time-series plots for the sequence in Panel (e). The x-axis is "Time" (0 to 15), and the y-axis is "Normalized Response." The plots track $r^{(1)}$, $r^{(2)}$, $r^{(3)}$, and the modulation weights $w^{(1)}$.

### Panel (g): Third-Level Responses in 2D Space
Panel (g) visualizes the third-level responses ($r^{(3)}$) in a 2D principal component space.
* **Left Plot:** Shows the responses colored according to "bouncing type." The axes are labeled PCI (Principal Component 1) and PCI.
* **Right Plot:** Shows the responses colored according to "motion direction." The axes are labeled PCI and PCI.

### Panel (h): Decoding Performance Comparison
Panel (h) is a bar chart comparing decoding performance. The x-axis displays two categories: "Bouncing" and "Motion." For each category, there are bars representing decoding accuracy. The caption specifies that the comparison is between "bouncing type versus motion direction" using modulation weights from the second and third levels. The y-axis represents "Decoding Accuracy," ranging from 0.0 to 1.0. Orange bars represent "Chance" accuracies.

https://doi.org/10.1371/journal.pcbi.1011801.g006

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
14 / 30


---

## Page 15

6b), when the first-level prediction error is larger than a threshold (see Methods), the second-
level state transitions to the next state, following the transition function predicted by the cur-
rent third-level state. The second-level prediction error is conveyed to the third level to correct
its state estimate, in the same way as the first-level prediction error corrects the second-level
state.

The Moving MNIST dataset we used for Fig 3 exhibited only one type of transition dynam-
ics of the second-level states, namely, transitioning from moving left to moving right, or mov-
ing up to moving down, and vice versa (henceforth referred to as “straight bouncing”
dynamics (Fig 6c). To demonstrate that the third-level states can learn different second-level
dynamics, we added to the dataset digit sequences with “clockwise bouncing” dynamics to the
dataset (for example, a digit moving to the left and hitting the boundary will move upward
instead of rightward, and so on (Fig 6e). This makes the second-level state transition function
ambiguous until the first bouncing event. If the third-level representations learned by DPC
capture the second-level transition dynamics, we expect the first large prediction error at the
second level (occurring at a boundary) to update the third-level state estimate to represent
either straight bouncing dynamics or clockwise bouncing dynamics. Thereafter, the third-level
state estimate should remain stable as long as the bouncing type remains the same.

In the following, we use the superscript (i) to denote the level i. We trained a three-level
neural network on the augmented Moving MNIST dataset (with the two types of bounding
dynamics discussed above). The network uses two second-level transition matrices fV

ð2Þ
1 ; V
ð2Þ
2 g
and a top-down network Hð2Þ (from the third to the second level), in addition to all the param-
eters in the two-level model. The first and second-level transition matrices were pretrained
(see Methods). Fig 6c and 6d show an inference example of the three-layer network on an
input sequence with straight bouncing dynamics. Red time steps denote the moments when
the first-level prediction errors were larger than the set threshold, causing the second-level
neurons to change their activities to transition to the next state (this can be seen as a neural
implementation of terminal states in a hierarchical HMM [59] (see Methods)). As seen in the
second row in Fig 6c, at the first bouncing event (t = 4), the second-level prediction was not
accurate; the third-level neural responses were updated to minimize this prediction error (see
Fig 6d). For the rest of the sequence, the predictions are accurate at the bouncing events (t = 9,
14, 19) and the third-level neural responses remained stable. The panels in Fig 6d show an
increase in response stability and timescale from the first to the third-level neural responses
(first three panels), as well as in the modulation weights that define the first and second-level
transition dynamics (last two panels). Fig 3e and 3f show a different example with clockwise
bouncing dynamics. Similar to the example above, the third-level responses showed notable
changes at times t = 3 and 4 but remained stable for the rest of the sequence. Comparing the
second-level modulation weights in Fig 6d and 6f, it is clear that the third-level DPC neurons
estimated different bouncing types and generated opposite modulation strengths for the two
types of sequences.

We performed PCA on the third-level responses r(3) obtained at the end of the Moving
MNIST sequences (t = 19) in the test set. Fig 6g visualizes these responses in the space of their
first two principal components (PCs), colored either by bouncing dynamics type (left) or mov-
ing direction (right). The third-level responses form clusters according to the bouncing
dynamics type but not motion direction. We then used SVMs to decode the bouncing dynam-
ics type or motion direction from w(1) and w(2), the weights predicted by r(2) and r(3) respec-
tively. As shown in Fig 6h, using w(2), the classifier yielded 92.7% 10-fold cross-validated
classification accuracy on the two bouncing types (chance accuracy: 50.0%). Using w(1)

resulted in significantly less classification accuracy for bouncing type (66.4%, p  0.001, t-

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
15 / 30


---

## Page 16

test). In contrast, decoding accuracy for the four motion directions (chance accurary: 25.4%)
was significantly higher using w(1) (74.5%) compared to using w(2) (38.0%, p  0.001, t-test).
These results show that the three-level DPC model succeeded in learning a temporal hierarchy,
with the third-level states encoding the longest timescale feature, i.e. the type of bouncing
dynamics, by modulating the transition function of the second-level states, which in turn
encoded intermediate timescale features (motion direction).

Discussion

Our results show that dynamic predictive coding (DPC) can learn hierarchical temporal repre-
sentations of sequences through top-down modulation of lower-level dynamics. Specifically,
we showed that by minimizing prediction errors on image sequences, a two-level DPC neural
network develops V1-like separable and inseparable space-time receptive fields at the lower
level [25], and representations encoding sequences at a longer timescale at the higher level [6,
8]. The trained DPC network provides a normative explanation for the flash-lag effect [26] and
accounts for both prediction and postdiction in visual motion processing [27, 28, 60]. The
temporal abstraction of sequences in a DPC network suggests a new mechanism for storing
and retrieving episodic memories by linking the DPC network to an associative memory, emu-
lating the interaction between the neocortex and the hippocampus. We show that such a mem-
ory-augmented DPC model explains cue-triggered activity recall in the visual cortex [1].
Finally, we show that the top level of a three-level DPC network captures the higher-order tem-
poral statistics encoding the transition dynamics of the second-level states, which in turn cap-
ture the temporal statistics of the first-level states. Taken together, the hierarchical temporal
representations learned by DPC, ranging from the lowest-level space-time representations
similar to those observed in visual cortical simple cells (Fig 2), through the intermediate-level
representations of steady motion (Fig 3), to the highest-level representation of how such
motion changes over a longer timescale (Fig 6), emulate the spatiotemporal representations
observed in visual cortical hierarchies, particularly along the dorsal visual pathway [61].

The key to the DPC model’s ability to capture lower-level dynamics with relatively stable
higher-level response vectors rh is the top-down modulation of transition dynamics of entire
lower-level state sequences, using the weights w generated by the higher level. There has been
increasing interest in neuroscience in the role of modulatory inputs (e.g., encoding top-down
contextual information) in shaping the dynamics of recurrent neural networks in the brain
[62–64]. The DPC model ascribes an important role to these modulatory inputs in enabling
cortical circuits to learn temporal hierarchies. The neural implementation used in this paper
can be seen as top-down feedback (w) targeting the distal apical dendrites of lower-level pyra-
midal neurons, thereby changing their gain (Fig 1c). Such a mechanism, which has been
shown to be possible experimentally [16, 17, 39, 65], can also modulate perceptual detection
[66]. Note that although we chose to model the top-down influence as multiplicative gain
modulation, it would be theoretically equivalent to model it as an additive component or con-
catenate it as an extra input for prediction (e.g., predicting first-level transitions as
rt ¼ fðrt  1; rhÞ, where f is a multi-layer perception). However, such an implementation may be
less efficient (in terms of the number of parameters required to reach the same level of perfor-
mance) under certain conditions, compared to a hypernetwork-based implementation [67]
such as our implementation based on multiplicative gain modulation.

Some of the first models of spatiotemporal predictive coding focused on signal processing
in the retina and LGN [41, 68]. Other models for sequence processing, such as sparse coding
[20, 38] and independent component analysis [18], have been shown to produce oriented
space-time receptive fields from natural image sequences, but these models require the entire

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
16 / 30


---

## Page 17

image sequence to be presented as a single vector input, which is hard to justify biologically;
they also do not explicitly model the temporal dynamics between images and therefore, cannot
make predictions into the future given a single input. A previous spatiotemporal predictive
coding model based on Kalman filtering [40] did incorporate state transitions but the model
was not hierarchical and was not shown to generate cortical space-time receptive fields. Our
model bears some similarities to slow feature analysis which extracts slowly varying features
from sequences of stimuli but it does not learn the transition dynamics between time steps [19,
21, 22]. DPC on the other hand learns a generative model that generates entire sequences, with
the assumption that the transition dynamics do not change within a sequence (a “slow” fea-
ture). Object identity remains in the lower-level representations of DPC (Fig 3f). From a learn-
ing perspective, Luczak et al. [69] propose that single neurons predicting their future activity at
a fixed delay could also serve as an effective learning mechanism.

Recent advances in deep learning [70] have spurred several efforts to learn spatiotemporal
hierarchies from sensory data. Lotter et al. developed a deep learning model called “PredNet”
for learning a hierarchical predictive coding-inspired model for natural videos [71, 72]. After
training, the model was shown to produce a wide range of visual cortical properties and
motion illusions. However, in PredNet, higher-level neurons predict lower-level prediction
errors rather than neural activities or dynamics, making it unclear what the underlying genera-
tive model is. It is also unclear if PredNet learns a temporal response hierarchy as found in the
cortex. A different model, proposed by Singer et al. [23] and later extended to hierarchies [24],
is trained by making higher layers predict lower layer activities: after training, model neurons
in different layers displayed different levels of tuning properties and direction selectivity simi-
lar to neurons in the dorsal visual pathway. However, similar to the sparse coding and ICA
models discussed above for spatiotemporal sequences, the Singer et al. model also requires a
sequence of images to be presented as a single input to the network, and the hierarchy of time-
scales is hard-coded (higher-level neurons predict future lower-level neural activities by receiv-
ing a fixed-length chunk of neural activities as input). The above models also do not provide
explanations for postdiction or episodic memory and recall.

Many experimental studies have shown an increase in temporal representation stability and
response timescales as one goes from lower-order to higher-order areas in the visual and other
parts of the cortex [6–9, 73, 74]. Most computational models have studied this phenomenon
through mechanistic rate-based models with parameters based on connectivity data [75, 76] or
spiking network models [77]. Kiebel et al. [78] proposed a model where second-level states
generate a single parameter for the first-level Lorenz attractor as the slower “sensory cause”
parameter. DPC generalizes this model by assuming higher-level states fully determine the
lower-level transition function by predicting the transition dynamics of lower-level states.
Under this formulation, temporal hierarchies emerge naturally as a consequence of the neo-
cortex learning from temporally structured data (e.g., stable dynamics in short time windows).
This view is consistent with findings that response timescales are functionally dynamic and
could expand for cognitive tasks such as working memory [79].

Previous normative models of postdiction in visual processing often relate the effect to the
concept of Bayesian smoothing (or backward message passing) [26, 80]. We have shown that a
trained two-level DPC network with higher-level sequence representations also exhibits post-
dictive effects without the need for smoothing. In the event of a temporal irregularity (e.g., an
unexpected motion reversal), the higher-level state in the DPC network is updated to reflect a
new revised input sequence, naturally implementing postdiction through online hierarchical
Bayesian filtering (Figs 1 and 3). Our flash-lag simulation results are consistent with the Bayes-
ian filtering model from Khoei et al. [81] showing that the flash-lag effect can be produced
through an internal model that explicitly represents object velocity. The higher-level sequence

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
17 / 30


---

## Page 18

representation in the DPC model supports an implicit (and more generalized) representation
of velocity and reproduces the same internal dynamics of the “speed” estimate at motion rever-
sal (compare Fig 4h with Fig 6 in [81]). It is worth noting that the trained DPC network
learned to predict no motion (static sequence) for the flashed object even though it was never
trained on static object sequences and did not assume a prior of zero speed [81]. This emergent
property was also seen in PredNet, which learned to predict relatively little motion for a flashed
bar stimulus [72].

The higher-level sequence representations of DPC, when combined with an associative
memory, support the formation of episodic memories and cue-triggered activity recall [1, 3,
32–35]. The associative memory in our model forms an episodic memory by binding the
inferred content representation and dynamics representation from the DPC network during
conditioning. When an initial portion of the sequence is presented during testing, the stored
episodic memory is retrieved, generating the dynamics component which modulates the
lower-level network to enable full recall of the sequence. Though previously considered to only
require V1 plasticity [1, 3], sequence learning is severely impaired in mice with hippocampal
damage [82]. Coordinated activity between V1 and the hippocampus has also been found in
human V1 during recall [48]. These experimental results support the involvement of the hip-
pocampus in sequence learning, consistent with our model. Overall, the memory-augmented
DPC model offers a highly efficient computational basis for forming and recalling episodic
memories [57, 83], where a single representation of content and transition dynamics from all
sensory areas of the neocortex can be bound together as a memory and later retrieved upon
receiving partial input.

In our three-level DPC model, the second-level state (under the influence of the current
third-level state) predicts the next second-level state only when the first-level prediction errors
are larger than an estimated threshold. This can be seen as a neural (and continuous-valued)
implementation of “terminal states” in hierarchical hidden Markov models (HHMMs) [59]. In
an HHMM, when a terminal state is reached at a lower level, the corresponding sub-HMM is
deemed to be completed and the higher-level state then transitions to the next higher-level
state (which activates the next sub-HMM at the lower level). In our hierarchical DPC model,
small first-level prediction errors are resolved locally between the first and second level, indi-
cating a continuing sub-sequence. When the error exceeds the threshold, the sub-sequence
ends and the second-level transitions are activated. Any second-level prediction errors are
resolved between the second and third level through third-level state inference. We used post-
hoc estimation of the error threshold after training but future work could attempt to estimate
the threshold online in terms of the inverse variance or “precision” of prediction errors [84]).
Additionally, second-level transitions could also correlate with the spatial information in the
videos (e.g. bouncing only happens when the digit is near the boundary). Models whose sec-
ond-level states depend on both the previous first- and previous second-level states could learn
this type of transition [85].

The DPC model can be extended to action-conditioned prediction and hierarchical plan-
ning (see, e.g., [86] for initial steps in this direction). There is a growing body of evidence that
neural activity in the sensory cortex is predictive of the sensory consequences of an animal’s
own actions [2, 4, 13, 47, 87]. These results can be understood in the context of a DPC model
in which the transition function at each level is a function of both a state and an action at that
level, thereby allowing the hierarchical network to predict the consequences of actions at mul-
tiple levels of abstraction [86]. Such a model allows probabilistic inference to be used not only
for perception but also for hierarchical planning, where actions are selected to minimize the
sensory prediction errors with respect to preferred goal states. Such a model is consistent with
theories of active inference [11] and planning by inference [88–92], and opens the door to

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
18 / 30


---

## Page 19

understanding the neural basis of navigation and planning [9, 93, 94] as an emergent property
of prediction error minimization.

Methods

Hierarchical generative model

We assume that the observation It 2 RM at time t is generated by a lower-level latent variable
rt 2 RN. The latent variable rt is generated by the previous step latent variable rt−1 and the
higher-level latent variable, rh 2 RNh. Together, the generative model factorizes as follows:

pðI0:T  1; r0:T  1; rhÞ ¼ pðrhÞpðr0Þ

Y
T  1

t¼0

pðIt j rtÞ

Y
T  1

t¼1

pðrt j rt  1; rhÞ:
ð3Þ

Each component of the factorization is parameterized as follows:

rh  N ð0; 1Þ
ð4Þ

rt j ðrt  1; rhÞ  N ðfðrh; rt  1Þ; s2

rIÞ
ð5Þ

It j rt  N ðUrt; s2IÞ;
ð6Þ

where N denotes the normal distribution and I denotes the identity matrix. The mean rm

t ¼
fðrh; rt  1Þ is given by:

w ¼ HyðrhÞ
ð7Þ

V ¼

X
K

k¼1

wkVk
ð8Þ

rm

t ¼ ReLUðVrt  1Þ:
ð9Þ

Here, Hy is a function (neural network) parameterized by θ.

To sum up, the trainable parameters of the model include spatial filters U, K transition
matrices V1, . . ., VK, and the neural network parameters θ. The latent variables are r0:T−1 and
rh. See “Summary of the DPC generative model” in S1 Text for a more detailed description of
the model architecture.

Prediction error minimization

Here, we derive the loss function used for inference and learning under the assumed genera-
tive model. We focus on finding the maximum a posteriori (MAP) estimates of the latent vari-
ables using a Bayesian filtering approach. At time t, the posterior of rt conditioned on the
input observations up to time t, I0:t, and the higher-level variable rh can be written as follows
using Bayes’ theorem:

pðrt j I0:t; rhÞ / pðIt j rtÞpðrt j I0:t  1; rhÞ;
ð10Þ

where the first term on the right-hand side is the likelihood function defined by Eq 6. The sec-
ond term is the posterior of rt given input up to the previous step and the higher-level state:

pðrt j I0:t  1; rhÞ ¼

Z

pðrt j rt  1; rhÞpðrt  1 j I0:t  1; rhÞdrt  1;
ð11Þ

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
19 / 30


---

## Page 20

where the first term inside the integral is the lower-level transition dynamics defined by Eq 5.
Note that the parameterization of the transition distribution is generated by the higher-level
latent variable as specified by Eqs 7 to 9.

Putting Eqs 10 and 11 together, we get

pðrt j I0:t; rhÞ / pðIt j rtÞ

Z

pðrt j rt  1; rhÞpðrt  1 j I0:t  1; rhÞdrt  1;
ð12Þ

which defines a recursive way to infer the posterior of rt at time t. In this model, we only main-
tain a single point (MAP) estimate of the posterior at each time step, so we simplify the poste-
rior distribution p(rt−1 j I0:t−1, rh) as a Dirac delta function:

pðrt  1 j I0:t  1; rhÞ  dðrt  1   ^rt  1Þ;
ð13Þ

where ^rt  1 is the MAP estimate from the previous step. Now we can further simplify Eq 12 as

pðrt j I0:t; rhÞ / pðIt j rtÞpðrt j ^rt  1; rhÞ:
ð14Þ

This gives the posterior of all the latent variables at time t as

pðrt; rh j I0:tÞ / pðIt j rtÞpðrt j ^rt  1; rhÞpðrh j I0:tÞ:
ð15Þ

We can find the MAP estimates of the latent variables by minimizing the negative log of Eq 15.
Substituting the generative assumptions (Eqs 4 to 6), we get:

rt ¼ fðrh;^rt  1Þ
ð16Þ

Lt ¼ 1

2s2 kIt   Urtk
2
2 þ 1
2s2
r

krt   rtk

2
2 þ lkrtk1 þ lhkrhk
2
2;
ð17Þ

where λ and λh are the sparsity penalty for rt and the Gaussian prior penalty for rh, respectively.
Note that we approximate p(rh j I0:t) with the unconditional prior p(rh) so that at each step the
dynamics are estimated using only the local pairwise transition and the prior. Using Eq 17, we
compute the MAP estimate of rt at time t as

^rt ¼ arg min

rt
Lt:
ð18Þ

At each time step, we update the current estimate of rh to minimize Lt as well:

rh ¼ arg min

rh Lt:
ð19Þ

To begin the recursive estimation (without the temporal prediction from the previous step),
we compute the MAP estimate of the first step latent variable r0 using the following reduced
loss

L0 ¼ 1

2s2 kI0   Ur0k
2
2 þ lkr0k1
ð20Þ

^r0 ¼ arg min

r0 L0:
ð21Þ

The parameters of the model can be optimized by minimizing the same prediction errors
summed across time and averaged across different sequences, using the MAP estimates of the
latent variables. See Algorithm A in S1 Text for detailed pseudocode describing the inference
and learning procedure.

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
20 / 30


---

## Page 21

Data and preprocessing

For the natural video dataset, we extracted 65520 image sequences from a YouTube video (link
here) recorded by a person walking on a forest trail (image size: 16 × 16 pixels, sequence
length: 10 frames ( 0.35 seconds, uniformly sampled in time). The image sequences do not
overlap with each other spatially or temporally. Each sequence was spatially and temporally
whitened to simulate retinal and LGN processing following the methods in Olshsausen &
Field [38] and Dong & Atick [95]. 58,968 sequences were used to train the model and the
remaining 6,552 were reserved for testing.

For the Moving MNIST dataset [45], we used 10000 image sequences (image size: 18 × 18
pixels, sequence length: 10 frames), each sequence containing a fixed digit moving in a particu-
lar direction. The motion of the digits was restricted to upward, downward, leftward, or right-
ward directions. When a digit hit the boundary, its motion direction was inverted (leftward to
rightward, upward to downward, and vice versa). No whitening procedures were performed
on the MNIST sequences. 9,000 sequences were used to train the model and the remaining
1,000 were reserved for testing.

Reverse correlation for computing space-time receptive fields

The reverse correlation stimuli for deriving the space-time receptive fields (Fig 2) were
extracted from the same natural video data but without any spatial and temporal overlapping
with the training and test set. We used 50 continuous image sequences with 80,000 steps ( 47
minutes, spanned the same time range but no spatial overlaps) and computed the space-time
receptive fields (STRFs) as the firing-rate-weighted average of input frame sequences of length
seven ( 250 ms), across time and sequences.

Formally, let fI

ðjÞ
0:T  1g
J
j¼1 be the J stimulus sequences of length T and let τ be the length of the
STRFs (here, J = 50, T = 80, 000, τ = 7). For each neuron i, its space-time receptive field STRFi
has dimensions M × τ, where M is the dimensionality of a single image frame vector (here,
M = 100 after vectorizing the 10 × 10 image frame). We compute the STRF of neuron i as fol-
lows

STRFi ¼
1
JðT   tÞ

X
J

j¼1

X
T  1

t¼t

^r

ðjÞ
t;iI

ðjÞ
t  t:t  1;
ð22Þ

where ^r

ðjÞ
t;i is the predicted firing rate of neuron i at time t in sequence j and I

ðjÞ
t  t:t  1 is the image
sequence from time t −τ to t −1 in sequence j. This procedure is analogous to the calculation
of the spike-triggered average widely used in neurophysiology [43]; in this case, we computed
the average of input sequences weighted by the activity ^r caused by the sequence.

Autocorrelation for quantifying timescales

Since our model responds deterministically to the same sequence (MAP estimation), we can-
not follow the exact approach of Murray et al. [6] that relies on across-trial variability to the
same stimulus. We computed the autocorrelation of single neuron responses to natural videos
and Gaussian white noise sequences. We averaged the single-neuron autocorrelations across
the lower or higher level, and trials. Formally, let rt,i,j be the response of neuron i at time t

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
21 / 30


---

## Page 22

during trial j. We computed the autocorrelation with lag k as follows:

mi;j ¼ 1

T

X
T  1

t¼0

rt;i;j
ð23Þ

si;j ¼

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

1
T

X
T  1

t¼0

ðrt;i;j   mi;jÞ

2
s

ð24Þ

ri;jðkÞ ¼

PT  k  1

t¼0
ðrt;i:j   mi;jÞðrtþk;i;j   mi;jÞ

ðT   kÞsi;jsi;j

8i ¼ 1 . . . N:
ð25Þ

To compute the autocorrelation for an entire population at lag k, we took the average of the
autocorrelations across all N neurons and J trials:

rðkÞ ¼ 1

NJ

X
N

i¼1

X
J

j¼1

ri;jðkÞ:
ð26Þ

For the results shown in Fig 3b and 3c, we choose J = 500, T = 50 and computed the autocorre-
lation with lag k = 0. . .9 for the lower- and higher-level neurons. White noise pixels were i.i.d.
samples from N ð0; 0:0075Þ. We also computed the autocorrelation for both levels with natural
videos selected from the same stimuli used for the reverse correlation analysis (note though
with natural videos the stationary mean and variance assumption is less valid). To quantify the
timescale of the autocorrelation decay, we fitted an exponential decay function ρfit(k) = a exp
(−k/τ) + b to the autocorrelation data on each level (through Scipy optimize.curve_fit
function), where a, b, and τ are fitted parameters of the function and τ represents the response
timescale following the definition by Murray et al. [6].

Flash-lag and postdiction simulation

We extracted five-step sequences that have a consistent leftward or rightward motion from the
Moving MNIST test set sequences (134 sequences in total, see Fig 5e for an example). To simu-
late the test conditions used by Eagleman & Sejnowski [26], we either used the first three steps
of the sequences to infer a motion (dynamics) estimate ^rh (conditions with initial trajectories),
or initialized ^rh to zero vectors (conditions without initial trajectories). Depending on the test
condition, the moving object stimulus at t = 3 could move following the original trajectory
(“Continuous”), remain at the same location (“Stopped”), move in the reversed trajectory
(“Reversed”), or disappear shown an empty frame (“Terminated”), shown in Fig 4a. The sti-
muli for simulating flashes correspond to the “no initial trajectory, terminate case”.

The model’s percept of either the moving object or the flashed object at t = 3 was computed
as the top-down spatiotemporal prediction of the image after correcting the prediction error at
t = 3:

w ¼ Hyð^rhÞ
ð27Þ

V ¼

X
K

k¼1

wkVk
ð28Þ

I3 ¼ UðReLUð V^r2ÞÞ:
ð29Þ

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
22 / 30


---

## Page 23

Here, Hy and V1, . . ., VK are the parameters defined in Eqs 7 and 8, ^rh is the optimal higher-
level estimate at t = 3 (Eq 19), and ^r2 is the optimal lower-level estimate at t = 2. We computed
the location of the percept as the center of mass of the percept image I3. The displacement in
percept between the moving object and the flashed object was calculated as

Displacement ¼

CoM   x



I

moving
3


  CoM   xðIflash

3
Þ
if the moving object has rightward motion

CoM   xðIflash

3
Þ   CoM   x



I

moving
3


if the moving object has leftward motion

ð30Þ

8
>
>
<

>
>
:

where CoM-x(I) returns the horizontal location (x dimension) of the center of mass of I.
Therefore, a positive displacement is along the original trajectory of the moving object, while a
negative displacement is along the reversed trajectory.

To compute the plots shown in Fig 4g and 4h, we used the “with initial trajectory, reversal”
test condition. The displacement was computed as in Eq 30 but Iflash

3
was replaced by the input
image I2 at t = 2, at every value of rh through the error correction process at t = 3 (Eqs 27 to 30,
see Fig 4b Perceived versus Input).

Sequence learning and recall simulation

To simulate the sequence learning experiment of Xu et al. [1], we used a five-step sequence
extracted from a Moving MNIST test set sequence (Fig 5e). We augmented the hierarchical
generative model of DPC with an associative memory layer m, which implements predictive
coding of the joint higher-level state rh and the lower-level state r0 through synapses G [10, 58]
(see “Summary of the memory model” in S1 Text for model details):

ðr0; rhÞ j m  N ðGm; s2

mIÞ:
ð31Þ

The memory layer was trained separately (the DPC network weights were fixed during condi-
tioning and recall) by minimizing the prediction error:

LmemoryðG; mÞ ¼ ks   Gmk

2
2 þ lmkmk
2
2;
ð32Þ

where s ¼ ½^r0;^rh is the concatenated lower- and higher-level state estimates from DPC and
λm is the regularization penalty on m.

During memory encoding, ^r0 and ^rh were estimated by the two-level DPC network from
the sequence shown in Fig 5e. Then the memory vector m was estimated by gradient descent
on Eq 32, yielding the optimal estimate ^m:

^m ¼ arg min

m LmemoryðG; mÞ:
ð33Þ

The remaining prediction error drives rapid synaptic plasticity in G through gradient descent
on the same equation (Fig 5c):

G0 G   ZG

@LmemoryðG; ^mÞ

@G
;
ð34Þ

where ηG is the learning rate for G. During conditioning, we updated the synaptic weights five
times using Eq 34. During recall, given the cue for the beginning of the sequence, the full mem-
ory vector m is retrieved by minimizing the prediction error with respect to the initial lower-
level state r0 portion of the stored memory only [58] (Fig 5d):

~m ¼ arg min

m k~s   b  ðGmÞk

2
2 þ lmkmk
2
2;
ð35Þ

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
23 / 30


---

## Page 24

where ~s ¼ ½^r0; 0Nh denotes the partial input (visual cue representing the first element of the
sequence),  denotes element-wise multiplication, and b 2 f0; 1g

NþNh is a binary mask:

bi ¼

1
if i  N

0
otherwise

:

(

ð36Þ

The rest of the sequence was retrieved by retrieving the stored higher-level state rh (the dynam-
ics of the sequence) as the top-down prediction through ~m (Fig 5d). Once the dynamics were
retrieved, we tested sequential recall in the network by predicting an entire five-step sequence
using the lower-level vector ^r0 from the visual cue and the retrieved dynamics vector rh from
the memory (Eqs 7 to 9). We tested recall in the network using three different visual cues: the
starting frame (t = 0), the middle frame (t = 2), or the end frame (t = 4) (see Fig 5e and 5f). The
cross correlation plot was computed following the same procedure as the one described in Xu
et al. [1] (Fig 5g and 5h).

Three-level DPC model

To make the level notation clear, we denote the first and second-level states r and rh from the
two-level model as r(1) and r(2) in the three-level model, and denote the highest (third-level)
state as r(3). We use superscripts to denote level and subscripts to denote time, unless noted
otherwise. The trainable parameters for the three-level model include those for the two-level
model as well as two second-level transition matrices fV

ð2Þ
1 ; V
ð2Þ
2 g and the third-level top-down
network H

ð2Þ
y that generates the second-level modulation weights.
Pretraining the second-level transition matrices.
Before training the three-level net-
work, we first pretrained two two-level DPC networks, each with a single transition matrix
V(2) on Moving MNIST sequences with either straight bouncing type or clockwise bouncing
type. We performed inference on the second-level states with the following loss function:

Lt ¼ 1

2s2 kIt   Urð1Þ
t k

2
2 þ 1
2s2
r

krð1Þ

t
  rð1Þ

t k

2
2 þ bt
1
2s2
rð2Þ

krð2Þ

t
  rð2Þ

t k

2
2

!

þ lkrtk1;
ð37Þ

where s2

rð2Þ is the variance of second-level prediction errors, bt 2 {0, 1} is a binary mask that
equals 1 if the first-level prediction error is larger than a threshold estimated from the training
set and 0 otherwise (Fig C in S1 Text), and r

ð2Þ
t
¼ Vð2Þr

ð2Þ
t  1 is the predicted second-level state.
We learned V(2) by gradient descent on the same loss as in Eq 37, summed across time and
averaged across sequences, using the MAP estimates of the latent variables.

Three-level model training.
We inferred the second- and third-level states using the
same loss function (Eq 37), with the predicted second-level state r

ð2Þ
t
defined as

wð2Þ ¼ H

ð2Þ
y ðrð3ÞÞ
ð38Þ

Vð2Þ ¼

X
Kð2Þ

k¼1

w

ð2Þ
k V

ð2Þ
k
ð39Þ

r

ð2Þ
t
¼ Vð2Þr

ð2Þ
t  1;
ð40Þ

where K(2) = 2 is the number of second-level transition matrices. Comparing this definition
with Eqs 7 to 9, it is easy to see that the third-level top-down prediction is recursively defined
in the same way as the top-down prediction in the two-level model. After obtaining the MAP

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
24 / 30


---

## Page 25

estimates of the second- and third-level states, we learned the third-level top-down network
H

ð2Þ
y by gradient descent on the same loss. See Algorithm B in S1 Text for detailed pseudocode
describing the inference and learning procedure for the three-level model.

Supporting information

S1 Text. Supporting information. Fig A. Improvement on test set loss saturates as the
number of transition matrices increases. (a) Test set loss as training proceeded. Shaded area
denotes ±1 standard deviation computed over eight runs with random initialization for each
K. K = 1 shows the performance of the single-layer model. (b) Best test loss as K increases.
Error bars denote ±1 standard deviation. Fig B. Cue-triggered recall is cue-specific. Four
examples of cue-specific sequence recall by the associative memory model after training on dif-
ferent sequences, when given the first frame as the cue. In each quadrant: top: the original
image sequence; bottom: cue-triggered recall of the stored sequence. Fig C. Prediction error
threshold robustly finds changes of dynamics. (a) The distribution of first-level prediction
errors in the two-level DPC model on the Moving MNIST training set. The red dashed line
denotes the threshold ρ = 0.73, where the cumulative density reaches 0.75. (b) Examples of
input sequences in the test set. The red arrows mark time steps when the first-level prediction
errors exceeded ρ, corresponding to changes in input dynamics. Table A. DPC generative
model parameters and values. Table B. Optimizers and learning rates used for inference
and learning in the DPC experiments. Here Δ denotes the difference in rt or rh from before
and after the current iteration of gradient descent. Table C. Memory model parameters and
values. Table D. Optimizers and learning rates used for inference and learning in the
memory model. Here Δ denotes the difference in m from before and after the current iteration
of gradient descent. Table E. Additional parameters and values for the three-level DPC
model. Table F. Additional optimizers and learning rates used for inference and learning
in the three-level DPC experiments. Algorithm A. Inference & learning process. Algorithm
B. Inference & learning process for the three-level DPC model.
(PDF)

Acknowledgments

The authors would like to thank Ares Fisher, Dimitrios Gklezakos, Prashant Rangarajan and
Vishwas Sathish for discussions related to hypernetworks and predictive coding. LPJ thanks
Daogao Liu for inspiring discussions on the modeling aspects of the paper.

Author Contributions

Conceptualization: Linxing Preston Jiang, Rajesh P. N. Rao.

Data curation: Linxing Preston Jiang.

Formal analysis: Linxing Preston Jiang.

Funding acquisition: Rajesh P. N. Rao.

Investigation: Linxing Preston Jiang, Rajesh P. N. Rao.

Methodology: Linxing Preston Jiang, Rajesh P. N. Rao.

Project administration: Linxing Preston Jiang, Rajesh P. N. Rao.

Resources: Linxing Preston Jiang, Rajesh P. N. Rao.

Software: Linxing Preston Jiang.

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | https://doi.org/10.1371/journal.pcbi.1011801
February 8, 2024
25 / 30


---

## Page 26

Supervision: Rajesh P. N. Rao.

Validation: Linxing Preston Jiang.

Visualization: Linxing Preston Jiang.

Writing – original draft: Linxing Preston Jiang, Rajesh P. N. Rao.

Writing – review & editing: Linxing Preston Jiang, Rajesh P. N. Rao.