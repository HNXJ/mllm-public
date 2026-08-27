## 

Single-phase deep learning in cortico-cortical networks

Will Greedy∗
Bristol Computational Neuroscience Unit
Department of Computer Science, SCEEM

University of Bristol, United Kingdom

will.greedy@bristol.ac.uk

Heng Wei Zhu∗
Bristol Computational Neuroscience Unit
School of Phys., Pharm. and Neuroscience

University of Bristol, United Kingdom

hengwei.zhu@bristol.ac.uk

Joseph Pemberton
Bristol Computational Neuroscience Unit
Department of Computer Science, SCEEM

University of Bristol, United Kingdom

joe.pemberton@bristol.ac.uk

Jack Mellor
School of Phys., Pharm. and Neuroscience

University of Bristol, United Kingdom

jack.mellor@bristol.ac.uk

Rui Ponte Costa
Bristol Computational Neuroscience Unit
Department of Computer Science, SCEEM

University of Bristol, United Kingdom

rui.costa@bristol.ac.uk

Abstract

The error-backpropagation (backprop) algorithm remains the most common solu-
tion to the credit assignment problem in artificial neural networks. In neuroscience,
it is unclear whether the brain could adopt a similar strategy to correctly modify its
synapses. Recent models have attempted to bridge this gap while being consistent
with a range of experimental observations. However, these models are either unable
to effectively backpropagate error signals across multiple layers or require a multi-
phase learning process, neither of which are reminiscent of learning in the brain.
Here, we introduce a new model, Bursting Cortico-Cortical Networks (BurstCCN),
which solves these issues by integrating known properties of cortical networks
namely bursting activity, short-term plasticity (STP) and dendrite-targeting in-
terneurons. BurstCCN relies on burst multiplexing via connection-type-specific
STP to propagate backprop-like error signals within deep cortical networks. These
error signals are encoded at distal dendrites and induce burst-dependent plasticity
as a result of excitatory-inhibitory top-down inputs. First, we demonstrate that
our model can effectively backpropagate errors through multiple layers using a
single-phase learning process. Next, we show both empirically and analytically
that learning in our model approximates backprop-derived gradients. Finally, we
demonstrate that our model is capable of learning complex image classification
tasks (MNIST and CIFAR-10). Overall, our results suggest that cortical features
across sub-cellular, cellular, microcircuit and systems levels jointly underlie single-
phase efficient deep learning in the brain.

∗Equal contributions

36th Conference on Neural Information Processing Systems (NeurIPS 2022).

---

## 

Introduction

For effective learning, synaptic modifications throughout the brain should result in improved be-
havioural function. This requires a process by which credit should be assigned to synapses given their
contribution to behavioural output [1-3]. In multilayer networks, credit assignment is particularly
challenging as the impact of changing a synaptic connection depends on its downstream brain areas.
Classical local Hebbian plasticity rules, even when coupled with global neuromodulatory factors,
are unable to communicate enough information for effective credit assignment through multiple
layers of processing [3]. In machine learning, the error-backpropagation (backprop) algorithm is
the most successful solution to the credit assignment problem. However, it relies on a number of
biologically implausible assumptions to compute gradient information used for synaptic updates.
Previous work has attempted to address these implausibilities but important issues remain open when
mapping backprop to the neuronal physiology. Earlier attempts relied on using single-compartment
neuron models [4, 5] but this poses a problem as single-compartment neurons are unable to simulta-
neously store the necessary inference and credit assignment signals. One solution is to model neurons
with an apical dendritic compartment that separately stores credit information [5, 6], supported by
the electrotonic separation of the soma and apical dendrites [7]. These distal credit signals can
then be communicated to the soma through non-linear dendritic events that trigger bursting at the
soma [8], thereby inducing long-term synaptic plasticity [9]. In particular, two recent approaches,
Error-encoding Dendritic Networks (EDNs) [6] and Burstprop [10], have demonstrated how such
multi-compartment neuron models can be used to construct networks capable of backprop-like credit
assignment. EDNs encode credit signals at apical dendrites resulting from the mismatch between
dendritic-targeting interneuron activity and downstream activity. Burstprop uses bursting, controlled
by dendritic excitability, as a mechanism to communicate credit signals. However, these models
still have major issues, such as the inability to effectively backpropagate error signals through many
layers (EDNs) and the requirement for a multi-phase learning process (Burstprop).

Here, we propose a new model called the Bursting Cortico-Cortical Network (BurstCCN) as a solution
to the credit assignment problem which addresses several outstanding issues of current biologically
plausible backprop research. Our model builds upon prior multi-compartment neuron models [6, 10]:
it encodes credit signals in distal dendritic compartments which trigger bursting activity at the
soma to drive backprop-like synaptic updates. We demonstrate that combining well-established
properties of cortical neurons such as bursting activity, short-term plasticity (STP) and dendrite-
targeting interneurons provides a biologically plausible mechanism for performing credit assignment.
In contrast to previous models, BurstCCN is highly effective at backpropagating credit signals in
multi-layer architectures while only requiring a single-phase learning process. We implement multiple
versions of the BurstCCN at different levels of abstraction in order to demonstrate some of its key
properties and to empirically confirm our theoretically motivated claims.

