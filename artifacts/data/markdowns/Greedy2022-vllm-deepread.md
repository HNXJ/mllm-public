## Page 1

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

## Page 2

1
Introduction

For effective learning, synaptic modifications throughout the brain should result in improved be-
havioural function. This requires a process by which credit should be assigned to synapses given their
contribution to behavioural output [1–3]. In multilayer networks, credit assignment is particularly
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
task. Next, we show both empirically and analytically that our model’s dynamics result in learning
that approximately follows backprop-derived gradients. Finally, we use a simplified discrete-time
BurstCCN implementation to demonstrate that the model achieves good performance on non-trivial
image classification tasks (MNIST and CIFAR-10), even in the presence of random feedback synaptic
weights.

2
Bursting Cortico-Cortical Networks

2.1
Burst Ensemble Multiplexing

Burst Ensemble Multiplexing (BEM) [11] refers to the idea that ensembles of cortical neurons are
capable of simultaneously representing multiple distinct signals within the patterns of their spiking
activity. Typically, pyramidal cells receive top-down and bottom-up signals into their apical and basal
dendrites, respectively. Bottom-up basal inputs affect the rate of spiking and top-down apical inputs
convert these somatically induced spikes into high-frequency bursts. Postsynaptic populations can
then use STP to decode these distinct signals from the overall spiking activity.

2


---

## Page 3

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
> Figure description (generated): ## Figure Description

This figure, labeled with the letter 'C', presents a schematic representation of plasticity rules and associated data plots related to bursting cortico-cortical networks (BurstCCN).

### Panel C: Plasticity Schematics and Heatmap

The panel is divided into two main sections: a schematic diagram illustrating plasticity rules (top) and a 2D heatmap plot (bottom).

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
> Figure description (generated): This figure presents a schematic representation of Bursting Cortico-Cortical Networks (BurstCCN) designed for credit assignment through bursting activity, structured across multiple layers.

### 1. Overall Layout & Structure
The figure is primarily a multi-layered neural circuit schematic, organized vertically into distinct layers. The main structure appears to be Panel (A), which illustrates the network flow, with references to subsequent panels (B) and (C) in the caption suggesting further detailed mechanisms.

### 2. Visual Components & Symbols
**Layers:** The network is divided into three main horizontal layers:
*   **Layer $\theta$ (input):** The bottom layer, representing the input stage.
*   **Layer 1 (hidden):** The middle layer, acting as an intermediate processing stage.
*   **Layer 2 (output):** The top layer, where the final output is generated.

**Neurons/Ensembles:** Each layer contains multiple stylized neuron ensembles, represented by groups of gray, cone-shaped icons (representing neurons).

**Connections and Synaptic Types:** Connections between layers are depicted by curved lines, color-coded to indicate the type of Short-Term Plasticity (STP):
*   **Blue lines:** Represent connections associated with **short-term depression (STD)**, indicated by the legend.
*   **Orange/Yellow lines:** Represent connections associated with **short-term facilitation**, indicated by the legend.

**Flow and Targets:**
*   Input events propagate forward from Layer $\theta$ through connections to Layer 1, and then further up to Layer 2.
*   In Layer 2, there is a specific node labeled **"target"** (a red diamond shape) connected to the output neurons.
*   An arrow labeled **"teacher"** points from this "target" node towards the output neurons in Layer 2, indicating a teaching or error signal.
*   The overall flow suggests forward propagation from input to output, followed by a feedback mechanism involving the target.

**Feedback Loops:**
*   The caption describes backward propagation: "Events are also propagated backwards via STD connections, Q." This is visually suggested by blue lines potentially looping back from higher layers.
*   The caption mentions feedback through facilitating connections, Y: "The error-carrying bursting signals are propagated back through short-term facilitating connections, Y." This is visually suggested by orange/yellow lines looping backward.

**Dendritic Signaling:**
*   The caption mentions that the error signal causes a "deflection in the dendritic potential from its resting potential." This is conceptually linked to the interaction between the target signal and the output layer.

### 3. Labels, Keys & Legends
**Layer Labels:**
*   "layer $\theta$ (input)"
*   "layer 1 (hidden)"
*   "layer 2 (output)"

**Connection/Signal Labels:**
*   "teacher" (pointing to the target node)
*   "target" (red diamond shape in Layer 2)
*   "output" (label near the output neurons in Layer 2)

**Legend/Color Key:**
*   $\text{Blue square icon}$: "short-term depression (events)"
*   $\text{Orange/Yellow square icon}$: "short-term facilitation (bursts)"

### 4. Data Trends & Details
No quantitative plots or axes are visible in the main schematic (Panel A). The figure is a qualitative circuit diagram.

### 5. Contextual Caption Integration
The caption clarifies the function of the elements:
*   **Forward Propagation:** Input events move forward through **STD connections (W)**. Output event rates are compared to a target value, generating a teaching signal presented to the output layer apical dendrites.
*   **Error Signal:** This teaching signal acts as an error signal, causing changes to bursting activity.
*   **Backward Propagation (Facilitation):** Error-carrying signals propagate back through **short-term facilitating connections (Y)**, interpreted as communication by dendrite-targeting interneurons.
*   **Backward Propagation (Depression):** Events also propagate backward via **STD connections (Q)** to cancel baseline bursting activity.
*   **Plasticity:** The difference between signals through Q and Y dictates the direction/magnitude of synaptic plasticity, leading to burst-dependent synaptic plasticity.

