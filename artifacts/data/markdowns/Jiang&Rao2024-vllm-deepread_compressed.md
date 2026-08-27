## 

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
cortex. Additionally, the network's hierarchical sequence representation exhibited both pre-
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

PLOS Computational Biology | 
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
PLoS Comput Biol 20(2): e1011801. 
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
available at 
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

## 

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
internal model of the world, and (b) the brain's temporal representations must span different
timescales to support predictions over both short and long horizons.

Many experimental studies have provided evidence for such computations. Predictive rep-
resentations of upcoming stimuli have been found in various open and closed-loop paradigms
where animals developed experience-dependent visual and auditory expectations [1-5]. Other
empirical evidence suggests that cortical representations exhibit a hierarchy of timescales and
an increase in stability from lower-order to higher-order areas across both sensory and cogni-
tive regions [6-9]. We asked the question: could such phenomena be explained by the neocor-
tex learning a spatiotemporal generative model based on a temporal hierarchy of
representations?

Predictive coding provides a unifying framework for understanding perception and predic-
tion in terms of learning hierarchical generative models of the environment [10-14]. Here, we
present dynamic predictive coding (DPC), a new predictive coding model for learning hierar-
chical temporal representations. The central idea of our proposal is that our perceptual system
learns temporally abstracted representations that encode entire sequences rather than single
points at any given time. Specifically, DPC assumes that higher-level model neurons modulate
the transition dynamics of lower-level networks, building on the computational concept of
hypernetworks [15]. Hypernetworks are neural networks that generate the parameters (synap-
tic weights) for another neural network. However, generating an entire set of high-dimen-
sional synaptic weights is not neurally plausible. Instead, DPC models the transition dynamics
at a lower level of a hierarchy using a small set of modulation weights for a group of learned
transition matrices. These weights implement "top-down" gain modulation of the lower-level
synapses [16, 17] and are predicted by the higher level through a feedback network (a hyper-
network) connecting the higher to the lower level. Compared to previous normative models of
video processing that either do not learn the temporal dynamics between images [18-22] or
presume a fixed temporal hierarchy [23, 24] (see Discussion), the DPC model offers a neural
implementation of spatiotemporal prediction that learns the transition dynamics of the input
and adapts its hierarchical temporal representation to the intrinsic timescales of the data.

We tested the DPC model using a two-level neural network trained on natural and artificial
image sequences to minimize spatiotemporal prediction errors. After training, the lower-level
neurons developed space-time receptive fields similar to those found in simple cells in the

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | 
February 8, 2024
2 / 30

from the Templeton World Charity Foundation, and
a Cherng Jia and Elizabeth Yun Hwang
Professorship to RPNR. The funders had no role in
study design, data collection and analysis, decision
to publish, or preparation of the manuscript."

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

## 