First, we use a spike-based implementation of the BurstCCN to demonstrate its ability to learn without
the need for multiple phases. We further show the importance of this single-phase learning by training
a continuous-time rate-based version of the BurstCCN on a continuous-time non-linear regression
task. Next, we show both empirically and analytically that our model's dynamics result in learning
that approximately follows backprop-derived gradients. Finally, we use a simplified discrete-time
BurstCCN implementation to demonstrate that the model achieves good performance on non-trivial
image classification tasks (MNIST and CIFAR-10), even in the presence of random feedback synaptic
weights.

Bursting Cortico-Cortical Networks

2.1
Burst Ensemble Multiplexing

Burst Ensemble Multiplexing (BEM) [11] refers to the idea that ensembles of cortical neurons are
capable of simultaneously representing multiple distinct signals within the patterns of their spiking
activity. Typically, pyramidal cells receive top-down and bottom-up signals into their apical and basal
dendrites, respectively. Bottom-up basal inputs affect the rate of spiking and top-down apical inputs
convert these somatically induced spikes into high-frequency bursts. Postsynaptic populations can
then use STP to decode these distinct signals from the overall spiking activity.

---

## 

output
teacher

target

layer 0
layer 1
layer 2

(input)
(hidden)
(output)

short-term depression (events)
short-term facilitation (bursts)

layer 1
layer 2

W1

W2

Q1

Y1

v1

u1

v2

IN

LTP
LTD

LTP
LTD

Figure 1: Bursting cortico-cortical networks (BurstCCN) for credit assignment through bursting
activity. (A) Network schematic consisting of neuron ensembles and connection-type-specific STP.
Events from the input are propagated forward through short-term depressing (STD) connections, W.
Output event rates are compared to a target value which generates a teaching signal that is presented
to the output layer apical dendrites. This acts as an error signal and appears as a deflection in the
dendritic potential from its resting potential which causes changes to bursting activity from its baseline.
The error-carrying bursting signals are propagated back through short-term facilitating connections,
Y, which we interpret as being communicated by populations of dendrite-targeting interneurons.
Events are also propagated backwards via STD connections, Q, to provide a means of cancelling
baseline bursting activity. The difference in activity from these two feedback connections results in
changes to dendritic excitability that lead to burst-dependent synaptic plasticity. (B) Burst-dependent
plasticity rule. Simple setup of a single connection between a pre- and post-synaptic cell that are both
modelled with Poisson spike trains with equal rates. As the firing rates increase, (top) plasticity of the
synaptic weight switches from long-term depression (LTD) to long-term potentiation (LTP) (middle)
when the burst probability increases above the baseline value. (bottom) The magnitude of the weight
change is scaled by the event rate. (C) Homeostatic plasticity rule for Q weights. The difference
between the signals through Q and Y dictates the direction and magnitude of synaptic plasticity.

> Figure caption (from PDF text): Figure 1: Bursting cortico-cortical networks (BurstCCN) for credit assignment through bursting
activity. (A) Network schematic consisting of neuron ensembles and connection-type-specific STP.
Events from the input are propagated forward through short-term depressing (STD) connections, W.
Output event rates are compared to a target value which generates a teaching signal that is presented
to the output layer apical dendrites. This acts as an error signal and appears as a deflection in the
dendritic potential from its resting potential which causes changes to bursting activity from its baseline.
The error-carrying bursting signals are propagated back through short-term facilitating connections,
Y, which we interpret as being communicated by populations of dendrite-targeting interneurons.
Events are also propagated backwards via STD connections, Q, to provide a means of cancelling
baseline bursting activity. The difference in activity from these two feedback connections results in
changes to dendritic excitability that lead to burst-dependent synaptic plasticity. (B) Burst-dependent
plasticity rule. Simple setup of a single connection between a pre- and post-synaptic cell that are both
modelled with Poisson spike trains with equal rates. As the firing rates increase, (top) plasticity of the
synaptic weight switches from long-term depression (LTD) to long-term potentiation (LTP) (middle)
when the burst probability increases above the baseline value. (bottom) The magnitude of the weight
change is scaled by the event rate. (C) Homeostatic plasticity rule for Q weights. The difference
between the signals through Q and Y dictates the direction and magnitude of synaptic plasticity.

This figure, labeled with the letter 'C', presents a schematic representation of plasticity rules and associated data plots related to bursting cortico-cortical networks (BurstCCN).

#### Top Section: Plasticity Schematics
This section displays two small, framed diagrams side-by-side, illustrating Long-Term Potentiation (LTP) and Long-Term Depression (LTD).

1.  **LTP Schematic (Left):**
    *   This diagram is enclosed in a green rectangular box labeled "LTP".
    *   It depicts a simplified synaptic interaction involving two nodes (pre- and post-synaptic).
    *   The pre-synaptic node is represented by a small blue circle.
    *   The post-synaptic region is represented by a larger, shaded gray area (likely representing dendritic structure).
    *   A curved arrow indicates the synaptic connection, suggesting a change in weight.
    *   Below this schematic, there is an annotation showing the plasticity rule: $\text{LTP} \uparrow$ and $\text{LTD} \downarrow$, indicating that the LTP mechanism is upregulated while LTD is downregulated.

2.  **LTD Schematic (Right):**
    *   This diagram is enclosed in a purple rectangular box labeled "LTD".
    *   It mirrors the structure of the LTP schematic.
    *   The pre-synaptic node is represented by a small orange circle.
    *   The post-synaptic region is again represented by the shaded gray area.
    *   A curved arrow indicates the synaptic connection, suggesting a change in weight.
    *   Below this schematic, there is an annotation showing the plasticity rule: $\text{LTP} \downarrow$ and $\text{LTD} \uparrow$, indicating that the LTD mechanism is upregulated while LTP is downregulated.