*(Note: Panels B and C mentioned in the caption describe specific rules—Burst-dependent plasticity rule and Homeostatic plasticity rule for Q weights, respectively—which are not visually present in the provided schematic excerpt.)*

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
> Figure description (generated): This image displays a schematic diagram, specifically Panel B from Figure 1, illustrating "Bursting cortico-cortical networks (BurstCCN) for credit assignment through bursting activity."

### 1. Overall Layout & Structure
The visual content is contained within a large, dashed-line rectangular boundary representing the network structure. The diagram depicts a multi-layered neural circuit schematic, organized vertically into distinct layers labeled "Layer 1" and "Layer 2." The structure shows forward propagation of signals from lower layers to higher layers, alongside complex feedback loops.

### 2. Visual Components & Symbols
**Layers and Neurons:**
*   The network is divided into two main layers: **Layer 1** (at the bottom) and **Layer 2** (at the top).
*   Neurons are represented by stylized, gray, inverted teardrop or cone shapes. These neurons appear to be organized in ensembles within each layer.
*   Specific nodes are highlighted: $V_1$ is a neuron in Layer 1, and $V_2$ is a neuron in Layer 2.
*   An intermediate region, highlighted by a dashed orange-pink box, is labeled **IN** (likely representing input or integration).

**Connections and Signals:**
*   **Forward Propagation:** Connections flow generally upwards from Layer 1 to Layer 2.
    *   Connections originating from $V_1$ (Layer 1) project upwards to neurons in Layer 2.
    *   The connection from $V_1$ to the IN region is labeled with a weight parameter, $\mathbf{w}_2$.
    *   The connection from $V_1$ to the neurons in Layer 2 is labeled with $\mathbf{w}_1$.
*   **Feedback Loops:** Two distinct feedback pathways are shown:
    *   **Path Q (STD Connections):** A thick, dark blue line labeled $\mathbf{Q}_1$ originates from a neuron in Layer 2 and curves downwards, connecting back towards the lower layers. The caption identifies these as Short-Term Depressing (STD) connections used for cancelling baseline activity.
    *   **Path Y (Facilitating Connections):** A thinner, light blue line labeled $\mathbf{Y}_1$ originates from the IN region and curves upwards/sideways, connecting back towards neurons in Layer 2. The caption identifies these as Short-Term Facilitating connections, interpreted as being communicated by dendrite-targeting interneurons.
*   **Input/Output:** The diagram implies an input stream feeding into the system, as indicated by the general flow towards Layer 1 neurons. The output signal is implied to be related to the comparison of event rates against a target value, as described in the caption.

### 3. Labels, Keys & Legends
**Variables and Annotations:**
*   $\mathbf{V}_1$: Neuron in Layer 1.
*   $\mathbf{V}_2$: Neuron in Layer 2.
*   **IN**: A central processing region, highlighted in orange/pink.
*   $\mathbf{w}_1$: Synaptic weight parameter connecting Layer 1 to Layer 2.
*   $\mathbf{w}_2$: Synaptic weight parameter connecting $V_1$ to the IN region.
*   $\mathbf{Q}_1$: Label for a feedback connection (STD).
*   $\mathbf{Y}_1$: Label for a feedback connection (Facilitating).

**Layer Labels:**
*   "Layer 1" is marked at the bottom.
*   "Layer 2" is marked above Layer 1.

### 4. Data Trends & Details
Since this panel is a schematic circuit diagram and not a plot, there are no axes or quantitative data trends to describe. The visual representation focuses on connectivity and signal flow rather than dynamic changes over time or rate.

### 5. Contextual Caption Integration
The caption clarifies the function of the elements shown:
*   **Forward Flow:** Events propagate forward through STD connections ($\mathbf{W}$ is mentioned in the caption, corresponding to $\mathbf{w}_1$ and $\mathbf{w}_2$).
*   **Error Signal:** Output event rates are compared to a target, generating an error signal that affects dendritic potential and bursting activity.
*   **Feedback Loops:** The error-carrying signals propagate back through facilitating connections ($\mathbf{Y}$), interpreted as interneuron communication. STD connections ($\mathbf{Q}$) propagate backward to cancel baseline activity.
*   **Plasticity:** The difference between signals through $\mathbf{Q}$ and $\mathbf{Y}$ dictates the direction and magnitude of synaptic plasticity, leading to burst-dependent changes in dendritic excitability.

The BurstCCN uses the concept of BEM in a similar way to Burstprop [10] in which ensembles
of cells encode both feedforward inference signals and feedback error signals. The model encodes
these signals as the rates of events and bursts, respectively, across the ensembles. Here, the specific
definition of a burst is a collection of spikes with interspike intervals less than 16ms and an event is
either a burst or a single isolated spike (i.e. a spike not followed or preceded by another within 16ms).
The burst probability of an ensemble is defined as the probability that an event at a given time is a
burst and is computed as a ratio of the event rate (e) and burst rate (b): p = b/e.

2.2
Rate-based BurstCCN

In our discrete-time implementation of the rate-based BurstCCN, example input-output pairs are
processed independently in discrete timesteps. For each example, the event rates of the input layer, e0,
encode the input stimulus. The model then computes each subsequent layer’s activities, equivalent to
that of a standard feedforward artificial neural network (Fig. 1A). Specifically, somatic potentials are
computed by integrating basal input as vl = Wlel−1 where Wl are short-term depressing (STD)
feedforward weights from layer l −1 to layer l. The STD nature of these weights ensures that only
event rate information propagates forwards. Each layer’s event rates are then computed by applying a
non-linear activation function, f, to the somatic potentials, el = f(vl). These linear and nonlinear
operations are repeated for each layer in the network to ultimately obtain the output layer event rates,
eL, where L denotes the total number of layers.