primary visual cortex (V1) [25]. Neurons in the second level learned to capture input dynamics
on a longer timescale and their responses exhibited greater stability compared to responses in
the first level, similar to the temporal response hierarchies observed in the cortex [6-9]. We
further show that the learned sequence representations in the network can explain both pre-
dictive and postdictive effects seen in visual processing [26-29], reproducing several aspects of
the flash-lag illusion [26, 30, 31]. When linked to an associative memory mimicking the role of
the hippocampus, the network allowed storage of episodic memories and exhibited cue-trig-
gered activity recall after repeated exposure to a fixed input sequence, an effect previously
reported in rodents [1], human V1 [32-34] and monkey V4 [35]. Lastly, when extended to
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
k¼1 which can be linearly combined using a set of "modulation"
weights given by a K-dimensional vector w. This vector of weights is generated by the higher-
level state vector rh using a function H (Fig 1b), implemented as a neural network (a "hyper-
network" [15]-see "Hypernetworks and neural gain modulation" in S1 Text):

w ¼ H(rh)
(1)

V ¼

X
K

k¼1

wkVk:
(2)

Here, wk is the kth component of the vector w. The lower-level state vector at time t + 1 is gen-
erated as rt+1 = ReLU(Vrt) + m where m is zero mean Gaussian white noise. Note that this is
one particular parameterization for top-down modulation of the lower-level transition dynam-
ics, with the hypernetwork formulation allowing other types of parameterizations (see "Hyper-
networks and neural gain modulation" in S1 Text).

The generative model in Fig 1b can be implemented in a hierarchical neural network: the
higher-level state rh, represented by higher-level neurons, generates a top-down modulation w
via a top-down feedback neural network H, and this top-down input w influences the groups
of lower-level neurons representing Vi through gain modulation [16, 17] (see "Hypernetworks
and neural gain modulation" in S1 Text for details). We propose that such a computation
could be implemented by cortical pyramidal neurons receiving top-down modulation via their
apical dendrites (through gain control [17, 39]) and the recurrent state rt (and input prediction
errors) via their basal dendrites, and integrating these to predict the next state (Fig 1c).

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | 
February 8, 2024
3 / 30

---

## 

When an input sequence is presented, the model employs a Bayesian filtering approach to
perform online inference on the latent vectors [40] by minimizing a loss function that includes
prediction errors and penalties from prior distributions over the latent variables (see Meth-
ods). Given the model's estimates ^rt and ^rh at time t, the estimate ^rtþ1 of r at time t + 1 is com-

puted by gradient descent to minimize the sum of the input prediction error kItþ1   U^rtk

2 and

the temporal state prediction error krtþ1   ReLU(V^rt)k

2 plus a sparseness penalty. Similarly,
the second level estimates ^rh is updated using the temporal prediction error plus a prior-related
penalty. The model's parameters are learned by minimizing the same prediction errors across
all time steps and input sequences, further reducing the errors not accounted for by the infer-
ence process above for latent vectors (see Methods).

Hierarchical predictive coding of natural videos

We implemented the DPC model described above using a two-level neural network where
neural responses represent estimates of the latent state vectors and whose synaptic weights rep-
resent the spatial filters and transition parameters. We used K = 5 transition matrices for the
first level (more matrices did not significantly improve performance-see Fig A in S1 Text).
Perception in the DPC network corresponds to estimating the latent vectors by updating neu-
ral responses (through network dynamics) to minimize prediction errors via gradient descent
(see Methods). Updating network parameters to further reduce prediction errors corresponds
to learning (slow changes in synaptic weights through synaptic plasticity).

Fig 1d and 1e illustrate the inference process for both levels of the network. The network
generates top-down and lateral predictions (green) using the current two-level state estimates

Fig 1. Dynamic predictive coding. (a) Generative model for dynamic predictive coding. (b) Parameterization of the model. The higher-
level state modulates the lower-level transition matrices through a top-down network ("hypernetwork") H. (c) A possible neural
implementation of the generative model using cortical pyramidal neurons. Pyramidal neurons receive the top-down embedding vector
input via synapses at apical dendrites and the current recurrent state vector via basal dendrites, and produce as their output the next state
vector. (d) Schematic depiction of an inference step when the dynamics at the lower level is stable. The higher-level state remains stable
due to minimal prediction errors. (e) Depiction of an inference step when the lower-level dynamics changes. The resulting large prediction
errors drive updates to the higher-level state to account for the new lower-level dynamics.

> Figure caption (from PDF text): Fig 1. Dynamic predictive coding. (a) Generative model for dynamic predictive coding. (b) Parameterization of the model. The higher-
level state modulates the lower-level transition matrices through a top-down network ("hypernetwork") H. (c) A possible neural
implementation of the generative model using cortical pyramidal neurons. Pyramidal neurons receive the top-down embedding vector
input via synapses at apical dendrites and the current recurrent state vector via basal dendrites, and produce as their output the next state
vector. (d) Schematic depiction of an inference step when the dynamics at the lower level is stable. The higher-level state remains stable
due to minimal prediction errors. (e) Depiction of an inference step when the lower-level dynamics changes. The resulting large prediction
errors drive updates to the higher-level state to account for the new lower-level dynamics.

This figure, labeled "Fig 1. Dynamic predictive coding," is composed of five distinct panels (a through e), illustrating different aspects of a dynamic predictive coding framework, ranging from generative models to neural implementations and inference steps.

---

## 

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
The next row shows the model's predictions Urt for each time step t, where rt was predicted
by the previous state estimate ^rt  1: rt ¼ ReLU(V^rt  1). The prediction errors It   Urt are
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
total). The first column labeled "Spatial" shows the spatial RFs of the example neurons.

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

PLOS Computational Biology | 
February 8, 2024
5 / 30

---

## 

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
frames. Top to bottom: Input sequence; model's prediction of the current input from the previous step (the first step prediction being zero);
prediction error (predicted input subtracted from the actual input); model's final estimate of the current input after prediction error
minimization. (b) The trained DPC network's response to the natural image sequence in (a). Each plotted line represents the responses of a
model neuron over 10 time steps. Top: responses of the 20 most active lower-level neurons (some colors are repeated); middle: responses of
seven randomly chosen higher-level neurons; bottom: predicted transition dynamics (each line is the modulation weight for a basis transition
matrix at the lower level). (c) 40 example spatial receptive fields (RFs) learned from natural videos. Each square tile is a column of U reshaped to
a 16 × 16 image. (d) Space-Time RFs (STRFs) of four example lower-level neurons. First column: the spatial RFs of the example neurons. Next
seven columns: the STRFs of the example neurons revealed by reverse correlation mapping. (e) Left panel: space-time plots of the example
neurons in (d). Right panel: space-time plots of the RFs of two simple cells in the primary visual cortex of a cat (adapted from [25]).

> Figure caption (from PDF text): Fig 2. Predictive coding of natural videos and learned space-time receptive fields. (a) Inference on an example input image sequence of 10
frames. Top to bottom: Input sequence; model's prediction of the current input from the previous step (the first step prediction being zero);
prediction error (predicted input subtracted from the actual input); model's final estimate of the current input after prediction error
minimization. (b) The trained DPC network's response to the natural image sequence in (a). Each plotted line represents the responses of a
model neuron over 10 time steps. Top: responses of the 20 most active lower-level neurons (some colors are repeated); middle: responses of
seven randomly chosen higher-level neurons; bottom: predicted transition dynamics (each line is the modulation weight for a basis transition
matrix at the lower level). (c) 40 example spatial receptive fields (RFs) learned from natural videos. Each square tile is a column of U reshaped to
a 16 × 16 image. (d) Space-Time RFs (STRFs) of four example lower-level neurons. First column: the spatial RFs of the example neurons. Next
seven columns: the STRFs of the example neurons revealed by reverse correlation mapping. (e) Left panel: space-time plots of the example
neurons in (d). Right panel: space-time plots of the RFs of two simple cells in the primary visual cortex of a cat (adapted from [25]).

This figure, Figure 2, is divided into five distinct panels (a, b, c, d, and e), illustrating the process of predictive coding applied to natural video sequences and visualizing the learned receptive fields.

## 

neural responses observed in the cortex [6-9] could be an emergent property of the cortex
learning a similar hierarchical generative model.

We tested this hypothesis in our DPC network trained on natural videos. As seen in the
inference example in Fig 2b, the lower-level responses change rapidly as the stimulus moves
(top panel). The higher-level responses (middle panel) and the predicted transition dynamics
(right panel) were more stable after the initial adaptation to the motion. Since the stimulus
continued to follow roughly the same dynamics (leftward motion) after the first two steps, the
transition matrix predicted by the higher-level neurons continued to be accurate for the rest of
the steps, leading to small prediction errors and few changes in the responses. Note that we did
not enforce a longer time constant or smoothness constraint for rh during inference-the lon-
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

To further understand the model's ability to learn hierarchical temporal representations, we
trained a DPC network on the Moving MNIST dataset [45]. Each image sequence in this data-
set contains ten 18 × 18 pixel frames showing a single example of a handwritten digit (chosen
from the original MNIST dataset) moving in a particular direction. The digit's motion is lim-
ited to up, down, left, or right directions with a fixed speed. Fig 3c illustrates the trained net-
work's inference process on an example image sequence. Similar to the responses to the
natural video sequence, the lower-level responses displayed fast changes while the higher-level
responses spanned a longer timescale and showed greater stability (Fig 3d). Note that at time
t = 4 and t = 8, the input dynamics changed as the digit "bounced" against the boundaries and
started to move in the opposite motion (Fig 3c red dashed box). The higher-level neurons' pre-
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

PLOS Computational Biology | 
February 8, 2024
7 / 30

---

## 

(46.5%, p  0.001, t-test). In contrast, decoding accuracy for digit identity was significantly
higher using the lower-level responses (76.1%) compared to using the higher-level responses
(20.9%, p  0.001, t-test). These results show that due to the structure of its generative model,
the DPC network learned to disentangle to a significant extent the motion information in an
input video from image content (here, digit identity), yielding a factored representation of
input image sequences.

Predictive and postdictive effects in visual motion processing

The ability of the DPC model to encode entire sequences at the higher level (cf. the "timeline"
model of perception [29]) leads to new normative and computational interpretations of visual
motion phenomena such as the flash-lag illusion [26, 30, 31], explaining both predictive and

Fig 3. Hierarchical temporal representation with different timescales. (a) Autocorrelation of the lower- and higher-
level responses in the trained network with natural videos. Shaded area denotes ±1 standard deviation. Dotted lines
show fitted exponential decay functions. Left: response recorded during natural video stimuli; right: white noise stimuli.
(b) Autocorrelation of the neural responses recorded from MT and LPFC of monkeys. Adapted from Murray et al. [6]
(c) Inference for an example Moving MNIST sequence in a trained network. The red dashed boxes mark the time steps
when the dynamics of the input changed. (d) The network's responses to the input Moving MNIST sequence in (c).
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
when the dynamics of the input changed. (d) The network's responses to the input Moving MNIST sequence in (c).
Note the changes in the higher-level responses after the input dynamics changed (red dashed boxes); this gradient-based
change helps to minimize prediction errors. (e) Higher-level responses to the Moving MNIST sequences visualized in
the 2D space of the first two principal components. Left: responses colored according to motion direction; right:
responses colored according to digit identities. (f) Comparison of decoding performance for motion direction versus
digit identity using lower- and higher-level neural responses. Error bars: ±1 standard deviation from 10-fold cross
validation. Orange: chance accuracies.

This figure, titled "Hierarchical temporal representation with different timescales," is composed of six distinct panels (a through f) presenting various types of data visualizations, including autocorrelation plots, sequence representations, and principal component analyses.

## 

postdictive effects [27, 29]. The flash-lag illusion refers to the phenomenon that a flashed,
intermittent object is perceived to be "lagged" behind the percept of a continuously moving
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
(Fig 4a bottom). After the flash, the ring could continue moving on its initial trajectory ("con-
tinuous"), stop moving ("stopped"), or move on the reversed trajectory ("reversed"). A flash
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
time of the flash (Fig 4b right). Note that flashed stimuli correspond to the "no initial trajec-
tory, terminate" condition. We computed the location of a digit as the center of mass of pixel
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

PLOS Computational Biology | 
February 8, 2024
9 / 30

---

## 

reported by Eagleman & Sejnowski (Fig 4c). Fig 4g confirms that the initial trajectories of the
moving object had no effects on the model's flash-lag illusion, consistent with the reported
results (Fig 4d) [26]. These results validate the explanation provided by the DPC model on the
flash-lag effect: for a hierarchical generative model with representations of sequences, a flashed
or stopped/terminated moving object leads to inference of a static object sequence (Fig 4e),

Fig 4. Flash-lag illusion and object representations in apparent motion. (a) The flash-lag test conditions used by [26].
The moving ring could have an initial trajectory (top) or no trajectory (bottom). At the time of the flash (bright disk), the
ring could move along the initial trajectory, stop, or reverse its trajectory. Adapted from [26]. (b) Two test conditions
(left) regarding initial trajectories of the moving object (a digit) in the flash-lag experiment with the model, and four test
conditions (right) for the moving object. The flashed object was shown at time t and turned off at time t + 1 (same as the
"Terminate" condition). (c & d) Psychophysical estimates for human subjects reported by [26] when the moving object
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
latency correspond to "Early percept" and "Late percept" respectively in part (h). (l) Perceived location of the digit at all
latencies during the prediction error minimization process in part (h).

> Figure caption (from PDF text): Fig 4. Flash-lag illusion and object representations in apparent motion. (a) The flash-lag test conditions used by [26].
The moving ring could have an initial trajectory (top) or no trajectory (bottom). At the time of the flash (bright disk), the
ring could move along the initial trajectory, stop, or reverse its trajectory. Adapted from [26]. (b) Two test conditions
(left) regarding initial trajectories of the moving object (a digit) in the flash-lag experiment with the model, and four test
conditions (right) for the moving object. The flashed object was shown at time t and turned off at time t + 1 (same as the
"Terminate" condition). (c & d) Psychophysical estimates for human subjects reported by [26] when the moving object
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
latency correspond to "Early percept" and "Late percept" respectively in part (h). (l) Perceived location of the digit at all
latencies during the prediction error minimization process in part (h).

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

PLOS COMPUTATIONAL BIOLOGY
Dynamic predictive coding

PLOS Computational Biology | 
February 8, 2024
10 / 30

---