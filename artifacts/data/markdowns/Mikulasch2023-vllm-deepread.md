## Page 1

Review
Where is the error? Hierarchical predictive
coding through dendritic error computation

Fabian A. Mikulasch,1,5,* Lucas Rudelt,1,5 Michael Wibral,2 and Viola Priesemann1,3,4

Top-down feedback in cortex is critical for guiding sensory processing, which
has prominently been formalized in the theory of hierarchical predictive coding
(hPC). However, experimental evidence for error units, which are central to the
theory, is inconclusive and it remains unclear how hPC can be implemented
with spiking neurons. To address this, we connect hPC to existing work on efﬁ-
cient coding in balanced networks with lateral inhibition and predictive computa-
tion at apical dendrites. Together, this work points to an efﬁcient implementation
of hPC with spiking neurons, where prediction errors are computed not in sepa-
rate units, but locally in dendritic compartments. We then discuss the correspon-
dence of this model to experimentally observed connectivity patterns, plasticity,
and dynamics in cortex.

Neural models of inference in cortex
A central feature of perception is that our internal expectations to a large degree shape how we
perceive the world [1]. A long line of research aims to describe these expectation-guided compu-
tations in our brain by Bayesian inference (see Glossary) (i.e., statistically optimal perception)
and, subsequently, could show that Bayesian inference often captures perception extraordinarily
well [2,3] (for a critical discussion see also [4]). In light of these results, it has been proposed that
the primary computation that is performed by the cortex is a hierarchically organized inference
process, where cortical areas combine bottom-up sensory information and top-down expecta-
tions to ﬁnd a consistent explanation of sensory data [5–8].

While the general idea of hierarchical inference in cortex found considerable experimental support
[7,9,10], it is less clear how exactly this inference could be implemented by cortical neurons. A
popular theory to describe the neural substrate of inference in cortex is classical hierarchical
predictive coding (hPC) [6,11]. A central proposition of this theory is the existence of error
units, which are thought to compare top-down predictions with bottom-up inputs, and guide
neural computation and plasticity. However, classical hPC for the most part remains on the
level of ﬁring-rate dynamics of neural populations and it has proven difﬁcult to connect the theory
to the properties of single neurons with spiking dynamics [12,13].

Here we point towards a different, emerging theory of hierarchical inference in cortex, which relies
on the local membrane dynamics in neural dendrites. The core idea of this theory, which we will
refer to as dendritic hPC, is to shift error computation from separate neural populations into the
dendritic compartments of pyramidal neurons. We will ﬁrst discuss how this shift in perspective
enables a biologically plausible implementation of hPC with spiking neurons, and how it connects
hPC to theories of efﬁcient coding in balanced spiking networks [14] and neural sampling [2].
In the second part, we will discuss the biological plausibility of dendritic hPC, explain how several
experimental observations of hierarchical cortical computation ﬁt into the picture, and highlight
the experimental predictions that can be generated from the theory.

Highlights

Hierarchical predictive coding has been
considered one of the most promising
unifying theories of cortical computation.
Yet, in its classical form, it remains difﬁcult
to connect to single neuron physiology.

We review work that shows that hier-
archical predictive coding can be im-
plemented by neurons with dendritic
compartments, where prediction er-
rors are computed by the local volt-
age dynamics in the dendrites.

This connects the theories of predictive
coding and efﬁcient coding in balanced
networks and provides a solution to the
open problem of implementing predictive
coding with spiking neurons.

This also links predictive coding to corti-
cal physiology and voltage-dependent
plasticity, which offers new ways to test
for predictive coding in cortex.

1Max-Planck-Institute for Dynamics and
Self-Organization, Göttingen, Germany
2Göttingen Campus Institute for Dy-
namics of Biological Networks, Georg-
August University, Göttingen, Germany
3Bernstein Center for Computational
Neuroscience (BCCN), Göttingen,
Germany
4Department of Physics, Georg-August
University, Göttingen, Germany
5These authors contributed equally to
this work

*Correspondence:
fabian.mikulasch@ds.mpg.de
(F.A. Mikulasch).

Trends in Neurosciences, January 2023, Vol. 46, No. 1
https://doi.org/10.1016/j.tins.2022.09.007
45
© 2022 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

Trends in
Neurosciences
OPEN ACCESS

> Figure description (generated): Since no figure image was provided, I cannot generate the detailed description.

**Please provide the academic PDF figure you would like me to describe.**

Once you provide the image, I will structure my response according to your strict requirements:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration**

I await the figure to proceed with the exhaustive analysis as a senior neuroscientist and technical editor.


---

## Page 2

Dendritic predictive coding in balanced spiking neural networks
Classical models of predictive coding
Hierarchical predictive coding (hPC) describes the processing of sensory information as inference
in a hierarchical model of sensory data (see Box 1 for mathematical details, which are not needed
to understand the main text). The central idea of hPC is that activity of prediction units in one
level of the hierarchy:

(i) should accurately predict sensory data or the prediction unit activity in a lower level, and
(ii) should be consistent with top-down predictions generated by higher levels in the hierarchy.

hPC tries to understand how these properties of neural activity can be ensured by neural dynamics
on short timescales, and neural learning and plasticity on long timescales. The theory predicts that
to this end, the prediction units in every level of the hierarchy need access to two types of errors:

Box 1. Mathematical details of classical predictive coding

The goal in hPC is to maximize the model log-likelihood [11] (for a detailed tutorial see [134])

L ¼

X
N

i¼1

log pθ ri−1jri



;
½I

where θ are the model parameters, r i is neural activity of a neural network at level i, and inputs are provided by the previous
level r i−1. This deﬁnes a hierarchy of processing stages that, for example, can be associated with different visual cortical
areas (e.g., V1, V2, etc.), where r0 are visual inputs from LGN [11]. Typically, a linear model is assumed, where inputs
are modeled according to

ri−1 ¼ Diri þ ni−1;
½II

with decoding matrix D i and Gaussian white noise ni−1 with zero mean and variance σi−1

2. With this model, for a single level
i, the relevant contributions of the negative log-likelihood  Li take the intuitive form of the square sum of coding errors for
bottom-up inputs and errors of top-down predictions:

bottom‐up error :
ei−1 ¼ ri−1 −D iri;
top‐down error :
ei ¼ ri −D iþ1riþ1;
½III

Li ¼
1
2σ2
i1

ei1⊤ei1 þ
1
2σ2
i

ei⊤ei:
½IV

The goal is then to minimize the sum of coding errors on a fast timescale τr via neural dynamics d

dt ri, and with a slow learning
rate ηD via neural plasticity on the weights Di, by performing gradient ascent on L:

dynamics :
τr

d
dt ri ¼
1
σ 2

i1

Di⊤ei1  1

σ2

i

ei
½V

plasticity :
η1

D

d
dt Di ¼
1
σ2

i1

ei1ri⊤:
½VI

To yield a neural implementation, the key innovation in classical hPC was to represent prediction errors within a distinct
neural population of error units. Error units integrate inputs of prediction units within the same level and subtract top-down
predictions according to

τ e

d
dt ei ¼ −ei þ ri−Diþ1riþ1;
½VII

where decoding weights Di now correspond directly to weights of neural connections [134]. Together with the dynamics of
prediction units, this results in the hierarchical neural circuit shown in Figure 1A in the main text.

Trends in Neurosciences
OPEN ACCESS

