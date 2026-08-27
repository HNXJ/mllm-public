## Page 1

Article
https://doi.org/10.1038/s41467-025-61399-5
Self-supervised predictive learning accounts
for cortical layer-speciﬁcity

Kevin Kermani Nejad1,2, Paul Anastasiades
3, Loreen Hertäg
4,5 &
Rui Ponte Costa
1,2,5

The neocortex constructs an internal representation of the world, but the
underlying circuitry and computational principles remain unclear. Inspired by
self-supervised learning algorithms, we propose a computational theory in
which layer 2/3 (L2/3) integrates past sensory input, relayed via layer 4, with
top-down context to predict incoming sensory stimuli. Learning is self-
supervised by comparing L2/3 predictions with the latent representations of
actual sensory input arriving at L5. We demonstrate that our model accurately
predicts sensory information in context-dependent temporal tasks, and that
its predictions are robust to noisy and occluded sensory input. Additionally,
our model generates layer-speciﬁc sparsity, consistent with experimental
observations. Next, using a sensorimotor task, we show that the model’s L2/3
and L5 prediction errors mirror mismatch responses observed in awake,
behaving mice. Finally, through manipulations, we offer testable predictions to
unveil the computational roles of various cortical features. In summary, our
ﬁndings suggest that the multi-layered neocortex empowers the brain with
self-supervised predictive learning.

Internal models of the external world are believed to endow the brain
with the ability to predict incoming sensory information and select
appropriate action-outcome contingencies1. Internal models are
widely believed to be encoded in the neocortex2,3, whose hallmark
feature is its laminar organization, comprising six distinct layers.
Although much has been learned about the underlying cellular het-
erogeneity and connectivity of individual cortical layers, why the
neocortex relies on a multi-layered structure remains unclear4. Unra-
veling its function could shed light on the neocortical algorithms
responsible for building rich internal representations of the world.

Historically, it has been proposed that unsupervised learning in
sensory cortices underpins the development of intricate sensory
representations that are critical for driving behavior5–7. Self-supervised
learning is a form of unsupervised learning that leverages the inherent
structure or patterns within the data as the target for learning. A

common application of self-supervised learning is to predict the
incoming input given past information8–12. Importantly, self-supervised
learning algorithms learn representations that capture experimentally
observed latent representations while resulting in richer models of
input statistics12–16. However, learning in these models is often treated
as a black box; therefore, it remains to be determined whether the
brain is capable of employing such learning principles.

The traditional view of the neocortical microcircuit postulates a
sequential ﬂow of sensory information. In this canonical view, sensory
input is relayed via the thalamus to layer 4 (L4) of the neocortex17,18. L4
subsequently forwards this information to layer 2/3 (L2/3), which is
thought to integrate ascending sensory information with top-down
modulatory input from higher-order cortical areas19–21. L2/3 in turn
projects to layer 5 (L5), which transmits the information to other brain
areas (Fig. 1a). However, growing evidence suggests that this model

Received: 21 May 2024

Accepted: 19 June 2025

Published online: 04 July 2025

Check for updates

1Centre for Neural Circuits and Behaviour, Department of Physiology, Anatomy and Genetics, University of Oxford, Oxford, United Kingdom. 2Bristol Com-
putational Neuroscience Unit, Intelligent Systems Lab, Faculty of Engineering, University of Bristol, Bristol BS8 1TH, United Kingdom. 3Department of
Translational Health Sciences, University of Bristol, Whitson Street, Bristol BS1 3NY, United Kingdom. 4Technische Universität Berlin & Bernstein Center for
Computational Neuroscience Berlin, 10115 Berlin, Germany. 5These authors jointly supervised this work: Loreen Hertäg and Rui Ponte Costa.

e-mail: rui.costa@dpag.ox.ac.uk

Nature Communications| (2025)16:6178
1

1234567890():,;

1234567890():,;


---

## Page 2

does not capture the full diversity of connections in the neocortical
microcircuit18. A body of experimental works suggests that L5 pyramidal
cells receive direct thalamic input that can drive short-latency, sensory-
evoked responses independently of activity within the cortical network
(Fig. 1b)22–26. These observations imply two distinct sensory-driven
pathways within the neocortex, one targeting L4 and the other L5
(Fig. 1a). However, why the cortex requires multiple inputs and the
computations supported by such parallel pathways remain unknown.

Inspired by this refreshed view of the canonical microcircuit and
the
predictive
capabilities
of
self-supervised
machine
learning
algorithms9,27, we propose a model in which L2/3, informed by past
sensory input from L4 and top-down context from higher-order cor-
tical areas, predicts incoming sensory input. In this model, the delay
from L4 to L2/3 enables L2/3 to generate predictions based on pre-
vious sensory information (Fig. 1c). Direct thalamic input to L5 pro-
vides the new sensoryinformation, which serves as an implicit target to
compare with the predictions generated by L2/3-to-L5 connections.
When the model’s predictions are violated, this comparison triggers
errors in both L5 and L2/3, thus driving circuit plasticity in a self-
supervised manner. This perspective of neocortical circuitry suggests
that the L4-L2/3-L5 laminar structure with parallel thalamic innervation
enables the brain to learn rich temporal representations.

We ﬁrst show that our learning rule for L2/3-to-L5 connections
closely resembles the long-term synaptic plasticity experimentally
observed28. Next, we demonstrate that by using self-supervised learn-
ing, our model can learn and predict sequential Gabor-like inputs in a
context-dependent manner, highlighting its ability to capture struc-
tured patterns. By ablating individual components of the model and
evaluating their impact on performance, we reveal how the neocortical
circuit components collaboratively enable self-supervised learning.
Next, we demonstrate that self-supervised learning leads to predic-
tions that are robust to sensory noise and occlusions. Moreover, the
model captures the relative differences in sparsity across layers,
aligning qualitatively with experimental ﬁndings in sensory systems.
Additionally, we demonstrate in a visuomotor task that violations of
predictions result in layer-speciﬁc mismatch errors, consistent with
mismatch responses observed in awake, behaving animals. Finally, we
suggest a set of optogenetic experiments capable of testing the core
predictions of our self-supervised learning model. Collectively, our

ﬁndings support the notion that the L4 →L2/3 →L5 pathway is
instrumental in enabling the brain to engage in temporal self-
supervised learning, highlighting its potential signiﬁcance in neural
mechanisms of predictive learning.

Results
Neocortical layers can implement self-supervised predictive
learning
To understand how neocortical microcircuits process temporal
information and learn latent representations in a self-supervised
manner, we created a model that emulates the properties of cortical
circuits. Our model contains three subnetworks with nonlinear neu-
rons separated into layers (L2/3, L4, and L5) to reﬂect the laminar
architecture of the neocortex (Fig. 2a). Within this framework, L4
receives ascending sensory information, x, at timestep t through input
weights WThal.→L4. At the same time, L2/3 receives delayed thalamic
input via L4 through WL4→L2/3 synapses, as well as top-down contextual
input via the weights Wtop-down→L2/3. We hypothesize that this combi-
nation of inputs enables L2/3 to make predictions about upcoming
sensory information. In our model, we deﬁne the predictions as the
output of L2/3, that is, W L2=3!L5  zL2=3

t
. These predictions are com-
pared with the activity of L5 neurons zL5

t (“target”) that also receive the
actual sensory input at timestep t. This comparison results in a self-
supervised error when L2/3 predictions and L5 targets are not equal,
which is deﬁned as CL2=3!L5 = 1

2 ðW L2=3!L5  zL2=3
t
 zL5

t Þ

2. In our model,
this error is fed back via L5-to-L2/3 connections to adjust the predictive
model of the incoming inputs. However, using this self-supervised
error alone would lead to a degenerate solution, as the model could
learn to output a constant value regardless of the input (known as
representational collapse12,29). To prevent this, in our model, L5, but
not L2/3 or L4, is also trained to reconstruct its own input (“recon-
struction cost”, see Methods). This strategy offers a solution to the
representational collapse problem in cortical circuits.

During learning, we modify connections to minimize the cost
function and facilitate the encoding of sensory input. Unlike predictive
coding approaches30, we do not use separate representation and error
neurons. Instead, each neuron in our model generates activity during
the forward pass (L4-to-L2/3-to-L5), which is then used to compute its
respective error signals through gradient calculations (Fig. S1; see

Thal

L4

L2/3

Top-down

L5

Sensory

Canonical view

Updated view

L6

L5

L4

L2/3

Time
t - 1
t
t + 1

L2/3

L4

L5

Thal

top-down
top-down
top-down

Fig. 1 | Information ﬂow in neocortical circuits. a The canonical and updated view
of the neocortical microcircuit. Sensory input is initially processed by the thalamus,
which, in the classical view, exclusively targets layer 4 (L4). L4 subsequently relays
this information to layer 2/3 (L2/3). L2/3, in turn, combines L4 input with top-down
contextual input that is fed forward to layer 5 (L5). However, recent studies have
emphasized the need to update this view due to direct projections from sensory
thalamic nuclei to L5 pyramidal cells26 (green arrow). For the sake of clarity, we
omitted feedback connections from the schematic, which in our self-supervised
model are responsible for carrying error signals that drive learning (see main text
and Methods). b Onset latencies of postsynaptic potentials (PSP) by cortical depth.
An onset latency of 0 ms denotes the timing of sensory input (whisker deﬂection).

> Figure caption (from PDF text): Fig. 1 | Information ﬂow in neocortical circuits. a The canonical and updated view
of the neocortical microcircuit. Sensory input is initially processed by the thalamus,
which, in the classical view, exclusively targets layer 4 (L4). L4 subsequently relays
this information to layer 2/3 (L2/3). L2/3, in turn, combines L4 input with top-down
contextual input that is fed forward to layer 5 (L5). However, recent studies have
emphasized the need to update this view due to direct projections from sensory
thalamic nuclei to L5 pyramidal cells26 (green arrow). For the sake of clarity, we
omitted feedback connections from the schematic, which in our self-supervised
model are responsible for carrying error signals that drive learning (see main text
and Methods). b Onset latencies of postsynaptic potentials (PSP) by cortical depth.
An onset latency of 0 ms denotes the timing of sensory input (whisker deﬂection).
> Figure description (generated): ## Figure 1: Information Flow in Neocortical Circuits

This figure is divided into three distinct panels (a, b, and c), illustrating different aspects of information flow within neocortical circuits.

### Panel (a): Canonical and Updated View of the Neocortical Microcircuit
Panel (a) presents a schematic flow chart illustrating two models of information processing: the "Canonical view" and an "Updated view."

**Structure and Flow:**
The diagram uses rectangular boxes to represent cortical layers (nodes) and arrows to indicate the direction of information flow.

1.  **Sensory Input:** The process begins with a node labeled "Thal" (Thalamus), representing sensory input.
2.  **Canonical View (Dashed Lines):**
    *   An arrow originates from "Thal" and points to a box labeled "L4," indicating the classical pathway.
    *   An arrow then proceeds from "L4" to a box labeled "L2/3."
    *   A dashed arrow originates from "L2/3" and points to a box labeled "L5," representing the top-down contextual input.
3.  **Updated View (Solid Green Line):**
    *   The flow from "Thal" to "L4" is shown, but an additional pathway is highlighted in green.
    *   A solid green arrow originates directly from "Thal" and points to a box labeled "L5," representing the direct projection emphasized in recent studies.
    *   The flow continues from "L4" to "L2/3," and then the canonical path proceeds from "L2/3" to "L5."

**Labels and Annotations:**
*   The legend indicates:
    *   A solid black line represents the "Canonical view."
    *   A solid green line represents the "Updated view."

### Panel (b): Onset Latencies of Postsynaptic Potentials (PSP) by Cortical Depth
Panel (b) is a scatter plot illustrating the timing of PSP onset across different cortical layers.

**Axes:**
*   The **Y-axis** is labeled "Microdrive depth ($\mu$m)" and ranges from 2 to 1800 $\mu$m, with major tick marks at intervals of 200 $\mu$m (e.g., 2, 600, 1400, 1800).
*   The **X-axis** is labeled "PSP onset latency (ms)" and ranges from 2 to 18 ms.

**Data Representation:**
*   The plot displays numerous small circles (data points) scattered across the depth and latency ranges.
*   The data is segmented vertically by cortical layers, indicated by shaded background regions:
    *   A light blue shaded region covers the depth range corresponding to L2/3.
    *   An orange shaded region covers the depth range corresponding to L5.
    *   The layers L4 and L6 are implied by the surrounding data distribution but are not explicitly shaded in this manner.

**Annotations:**
*   A vertical line is present at $0 \text{ ms}$ on the X-axis, annotated with the text: "An onset latency of 0 ms denotes the timing of sensory input (whisker deflection)."

### Panel (c): Temporal Progression of Cortical Activity
Panel (c) is a schematic timeline illustrating the temporal progression of activity across different cortical layers over time.

**Structure:**
The panel is organized horizontally along a timeline axis labeled "Time." Three discrete time points are marked: $t-1$, $t$, and $t+1$.

**Components:**
*   The layers L2/3, L4, and L5 are represented by schematic icons (boxes containing internal structures) positioned above the timeline.
*   The Thalamus ("Thal") is shown below the layers, representing input timing.

**Temporal Progression:**
*   At each time point ($t-1, t, t+1$), the layers L2/3, L4, and L5 are shown with distinct visual states:
    *   **L2/3:** Shows a state at $t-1$, $t$, and $t+1$.
    *   **L4:** Shows a state at $t-1$, $t$, and $t+1$.
    *   **L5:** Shows a state at $t-1$, $t$, and $t+1$.
*   The icons within the layers appear to change state across time, suggesting dynamic processing.

**Annotations:**
*   Arrows labeled "$+18^\circ$" are positioned above the L2/3 and L4 icons at time $t$, indicating a specific angular shift or transformation associated with the processing at that moment.

These results demonstrate the simultaneous activation of L4 and L5 neurons by the
thalamus (blue bands), indicating a direct thalamic input to L5, and a delayed
activation of L2/3 neurons (orange band). c Illustration of information ﬂow of the
proposed self-supervised temporal learning in the neocortical microcircuit. L2/3,
informed by past sensory input from L4 and top-down contextual input, predicts
the current sensory input arriving in L5. The direct thalamic inputs to L5 provide
sensory input, which is used as a teaching signal to instruct the L2/3 predictive
model. Gabor-like gratings represent neuronal encoding of the sensory input, or its
prediction in the case of L2/3-to-L5 connections. Panel b adapted from Christine M
Constantinople and Randy M Bruno. Deep cortical layers are activated directly by the
thalamus. Science 340 (2013); reprinted with permission from AAAS.

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
2


---

## Page 3

Methods). Consequently, our model requires both feedforward con-
nections from L4 →L2/3, which relay sensory information, as well as
feedback connections from L5 back to L2/3, to transmit self-supervised
error signals. All weights are optimized via gradient descent. This
approach allows us to recapitulate learning rules observed in experi-
mental data. We compared the learning rule for the weights connect-
ing L2/3 and L5 in our model, WL2/3→L5 (Methods Eq. (7)), with observed
long-term synaptic plasticity in primary sensory cortices (Fig. 2b)28.
Our learning rule predicts a depression-to-potentiation switch as the
activity of L5 neurons increases. This is in line with experimental
observations showing a similar depression-to-potentiation switch of
WL2/3→L5 connections with increasing depolarization of L5 pyramidal
cells28. Hence, this experimental evidence corroborates our model’s
learning rule, showing that the model is consistent with known
synaptic plasticity mechanisms in primary sensory cortices.

