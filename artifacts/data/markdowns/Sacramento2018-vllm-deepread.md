## Page 1

Dendritic cortical microcircuits
approximate the backpropagation algorithm

João Sacramento⇤
Department of Physiology
University of Bern, Switzerland

sacramento@pyl.unibe.ch

Rui Ponte Costa†
Department of Physiology
University of Bern, Switzerland

costa@pyl.unibe.ch

Yoshua Bengio‡
Mila and Université de Montréal, Canada

yoshua.bengio@mila.quebec

Walter Senn
Department of Physiology
University of Bern, Switzerland

senn@pyl.unibe.ch

Abstract

Deep learning has seen remarkable developments over the last years, many of
them inspired by neuroscience. However, the main learning mechanism behind
these advances – error backpropagation – appears to be at odds with neurobiology.
Here, we introduce a multilayer neuronal network model with simpliﬁed dendritic
compartments in which error-driven synaptic plasticity adapts the network towards
a global desired output. In contrast to previous work our model does not require
separate phases and synaptic learning is driven by local dendritic prediction errors
continuously in time. Such errors originate at apical dendrites and occur due to
a mismatch between predictive input from lateral interneurons and activity from
actual top-down feedback. Through the use of simple dendritic compartments
and different cell-types our model can represent both error and normal activity
within a pyramidal neuron. We demonstrate the learning capabilities of the model
in regression and classiﬁcation tasks, and show analytically that it approximates
the error backpropagation algorithm. Moreover, our framework is consistent
with recent observations of learning between brain areas and the architecture of
cortical microcircuits. Overall, we introduce a novel view of learning on dendritic
cortical circuits and on how the brain may solve the long-standing synaptic credit
assignment problem.

1
Introduction

Machine learning is going through remarkable developments powered by deep neural networks (Le-
Cun et al., 2015). Interestingly, the workhorse of deep learning is still the classical backpropagation
of errors algorithm (backprop; Rumelhart et al., 1986), which has been long dismissed in neuro-
science on the grounds of biologically implausibility (Grossberg, 1987; Crick, 1989). Irrespective
of such concerns, growing evidence demonstrates that deep neural networks outperform alternative
frameworks in accurately reproducing activity patterns observed in the cortex (Lillicrap and Scott,
2013; Yamins et al., 2014; Khaligh-Razavi and Kriegeskorte, 2014; Yamins and DiCarlo, 2016; Kell
et al., 2018). Although recent developments have started to bridge the gap between neuroscience

⇤Present address: Institute of Neuroinformatics, University of Zürich and ETH Zürich, Zürich, Switzerland
†Present address: Computational Neuroscience Unit, Department of Computer Science, SCEEM, Faculty of
Engineering, University of Bristol, United Kingdom

‡CIFAR Senior Fellow

32nd Conference on Neural Information Processing Systems (NeurIPS 2018), Montréal, Canada.


---

## Page 2

and artiﬁcial intelligence (Marblestone et al., 2016; Lillicrap et al., 2016; Scellier and Bengio, 2017;
Costa et al., 2017; Guerguiev et al., 2017), how the brain could implement a backprop-like algorithm
remains an open question.

In neuroscience, understanding how the brain learns to associate different areas (e.g., visual and
motor cortices) to successfully drive behaviour is of fundamental importance (Petreanu et al., 2012;
Manita et al., 2015; Makino and Komiyama, 2015; Poort et al., 2015; Fu et al., 2015; Pakan et al.,
2016; Zmarz and Keller, 2016; Attinger et al., 2017). However, how to correctly modify synapses to
achieve this has puzzled neuroscientists for decades. This is often referred to as the synaptic credit
assignment problem (Rumelhart et al., 1986; Sutton and Barto, 1998; Roelfsema and van Ooyen,
2005; Friedrich et al., 2011; Bengio, 2014; Lee et al., 2015; Roelfsema and Holtmaat, 2018), for
which the backprop algorithm provides an elegant solution.

Here we propose that the prediction errors that drive learning in backprop are encoded at distal
dendrites of pyramidal neurons, which receive top-down input from downstream brain areas (we
interpret a brain area as being equivalent to a layer in machine learning) (Petreanu et al., 2009;
Larkum, 2013). In our model, these errors arise from the inability to exactly match via lateral input
from local interneurons (e.g. somatostatin-expressing; SST) the top-down feedback from downstream
cortical areas. Learning of bottom-up connections (i.e., feedforward weights) is driven by such error
signals through local synaptic plasticity. Therefore, in contrast to previous approaches (Marblestone
et al., 2016), in our framework a given neuron is used simultaneously for activity propagation (at the
somatic level), error encoding (at distal dendrites) and error propagation to the soma without the need
for separate phases.

We ﬁrst illustrate the different components of the model. Then, we show analytically that under
certain conditions learning in our network approximates backpropagation. Finally, we empirically
evaluate the performance of the model on nonlinear regression and recognition tasks.

2
Error-encoding dendritic cortical microcircuits

2.1
Neuron and network model

Building upon previous work (Urbanczik and Senn, 2014), we adopt a simpliﬁed multicompart-
ment neuron and describe pyramidal neurons as three-compartment units (schematically depicted
in Fig. 1A). These compartments represent the somatic, basal and apical integration zones that
characteristically deﬁne neocortical pyramidal cells (Spruston, 2008; Larkum, 2013). The dendritic
structure of the model is exploited by having bottom-up and top-down synapses converging onto
separate dendritic compartments (basal and distal dendrites, respectively), a ﬁrst approximation in line
with experimental observations (Spruston, 2008) and reﬂecting the preferred connectivity patterns of
cortico-cortical projections (Larkum, 2013).