The desired target output of the network, etarget, is compared to the output layer event rates to
produce a signed error, etarget −eL, which is used as a teaching signal. This error information is then
propagated backwards through each layer in the network by altering the apical dendritic compartment
potential and, as a result, the burst probability of each pyramidal ensemble. At the output layer,
the burst probability is computed directly as pL = pb

L + pb

L ⊙(etarget −eL) ⊙h(eL) where ⊙

3


---

## Page 4

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
recent experimental studies [12–17]. The signals through both sets of feedback weights lead to the
apical potentials in the previous layer, ul−1 = Ql−1el −Yl−1bl. These determine the layer’s burst
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

4


---

## Page 5

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
> Figure description (generated): ## Figure Description: Burstprop vs. BurstCCN Performance Analysis

This figure, labeled with the letter 'C' and implicitly comparing against a panel 'D', presents comparative plots detailing the performance metrics of two models: **Burstprop** and **BurstCCN**. The figure is structured into three rows of plots, with two columns corresponding to the two models.

### Overall Layout and Structure
The figure is organized into a $3 \times 2$ grid of plots. The left column displays results for **Burstprop**, and the right column displays results for **BurstCCN**. Each model's section contains three distinct plots stacked vertically:
1. Top Plot: Event Rate ($\text{e}$)
2. Middle Plot: Burst Probability ($\text{p}$ and $\bar{\text{p}}$)
3. Bottom Plot: Weight Updates ($\Delta W$)

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
> Figure description (generated): ## Figure D Description

This figure, labeled **D**, presents a set of comparative plots illustrating the performance metrics for two models: "Burstprop" and "BurstCCN." The figure is structured as a $3 \times 2$ grid of time-series plots, comparing the two models across three different metrics.

### Overall Layout and Structure
The figure is organized into two main columns, one for "Burstprop" (left) and one for "BurstCCN" (right). Each column contains three stacked subplots, resulting in six total plots. The vertical axis labels indicate the measured quantity for each row of plots.

### Visual Components and Data Trends (Row by Row)

**Top Row: Event Rate ($\text{Hz}$)**
*   **Y-axis Label:** "Event rate [Hz]" (ranging from 0 to 10).
*   **X-axis:** The x-axis represents different input conditions, labeled with mathematical notation: $(\theta, \theta)$, $(\theta, 1)$, $(1, \theta)$, and $(1, 1)$. These likely correspond to different input patterns for the XOR classification task mentioned in the caption.
*   **Shading:** Gray shaded vertical bars are present over specific input conditions, indicating a particular phase or condition during the process.
*   **Burstprop (Left):** Shows an event rate that is low ($\approx 3 \text{ Hz}$) for the first input $(\theta, \theta)$. It rises significantly to $\approx 6-7 \text{ Hz}$ during the second input $(\theta, 1)$, drops sharply for $(1, \theta)$, and remains low again for $(1, 1)$.
*   **BurstCCN (Right):** Shows a more consistent pattern. The event rate is low for $(\theta, \theta)$, rises to $\approx 8-9 \text{ Hz}$ during $(\theta, 1)$ and $(1, \theta)$, and drops sharply for $(1, 1)$.

**Middle Row: Burst Probability ($p$)**
*   **Y-axis Label:** "Burst probability" (ranging from 0.0 to 1.0).
*   **X-axis:** Same input conditions as the top row: $(\theta, \theta)$, $(\theta, 1)$, $(1, \theta)$, and $(1, 1)$.
*   **Burstprop (Left):** Shows the burst probability starting low ($\approx 0.3$). It increases significantly for $(\theta, 1)$ to nearly $1.0$, remains high for $(1, \theta)$, and drops back down for $(1, 1)$.
*   **BurstCCN (Right):** Shows the burst probability starting low ($\approx 0.3$). It rises to $\approx 0.8$ for $(\theta, 1)$, remains high for $(1, \theta)$, and drops sharply to near $0.0$ for $(1, 1)$.

**Bottom Row: Weight Update ($\Delta W$)**
*   **Y-axis Label:** "$\Delta W$" (ranging from 0 to 30).
*   **X-axis:** Same input conditions as the top row: $(\theta, \theta)$, $(\theta, 1)$, $(1, \theta)$, and $(1, 1)$.
*   **Baseline/Reference:** A dashed horizontal line at $\Delta W = 0$ is present across all plots, representing the baseline or zero change.
*   **Burstprop (Left):** Shows weight updates that are generally low, with a small positive spike around $(\theta, 1)$ and $(1, \theta)$, remaining close to zero otherwise.
*   **BurstCCN (Right):** Shows distinct weight updates. There is a significant positive spike in $\Delta W$ around $(\theta, 1)$ and $(1, \theta)$, reaching values up to $\approx 25$, while the updates for $(\theta, \theta)$ and $(1, 1)$ remain close to zero.

### Contextual Caption Integration
The caption clarifies the meaning of the plots:
*   **Top Plot:** Represents the "event rate ($e$) of the output layer."
*   **Middle Plot:** Represents the "burst probability ($p$) for the output layer" (for BurstCCN) and the "baseline or moving average of the burst probability ($\bar{p}$)" (for Burstprop).
*   **Bottom Plot:** Represents "the resulting weight updates for connections from hidden layer neurons."