#### Bottom Section: Heatmap Plot
This section features a 2D heatmap plot displaying the magnitude of weight change ($\Delta Q$) as a function of two variables, $Q_e$ and $Yb$.

*   **Axes:**
    *   The **x-axis** is labeled "$Yb$" and ranges from 0 to 4.
    *   The **y-axis** is labeled "$Q_e$" and ranges from 0 to 4.
*   **Color Bar/Legend:** A vertical color bar is positioned to the right of the heatmap, labeled "$\Delta Q$". This scale ranges from -0.4 (dark purple) to 0.4 (bright green), with white/light colors representing values near zero.
*   **Data Trend:** The heatmap shows a gradient:
    *   The upper-left corner (low $Yb$, high $Q_e$) is colored in shades of green, indicating positive $\Delta Q$ values (potentiation).
    *   The lower-right corner (high $Yb$, low $Q_e$) is colored in shades of purple, indicating negative $\Delta Q$ values (depression).
    *   The transition between these colors is smooth, suggesting a continuous relationship between the input variables and the resulting weight change.

### Contextual Integration (Based on Caption)
The caption identifies this figure as illustrating the "Homeostatic plasticity rule for Q weights." The schematic diagrams (LTP/LTD) represent the outcome of this plasticity, while the heatmap likely visualizes how the difference between signals through $Q$ and $Y$ (as mentioned in the caption) dictates the direction and magnitude of synaptic plasticity ($\Delta Q$).

> Figure caption (from PDF text): Figure 1: Bursting cortico-cortical networks (BurstCCN) for credit assignment through bursting
activity. (A) Network schematic consisting of neuron ensembles and connection-type-specific STP.
Events from the input are propagated forward through short-term depressing (STD) connections, W.
Output event rates are compared to a target value which generates a teaching signal that is presented
to the output layer apical dendrites. This acts as an error signal and appears as a deflection in the
dendritic potential from its resting potential which causes changes to bursting activity from its baseline.
The error-carrying bursting signals are propagated back through short-term facilitating connections,
Y, which we interpret as being communicated by populations of dendrite-targeting interneurons.
Events are also propagated backwards via STD connections, Q, to provide a means of cancelling
baseline bursting activity. The difference in activity from these two feedback connections results in
changes to dendritic excitability that lead to burst-dependent synaptic plasticity. (B) Burst-dependent
plasticity rule. Simple setup of a single connection between a pre- and post-synaptic cell that are both
modelled with Poisson spike trains with equal rates. As the firing rates increase, (top) plasticity of the
synaptic weight switches from long-term depression (LTD) to long-term potentiation (LTP) (middle)
when the burst probability increases above the baseline value. (bottom) The magnitude of the weight
change is scaled by the event rate. (C) Homeostatic plasticity rule for Q weights. The difference
between the signals through Q and Y dictates the direction and magnitude of synaptic plasticity.

## 

denotes the element-wise product, pb

L represents the baseline burst probability in the absence of
any teaching signal and h(el) = f ′(vl) ⊙e−1

l
. These burst probabilities are used at the output
layer (l = L) to compute the burst rates as bl = el ⊙pl which are decoded and sent backwards to
layer l −1 apical dendrites by a set of short-term facilitating (STF) feedback weights, Yl−1. The
STF feedback weights and STD feedforward weights are similarly used in Burstprop. However, the
BurstCCN additionally includes a novel set of apical dendrite-targeting STD feedback weights, Ql−1,
which send event rates backwards. We interpret the STF feedback connections as being provided
via a type of dendrite-targeting interneuron and STD feedback as direct connections in line with
recent experimental studies [12-17]. The signals through both sets of feedback weights lead to the
apical potentials in the previous layer, ul−1 = Ql−1el −Yl−1bl. These determine the layer's burst
probabilities which are computed as pl−1 = ¯σ(ul−1 ⊙h(el−1)) where ¯σ denotes the sigmoid
function, σ, with scaling and offset parameters, ¯σ(x) = σ(αx + β) ([10]; see SM, Section B). The
same process is repeated backwards for each layer until the input layer to obtain their dendritic
potentials and burst probabilities. Note that for all experiments, we set α = 4 (and β = 0) to prevent
this function from implicitly scaling down the errors propagating backwards through each layer by a
factor of 4 (since dσ

dx ≈1

4 around x = 0).

After the error information has been propagated backwards, feedforward synaptic weight changes are
computed using a burst-dependent synaptic plasticity rule:

∆Wl = η(W)

l
((pl −pb

l) ⊙el) eT

l−1
(1)

where η(W) is a learning rate and ·T is the transpose operation. Importantly, the learning rule
depends on the change in burst probability from the predefined layer-wise baseline burst probability,
pb

l = pb

l(1, . . . , 1)T , which represents the signed error signal required for backprop-like learning.
Consequently, when we make both pre- and postsynaptic cells fire following Poisson statistics we
obtain long-term depression and long-term potentiation for low and high firing rates, respectively
(Fig. 1B). This is in line with a large number of experimental studies of cortical synapses [18, 19].
It can be shown that the updates produced by this learning rule approximate those obtained by the
backpropagation algorithm in the weak-feedback case (see Section 3.3.1 and SM, Section B).