To demonstrate our model’s ability to learn predictive repre-
sentations, we created a sequence of Gabor patches, commonly used
to evoke responses in the primary visual cortex (see Methods)31,32.
Starting with a random Gabor patch, the orientation of the patch
changes based on randomly generated top-down contextual input (see
Methods). This higher-order contextual cue to L2/3 is provided at each
time step and conveys contextual information, for instance, an ani-
mal’s own locomotion in a sensorimotor task, which may be provided
by the motor cortex33. Given this top-down input, the Gabor patch
either rotates anti-clockwise by −18°, remains the same, or rotates
clockwise by +18° (Fig. 2c). For example, if the current Gabor patch has
0° orientation, the orientation of the subsequent input can be −18°, 0°,

or +18° for contextual cue values of
−18°, 0°, and
+18°, respec-
tively (Fig. 2c).

To evaluate the representations learned by our model, we use a
linear decoder8,34,35. We trained this decoder on L2/3’s output to pre-
dict the orientation of the Gabor patches received by L5 at any given
timestep. L2/3 output effectively learns to predict upcoming Gabor
patches with near-perfect accuracy (93%) using the previous input,
provided by L4, and the top-down context value (Fig. 2d). Next, we
applied a linear classiﬁer to L5’s output. On average, L5 achieves a test
accuracy of 89% (classiﬁcation accuracy on a random model is 11%),
indicating that L5 successfully identiﬁes and encodes each Gabor
patch’s distinctfeatures (Fig. 2e).These results directly follow fromour
model, where L5 encodes the input while L2/3 predicts the incoming
input, which are in line with experimental ﬁndings showing that L2/3
can learn to predict image sequences in a passive task32. In addition, we
obtain similar results in a more complex task in which hand-written
digits are used as input (Fig. S2).

In summary, we have shown the model’s ability to perform self-
supervised learning in a temporal task and its consistency with synaptic
plasticity observations. However, we have yet to explore the precise
contribution of each circuit element to self-supervised learning.

Neocortical circuitry jointly underlies self-supervised learning
In our model, different cortical layers give rise to distinct computa-
tional roles. To demonstrate the contribution of different circuit
components, while generating experimentally testable predictions, we
systematically ablated individual connections, allowing us to quantify

a

c
d

b

e
top-down

context

time

Thal

*

Model
Data

Stim

L2/3
L5

boosted L2/3    L5 exp.

(context)

(sensory)

(delayed)

(prediction)

prediction error

L2/3-to-L5 pairs

Boosted L2/3-to-L5 pairs

Fig. 2 | A model of temporal self-supervised learning in cortical circuits.
a Schematic of model of self-supervised learning in cortical layers (black denotes
elements used for inference and red for learning). b Left: schematic of the
experimental setup in which an extracellular electrode was used to boost L5 activity
while inducing long-term synaptic plasticity on L2/3-to-L5 connections28. Middle:
observed changes in synaptic weights as a function of L5 depolarization (scatter
plot: individual data points, solid line: linear ﬁt to the data). Right: L2/3-to-L5
learning rule as predicted by our model as a function of L5 activity for multiple
randomly drawn samples of L2/3 and L5 activity (circles), and linear ﬁt to the data

> Figure caption (from PDF text): Fig. 2 | A model of temporal self-supervised learning in cortical circuits.
a Schematic of model of self-supervised learning in cortical layers (black denotes
elements used for inference and red for learning). b Left: schematic of the
experimental setup in which an extracellular electrode was used to boost L5 activity
while inducing long-term synaptic plasticity on L2/3-to-L5 connections28. Middle:
observed changes in synaptic weights as a function of L5 depolarization (scatter
plot: individual data points, solid line: linear ﬁt to the data). Right: L2/3-to-L5
learning rule as predicted by our model as a function of L5 activity for multiple
randomly drawn samples of L2/3 and L5 activity (circles), and linear ﬁt to the data
> Figure description (generated): This image displays three distinct panels, labeled 'a', 'b', and 'd' (though the provided crop only shows parts of these, we will describe what is visible), focusing on a model of temporal self-supervised learning.

### Panel Structure and Content Analysis

**Panel (a): Temporal Dynamics Schematic**
This panel illustrates a temporal progression of visual stimuli.
*   **Structure:** It is a flow diagram showing input at time $t-1$ leading to output/prediction at time $t$.
*   **Visual Components:** Three distinct visual patterns (likely representing orientations or textures) are shown.
    *   The top pattern is associated with a label "+$18^\circ$" and shows a striped texture.
    *   The middle pattern is associated with "$0^\circ$" and shows a horizontally oriented striped texture.
    *   The bottom pattern is associated with "$-18^\circ$" and shows a vertically oriented striped texture.
*   **Flow:** Arrows indicate the temporal flow: an input pattern at $t-1$ leads to a corresponding output/prediction pattern at time $t$. The arrows connect the input patterns (on the left) to the output patterns (on the right).

**Panel (d): Prediction vs. Input Plot**
This panel presents a scatter plot comparing predicted input values against actual input values, likely demonstrating the model's predictive accuracy across different angular conditions.
*   **Axes:**
    *   The x-axis is labeled "input ($\mathbf{x}_{t-1}$)" and features tick marks corresponding to different input states.
    *   The y-axis is labeled "predicted input ($\hat{\mathbf{x}}_t$)" and features corresponding tick marks.
*   **Data Representation:** There are three distinct sets of data points, each associated with a different angular condition:
    *   **Orange Circles:** Labeled "+$18^\circ$" in the legend.
    *   **Gray Circles:** Labeled "$0^\circ$" in the legend.
    *   **Blue Circles:** Labeled "$-18^\circ$" in the legend.
*   **Trend Lines:** Each data set is accompanied by a fitted line:
    *   The orange points are fitted with an upward-sloping line.
    *   The gray points are fitted with a steeper, upward-sloping line.
    *   The blue points are fitted with an upward-sloping line, appearing slightly less steep than the gray line.
*   **Annotation:** A black asterisk ($\text{*}$) is placed near the bottom left of the plot, indicating a specific data point or region.

**Panel (e): Prediction Accuracy Heatmap**
This panel is a heatmap visualizing the correlation or accuracy between predicted and actual inputs across various states.
*   **Structure:** It is a square matrix or heatmap where both the rows and columns represent input states.
*   **Axes:**
    *   The y-axis is labeled "predicted input ($\hat{\mathbf{x}}_t$)" and lists discrete states.
    *   The x-axis is labeled "input ($\mathbf{x}_t$)" and lists corresponding discrete states.
*   **Color Coding:** The heatmap uses a color gradient, indicated by the vertical bar on the right labeled "acc.(%)".
    *   Dark blue/black indicates high accuracy (approaching 100%).
    *   Light blue/white indicates low accuracy (approaching 0%).
*   **Data Pattern:** The matrix exhibits a strong diagonal pattern, where the cells along the main diagonal are dark blue, indicating high accuracy when the predicted state matches the actual input state. Off-diagonal elements show varying levels of correlation, with some darker patches visible away from the main diagonal.

points (solid line). c, Schematic of a sequential Gabor task. The generative factor
provided to the model as top-down context at timestep t determines the orienta-
tion of the next Gabor patch at timestep t + 1. d Decoding accuracy of a linear model
trained on the output of L2/3. For a given input, L2/3 predicts the incoming sensory
input with high accuracy. Colors represent the three possible conditions (−18°, 0°,
and +18°). ∗points to the example illustrated in (b). Error bars represent the
standard error of the mean over ﬁve different initial conditions. e Confusion matrix
for classiﬁcation accuracy of a linear model trained on the output of L5. The matrix
is calculated over ﬁve different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

> Figure description (generated): This figure is a schematic diagram illustrating a neural circuit model, titled "boosted L2/3 $\rightarrow$ L5 exp."

**1. Overall Layout & Structure:**
The diagram is presented as a single, contained schematic within dashed rectangular boundaries. It depicts two distinct layers of cortical circuitry stacked vertically: an upper layer labeled L2/3 and a lower layer labeled L5. The overall structure suggests a feedforward or recurrent connection between these two layers, with an external stimulus input shown targeting the lower layer.

**2. Visual Components & Symbols:**
*   **Layers/Boxes:** Two large, shaded gray rectangular regions represent the cortical layers. The upper region is labeled "L2/3," and the lower region is labeled "L5."
*   **Neurons (Nodes):** Within each shaded layer, there are stylized representations of neurons. These are depicted as triangular shapes with branching dendrites extending upwards and downwards, characteristic of pyramidal cells or similar cortical neurons.
*   **Connections (Synapses/Axons):** Lines connect the neurons across and within the layers, representing synaptic connections.
    *   In the L2/3 layer, neurons are shown connected to each other and potentially projecting downwards.
    *   In the L5 layer, neurons are shown connected to each other and receiving input.
    *   A prominent curved line connects a neuron in the L2/3 layer downwards to a neuron in the L5 layer, indicating a projection from L2/3 to L5.
*   **Inputs:**
    *   In the L2/3 layer, there are small lines entering from above or sides, suggesting external input or connections originating outside the depicted circuit.
    *   In the L5 layer, there is a specific input labeled "Stim" (Stimulus) shown targeting one of the neurons.
    *   Additionally, there are small lines entering from below or sides in both layers, representing other inputs.

**3. Labels, Keys & Legends:**
*   **Title/Header:** The figure is titled "boosted L2/3 $\rightarrow$ L5 exp."
*   **Layer Labels:** The upper shaded box is labeled "L2/3," and the lower shaded box is labeled "L5."
*   **Connection Labels:** A label positioned to the right of the circuit indicates a specific pathway: "$W^{\text{L2/3}\rightarrow\text{L5}}$," suggesting a weight or connection strength associated with the L2/3 to L5 projection.
*   **Input Label:** The stimulus input targeting the lower layer is explicitly labeled "Stim."

**4. Data Trends & Details:**
As this is a schematic diagram and not a plot, there are no axes or quantitative data trends to describe.

**5. Contextual Caption Integration:**
The schematic visually represents a model where activity originating in Layer 2/3 projects down to Layer 5, as indicated by the $W^{\text{L2/3}\rightarrow\text{L5}}$ notation. The term "boosted" in the title suggests that this specific L2/3 $\rightarrow$ L5 connection is being emphasized or enhanced in the experimental context described. The presence of "Stim" indicates that the L5 layer is being driven by an external stimulus while interacting with inputs from L2/3.

> Figure description (generated): This figure is a scatter plot with an overlaid linear regression line, likely illustrating the relationship between two continuous variables.

**1. Overall Layout & Structure:**
The figure consists of a single plot area, characterized by Cartesian axes (x-axis and y-axis). The data is presented as individual circular markers scattered across the plot, with a solid straight line fitted through the data points.

**2. Visual Components & Symbols:**
*   **Data Points:** The individual data points are represented by small, unfilled circles (open circles). These points are distributed across the plot area.
*   **Trend Line:** A solid, straight black line is drawn through the data points, representing a linear trend or regression fit.
*   **Reference Line:** A horizontal dashed line is present across the plot, positioned at $y=0.0$.

**3. Labels, Keys & Legends:**
*   **Y-Axis Labeling:** The vertical axis (y-axis) is labeled with numerical values, starting from a negative value and increasing upwards. Visible tick marks include $-0.2$, $0.0$, and $0.2$.
*   **X-Axis Labeling:** The horizontal axis (x-axis) is labeled with numerical values, starting from $0.0$ and increasing to at least $0.7$.
*   **Annotations:** There are no explicit titles or legends provided within the visible frame of the plot itself.

**4. Data Trends & Details:**
*   **Axes Variables:** The x-axis represents the independent variable, and the y-axis represents the dependent variable.
*   **Data Trend:** The data points generally exhibit a positive correlation with respect to the fitted line. As the values on the x-axis increase, the corresponding y-values tend to increase.
*   **Line Fit:** The solid black line shows a clear positive slope, indicating that the relationship between the two variables is positively linear.
*   **Data Distribution:** The data points are clustered around the regression line, suggesting a moderate to strong positive linear relationship.

**5. Contextual Caption Integration:**
No contextual caption was provided, so no specific biological or technical interpretations can be made regarding the variables represented by the axes.

Nature Communications| (2025)16:6178
3


---

## Page 4

their
impact
on
both
representational
capability
and
perfor-
mance (Fig. 3a).

When we knocked out the L2/3-to-L5 connection, L2/3 could no
longer learn to predict upcoming sensory information (Figs. 2c vs. 3b).
However, due to the continued presence of top-down contextual
input, L2/3 still displayed contextual segregation. Note that there are
also implicit feedback connections from L5-to-L2/3, which mediate
learning, and which we study in the next section.

Our model proposes a key function for the delay introduced by L4
as information propagates to L2/3. This delay creates a temporal dis-
crepancy between the information available to L2/3 (past input) and L5
(present input), which enables L2/3 to anticipate the incoming sensory
input. When this delay is removed, which would be equivalent to L2/3
receiving direct thalamic input, the entire network operates on
incoming sensory input, i.e., at timestep t. Consequently, the network
can no longer generate meaningful predictions of future inputs. This is
evident in our model, where removing the delay rendered L2/3 unable
to reliably distinguish between potential future outcomes (Fig. 3c).
This result highlights the key role that temporal delays may have in
shaping predictive learning within the neocortical microcircuit. The L4
to L2/3 delay is essential for biasing L2/3 representations toward the
future. Without it, both the Thal. →L4 →L2/3 →L5 and Thal. →L5
pathways end up representing the current sensory input, causing the
former pathway to be redundant.

Next, we investigate how ablations of these different circuit ele-
ments affect the ability to decode current sensory information from both
L2/3 and L5 representations. For current input decoding (Fig. 3d), L5
demonstrated robust accuracy as long as it retained access to thalamic
sensory input. This aligns with its role as the primary recipient of sensory
data, together with L423,26,36. L2/3 accuracy, however, was more depen-
dent on the overall circuit properties. While top-down input to L2/3
provided useful context-dependent input (Fig. S3), any disruption to the

core pathways within the microcircuit, except the delay knockout,
compromised L2/3’s ability to represent the current sensory input.

Decoding the previous input (Fig. 3e) further differentiated L2/3
and L5. As anticipated, L5 exhibited limited information about pre-
vious inputs due to its exclusive focus on current thalamic information.
L2/3, however, encodes information about the past as a result of the
delay introduced by L4. Complete loss of this past-input representa-
tion occurred only in two scenarios: when critical learning pathways
were ablated (Thal. →L5, L2/3 →L5), or when removing the delay
synchronized the inputs to L2/3 and L5.

Finally, we demonstrate the importance of the cost functions
used in our model, speciﬁcally the role of the L5 reconstruction cost
and the L2/3 self-supervised cost. Removing the L5 reconstruction
loss leads to representational collapse12,29, a state where L2/3 and L5
converge to similar outputs regardless of input (Fig. S5). While add-
ing a reconstruction loss effectively prevents representational col-
lapse, other mechanisms, such as variance maximization37, have also
been successful. Replacing the L2/3 self-supervised cost function
with a simpler regression task impairs L2/3’s predictive ability,
highlighting the importance of an appropriate self-supervised
objective (Fig. S5).

Our ablation and decoding analyses suggest that predictive
learning within the neocortical microcircuit depends on a complex
interplay between the layers. While the L2/3-to-L5 connection is
essential for the model to learn predictive representations, the tem-
poral delay between L4 and L2/3 is crucial for generating future-
oriented predictions, but not current representations. In terms of
decoding past and present sensory input, our results demonstrate that
L2/3 specializes in representing temporal context, while L5 primarily
encodes immediate sensory information. This result aligns with the
experimental observations showing that L2/3 effectively encodes
temporal information with high precision38.

a
b
c

d
e

delay
knockout

L2/3  L5
knockout

delay
knockout

Thal

L4

L2/3

Top-down

L5

delay

topdown
knockout

thal  L5
knockout

L2/3  L5
knockout

optimal