The comparison between Burstprop and BurstCCN demonstrates how the two models achieve classification results (implied by the input conditions) using different learning paradigms, as detailed in the caption regarding two-phase vs. single-phase learning.

details away and only considering the ensemble-level behaviour. Neurons are modelled with two
compartments corresponding to the soma and apical dendrites and spikes are generated when a
somatic threshold potential is met (see SM, Section A.2 for more details).

2.4
Related work

As previously mentioned, BurstCCN takes inspiration from two prior models: EDNs [6] and Burst-
prop [10]. Similar to these models, the BurstCCN uses a separate apical dendritic compartment to
represent an error signal. To silence this apical compartment and maintain correct error signals, the
EDN uses a homeostatic plasticity rule from local interneurons to cancel the signals received from a
separate feedback pathway. In the BurstCCN, we use the same principle by adapting this plasticity
rule for learning of the novel Q weights. Unlike the EDN, we use a similar idea to Burstprop in
which error signals are encoded as bursts in the neural activity and decoded by STP dynamics.

Within each layer, Burstprop includes a set of recurrent connections onto the apical compartments
which aim to maintain the dendritic potential in the linear regime of the feedback non-linearity.
Updating the weights of these connections requires separate learning phases and it is unclear how the
plasticity rule can be justified. In contrast, the BurstCCN does not require these connections. Instead,
the novel set of STD feedback connections (Q) onto the apical dendrites provide a mechanism for
single-phase learning and perform a similar role of linearising the feedback. Additionally, burst-
dependent plasticity in our model relies on a constant baseline burst probability instead of using a
moving average of the burst probability (see SM, Section A.2 for more information).

3
Results

3.1
BurstCCN can learn with a single learning phase

A key motivation for developing the BurstCCN was to design a model capable of learning without
the need for separate learning phases, while being consistent with a range of cortical features across

5


---

## Page 6

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

6


---

## Page 7

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
> Figure description (generated): This figure, labeled as Figure 3, illustrates the capability of BurstCCN to learn a dynamic non-linear regression task. It is composed of several distinct visual sections: a schematic diagram (implied Panel A), and two time-series plots (Panel B, C, and D).

### 1. Overall Layout & Structure
The figure is structured into a top schematic diagram followed by two distinct plots arranged horizontally below the schematic. The caption indicates that the schematic represents Panel (A), and the subsequent plots represent Panels (B), (C), and (D).

### 2. Visual Components & Symbols (Schematic Diagram)
The top section is a schematic flow diagram:
*   **Inputs:** On the left, there are three gray arrows originating from an unseen source and pointing towards a central circular node.
*   **Central Node:** A large, light gray circle represents an intermediate processing unit or node.
*   **Processing/Transformation:** From this central gray circle, a wavy blue line emanates, representing dynamic input or signal processing. This wave pattern is complex and oscillatory.
*   **Output/Target:** The blue wavy line leads into a diamond-shaped node (colored reddish-brown). This diamond likely represents the target output.
*   **Feedback Loop:** A thick, curved red arrow originates from the reddish-brown diamond node and loops back to connect near the central gray circle, indicating a feedback mechanism.
*   **Input Connection:** A thick black arrow originates from the central gray circle and points towards a point near the reddish-brown diamond, suggesting a direct connection or influence path.

### 3. Data Trends & Details (Plots)
Below the schematic, there are two main plots visible:

**Plot 1 (Panel B - Learning Curve):**
*   **Type:** Line graph showing a learning curve over time.
*   **X-axis Label:** "Time (s)" ranging from 0 to 100 seconds.
*   **Y-axis Label:** Unlabeled, but the scale ranges from 0.60 to 0.85.
*   **Curves:** Two distinct lines are plotted:
    *   A dashed black line labeled "target," which exhibits high-frequency, erratic fluctuations across the time axis.
    *   A solid light blue line labeled "output," which remains relatively stable and low, fluctuating around the 0.62–0.64 range throughout the measurement period.

**Plot 2 (Panel D - Example Output Trace):**
*   This plot is partially visible on the right side. It appears to be a time-series trace, similar in structure to Plot 1 but showing different data.
*   **X-axis:** Shows a time scale starting near 0, but the full range is cut off.
*   **Y-axis:** Shows a scale where values are visible, suggesting the output trace is being displayed.

### 4. Contextual Caption Integration
The caption clarifies the function of these elements:
*   **Task:** The system learns a "dynamic non-linear regression task."
*   **Inputs (Panel A):** The inputs are described as "Three sinusoidal waves with random frequencies."
*   **Target (Panel A):** The target pattern is generated by passing the same inputs through a "fixed, randomly initialised ANN."
*   **Plots (Panel B, C, D):** The plots show the "Learning curve for the (continuous-time) BurstCCN" (Panel B), and "Example output traces for (C) before and (D) after training."
*   **Error Representation:** The caption notes that "Model results represent mean $\pm$ standard error ($n=5$)."

> Figure caption (from PDF text): Figure 3: BurstCCN can learn a dynamic non-linear regression task. (A) Schematic of the task.
Three sinusoidal waves with random frequencies are given as inputs. The task is to learn to match
the target pattern which is obtained by passing the same inputs through a fixed, randomly initialised
ANN. (B) Learning curve for the (continuous-time) BurstCCN. (C, D) Example output traces for (C)
before and (D) after training. Model results represent mean ± standard error (n = 5).
> Figure description (generated): This image displays a single plot, which corresponds to Panel (B) mentioned in the accompanying caption.