In the absence of a teaching signal, it is important for pyramidal ensembles to produce a baseline
level of bursting such that no weight changes occur (cf. Eq. 1). This holds true for the output layer
as there are no other inputs onto the apical dendrites. However, for the hidden layers the event rate
signals through Q and the burst rate signals through Y need to exactly cancel each other out such that
the apical dendritic potentials are at rest (i.e. u = 0). For any Y weights, there is always an optimal
set of Q weights that will produce this exact cancellation regardless of the event rates propagating
through the network. Specifically, they must be set as Ql = pb

lYl which we refer to as the weights
being in a Q-Y symmetric state. However, it is not biologically plausible for the Q synapses to have
direct knowledge of Y. Therefore, inspired by earlier work [6, 20], we use a learning rule for Q to
provide this cancellation:

∆Ql = −η(Q)

l
ul eT

l+1
(2)
which explicitly aims to silence the apical potentials (Fig. 1C). In the absence of a teaching signal
at the output layer, all Q weights will eventually converge to their optimal values and achieve a
symmetric state under reasonable assumptions (see SM, Section B.2). Note that we could similarly
have added this learning rule on the Y feedback weights to cancel the activity through the Q weights,
which produces similar results (Fig. S1).

When teaching signals are applied at the output layer, it is important to note that only the bursting
activity propagated through the Y connections changes because the event rates through Q are
unaffected by the dendritic activity. This enables single-phase learning as the symmetry in the two
feedback connection types (Q and Y) can be exploited to directly compare without teacher signals
(i.e. at baseline) to with teacher signals.

Details of the continuous time implementation can be found in the Supplementary Materials.

2.3
Spiking BurstCCN

For our spiking implementation of the BurstCCN, we adapted the burst-dependent synaptic plasticity
rule in Equation 1 (see SM, Eq. 12). Unlike the two rate-based implementations, the spiking
BurstCCN more accurately models the internal neuron spiking dynamics instead of abstracting these

---

## 

Figure 2: Spiking BurstCCN does not require multi-phase learning to solve the XOR classifi-
cation task. Schematic of the (A) two-phase and (B) single-phase learning settings. (A) For each
input during two-phase learning, networks are given a 7.2s prediction period during which teaching
signals and plasticity are turned OFF, followed by a 0.8s learning period where both teaching signals
and plasticity are turned back ON. (B) During single-phase learning, both the teaching signals and
plasticity remain ON throughout training. (C, D) Top: event rate (e) of the output layer. Middle: burst
probability (p) for the output layer and the baseline or moving average of the burst probability (pb or
¯p) for BurstCCN and Burstprop, respectively. Bottom: the resulting weight updates for connections
from hidden layer neurons. Model results represent mean ± standard error (n = 5).

> Figure caption (from PDF text): Figure 2: Spiking BurstCCN does not require multi-phase learning to solve the XOR classifi-
cation task. Schematic of the (A) two-phase and (B) single-phase learning settings. (A) For each
input during two-phase learning, networks are given a 7.2s prediction period during which teaching
signals and plasticity are turned OFF, followed by a 0.8s learning period where both teaching signals
and plasticity are turned back ON. (B) During single-phase learning, both the teaching signals and
plasticity remain ON throughout training. (C, D) Top: event rate (e) of the output layer. Middle: burst
probability (p) for the output layer and the baseline or moving average of the burst probability (pb or
¯p) for BurstCCN and Burstprop, respectively. Bottom: the resulting weight updates for connections
from hidden layer neurons. Model results represent mean ± standard error (n = 5).

This figure, labeled with the letter 'C' and implicitly comparing against a panel 'D', presents comparative plots detailing the performance metrics of two models: **Burstprop** and **BurstCCN**. The figure is structured into three rows of plots, with two columns corresponding to the two models.

### Detailed Component Analysis (Panel C - Burstprop)

**Top Plot (Event Rate):**
*   **Y-axis:** Labeled "Event rate [Hz]", ranging from 0 to 10.
*   **X-axis:** Represents time or input sequence, marked with discrete labels: $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** A line graph shows the event rate. The rate starts low (around 4-5 Hz), increases sharply during the first input segment $(\theta, \emptyset)$ to a peak near 8-9 Hz, remains high during the second segment $(\theta, 1)$, and then drops sharply towards a low level (around 3-4 Hz) during the final segment $(1, 1)$. Vertical dashed pink lines delineate transitions between these input segments.

**Middle Plot (Burst Probability):**
*   **Y-axis:** Labeled "Burst probability", ranging from 0.2 to 0.5.
*   **X-axis:** Corresponds to the input segments $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** Two curves are plotted:
    *   $\bar{p}$ (Baseline/Moving Average): Represented by an orange line, showing a relatively stable baseline around 0.4 across the segments.
    *   $p$: Represented by a dark red line, showing a dip below the baseline during $(\theta, \emptyset)$ and $(\theta, 1)$, followed by a slight recovery or stabilization in $(1, 1)$.

**Bottom Plot (Weight Updates $\Delta W$):**
*   **Y-axis:** Labeled "$\Delta W$", ranging from -2.5 to 2.5.
*   **X-axis:** Corresponds to the input segments $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** Two lines represent weight updates from hidden layer neurons:
    *   $W_{\text{hid1}}$ (Purple line): Shows a significant positive spike during $(\theta, 1)$ and a negative value during $(\theta, \emptyset)$.
    *   $W_{\text{hid2}}$ (Green line): Shows a strong positive spike during $(\theta, 1)$ and a negative value during $(\theta, \emptyset)$.