Fig. 3 | Neocortical circuitry jointly enables self-supervised learning.
a Schematic of the model with individual components knocked out (colored
crosses) within the neocortical microcircuit architecture. b Connections from L2/3
to L5 are necessary for L2/3 to learn a predictive representation of the input.
c Impact of L4-mediated delay in self-supervised learning (dashed lines represent
the optimal prediction). d Summary of decoding accuracy of the current input for

L2/3 and L5 when speciﬁc connections are knocked out. The x-axis indicates the
speciﬁc ablation, while the y-axis indicates the decoding accuracy for the current
input (xt). e Similar to (d), but for the past input (xt−1). Knockout components in
(d, e) are color-coded as in (a). Horizontal dashed lines in d, e represent chance
decoding accuracy. Error bars represent the standard error of the mean over ﬁve
different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

> Figure description (generated): This figure is composed of five panels (b, c, d, and e), presenting quantitative data related to neural decoding accuracy under different experimental conditions.

### Panel (b): Predicted Input vs. Actual Input (Top-down)
This panel is a scatter plot comparing predicted input against actual input for the "top-down" condition.
*   **Y-axis Label:** `predicted input ($\hat{x}_t$)` (ranging from approximately 0.0 to 1.0).
*   **X-axis Label:** `input ($x_{t-1}$)` (representing the input from the previous time step).
*   **Data Representation:** There are three distinct sets of data points, differentiated by color and shape:
    *   **Orange Circles ($\bullet$):** Labeled `+18°`. These points show a general positive correlation between predicted and actual input.
    *   **Gray Squares ($\blacksquare$):** Labeled `0°`. These points show a moderate positive correlation.
    *   **Blue Circles ($\bullet$):** Labeled `-18°`. These points show a weaker positive correlation compared to the other two groups.
*   **Structure:** The data points are plotted across a range of input values on the x-axis, showing how well the model predicts the previous state based on the current context.

### Panel (c): Predicted Input vs. Actual Input (Knockout)
This panel is also a scatter plot, comparing predicted input against actual input under the "knockout" condition.
*   **Y-axis Label:** `predicted input ($\hat{x}_t$)` (ranging from approximately 0.0 to 1.0).
*   **X-axis Label:** `input ($x_{t-1}$)` (representing the input from the previous time step).
*   **Data Representation:** The data points are plotted, and a dashed line labeled `optimal` is included, representing the ideal prediction scenario (where $\hat{x}_t = x_{t-1}$).
    *   The data points appear to be clustered, showing a general trend towards the optimal line, though perhaps with more scatter than in Panel (b).

### Panel (d): Decoding Accuracy (%)
This panel is a bar chart showing the decoding accuracy for different experimental manipulations.
*   **Y-axis Label:** `$\chi_t$ decoding acc. (%)` (ranging from 0 to 100).
*   **X-axis Labels:** The x-axis displays several conditions: `full`, `topdown k.o.`, `Thal. $\rightarrow$ L5 k.o.`, `L2/3 $\rightarrow$ L5 k.o.`, and `delay k.o.`.
*   **Data Representation:** For each condition, there are two bars:
    *   A **Black Bar** representing the accuracy for a specific condition (likely related to L2/3).
    *   A **White Bar** representing the accuracy for another condition (likely related to L5).
*   **Color Coding:** The bars are colored differently across the conditions, suggesting different experimental contexts or cell types being tested.

### Panel (e): Decoding Accuracy (%)
This panel is a bar chart, structurally identical to Panel (d), but measuring decoding accuracy for $\chi_{t-1}$.
*   **Y-axis Label:** `$\chi_{t-1}$ decoding acc. (%)` (ranging from 0 to 100).
*   **X-axis Labels:** The x-axis displays the same conditions as Panel (d): `full`, `topdown k.o.`, `Thal. $\rightarrow$ L5 k.o.`, `L2/3 $\rightarrow$ L5 k.o.`, and `delay k.o.`.
*   **Data Representation:** Similar to Panel (d), for each condition, there are two bars:
    *   A **Black Bar**.
    *   A **White Bar**.

### Contextual Annotations (From Caption)
The caption provides crucial context for interpreting the panels:
*   **L2/3 and L5:** These refer to specific cortical layers.
*   **Knockout (k.o.):** Indicates that components in the specified layers are ablated or removed.
*   **$\chi_t$ and $\chi_{t-1}$:** These variables refer to the decoding accuracy for the current input ($\chi_t$) and the previous input ($\chi_{t-1}$), respectively.
*   **Color Coding:** The caption notes that colors are coded as in (a) [though panel (a) is not visible here], and that the bars represent different conditions.

Nature Communications| (2025)16:6178
4


---

## Page 5

L5 →L2/3 feedback is required for self-supervised learning
A cardinal feature of self-supervised learning models is that they require
an error or teaching signal to guide plasticity across the network. This
error signal drives adjustments in synaptic weights, reﬁning the net-
work’s predictive capabilities. In our model, the learning-driving error
signal originates in L5. Hence, this error signal must be fed back to L2/3
to reﬁne the predictive model. This suggests the need for a feedback
connection that propagates this information from L5 to L2/3. Although
the vast majority of work on neocortical circuits has disregarded

feedback connections from L5 to L2/3 pyramidal cells17,18, growing evi-
dence shows that they are more abundant than previously assumed39,40.

Here, we explored the importance of the L5 to L2/3 feedback
connection for learning in our model. In particular, we contrast opti-
mal feedback, as used in previous ﬁgures, with random and no feed-
back. The optimal feedback condition corresponds to a setting in
which the feedback weights mirror the feedforward weights (i.e.,
W L5!L2=3 = W T

L2=3!L5), whereas in the random feedback condition, the
feedback weights are set to a random weight matrix41.

a

b

c

d

e

f

L5
L2/3

random L5     L2/3
no L5     L2/3

Fig. 4 | Role of L5-to-L2/3 feedback connections in self-supervised predictive
learning. a L2/3 learns to predict the input in the presence of random feedback
(left) but fails to do so without L5-to-L2/3 feedback (right). b L5 learns to represent
the inputs accurately with random feedback (left) but shows lower decoding
accuracy without feedback (right). c Two main principal components of L2/3
representations for random (left) and no feedback (right) across different top-
down contexts (symbols) and input Gabor orientations (colors). d Two main

> Figure caption (from PDF text): Fig. 4 | Role of L5-to-L2/3 feedback connections in self-supervised predictive
learning. a L2/3 learns to predict the input in the presence of random feedback
(left) but fails to do so without L5-to-L2/3 feedback (right). b L5 learns to represent
the inputs accurately with random feedback (left) but shows lower decoding
accuracy without feedback (right). c Two main principal components of L2/3
representations for random (left) and no feedback (right) across different top-
down contexts (symbols) and input Gabor orientations (colors). d Two main
> Figure description (generated): This figure appears to be a scatter plot, likely representing dimensionality reduction (like PCA) of neural representations. Based on the provided caption fragments, this specific panel likely corresponds to **Panel (c)**, which describes "Two main principal components of L2/3 representations for random (left) and no feedback (right) across different top-down contexts (symbols) and input Gabor orientations (colors)."

Here is a detailed description of the visual contents:

### 1. Overall Layout & Structure
The image displays a single, two-dimensional scatter plot. The data points are densely clustered within the central area of the plotting space, suggesting a projection onto two principal components.

### 2. Visual Components & Symbols
*   **Data Points:** Numerous individual data points are scattered across the plot. These points vary in both shape and color, indicating that they encode multiple variables as described in the caption.
*   **Color Coding:** Different colors are used to represent different **input Gabor orientations**. The distribution of these colors across the plot suggests how orientation relates to the principal components.
*   **Symbol Shapes:** Different geometric shapes (e.g., squares, circles, triangles) are used to represent different **top-down contexts**. The mixture of shapes indicates the presence of various contextual conditions.
*   **Axes:** The plot has a horizontal (x-axis) and a vertical (y-axis).

### 3. Labels, Keys & Legends
*   **Axis Labels:** The axes are labeled with numerical scales:
    *   The **Y-axis** ranges from approximately -75 to 75, with major tick marks at intervals of 25 (e.g., -75, -50, -25, 0, 25, 50, 75).
    *   The **X-axis** ranges from approximately -0.1 to 0.1, with major tick marks at intervals of 0.1 (e.g., -0.1, 0.0, 0.1).
*   **Annotations:** There are no explicit legends visible in this cropped image to map specific colors or shapes to their corresponding variables (Gabor orientations or top-down contexts), but the caption specifies these mappings.

### 4. Data Trends & Details
*   **Distribution:** The data points are not uniformly distributed but form a somewhat diffuse, cloud-like structure centered near the origin (0.0 on both axes).
*   **Clustering:** While generally spread, there appears to be a slight concentration or density variation across the plot.
*   **Bimodal/Multimodal Tendencies:** The distribution does not appear perfectly Gaussian; the mixture of colors and shapes suggests that different contexts/orientations might occupy slightly distinct regions within this 2D space.

### 5. Contextual Caption Integration
The caption identifies this plot as representing the **"Two main principal components of L2/3 representations."**
*   The caption specifies that the data shown likely compares two conditions: **"random (left)"** and **"no feedback (right)."** Although the plot itself does not explicitly delineate "left" vs. "right" conditions, the caption implies that the overall scatter plot represents a combination or comparison of these two states.
*   The use of **symbols** maps to different **top-down contexts**.
*   The use of **colors** maps to different **input Gabor orientations**.

> Figure caption (from PDF text): Fig. 4 | Role of L5-to-L2/3 feedback connections in self-supervised predictive
learning. a L2/3 learns to predict the input in the presence of random feedback
(left) but fails to do so without L5-to-L2/3 feedback (right). b L5 learns to represent
the inputs accurately with random feedback (left) but shows lower decoding
accuracy without feedback (right). c Two main principal components of L2/3
representations for random (left) and no feedback (right) across different top-
down contexts (symbols) and input Gabor orientations (colors). d Two main
> Figure description (generated): This image appears to be a scatter plot, likely representing dimensionality reduction (like PCA) of neural representations, as suggested by the caption fragment mentioning "Two main principal components."

Here is a detailed description:

### 1. Overall Layout & Structure
The figure consists of a single, large scatter plot occupying the majority of the frame. It is structured around two axes (X and Y) representing principal components, with numerous data points scattered across the plane.

### 2. Visual Components & Symbols
*   **Data Points:** The plot is densely populated with individual data points, which are differentiated by both **color** and **shape**.
*   **Color Coding:** There is a variety of colors present, including yellow/gold, gray, red/orange, blue, green, and purple.
*   **Shape Coding:** Various shapes are used for the data points, including squares ($\square$), circles ($\bullet$ or $\circ$), and triangles ($\triangle$).
*   **Spatial Distribution:** The points are clustered in several regions: a dense cluster around the origin (0, 0), a group extending towards negative X values and positive Y values, and another spread across the positive X region.

### 3. Labels, Keys & Legends
*   **Axes:** The axes are labeled with numerical values:
    *   The **Y-axis** ranges from approximately -0.1 to 0.1, with major tick marks labeled at intervals (e.g., -0.1, 0.0, 0.1).
    *   The **X-axis** ranges from approximately -0.1 to 0.1, with major tick marks labeled at intervals (e.g., -0.1, 0.0, 0.1).
*   **Annotations:** There are no explicit legends or keys visible within the plot area itself to define what specific color or shape corresponds to a variable (e.g., Gabor orientation or context).

### 4. Data Trends & Details
The plot displays the distribution of data points across two dimensions (Principal Components 1 and 2).
*   **Central Density:** The highest concentration of points is near the center (around X=0, Y=0).
*   **Clustering:** Distinct clusters are visible:
    *   A cluster of yellow/gold and gray points in the upper-left quadrant (negative X, positive Y).
    *   A cluster of red/orange and green points near the center-left.
    *   A large, diffuse cluster of blue points dominating the right side (positive X).

### 5. Contextual Caption Integration
The provided caption fragment states: "c Two main principal components of L2/3 representations for random (left) and no feedback (right) across different top-down contexts (symbols) and input Gabor orientations (colors)."

Based on this context:
*   The X and Y axes represent the **Two main principal components** derived from L2/3 representations.
*   The **colors** likely encode the **input Gabor orientations**.
*   The **symbols (shapes)** likely encode different **top-down contexts**.
*   The distinction between "random" and "no feedback" is likely represented by the overall grouping or separation of data points, although this specific binary division (left vs. right) is not explicitly mapped onto the visual elements in this single plot view, as the caption implies a comparison between two conditions.

> Figure caption (from PDF text): Fig. 4 | Role of L5-to-L2/3 feedback connections in self-supervised predictive
learning. a L2/3 learns to predict the input in the presence of random feedback
(left) but fails to do so without L5-to-L2/3 feedback (right). b L5 learns to represent
the inputs accurately with random feedback (left) but shows lower decoding
accuracy without feedback (right). c Two main principal components of L2/3
representations for random (left) and no feedback (right) across different top-
down contexts (symbols) and input Gabor orientations (colors). d Two main
> Figure description (generated): This image displays a single plot, likely representing one part of a larger figure (indicated by the caption referencing "Fig. 4").

**1. Overall Layout & Structure:**
The image consists of a single two-dimensional line graph plotted on Cartesian axes.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Data Representation:** Two distinct curves are plotted: one solid line and one dashed line.
*   **Error Bars:** Vertical error bars are visible above the data points associated with the dashed line, indicating variability or standard deviation.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0.2 to 1.0, marked in increments of 0.2 (e.g., 0.2, 0.4, 0.6, 0.8, 1.0).
*   **X-Axis Label:** The horizontal axis is labeled with numerical values ranging from 1 to 8, marked in increments of 1 (e.g., 1, 2, 3, 4, 5, 6, 7, 8).

**4. Data Trends & Details:**
*   **Solid Line Trend:** The solid line shows a monotonically increasing trend, starting near $y \approx 0.25$ at $x=1$ and rising smoothly to approach $y \approx 0.95$ at $x=8$.
*   **Dashed Line Trend:** The dashed line also shows a monotonically increasing trend, starting slightly lower than the solid line (around $y \approx 0.3$ at $x=1$). It rises more steeply initially than the solid line, reaching a higher value (approaching $y \approx 1.0$) by $x=8$.
*   **Comparison:** At lower x-values (e.g., $x=2$ to $x=4$), the dashed line is visibly higher than the solid line, especially when considering the error bars associated with the dashed line.

**5. Contextual Caption Integration:**
The provided caption mentions: "Fig. 4 | Role of L5-to-L2/3 feedback connections in self-supervised predictive learning. a L2/3 learns to predict the input in the presence of random feedback (left) but fails to do so without L5-to-L2/3 feedback (right). b L5 learns to represent the inputs accurately with random feedback (left) but shows lower decoding accuracy without feedback (right). c Two main principal components of L2/3 representations for random (left) and no feedback (right) across different top-down contexts (symbols) and input Gabor orientations (colors). d Two main..."

Based on the caption structure, this specific plot likely corresponds to one of the subpanels (a, b, or c). Given the description in panel 'a' ("L2/3 learns to predict the input in the presence of random feedback (left) but fails to do so without L5-to-L2/3 feedback (right)"), the two curves likely represent these two conditions:
*   One curve represents performance *with* random feedback (likely the higher performing line).
*   The other curve represents performance *without* L5-to-L2/3 feedback (likely the lower performing line).

The presence of error bars on the dashed line suggests that this specific curve might correspond to a condition where variability is being measured, possibly related to the "random feedback" or "no feedback" conditions described in the caption.

principal components of L5 representations for random (left) and no feedback
(right) across different top-down contexts (symbols) and input Gabor orientations
(colors). e L2/3 (top) and L5 (bottom) decoding accuracy for different degrees of
L5-to-L23 feedback. f Explained variance of L2/3 (top) and L5 (bottom) learnt
representations. Error bars represent the standard error of the mean over ﬁve
different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