**1. Overall Layout & Structure:**
The figure consists of a single two-dimensional line graph plotting a function over time.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Data Curve:** A single, smooth curve is plotted on the graph. This curve starts at a high value and rapidly decreases, then gradually flattens out as time increases.

**3. Labels, Keys & Legends:**
*   **Y-axis Label:** The vertical axis is labeled with numerical values ranging from 0.00 to 0.08, marked in increments of 0.02 (e.g., 0.00, 0.02, 0.04, 0.06, 0.08).
*   **X-axis Label:** The horizontal axis is labeled "Time (s)" and ranges from 0 to $1\text{e}3$ (or 1000 seconds).

**4. Data Trends & Details:**
*   The curve begins at a high value, approximately around 0.058 or 0.06 on the y-axis at Time = 0 s.
*   The curve exhibits a very steep initial decay, dropping sharply from its starting point to below 0.01 within the first few tens of seconds.
*   After this initial rapid decline, the curve continues to decrease but at a much slower rate, asymptotically approaching zero as time approaches $1000\text{ s}$.

**5. Contextual Caption Integration:**
Based on the caption, this plot represents the "Learning curve for the (continuous-time) BurstCCN." The y-axis likely represents a measure of error or loss, and the x-axis represents training time. The curve demonstrates the convergence of the learning process over time.

> Figure caption (from PDF text): Figure 3: BurstCCN can learn a dynamic non-linear regression task. (A) Schematic of the task.
Three sinusoidal waves with random frequencies are given as inputs. The task is to learn to match
the target pattern which is obtained by passing the same inputs through a fixed, randomly initialised
ANN. (B) Learning curve for the (continuous-time) BurstCCN. (C, D) Example output traces for (C)
before and (D) after training. Model results represent mean ± standard error (n = 5).
> Figure description (generated): This image displays a single plot, titled "After Training," which represents the output of a system after a training process.

**1. Overall Layout & Structure:**
The figure consists of one primary time-series plot, which is labeled as part (D) in the accompanying caption context. It is a 2D line graph showing signal amplitude over time.

**2. Visual Components & Symbols:**
*   **Axes:** The plot features a horizontal x-axis representing time and a vertical y-axis representing signal amplitude.
*   **Data Lines:** There are two distinct lines plotted: a solid blue line and a dashed black line. The solid blue line appears to represent the model's output, while the dashed black line likely represents the target pattern or ground truth.
*   **Signal Characteristics:** Both lines exhibit complex, high-frequency oscillatory behavior, resembling a superposition of multiple sine waves. The oscillations are dynamic and non-uniform across the time course.

**3. Labels, Keys & Legends:**
*   **Title:** The main title above the plot is "After Training."
*   **X-Axis Label:** The horizontal axis is labeled "Time (s)". The scale ranges from 0 to $10^4$ seconds, with major tick marks at intervals like 0, 50, and 100.
*   **Y-Axis Label:** The vertical axis lacks an explicit label in the visible portion of the image, but it represents the amplitude/output value.
*   **Annotations:** There is a small annotation near the bottom right corner: "+8e4".

**4. Data Trends & Details:**
*   **X-Axis Range:** The time axis spans from 0 seconds up to approximately $10^4$ seconds.
*   **Signal Dynamics:** The plot shows the system's response over this extended time period. Both the solid blue line and the dashed black line track each other very closely, indicating a high degree of correspondence between the learned output and the target pattern. The signals are characterized by rapid fluctuations, suggesting the successful learning of a complex, dynamic function (as implied by the caption context).

**5. Contextual Caption Integration:**
Based on the provided caption, this plot corresponds to panel (D), which shows an "Example output trace... after training." The visual evidence confirms that the system (BurstCCN) has successfully learned to match a complex target pattern derived from inputs consisting of "Three sinusoidal waves with random frequencies." The close tracking between the blue (model output) and dashed black (target pattern) lines demonstrates this successful learning of a "dynamic non-linear regression task."

This approximates the same relationship present in backprop up to a third-order1 term with respect to
the apical potentials ul if the feedback weights are set to be symmetric with the feedforward weights
(i.e. Yl = −WT

l+1). We refer to this as the W-Y symmetric state. The link between weight updates
from simply performing gradient descent with backprop and the BurstCCN can be seen clearly:

∆WBurstCNN

l
= η(W)

l
δbl eT

l−1
(4)

∆Wbackprop

l
= −η(W)

l

∂Etask

∂vl

eT

l−1
(5)

It remains to be shown that the apical potentials, ul, of every layer are indeed appropriately small (so
that the approximation error, ||u3

l ||, is small). Under the assumption ul+1 is small, we can derive
the recursive relationship ul ≈f ′ (vl+1) ⊙(−Yl)ul+1 (see SM, Section B). We show that if f ′ is
bounded (as is the case for sigmoid and many activation functions) and the weights Yl are reasonably
small then ||u3

l || ≤||u3

l+1||. This means that if the error gradient at the output layer, ∂Etask

∂eN , is small

then, by induction, ||u3

l || is small for every layer and ∆WBurstCNN

l
≈∆Wbackprop

l
.

3.3.2
Learning Q feedback connections better approximates backprop-derived gradients