### Detailed Component Analysis (Panel D - BurstCCN)

**Top Plot (Event Rate):**
*   **Y-axis:** Labeled "Event rate [Hz]", ranging from 0 to 10.
*   **X-axis:** Corresponds to the input segments $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** A line graph shows the event rate. The rate starts low (around 3-4 Hz), increases sharply during $(\theta, \emptyset)$ to a high level (near 9-10 Hz), remains high during $(\theta, 1)$, and then drops sharply to a low level (around 3-4 Hz) during $(1, 1)$. Vertical dashed pink lines delineate transitions.

**Middle Plot (Burst Probability):**
*   **Y-axis:** Labeled "Burst probability", ranging from 0.2 to 0.5.
*   **X-axis:** Corresponds to the input segments $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** Two curves are plotted:
    *   $\bar{p}$ (Baseline/Moving Average): Represented by a light orange line, showing a relatively stable baseline around 0.4 across the segments.
    *   $p$: Represented by a dark red line, which remains relatively close to the baseline $\bar{p}$ across all segments.

**Bottom Plot (Weight Updates $\Delta W$):**
*   **Y-axis:** Labeled "$\Delta W$", ranging from -2.5 to 2.5.
*   **X-axis:** Corresponds to the input segments $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$.
*   **Data:** Two lines represent weight updates from hidden layer neurons:
    *   $W_{\text{hid1}}$ (Purple line): Shows a small negative value during $(\theta, \emptyset)$, followed by a positive spike during $(\theta, 1)$.
    *   $W_{\text{hid2}}$ (Green line): Shows a small negative value during $(\theta, \emptyset)$, followed by a positive spike during $(\theta, 1)$.

### Summary of Notations and Legends
*   **Variables:** $e$ (Event rate), $p$ (Burst probability for the output layer), $\bar{p}$ (Baseline/Moving average of burst probability).
*   **Weight Updates:** $\Delta W$ represents the change in weights. $W_{\text{hid1}}$ and $W_{\text{hid2}}$ denote the weight updates originating from hidden layer neurons 1 and 2, respectively.
*   **Input Segments:** The x-axis labels $(\theta, \emptyset)$, $(\theta, 1)$, and $(1, 1)$ denote specific input conditions or phases of the task.
*   **Color Coding:** Purple and Green lines denote $W_{\text{hid1}}$ and $W_{\text{hid2}}$, respectively, in the $\Delta W$ plots. Orange and Dark Red lines denote $\bar{p}$ and $p$, respectively, in the middle plots.

> Figure caption (from PDF text): Figure 2: Spiking BurstCCN does not require multi-phase learning to solve the XOR classifi-
cation task. Schematic of the (A) two-phase and (B) single-phase learning settings. (A) For each
input during two-phase learning, networks are given a 7.2s prediction period during which teaching
signals and plasticity are turned OFF, followed by a 0.8s learning period where both teaching signals
and plasticity are turned back ON. (B) During single-phase learning, both the teaching signals and
plasticity remain ON throughout training. (C, D) Top: event rate (e) of the output layer. Middle: burst
probability (p) for the output layer and the baseline or moving average of the burst probability (pb or
¯p) for BurstCCN and Burstprop, respectively. Bottom: the resulting weight updates for connections
from hidden layer neurons. Model results represent mean ± standard error (n = 5).

This figure, labeled **D**, presents a set of comparative plots illustrating the performance metrics for two models: "Burstprop" and "BurstCCN." The figure is structured as a $3 \times 2$ grid of time-series plots, comparing the two models across three different metrics.

## 

multiple levels. To demonstrate that our model can perform single-phase learning, we trained the
spiking version of our model on the XOR classification task and contrasted it with Burstprop, which
requires a two-phase learning process (Fig. 2). In both single- and two-phase learning regimes, the
input stimulus is presented for a total of 8s before the next example is shown. The two-phase learning
regime has an initial prediction phase, lasting 7.2s for each input presentation, where plasticity is
switched off throughout the network and the output neurons do not receive any teaching signals
(Fig. 2A). This is followed by a teacher phase for the remaining 0.8s where plasticity is restored and
teaching signals are delivered at the output. The single-phase regime removes the initial prediction
phase and extends the teacher phase to the full duration of the input stimulus (Fig. 2B).

Our results show that both models were capable of successfully learning the task in the two-phase
regime as indicated by the high output event rates in response to the (0, 1) and (1, 0) inputs and low
event rates for the (0, 0) and (1, 1) inputs (Fig. 2C). However, when training in the single-phase
regime, only BurstCCN was able to learn the task (Fig. 2D). The inability of Burstprop to learn the
task can be explained by comparing the moving average of the burst probability (p) with the actual
burst probability (p) which determines the sign of synaptic weight updates (Fig. 2D). Burstprop failed
to learn in the single-phase learning setup due to the teaching signal remaining on and preventing p
from being able to provide a stable representation of the without-teacher burst probability.

3.2
BurstCCN can learn with dynamic input-output