Consistent with the connectivity of SST interneurons (Urban-Ciecko and Barth, 2016), we also
introduce a second population of cells within each hidden layer with both lateral and cross-layer
connectivity, whose role is to cancel the top-down input so as to leave only the backpropagated
errors as apical dendrite activity. Modelled as two-compartment units (depicted in red, Fig. 1A), such
interneurons are predominantly driven by pyramidal cells within the same layer through weights
WIP

k,k, and they project back to the apical dendrites of the same-layer pyramidal cells through weights
WPI

k,k (Fig. 1A). Additionally, cross-layer feedback onto SST cells originating at the next upper layer
k+1 provide a weak nudging signal for these interneurons, modelled after Urbanczik and Senn
(2014) as a conductance-based somatic input current. We modelled this weak top-down nudging on a
one-to-one basis: each interneuron is nudged towards the potential of a corresponding upper-layer
pyramidal cell. Although the one-to-one connectivity imposes a restriction in the model architecture,
this is to a certain degree in accordance with recent monosynaptic input mapping experiments show
that SST cells in fact receive top-down projections (Leinweber et al., 2017), that according to our
proposal may encode the weak interneuron ‘teaching’ signals from higher to lower brain areas.

The somatic membrane potentials of pyramidal neurons and interneurons evolve in time according to

d
dtuP

k (t) = −glk uP

k (t) + gB

!

vP

B,k(t) −uP

k (t)

"

+ gA

!

vP

A,k(t) −uP

k (t)

"

+ σ ⇠(t)
(1)

d
dtuI

k(t) = −glk uI

k(t) + gD

!

vI

k(t) −uI

k(t)

"

+ iI

k(t) + σ ⇠(t),
(2)

2


---

## Page 3

with one such pair of dynamical equations for every hidden layer 0 < k < N; input layer neurons
are indexed by k = 0, g’s are ﬁxed conductances, σ controls the amount of injected noise. Basal
and apical dendritic compartments of pyramidal cells are coupled to the soma with effective transfer
conductances gB and gA, respectively. Subscript lk is for leak, A is for apical, B for basal, D for
dendritic, superscript I for inhibitory and P for pyramidal neuron. Eqs. 1 and 2 describe standard
conductance-based voltage integration dynamics, having set membrane capacitance to unity and
resting potential to zero for clarity. Background activity is modelled as a Gaussian white noise input,
⇠in the equations above. To keep the exposition brief we use matrix notation, and denote by uP

k
and uI

k the vectors of pyramidal and interneuron somatic voltages, respectively. Both matrices and
vectors, assumed column vectors by default, are typed in boldface here and throughout. Dendritic
compartmental potentials are denoted by v and are given in instantaneous form by

vP

B,k(t) = WPP

k,k−1 φ(uP

k−1(t))
(3)

vP

A,k(t) = WPP

k,k+1 φ(uP

k+1(t)) + WPI

k,k φ(uI

k(t)),
(4)

where φ(u) is the neuronal transfer function, which acts componentwise on u.

A
B
C

(i)

layer 2

(output)

layer 1

(hidden)

sensory input

layer 0

output

(ii)

u: somatic potential
v: dendritic potential

}

B: basal
A: apical
P: pyramidal cell

I: interneuron

I
1

uI

1

uP

2

v

layer 2
layer 1

P
B,k
v

wPI

1,1 -

IP
1,1

w2,1

w

PP

target

} error

sensory input

(layer 0)

utrgt

2

PP
1,0
w
PP
1,0
w

+

uP

1

P
A,1
v

0
1500
0

1

0
1500
0

10

||Apical pot.||

Time (ms)

Time (ms)

before

learning

after

plasticity

Apical

potential

Time (ms)
0
100
200

error

0

Sensory

input

target

0
100
200
Time (ms)

(ii)
(i)

1
Apical topdown

Apical cancelation

u trgt

2
Output

uP

2

error

rP

0

P
A,1
V

PP
1,0
w

||pyrk+1 - intk||2

target

target