> Figure description (generated): This figure is composed of four distinct panels, arranged in a 2x2 grid.

### Top-Left Panel: Line Plot (Prediction Accuracy vs. Input)
This panel is a line plot titled "top-down" (though the title appears truncated or incomplete in the image).
*   **Y-axis:** Labeled "predicted input ($\hat{x}_t$)" (ranging from approximately 0 to 1.0).
*   **X-axis:** Labeled "input ($x_{t-1}$)" (represented by a sequence of discrete, small rectangular markers).
*   **Data Series:** There are three distinct lines plotted:
    *   A red line, corresponding to "+18°".
    *   A gray line, corresponding to "0°".
    *   A blue line, corresponding to "-18°".
*   **Trend:** All three lines show a positive correlation, increasing as the input ($x_{t-1}$) increases. The red line (+18°) consistently shows the highest predicted values, followed by the gray line (0°), and then the blue line (-18°) shows the lowest predicted values. Error bars are present on the data points for each line, indicating variability.

### Top-Right Panel: Line Plot (Prediction Accuracy vs. Input)
This panel is a line plot, positioned next to the top-left panel. It appears related to prediction accuracy but uses different axes or contexts than the left panel.
*   **Y-axis:** Labeled "predicted input ($\hat{x}_t$)" (ranging from approximately 0 to 1.0).
*   **X-axis:** Labeled "input ($x_{t-1}$)" (represented by a sequence of discrete, small rectangular markers).
*   **Data Series:** Similar to the top-left panel, there are three data series distinguished by color:
    *   A red line/set of points, corresponding to "+18°".
    *   A gray line/set of points, corresponding to "0°".
    *   A blue line/set of points, corresponding to "-18°".
*   **Trend:** The lines show a general trend across the input sequence, with visible error bars indicating variability around the mean prediction for each condition.

### Bottom-Left Panel: Heatmap (Prediction Accuracy Matrix)
This panel is a heatmap displaying a matrix of prediction values.
*   **Y-axis:** Labeled "predicted input ($\hat{x}_t$)" (represented by discrete markers along the axis).
*   **X-axis:** Labeled "input ($x_t$)" (represented by discrete markers along the axis).
*   **Color Scale:** A color bar on the right indicates "L5 acc.(%)" (Layer 5 accuracy percentage), ranging from 0% to 100%.
*   **Data Visualization:** The matrix shows color intensity corresponding to the accuracy. Darker blue/white areas indicate higher accuracy, while lighter or less intense colors indicate lower accuracy. The pattern suggests a non-uniform relationship between the predicted input and the current input across different time steps or states.

### Bottom-Right Panel: Scatter Plot (Principal Component Analysis)
This panel displays a scatter plot, likely representing the results of Principal Component Analysis (PCA).
*   **Y-axis:** Labeled "principal component 2".
*   **X-axis:** Labeled with numerical values, centered around 0.0 (ranging roughly from -0.1 to 0.1).
*   **Data Points:** Numerous small, colored dots are scattered across the plot. The colors correspond to different conditions indicated in a legend located below this panel.
*   **Legend:** A small legend box shows color-coded swatches corresponding to different conditions, labeled with text such as "gabor" and various color combinations (e.g., red/black, blue/white).
*   **Trend:** The data points appear somewhat clustered around the origin (0, 0), though there is visible spread along both axes.

> Figure description (generated): This figure is a line graph illustrating connection probabilities under different experimental conditions.

**1. Overall Layout & Structure:**
The figure consists of a single plot panel. It is a standard 2D Cartesian coordinate system graph used to display the relationship between an independent variable (on the x-axis) and a dependent variable (on the y-axis).

**2. Visual Components & Symbols:**
The plot contains three distinct curves representing different scenarios:
*   **Solid Blue Line with Markers:** Represents the "optimal L5 $\to$ L2/3" condition.
*   **Dashed Black Line:** Represents the "random L5 $\to$ L2/3" condition.
*   **Dotted Black Line:** Represents the "no L5 $\to$ L2/3" condition.

All three curves are plotted against the axes, showing how the connection probability changes as the x-axis variable increases.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0.6 to 1.0, representing the "connection probability."
*   **X-Axis Label:** The horizontal axis is labeled with numerical values ranging from 0 to 30, although the specific label for this axis is truncated or absent in the provided view.
*   **Legend:** A legend box is present within the plot area, defining the three lines:
    *   $\text{■}$ (Blue square marker): "optimal L5 $\to$ L2/3"
    *   $\text{--}$ (Dashed line): "random L5 $\to$ L2/3"
    *   $\text{...}$ (Dotted line): "no L5 $\to$ L2/3"

**4. Data Trends & Details:**
*   **Y-Axis Range:** The connection probability ranges from approximately 0.6 to 1.0.
*   **X-Axis Range:** The independent variable ranges from 0 to 30.
*   **Trends:**
    *   All three curves exhibit a rapid increase in connection probability as the x-axis value increases from 0, quickly saturating towards a maximum probability near 1.0.
    *   The **"optimal L5 $\to$ L2/3"** curve (solid blue) shows the steepest initial rise and reaches a high probability quickly.
    *   The **"random L5 $\to$ L2/3"** curve (dashed black) rises slightly slower than the optimal condition initially but converges closely with it.
    *   The **"no L5 $\to$ L2/3"** curve (dotted black) shows the slowest initial increase and remains at a lower probability level compared to the other two conditions for most of the plotted range.

**5. Contextual Caption Integration:**
The legend explicitly defines the structural elements being compared: "L5 $\to$ L2/3" refers to connections originating from Layer 5 (L5) projecting to Layers 2 and 3 (L2/3). The comparison tests the effect of having an *optimal* vs. *random* versus *no* such projection pathway on the measured connection probability.

> Figure description (generated): ## Figure Description: L2/3 Transition Performance Plot

This figure is a single-panel line graph illustrating the performance of two different transition strategies when moving from Layer 5 (L5) to Layers 2/3 (L2/3).

**1. Overall Layout & Structure:**
The figure consists of a single 2D line plot, titled "L2/3," which plots performance metrics against an unspecified normalized variable on the x-axis.

**2. Visual Components & Symbols:**
*   **Axes:** The plot features a vertical (Y) axis and a horizontal (X) axis.
*   **Curves:** Two distinct lines are plotted:
    *   A solid gray line representing the "random L5 $\rightarrow$ L2/3" transition.
    *   A dashed blue line representing the "optimal L5 $\rightarrow$ L2/3" transition.
*   **Data Points:** The lines show a rapid initial increase followed by saturation near the top of the Y-axis.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "L2/3" centered at the top.
*   **Y-Axis:** The vertical axis is labeled with numerical ticks ranging from 0 to 100, marked every 50 units (0, 50, 100). The axis lacks an explicit label in the visible area.
*   **X-Axis:** The horizontal axis is labeled with numerical ticks ranging from 0.0 to 1.0, marked at intervals of 0.5 (0.0, 0.5, 1.0). The axis lacks an explicit label in the visible area.
*   **Legend:** A legend is provided in the lower-left quadrant of the plot area:
    *   A gray line swatch corresponds to "random L5 $\rightarrow$ L2/3".
    *   A dashed blue line swatch corresponds to "optimal L5 $\rightarrow$ L2/3".

**4. Data Trends & Details:**
*   **Random Transition (Gray Line):** This curve starts near zero on the Y-axis at $X=0.0$. It rises very steeply, reaching a high plateau (near 100) by an X-value slightly greater than 0.0, and remains flat at this high level for the remainder of the X-axis range (up to $X=1.0$).
*   **Optimal Transition (Blue Dashed Line):** This curve also starts near zero at $X=0.0$. It rises rapidly, closely tracking the random curve initially, and appears to reach or approach the maximum value (100) slightly faster than the random curve, maintaining a high plateau across the entire X-axis range.

**5. Contextual Caption Integration:**
The labels "L2/3," "random L5 $\rightarrow$ L2/3," and "optimal L5 $\rightarrow$ L2/3" indicate that the figure compares the performance (measured on the Y-axis, likely a metric like accuracy or correlation) of two methods—a random mapping versus an optimized mapping—when transitioning information flow from Layer 5 (L5) to Layers 2/3 (L2/3).

> Figure description (generated): ## Figure Description

This figure is a single-panel line graph titled "L5," likely representing data related to Layer 5 (L5) in a neural context.

**1. Overall Layout & Structure:**
The figure consists of one primary plot area, a standard Cartesian coordinate system graph.

**2. Visual Components & Symbols:**
*   **Axes:** The plot utilizes a horizontal (x-axis) and vertical (y-axis).
*   **Data Lines:** There are two distinct lines plotted:
    *   A solid, gray line representing the measured data trend.
    *   A dashed, light blue horizontal line positioned near the top of the graph, likely representing a baseline or target value.
*   **Data Trend:** The gray line starts at a relatively low point on the left side (near $x=0.0$), rises sharply to reach a plateau, and then remains relatively flat across the rest of the x-axis range.

**3. Labels, Keys & Legends:**
*   **Title:** The title centered above the plot is "L5".
*   **Y-Axis Labeling:** The vertical axis (y-axis) is scaled with numerical markers: 0, 50, and 100. The axis itself lacks an explicit label in the visible area of the image provided, but the values suggest a quantitative measure.
*   **X-Axis Labeling:** The horizontal axis (x-axis) is scaled with numerical markers: 0.0, 0.5, and 1.0. The axis itself lacks an explicit label in the visible area of the image provided, but these values suggest a normalized or time-based variable.

**4. Data Trends & Details:**
*   **Y-Axis Range:** The visible range spans from 0 to 100.
*   **X-Axis Range:** The visible range spans from 0.0 to 1.0.
*   **Trend Analysis:**
    *   At $x=0.0$, the gray line starts at a value slightly above 50 (approximately 52-53).
    *   The line rapidly increases between $x=0.0$ and approximately $x=0.1$, reaching a peak value close to the dashed line (around 80-82).
    *   From approximately $x=0.1$ onward, the gray line plateaus, showing minimal change across the remainder of the x-axis (from $x=0.1$ to $x=1.0$), maintaining a value slightly below the dashed line.
    *   The dashed blue line remains constant across the entire x-axis range, positioned at a value slightly above 80 (approximately 83).

**5. Contextual Caption Integration:**
No external caption text was provided, so no specific contextual interpretation regarding cell types or layers can be made beyond the title "L5."

Nature Communications| (2025)16:6178
5


---

## Page 6

Inspired by work showing that random feedback weights are
sufﬁcient for credit assignment41, we tested whether this form of
unstructured feedback was sufﬁcient for L2/3 to learn. We observed
that L2/3 output was indeed able to learn to predict the input with
random feedback weights (Figs. 4a and 2c). These results suggest that
unstructured feedback may be sufﬁcient in enabling L2/3 output to
develop useful predictive representations. Furthermore, our ﬁndings
demonstrate a signiﬁcant drop in the decoding accuracy of L5 when
feedback connections from L5-to-L2/3 were removed (Fig. 4b). This
decline is due to L2/3’s inability to learn, causing L5 to adopt erroneous
representations inﬂuenced by L2/3’s unlearned state. These results
demonstrate the need for L5 →L2/3 feedback.

To study the neuronal representations learned by the different
layers, we analyzed the two main principal components of L2/3. This
revealed a notable difference in the structural organization across
feedback conditions (that is, random and no feedback). With feedback,
L2/3 representations were differentiated based on the identity of the
Gabor patch as well as the top-down context (Fig. 4c, left). Without
feedback, the L2/3 representations were only distinguished based on
top-down inputs, indicating a limitation in the network’s learning
capability (Fig. 4c, right).

Similarly, analysis of L5 revealed that with random feedback,
representations are organized according to Gabor patch features,
suggesting a structured learning process (Fig. 4d, left; similar to the
optimal feedback condition, Fig. S6). These observations are in line
with the increased sparsity we observed in L2/3 compared to L5 (see
below). In contrast, when feedback was absent, L5 representations
were less organized (Fig. 4d, right).

Classically, feedback connections within the neocortex occur at
lower probabilities than the corresponding feedforward pathway39,40.
To test how connection density inﬂuences the properties of the net-
work, we next explored how the linear decoding accuracy of both L5
and L2/3 varies with the probability of feedback connections from L5
to L2/3. An increase in connection probability corresponded to
enhanced decoding accuracy (Fig. 4e). Therefore, while a very low
feedback connection probability was sufﬁcient for learning the task

considered here, for more complex tasks, higher connection prob-
abilities may be required for optimal performance (Fig. S7).

Finally, to determine how distributed information was, we exam-
ined how the explained variance, as assessed by the number of prin-
cipal components (PCs), changed with varying feedback probabilities.
The absence of feedback required a greater number of PCs to explain
the data effectively, while random feedback closely mirrored the efﬁ-
ciency of optimal feedback connections (Fig. 4f). This increase in the
number of PCs to capture the same variance is consistent with our
ﬁndings, showing the importance of feedback in organizing sensory
information in superﬁcial layers (Fig. 4c, d).

This analysis highlights the crucial role of feedback connections in
neural networks, particularly in improving predictive capabilities and
structuring neural representations. The nuanced differences observed
across various types and intensities of feedback offer insight into the
role of L5-to-L2/3 feedback connections39,40 for learning and informa-
tion processing in cortical networks.

Self-supervised learning leads to robustness to noise and
occlusion in cortical networks
As a consequence of learning a robust predictive model of the sensory
input, the cortical network should disregard unpredictable aspects like
noise. Therefore, we hypothesized that the self-supervised L2/3 →L5
component would help L5 ﬁlter out sensory noise. To test this, we
ablated the L2/3 →L5 projection in our model and used input with
varying noise levels. The simulated ablation shows that removing the
self-supervised component dramatically reduces robustness to dif-
ferent noise levels (Fig. 5a; similar results are obtained when ablating
the L4-to-L2/3 delay, Fig. S4). This denoising capability naturally
emerges from the model’s design, despite not being explicitly
designed for this purpose, making it comparable to a near-optimal
denoising autoencoder network.

To further investigate the model’s robustness to input perturba-
tions, we tested its ability to reconstruct input patterns during partial
input occlusions. After training the model without occlusions, we
evaluated the robustness of the learned representations in each layer

input

L2/3

L5

exp. #1
exp. #2
exp. #3
exp. #1
exp. #2
exp. #3

fixed
moving
a
b
c

Fig. 5 | L2/3-to-L5 predictions are crucial for denoising and resolving occluded
stimuli. a L2/3-to-L5 connections promote noise suppression in L5 representations.
Top: Schematic of noise added to the original inputs. Bottom: Noise-corrupted
input samples lead to higher L5 reconstruction residuals (^xt  xt) when the L2/
3 →L5 pathway is ablated (purple) compared to the full model (solid black). We also
provide the reconstruction residual for an autoencoder that was explicitly trained
to denoise the input (dashed black line). b Top: Decoding accuracy with and
without L2/3 →L5 for a Gabor task with occlusion. Bottom: Three examples
depicting L2/3's ability to recover occluded information, compared to L5's

> Figure caption (from PDF text): Fig. 5 | L2/3-to-L5 predictions are crucial for denoising and resolving occluded
stimuli. a L2/3-to-L5 connections promote noise suppression in L5 representations.
Top: Schematic of noise added to the original inputs. Bottom: Noise-corrupted
input samples lead to higher L5 reconstruction residuals (^xt  xt) when the L2/
3 →L5 pathway is ablated (purple) compared to the full model (solid black). We also
provide the reconstruction residual for an autoencoder that was explicitly trained
to denoise the input (dashed black line). b Top: Decoding accuracy with and
without L2/3 →L5 for a Gabor task with occlusion. Bottom: Three examples
depicting L2/3's ability to recover occluded information, compared to L5's
> Figure description (generated): ## Figure 5 Description