Typically, studies that have attempted to solve the credit assignment problem with biologically
plausible implementations of backprop make an implicit assumption that during learning there is
a period where the continuous-time input stream is fixed [6, 10]. This is required in most cases
to allow the network to stabilise its activities before learning can take place. With single-phase
learning, we can relax this assumption to enable learning in conditions where the inputs and their
corresponding teaching signals are dynamically changing over time. We assessed this ability by
training the continuous-time BurstCCN (see SM, Section A.1) on an online non-linear regression
task (Fig. 3). This task consisted of three sinusoidal inputs, xi(t) = sin(αit + βi), with random
frequencies αi ∼U(0, π

2 ) and phase offsets βi ∼U(0, 2π) (Fig. 3A). The network had a single
output unit for which a non-trivial target was obtained by passing the same inputs to a 3-25-1 artificial
neural network (ANN). This approximates a setting in which a given cortical area learns to regress
its input onto the activity of another cortical area. The ANN weights were randomly initialised
with w1

ij ∼U(−

√

3,
√

3) for the first layer and w2
ij ∼U(−0.6, 0.6) for the second layer. Despite
the BurstCCN initially producing outputs that were significantly different to the target (Fig. 3C),
the results show that over training it learned to produce output patterns that closely matched the
non-linear and dynamic target (Fig. 3B,D). This highlights that the BurstCCN is capable of adequately
backpropagating useful error signals when both inputs and teaching signals are constantly changing.

3.3
Feedback plasticity rule facilitates alignment to backprop updates

Next, we wanted to understand how well our model approximates backprop. As stated above, the
purpose of the learning rule for the feedback STD Q connections (Eq. 2) is to silence the apical
compartments in every ensemble by cancelling activity through the feedback STF Y connections.
When a teaching signal is applied, this becomes important for computing the correct local error signal
that is used for learning and backpropagated to previous layers. Here, we show both analytically and
empirically using the discrete version of the model how the computed errors relate to backprop.

3.3.1
BurstCCN with weak feedback approximates backpropagation algorithm

Under some small assumptions, we analytically show that the feedback pathway of BurstCCN is
approximately communicating the same error gradients that are computed by backprop. Specifically,
we assume that the feedback weights are optimally aligned (i.e. Ql = pb

lYl) and focus on the change
in burst rate, δbl := (pl −pb

l) ⊙el. If we let Etask = ||eL −etarget||2 define the task error
then, by construction, the change in burst rate at the output layer is equivalent to the negative error
gradient, δbL = −∂Etask

∂vL . For the hidden layers, we derive the following iterative relationship (see
SM, Section B):

δbl = f ′ (vl) ⊙(−Yl)δbl+1 + O(u3

l ).
(3)

---

## 

D

Figure 3: BurstCCN can learn a dynamic non-linear regression task. (A) Schematic of the task.
Three sinusoidal waves with random frequencies are given as inputs. The task is to learn to match
the target pattern which is obtained by passing the same inputs through a fixed, randomly initialised
ANN. (B) Learning curve for the (continuous-time) BurstCCN. (C, D) Example output traces for (C)
before and (D) after training. Model results represent mean ± standard error (n = 5).

> Figure caption (from PDF text): Figure 3: BurstCCN can learn a dynamic non-linear regression task. (A) Schematic of the task.
Three sinusoidal waves with random frequencies are given as inputs. The task is to learn to match
the target pattern which is obtained by passing the same inputs through a fixed, randomly initialised
ANN. (B) Learning curve for the (continuous-time) BurstCCN. (C, D) Example output traces for (C)
before and (D) after training. Model results represent mean ± standard error (n = 5).

## 

with
teacher

without
teacher

symmetric only
random only

symmetric only
random only

feedback weights:

Figure 4: Feedback learning rule enables a close alignment with backprop and feedback
alignment. The network is a randomly initialised 5-layer discrete-time BurstCCN with random (solid
line) or symmetric (dashed line), fixed W and Y weights. The Q weights are updated in the presence
of (A-D) no teaching signal or (E-H) a teaching signal. (A,E) Alignment between Q and Y weights,
(B,F) the mean absolute value of the apical potentials, (C,G) the alignment to backprop (BP) and
(D,H) feedback alignment (FA) as the Q weights learn to silence apical dendrite potential. Updates
below 90◦marked by the black dashed line are considered useful as they still follow the direction of
backprop on average. Model results represent mean ± standard error (n = 5).

> Figure caption (from PDF text): Figure 4: Feedback learning rule enables a close alignment with backprop and feedback
alignment. The network is a randomly initialised 5-layer discrete-time BurstCCN with random (solid
line) or symmetric (dashed line), fixed W and Y weights. The Q weights are updated in the presence
of (A-D) no teaching signal or (E-H) a teaching signal. (A,E) Alignment between Q and Y weights,
(B,F) the mean absolute value of the apical potentials, (C,G) the alignment to backprop (BP) and
(D,H) feedback alignment (FA) as the Q weights learn to silence apical dendrite potential. Updates
below 90◦marked by the black dashed line are considered useful as they still follow the direction of
backprop on average. Model results represent mean ± standard error (n = 5).

This figure, titled "Figure 4: Feedback learning rule enables a close alignment with backprop and feedback alignment," consists of eight subplots arranged in a $2 \times 4$ grid (Panels A through H). All subplots are line graphs tracking a metric over the number of iterations.

**Overall Layout and Structure:**
The figure is divided into two main rows: the top row (Panels A, B, C, D) and the bottom row (Panels E, F, G, H). The columns represent different conditions:
*   **Column 1 (A & E):** QY alignment.
*   **Column 2 (B & F):** Mean apical potential.
*   **Column 3 (C & G):** Alignment to Backpropagation (BP).
*   **Column 4 (D & H):** Feedback Alignment (FA).