Figure 1: Learning in error-encoding dendritic microcircuit network. (A) Schematic of network
with pyramidal cells and lateral inhibitory interneurons. Starting from a self-predicting state – see
main text and supplementary material (SM) – when a novel teaching (or associative) signal is
presented at the output layer (utrgt

> Figure caption (from PDF text): Figure 1: Learning in error-encoding dendritic microcircuit network. (A) Schematic of network
with pyramidal cells and lateral inhibitory interneurons. Starting from a self-predicting state – see
main text and supplementary material (SM) – when a novel teaching (or associative) signal is
presented at the output layer (utrgt
> Figure description (generated): ## Figure 1 Description: Learning in Error-Encoding Dendritic Microcircuit Network

This figure presents a schematic representation of a neural network architecture, divided into two main panels, **A** and **B**, illustrating the structure of a learning mechanism within a dendritic microcircuit.

### Overall Layout & Structure
The figure is structured into two interconnected parts: Panel A shows a high-level, layered schematic of the network, while Panel B provides a detailed, zoomed-in view of the synaptic and cellular interactions within one layer.

### Panel A: Network Schematic
Panel A depicts a multi-layered network structure, organized vertically into three layers: Layer 0 (sensory input), Layer 1 (hidden), and Layer 2 (output).

*   **Layers:**
    *   **Layer 0 (Sensory Input):** Represented by a row of small, gray triangular nodes at the bottom.
    *   **Layer 1 (Hidden):** A middle layer containing several interconnected nodes, depicted as gray triangles.
    *   **Layer 2 (Output):** The top layer, containing nodes that feed into the final output.
*   **Connectivity:** Arrows indicate signal flow:
    *   Inputs flow from Layer 0 $\rightarrow$ Layer 1.
    *   Signals flow from Layer 1 $\rightarrow$ Layer 2.
    *   A distinct arrow labeled "output" points upward from the nodes in Layer 2.
*   **Cell Types/Components:** The schematic includes representations of different cell types:
    *   Gray triangles represent general network nodes.
    *   A green node in Layer 1 is highlighted, suggesting a specific cell type or activation state.
    *   The caption identifies the presence of "pyramidal cells and lateral inhibitory interneurons."

### Panel B: Detailed Microcircuit View
Panel B is a magnified view focusing on the interactions within Layer 1 and its connections to Layer 0, illustrating dendritic processing. This section is enclosed in a dashed box.

*   **Layers:** It clearly delineates Layer 0 (sensory input) at the bottom and Layer 1 above it.
*   **Nodes & Cells:** Nodes are represented as circles, and specific cell types are indicated by color:
    *   **Pyramidal Cells ($\text{P}$):** Represented by larger, gray nodes.
    *   **Interneurons ($\text{I}$):** Represented by smaller, red nodes.
    *   **Apical/Dendritic Elements:** The structure suggests dendritic integration, with inputs arriving at the nodes.
*   **Inputs and Outputs:**
    *   Sensory input arrives from Layer 0.
    *   The output of the system is indicated by a blue node labeled $\text{U}_{\text{trgt}}$ (target) in Layer 2, which is connected to the circuit.
*   **Synaptic Connections and Variables:** Numerous arrows denote synaptic connections, labeled with specific variables:
    *   **Inputs to Pyramidal Cells ($\text{P}$):** Connections are labeled with weights like $W_{1,1}$, $W_{2,1}$, and $W_{\text{IP}}$.
    *   **Inputs to Interneurons ($\text{I}$):** Connections are labeled with weights like $W_{1,0}$.
    *   **Dendritic Potentials:** Variables $\text{v}_1$ (dendritic potential) and $\text{u}_2$ (somatic potential, implied by context/labeling) are shown.
    *   **Error Signal:** A distinct pathway shows an "error" signal, indicated by a red arrow originating from the interaction between $\text{U}_{\text{trgt}}$ and the network, feeding back into the circuit.
*   **Key Components Labeled:**
    *   $\text{U}_{\text{trgt}}$: The target signal node in Layer 2.
    *   $\text{P}$: Pyramidal cell.
    *   $\text{I}$: Interneuron.
    *   $\text{A}$: Apical (referring to the apical dendrite structure).
    *   $\text{v}_{\text{k}}$: Dendritic potential.

### Labels, Keys & Legends
The figure uses specific notations to define components:
*   **Cell Types:** $\text{P}$ (Pyramidal cell), $\text{I}$ (Interneuron).
*   **Potentials/Signals:** $\text{u}$ (somatic potential), $\text{v}$ (dendritic potential).
*   **Weights:** $W_{i,j}$ denotes synaptic weights.
*   **Error Term:** Explicitly labeled "error" in Panel B, indicating the learning signal.

### Contextual Caption Integration
The caption clarifies that this figure illustrates "Learning in error-encoding dendritic microcircuit network." It specifies the starting condition as a "self-predicting state" and notes that novel teaching or associative signals are presented at the output layer ($\text{U}_{\text{trgt}}$). This confirms that Panel B models how the network processes an error signal derived from comparing its output to a target.

2
), a prediction error in the apical compartments of pyramidal
neurons in the upstream layer (layer 1, ‘error’) is generated. This error appears as an apical voltage
deﬂection that propagates down to the soma (purple arrow) where it modulates the somatic ﬁring rate,
which in turn leads to plasticity at bottom-up synapses (bottom, green). (B) Activity traces in the
microcircuit before and after a new teaching signal is learned. (i) Before learning: a new teaching
signal is presented (utrgt

2
), which triggers a mismatch between the top-down feedback (grey blue)
and the cancellation given by the lateral interneurons (red). (ii) After learning (with plasticity at the
bottom-up synapses (WPP

1,0)), the network successfully predicts the new teaching signal, reﬂected on
no distal ’error’ (top-down and lateral interneuron input cancel each other). (C) Interneurons learn to
predict the backpropagated activity (i), while simultaneously silencing the apical compartment (ii),
even though the pyramidal neurons remain active (not shown).

For simplicity, we reduce pyramidal output neurons to two-compartment cells: the apical compartment
is absent (gA = 0 in Eq. 1) and basal voltages are as deﬁned in Eq. 3. Although the design can be
extended to more complex morphologies, in the framework of dendritic predictive plasticity two
compartments sufﬁce to compare desired target with actual prediction. Synapses proximal to the
soma of output neurons provide direct external teaching input, incorporated as an additional source of
current iP

N. In practice, one can simply set iP

N = gsom(utrgt

N −uP

N), with some ﬁxed somatic nudging
conductance gsom. This can be modelled closer to biology by explicitly setting the somatic excitatory
and inhibitory conductance-based inputs (Urbanczik and Senn, 2014). For a given output neuron,
iP

N(t) = gP

exc,N(t)

!

Eexc −uP

N(t)

"

+gP

inh,N(t)

!

Einh −uP

N(t)

"

, where Eexc and Einh are excitatory
and inhibitory synaptic reversal potentials, respectively, where the inputs are balanced according to

3


---

## Page 4

gP

exc,N = gsom

utrgt

N −Einh
Eexc−Einh , gP

inh,N = −gsom

utrgt

N −Eexc
Eexc−Einh . The point at which no current ﬂows, iP

N = 0,
deﬁnes the target teaching voltage utrgt

N towards which the neuron is nudged4.

Interneurons are similarly modelled as two-compartment cells, cf. Eq. 2. Lateral dendritic projections
from neighboring pyramidal neurons provide the main source of input as

vI

k(t) = WIP

k,k φ(uP

k (t)),
(5)

whereas cross-layer, top-down synapses deﬁne the teaching current iI

k. This means that an interneuron
at layer k permanently (i.e., when learning or performing a task) receives balanced somatic teaching
excitatory and inhibitory input from a pyramidal neuron at layer k+1 on a one-to-one basis (as above,
but with uP

k+1 as target). With this setting, the interneuron is nudged to follow the corresponding
next layer pyramidal neuron. See SM for detailed parameters.

2.2
Synaptic learning rules

The synaptic learning rules we use belong to the class of dendritic predictive plasticity rules (Ur-
banczik and Senn, 2014; Spicher et al., 2018) that can be expressed in its general form as

d
dtw = ⌘(φ(u) −φ(v)) r,
(6)

where w is an individual synaptic weight, ⌘is a learning rate, u and v denote distinct compartmental
potentials, φ is a rate function, and r is the presynaptic input. Eq. 6 was originally derived in the light
of reducing the prediction error of somatic spiking, when u represents the somatic potential and v is
a function of the postsynaptic dendritic potential.

In our model the plasticity rules for the various connection types are:

d
dtWPP

k,k−1 = ⌘PP

k,k−1

!

φ(uP

k ) −φ(ˆvP

B,k)

" !

rP

k−1

"T ,
(7)

d
dtWIP

k,k = ⌘IP

k,k

!

φ(uI

k) −φ(ˆvI

k)

" !

rP

k

"T ,
(8)

d
dtWPI

k,k = ⌘PI

k,k

!

vrest −vP

A,k

" !

rI

k

"T ,
(9)

where (·)T denotes vector transpose and rk ⌘φ(uk) the layer k ﬁring rates. The synaptic weights
evolve according to the product of dendritic prediction error and presynaptic rate, and can undergo
both potentiation or depression depending on the sign of the ﬁrst factor (i.e., the prediction error).

For basal synapses, such prediction error factor amounts to a difference between postsynaptic rate
and a local dendritic estimate which depends on the branch potential. In Eqs. 7 and 8, ˆvP

B,k =
gB
glk+gB+gA vP

B,k and ˆvI

k =
gD
glk+gD vI

k take into account dendritic attenuation factors of the different
compartments. On the other hand, the plasticity rule (9) of lateral interneuron-to-pyramidal synapses
aims to silence (i.e., set to resting potential vrest = 0, here and throughout zero for simplicity)
the apical compartment; this introduces an attractive state for learning where the contribution from
interneurons balances (or cancels out) top-down dendritic input. This learning rule of apical-targeting
interneuron synapses can be thought of as a dendritic variant of the homeostatic inhibitory plasticity
proposed by Vogels et al. (2011); Luz and Shamir (2012).

In experiments where the top-down connections are plastic, the weights evolve according to

d
dtWPP

k,k+1 = ⌘PP

k,k+1

!

φ(uP

k ) −φ(ˆvP

TD,k)

" !

rP

k+1

"T ,
(10)

with ˆvP

TD,k = Wk,k+1 rP

k+1. An implementation of this rule requires a subdivision of the apical
compartment into a distal part receiving the top-down input (with voltage ˆvP

TD,k) and another distal
compartment receiving the lateral input from the interneurons (with voltage vP

A,k).

4Note that in biology a target may be represented by an associative signal from the motor cortex to a sensory
cortex (Attinger et al., 2017).

4


---

## Page 5

2.3
Comparison to previous work

It has been suggested that error backpropagation could be approximated by an algorithm that requires
alternating between two learning phases, known as contrastive Hebbian learning (Ackley et al., 1985).
This link between the two algorithms was ﬁrst established for an unsupervised learning task (Hinton
and McClelland, 1988) and later analyzed (Xie and Seung, 2003) and generalized to broader classes
of models (O’Reilly, 1996; Scellier and Bengio, 2017).

The concept of apical dendrites as distinct integration zones, and the suggestion that this could
simplify the implementation of backprop has been previously made (Körding and König, 2000, 2001).
Our microcircuit design builds upon this view, offering a concrete mechanism that enables apical error
encoding. In a similar spirit, two-phase learning recently reappeared in a study that exploits dendrites
for deep learning with biological neurons (Guerguiev et al., 2017). In this more recent work, the
temporal difference between the activity of the apical dendrite in the presence and in the absence of
the teaching input represents the error that induces plasticity at the forward synapses. This difference
is used directly for learning the bottom-up synapses without inﬂuencing the somatic activity of the
pyramidal cell. In contrast, we postulate that the apical dendrite has an explicit error representation by
simultaneously integrating top-down excitation and lateral inhibition. As a consequence, we do not
need to postulate separate temporal phases, and our network operates continuously while plasticity at
all synapses is always turned on.

Error minimization is an integral part of brain function according to predictive coding theories
(Rao and Ballard, 1999; Friston, 2005). Interestingly, recent work has shown that backprop can
be mapped onto a predictive coding network architecture (Whittington and Bogacz, 2017), related
to the general framework introduced by LeCun (1988). A possible network implementation is
suggested by Whittington and Bogacz (2017) that requires intricate circuitry with appropriately tuned
error-representing neurons. According to this work, the only plastic synapses are those that connect
prediction and error neurons. By contrast, in our model, lateral, bottom-up and top-down connections
are all plastic, and errors are directly encoded in dendritic compartments.

3
Results

3.1
Learning in dendritic error networks approximates backprop

In our model, neurons implicitly carry and transmit errors across the network. In the supplementary
material, we formally show such propagation of errors for networks in a particular regime, which we
term self-predicting. Self-predicting nets are such that when no external target is provided to output
layer neurons, the lateral input from interneurons cancels the internally generated top-down feedback
and renders apical dendrites silent. In this case, the output becomes a feedforward function of the
input, which can in theory be optimized by conventional backprop. We demonstrate that synaptic
plasticity in self-predicting nets approximates the weight changes prescribed by backprop.

We summarize below the main points of the full analysis (see SM). First, we show that somatic
membrane potentials at hidden layer k integrate feedforward predictions (encoded in basal dendritic
potentials) with backpropagated errors (encoded in apical dendritic potentials):

uP

k = u−

k + λN−k+1 WPP

k,k+1

N−1
Y

l=k+1

D−

l WPP

l,l+1

!

D−

N

!

utrgt

N −u−

N

"

+ O(λN−k+2).

Parameter λ ⌧1 sets the strength of feedback and teaching versus bottom-up inputs and is assumed
to be small to simplify the analysis. The ﬁrst term is the basal contribution and corresponds to u−

k ,
the activation computed by a purely feedforward network that is obtained by removing lateral and
top-down weights from the model (here and below, we use superscript ‘-’ to refer to the feedforward
model). The second term (of order λN−k+1) is an error that is backpropagated from the output layer
down to k-th layer hidden neurons; matrix Dk is a diagonal matrix with i-th entry containing the
derivative of the neuronal transfer function evaluated at u−

k,i.

Second, we compare model synaptic weight updates for the bottom-up connections to those prescribed
by backprop. Output layer updates are exactly equal by construction. For hidden neuron synapses,

5


---

## Page 6

we obtain

∆WPP

k,k−1 = ⌘PP

k,k−1λN−k+1

N−1
Y

l=k

D−

l WPP

l,l+1

!

D−

N

!

utrgt

N −u−

N

" !

r−

k−1

"T + O(λN−k+2).

Up to a factor which can be absorbed in the learning rate, this plasticity rule becomes equal to the
backprop weight change in the weak feedback limit λ ! 0, provided that the top-down weights are
set to the transpose of the corresponding feedforward weights.

In our simulations, top-down weights are either set at random and kept ﬁxed, in which case the
equation above shows that the plasticity model optimizes the predictions according to an approxima-
tion of backprop known as feedback alignment (Lillicrap et al., 2016); or learned so as to minimize
an inverse reconstruction loss, in which case the network implements a form of target propagation
(Bengio, 2014; Lee et al., 2015).

3.2
Deviations from self-predictions encode backpropagated errors

To illustrate learning in the model and to conﬁrm our analytical insights we ﬁrst study a very simple
task: memorizing a single input-output pattern association with only one hidden layer; the task
naturally generalizes to multiple memories.

Given a self-predicting network (established by microcircuit plasticity, Fig. S1, see SM for more
details), we focus on how prediction errors get propagated backwards when a novel teaching signal is
provided to the output layer, modeled via the activation of additional somatic conductances in output
pyramidal neurons. Here we consider a network model with an input, a hidden and an output layer
(layers 0, 1 and 2, respectively; Fig. 1A).

When the pyramidal cell activity in the output layer is nudged towards some desired target (Fig. 1B
(i)), the bottom-up synapses WPP

2,1 from the lower layer neurons to the basal dendrites are adapted,
again according to the plasticity rule that implements the dendritic prediction of somatic spiking (see
Eq. 7). What these synapses cannot explain away encodes a dendritic error in the pyramidal neurons
of the lower layer 1. In fact, the self-predicting microcircuit can only cancel the feedback that is
produced by the lower layer activity.

The somatic integration of apical activity induces plasticity at the bottom-up synapses WPP

1,0 (Eq. 7).
As the apical error changes the somatic activity, plasticity of the WPP

1,0 weights tries to further reduce
the error in the output layer. Importantly, the plasticity rule depends only on local information
available at the synaptic level: postsynaptic ﬁring and dendritic branch voltage, as well as the
presynaptic activity, in par with phenomenological models of synaptic plasticity (Sjöström et al., 2001;
Clopath et al., 2010; Bono and Clopath, 2017). This learning occur concurrently with modiﬁcations
of lateral interneuron weights which track changes in the output layer. Through the course of learning
the network comes to a point where the novel top-down input is successfully predicted (Fig. 1B,C).

3.3
Network learns to solve a nonlinear regression task

We now test the learning capabilities of the model on a nonlinear regression task, where the goal is to
associate sensory input with the output of a separate multilayer network that transforms the same
sensory input (Fig. 2A). More precisely, a pyramidal neuron network of dimensions 30-50-10 (and 10
hidden layer interneurons) learns to approximate a random nonlinear function implemented by a held-
aside feedforward network of dimensions 30-20-10. One teaching example consists of a randomly
drawn input pattern rP

0 assigned to corresponding target rtrgt
2
= φ(k2,1Wtrgt

2,1 φ(k1,0 Wtrgt
1,0 rP
0 )),
with scale factors k2,1 = 10 and k1,0 = 2. Teacher network weights and input pattern entries are
sampled from a uniform distribution U(−1, 1). We used a soft rectifying nonlinearity as the neuronal
transfer function, φ(u) = γ log(1 + exp(β(u −✓)), with γ = 0.1, β = 1 and ✓= 3. This parameter
setting led to neuronal activity in the nonlinear, sparse ﬁring regime.

The network is initialized to a random initial synaptic weight conﬁguration, with both pyramidal-
pyramidal WPP

1,0, WPP
2,1, WPP
1,2 and pyramidal-interneuron weights WIP
1,1, WPI
1,1 independently drawn
from a uniform distribution. Top-down weight matrix WPP

1,2 is kept ﬁxed throughout, in the spirit
of feedback alignment (Lillicrap et al., 2016). Output layer teaching currents iP

2 are set so as to
nudge uP

2 towards the teacher-generated utrgt
2
. Learning rates were manually chosen to yield best

6


---

## Page 7

A

WPP

2,1

WPP

1,0

WPP

1,2

WIP

1,1

WPI

1,1

P
A,1

r P

2

shallow learning

pyramidal neuron learning

Squared  error

Training trial (x107)

0
0.5
1
0

0.1

C

0
100
200

r P

0

0
100
200

P
A,1

Time [ms]
Time [ms]

(ii)
(i)
before
after
B

learning

r2

trgt
25

0
r P

2

0

v

0

separate network

teaching/associative input

v

r2

trgt

layer 2

(output)

layer 1

(hidden)

sensory
input

layer 0

Apical

potential
Sensory

input
Output (Hz)

0
0.5
0

3

||Apical pot. ||2

0
0.5
0

3

|| pyrk+1 - intk||2

Trial (x107)

(i)

(ii)

Figure 2: Dendritic error microcircuit learns to solve a nonlinear regression task online and
without phases. (A-C) Starting from a random initial weight conﬁguration, a 30-50-10 fully-
connected network learns to approximate a nonlinear function (‘separate network’) from input-output
pattern pairs. (B) Example ﬁring rates for a randomly chosen output neuron (rP

2 , blue noisy trace)
and its desired target imposed by the associative input (rtrgt

2
, blue dashed line), together with the
voltage in the apical compartment of a hidden neuron (vP

A,1, grey noisy trace) and the input rate from
the sensory neuron (rP

0 , green). Traces are shown before (i) and after learning (ii). (C) Error curves
for the full model and a shallow model for comparison.

performance. Some learning rate tuning was required to ensure the microcircuit could track the
changes in the bottom-up pyramidal-pyramidal weights, but we did not observe high sensitivity once
the correct parameter regime was identiﬁed. Error curves are exponential moving averages of the sum
of squared errors loss krP

2 −rtrgt
2
k2 computed after every example on unseen input patterns. Test
error performance is measured in a noise-free setting (σ = 0). Plasticity induction terms given by
Eqs. 7-9 are low-pass ﬁltered with time constant ⌧w before being deﬁnitely consolidated, to dampen
ﬂuctuations; synaptic plasticity is kept on throughout. Plasticity and neuron model parameters are as
deﬁned above.

We let learning occur in continuous time without pauses or alternations in plasticity as input patterns
are sequentially presented. This is in contrast to previous learning models that rely on computing
activity differences over distinct phases, requiring temporally nonlocal computation, or globally
coordinated plasticity rule switches (Hinton and McClelland, 1988; O’Reilly, 1996; Xie and Seung,
2003; Scellier and Bengio, 2017; Guerguiev et al., 2017). Furthermore, we relaxed the bottom-up
vs. top-down weight symmetry imposed by backprop and kept the top-down weights WPP

1,2 ﬁxed.

Forward WPP

1,2 weights quickly aligned to ⇠45o of the feedback weights
!

WPP

2,1
"T (see Fig. S1),
in line with the recently discovered feedback alignment phenomenon (Lillicrap et al., 2016). This
simpliﬁes the architecture, because top-down and interneuron-to-pyramidal synapses need not be
changed. We set the scale of the top-down weights, apical and somatic conductances such that
feedback and teaching inputs were strong, to test the model outside the weak feedback regime
(λ ! 0) for which our SM theory was developed. Finally, to test robustness, we injected a weak
noise current to every neuron.

Our network was able to learn this harder task (Fig. 2B), performing considerably better than a
shallow learner where only hidden-to-output weights were adjusted (Fig. 2C). Useful changes were
thus made to hidden layer bottom-up weights. The self-predicting network state emerged throughout
learning from a random initial conﬁguration (see SM; Fig. S1).

3.4
Microcircuit network learns to classify handwritten digits

Next, we turn to the problem of classifying MNIST handwritten digits. We wondered how our
model would fare in this benchmark, in particular whether the prediction errors computed by the
interneuron microcircuit would allow learning the weights of a hierarchical nonlinear network with
multiple hidden layers. To that end, we trained a deeper, larger 4-layer network (with 784-500-500-10
pyramidal neurons, Fig. 3A) by pairing digit images with teaching inputs that nudged the 10 output
neurons towards the correct class pattern. We initialized the network to a random but self-predicting

7


---

## Page 8

B

MNIST handwritten digit images

500

28x28

10

500

input

hidden 1
hidden 2
output

8
9
A

1.96%
1.53%

8.4%

0
200
0

5

10

Trials

Test error (%)

single-layer

dendritic microcircuit

backprop

Figure 3: Dendritic error networks
learn to classify handwritten digits.
(A) A network with two hidden lay-
ers learns to classify handwritten digits
from the MNIST data set. (B) Classi-
ﬁcation error achieved on the MNIST
testing set (blue; cf. shallow learner
(black) and standard backprop6(red)).

> Figure description (generated): Based on the provided image snippet, here is a detailed, comprehensive description of its visual and structural contents:

### Figure Description

**1. Overall Layout & Structure:**
The image appears to be a segment of a technical diagram, likely illustrating the input stage or data source for a neural network model. It is not a complete circuit schematic but rather a presentation of the input data format alongside some accompanying text fragments.

**2. Visual Components & Symbols:**
*   **Input Data Representation:** A row of handwritten digits is displayed centrally. These digits are presented in a grid-like fashion, suggesting they represent samples from a dataset.
    *   The digits visible are: `3`, `4`, `2`, `1`, `9`, `5`, `6`, `2`, `1`, `8` (in the top row) and `8`, `9`, `1`, `2`, `5`, `0`, `0`, `6`, `6`, `4` (in the bottom row).
*   **Input Dimension Label:** To the left of the digit display, there is a label indicating image dimensions: `28x28`.
*   **Flow/Connection Indicator:** A curved green arrow originates from the left side, pointing towards the block containing the handwritten digits. This suggests a flow or input pathway leading into the data representation.
*   **Textual Annotations:** Several fragments of text are present, positioned around the main visual elements.

**3. Labels, Keys & Legends:**
*   **Data Source Label:** Directly beneath the grid of digits is the label: `MNIST handwritten digit images`.
*   **Trial Count Label:** Above the grid of digits, centered, is a label indicating the scale: `200 Trials`.
*   **Dimensionality Label:** The text `28x28` is positioned next to the green arrow, specifying the input size.
*   **Text Fragments (Contextual):** The surrounding text includes fragments such as:
    *   "...fication testin..." (Top right)
    *   "...(black" (Bottom right, likely referring to a specific component or color)
    *   "...interneurons cancelled top-down inputs, n..." (Lower left)
    *   "...started. Top-down and interneuron-to-pyra..." (Lower center)
    *   "...l efficiency we used a simplified network u..." (Bottom edge)

**4. Data Trends & Details:**
Since the image displays static input data (the digits) rather than a plot, there are no discernible trends or axes to describe. The data itself represents 20 samples (10 in the top row, 10 in the bottom row) of $28 \times 28$ pixel images, sourced from the MNIST dataset.

**5. Contextual Caption Integration:**
The label `MNIST handwritten digit images` explicitly identifies the source and nature of the input data. The dimension `28x28` specifies the feature vector size for each sample. The surrounding text fragments suggest this figure is part of a discussion detailing the architecture or processing steps involving "interneurons," "top-down inputs," and network efficiency, implying the digits shown are the input stimuli to a described neural model.

conﬁguration where interneurons cancelled top-down inputs, rendering the apical compartments
silent before training started. Top-down and interneuron-to-pyramidal weights were kept ﬁxed.

Here for computational efﬁciency we used a simpliﬁed network dynamics where the compartmental
potentials are updated only in two steps before applying synaptic changes. In particular, for each
presented MNIST image, both pyramidal and interneurons are ﬁrst initialized to their bottom-
up prediction state (3), uk = vB,k, starting from layer 1 up to the top layer N. Output layer
neurons are then nudged towards their desired target utrgt

N , yielding updated somatic potentials
uP

N = (1 −λN) vB,N + λN utrgt

N . To obtain the remaining ﬁnal compartmental potentials, the
network is visited in reverse order, proceeding from layer k = N −1 down to k = 1. For each k,
interneurons are ﬁrst updated to include top-down teaching signals, uI

k = (1−λI) vI

k +λI uP

k+1; this
yields apical compartment potentials according to (4), after which we update hidden layer somatic
potentials as a convex combination with mixing factor λk. The convex combination factors introduced
above are directly related to neuron model parameters as conductance ratios. Synaptic weights are
then updated according to Eqs. 7-10. Such simpliﬁed dynamics approximates the full recurrent
network relaxation in the deterministic setting σ ! 0, with the approximation improving as the
top-down dendritic coupling is decreased, gA ! 0.

We train the models on the standard MNIST handwritten image database, further splitting the training
set into 55000 training and 5000 validation examples. The reported test error curves are computed
on the 10000 held-aside test images. The four-layer network shown in Fig. 3 is initialized in a
self-predicting state with appropriately scaled initial weight matrices. For our MNIST networks,
we used relatively weak feedback weights, apical and somatic conductances (see SM) to justify
our simpliﬁed approximate dynamics described above, although we found that performance did not
appreciably degrade with larger values. To speed-up training we use a mini-batch strategy on every
learning rule, whereby weight changes are averaged across 10 images before being applied. We
take the neuronal transfer function φ to be a logistic function, φ(u) = 1/(1 + exp(−u)) and include
a learnable threshold on each neuron, modelled as an additional input ﬁxed at unity with a plastic
weight. Desired target class vectors are 1-hot coded, with rtrgt

N
2 {0.1, 0.8}. During testing, the
output is determined by picking the class label corresponding to the neuron with highest ﬁring rate.
We found the model to be relatively robust to learning rate tuning on the MNIST task, except for the
rescaling by the inverse mixing factor to compensate for teaching signal dilution (see SM for the
exact parameters).

The network was able to achieve a test error of 1.96%, Fig. 3B, a ﬁgure not overly far from the
reference mark of non-convolutional artiﬁcial neural networks optimized with backprop (1.53%) and
comparable to recently published results that lie within the range 1.6-2.4% (Lee et al., 2015; Lillicrap
et al., 2016; Nøkland, 2016). The performance of our model also compares favorably to the 3.2%
test error reported by Guerguiev et al. (2017) for a two-hidden-layer network. This was possible
despite the asymmetry of forward and top-down weights and at odds with exact backprop, thanks
to a feedback alignment dynamics. Apical compartment voltages remained approximately silent
when output nudging was turned off (data not shown), reﬂecting the maintenance of a self-predicting
state throughout learning, which enabled the propagation of errors through the network. To further
demonstrate that the microcircuit was able to propagate errors to deeper hidden layers, and that the
task was not being solved by making useful changes only to the weights onto the topmost hidden
layer, we re-ran the experiment while keeping ﬁxed the pyramidal-pyramidal weights connecting the
two hidden layers. The network still learned the dataset and achieved a test error of 2.11%.

8


---

## Page 9

As top-down weights are likely plastic in cortex, we also trained a one-hidden-layer (784-1000-10)
network where top-down weights were learned on a slow time-scale according to learning rule (10).
This inverse learning scheme is closely related to target propagation (Bengio, 2014; Lee et al., 2015).
Such learning could play a role in perceptual denoising, pattern completion and disambiguation,
and boost alignment beyond that achieved by pure feedback alignment (Bengio, 2014). Starting
from random initial conditions and keeping all weights plastic (bottom-up, lateral and top-down)
throughout, our network achieved a test classiﬁcation performance of 2.48% on MNIST. Once more,
useful changes were made to hidden synapses, even though the microcircuit had to track changes in
both the bottom-up and the top-down pathways.

4
Conclusions

Our work makes several predictions across different levels of investigation. Here we brieﬂy highlight
some of these predictions and related experimental observations. The most fundamental feature of
the model is that distal dendrites encode error signals that instruct learning of lateral and bottom-
up connections. While monitoring such dendritic signals during learning is challenging, recent
experimental evidence suggests that prediction errors in mouse visual cortex arise from a failure
to locally inhibit motor feedback (Zmarz and Keller, 2016; Attinger et al., 2017), consistent with
our model. Interestingly, the plasticity rule for apical dendritic inhibition, which is central to error
encoding in the model, received support from another recent experimental study (Chiu et al., 2018).

A further implication of our model is that prediction errors occurring at a higher-order cortical area
would imply also prediction errors co-occurring at earlier areas. Recent experimental observations in
the macaque face-processing hierarchy support this (Schwiedrzik and Freiwald, 2017).

Here we have focused on the role of a speciﬁc interneuron type (SST) as a feedback-speciﬁc
interneuron. There are many more interneuron types that we do not consider in our framework. One
such type are the PV (parvalbumin-positive) cells, which have been postulated to mediate a somatic
excitation-inhibition balance (Vogels et al., 2011; Froemke, 2015) and competition (Masquelier
and Thorpe, 2007; Nessler et al., 2013). These functions could in principle be combined with our
framework in that PV interneurons may be involved in representing another type of prediction error
(e.g., generative errors).

Humans have the ability to perform fast (e.g., one-shot) learning, whereas neural networks trained by
backpropagation of error (or approximations thereof, like ours) require iterating over many training
examples to learn. This is an important open problem that stands in the way of understanding the
neuronal basis of intelligence. One possibility where our model naturally ﬁts is to consider multiple
subsystems (for example, the neocortex and the hippocampus) that transfer knowledge to each other
and learn at different rates (McClelland et al., 1995; Kumaran et al., 2016).

Overall, our work provides a new view on how the brain may solve the credit assignment problem
for time-continuous input streams by approximating the backpropagation algorithm, and bringing
together many puzzling features of cortical microcircuits.

Acknowledgements

The authors would like to thank Timothy P. Lillicrap, Blake Richards, Benjamin Scellier and Mihai
A. Petrovici for helpful discussions. WS thanks Matthew Larkum for many inspiring discussions on
dendritic processing. JS thanks Elena Kreutzer, Pascal Leimer and Martin T. Wiechert for valuable
feedback and critical reading of the manuscript.

This work has been supported by the Swiss National Science Foundation (grant 310030L-156863 of
WS), the European Union’s Horizon 2020 Framework Programme for Research and Innovation under
the Speciﬁc Grant Agreement No. 785907 (Human Brain Project), NSERC, CIFAR, and Canada
Research Chairs.

9


---

## Page 10