We empirically evaluated our feedback plasticity rule by updating only the Q weights of a randomly
initialised 5-layer discrete-time BurstCCN with all other weight types (W and Y) fixed. We used
multiple initialisations and training regimes to understand how the plasticity rule behaves in different
scenarios. The network was either initialised in the W-Y symmetric state or with random feedback
weights (where Yl̸ = −WT

l+1). We computed the angle between the update that would have been
made by the feedforward plasticity rule (Eq. 1) and either backprop or feedback alignment [4] for the
symmetric and random configurations, respectively. We examined both cases: in the theoretically
ideal case for learning Q where no teaching signal is present (Fig. 4A-D) and with a teaching signal
at the output layer (Fig. 4E-H).

In all cases, as the alignment between the Q and Y connections improved (Fig. 4A,E), the apical
potential decreased (Fig. 4B,F) and this resulted in updates that more closely aligned to back-
prop (Fig. 4C,G) and feedback alignment (Fig. 4D,H). In the absence of a teaching signal, this

1Here we use abuse of notation u3
l =

 

u3

l,1, u3

l,2, . . .

T to represent the element-wise cubic of ul

7


---

## Page 8

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
> Figure description (generated): ## Figure 4 Description

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
> Figure description (generated): ## Detailed Figure Description: Figure 5

This figure, titled "Figure 5," presents four distinct panels (A, B, C, and D) illustrating the performance of different deep learning models on classifying handwritten digits (MNIST). All panels utilize line graphs to depict model performance metrics.

### 1. Overall Layout & Structure
The figure is structured horizontally, consisting of four adjacent subplots: Panel A, Panel B, Panel C, and Panel D.

### 2. Visual Components & Symbols
*   **Panel A:** A line graph showing "Test error (%)" versus "Epoch." Multiple colored lines represent different models.
*   **Panel B:** A line graph showing "Test error (%)" versus the "Number of layers." Multiple colored lines represent different models.
*   **Panel C:** A line graph showing "Alignment to BP" versus "Epoch." Multiple colored lines represent different models.
*   **Panel D:** A line graph showing "Alignment to BP" versus the "Number of layers." Multiple colored lines represent different models.

**Color Coding and Legend (from Panel A):**
The legend in Panel A identifies the following models by color:
*   **Black line:** ann (Artificial Neural Network)
*   **Blue line:** BurstCCN
*   **Light Blue line:** BurstCCN ($\eta(Q) = 0$)
*   **Red line:** burstprop
*   **Green line:** edn

### 3. Labels, Keys & Legends
**Axis Labels and Titles:**
*   **Panel A:** Y-axis is labeled "Test error (%)"; X-axis is labeled "Epoch."
*   **Panel B:** Y-axis is labeled "Test error (%)"; X-axis is labeled "Number of layers."
*   **Panel C:** Y-axis is labeled "Alignment to BP"; X-axis is labeled "Epoch."
*   **Panel D:** Y-axis is labeled "Alignment to BP"; X-axis is labeled "Number of layers."

**Annotations:**
*   A note in the caption specifies: "The black circle indicates that the hyperparameters for each model were optimised for 5-layer networks."

### 4. Data Trends & Details

**Panel A: Learning Curve (Test Error vs. Epoch)**
*   The Y-axis ranges from 0% to 100%. The X-axis ranges from 0 to 200 epochs.
*   The **black line (ann)** starts high and decreases rapidly, stabilizing at a low error rate.
*   The **blue line (BurstCCN)** and **light blue line (BurstCCN ($\eta(Q) = 0$))** show a steep initial drop, quickly reaching very low error rates.
*   The **red line (burstprop)** and **green line (edn)** also decrease, but their final error rates appear higher than the BurstCCN variants.

**Panel B: Test Error vs. Number of Layers**
*   The Y-axis ranges from 0% to 12.5%. The X-axis shows the "Number of layers" from 2 to 9.
*   All models generally show low test error, particularly for the BurstCCN variants (blue and light blue), which maintain very low errors across 3 to 9 layers.
*   The **red line (burstprop)** shows a slight increase in error as the number of layers increases.
*   The **green line (edn)** shows a steady, gradual increase in test error as the number of layers increases.

**Panel C: Alignment to Backprop (BP) vs. Epoch**
*   The Y-axis ranges from 0% to 100%. The X-axis ranges from 0 to 200 epochs.
*   All models start with high alignment (near 100%).
*   The **black line (ann)** maintains the highest alignment throughout.
*   The other lines show a gradual decrease in alignment over epochs, with the **red line (burstprop)** showing the most significant decline.

**Panel D: Alignment to Backprop (BP) vs. Number of Layers**
*   The Y-axis ranges from 0% to 80%. The X-axis shows the "Number of layers" from 2 to 9.
*   The **black circle** is explicitly marked at the 5-layer point, indicating hyperparameter optimization for this configuration.
*   The **blue line (BurstCCN)** and **light blue line (BurstCCN ($\eta(Q) = 0$))** maintain a high alignment percentage across the layer count.
*   The **red line (burstprop)** shows a clear, positive correlation between the number of layers and alignment percentage.
*   The **green line (edn)** shows a moderate, increasing trend in alignment with more layers.

### 5. Contextual Caption Integration
The caption clarifies that the models are learning to classify handwritten digits (MNIST). The specific notations used in the legend correspond directly to the models being compared:
*   **ann:** Standard Artificial Neural Network.
*   **BurstCCN / BurstCCN ($\eta(Q) = 0$):** Variants of the Burst Convolutional Neural Network.
*   **burstprop:** A specific variant, likely related to backpropagation mechanisms.
*   **edn:** Another model architecture being tested.