> Figure description (generated): Since no figure image was provided, I cannot generate the detailed description.

**Please provide the academic PDF figure you would like me to describe.**

Once you provide the image, I will adhere strictly to your instructions and deliver a highly detailed, comprehensive, and exhaustive description structured as follows:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration (using the provided glossary terms if relevant to the figure's content)**

46
Trends in Neurosciences, January 2023, Vol. 46, No. 1

Glossary

Balanced spiking networks: recur-
rent networks of spiking neurons with
E-I balance; these networks show
asynchronous irregular spiking activity
and can efﬁciently encode dynamic vari-
ables.
E-I balance: excitatory and inhibitory
currents are ‘balanced’, when their
magnitude approximately matches.
Hierarchical predictive coding
(hPC): a theory of hierarchical inference
in cortex.
Inference: in hPC, inference is the
process of ﬁnding the underlying causes
of sensory data; these underlying
causes can be used to predict (or simi-
larly, ‘explain away’) the sensory input or
the activity in lower levels of the hierar-
chy.
Lateral inhibition: pyramidal neurons
in a population compete via lateral inhi-
bition through interneurons, which can
be used to both increase the efﬁciency of
the neural code and to distinguish
between competing explanations of
sensory data.
Neural sampling: instead of comput-
ing a single best explanation of sensory
data, neural activity can sample possible
explanations according to their likeli-
hood.
Prediction neuron: pyramidal neuron
that aims to predict the activity of other
neurons, as proposed by dendritic hPC.
Prediction unit: abstract unit of neu-
rons that aims to predict the activity of
other units, as proposed by classical
hPC.
Pyramidal neuron: the primary excit-
atory neuron in cortex, typically with a
characteristic long ‘apical’ dendrite.
Tight balance: if the E-I balance is
present not only on average, but also on
short timescales, it is ‘tight’.
Voltage-dependent plasticity (VDP):
changes in synaptic strength that
depend on the postsynaptic membrane
potential in the vicinity of the synapse.

> Figure description (generated): Since no image was provided, I cannot generate the detailed description of Figure 1.

**Please provide the figure you wish me to describe.**

Once you provide the image, I will adhere strictly to your instructions and deliver a highly detailed, comprehensive, and exhaustive description structured as follows:

1. **Overall Layout & Structure**: (e.g., Schematic diagram, multi-panel layout)
2. **Visual Components & Symbols**: (Detailed description of nodes, connections, flow direction)
3. **Labels, Keys & Legends**: (Listing all text, variables, and annotations)
4. **Data Trends & Details**: (If applicable to plots/graphs)
5. **Contextual Caption Integration**: (Explaining elements based on the provided caption context)


---

## Page 3

(i) bottom-up errors (i.e., the mismatch between activity in lower levels and predictions gener-

ated within the level);
(ii) top-down errors (i.e., the mismatch between activity within the level and top-down predictions

from higher levels).

In classical hPC [11], the key innovation was to represent these errors in distinct populations of error
units that compare top-down predictions with the activity within a level (Figure 1A, Key ﬁgure). The
elegance of this approach is that the same error units can mediate both, bottom-up errors to update
prediction units in the next level, as well as top-down errors to neurons of the same level. Another
central result of classical hPC is that the learning rules that improve the hierarchical model take the
form [error × prediction], which turns out to be classic Hebbian plasticity (i.e., the multiplication of
pre- and postsynaptic activity).

A functionally equivalent formulation of predictive coding with dendritic error computation
Although the idea of error units is undeniably elegant, it is not the only way to compute prediction
errors in a neural circuit. More recent models showed that error computation can also be per-
formed in the voltage dynamics of individual dendritic compartments [14–16] and, thus, without
specialized error units. Combining these models allows for a reinterpretation of hPC, which we
term dendritic hPC, where every prediction neuron will represent the two types of errors we
discussed before in different sections of its dendritic tree (Figure 1B, see Box 2 for mathematical
details):

Key figure
Implementation of predictive coding with dendritic error computation and spiking neurons

Trends
Trends in
in Neurosciences
Neurosciences

Figure 1. (A) Illustration of the classical model of hierarchical predictive coding (hPC). Errors and predictions are computed in different neural populations within one level of
the hierarchy. Errors are sent up the hierarchy, while predictions are sent downwards. (B) In dendritic hPC, prediction neurons implement the same function, but errors are
computed in neural dendrites. Predictions are sent up the hierarchy to basal dendrites, where they are balanced by lateral connections to compute bottom-up prediction
errors (left). At the same time, predictions are sent down the hierarchy to apical dendrites, where they try to predict somatic spiking and guide the inference process (right).
The pathways are shown separately for better visibility. (C) Dendritic hPC can be implemented with spiking neurons. The errors that are computed in the dendritic
membrane potentials are integrated at the soma to form an overall error signal of the neuron’s encoding. A spike is emitted when the somatic error potential grows too
large and a spike would lead to a reduction in the overall error.

> Figure caption (from PDF text): Figure 1. (A) Illustration of the classical model of hierarchical predictive coding (hPC). Errors and predictions are computed in different neural populations within one level of
the hierarchy. Errors are sent up the hierarchy, while predictions are sent downwards. (B) In dendritic hPC, prediction neurons implement the same function, but errors are
computed in neural dendrites. Predictions are sent up the hierarchy to basal dendrites, where they are balanced by lateral connections to compute bottom-up prediction
errors (left). At the same time, predictions are sent down the hierarchy to apical dendrites, where they try to predict somatic spiking and guide the inference process (right).
The pathways are shown separately for better visibility. (C) Dendritic hPC can be implemented with spiking neurons. The errors that are computed in the dendritic
membrane potentials are integrated at the soma to form an overall error signal of the neuron’s encoding. A spike is emitted when the somatic error potential grows too
large and a spike would lead to a reduction in the overall error.
> Figure description (generated): ## Detailed Figure Description: Implementation of Predictive Coding with Dendritic Error Computation and Spiking Neurons

This figure, titled "Implementation of predictive coding with dendritic error computation and spiking neurons," is structured into three main panels: (A), (B), and (C), illustrating different computational models of predictive coding.

### 1. Overall Layout & Structure
The figure is organized horizontally into three distinct schematic sections: (A) Classical predictive coding, (B) Dendritic predictive coding, and (C) Implementation with spiking neurons. Each panel uses a schematic representation of neural circuits to illustrate information flow and computation across hierarchical levels.

### 2. Visual Components & Symbols
**General Circuit Elements:**
*   **Units (Nodes):** Represented by circles ($\circ$). These nodes are organized into vertical columns, representing different neural populations or levels.
*   **Error/Prediction Signals:** Represented by triangles ($\blacktriangle$). These are shown associated with the units.
*   **Connections:** Represented by lines connecting the nodes.
    *   **Excitation (Red/Orange):** Indicated by red or orange lines.
    *   **Inhibition (Blue):** Indicated by blue lines.
    *   **Dendrites (Black/Gray):** Represented by thin black lines connecting nodes, particularly in Panel B.
*   **Levels:** Indicated by horizontal groupings of units, with a label "Level" next to the nodes.

**Panel (A): Classical Predictive Coding**
*   This panel shows a layered structure with multiple levels. Within each level, units are connected both vertically (between levels) and horizontally (within the same level).
*   The flow shows predictions ($\blacktriangle$) moving downwards and errors ($\circ$ associated with $\blacktriangle$) moving upwards between levels.

**Panel (B): Dendritic Predictive Coding**
*   This panel is divided into two sub-schematics: "Bottom-up pathway" (left) and "Top-down pathway" (right).
*   **Bottom-up Pathway:** Shows a circuit where predictions are sent up to basal dendrites. Lateral connections within the dendritic structure appear to balance these signals to compute bottom-up prediction errors.
*   **Top-down Pathway:** Shows predictions being sent down to apical dendrites, which are shown interacting with somatic spiking mechanisms.
*   The schematic emphasizes the internal dendritic structure (represented by thin lines) where computation occurs, distinct from the classical nodal representation.

**Panel (C): Implementation with Spiking Neurons**
*   This panel is a block diagram illustrating the integration of dendritic computation into spiking neuron dynamics. It is divided vertically into "Higher level" and "Lower level."
*   **Higher Level:** Shows a schematic of a neuron with dendrites and a soma. An arrow points from the dendritic computation down to the somatic integration point.
*   **Lower Level:** Shows a detailed representation of the dendritic computation, including multiple input lines representing Excitation (red/orange), Inhibition (blue), and the resulting Error signal.
*   **Somatic Integration:** The soma integrates these inputs, leading to the emission of a spike when the somatic error potential crosses a threshold.

### 3. Labels, Keys & Legends
**Legend/Key:**
*   $\circ$: Error
*   $\blacktriangle$: Prediction

**Text Labels:**
*   **(A)** Classical predictive coding
*   **(B)** Dendritic predictive coding
    *   Bottom-up pathway
    *   Top-down pathway
*   **(C)** Implementation with spiking neurons
    *   Higher level
    *   Lower level

**Internal Annotations (Panel C):**
*   "Spike-based error minimization" is labeled above the higher level schematic.
*   "Dendritic error computation" labels the lower level circuit.
*   Lines within the lower level are explicitly labeled: "Excitation," "Error," and "Inhibition."

### 4. Data Trends & Details
Panel (C) includes schematic representations of signals rather than quantitative plots:
*   **Overall Error:** Shown as a fluctuating signal line in the higher level, indicating the integrated error.
*   **Dendritic Signals (Lower Level):** Show distinct, fluctuating waveforms for Excitation, Error, and Inhibition inputs feeding into the soma.

### 5. Contextual Caption Integration
The caption clarifies the function of the elements:
*   **Panel (A):** Errors are computed in neural populations, sent up the hierarchy; predictions are sent down.
*   **Panel (B):** In dendritic hPC, errors are computed in dendrites. Predictions travel up to basal dendrites for bottom-up error calculation (left), and down to apical dendrites to guide inference via somatic spiking (right).
*   **Panel (C):** Dendritic error potentials are integrated at the soma to form an overall error signal. A spike is emitted when this somatic error potential becomes sufficiently large, leading to a reduction in the overall error.

Trends in Neurosciences

OPEN ACCESS

Trends in Neurosciences, January 2023, Vol. 46, No. 1
47


---

## Page 4

(i) bottom-up errors in basal dendritic compartments [16], where input from lower-level cortical

areas is integrated [17];
(ii) the top-down prediction error (for the neuron’s own activity) in an apical compartment [15],

where higher-level cortical feedback arrives [17].

Besides the absence of error units, two additional central differences arise between the architec-
tures of classical and dendritic hPC. First, in dendritic hPC both bottom-up and top-down signals
are predictions, a possibility that has been discussed before [18]. Second, and more importantly,
while prediction units in classical hPC inhibit each other through error units, prediction neurons in
dendritic hPC directly compete through lateral inhibition on basal dendrites. Such networks
with strong lateral inhibition (or similarly, winner-take-all-like dynamics [19]) have a long tradition
in theoretical neuroscience, as models for the sparse and efﬁcient encoding of sensory data
[16,20–25] and as divisive normalization models of cortical computation [26,27]. Dendritic hPC

Box 2. Mathematical details of dendritic predictive coding

In dendritic hPC, the computation of errors in Equation VII is accomplished by the leaky voltage dynamics of dendritic
compartments. Different models have explored this idea separately for basal dendrites [16,25,40] and apical dendrites
(also with nonlinearities, which we here omit) [15,28], which we here combine to form a model that is equivalent to classical
hPC. To this end, for each prediction neuron j, one introduces basal dendritic compartments bjk

i ≈Dkj

i ek

i−1, which are each
innervated by a single synapse of a prediction neuron k of the previous level [16], as well as an apical compartment aj

i ≈−ej

i

that is innervated by prediction neurons of a higher level [15] (see Figure 1B in the main text). The error computation is then
performed by voltage dynamics according to

τ b

d
dt bi

jk ¼ −bi

jk þ Di

kjr i−1

k −

X

l

Wi

jklr i

l;
½VIII

τ a

d
dt ai

j ¼ −ai

j −r i

j þ

X

l

Diþ1

jl
r iþ1

l
;
½IX

where bottom-up inputs are balanced with lateral connections Wjkl

i (connection of neuron rl

i to the kth dendritic compartment
of neuron rj

i), and top-down predictions are matched by the neurons own predictions rj

i. The latter has been proposed to be
implemented via the backpropagating action potential [15], solving the one-to-one connections problem of classical hPC
[135]. To compute bottom-up errors, lateral weights have to be chosen as Wjkl

i = Dkj

i Dlj

i. Such weights can be found through
a voltage-dependent plasticity rule, which enforces a tight balance in the kth dendritic compartment [16]

η−1

W

d
dt Wi

jkl ¼
1
σ2

i−1

bi

jkr i

l :
½X

The dynamics of prediction neurons are then simply driven by the dendritic error potentials

τ r

d
dt r i

j ¼
1
σ2

i−1

X

k

bi

jk þ 1

σ2

i

ai

j;
½XI

and weights for bottom-up and top-down inputs can be learned with voltage-dependent rules (Equation XII proposed in
[16], Equation XIII proposed in a generalized form in [15])

η−1

D

d
dt Di

kj ¼
1
σ2

i−1

1
Di

kj

bi

jkr i

j;
½XII

η−1

D

d
dt Diþ1

jl
¼ −1

σ2

i

ai

jr iþ1

l
:
½XIII

Here, learning of bottom-up weights requires that lateral and bottom-up weights always align via Wjkl

i = Dkj

i Dlj

i, which in
classical hPC is known as the weight transport problem [49,135]. For dendritic hPC a solution based on weight decay
has been proposed in [16], which was demonstrated in a single-level model and is similar to a solution proposed for
classical hPC [49]. Together, these equations yield an equivalent formulation of hPC for both learning and inference, where
prediction errors are computed locally in dendritic compartments.

Trends in Neurosciences
OPEN ACCESS

> Figure description (generated): Since no figure was provided, I cannot generate the detailed description. Please provide the image you would like me to describe.

Once you provide the figure, I will structure my response according to your requirements:

1. **Overall Layout & Structure**: Detailed description of the figure's organization.
2. **Visual Components & Symbols**: Exhaustive breakdown of all graphical elements, connections, and flow.
3. **Labels, Keys & Legends**: Transcription of all text, variables, and annotations within the figure.
4. **Data Trends & Details**: Analysis of any plots or graphs present.
5. **Contextual Caption Integration**: Explanation linking visual elements to the provided caption context.

48
Trends in Neurosciences, January 2023, Vol. 46, No. 1


---

## Page 5

is closely related to these models, except that in these models it was not considered how exactly
top-down connections could guide neural computations with predictions. In a more general
context it has been proposed that top-down connections could provide these predictions by
targeting apical dendrites [15,28–31]. Dendritic hPC combines these ideas of lateral competition
and top-down predictions into a coherent theory of hierarchical inference in cortex.

Since in dendritic hPC error computation takes place in the voltage dynamics of basal and apical
dendritic compartments, these local potentials play an important role for synaptic plasticity. For
basal dendrites, dendritic hPC predicts that plastic lateral connections compute the errors for
bottom-up inputs by establishing a tight balance locally in individual dendritic compartments
(i.e., trying to closely match excitatory with inhibitory currents [32]). The intuitive explanation for
this computation is that in a tightly balanced state, every input that can be predicted from other
neurons is effectively canceled and the remaining unpredictable input constitutes the prediction
error [14,16]. These errors can then be exploited by another voltage-dependent rule for
bottom-up connections, in order to ﬁnd an optimal encoding of inputs [16]. This learning rule is
Hebbian-like (i.e., pairing postsynaptic ﬁring with presynaptic input will induce potentiation of
the synapse). At the same time, strong local inhibition during the postsynaptic spike would signal
an over-prediction of the input and consequently should lead to long-term depression of the
synapse. For apical dendrites, it has been proposed that error computation relies on the
mismatch between apical prediction and somatic spiking [15]. In this theory of apical learning,
plasticity of top-down connections is Hebbian-like as well, but synapses are depressed for a
depolarization of the apical dendritic potential in the absence of somatic spiking. By employing
these voltage-dependent plasticity (VDP) rules, dendritic hPC implements the same learning
algorithm as classical hPC, but in prediction neurons with dendritic error computation (Box 2).

Dendritic error computation has also been used in a different context to implement the
backpropagation algorithm in a cortical microcircuit [33–36]. Although this model of dendritic
error backpropagation and dendritic hPC employ similar ideas, they ultimately pursue different
goals and thus make distinct predictions for plasticity and E-I balance in basal and apical
dendritic compartments (Figure 2).

Dendritic errors enable an efﬁcient implementation of hPC with spiking neurons
Dendritic errors do not only yield an equivalent formulation of hPC, they also enable inference with
spiking neurons. Here, the inferred variables have to be efﬁciently represented by spikes, which is

Trends
Trends in
in Neurosciences
Neurosciences

Figure 2. Relation of dendritic
predictive coding to dendritic
microcircuits
for
error
backpropagation. (Left) In dendritic
hierarchical predictive coding (hPC)
the goal is to generate predictions
of bottom-up sensory inputs. Here
prediction errors are computed via
balancing inhibition to basal dendrites
and
the
mismatch
of
top-down
predictions and somatic spiking at
apical dendrites. (Right) In models
that employ backpropagation the
goal is to generate a target output at the highest level (e.g., a label) [33]. To this end an ‘inverted’ model of hPC is employed [35],
where balancing inhibition at the apical dendrite is used to compute the backpropagated error of the output. While thorough testing
of both theories remains to be conducted, a recent study indicates that pyramidal neurons learn predictive (and not balanced) apical
activity [31], more consistent with dendritic hPC. However, this particular observation of course would not rule out that cortical
networks could make use of both proposed mechanisms in different modes of operation or different neural populations.

Trends in Neurosciences

OPEN ACCESS

Trends in Neurosciences, January 2023, Vol. 46, No. 1
49


---

## Page 6

possible if spikes are only ﬁred if they reduce the overall prediction error [14,37,38] (see Box 3 for
the mathematical details of dendritic hPC with spiking neurons). Since in dendritic hPC prediction
errors are represented in the balanced membrane potentials, an efﬁcient spike encoding can be
found with a simple threshold mechanism that generates a spike when the error potential grows
too large (Figure 1C), as demonstrated in single-level models [39,40]. Predictive coding thus
serves a dual purpose in dendritic hPC, by enabling both inference in a hierarchical model and
an efﬁcient spike encoding of dynamical variables.

A central role in this inference scheme with spikes is played by noise in the neural dynamics, for
two reasons. First, noise enables an efﬁcient spike encoding in the face of transmission delays.
With deterministic neurons, even a small delay of inhibition can lead to erratic network behavior,
since inhibition will often arrive too late to prevent synchronous spiking of large parts of a

Box 3. Mathematical details of dendritic predictive coding with spikes

Spike-based predictions of sensory data

A popular choice to mathematically formalize the prediction generated by a spike at time tsp is via spike traces κ(t,tsp) =
exp(−(t −tsp)/τ) that decay exponentially with some time constant τ [16,40]. Predictions of a neuron then change upon a
spike according to r(t) →r(t) + κ(t,tsp), which approximately corresponds to the way spikes are read out in the
membranes of postsynaptic neurons. With these predictions r(t), the same formalism as before can be used to compute
the instantaneous log-likelihood (see Box 1 in the main text):

L tð Þ ¼

X
N

i¼1

log pθ ri−1 tð Þjri tð Þ




:
½XIV

However, due to the discontinuous nature of spikes, inference can no longer be implemented by simple gradient ascent.

Efficient spiking implementation of predictive coding with dendritic errors

One straightforward approach to implement inference with spikes is to deterministically ﬁre a spike at time t if it instantly
improves bottom-up and top-down errors, that is, the log-likelihood L(t) [40]:

L tjneuron jspikes at time t
ð
Þ > L tjno spike at time t
ð
Þ:
½XV

This can be seen as a discrete implementation of gradient ascent to ﬁnd the instantaneous maximum a posteriori (MAP)
estimate for predictions rj

i. From this principle it can be derived that a neuron should spike if its balanced membrane
potential uj

i(t) surpasses a ﬁring threshold Tj [40], that is, if

ui

j tð Þ ¼
1
σ2

i−1

X

k

bi

jk þ 1

σ 2

i

ai

j > T j:
½XVI

This equation is analogous to Equation XI, where bjk

i (t) are the balanced dendritic potentials of basal dendrites and aj

i(t) the
potential of the apical dendrite.

Predictive coding with neural sampling

A more general approach to inference with spikes is to sample a (binary) spike train S0:T = {si(t)|i ∈{1,…,N},t ∈{0,…,T}}
from the posterior distribution of the generative model S0:T ∼pθ(S0:T|r0:T

0) [16,136]. The posterior is implicitly deﬁned via
the model pθ(ri-1(t)|ri(t)), a prior on spiking pθ(sN(t)) and spike traces r i(t) = ∑t′=0

t si(t′)κ(t,t′). While computing the posterior
distribution exactly is intractable [16,136], approximate online sampling can be implemented with the same membrane
potentials uj

i(t) and threshold Tj as before (up to a constant factor) and a soft spiking threshold mechanism

p neuron j spikes at timet
ð
Þ ¼ sig ui

j tð Þ −T j



;
½XVII

where sig(x) = 1/(1 + exp(−x)) is the logistic function [16]. Note, that uj

i(t) and Tj are scaled by the precisions of errors 1

σ2

i
(Equation XVI) and thus the stochasticity of spiking will capture the uncertainty in inference. This model is a special case
of the spike response model with escape noise [137] and can be implemented by a leaky-integrate-and-ﬁre neuron with
a noisy membrane potential. Equations XI, XVI, and XVII highlight the intimate relation that exists between the theories of
hPC, efﬁcient coding with spikes, and neural sampling.

Trends in Neurosciences
OPEN ACCESS

> Figure description (generated): Since no figure was provided, I cannot generate the detailed description. Please provide the image you would like me to describe.

Once you provide the figure, I will structure my response according to your requirements:

1. **Overall Layout & Structure**: Detailed description of the figure's organization.
2. **Visual Components & Symbols**: Exhaustive breakdown of all graphical elements, connections, and flow.
3. **Labels, Keys & Legends**: Transcription of all text, variables, and mathematical notations within the figure.
4. **Data Trends & Details**: Specific analysis of any plots or graphs present.
5. **Contextual Caption Integration**: Explanation linking visual elements to the provided caption's context.

50
Trends in Neurosciences, January 2023, Vol. 46, No. 1


---

## Page 7

population [41]. Noise relaxes this constraint on the speed of feedback, since it effectively decou-
ples and desynchronizes neural spiking [37,41,42]. Second, noise in spiking neural networks en-
ables neural sampling [2,43–46]. Here, the idea is that neural activity samples possible predictions
according to their likelihood, instead of computing a single best estimate as in classical hPC (Box 3).
Neural sampling therefore is a principled way to represent uncertainty in inference via neural activity
and has, for example, been used to explain variability in neural responses [47,139] and the origin of
multistability in perception [48]. Recent models show that neural sampling and efﬁcient spike coding
with tight E-I balance can be combined in a single model with dendritic error computation [16,43], re-
lating these concepts to the proposed model of dendritic hPC (Box 3).

In addition to neural inference, dendritic errors also enable learning in populations of spiking
neurons. This is not straightforward, since the switch from rate-based to spike-based models
typically requires a modiﬁcation of the learning algorithms. For example, when using spiking
error units, as in classical hPC, it is not directly possible to represent both positive and negative errors
by non-negative activity [49]. To resolve this, it was proposed that errors are represented by devia-
tions relative to a baseline ﬁring rate [49], but this would require high ﬁring rates and therefore
seems implausible considering the low ﬁring rates in neocortex [50]. An alternative is to represent pos-
itive and negative errors in separate populations [11,50], but it is unclear how in this case biological
plasticity can recombine the positive and negative parts, which are both required for the learning of
single synapses. Due to these difﬁculties, to date, no complete implementation of hPC that uses spik-
ing error units has been proposed [13]. By contrast, in dendritic hPC the same learning algorithm as
for rate-based units can be straightforwardly applied to spiking neurons. The reason is that dendritic
membrane potentials remain continuous quantities, despite the spiking nature of neural activity, and
thus can easily represent the prediction errors that are required for the learning of bottom-up and top-
down connections (Box 2), which has been successfully applied in [15,16].

Is dendritic predictive coding biologically plausible?
In the previous section we have introduced the two main assumptions of dendritic hPC, which are: (i)
cortex implements inference in a hierarchical probabilistic model, and (ii) errors of the resulting predic-
tions are computed in the local voltage dynamics of basal and apical dendrites. The implications of the
ﬁrst assumption have been discussed at length in the context of classical hPC and were found to align
well with experimental observations [7,10,51]. In the following we will discuss the biological plausibility
of the second assumption. Ultimately, we will argue that dendritic hPC can indeed be closely con-
nected to many properties of pyramidal neurons and inhibitory connectivity in cortex.

Dendritic error computation and synaptic plasticity in pyramidal neurons
To compute errors in basal dendrites, a tight and local E-I balance is required. Indeed, it has been
found in several instances that inhibitory and excitatory currents are tightly correlated, with inhibi-
tion trailing excitation by few milliseconds [14,52,53]. This tight balance leaves neurons only with a
brief window of opportunity for spiking, which effectively decorrelates neural responses to inputs
and thereby ensures an efﬁcient neural code [25]. A tight E-I balance can therefore explain the
origin of the irregular spiking patterns of neurons that have been observed throughout cortex
[14,54]. Although models with a tight balance can reproduce irregular ﬁring on the single neuron
level, incorporating realistic synaptic transmission delays in these models can lead to oscillations
on the population level [37]. Oscillations in cortical activity in the gamma frequency band have
therefore been discussed as signatures of efﬁcient coding in balanced networks [42] (and
might also support efﬁcient neural sampling [45,55]).

Consistent with dendritic hPC, this balance has also been found to extend to individual dendritic
compartments [32,56,57]. Crucially, this local balance can be observed down to the scale of

Trends in Neurosciences

OPEN ACCESS

Trends in Neurosciences, January 2023, Vol. 46, No. 1
51


---

## Page 8

(at least) single dendritic branches [56], since the attenuation of dendritic currents prevents that inhib-
itory postsynaptic potentials spread into other dendritic branches and inﬂuence the E-I balance there
[58,59]. Experiments could also show that this local balance is maintained through localized synaptic
plasticity, which re-establishes the balance after a perturbation and coordinates excitatory and inhib-
itory plasticity locally [56,60–65]. Overall, these ﬁndings are compatible with the idea that a local
balance can compute prediction errors for speciﬁc synaptic contacts at basal dendrites.

Another prediction of dendritic hPC, which has been consistently observed in a range of experi-
ments, is that the local membrane potential is a central determinant of synaptic plasticity
[61,65–68]. This VDP is thought to be mainly mediated by the local calcium concentration,
which follows the local membrane potential and modulates synaptic plasticity [59,69,70].
Based on these observations, VDP rules have been proposed that can reproduce several exper-
iments of spike-timing-dependent plasticity in a uniﬁed picture [71–73]. An especially important
consequence of locally organized VDP, which is also required by dendritic hPC, is that inhibition
can strongly modulate synaptic plasticity in a very localized manner [32,65,74–76].

Are the VDP rules that can be derived from dendritic hPC consistent with these experimentally
observed VDP rules? A distinction has to be made here between VDP rules in basal dendrites,
which should enable the learning of neural representations [16], and VDP in apical dendrites,
which should enable the prediction of somatic spiking [15]. For representation learning in basal
dendrites, we have argued in [16] that previously proposed VDP rules [71,72] can be reconciled
with the VDP rules derived from dendritic hPC. One prediction of these derived VDP rules is that
strong local inhibition should promote the depression of excitatory synapses, an effect that has
been observed in proximal dendrites of hippocampal pyramidal neurons [75] (similarly found in
[77]). By contrast, for the learning of apical connections, an explicit correspondence to experi-
mental VDP still has to be proposed. Experiments show that synaptic plasticity close to and far
from the soma behaves vastly differently [31,78–80], which could support the different require-
ments for basal and apical synaptic plasticity in dendritic hPC. While more experimental and
theoretical work is needed to clarify the connections between dendritic hPC and experimental
VDP, these results suggest that cortical pyramidal neurons in principle are suited to implement
the learning algorithm proposed by dendritic hPC.

A diversity of inhibitory interneurons is required for dendritic predictive coding
Since pyramidal neurons in general only excite other cells, additional inhibitory interneurons are
required to implement the dendritic hPC model. The central inhibitory motif of dendritic hPC
requires interneurons that balance bottom-up inputs to basal dendrites via lateral connections
[16,25]. These interneurons show strong similarities to parvalbumin-expressing (PV) interneurons
in cortex, which implement a precisely adjusted competition between pyramidal neurons
[24,81–84]. PV positive, fast-spiking basket cells alone make up around 30–50% of all interneu-
rons in the cortical microcircuit [85] and are especially adapted to tightly control pyramidal neuron
spiking and the cortical E-I balance via very fast inhibition to somata and basal dendrites [86,87].
PV interneurons also seem to be responsible for the gamma oscillations that similarly arise
through lateral inhibition in dendritic hPC [87–89]. Dendritic hPC is therefore closely linked to
one of the deﬁning inhibitory motifs of cortex.

Next to PV interneurons, most other interneurons in cortex can be classiﬁed as either
somatostatin-expressing (SST) interneurons, which preferentially target the apical dendrites of
pyramidal neurons, or vasoactive intestinal peptide-expressing (VIP) interneurons, which mainly
inhibit other interneurons, especially SST [86,90]. SST and VIP interneurons, for example, have
been observed to be responsible for top-down inhibitory control [91], which is also required in

Trends in Neurosciences
OPEN ACCESS

52
Trends in Neurosciences, January 2023, Vol. 46, No. 1


---

## Page 9

dendritic hPC when top-down input predicts a decrease in activity. However, not all of the major
connectivity patterns of SST and VIP cells can be straightforwardly explained by dendritic hPC:
SST interneurons, for example, also mediate short-range lateral inhibition to apical dendrites,
which allows them to contribute to surround suppression [92] and to gate top-down input
[93,94]. The disinhibitory circuit of VIP contributes to this gating mechanism by speciﬁcally
suppressing SST neurons during active behavior [93,95,96]. SST and VIP neurons have also
been found to be crucial for gating apical plasticity, for example, during reward-based learning
[97–99]. These connectivity motifs thus play a central role in how predictions are processed by
apical dendrites, but precisely what functions they could implement, especially in the context of
dendritic hPC, has yet to be understood [65].

Dendritic predictive coding in neocortical lamination
Neocortex employs multiple types of pyramidal neurons that reside on different cortical layers and
exhibit speciﬁc connectivity [17]. We here propose that dendritic hPC in particular describes the
computations of layer 2/3 neurons (Figure 3D). That layer 2/3 neurons are central in the hierarchi-
cal integration of information and the interpretation of sensory data has been proposed before, for
example, based on cortical physiology [19] or in theories of classical hPC, where errors and pre-
dictions are ﬁrst computed in layer 2/3 [6] (Figure 3C). There are several arguments for why den-
dritic hPC is particularly well suited to describe layer 2/3: ﬁrst, like in dendritic hPC, layer 2/3
neurons combine bottom-up signals (sent from layer 4 to their basal dendrites) with top-down

(A)

(B)

(C)
(D)

Trends
Trends in
in Neurosciences
Neurosciences

Figure 3. How could dendritic predictive coding be embedded into neocortical microcircuits and lamination? (A) Core circuitry of mammalian neocortex, as
shown in [102,104]. Input neurons in layer 4 (green) receive sensory information from the dorsal thalamus, layer 2/3 intratelencephalic (IT) neurons (blue) further process this
information, and output neurons in layer 5 (red) project to the brainstem and other areas. Additional connections, for example, from thalamus to layer 1 (mostly relayed from
other cortical areas [94]) or layer 5 (broken lines), or within layer 2/3 between areas exist [17,138], but will be omitted in the following for simplicity. (B) Theories of cortical
evolution hypothesize that these input, IT, and output cells are homologous to cells that existed in the ancestral amniote pallium [104]. Also, in birds and non-avian reptiles,
homologous cell types exist, but are organized in architectures that differ from the laminar organization of mammalian neocortex. (C) The predictive coding microcircuit as
proposed by [6] (here presented in a simpliﬁed form) follows the organization of the neocortical microcircuit. Predictions (ri) and prediction errors (ei) are computed in layer 2/
3. Deeper layers mainly act as communication hubs by copying signals from layer 2/3. (D) Speculative microcircuit for dendritic predictive coding. Here, deeper layers fulﬁll
the same role as communication hubs (and possibly complementary functions [19]), but layer 2/3 only computes predictions.

> Figure caption (from PDF text): Figure 3. How could dendritic predictive coding be embedded into neocortical microcircuits and lamination? (A) Core circuitry of mammalian neocortex, as
shown in [102,104]. Input neurons in layer 4 (green) receive sensory information from the dorsal thalamus, layer 2/3 intratelencephalic (IT) neurons (blue) further process this
information, and output neurons in layer 5 (red) project to the brainstem and other areas. Additional connections, for example, from thalamus to layer 1 (mostly relayed from
other cortical areas [94]) or layer 5 (broken lines), or within layer 2/3 between areas exist [17,138], but will be omitted in the following for simplicity. (B) Theories of cortical
evolution hypothesize that these input, IT, and output cells are homologous to cells that existed in the ancestral amniote pallium [104]. Also, in birds and non-avian reptiles,
homologous cell types exist, but are organized in architectures that differ from the laminar organization of mammalian neocortex. (C) The predictive coding microcircuit as
proposed by [6] (here presented in a simpliﬁed form) follows the organization of the neocortical microcircuit. Predictions (ri) and prediction errors (ei) are computed in layer 2/
3. Deeper layers mainly act as communication hubs by copying signals from layer 2/3. (D) Speculative microcircuit for dendritic predictive coding. Here, deeper layers fulﬁll
the same role as communication hubs (and possibly complementary functions [19]), but layer 2/3 only computes predictions.
> Figure description (generated): This figure, titled "How could dendritic predictive coding be embedded into neocortical microcircuits and lamination?", is divided into four distinct panels: (A), (B), (C), and (D). The overall style is a combination of schematic diagrams representing neural circuitry and layered structures.

### Panel (A): Mammalian Neocortex
Panel (A) depicts a cross-section of the mammalian neocortex, illustrating its layered structure.
*   **Structure:** It shows a vertical stack of layers labeled L1 through L6, representing the cortical lamination.
*   **Cellular Representation:** Within these layers, there are schematic representations of neurons using colored dots:
    *   Green dots are shown primarily in Layer 4 (L4).
    *   Blue dots are shown primarily in Layers 2/3 (L2/3).
    *   Red dots are shown primarily in Layer 5 (L5).
*   **Connectivity:** Dashed lines indicate connections between these layers. Specifically, there are curved arrows suggesting processing flow:
    *   An arrow originates from L4 (green) and moves towards L2/3.
    *   Another arrow originates from L2/3 (blue) and moves towards L5.
    *   A curved arrow suggests feedback or processing flow involving the layers.

### Panel (B): Ancestral Pallium
Panel (B) illustrates a simplified evolutionary model of cortical organization, contrasting it with the laminar structure in Panel (A).
*   **Structure:** It shows three main components connected by arrows: "Dorsal thalamus," a central processing unit labeled "IT" (Intratelencephalic), and "Brainstem."
*   **Connectivity:** Arrows indicate information flow:
    *   An arrow points from "Dorsal thalamus" to the central processing unit.
    *   An arrow points from the central processing unit to "Brainstem."
    *   A separate, curved arrow indicates a feedback loop from the central processing unit back towards the "Dorsal thalamus."

### Panel (C): Classical Predictive Coding
Panel (C) presents a schematic of the predictive coding microcircuit, aligned with neocortical organization.
*   **Layers:** The diagram is structured vertically, referencing cortical layers: L2/3 and L5.
*   **Nodes & Variables:** There are several nodes representing computational units:
    *   In Layer 2/3, there is a node labeled $e_{i+1}$ (Prediction Error).
    *   In Layer 2/3, there is a node labeled $r_i$ (Prediction).
    *   In Layer 5, there is a node labeled $r_i$ (Prediction).
*   **Flow & Connections:** Arrows depict the flow of information:
    *   An arrow points from $r_i$ (L2/3) to $e_{i+1}$ (L2/3), labeled "Forward prediction error."
    *   An arrow points from $e_{i+1}$ (L2/3) to $r_i$ (L5), labeled "Backward prediction."
    *   A connection is shown between the L2/3 and L5 nodes, indicated by a label "(Copy)" near both.
    *   An arrow points from $r_i$ (L5) back towards the L2/3 region, labeled "Backward prediction."
    *   An arrow points from $r_i$ (L2/3) towards the L5 node, labeled "Forward prediction error."

### Panel (D): Dendritic Predictive Coding
Panel (D) presents a speculative microcircuit model for dendritic predictive coding, differing from Panel (C).
*   **Layers:** This diagram also implies a layered structure, though the focus is on the computational nodes.
*   **Nodes & Variables:** The key difference lies in how predictions and errors are computed:
    *   In the upper region (analogous to L2/3), there is a node labeled $r_i$ (Prediction).
    *   In the lower region (analogous to L5), there is a node labeled $r_i$ (Prediction).
*   **Flow & Connections:** The connections emphasize the role of prediction:
    *   An arrow points from $r_i$ (upper node) downwards to the lower node, labeled "Forward prediction."
    *   An arrow points from the lower node upwards to $r_i$ (upper node), labeled "Backward prediction."
    *   Both nodes are accompanied by the label "(Copy)," suggesting a role as communication hubs, similar to Panel (C).

Trends in Neurosciences

OPEN ACCESS

Trends in Neurosciences, January 2023, Vol. 46, No. 1
53


---

## Page 10

signals (sent from layer 5 or layer 2/3 to their apical dendrites) [6,17,19]. Second, layer 2/3 neu-
rons exhibit sparse activity, which is mainly enforced by lateral inhibition via PV interneurons
[83,84,100], a motif that is present in dendritic hPC but not in other theories of hPC [6,35].
Last, superﬁcial cortical layers show pronounced gamma oscillations [6,88,89] that are expected
to arise through lateral inhibition in dendritic hPC [37,42].

Importantly, these properties implied by dendritic hPC are not general features of pyramidal
neurons, which in other layers likely implement different functions. Layer 5 neurons, for example,
employ a dense and not a sparse code [100] and show less gamma oscillations [6,89]. These
properties, together with the position of layer 5 neurons as downstream elements in the microcir-
cuit [17], have led to the suggestion that layer 5 might be employed in long-range communication
[100] and output selection [19]. Layer 4 in turn shows an abundance of PV interneurons [86] and
could implement a preprocessing of bottom-up inputs [17]. These different roles of deeper layers
are also in line with theories of cortical evolution, which hypothesize that deeper layers have
migrated from previously separate ‘input’ and ‘output’ neural populations to neocortex in order
to integrate cortical neurons more deeply with the rest of the brain and other cortical areas
[101–104] (Figure 3A,B). Hence, the different functions of deeper layers could complement the
computations of dendritic hPC in important ways, but how exactly such an interaction could
look has yet to be formulated.

Another aspect of cortical lamination that could support the computations of dendritic hPC are
neuromodulators. Neuromodulators act on a wide range of scales [105] and can target speciﬁc
cortical layers, where they might modulate computations in speciﬁc dendritic domains of pyrami-
dal cells [94,106–108]. For example, acetylcholine (ACh), which is associated with attention and
learning, has been found to promote (dis-)inhibition of apical or basal dendrites through distinct
mechanisms, possibly in a very targeted manner [96,99,107–109]. In the context of hPC, ACh
and other neuromodulators have been proposed to set the precisions of the internal model and
thereby determine the inﬂuence of sensory and top-down information [110–112]. The separation
of top-down and bottom-up inputs across cortical layers, as in dendritic hPC, could therefore be
a central factor to enable the targeted modulation of these pathways. This might not only apply to
the effects of ACh on neural gain, but also to the various other effects ACh and other neuromod-
ulators have on cortical dynamics and plasticity [105].

How can error responses arise in prediction neurons?
One of the central features of classical hPC is its ability to explain a variety of experimental
observations through the concept of error neurons. Error neurons have, for example, been
used to explain extra-classical receptive ﬁeld effects in visual cortex [11], as well as mismatch
responses in cortex, which are neural responses that appear to signal the mismatch between
an internal model and sensory data [10]. Thus, an important question for dendritic hPC is if and
how these experimental observations can arise in a model without error neurons.

The ﬁrst experimental observation that has been explained with error neurons in hPC is the extra-
classical receptive ﬁeld effect of endstopping [11]. In endstopping it is found that, ﬁrst, the
response of a neuron in V1 to a bar stimulus decreases when the bar extends over its receptive
ﬁeld, and second, this effect is reduced when feedback from higher-level areas is disabled
[113,114]. Recent theoretical work showed that endstopping behavior, as well as other extra-
classical receptive ﬁeld effects, also occur in prediction neurons, where top-down connections
strengthen these effects [7,115,116]. Here, endstopping is mainly mediated by lateral inhibition
between neurons with overlapping receptive ﬁelds [116]. Top-down connections from higher-
level areas predict the activity patterns that arise from these lateral interactions and enhance

Trends in Neurosciences
OPEN ACCESS

54
Trends in Neurosciences, January 2023, Vol. 46, No. 1


---

## Page 11

them, which strengthens endstopping behavior [115]. This cooperation of lateral and top-down
interactions could be important to help the network to cope with noise in the inputs and improve
visual processing [115,117] and has been widely observed in visual cortex [114,117–119].

Mismatch responses have been observed in different forms, such as responses to the omission
of expected stimuli [10], responses to a mismatch between information in different modalities
(e.g., visual and motor information) [120–122], strong responses to unexpected stimuli [7,123],
or suppressed responses to expected stimuli [1,124]. Omission responses can already occur
in straightforward prediction neuron responses, as prediction neurons can be active even without
the expected input [10]. Recent work from our group has also shown that multimodal mismatch
responses can naturally arise in prediction neurons, when different cortical areas jointly infer a
consistent explanation of sensory data [125]. This joint inference aims to ﬁnd single causes that
underlie stimuli in multiple modalities, meaning cortical areas should suppress predictable ac-
tivity in other areas (as in [122,126]), but might also drive activity in case of a prediction mis-
match (as in [120,121,127]). Strong/suppressed responses to unexpected/expected stimuli
in turn have so far not been explained with pure prediction responses, but it has been argued
that they might be mediated by other mechanisms, such as attention to interesting stimuli, the
variance in neural sampling, or adaptation mechanisms [7,124,128]. In conclusion, the ob-
served mismatch responses can be explained by a variety of plausible mechanisms in predic-
tion neurons, which, however, in some cases might not be directly relatable to the
computations of dendritic hPC.

Testable predictions
To better assess the potential as well as the limitations of dendritic hPC to describe inference in
cortex, we here propose experiments that: (i) test predictions for speciﬁc neural mechanisms,
and (ii) aim to distinguish between the different implementations of hPC with and without error
neurons.

Predictions for speciﬁc neural mechanisms
• Bottom-up excitation to basal dendrites of layer 2/3 pyramidal cells should be locally matched
and balanced with lateral inhibition, likely via PV interneurons (an indication that such a precise
matching is possible, e.g., in dendritic spines, has been found in [129]). This could be tested in
detail, for example, using large-scale connectomics datasets [130].
• Plasticity for excitatory bottom-up connections is predicted to be modulated by local inhibitory
input, which is expected to turn long-term potentiation into depression. While such modulation
of plasticity has been found (e.g., in hippocampal neurons in a spike-timing-dependent plas-
ticity experiment [56]), it would be interesting to test this more speciﬁcally in layer 2/3 basal
dendrites, with a particular focus on the predicted impact of the strength and timing of inhibi-
tion on plasticity [16].
• Similar experiments could be conducted for top-down connections to apical dendrites, where
plasticity should be Hebbian, but switch to depression when presynpaptic spikes depolarize
the dendrite while the neuron remains silent. Also, here it would be interesting to explicitly
test for the predicted dependence of plasticity on the dendritic membrane potential [15].
• As a consequence of these plasticity mechanisms, activity in basal dendrites is expected to
be decreased (‘explained away’) in the course of learning, whereas activity in apical den-
drites should increase and become predictive of somatic spiking (similar to what was
found in [31]). An important experiment would be to test explicitly if apical activity indeed be-
comes predictive on a single neuron level, which would also distinguish dendritic hPC from
theories of dendritic error backpropagation that predict a clear decrease of apical activity
(Figure 2).

Trends in Neurosciences

OPEN ACCESS

Trends in Neurosciences, January 2023, Vol. 46, No. 1
55


---

## Page 12

Distinguishing between hPC with and without error neurons
The central challenge in distinguishing between different implementations of hPC is that their
underlying mathematical framework is the same, hence they predict the same computations in
prediction neurons. Thus, since classical hPC as yet does not make clear predictions on the
single neuron level, the main distinguishing characteristic between classical and dendritic hPC
is the presence or absence of error units. For speciﬁc computations, this might be used to rule
out one of the models:

• As we discussed, mismatch responses are explained via distinct mechanisms in models with
or without error neurons, which could be tested on a case-by-case basis. For example, mis-
match responses in multimodal mismatch experiments are transient [131], where classical
hPC predicts this decrease to be caused by top-down inhibition, while in dendritic hPC one
would expect the origin in adaptation or other bottom-up mechanisms [125] (for other exper-
iments, see also discussion in [7,124]).
• Another, more direct approach would be to map out the functional circuits in cortex, where
classical hPC expects a clear separation between error and prediction units (i.e., error units
only receive predictions and vice versa), but dendritic hPC expects no such separation. For
example, in several experiments reporting ‘error’ and ‘prediction’ neurons, their populations
appear intermixed [123,132] and it would be important to clarify whether or not there exists
a clear feedforward–feedback circuit motif between these populations (e.g., if bottom-up
excitation and inhibition always arrives ﬁrst in one of the populations).

For these experiments it is important to note that dedicated error neurons (or even classical
hPC) might coexist with dendritic hPC for complementary computations. For example, it is
well known that dopaminergic neurons code for reward prediction errors to guide behavioral
learning [133]. However, it is unclear whether there exists an advantage to implement the
same computation, such as inference in sensory cortex, simultaneously with two different
implementations of hPC.

Concluding remarks
Since its conception over 20 years ago, hPC has been considered one of the most promising
unifying theories of cortical computation, but – in its classical form – it is still facing substantial
questions regarding its biological plausibility. Here, we outlined an emerging hPC scheme
based on dendritic error computation, which is functionally equivalent, but provides solutions
to the most pressing open problems of the established theory of classical hPC: ﬁrst, it can
explain the lack of clear empirical evidence for the coexistence of error and prediction neurons
[10,51], and second, it overcomes the unresolved question of how learning can be efﬁciently
implemented with spiking error neurons [13]. Moreover, we explained how dendritic hPC
could connect the microscopic properties of neural dendrites, such as the local E-I balance
[14,32,57] and VDP [72,75], to neural dynamics [14] and learning [15,16,115] in the cortical
hierarchy.

These advances open up several interesting paths for future research. Next to experimen-
tally testing for the predicted mechanisms of inference and learning in cortex (see section
‘Testable predictions’), there are a number of open theoretical challenges, especially con-
cerning the details of the biological implementation (see Outstanding questions). Going
forward, it will also be important to understand how the learning of a hierarchical model of
sensory data interacts with complementary mechanisms, such as attention and behavioral
learning, not only for dendritic hPC, but also for hPC and other theories of inference in
cortex more generally.

Trends in Neurosciences
OPEN ACCESS

> Figure description (generated): Since no figure image was provided, I cannot generate the detailed description.

**Please provide the academic PDF figure you would like me to describe.**

Once you provide the image, I will adhere strictly to your instructions and deliver a highly detailed, comprehensive, and exhaustive description following this structure:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration**

56
Trends in Neurosciences, January 2023, Vol. 46, No. 1

Outstanding questions

Dendritic hPC has been derived under
the assumption of linear dendrites
for a linear encoding of sensory data,
but dendrites often show nonlinear
behavior. How can the ideas of
dendritic hPC be transported to a
model with nonlinear dendrites and
could this allow for a nonlinear and
thus more versatile encoding?

Pyramidal cells show extensive lateral
excitatory connectivity, which could be
used to learn and predict temporal
sequences within a single level. Can
these mechanisms interact purposefully
with the learning of predictions in a
hierarchical model?

When cortical areas communicate
there might be substantial challenges,
such as long transmission delays or
sparse activity in both areas. Are
there additional mechanisms that
could improve neural communication
under these conditions, such as
communication through coherence,
and how could they be integrated
into dendritic hPC?

Pyramidal cells are not a uniform class
of cells, for example, the different
physiology of layer 2/3 and layer 5
apical dendrites leads to different
integration of top-down inputs, but
also layers 2 and 3 contain slightly dif-
ferent subtypes of pyramidal cells.
What are the functional reasons for
these properties and how are they re-
lated to dendritic hPC?

We have suggested that dendritic
hPC describes the computations of
layer 2/3 pyramidal neurons. Under
this assumption, what are the roles
of deeper cortical layers and how can
they be integrated into the framework?

Inference has not only been used to
model sensory processing, but also
computations in hippocampus, and
some of the core predictions of
dendritic hPC also seem to apply to
hippocampal pyramidal cells. Are
principles
of
dendritic
hPC
also
employed by different brain regions,
or different neuron types?

Often indirect measures of neural
activity (e.g., electroencephalography,
fMRI) have been used to search for ev-
idence of classical hPC. How would


---

## Page 13

Acknowledgments

We would like to thank Abdullah Makkeh, Beatriz Belbut, Caspar Schwiedrzik, David Ehrlich, Georg Keller, and members of
the Priesemann Lab, especially Andreas Schneider, Kjartan van Driel, and Matthias Loidolt, for helpful discussions and com-

ments on the manuscript. F.A.M. and L.R. were funded by the German Research Foundation (DFG), SFB 1286. V.P. and
M.W. received support from the German Research Foundation (DFG), SFB 1528, Cognition of Interaction. F.A.M., L.R.,

and V.P. acknowledge support by the Max Planck Society.

Declaration of interests

The authors declare no competing interests in relation to this work.