The top row (A-D) represents the scenario "no teaching signal," while the bottom row (E-H) represents the scenario "a teaching signal."

**Visual Components and Legends:**
Each subplot contains two distinct lines representing different weight update schemes:
1.  **Random Weights:** Represented by a **solid line**.
2.  **Symmetric Weights:** Represented by a **dashed line**.

A critical annotation is present in Panels C and G: A **black dashed horizontal line** is drawn across the plots, labeled with a value (implied to be $90^\circ$ based on the caption). The caption specifies that updates below this line are considered useful as they still follow the direction of backprop on average.

**Axis Labels and Variables:**
*   **X-axis (Horizontal):** Labeled "Iterations ($\times 10^3$)" in Panels C and G, indicating the progression of learning over thousands of iterations. The range appears to span from 0 to 15 on the scale shown in C and G.
*   **Y-axis (Vertical):** The specific label varies by panel:
    *   Panels A & E: "QY alignment" (ranging from 0 to 100).
    *   Panels B & F: "Mean |apical potential|" (ranging from 0.0 to 0.6).
    *   Panels C & G: "Alignment to BP" (ranging from 0 to 100).
    *   Panels D & H: "Alignment to FA" (ranging from 0 to 100).

**Data Trends and Details:**

**Top Row (No Teaching Signal):**
*   **Panel A (QY alignment):** Both the solid (random) and dashed (symmetric) lines start near 100% alignment and rapidly decrease, leveling off at a low value (around 20-30%) as iterations increase.
*   **Panel B (Mean |apical potential|):** Both lines start high (near 0.6) and decrease sharply, approaching zero as iterations increase.
*   **Panel C (Alignment to BP):** Both lines start near 100%. They decrease rapidly, crossing below the black dashed line (implied $90^\circ$) relatively early on. The solid and dashed lines track very closely, converging to a low alignment value (around 20-30%).
*   **Panel D (Alignment to FA):** Both lines start near 100% and decrease, leveling off at a low value (around 20-30%).

**Bottom Row (With Teaching Signal):**
*   **Panel E (QY alignment):** Similar to Panel A, both lines start high and decrease, leveling off at a low value.
*   **Panel F (Mean |apical potential|):** Similar to Panel B, both lines start high and decrease sharply toward zero.
*   **Panel G (Alignment to BP):** Both lines start near 100%. They decrease, but the solid (random) and dashed (symmetric) lines remain very close to each other. They appear to track closely below the black dashed line, converging to a low alignment value (around 30-40%).
*   **Panel H (Alignment to FA):** Both lines start high and decrease, leveling off at a low value, similar in trend to Panel D.

**Contextual Interpretation (Based on Caption):**
The figure illustrates the performance of a "randomly initialised 5-layer discrete-time BurstCCN." The comparison between the top row (no teaching signal) and the bottom row (with a teaching signal) demonstrates how the learning rule affects alignment metrics. The caption specifies that Q weights are updated in these scenarios, and the goal is for the network to learn to "silence apical dendrite potential" (as seen in Panels B and F).

alignment angle to both backprop and feedback alignment eventually became very small which
supports our analytical results that show our model approximates these methods (Fig. 4C-D). Despite
producing less aligned feedforward updates in the presence of a teaching signal, the updates computed
were still informative since they were consistently well below 90◦of the direction of steepest descent
(Fig. 4G).

3.4
BurstCCN learns image classification tasks with multiple hidden layers

3.4.1
MNIST

Figure 5: BurstCCN learns to classify handwritten digits (MNIST) with deep networks. (A)
Learning curve of 5-layer ANN (black), BurstCCN (blue), BurstCCN (η(Q) = 0) (light blue),
Burstprop (red) and EDN (green). (B) Test error with different numbers of hidden layers for all
models. (C) Alignment to backprop (BP) over time for all 5-layer models. (D) Alignment to
backprop with different numbers of hidden layers for all models. The black circle indicates that
the hyperparameters for each model were optimised for 5-layer networks. Model results represent
mean ± standard error (n = 5).

> Figure caption (from PDF text): Figure 5: BurstCCN learns to classify handwritten digits (MNIST) with deep networks. (A)
Learning curve of 5-layer ANN (black), BurstCCN (blue), BurstCCN (η(Q) = 0) (light blue),
Burstprop (red) and EDN (green). (B) Test error with different numbers of hidden layers for all
models. (C) Alignment to backprop (BP) over time for all 5-layer models. (D) Alignment to
backprop with different numbers of hidden layers for all models. The black circle indicates that
the hyperparameters for each model were optimised for 5-layer networks. Model results represent
mean ± standard error (n = 5).

This figure, titled "Figure 5," presents four distinct panels (A, B, C, and D) illustrating the performance of different deep learning models on classifying handwritten digits (MNIST). All panels utilize line graphs to depict model performance metrics.

## 

weights (i.e. feedback alignment [4]; see Fig. S2 for symmetric feedback weight case) with the
remaining connection types of the different models updated using their respective plasticity rules. We
also tested the BurstCCN in its idealised case where the feedback STD weights (Q) were fixed in the
Q-Y symmetric state (see Section 2.2). We denote this model as "BurstCCN (Q-Y sym)".