The caption confirms that the results represent mean $\pm$ standard error ($n=5$).

Next, to test whether our model can indeed perform backprop-like deep learning, we trained a number
of (discrete-time) BurstCCN architectures on the MNIST handwritten digit classification task [21].
We compared the BurstCCN with Burstprop [10] and EDNs [6] using similar architectures (see SM,
Section C.3.3). We focused on the more biologically plausible case of using random fixed feedback

8


---

## Page 9

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
Burstprop’s updates were most closely aligned to backprop, followed by the two BurstCCN models
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
> Figure description (generated): ## Figure Description: BurstCCN Architecture and Learning Curves

This figure, labeled as Figure 6 in the source material, is divided into three conceptual parts: Panel A (a schematic diagram), and Panels B and C (learning curves, though only Panel B is fully visible in the provided image).

### Panel A: BurstCCN Architecture Schematic
Panel A presents a schematic diagram illustrating the architecture of the BurstCCN model.

**Visual Components:**
1. **Input Image Representation (Left):** On the far left, there is a small image of a dog, representing the input data. A dashed blue line originates from this image and points towards a structured block diagram on the right, indicating data flow.
2. **Layered Structure (Center-Right):** The core of the schematic is a block diagram representing the network layers. This structure appears to be composed of multiple processing units arranged in a grid-like fashion, suggesting convolutional or feature extraction layers.
    * The diagram shows several small squares/rectangles arranged in a grid pattern, implying multiple feature maps or processing units.
    * Within this structure, there are small icons resembling stylized neurons or nodes (represented by a circle with internal lines/spikes) distributed across the grid, suggesting computational units.
3. **Weight Connections (Right):** To the right of the layered structure, there are three distinct variables/vectors indicated:
    * **W:** Represented by a block, suggesting feedforward weights. An arrow points from the layered structure towards this block labeled 'W'.
    * **Y:** Represented by a block, suggesting feedback weights. An arrow points from the layered structure towards this block labeled 'Y'.
    * **Q:** Represented by a block, suggesting another set of weights. An arrow points from the layered structure towards this block labeled 'Q'.

**Contextual Interpretation (from Caption):**
The caption clarifies that this schematic represents the BurstCCN architecture, which includes an input layer, three convolutional layers, a fully-connected hidden layer, and an output layer. The diagram visually represents the connection of these layers with feedforward weights ($\mathbf{W}$), feedback weights ($\mathbf{Y}$), and another set of weights ($\mathbf{Q}$).

### Panel B: Learning Curve Plot
Panel B displays a learning curve comparing the performance of different models over training epochs.

**Axes and Scale:**
* **Y-axis (Vertical):** Labeled "Test error (%)", ranging from 0% to 90%, with major ticks every 10 percentage points.
* **X-axis (Horizontal):** Labeled "Epoch", ranging from 0 to 400, with major ticks every 50 epochs.

**Legend and Curves:**
The plot contains multiple lines, differentiated by color and line style, corresponding to different model configurations:

* **Solid Lines (Random Feedback Weights):**
    * **Black Line:** Labeled "ann" (likely referring to a standard ANN model).
    * **Blue Line:** Labeled "burstccn".
    * **Light Blue Line:** Labeled "burstccn (Q-Y sym)".
    * **Red Line:** Labeled "burstprop".
* **Dashed Lines (Symmetric Feedback Weights):** The legend indicates that the line styles differentiate between "random" (solid lines) and "symmetric" (dashed lines) feedback weight regimes.

**Data Trends:**
All curves show a general decreasing trend in test error as the number of epochs increases, indicating learning convergence.
* At Epoch 0, all models start with a high test error (around 80-90%).
* The curves generally converge towards lower error rates as epochs approach 400.
* Visually, the "ann" (black solid line) and "burstccn" (blue solid line) appear to achieve the lowest final test error among the models shown in this panel.

**Contextual Annotation:**
Below the main plot area, there is a legend specifying the feedback weight regimes:
* **Solid line:** "random"
* **Dashed line:** "symmetric"

> Figure caption (from PDF text): Figure 6: BurstCCN with convolutional layers learns to solve natural image classification
task (CIFAR-10). (A) Schematic of BurstCCN architecture consisting of an input layer, three
convolutional layers, a fully-connected hidden layer and output layer. For the BurstCCN, each layer
was connected with a set of feedforward weights, W, and feedback weights, Y and Q. (B) Learning
curve and (C) alignment to backprop of the different models with random (solid lines) and symmetric
(dashed lines) feedback weight regimes. Model results represent mean ± standard error (n = 5).
> Figure description (generated): This figure, labeled as Figure 6, presents a combination of architectural schematics and learning curves related to the BurstCCN model applied to natural image classification (CIFAR-10). The figure is divided into multiple panels, though only the plot section is fully visible in the provided image snippet.

### 1. Overall Layout & Structure
The figure is structured into multiple parts, indicated by labels (A), (B), and (C) in the caption. The visible portion of the image primarily displays a set of line graphs, corresponding to Panel (B) or (C) mentioned in the caption.

### 2. Visual Components & Symbols (Focusing on the visible plot)
The visible section is a 2D line graph plotting performance metrics over training epochs.