This figure is divided into three main panels: **a**, **b**, and **c**.

### Panel a: Reconstruction Residual Plot
Panel **a** presents a schematic illustrating the effect of ablating the L2/3 $\rightarrow$ L5 pathway on reconstruction residuals.

**Structure:**
*   The top section is a schematic flow diagram showing the input and noise addition.
    *   An image labeled "$x_{\text{original}}$" is shown on the left.
    *   An image labeled "noise" is shown next to it, with an addition sign ($+$) connecting them.
    *   The result of this addition leads to "$x_{\text{noisy}}$".
    *   An arrow points from $x_{\text{noisy}}$ to a representation of the reconstructed output, labeled "$x_{\text{reconstructed}}$".
*   The bottom section is a line graph plotting "reconstruction residual" against "noise."

**Data Details (Line Graph):**
*   **Y-axis:** Labeled "reconstruction residual," ranging from 0.0 to 7.5.
*   **X-axis:** Labeled "noise," ranging from 0.0 to 1.0.
*   **Lines:** Three distinct lines are plotted:
    1.  A solid black line labeled "full." This line shows a steady, increasing trend as noise increases.
    2.  A magenta/purple dashed line labeled "L2/3 $\rightarrow$ L5 k.o." This line shows a steeper increase than the "full" model, indicating higher residuals when the pathway is ablated.
    3.  A dashed black line labeled "denoising AE." This line remains very close to zero across the range of noise, representing an autoencoder trained for denoising.

### Panel b: Decoding Accuracy (Fixed)
Panel **b** presents a bar chart comparing decoding accuracy under fixed conditions, specifically related to the L2/3 $\rightarrow$ L5 pathway.

**Structure:**
*   The panel is divided into two main sections: a bar chart at the top and three example image sets below.
*   **Top Bar Chart:** Compares decoding accuracy for L2/3 and L5.
    *   **Y-axis:** Labeled "$\text{x}_t$ decoding acc. (%)", ranging from 0 to 100.
    *   **X-axis:** Shows categories "L2/3" and "L5."
    *   **Bars:** Two sets of bars are present for each category, distinguished by color:
        *   A magenta/purple bar (representing "L2/3 $\rightarrow$ L5 k.o.").
        *   A solid black bar (representing "full").
    *   **Annotations:** Above the bars, there are labels indicating experimental runs: "exp. #1," "exp. #2," and "exp. #3."

*   **Bottom Image Examples:** Three rows of image pairs illustrate the concept:
    *   The top row shows input images corresponding to "exp. #1," "exp. #2," and "exp. #3."
    *   The middle row shows corresponding representations for L2/3, and the bottom row shows representations for L5. Each image set appears to show a comparison between an input and its representation/reconstruction across the three experiments.

### Panel c: Decoding Accuracy (Moving)
Panel **c** presents a bar chart comparing decoding accuracy under moving conditions, mirroring the structure of Panel b.

**Structure:**
*   The panel is a bar chart comparing decoding accuracy for L2/3 and L5 under "moving" conditions.
*   **Y-axis:** Labeled "$\text{x}_t$ decoding acc. (%)", ranging from 0 to 100.
*   **X-axis:** Shows categories "L2/3" and "L5."
*   **Bars:** Similar to Panel b, two sets of bars are present for each category:
    *   A magenta/purple bar (representing "L2/3 $\rightarrow$ L5 k.o.").
    *   A solid black bar (representing "full").
*   **Annotations:** Above the bars, there are labels indicating experimental runs: "exp. #1," "exp. #2," and "exp. #3."

**Overall Contextual Notes from Caption:**
The caption clarifies that the L2/3 $\rightarrow$ L5 connections are crucial for denoising and resolving occluded stimuli. Panel **a** specifically shows that ablating the L2/3 $\rightarrow$ L5 pathway (purple line) leads to higher reconstruction residuals compared to the full model (solid black line). Panel **b** and **c** illustrate L2/3's ability to recover occluded information compared to L5.

incomplete reconstructions (top row: original occluded input; middle row: L2/3
prediction; bottom row: L5 reconstruction). c Top: Accuracy with and without L2/
3 →L5 connections for a task in which Gabor patches move randomly. Bottom:
Examples illustrating the robustness with moving Gabor patches (top row: original
input with motion (cf. panel b); middle row: L2/3 prediction; bottom row: L5
reconstruction). L2/3 reconstruction encodes uncertainty about the future possible
input location. Error bars represent the standard error of the mean over ﬁve dif-
ferent initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
6


---

## Page 7

by testing their ability to classify sensory input with randomly occlu-
ded segments (Fig. 5b). We observed that L2/3 achieves higher
decoding accuracy compared to L5, and that L5 decoding remained
unaffected by L2/3 →L5 knockout (Fig. 5b, top). Further analysis shows
that L2/3 can fully reconstruct the input while L5 is only able to
reconstruct the observable parts of the input (Fig. 5b, bottom). These
results support the idea that a strong predictive model leads to
representations that are robust to several perturbations.

Finally, we explored whether L2/3 can also encode the uncertainty
about the possible input locations. To test this, we introduced random
shifts in the position of the Gabor patch on the blank canvas during the
task. Decoding performance remained similar to the ﬁxed-position
task(Fig. 5c, top), but reconstructions were different. L2/3 repre-
sentations reﬂect the input’s positional uncertainty (blurred recon-
structions across possible locations), while L5 again encodes only the
visible parts (Fig. 5c, bottom). This suggests that self-supervised
learning also leads to useful L2/3 representations in the presence of
sensory uncertainty.

Collectively, these results underscore the robustness exhibited by
the proposed neocortical predictive learning model across diverse
input conditions. Consequently, our model offers valuable insights
into the mechanisms through which cortical circuits deal with the
considerable variability inherent in naturalistic environments.

Layer-speciﬁc sparseness emerges from self-supervised learning
Sparse coding, in which only a small subset of neurons are strongly
active for a given stimulus, is a widespread phenomenon across the
neocortex42–46. This sparsity is particularly pronounced in superﬁcial
layers (L2/3) compared to deeper layers (e.g., L5)47. However, it is
unclear why the degree of sparsity varies across cortical layers and how
it relates to their computational role.

We wondered whether our network, equipped for temporal self-
supervised
learning,
could
reproduce
experimentally
observed

sparsity distributions. Moreover, we wanted to investigate how dif-
ferent network features may control sparsity across different neocor-
tical layers. To this end, we trained our model on the sequential Gabor
task. After training, we measured population sparseness across layers
using established metrics48 (see Methods). Interestingly, our results
capture qualitative differences in the level of sparsity, showing a trend
that is similar to experimental ﬁndings47: L2/3 presents the highest
sparseness, followed by L4 and then L5 (Fig. 6a). This alignment sug-
gests that self-supervised learning, focused on input prediction, could
be a key factor driving sparsity in biological neural networks.

Layer 2/3 has undergone rapid expansion relative to other layers
within the human evolutionary lineage49,50. Could this expansion sup-
port greater predictive learning capabilities? We found that L2/3
sparseness increased with network size, while sparsity in L4 and L5
remained relatively stable (Fig. 6b). Consistent with the increased
sparsity in L2/3, we ﬁnd that an increase in the number of L2/3 neurons
also results in improved L2/3 decoding accuracy of upcoming sensory
inputs (Fig. 6c, d), in line with previous work51. In contrast, the rela-
tionship between the number of neurons, sparsity, and decoding
accuracy was not present in L5 neurons (Figs. 6c, d and S9). These
qualitative results do not depend on the type of optimizer and learning
rate used (Fig. S10).

To determine whether sparsity is due to the encoding of sensory
input or is simply an underlying feature of the circuitry, we trained the
network with Gaussian noise instead of Gabor-like inputs. When sen-
sory input was replaced with background noise, L2/3 retained high
sparsity, whereas L4 and L5 responses showed a strong decrease in
response sparsity (Fig. 6e). These results suggest that L2/3 sparsity is a
consequence of learning to predict sensory input (Fig. S9d). One
possible explanation is that L2/3 is forced to extract and rely only on
the most salient temporal features from the previous input in order to
forecast the current latent state, whereas L5 is free to capture the full
complexity, and a more distributed representation of the input. In

a
b

d
e
f

c
Data
Model

Fig. 6 | Population sparseness depends on the neocortical layer. a Population
sparseness across layers in the model (left; full histogram in S8) and experimental
data47 (right). b Population sparseness as a function of the number of neurons. The
qualitative relationship between layers is preserved, but L2/3 sparseness increases
with network size. c Decoding accuracy of current input as a function of the
population sparsity of L2/3 and L5 (L2/3: r = 0.78, p = 2.1e-11; L5: r = −0.35, p = 0.01).
d L2/3 decoding accuracy of the current input as a function of the number of
neurons in L2/3 and L5. e Population sparseness with or without sensory input

(noise condition) after learning. L2/3 remains sparse, while L4 and L5 show a strong
reduction in response sparsity. f Population sparseness following the ablation of
various model components during learning. Top-down input ablation slightly
increases L2/3 sparseness. Thalamic input ablation to L5 decreases L2/3 sparseness
while increasing L5 sparseness. Ablation of L2/3-to-L5 connections abolishes spar-
seness across all layers. Bars are color-coded following Fig. 3a, d, e. Statistical tests
are two-sided, and no adjustments were made for multiple comparisons. Error bars
represent the standard error of the mean over ﬁve different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

> Figure description (generated): This figure is composed of six distinct panels: (a), (b), (c), (d), (e), and (f). The panels primarily consist of bar charts, scatter plots, and line graphs illustrating data related to neuronal sparsity across different layers.

### Panel (a): Model Sparsness
This panel displays a bar chart comparing "pop. sparseness" across three layers: L2/3, L4, and L5.
*   **Y-axis:** "pop. sparseness" (ranging from 0.0 to 1.0).
*   **X-axis:** Layer labels (L2/3, L4, L5).
*   **Data:** Three vertical bars are present. The bar for L2/3 is the tallest, reaching approximately 0.9. The bar for L4 is significantly shorter, around 0.5. The bar for L5 is the shortest, near 0.2.

### Panel (b): Data Sparsness
This panel is a bar chart comparing "pop. sparseness" for the same layers as Panel (a), but representing experimental data.
*   **Y-axis:** "pop. sparseness" (ranging from 0.0 to 1.0).
*   **X-axis:** Layer labels (L2/3, L4, L5).
*   **Data:** Three vertical bars are present. The bar for L2/3 is the tallest, reaching approximately 0.85. The bar for L4 is slightly lower than in Panel (a), around 0.75. The bar for L5 is the shortest, near 0.3.

### Panel (c): L2/3 Dec. vs. Pop. Sparsity
This panel is a scatter plot showing the relationship between two variables.
*   **Y-axis:** "L2/3 dec. (%)" (ranging from 0.0 to 100).
*   **X-axis:** "pop. sparsity" (ranging from 0.0 to 1.0).
*   **Data:** Multiple scattered data points are visible, generally trending upwards from the bottom-left to the top-right. Two regression lines are overlaid:
    *   A dashed line labeled "L2/3" showing a positive correlation.
    *   A solid line labeled "L5" also showing a positive trend, though perhaps less steep than the L2/3 line.
*   **Annotations:** Two correlation coefficients are noted in the top right corner: $R = 0.352$ and $p < 0.01$.

### Panel (d): Pop. Sparseness vs. Number of Neurons
This panel is a line graph illustrating how population sparsity changes with the number of neurons.
*   **Y-axis:** "pop. sparseness" (ranging from 0.0 to 1.0).
*   **X-axis:** "number of neurons" (labeled with values 16, 32, 64, 128).
*   **Data:** Three distinct lines are plotted: L2/3, L4, and L5.
    *   The **L2/3** line starts high (around 0.7) and remains relatively flat or slightly decreasing across the neuron counts.
    *   The **L4** line starts around 0.3 and shows a slight increase or remains relatively stable.
    *   The **L5** line starts low (around 0.2) and remains relatively flat or slightly increasing.

### Panel (e): Pop. Sparsity vs. Number of Neurons (Detailed View)
This panel is a grouped bar chart showing population sparsity across different neuron counts, separated by whether the data includes "with input" or "noise."
*   **Y-axis:** "pop. sparseness" (ranging from 0.0 to 1.0).
*   **X-axis:** "number of L5 neurons" (labeled with values 4, 8, 16, 32, 64).
*   **Grouping:** For each neuron count on the X-axis, there are two bars: one representing "with input" (darker/filled) and one representing "noise" (lighter/outlined).
*   **Structure:** The chart is organized vertically, with the X-axis representing L5 neuron count and a secondary axis structure implied by the grouping. The overall structure suggests comparing sparsity under different conditions across increasing neuron counts.

### Panel (f): Pop. Sparseness vs. Experimental Conditions
This panel is a bar chart comparing population sparsity under various experimental manipulations, categorized by layer.
*   **Y-axis:** "pop. sparseness" (ranging from 0.0 to 1.0).
*   **X-axis:** Labels indicating experimental conditions: "full," "topdown k.o.," "Thal. $\rightarrow$ L5 k.o.," and "delay k.o."
*   **Grouping/Legend:** The bars are grouped by layer, indicated in the legend: L2/3 (black), L4 (dark gray), and L5 (light gray).
*   **Data Trends:**
    *   For the "full" condition, L2/3 sparsity is highest (around 0.85), followed by L4 and L5.
    *   In the "topdown k.o." condition, all layers show reduced sparsity compared to "full."
    *   In the "Thal. $\rightarrow$ L5 k.o." condition, sparsity is significantly reduced across all layers compared to "full."
    *   In the "delay k.o." condition, sparsity remains low across all layers.

Nature Communications| (2025)16:6178
7


---

## Page 8

effect, L2/3 is tasked with ﬁltering out the redundant (such as extra-
neous details or noise) or less informative parts of the previous
encoding (by L4), which leads to a naturally sparser pattern of
activation.

Next, we ablated different model elements during learning to test
their contribution to the emergence of response sparsity (Fig. 6f).
Removing top-down input had a minimal effect on sparseness. How-
ever, ablating thalamic input to L5 during learning selectively decrea-
ses L5 sparseness, likely due to the randomization of L5 responses as a
result. Finally, ablating L2/3-to-L5 connections or the delay component
completely abolished sparsity across all layers, demonstrating their
crucial role in encouraging sparseness over learning.

Overall, these results show that sparsity emerges as a function of
input-driven predictive learning as postulated by our model, thus
providing
an
explanation
for
layer-speciﬁc
sparsity
observed
experimentally.

Model generates sensorimotor mismatch error signals con-
sistent with experimental observations
Our study demonstrates the ability of our cortical model to predict
upcoming sequences. We next sought to investigate the model’s
response when those predictions are violated and to determine if these
responses vary between superﬁcial and deep cortical layers. Addi-
tionally, we wanted to test whether our network generates mismatch
error signals that resemble those observed in cortical networks of
behaving animals19,33,52.

More precisely, we veriﬁed whether our model could reproduce the
mismatch
responses
in
both
L2/3
and
L5,
recently
observed
experimentally19. In the study by Jordan and Keller19 the authors explored
the mismatch error responses in a setting where animals learn to couple
the speed of the visual ﬂow (that is, sliding vertical gratings) to the
animal’s locomotion (Fig. 7a). This paradigm allows for the systematic
investigation of how neural responses in the primary visual cortex are
shaped by the interplay of external sensory stimuli (visual ﬂow) and
internal expectations (running speed). Using whole-cell recordings, Jor-
dan and Keller19 showed that when the visuomotor coupling is tem-
porarily broken (i.e., “visuomotor mismatch”), the majority of L2/3
pyramidal neurons depolarize, whereas a smaller fraction of L2/3 neu-
rons hyperpolarize. In contrast, almost all L5 excitatory neurons hyper-
polarize in visuomotor mismatch. We propose that the differences in L2/
3 and L5 mismatch responses observed experimentally19 can be
explained in a network implementing self-supervised predictive learning.