Using 5-layer networks, the BurstCCN obtained a test error of 1.84±0.01%, comparable to that of
Burstprop with 1.75±0.01% and significantly outperforming the EDN with 10.65±0.09% (Fig. 5A).
As the network depth was increased, both BurstCCN and Burstprop retained high performances but
the EDN showed a substantial decay in performance with deeper networks (Fig. 5B). In an idealised
case for the EDN, the disparity in performance and the effect of depth is less evident (Fig. S3).
We then compared the alignment between the models and backprop. For the 5-layer networks,
Burstprop's updates were most closely aligned to backprop, followed by the two BurstCCN models
which all vastly outperformed the EDN (Fig. 5C). As expected, the BurstCCN with Q-Y symmetry
could better propagate error signals. By increasing the network depth, we demonstrate that it was
more difficult to produce updates that were closely aligned to backprop. However, we show that
the BurstCCN was still capable of backpropagating useful error signals in relatively deep networks
(Fig. 5D).

3.4.2
CIFAR-10

input
convolutional

layers

fully-connected

layers

Q

W

Y

feedback weights:

Figure 6: BurstCCN with convolutional layers learns to solve natural image classification
task (CIFAR-10). (A) Schematic of BurstCCN architecture consisting of an input layer, three
convolutional layers, a fully-connected hidden layer and output layer. For the BurstCCN, each layer
was connected with a set of feedforward weights, W, and feedback weights, Y and Q. (B) Learning
curve and (C) alignment to backprop of the different models with random (solid lines) and symmetric
(dashed lines) feedback weight regimes. Model results represent mean ± standard error (n = 5).

> Figure caption (from PDF text): Figure 6: BurstCCN with convolutional layers learns to solve natural image classification
task (CIFAR-10). (A) Schematic of BurstCCN architecture consisting of an input layer, three
convolutional layers, a fully-connected hidden layer and output layer. For the BurstCCN, each layer
was connected with a set of feedforward weights, W, and feedback weights, Y and Q. (B) Learning
curve and (C) alignment to backprop of the different models with random (solid lines) and symmetric
(dashed lines) feedback weight regimes. Model results represent mean ± standard error (n = 5).

This figure, labeled as Figure 6 in the source material, is divided into three conceptual parts: Panel A (a schematic diagram), and Panels B and C (learning curves, though only Panel B is fully visible in the provided image).

## 

again, obtained a similar error to the symmetric ANN (22.62±0.10%) and Burstprop (24.15±0.17%)
models. In the symmetric setups, there was a large improvement in the alignment angles to backprop
compared to the random feedback setup (Fig. 6C). This suggests that they were backpropagating
errors more effectively which likely explains the increase in performance. However, as seen within
the random feedback setups, an improvement in this alignment does not guarantee an improvement to
performance. This is because each model will traverse a different learning trajectory and converge to
a different local minimum but the alignment angle remains a good indicator of expected performance.

Conclusions and discussion

We have introduced a new model capable of backprop-like credit assignment by integrating known
properties of cortical networks. We have shown that by combining specific biological mechanisms
such as bursting, STP and dendrite-targeting inhibition it is possible to construct a model that learns
effectively in a continuous setting that is reminiscent of learning in the brain. Moreover, we have
demonstrated that such a model can learn complex image classification tasks with deep networks.

Our model proposes specific STP dynamics on the feedforward and feedback connections. It requires
STD on cortico-cortical projections onto pyramidal cells in line with experimental evidence [12-16].
In addition, it suggests a key role for dendrite-targeting interneurons such as SST-positive Martinotti
cells in the feedback pathway. There is evidence that these interneurons receive STF top-down
connections whereas top-down projections onto pyramidal cells exhibit STD dynamics as required by
our model [12-17]. In future work, it would be interesting to model the specific neuron types for
each connection to satisfy Dale's law and further increase biological plausibility.

A prediction from our model is that manipulations of interneurons with STF connections would lead
to disruptions in burst decoding from the layer (brain area) above thereby obstructing learning in the
brain area below. Additionally, as error signals alter the level of bursting in the network, the model
predicts that the variance in bursting activity and the distal dendritic potentials would correlate with
the severity of errors made by the network during learning.

Although our model captures a wide range of biological features, some biological implausibilities re-
main. Currently, we use feedback alignment to provide a solution to the weight transport problem [23]
but this has a substantial impact on performance, particularly in more challenging tasks. Therefore,
it would be important to explore some of the recently introduced plausible feedback learning rules
[24-26] which could be used in conjunction with our proposed learning rules to outperform feedback
alignment [4].

Overall, our work provides a novel solution to the credit assignment problem and suggests that a
range of cortical features from sub-cellular to the systems level jointly underlie single-phase, efficient
deep learning in the brain.

Acknowledgments and Disclosure of Funding

The authors would like to thank Alexandre Payeur, Jordan Guerguiev, Blake Richards, Richard Naud,
Kevin Nejad, Jesper Sjostrom, Paul Anastasiades, Joao Sacramento, Adil Khan and Jasper Poort
for useful discussions. This work made use of the supercomputer BluePebble. We would also like
to thank Callum Wright and the rest of the High Performance Computing team at the University
of Bristol for constant and quick help with BluePebble. This work has been supported by two
EPSRC Doctoral Training Partnership PhD studentships to Will Greedy and Joseph Pemberton and a
Wellcome Trust Neural Dynamics PhD studentship to Heng Wei Zhu.

---

##