*   **Axes:**
    *   The **x-axis** is labeled "Epoch" and ranges from 0 to 400, marked at intervals of 50.
    *   The **y-axis** represents a performance metric (likely accuracy or loss, given the context of learning curves) and ranges from 0 to 100, marked in increments of 20.
*   **Lines/Curves:** Several distinct lines are plotted, differentiated by color and line style:
    *   **Solid Lines (representing random feedback weight regimes):** There are multiple solid lines, colored in shades of blue, black/dark gray, and red/maroon.
    *   **Dashed Lines (representing symmetric feedback weight regimes):** There is at least one distinct dashed line visible near the bottom of the plot.

### 3. Labels, Keys & Legends
*   **Axis Labels:** "Epoch" (x-axis) and a numerical scale (0 to 100) on the y-axis.
*   **Annotations:** The caption specifies that "Model results represent mean $\pm$ standard error ($n=5$)," implying the plotted lines incorporate error bars, although they are not explicitly detailed in this cropped view.

### 4. Data Trends & Details (Learning Curves)
The plot displays the convergence behavior of different model configurations:

*   **Upper Curves (High Performance):** Several solid lines start at high values on the y-axis (around 70-85) at Epoch 0 and generally trend downwards or plateau slightly, indicating a learning process.
    *   The highest performing curves (e.g., the top solid line) start near 85 and gradually decrease towards a plateau around 65-70 by Epoch 400.
    *   Other solid lines show similar downward trends, settling around the 60-75 range.
*   **Middle Curves (Intermediate Performance):** A set of curves, including one solid line and potentially others, hover in the 50-70 range.
*   **Lower Curves (Low Performance):** A distinct set of lines remains near the bottom:
    *   A solid line (likely representing a specific model configuration) shows an initial rise from near 0 to approximately 25-30 by Epoch 400.
    *   A dashed line remains very close to the x-axis (near 0) throughout the entire training period.

### 5. Contextual Caption Integration
The caption clarifies that this plot relates to the "Learning curve" (Panel B) and compares results across different feedback weight regimes:
*   **Solid lines:** Represent models with **random** feedback weights.
*   **Dashed lines:** Represent models with **symmetric** feedback weights.

The overall context is that these curves illustrate how the BurstCCN architecture learns to solve natural image classification on CIFAR-10.

Finally, we wanted to investigate the capabilities of the BurstCCN on more challenging tasks
that are commonly tested in deep learning. We constructed a deep network consisting of three
convolutional layers followed by a fully-connected hidden layer and output layer (Fig. 6A). We trained
ANN, BurstCCN and Burstprop models using this network architecture on the CIFAR-10 image
classification task [22]. BurstCCN (Q-Y sym) was trained in the Q-Y symmetric regime whereas
BurstCCN was initialised in this state and Q weights were then updated using the corresponding
plasticity rule. All model types were tested with two feedback weight regimes: W-Y symmetric and
random fixed Y feedback weights (i.e. feedback alignment).

After training in the random feedback weight regime, we observed a test error of 38.99±0.18%
for BurstCCN, similar to performances achieved by an ANN (36.30±0.16%) and Burstprop
(41.32±0.14%) (Fig. 6B). For the W-Y symmetric regime which most resembles backprop,
BurstCCN (22.92±0.03%) performed significantly better than all random feedback setups and, once

9


---

## Page 10

again, obtained a similar error to the symmetric ANN (22.62±0.10%) and Burstprop (24.15±0.17%)
models. In the symmetric setups, there was a large improvement in the alignment angles to backprop
compared to the random feedback setup (Fig. 6C). This suggests that they were backpropagating
errors more effectively which likely explains the increase in performance. However, as seen within
the random feedback setups, an improvement in this alignment does not guarantee an improvement to
performance. This is because each model will traverse a different learning trajectory and converge to
a different local minimum but the alignment angle remains a good indicator of expected performance.

4
Conclusions and discussion

We have introduced a new model capable of backprop-like credit assignment by integrating known
properties of cortical networks. We have shown that by combining specific biological mechanisms
such as bursting, STP and dendrite-targeting inhibition it is possible to construct a model that learns
effectively in a continuous setting that is reminiscent of learning in the brain. Moreover, we have
demonstrated that such a model can learn complex image classification tasks with deep networks.

Our model proposes specific STP dynamics on the feedforward and feedback connections. It requires
STD on cortico-cortical projections onto pyramidal cells in line with experimental evidence [12–16].
In addition, it suggests a key role for dendrite-targeting interneurons such as SST-positive Martinotti
cells in the feedback pathway. There is evidence that these interneurons receive STF top-down
connections whereas top-down projections onto pyramidal cells exhibit STD dynamics as required by
our model [12–17]. In future work, it would be interesting to model the specific neuron types for
each connection to satisfy Dale’s law and further increase biological plausibility.

A prediction from our model is that manipulations of interneurons with STF connections would lead
to disruptions in burst decoding from the layer (brain area) above thereby obstructing learning in the
brain area below. Additionally, as error signals alter the level of bursting in the network, the model
predicts that the variance in bursting activity and the distal dendritic potentials would correlate with
the severity of errors made by the network during learning.

Although our model captures a wide range of biological features, some biological implausibilities re-
main. Currently, we use feedback alignment to provide a solution to the weight transport problem [23]
but this has a substantial impact on performance, particularly in more challenging tasks. Therefore,
it would be important to explore some of the recently introduced plausible feedback learning rules
[24–26] which could be used in conjunction with our proposed learning rules to outperform feedback
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

10


---

## Page 11