To gain deeper insights into how our cortical model responds to
violations of expectations, we extended our model to examine its
computational principles under visuomotor mismatch conditions.
Speciﬁcally, we aimed to investigate how the mechanisms underlying
self-supervised predictive learning shape responses to unexpected
disruptions in sensory input. In our setup, the top-down input to L2/3
was deﬁned as the running speed of an animal, modeled by a random
walk process where the speed at any given moment depended on the
preceding speed plus a random variation (see Methods). Under normal
conditions, changes in visual ﬂow were linked to changes in speed by

L5 
L2/3

Locomotion

Visual flow

Data

Data
Model
Data
Model

Model

L2/3 
L5

a
b
c

e
d

Locomotion

Visual flow

Data

500ms

5mv

Model

300 time (a.u.)

1 a.u.

time (s)

Mismatch
Mismatch

600
1200

mismatch error

mismatch error (a.u.)

Fig. 7 | Model generates sensorimotor mismatch prediction errors in line with
experimental observations. a Illustration of visuomotor task used by Jordan and
Keller19 in which mice learned to associate visual ﬂow with locomotion. b Sample of
training data from experiments (top) and our synthetic dataset (bottom). As in the
experimental setup, we randomly halt the visual ﬂow (ﬂat green line) to generate
visuomotor mismatches. c When the visual ﬂow is halted, a sample neuron in L2/3
of the mouse visual cortex shows depolarization (magenta), while a sample neuron
in L5 shows hyperpolarization (blue; left). In our model, in line with the data, L2/
3 shows a positive mismatch error, while L5 shows a negative mismatch error

> Figure caption (from PDF text): Fig. 7 | Model generates sensorimotor mismatch prediction errors in line with
experimental observations. a Illustration of visuomotor task used by Jordan and
Keller19 in which mice learned to associate visual ﬂow with locomotion. b Sample of
training data from experiments (top) and our synthetic dataset (bottom). As in the
experimental setup, we randomly halt the visual ﬂow (ﬂat green line) to generate
visuomotor mismatches. c When the visual ﬂow is halted, a sample neuron in L2/3
of the mouse visual cortex shows depolarization (magenta), while a sample neuron
in L5 shows hyperpolarization (blue; left). In our model, in line with the data, L2/
3 shows a positive mismatch error, while L5 shows a negative mismatch error
> Figure description (generated): This figure, labeled as Figure 7, is divided into several panels (a through e) presenting illustrations of an experimental setup, sample data, and model predictions related to sensorimotor mismatch prediction errors in the mouse visual cortex.

### Panel a: Illustration of Visuomotor Task
Panel **a** is an illustration depicting the experimental setup. It shows a schematic of a mouse performing a visuomotor task.
*   On the left, there is an inset showing a close-up view of the mouse's head/visual field. A scale bar indicates "$<400 \mu\text{m}$".
*   The main illustration shows a mouse on a treadmill or similar apparatus, suggesting locomotion.
*   Above the mouse, there are two schematic representations of visual flow: one labeled "Data" and another labeled "Model."
    *   The "Data" section shows a waveform representing visual flow, with an associated label indicating the experimental context.
    *   The "Model" section shows a corresponding waveform, suggesting the model's simulation of visual flow.

### Panel b: Sample Data and Model Waveforms
Panel **b** presents sample waveforms for locomotion and visual flow, comparing experimental data with model output.
*   The top section is labeled "Data." It shows two waveforms: one for "Locomotion" and another for "Visual flow," both appearing as time-series traces.
*   The bottom section is labeled "Model." It shows two corresponding waveforms: one for "Locomotion" and another for "Visual flow," mirroring the structure of the data section.

### Panel c: Neural Activity Comparison
Panel **c** compares neural activity in different cortical layers during a mismatch event.
*   The panel is divided into two main sections: "Data" (left) and "Model" (right).
*   **Left side ("Data"):** Shows two traces. The top trace is labeled "L2/3" and displays a magenta waveform, indicating depolarization. The bottom trace is labeled "L5" and displays a blue waveform, indicating hyperpolarization.
*   **Right side ("Model"):** Shows two corresponding traces. The top trace is labeled "L2/3" and displays a waveform consistent with the data, while the bottom trace is labeled "L5" and shows a corresponding waveform.

### Panel d: Mismatch Error vs. Locomotion Speed
Panel **d** contains two scatter plots comparing mismatch error against locomotion speed, one for data and one for the model.

*   **Left Plot (Data):**
    *   Y-axis: "mismatch responses ($\text{mV}$)" (ranging roughly from -6 to 5).
    *   X-axis: "locomotion speed ($\text{cm/s}$)" (ranging from 0 to 30).
    *   The plot shows several red data points. A linear fit line is drawn, and the correlation coefficient $R = 0.48$ with $p < 0.001$ is noted, indicating a weak positive correlation.
    *   A second set of data points (blue) is shown, suggesting a different condition or measurement. A linear fit line for this set shows $R = -0.67$ with $p < 0.05$, indicating a moderate negative correlation.

*   **Right Plot (Model):**
    *   Y-axis: "mismatch error ($\text{a.u.}$)" (ranging from -0.5 to 1).
    *   X-axis: "locomotion speed ($\text{a.u.}$)" (ranging from 0 to 10).
    *   The plot shows data points that closely follow a curve, and the fit is indicated with $R = 0.99$ and $p < 1\text{e-}5$, suggesting a strong correlation between the model's mismatch error and locomotion speed.

### Panel e: Spatiotemporal Mismatch Error Maps
Panel **e** displays heatmaps illustrating the mismatch error across different conditions and time points, again comparing data and model.

*   **Top Section (L2/3):**
    *   This section shows a heatmap labeled "Data" on the left and "Model" on the right.
    *   The Y-axis is labeled "Sorted neuron \#" (ranging from 1 to 30).
    *   The X-axis is labeled "time ($\text{s}$)" (ranging from -1 to 2).
    *   The color scale indicates the mismatch error, ranging from approximately -1.0 to 1.5 (with a color bar provided).
    *   The "Data" heatmap shows distinct patterns of activity across neurons and time. The "Model" heatmap mirrors this structure, showing the model's prediction of the mismatch error.

*   **Bottom Section (L5):**
    *   This section also shows a heatmap for "Data" and "Model."
    *   The Y-axis is labeled "Sorted neuron \#" (ranging from 1 to 12).
    *   The X-axis is labeled "time ($\text{s}$)" (ranging from -1 to 2).
    *   The color scale indicates the mismatch error, ranging from approximately -1.0 to 1.0 (with a color bar provided).
    *   Similar to the L2/3 section, both the "Data" and "Model" heatmaps display spatiotemporal patterns of mismatch error.

(right). Shaded areas represent the standard deviation over ﬁve runs. d The mis-
match error signals in L2/3 of the model are correlated with the modeled loco-
motion speed when the visual ﬂow is halted (right), in line with experimental
observations19,52 (left). e The model generates a distribution of mismatch errors
which are biased towards positive errors in L2/3 and negative errors in L5 (right), in
line with mismatch responses observed in primary visual cortex19 (left). Panels
(a, c–e) were partially reprinted from19, with permission from Elsevier. Statistical
tests are two-sided, and no adjustments were made for multiple comparisons. Error
bars represent the standard error of the mean over ﬁve different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
8


---

## Page 9

scaling the visual ﬂow linearly with running speed. Occasionally, we
uncoupled visual ﬂow and speed (locomotion) by setting visual ﬂow to
zero, thus generating visuomotor mismatches (Fig. 7b). This approach
allowed us to probe how predictive learning mechanisms adapt to
disruptions in sensory-motor integration, providing fundamental
insights into cortical computation beyond merely replicating previous
experimental ﬁndings.

We ﬁrst studied the sign and magnitude of layer-speciﬁc mis-
match errors in our model. Since we do not model explicit error neu-
rons, we use a proxy for error activity. Speciﬁcally, we chose to use the
gradient of the cost function with respect to the activity of either L2/3

(MEL2=3 / ∂Ctotal

∂zL2=3

t
) or L5 (MEL5 / ∂Ctotal

∂zL5

t ), which reﬂects the error in each

layer during learning (see Methods). To quantify the mismatch error,
we calculate the gradient in those mismatch phases (visual ﬂow and
running speed uncoupled) relative to the gradient that would occur in
the absence of a mismatch (baseline). If this error is positive relative to
the error baseline (see Methods), we refer to it as a positive mismatch
error. Conversely, if the error is negative relative to the error baseline,
we refer to it as a negative mismatch error.

When visual ﬂow was randomly halted during locomotion, we
observed, on average, a positive mismatch error in L2/3 and a negative
mismatch error in L5 (Fig. 7c), consistent with mismatch responses
observed experimentally (Fig. 7c). The discrepancy between L2/3 and
L5 arises from their roles, as postulated by our self-supervised learning
cost (or error function, Eq. 5): L2/3 output predicts the upcoming
visual ﬂow while L5 encodes the actual visual ﬂow. Hence, when visual
ﬂow halts and given top-down running speed, L2/3 output predicts a
non-zero ﬂow, thereby resulting in a positive mismatch error
(zL2=3

t
> zL5

t , MEL2/3 >0). L5, in contrast, encodes the actual zero ﬂow,
and, hence, generates a negative mismatch error due to the (positive)
prediction provided by L2/3 output targeting L5 (zL2=3

t
> zL5

t , MEL5 <0).
Furthermore, we found that the mismatch responses in our model
scale linearly with the running speed (Fig. 7d), in line with
experiments19,52. These differential mismatch errors between L2/3 and
L5 disappear when each layer optimizes its own error function rather
than a shared one (Fig. S11), suggesting that both layers are jointly
optimized towards common objectives.

To further test whether the mismatch errors across neurons
resemble those experimentally19, we analyzed the distribution of mis-
match errors in our model. Our results show that the majority of L2/3
neurons exhibit positive mismatch errors while the majority of L5
neurons exhibit negative mismatch errors (Fig. 7e; see also Fig. S12 for
mismatch errors across different model conditions), in line with Jordan
and Keller19.

A key ﬁnding from Jordan and Keller19 was that mismatch
responses invert under an open-loop paradigm, where visual ﬂow is
decoupled and presented independently of locomotion. In this open-
loop condition, L2/3 neurons, which were previously depolarized dur-
ing visuomotor mismatch in the closed-loop condition, instead exhib-
ited hyperpolarization, while L5 neurons showed the opposite effect.
This suggests that mismatch responses are shaped by the expected
visual input rather than simply reﬂecting inherited sensory signals.

To better understand the computational principles underlying
these experimental observations, we examined whether our model
could capture this inversion of mismatch responses. Our model
leverages top-down contextual information to help L2/3 in predicting
incoming sensory input. However, predictive signals can also emerge
intrinsically from the data itself, independent of top-down input, as
shown in Fig. S3c. To investigate how our self-supervised predictive
mechanism inﬂuences error signals, we trained our model in an open-
loop paradigm where visual ﬂow varied independently of running
speed (see SM for details). After training, we examined how the model
responds when the expected visual ﬂow pattern is disrupted by pre-
senting visual ﬂow after a brief period of zero ﬂow. Our model

qualitatively reproduced the experimental ﬁndings (Fig. S13), showing
an inversion of mismatch errors between L2/3 and L5.

This sign ﬂip arises from the predictive mechanism: in the closed-
loop condition, where visual ﬂow halts, L2/3 neurons overestimate sen-
sory input, leading to a positive mismatch error. In contrast, in the open-
loop condition, where visual ﬂow is introduced randomly, L2/3 neurons
underestimate sensory input, resulting in an error of the opposite sign.
These results align with experimental observations and further support
the presence of predictive mechanisms in the cortical circuit.

Here, we have focused on a feedforward implementation of the
model, but cortical layers are also known to integrate information over
time53. To test the effect of recurrence, we extended our model by
incorporating an RNN in L2/3 (Fig. S14). Modeling L2/3 as an RNN enables
it to integrate information from past inputs over longer timescales and
use this temporal context to predict incoming inputs in layer 5. Inter-
estingly, in addition to capturing the key ﬁndings described above, our
model also captures the qualitative differences in neural responses
between playback halt and visuomotor mismatch conditions observed in
coupled training (CT) and non-coupled training (NT) paradigms, as
reported by Attinger et al.54. Speciﬁcally, the model reproduces the
selective mismatch responses in CT (response to mismatch, but not
playback halt) versus generalized responses in NT (responses to both
conditions). However, while the experimental data shows that CT mis-
match responses are two to three times larger than NT responses, our
model produces similar response magnitudes under both conditions.

Differential role of L2/3 and L5 during sensorimotor mismatches
We have shown that the mismatch error responses observed in L2/3
and L5 of awake, behaving animals19 can be explained by the distinct
roles played by cortical layers engaged in self-supervised predictive
learning. This suggests that layer-speciﬁc manipulations, for example,
simulated optogenetic stimulation of L2/3 and L5 neurons, may reveal
their unique functions. To test this in our model, we selectively
increased the neuronal response of either L2/3 or L5 neurons during
sensorimotor mismatches to determine their contributions to the
mismatch errors in the other layer, L5 and L2/3, respectively.

To this end, we ﬁrst scaled the output of L5 neurons. With mod-
erate scaling, both positive and negative mismatch errors in L2/3
decrease in magnitude (Fig. 8b). As L5 activity increased further,
neurons that displayed a positive mismatch error before scaling swit-
ched their sign to display a negative mismatch error. Likewise, neurons
with a negative mismatch error before scaling signal a positive mis-
match error after scaling (Fig. 8a, b). These results are a consequence
of L5 neurons representing zero input during sensorimotor mismatch,
while L2/3 neurons predict non-zero visual ﬂow due to non-zero top-
down input. Hence, as the L5 output increases, the feedback signal
from L5 eventually surpasses the L2/3 prediction, leading to a reversal
in the signs of mismatch errors in L2/3.

Thus far, we have scaled the L5 output as a whole, without dif-
ferentiating between neurons exhibiting a positive or negative mis-
match error. When we scaled only the outputs of L5 neurons with a
positive mismatch error, the changes in L2/3 mismatch errors were
heterogeneous (Fig. S15). This is likely due to the low number of neu-
rons with positive mismatch errors in L5, limiting their impact on L2/3.
In contrast, scaling only the output of L5 neurons with negative mis-
match errors reversed the mismatch errors in L2/3 (Fig. S15), similar to
the effect of scaling the entire L5 output (Fig. 8b).

Next, we studied how scaling the output of L2/3 affects the mis-
match errors in L5. When the output of L2/3 neurons is scaled as a
whole, the mismatch errors in L5 are ampliﬁed: neurons with a negative
mismatch error before scaling exhibit an even stronger negative error,
while those with a positive mismatch error show an even stronger
positive error after scaling (Fig. 8c, d). This remains true even when we
only scale the neurons with a positive mismatch error in L2/3 (Fig. S15).
However, scaling only the L2/3 neurons with negative mismatch errors

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
9


---

## Page 10

reverses the mismatch errors in L5 (Fig. S15. Hence, our model predicts
a dynamic interplay between L2/3 and L5, with L2/3 stimulation gen-
erally amplifying L5 mismatch errors. Interestingly, this effect is pre-
dominantly driven by L2/3 neurons signaling positive mismatch errors,
while stimulating the neurons in L2/3 with negative mismatch errors
reverses the direction of mismatch errors in L5.

These results can be best explained by the asymmetric contribu-
tion of L5 and L2/3 in generating mismatch errors. The strong effect of
neurons with a positive mismatch error in L2/3 aligns with their role in
predicting sensory input; increasing their activity strengthens this
prediction signal within L5. Conversely, neurons with a negative mis-
match error in L2/3 likely represent neurons suppressed by a greater-
than-expected input. Enhancing their activity during a mismatch fur-
ther emphasizes this “less-than-expected” signal, ultimately reversing
the sign of the mismatch error in L5.

Overall, these targeted manipulations of layer-speciﬁc mismatch
errors provide a valuable method for dissecting the distinct functional
roles of L5 and L2/3 populations. This approach could be further
explored experimentally to deepen our understanding of how neo-
cortical layers contribute to the predictive learning of sensory streams.

Discussion
Inspired by a refreshed view of the canonical neocortical circuitry and
modern self-supervised learning algorithms, we introduce a compu-
tational theory wherein L2/3 output learns to anticipate incoming
sensory input. We demonstrated L2/3’s capacity to predict incoming
sensory information using temporal-contextual tasks. As a result, L2/3
develops latent sensory representations that are resilient to sensory
noise and occlusions, improving the ability of cortical networks to
encode partially observable information. Additionally, the proposed
optimization leads to layer-speciﬁc sparsity, in line with experimental
ﬁndings. Subsequently, by employing a sensorimotor task, we reveal
that the model’s mismatch errors align with L2/3 and L5 mismatch
responses observed in awake, behaving mice. Finally, using manip-
ulations, we generated predictions for the role of speciﬁc circuit ele-
ments in self-supervised predictive learning.

Our study focuses on the canonical L4-L2/3-L5 three-layered
motif17,18. This classical view of the neocortical microcircuit emphasizes
the feedforward ﬂow of information across layers. However, feedback
projections are also evident39,40 and both anatomical and electro-
physiological data suggest the existence of direct thalamic input into L5
pyramidal cells that effectively bypasses this feedforward circuit22,23,25,26,55.
Our model explores the computational signiﬁcance of these pathways by

mapping them onto a self-supervised learning framework. Our results
suggest that the two parallel thalamic pathways serve critical but distinct
functions: the L4-L2/3 pathway generates temporal predictions, while the
thalamic-L5 pathway provides the self-supervised target (i.e., incoming
sensory input) against which these predictions are tested. Feedback from
L5-to-L2/3 connects the two parallel systems to guide learning. However,
in principle, the L2/3 lateral connectivity can also provide similar spa-
tiotemporal targets for self-supervised learning. This possibility remains
to be explored in future work.

Our model proposes that a critical feature of L2/3’s integrative
capacity is to use past information to predict incoming sensory
input. This is in line with the stronger temporal integration of sensory
information in superﬁcial layers compared to deep layers56,57, which
is further reinforced by our variant of the model, where we represent
L2/3 as an RNN (Fig. S14). Moreover, our work indicates that the
delay introduced by the thalamic-L4-L2/3 pathway is critical for the
emergence of these properties. It also suggests that the delay
introduced by these neurons and synapses sets the time scale that
L2/3 neurons use for temporal prediction. Since this delay is on the
order of a few milliseconds26,58, our model suggests that the temporal
resolution for prediction in L2/3 of primary sensory cortices is
constrained.

In principle, it is possible to achieve hierarchical spatiotemporal
learning by stacking cortical areas. This is because the inherent delay in
the L4-to-L2/3 circuit within each cortical area introduces a lag
between the information available to L2/3 and the target represented
in L5 (Fig. S16). Although simulating this hierarchical model is beyond
the scope of this work, we can speculate on its computational and
functional beneﬁts. First, such an organization enables learning tem-
poral dependencies beyond a single timestep, allowing the system to
integrate information over longer timescales. Although learning
extended temporal structures can be challenging, this architecture
mitigates the difﬁculty by making predictions in the latent space rather
than the input space. By leveraging hierarchical feature extraction, the
model focuses on high-level, abstract features while discarding irre-
levant details. Speciﬁcally, higher-order areas make predictions based
on more past information, but their task is simpliﬁed as they predict
higher-level, more invariant features. In contrast, lower-level areas,
which have access to more recent inputs, must predict ﬁner details.
This hierarchical model suggests that higher-order areas integrate
sensory information over progressively extended durations, con-
sistent with evidence showing that cortical areas incorporate increas-
ingly longer temporal windows at higher levels of the hierarchy59,60.

b
c
d
a

L2/3

L4

L5
Stim

L2/3

L4

L5

Stim

Mismatch
Mismatch

mismatch error

mismatch error

L2/3 mismatch error

L5 mismatch error

no stimulation
with stimulation

no stimulation
with stimulation

Fig. 8 | Differential role of L5 and L2/3 activation in generating mismatch
errors. a Stimulating L5 during the mismatch interval causes mismatch errors in L2/3
to switch signs. When stimulating L5 neurons, L2/3 neurons that exhibited positive
mismatch errors (magenta) become negative (top) and vice versa (blue; bottom).
b Positive errors gradually shift towards negative and vice versa, demonstrating a
direct relationship between L5 stimulation and L2/3 mismatch error modulation.

> Figure caption (from PDF text): Fig. 8 | Differential role of L5 and L2/3 activation in generating mismatch
errors. a Stimulating L5 during the mismatch interval causes mismatch errors in L2/3
to switch signs. When stimulating L5 neurons, L2/3 neurons that exhibited positive
mismatch errors (magenta) become negative (top) and vice versa (blue; bottom).
b Positive errors gradually shift towards negative and vice versa, demonstrating a
direct relationship between L5 stimulation and L2/3 mismatch error modulation.
> Figure description (generated): This figure, labeled "Fig. 8," presents a set of plots illustrating the differential role of L5 and L2/3 activation in generating mismatch errors. The figure appears to be composed of two main parts, labeled 'a' and 'b', although the provided image snippet only clearly shows the data associated with a single plot structure, which is described in the caption as relating to both parts.

### 1. Overall Layout & Structure
The visible portion of the figure is a line graph displaying data points connected by lines, suggesting a trend analysis over some variable (likely time or stimulus condition). The structure includes a Y-axis and an X-axis, with multiple data series represented by different markers and colors.

### 2. Visual Components & Symbols
*   **Axes:** A vertical Y-axis is present, with numerical markings visible (e.g., 0, 5). A horizontal X-axis is present but lacks explicit labels in the visible area.
*   **Data Series:** Two distinct data series are plotted:
    *   One series is represented by **gray circular markers ($\bullet$)**.
    *   The second series is represented by **black inverted triangle markers ($\boldsymbol{\nabla}$)**.
*   **Lines and Markers:** Both series are connected by lines, indicating a progression or trend.
*   **Reference Line:** A dashed horizontal line is present across the plot, positioned at a value of 0 on the Y-axis.
*   **Error Bars:** Vertical lines (error bars) are attached to some of the data points, indicating variability.

### 3. Labels, Keys & Legends
*   **Legend:** A legend is provided in the lower-left corner:
    *   "positive" corresponds to the **gray circular markers ($\bullet$)**.
    *   "negative" corresponds to the **black inverted triangle markers ($\boldsymbol{\nabla}$)**.
*   **Annotations:** The text "L5 Stim" is visible near the top, suggesting the context of L5 stimulation.

### 4. Data Trends & Details
The plot shows a clear divergence between the two data series:

*   **Gray Circles ("positive"):** These points start high (near +5) on the left side of the graph, decrease sharply, cross the zero line, and continue to decrease towards negative values on the right side.
*   **Black Triangles ("negative"):** These points start low (near -5) on the left side of the graph, increase sharply, cross the zero line, and continue to increase towards positive values on the right side.

The caption clarifies that this plot illustrates how L5 stimulation causes a sign switch in L2/3 mismatch errors: "When stimulating L5 neurons, L2/3 neurons that exhibited positive mismatch errors (magenta) become negative (top) and vice versa (blue; bottom)." While the plot uses gray/black markers, the caption links these trends to positive and negative error states.

### 5. Contextual Caption Integration
The caption provides crucial context:
*   **Panel (a) Interpretation:** Stimulating L5 during the mismatch interval causes mismatch errors in L2/3 to switch signs. Specifically, neurons showing positive errors (represented by magenta in the caption's description) become negative, and vice versa.
*   **Panel (b) Interpretation:** The data demonstrates a direct relationship where positive errors gradually shift towards negative, and vice versa, due to L5 stimulation.

In summary, the visible plot visually represents a dynamic shift in error polarity (positive $\leftrightarrow$ negative) as a function of the experimental condition, consistent with the described modulation effect of L5 stimulation on L2/3 mismatch errors.

> Figure caption (from PDF text): Fig. 8 | Differential role of L5 and L2/3 activation in generating mismatch
errors. a Stimulating L5 during the mismatch interval causes mismatch errors in L2/3
to switch signs. When stimulating L5 neurons, L2/3 neurons that exhibited positive
mismatch errors (magenta) become negative (top) and vice versa (blue; bottom).
b Positive errors gradually shift towards negative and vice versa, demonstrating a
direct relationship between L5 stimulation and L2/3 mismatch error modulation.
> Figure description (generated): This figure presents a single plot illustrating the modulation of mismatch errors, likely derived from electrophysiological recordings.

**1. Overall Layout & Structure:**
The figure consists of a single graph, which appears to be a time-series plot showing error magnitude over time. The structure is dominated by the plotted data curves against a background timeline marked with an annotation indicating a "Mismatch" interval.

**2. Visual Components & Symbols:**
*   **Axes:** The vertical axis (Y-axis) is labeled with numerical values ranging from 0 to at least 7. The horizontal axis (X-axis) is marked with numerical values, including 0 and 500.
*   **Data Curves:** Two distinct lines are plotted:
    *   A magenta/pink line representing one condition. This curve shows a characteristic "M" shape within the shaded region.
    *   A black line representing another condition, which remains close to zero across the entire plotted range.
*   **Shading/Annotation:** A light gray shaded rectangular region spans a specific interval on the X-axis, labeled above as "Mismatch." This shading highlights the period during which mismatch errors are being analyzed.
*   **Legend:** A legend is present in the upper right quadrant of the plot area, defining the line styles:
    *   A dashed black line corresponds to "no" (presumably no L5 stimulation).
    *   A solid black line corresponds to "wit" (presumably with L5 stimulation, although the magenta curve seems to represent the primary data being discussed in the caption).

**3. Labels, Keys & Legends:**
*   **Title/Annotation:** "Mismatch" is displayed above the shaded region.
*   **Y-axis Labeling:** Numerical ticks are present (0, 5, etc.).
*   **X-axis Labeling:** Numerical ticks are present (0, 500).
*   **Legend Entries:** "no" and "wit".

**4. Data Trends & Details (Interpreting the Plot based on Caption Context):**
The plot displays error magnitude over time. The magenta curve exhibits significant, transient activity within the "Mismatch" interval (roughly between X=100 and X=650). This curve shows a pattern: it rises sharply, dips significantly into negative values (implied by the context of error modulation), and then rises again. The black line ("no") remains near zero throughout the interval, suggesting a baseline or control condition where errors are minimal.

**5. Contextual Caption Integration:**
The caption clarifies the meaning of these visual elements:
*   **Panel Context (Implied):** The figure likely represents the results described in Figure 8, which examines the "Differential role of L5 and L2/3 activation in generating mismatch errors."
*   **Curve Interpretation:** The caption states that stimulating L5 causes changes in L2/3 errors. Specifically, "L2/3 neurons that exhibited positive mismatch errors (magenta) become negative (top) and vice versa (blue; bottom)." This strongly suggests the magenta curve represents a condition where positive errors are observed, and its subsequent modulation (or comparison to other conditions not fully visible or labeled in the plot) demonstrates the effect of L5 stimulation.
*   **Trend Interpretation:** The caption notes, "Positive errors gradually shift towards negative and vice versa, demonstrating a direct relationship between L5 stimulation and L2/3 mismatch error modulation." This confirms the plot is designed to show this dynamic shift in error polarity due to L5 input.

c Stimulating L2/3 during the mismatch interval ampliﬁes existing mismatch errors
within L5. When stimulating L2/3 neurons, L5 neurons that exhibited positive mis-
match errors remain positive (top), and L5 neurons that exhibited negative mismatch
errors remain negative (bottom). d Plot demonstrates a proportional increase or
decrease in mismatch error magnitude as the output of L2/3 is scaled. Error bars
represent the standard error of the mean over ﬁve different initial conditions.

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
10


---

## Page 11

Furthermore, experimental ﬁndings indicate that superﬁcial layers
exhibit stronger temporal integration than deeper layers56,57, further
supporting the role of hierarchical structure in temporal learning.

Beyond facilitating multi-timestep predictions, this hierarchy also
serves a regularizing function. The joint self-supervised loss between
L2/3 and L5 encourages L5 to encode not only spatially invariant fea-
tures but also temporally invariant representations. This aligns with
ﬁndings that hierarchical temporal prediction can explain receptive
ﬁeld properties across the visual cortex61, suggesting that the brain’s
predictive mechanisms inherently favor stable, abstract representa-
tions at higher levels.

These properties suggest a computational advantage for hier-
archical predictive learning, where extended temporal context
enhances abstraction and stability in neural representations. However,
further work is needed to validate these hypotheses through simula-
tions and experimental studies.

It has been well documented that superﬁcial layers respond
more sparsely to sensory stimuli than deep layers47. However, it was
not known how this feature emerges. In our model, layer-speciﬁc
sparsity occurs naturally due to the proposed predictive function of
L2/3 output (Fig. 6). Our results also imply that simple measures like
sparsity can help infer the optimization/learning processes of various
brain structures. Indeed, we show how selective ablations of
individual components of the network alter sparsity in a layer- and
pathway-speciﬁc
manner.
While
these
ﬁndings
provide
important insights into the nature of sparsity in cortical networks,
fully understanding the interplay between input, connectivity, and
the
emergence
of
sparsity
during
learning
requires
further
investigation.

While our model has been mapped onto the canonical six-layered
structure of the neocortex, it operates with only three layers. This
raises an intriguing consideration: the evolutionarily conserved three-
layered structures found in other brain regions, such as the hippo-
campus and piriform cortex in mammals, as well as in the cortices of
other species, such as turtles62, may represent the foundational blue-
print for self-supervised learning. This structure was subsequently
elaborated upon throughout evolution, ﬁrstly by increasing the num-
ber of layers, and secondly by expanding the primary locus of self-
supervised learning in L2/3. Consistent with this view, we also ﬁnd that
sparsity increases as the number of neurons in L2/3 increases (Fig. 6b).
L2/3 is greatly expanded in human evolution, even when compared to
other layers49,50. Our results suggest that this expansion could enhance
network function, particularly by broadening the predictive cap-
abilities of the human neocortex.

L2/3’s predictive capability can be enhanced by the contextual
information it receives via top-down inputs. This contextual infor-
mation can originate from higher-order areas within the same sen-
sory modality or from other sensory and motor areas. According to
our model, L5 neurons primarily encode the current input received
through thalamic projections and provide learning signals to L2/3 via
feedback connections within a cortical column. Because L5 repre-
sents the present sensory input, as opposed to L2/3’s potentially
inaccurate predictions, it is well-positioned to supply other areas
with contextual information about the sensory state it is currently
encoding. For example, L5 pyramidal cells in the auditory cortex
might provide auditory context to L2/3 neurons in the visual
cortex63,64. Within L5, different cell types likely serve distinct roles: L5
pyramidal tract neurons may facilitate the form of local self-
supervised learning proposed here, while L5 intratelencephalic neu-
rons might specialize in relaying feedback to L2/3 across cortical
areas40,65.

Our model predicts the need for feedback between the neo-
cortical layers that carry information about error signals. This pro-
vides a form of credit assignment within the neocortical microcircuit.
Although neocortex models often overlook feedback pathways,

numerous experimental studies demonstrate their existence39,40,66.
Despite this, these pathways are understudied and their organization
is not well understood, in contrast to feedforward, which often
shows highly organized subnetwork architectures67–69. Our ﬁndings
indicate that both structured (i.e., reciprocal), as well as sparse,
random
feedback
enable
learning,
with
the
former
potentially advantageous for more complex tasks. A further question
is how feedback error signals may be computed in a biologically
plausible manner. Recent work shows how this can be achieved using
dendritic compartments and interneuron cell types70–72. Different
interneuron subtypes, with distinct connectivity, control feedfor-
ward and feedback processing in the L2/3-L5 circuitry73–76, which may
underlie
distinct
aspects
of
the
self-supervised
learning
proposed here.

While these studies suggest biological mechanisms through
which self-supervised learning may emerge, is there evidence that it
occurs within the brain? Recent experimental studies support the
ability of the neocortex to perform self-supervised learning77. Con-
sistent with these observations, deep networks trained using self-
supervised learning better capture experimentally observed repre-
sentations compared to networks trained via supervised learning13. For
example, training deep networks using self-supervised predictive error
functions
yields
representations
that
resemble
visual
cortical
features8,16,61,78–80. Taking a step towards understanding the underlying
learning mechanisms, recent research has introduced a combination
of Hebbian and predictive synaptic plasticity12. This body of work
supports the notion that sensory cortices engage in self-supervised
learning, yet the speciﬁc circuit-level computations facilitating this
process have remained unclear. Our work ties self-supervised learning
to speciﬁc neocortical layers, suggesting that L2/3 and L5 provide
complementary roles for implementing self-supervised learning.
Consistent with these ﬁndings, the L2/3-to-L5 pathway is highly con-
served across cortical regions81,82, and behavioral studies have high-
lighted its importance for learning83. In future work, it would be
interesting
to
test
our
theory
by
performing
layer-speciﬁc
experiments84,85.

Predictive coding offers a framework for understanding how
sensory representations are learned in the brain86–88. It postulates that
the brain learns an internal model of the world from sensory streams
by directly updating neuronal dynamics through prediction errors1,7. In
temporal predictive coding, the neural networks constantly attempt to
predict the incoming stimulus. Lotter et al.89 demonstrated that a deep
convolutional network that is trained using predictive coding learned
sensory representations useful for downstream tasks. This contrasts
with our model, where prediction violations drive plasticity rather than
directly altering neuronal dynamics.

A related point is the fact that in our model, self-supervised
errors and mismatch signals are derived directly from the error
functions to drive the plasticity of model parameters. Implementing
such error-driven signals in a biologically plausible manner remains
an open question. However, we suggest two potential approaches to
further develop our model, combining both inference and learning
through neural dynamics (see also extended discussion in the SM).
The ﬁrst approach involves building on multiplexing theories of the
backpropagation algorithm72,90,91. Building on the multiplexing fra-
mework, error signals originating in layer 5 could be kept separate
from inference signals. These error-like events, potentially in the
form of bursts, would propagate from L5 to L2/3, representing pre-
diction errors in neuronal activity. The second approach would be to
recast our model within a predictive coding framework30,92. Pre-
dictive coding jointly optimizes both model parameters and neuro-
nal activities, which could naturally lead to prediction errors
observable in the activity of both L2/3 and L5 neurons. Note that
these two views are not mutually exclusive, as has previously been
demonstrated30.

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
11


---

## Page 12

Temporal predictive coding models are also often relatively
abstract and do not consider how predictive coding is implemented. A
notable exception is the work of Bastos et al.1 in which it was proposed
that L5 encodes input expectation while L2/3 encodes positive and
negative prediction errors in separate populations. In contrast, our
model proposes that L2/3 output predicts the incoming input to L5,
which encodes the current sensory input. Additionally, L5 locally
computes the self-supervised error between the L2/3 prediction and its
current state. This approach helps explain a range of experimental
observations. A distinguishing feature of our model, compared to
existing predictive coding models, is its ability to both predict
incoming sensory input in L2/3 and represent the current input in L5,
aligning with recent advancements in deep learning93. In future work, it
would be of interest to explicitly contrast our model with existing
predictive coding frameworks.

In general, our work suggests that the circuit motifs found
throughout the neocortex implement self-supervised predictive
learning in the brain.

Methods
We model the neocortical circuitry by using a network of inter-
connected neuronal layers. The architecture includes distinct layers
corresponding to L4, L2/3, and L5 of the neocortex, with all-to-all
connectivity between layers unless otherwise speciﬁed.

To represent the delayed input from L4 to L2/3, we denote the
encoding of past sensory (or thalamic) input xt−1 by L4 as follows:

zL4

t1 = σðWThal.!L4  xt1Þ
ð1Þ

where σ is a sigmoid function and WThal.→L4 is the weight matrix that
models the connectivity from the thalamus to all L4 neurons. We
model the neuronal and synaptic delay by explicitly representing L4’s
encoding of input from the previous time step, t −1, which is then
processed by L2/3. More precisely, L2/3 integrates the delayed input,
zL4

t1, from L4 with top-down inputs at t from higher-order cortical
areas, Itd

t . Hence, L2/3 is modeled as

zL2=3

t
= σðW L4!L2=3  zL4

t1 + W td!L2=3  Itd

t Þ
ð2Þ

where z23 is a vector with all neurons in L2/3 and WL4→L2/3 is the weight
matrix from L4 to L2/3. As above, all neurons are subject to the sigmoid
non-linearity σ. L5 receives direct thalamic input, xt, and L2/3 input. It is
modeled as,

zL5

t = σðαW L2=3!L5  zL2=3

t
+ W Thal:!L5  xtÞ
ð3Þ

where z5 is a vector with all L5 neurons, WL2/3→L5 and WThal.→L5 are the
weight matrices from L2/3-to-L5 and thalamus-to-L5, respectively. The
constant α models the dendritic-to-somatic attenuation of L2/3-to-L5

input. We set α = 0.3, but the exact value does not qualitatively change
our results.

In our network, the weight matrices WL2/3→L5, WL4→L2/3, WThal.→L4,
WThal.→L5, and Wtd→L2/3 are subject to optimization through gradient
descent. The learning rules for these connections are derived from
cost functions inspired by those commonly used in self-supervised
machine learning. In particular, we use a combination of two cost
functions,

Ctotal = λpCL2=3!L5
|ﬄﬄﬄﬄﬄﬄﬄ{zﬄﬄﬄﬄﬄﬄﬄ}
predictive

+
λrCL5
|ﬄ{zﬄ}
reconstruction

,

ð4Þ

where λp and λr are hyperparameters that scale the predictive and
reconstruction costs, respectively. The ﬁrst component of Ctotal is the
temporal self-supervised cost, where L2/3 predictions based on L4
input at time t −1 are compared with L5 activity at time t

CL2=3!L5 = 1

2 ðWL2=3!L5  zL2=3
t
|ﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄ{zﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄﬄ}

prediction, ^zL5

t

zL5

t Þ

2:
ð5Þ

The second component of Ctotal encourages the model to learn non-
trivial representations by reconstructing L5 thalamic input given its
own activity, as follows

CL5 = 1

2 ðxt  W decoder  zL5
t Þ

2:
ð6Þ

The reconstruction cost serves as a regularization term to prevent
representational collapse (i.e., trivial representations) in L5. It is
applied only in L5, as it receives direct thalamic input and acts as the
primary representational layer, whereas L2/3 predicts the input
representation without directly encoding it or accessing thalamic
input. To maintain this distinction, WL2/3→L5 and WL4→L2/3 are updated
solely to minimize prediction loss, while WThal.→L5 is also adapted to
minimize both prediction and reconstruction loss.

Hence, to ensure that the reconstruction error is not propagated
to L2/3, we block the resulting error signals (i.e., gradients) from
adjusting WL2/3→L5 weights and WL4→L2/3. To be precise, WL2/3→L5
weights and WL4→L2/3 synapses are only adapted to minimize the
prediction error from the past, while the WThal.→L5 synapses are
adapted in addition to minimize both the prediction and recon-
struction loss. This particular separation of learning helps prevent
representational collapse29, by ensuring that L2/3 and L5 follow dif-
ferent learning objectives. However, other approaches, such as var-
iance maximization12,37, also work (see Fig. S5).

The learning rule for WL2/3→L5 can be derived from the cost func-
tion as,

ð7Þ

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
12


---

## Page 13

where we denote the effect of the attenuation factor by A. The term

λr∂CL5
∂W L2=3!L5 is set to zero to prevent the reconstruction cost-related gra-

dient from ﬂowing back to L2/3.

Similarly, one can derive the learning rule for WL4→L2/3 is given
by the derivative of the cost function with respect to this weight
matrix,

where W T=random

L2=3!L5
is the transpose of WL2/3→L5 or a random matrix,

depending on the experiments we performed (see Fig. 6). As before,

the term
λr∂CL5
∂W L4!L2=3 is set to zero to prevent the reconstruction cost-

related gradient from ﬂowing back to L2/3. Finally, the learning rule for
WThal.→L5 can also be derived following a similar procedure:

ΔWThal.!L5 =  η
∂Ctotal
∂WThal.!L5

!

=  η

λp∂CL2=3!L5

∂zL5

t

+ λr∂CL5

∂zL5

t





∂zL5

t
∂WThal.!L5

=  η λpðW L2=3!L5  zL2=3

t
 zL5

t Þ + λrðW decoder  zL5

t  xtÞ  W decoder
h
i

xt:

ð9Þ

Tasks
Gabor contextual-temporal task. This task aims to investigate how
Gabor patches at t can be predicted based on their orientation deter-
mined by a top-down variable. To do so, we generate synthetic
sequential data where each data point is a 28 × 28 Gabor patch. The
frequencies of these patches are sampled from N ð0:2, 0:1Þ, with
variability along the x and y axes drawn from Uð3, 8Þ, and orientations
ﬁxed for each class, θ = [0, 18°, 36°, …, 162°]. The top-down inputs can
take values of [−18°, 0°, +18°].

At each timestep, we randomly sample a data point xt with
orientations θi where i denotes the index in the θ list, and a top-down
contextual input Itd

t . The next input xt+1 is then generated by sampling
a data point with orientation θi + Itd

t . This setup allows for three
orientations at time step t + 1 (orientation shifts to the left, shifts to the
right, or remains the same), except for angles 0° and +162°, which only
have two possible successors.

According to our model, at each time step, L5 receives xt as its
sensory input. Simultaneously, the L2/3 network processes the output
of L4 combined with the top-down contextual input.

Noise and occlusion tests. These experiments assess the model’s
robustness to input degradation (Fig. 4). We focus on two forms of
degradation: noise and occlusion. For noise, Gaussian noise is added to
the input as x*

t = xt + λ ϵt, where ϵt  N ð0, IÞ, and λ scales the noise
level (values from 0 to 1, in increments of 0.2). To examine the
importance of the L2/3 →L5 connection, we selectively disable the self-
supervised cost during training. This prevents updates to WL2/3→L5,
WL4→L2/3, and WThal.→L4through this loss, isolating the effects of this
connection. Reconstruction performance across layers is measured
using the mean squared error between the reconstructed and the
original (denoised) input.

For occlusion, random image sections are obscured with a dark
patch (pixel values set to zero). After training, a Support Vector
Machine is used to classify outputs of L2/3 and L5 based on the xt label.

Classiﬁcation accuracy on a held-out test set indicates how well the
model copes with occlusions.

Visuomotor task
Simulating the experimental setup. To closely replicate the visuo-
motor task from Jordan and Keller19, we generated synthetic sensor-
imotor data to model visual ﬂow and motor speed. In our model, each

vector dimension encapsulates a distinct aspect of visual ﬂow, which is
essential for simulating the sensory inputs typical in motion perception
tasks. In particular, visual ﬂow was calculated as xt at any given time t
following

xt = f st




+ ϵt

where, f denotes a function that converts speed into visual ﬂow. We set
f(st) = st to model a linear relationship (Figs. 7, 8) or f ðstÞ = sinðstÞ to
model a nonlinear interaction (Fig. S11c). The term st represents the
speed at time t. To mimic more realistic conditions, we also add
Gaussian noise, ϵt  N ð0, IÞ. In our simulations, we model speed fol-
lowing a random walk. At each timestep, the speed st is determined
with equal probability between the following options

• Decreasing by 1: st = st−1 −1
• Remaining the same: st = st−1
• Increasing by 1: st = st−1 + 1

This approach simulates natural ﬂuctuations of running speed, in
which an individual might slightly accelerate, decelerate, or maintain
pace from moment to moment. After sampling speeds, we generate
visual ﬂow input xt−1 = f(st−1) and xt = f(st), with noise as deﬁned above.

The speed variable provides top-down context, an important
factor in our model that provides contextual information. This infor-
mation helps L2/3 to predict the incoming visual ﬂow given past visual
ﬂow and the current speed.

Mismatch simulation and measurement. After training, we obtain a
baseline error signal by averaging the gradient for each neuron across

the dataset, that is, MEi, BL = h∂Ctotal

∂zi

t i

BL. Next, we simulate a mismatch (i.e.,

breaking the coupling between locomotion and visual feedback) by
randomly setting the visual ﬂow to zero. Each mismatch period lasted
for k timesteps (k = 600 timesteps). During this mismatch period, we
record
the
average
gradient
for
each
neuron,
that
is,

MEi, MM = h∂Ctotal

∂zi

t i

MM. To isolate the mismatch response for each neuron

zi, we use the formula: MEi = MEi,MM −MEi,BL. We provide a simulation
of the contribution of the reconstruction and predictive losses to the
total gradient in Fig. S17. This analysis shows that backpropagating the
L5 reconstruction cost to L2/3 does not have a signiﬁcant impact on
the L2/3 gradients.

L2/3 and L5 mismatch errors (ME). The mismatch errors in L2/3 and
L5 analysed in Figs. 7, 8 were calculated using the gradients of the self-
supervised learning cost with respect to the activity of L2/3 and L5
neurons during mismatch and baseline conditions (see above). The L2/

ð8Þ

Article
https://doi.org/10.1038/s41467-025-61399-5

Nature Communications| (2025)16:6178
13


---

## Page 14

3 gradient is calculated as

∂Ctotal
∂zL2=3

t

= λp W L2=3!L5  zL2=3

t
 zL5

t



W L2=3!L5  α  σ0 αW L2=3!L5  zL2=3

t
+ W Thal:!L5  xt



W L2=3!L5



:

ð10Þ

Similarly, the L5 gradient is calculated as

∂Ctotal

∂zL5

t

=  λpðW L2=3!L5  zL2=3

t
 zL5

t Þ  λrðxt  W decoder  zL5

t ÞW decoder:
ð11Þ

Sparsity metric
To measure the sparsity of each layer in our model, we used the
Treves–Rolls metric48,94. The population sparseness, S, of each layer for
a single stimulus was measured as:

S = ½PN

i = 1 ri=N

2

PN

i = 1½r2

i =N

where N is the number of neurons, and ri the activation rate of neuron i.
To get the average population sparseness for the entire sequence, we
average S over a trial.

Feedback and feedforward connection probabilities
In our work, we investigated the importance of feedback from L5 to L2/3
for learning. As part of this, we tested a range of connection prob-
abilities, Pconnectivity, for this feedback pathway. The feedback connec-
tions from L5 to L2/3 are removed with the probabilityof(1 −Pconnectivity).
The connection probability of all forward connections was set to 1.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability
Source data for all ﬁgures are provided as a Source Data ﬁle. Note that
this is a computational study for which all the data can be generated
using the code described below. Source data are provided with
this paper.

Code availability
The source code for the model proposed here and the respective
analyses are available at https://github.com/neuralml/neoSSL (https://
doi.org/10.5281/zenodo.15359568). For this implementation, PyTorch
2.2.2 was used (full list of dependencies at https://github.com/
neuralml/neoSSL/blob/main/environment.yml).