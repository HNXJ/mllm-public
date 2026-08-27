## Page 1

> Figure description (generated): Since no actual figure image was provided, I cannot provide a detailed description.

**Please upload the academic PDF figure you would like me to describe.**

Once you provide the image, I will generate a response adhering strictly to your requirements:

1. **Overall Layout & Structure**: Detailed description of the figure's organization (panels, schematic type).
2. **Visual Components & Symbols**: Exhaustive breakdown of all shapes, connections, and directional flow.
3. **Labels, Keys & Legends**: Transcription of all visible text, variables, and annotations within the figure.
4. **Data Trends & Details**: Specific analysis of any graphs (axes, trends).
5. **Contextual Caption Integration**: Explanation linking visual elements to the provided context (if a caption were available).

I am ready to act as your senior neuroscientist and technical editor.

Articles

https://doi.org/10.1038/s41593-021-00857-x

1Department of Cellular and Molecular Medicine, University of Ottawa, Ottawa, ON, Canada. 2Ottawa Brain and Mind Institute, University of Ottawa, 
Ottawa, ON, Canada. 3Centre for Neural Dynamics, University of Ottawa, Ottawa, ON, Canada. 4Department of Biological Sciences, University of Toronto 
Scarborough, Toronto, ON, Canada. 5Department of Cell and Systems Biology, University of Toronto, Toronto, ON, Canada. 6Friedrich Miescher Institute 
for Biomedical Research, Basel, Switzerland. 7Mila, Montréal, QC, Canada. 8Department of Neurology and Neurosurgery, McGill University, Montréal, 
QC, Canada. 9School of Computer Science, McGill University, Montréal, QC, Canada. 10Learning in Machines and Brains Program, Canadian Institute for 
Advanced Research, Toronto, ON, Canada. 11Department of Physics, University of Ottawa, Ottawa, ON, Canada. 12Present address: University of Montréal 
and Mila, Montréal, QC, Canada. 13These authors contributed equally: Alexandre Payeur, Jordan Guerguiev. 14These authors jointly supervised this work: 
Blake A. Richards, Richard Naud. ✉e-mail: blake.richards@mila.quebec; rnaud@uottawa.ca

T

he current canonical model of synaptic plasticity in the cortex 
is based on the co-occurrence of activity on the two sides of 
the synapse, pre- and postsynaptic1. The occurrence of either 
long-term depression (LTD) or long-term potentiation (LTP) is con-
trolled by specific features of pre- and postsynaptic activity2–9 and 
a more global state of neuromodulation10–12. However, local learn-
ing rules by themselves do not provide a guarantee that behavioral 
metrics will improve. With neuromodulation driven by an external 
reward/punishment mechanism, this guarantee is achievable13. But, 
such learning is very slow in tasks that require large or deep net-
works because a global signal provides very limited information to 
neurons deep in a hierarchy14,15. Thus, an outstanding question is 
(Fig. 1): how can neurons high-up in a hierarchy signal to other 
neurons—sometimes multiple synapses lower—whether to engage 
in LTP or LTD to improve behavior? This question is sometimes 
referred to as the ‘credit assignment problem’: essentially, how can 
we assign credit for any errors or successes to neurons that are mul-
tiple synapses away from the output16?

In machine learning, the credit assignment problem is typically 
solved with the backpropagation-of-error algorithm (backprop17), 
which explicitly uses gradient information in a biologically implau-
sible manner15 to calculate synaptic weight updates. Many previous 
studies have attempted to capture the credit assignment properties 
of backprop with more biologically plausible implementations in 
the hope that a biological model could match backprop’s learning 
performance15. However, a problem with most of these models is 
that there is always an implicit assumption that during some phases 
of learning no sensory stimuli are processed, that is, the models are 
not ‘online’ in their learning, which is problematic for both biologi-
cal plausibility and for potential future development of low-energy 
neuromorphic computing devices. Moreover, there are several

well-established properties of real neurons, including nonlinearities 
in the apical dendrites18, short-term synaptic plasticity (STP)19 and 
inhibitory microcircuits that are ignored. None of the previous stud-
ies successfully incorporated all of these features to perform online 
credit assignment (Supplementary Table 1). Furthermore, none of 
these models captured the frequency dependence of synaptic plas-
ticity, which is a very well-established property of LTP/LTD4,6,7,20,21.

As established in nonhierarchical systems, such as the electro-
sensory lateral line lobe of the electric fish22,23 or the cerebellum24, 
feedback connections on dendrites are well-poised to orchestrate 
learning. But for credit assignment in hierarchical networks, these 
connections should obey four constraints: (1) feedback must steer 
the sign and magnitude of plasticity. (2) Feedback signals from 
higher-order areas should be multiplexed with feedforward signals 
from lower-order areas so that credit information can percolate 
down the hierarchy with minimal disruption to sensory informa-
tion. (3) There should be some degree of alignment between feed-
back connections and feedforward connections. (4) Integration of 
credit-carrying feedback signals should be close to linear and avoid 
saturation (that is, feedback signals should be linear with respect 
to any credit information). Experimental and theoretical work have 
addressed steering9,25, multiplexing26–28, alignment15,29,30 or linearity31 
in isolation. But, it remains unclear whether a single set of cellular 
and subcellular mechanisms can address all four requirements for 
orchestrating learning in cortical hierarchies efficiently.

Here, we address the credit assignment problem with a 
spike-based learning rule that models how high-frequency bursts 
determine the sign of synaptic plasticity4,6,7,20,21. Guided by the under-
lying philosophy first espoused by the work of Körding and König32 
that the unique properties of pyramidal neurons may contain a 
solution to biologically plausible credit assignment, we show that

Burst-dependent synaptic plasticity can 
coordinate learning in hierarchical circuits

Alexandre Payeur   1,2,3,12,13, Jordan Guerguiev4,5,13, Friedemann Zenke   6, Blake A. Richards   7,8,9,10,14 ✉ 
and Richard Naud   1,2,3,11,14 ✉

Synaptic plasticity is believed to be a key physiological mechanism for learning. It is well established that it depends on pre- and 
postsynaptic activity. However, models that rely solely on pre- and postsynaptic activity for synaptic changes have, so far, not 
been able to account for learning complex tasks that demand credit assignment in hierarchical networks. Here we show that 
if synaptic plasticity is regulated by high-frequency bursts of spikes, then pyramidal neurons higher in a hierarchical circuit 
can coordinate the plasticity of lower-level connections. Using simulations and mathematical analyses, we demonstrate that, 
when paired with short-term synaptic dynamics, regenerative activity in the apical dendrites and synaptic plasticity in feedback 
pathways, a burst-dependent learning rule can solve challenging tasks that require deep network architectures. Our results 
demonstrate that well-known properties of dendrites, synapses and synaptic plasticity are sufficient to enable sophisticated 
learning in hierarchical circuits.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1010


---

## Page 2

Articles
NatUrE NEUrOScIEncE

combining properties of apical dendrites18 with our burst-dependent 
learning rule allows feedback to steer plasticity. We further show 
that feedback information can be multiplexed across multiple lev-
els of a hierarchy when feedforward and feedback connections 
have distinct STP33,34. Using spiking simulations, we demonstrate 
that these mechanisms can be used to coordinate learning across 
a hierarchical circuit in a fully online manner. We also show that 
a coarse-grained equivalent of these dynamical properties will, on 
average, lead to learning that approximates loss-function gradients 
as used in backprop. We further show that this biological approxi-
mation to loss-function gradients is improved by a burst-dependent 
learning rule performing the alignment of feedback weights with 
feedforward weights, as well as recurrent connections that linear-
ize credit signals. Finally, we show that networks trained with these 
mechanisms can learn to classify complex image patterns with high 
accuracy. Altogether, our work highlights that well-known proper-
ties of dendritic excitability, synaptic transmission, STP, inhibitory 
microcircuits and burst-dependent synaptic plasticity are sufficient 
to solve the credit assignment problem in hierarchical networks.

Results
A burst-dependent rule enables top-down steering of plasticity. 
Experimental work has demonstrated that the sign of plasticity can 
be determined by patterns of pre- and postsynaptic activity. The 
most common formulation of this is spike-timing-dependent plas-
ticity (STDP), wherein the timing of pairs of pre- and postsynaptic 
spikes is what determines whether LTP or LTD occurs3. However, 
there is also evidence suggesting that in many circuits, particularly 
mature ones35, the principal determinant of plasticity is the level of 
postsynaptic depolarization, with large depolarization leading to 
LTP and small depolarization leading to LTD2,4,5, which is a direct 
consequence of the dynamics of NMDA receptor-dependent cal-
cium influx36. One of the easiest ways to induce large magnitude 
depolarization in dendrites is via high-frequency bursts of back-
propagating action potentials37 and, therefore, the degree of post-
synaptic bursting controls plasticity4–7,21. Since bursting may be 
modulated by feedback synapses on apical dendrites18,38, feedback 
could control plasticity in the basal dendrites via control of bursting. 
Thus, in considering potential mechanisms for credit assignment 
during top-down supervised learning, the burst-dependence of syn-
aptic plasticity appears to be a natural starting point.

To explore how high-frequency bursting could control learning in 
biological neural networks, we formulated a burst-dependent plas-
ticity rule as an abstraction of the experimental data. We consider

a burst to be any occurrence of at least two spikes with a short inter-
spike interval. Following ref. 28, we further define an event as either 
an isolated single spike or a burst. The learning rule states that the 
change over time (t) of a synaptic weight between postsynaptic neu-
ron i and presynaptic neuron j, dwij/dt, results from a combination 
of an eligibility trace of presynaptic activity, Ej, and the potentiating 
(or depressing) effect of bursts Bi(t) (or events Ei(t)) of the postsyn-
aptic cell (Fig. 2a and Methods):

dwij

dt
= η[Bi(t) −Pi(t)Ei(t)]Ej(t).
(1)

The constant η is the learning rate. The variable Pi ∈[0, 1] is an 
exponential moving average of the proportion of events that are 
bursts in postsynaptic neuron i, with a slow (τavg ≈ 1−10 s) time 
constant (Methods). When a postsynaptic event that is not a burst 
occurs, the weight decreases proportionally to −Pi(t)Ej(t) < 0. In 
contrast, if a postsynaptic event is a burst, then the weight increases 
proportionally to [1 −Pi(t)]Ej(t) > 0. Hence, this moving average 
regulates the relative strength of burst-triggered potentiation and 
event-triggered depression. It has been well established that such 
mechanisms exist in real neurons39.

The plasticity rule stipulates that when a presynaptic input 
is paired with a postsynaptic burst LTP is induced, whereas with 
an isolated spike, LTD results (Fig. 2a)6,7,20,21,35,36. Using this rule, 
we simulated a series of synaptic plasticity experiments from the 
experimental and computational literature. First, we examined 
a frequency-dependent STDP protocol5. We found that when the 
spike pairing frequency is low, LTD is produced, and when the 
pairing frequency is high, LTP is produced (Fig. 2b). This matches 
previous reports on frequency-dependent STDP and shows that 
a burst-dependent synaptic plasticity rule can explain these data. 
Then, we explored the behavior of our rule when the pre- and post-
synaptic neuron fire independently according to Poisson statistics 
(Fig. 2c). Experimental results have established that in such a situa-
tion the postsynaptic firing rate should determine the sign of plas-
ticity5. We found that a burst-dependent plasticity rule produces 
exactly this behavior (Fig. 2c), but with a dependence on bursting 
history not typically explored. Notably, contrary to the Bienenstock–
Cooper–Munro model40 where the switching point between LTD 
and LTP depends on a nonlinear moving average of the feedforward 
activity, in the present case, the adaptive threshold is a burst prob-
ability, which can be controlled independently of the feedforward 
activity. These results demonstrate that a burst-dependent plastic-
ity rule is capable of linking a series of known experimental and 
theoretical results.

The burst-dependent rule suggests that feedback-mediated 
steering of plasticity could be achieved if there were a mechanism 
for top-down control of the likelihood of a postsynaptic burst. To 
illustrate this, in Fig. 2d we simulated another protocol wherein 
events were generated with Poisson statistics, and each event could 
become a burst with probability P (x axis in Fig. 2d). Manipulating 
this burst probability against the initial burst probability estimate 
(Pi(0) = 20%) controlled the occurrence of LTP and LTD, while 
changing the pre- and postsynaptic event rates simply modified the 
rate of change of the weight (but not the transition point between 
LTP and LTD). This shows that one way for neurons to control the 
sign of plasticity to ensure effective learning may be to regulate the 
probability of high-frequency bursts. Evidence indicates that in 
pyramidal neurons of sensory cortices the probability of generat-
ing high-frequency bursts is controlled by inputs to the distal api-
cal dendrites and their activation of voltage-gated calcium channels 
(VGCCs)18,41. Anatomical and functional data have shown that these 
inputs often come from higher-order cortical or thalamic regions42.

We wondered whether combining a burst-dependent plastic-
ity rule with regenerative activity in apical dendrites could permit

Higher-order
area

Lower-order
area

a
b

Top-down

Bottom-up

LTD?
LTP?
Synapse

Fig. 1 | The credit assignment problem for hierarchical networks. 
a, Illustration of a hierarchical neural network with feedforward and 
feedback connections. b, For an orchestration of learning in this network, 
the representations in higher-level neurons should steer the plasticity of 
connections at a lower level.

> Figure caption (from PDF text): Fig. 1 | The credit assignment problem for hierarchical networks. 
a, Illustration of a hierarchical neural network with feedforward and 
feedback connections. b, For an orchestration of learning in this network, 
the representations in higher-level neurons should steer the plasticity of 
connections at a lower level.
> Figure description (generated): ## Figure Description: The Credit Assignment Problem for Hierarchical Networks

This figure, labeled as Fig. 1, illustrates the concept of credit assignment within a hierarchical neural network structure, divided into two main panels: (a) and (b).

### 1. Overall Layout & Structure
The figure is composed of two distinct panels, **(a)** and **(b)**. Panel (a) presents a broad schematic of the entire hierarchical network architecture, while Panel (b) provides a magnified, detailed view focusing on the interaction between higher and lower-level neurons at a single synaptic connection.

### 2. Visual Components & Symbols

#### Panel (a): Hierarchical Network Schematic
*   **Structure:** This panel depicts a multi-layered network structure. Neurons are represented by stylized shapes:
    *   **Blue/Cyan Triangles (Top Layers):** Represent neurons in higher layers.
    *   **Green/Teal Triangles (Middle Layers):** Represent neurons in intermediate layers.
    *   **Black Triangles (Bottom Layers):** Represent neurons in the lowest layer/input or output.
*   **Connections:** Lines represent synaptic connections between neurons across different layers.
    *   **Feedforward Connections (Downward Flow):** Lines connect higher-level neurons to lower-level neurons, indicating information flow from top to bottom.
    *   **Feedback Connections (Upward Flow):** Lines connect lower-level neurons back up to higher-level neurons, indicating recurrent or feedback pathways.
*   **Overall Flow:** The structure suggests a deep network where information flows both forward (feedforward) and backward (feedback).

#### Panel (b): Synaptic Plasticity Detail
*   **Magnification:** This panel is a zoomed-in view of the interaction occurring at a single synapse, as indicated by the bracket connecting it to Panel (a).
*   **Components:**
    *   **Higher-Level Neuron (Top):** Represented by a cyan/light blue triangle, positioned at the top.
    *   **Lower-Level Neuron (Bottom):** Represented by a dark green triangle, positioned below the higher neuron.
    *   **Synapse:** The connection point between the two neurons is explicitly labeled "Synapse."
*   **Flow and Influence:**
    *   **Top-down Flow:** A light blue arrow originates from the higher-level neuron and points down toward the synapse, labeled **"Top-down."** This indicates influence or control originating from the higher level.
    *   **Bottom-up Flow:** Multiple dark arrows originate from the lower-level neuron and point upward toward the synapse, labeled **"Bottom-up."** This indicates information or influence flowing from the lower level.
*   **Plasticity Indicators:** Next to the synapse, there are two dashed boxes indicating potential outcomes of learning:
    *   **LTP?:** Labeled "LTP?" (Long-Term Potentiation?), suggesting a potential strengthening of the connection.
    *   **LTD?:** Labeled "LTD?" (Long-Term Depression?), suggesting a potential weakening of the connection.

### 3. Labels, Keys & Legends
*   **Panel Titles:** The panels are labeled **"a"** and **"b"**.
*   **Key Annotations in Panel (b):**
    *   "Top-down"
    *   "Bottom-up"
    *   "Synapse"
    *   "LTP?" and "LTD?"

### 4. Contextual Caption Integration
The provided caption clarifies the function of these elements:
*   **Panel (a):** Is described as an "Illustration of a hierarchical neural network with feedforward and feedback connections."
*   **Panel (b):** Is described as illustrating "For an orchestration of learning in this network, the representations in higher-level neurons should steer the plasticity of connections at a lower level." This confirms that the "Top-down" influence dictates how the synaptic plasticity (LTP/LTD) is managed based on higher-level representations.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1011


---

## Page 3

Articles
NatUrE NEUrOScIEncE

top-down signals to act as a ‘teaching signal’, instructing the sign of 
plasticity in a neuron. To explore this, we ran simulations of pyra-
midal neuron models with simplified VGCC kinetics in the api-
cal dendrites (Methods). We found that by manipulating the distal 
inputs to the apical dendrites we could control the number of events 
and bursts in the neurons independently (Fig. 2e,g). The inputs to 
the apical dendrites in the postsynaptic neurons were what regulated 
the number of bursts, and this also controlled changes in the synaptic 
weights, through the burst-dependent learning rule. When the rela-
tive proportion of bursts increased, the synaptic weights potentiated 
on average, and when the relative proportion of bursts decreased, 
the synaptic weights depressed (Fig. 2f). Thus, in Fig. 2f, the weight 
increases (decreases) on average when P −P is positive (negative). 
Modifying the proportion of bursts in the presynaptic neurons had 
little effect on the weights (see the rightmost gray shaded area in Fig. 
2e–g). The sign of plasticity was independent of the number of events, 
although the magnitude was not. Therefore, while the number of 
events contributed to the determination of the magnitude of changes, 
the top-down inputs to the apical dendrites controlled the sign of plas-
ticity. In this way, the top-down inputs acted as a ‘teaching signal’ that 
determined whether LTP or LTD would occur. These results show 
that a burst-dependent learning rule paired with the control of burst-
ing provided by apical dendrites enables a form of top-down steering 
of synaptic plasticity in an online, local and spike-based manner.

Dendrite-dependent bursting combined with short-term plastic-
ity supports multiplexing of feedforward and feedback signals. 
The question that naturally arises from our finding that top-down 
inputs can steer synaptic plasticity via a burst-dependent rule is 
whether feedback can steer plasticity without affecting the com-
munication of bottom-up signals? Using numerical simulations, we 
previously have demonstrated that in an ensemble of pyramidal neu-
rons the inputs to the perisomatic and distal apical dendritic regions 
can be distinctly encoded using the event rate computed across the 
ensemble of cells and the percentage of events in the ensemble 
that are bursts (the ‘burst probability’), respectively28. When com-
municated by synapses with either short-term facilitation (STF) or 
short-term depression (STD), this form of ‘ensemble multiplexing’ 
may allow top-down and bottom-up signals to be simultaneously 
transmitted through a hierarchy of pyramidal neurons.

To explore this possibility, we conducted simulations of two 
reciprocally connected ensembles of pyramidal neurons along 
with interneurons providing feedforward inhibition. One ensem-
ble received currents in the perisomatic regions and projected 
to the perisomatic regions of the other ensemble (Fig. 3a, green 
ensemble). The other ensemble (Fig. 3a, light blue) received cur-
rents in the distal apical compartments and projected to the distal 
apical compartments of the first ensemble. As such, we considered 
the first ensemble to be ‘lower’ (receiving and communicating

Learning rule

1
100
Pairing frequency (Hz)

–0.3

0

0.3

ΔW

Periodic protocol

1
50
Rate (Hz)

–2.5

0

2.5

5.0

ΔW

Poisson protocol

P(0) = 30%

P(0) = 50%

0
50
Burst probability (%)

0

2

ΔW

Burst–Poisson protocol

ER = 5 Hz
ER = 10 Hz

Strong

distal

Weak

distal

Presynaptic

perturb.
a
b

c
d

Pre

Post

Pre

Post

e

f

g

Presynaptic

perturb.

Distal input

Pre

Post

LTP

LTD

Ctrl
Postinduction

Pre

Post

Pre

Post

0

5

Postsynaptic ER (Hz)

0

50

Postsynaptic BP (%)

P

> Figure description (generated): This figure presents a single plot illustrating a "Periodic protocol."

**1. Overall Layout & Structure:**
The figure consists of a single two-dimensional line graph plotted against an x-axis and a y-axis.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Curves/Lines:** There are two primary visual elements: a continuous, smooth curve representing the main function being plotted, and several vertical lines indicating specific time points or phases.
*   **Annotations:** Several text labels are positioned near the top of the plot area, and dashed lines mark specific values on the y-axis.

**3. Labels, Keys & Legends:**
*   **Title:** The title above the plot reads: "Periodic protocol".
*   **Y-Axis Label:** The y-axis is numbered with values: 0, 3.
*   **X-Axis Label:** The x-axis is numbered with values: 1, 100.
*   **Y-Axis Annotations:** The y-axis has tick marks and labels indicating values 0 and 3.
*   **Protocol Phase Labels:** Near the top left, there are labels indicating phases: "Post" and "Pre".
*   **Dashed Line:** A horizontal dashed line is present at $y=0$.

**4. Data Trends & Details:**
*   **The Curve:** The main curve exhibits a distinct sigmoidal or step-like transition.
    *   **Initial Phase (Left):** Starting from the left side of the plot (around $x=1$), the curve is decreasing, starting near a value of 3 and sloping downwards.
    *   **Transition Phase (Middle):** The curve remains low until a certain point, then undergoes a rapid, steep increase.
    *   **Final Phase (Right):** After the sharp transition, the curve continues to increase, leveling off towards a value approaching 3 as $x$ approaches 100.
*   **Vertical Lines (Protocol Markers):** There are five distinct, thin vertical lines positioned above the plot area. These lines appear to be associated with the "Post" and "Pre" labels, suggesting discrete events or time windows within the protocol.

**5. Contextual Caption Integration:**
The labels "Post" and "Pre," along with the vertical lines, indicate that the protocol involves distinct phases or periods. The curve itself likely represents a measured variable (e.g., neural activity, concentration) changing over time or some experimental parameter represented by the x-axis. The transition around $y=0$ suggests a critical threshold or switching point within the periodic protocol.

> Figure description (generated): This figure is composed of two distinct schematic panels, labeled implicitly by the large text headers above each panel: "LTP" (Long-Term Potentiation) and "LTD" (Long-Term Depression). Both panels depict a simplified representation of synaptic plasticity, likely involving pre- and post-synaptic neurons.

### Overall Layout & Structure
The figure is divided vertically into two main sections: the top section illustrating LTP, and the bottom section illustrating LTD. Each panel uses a schematic diagram style to represent synaptic connections between two neuronal elements, labeled "Post" (postsynaptic) and "Pre" (presynaptic).

### Visual Components & Symbols

**General Elements:**
*   **Neuronal Representations:** Both the pre- and postsynaptic elements are represented by stylized, inverted triangle shapes.
    *   The **Presynaptic Neuron (Pre)** is colored dark green/teal.
    *   The **Postsynaptic Neuron (Post)** is colored light blue/cyan.
*   **Synaptic Connection:** A vertical line connects the base of the pre-synaptic triangle to the top of the post-synaptic triangle, representing the synapse.
*   **Activity/Plasticity Representation:** Above each synaptic connection, there is a small plot showing the change in synaptic strength or activity. This plot consists of two lines:
    *   A **dashed line ($\text{---}$)**, representing the "Ctrl" (Control) condition.
    *   A **solid line ($\text{---}$)**, representing the "Postinduction" condition.

**Panel Specifics:**

**1. LTP Panel (Top):**
*   This panel shows the synaptic connection structure for Long-Term Potentiation.
*   The schematic elements (Pre and Post neurons) are present as described above.
*   The associated plot shows the solid line (Postinduction) exhibiting a higher baseline or greater magnitude compared to the dashed line (Ctrl), indicating potentiation.

**2. LTD Panel (Bottom):**
*   This panel shows the synaptic connection structure for Long-Term Depression.
*   The schematic elements (Pre and Post neurons) are present as described above.
*   The associated plot shows the solid line (Postinduction) exhibiting a lower baseline or reduced magnitude compared to the dashed line (Ctrl), indicating depression.

### Labels, Keys & Legends
*   **Panel Headers:** The top of the LTP panel is labeled **"LTP"**, and the top of the LTD panel is labeled **"LTD"**.
*   **Neuronal Labels:** Within each schematic, the top neuron is labeled **"Post"** and the bottom neuron is labeled **"Pre"**.
*   **Legend:** A legend is provided below the two panels:
    *   **"--- Ctrl"**: Indicates the control condition, represented by a dashed line.
    *   **"--- Postinduction"**: Indicates the condition following induction, represented by a solid line.

### Data Trends & Details
The plots above the synaptic connections illustrate the change in synaptic efficacy:

*   **LTP Panel:** The solid line (Postinduction) is visibly higher than the dashed line (Ctrl), suggesting an increase in synaptic strength.
*   **LTD Panel:** The solid line (Postinduction) is visibly lower than the dashed line (Ctrl), suggesting a decrease in synaptic strength.

The plots are abstract representations of change, lacking explicit axes labels (e.g., $\Delta$ weight or time), but the relative positioning of the curves clearly demonstrates the difference between potentiation and depression.

–10

0

10

(%)

Weight change
Postsynaptic BP–P

0
20
45
70
95
120
145
170
Time (s)

0

5

Presynaptic ER (Hz)

0

50

Presynaptic BP (%)

Fig. 2 | Burst-dependent plasticity rule. a, Schematics of the learning rule. When there is a presynaptic eligibility trace, the occurrence of a postsynaptic 
burst leads to potentiation (top) whereas an isolated postsynaptic spike leads to depression of the synapse (bottom). Ctrl, control. b–d, Net weight 
change for different pairing protocols. b, The periodic protocol consisted of 15 sequences of five pairings, separated by a 10 s interval. We used pairings 
with tpost = tpre. c, For the Poisson protocol, the pre- and postsynaptic activities were Poisson spike trains with equal rates. The protocol was repeated 
with different initial time-averaged burst probabilities (P). d, For the Burst–Poisson protocol, pre- and postsynaptic Poisson events were generated at 
a fixed rate (ER). For each event, a burst was produced with a probability that varied from 0 to 50%. e–g, Impact of distal inputs on burst probability 
and feedforward synaptic weights for constant presynaptic event rate. Positive distal input (45–70 s) increases burst probability (e) and strengthens 
feedforward synapses (f). Negative distal input (95–120 s) decreases burst probability and weakens synapses. A dendritic input to the presynaptic neuron 
(145–170 s) increases its burst probability and mildly affects its event rate (g), but does not notably change the weights (f). e, Event rate (ER, blue), burst 
probability (BP, solid red curve) and moving average of the BP (dashed red curve) for the postsynaptic population. The black dotted line indicates the 
prestimulation ER and serves as a reference for the variations of the ER with plasticity. f, Weight change relative to the initial average value of the weights. 
g, Same as e, but for the presynaptic population. For the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) 
population represent Poisson input noise; such noise is absent for the postsynaptic (light blue) population for this simulation. For e–g, the time constants 
and segment durations were selected to get a clear illustration of the learning rule. In all relevant panels, results are displayed as mean ± s.d. over 20 
realizations of the noise. Perturb., perturbation.

> Figure caption (from PDF text): Fig. 2 | Burst-dependent plasticity rule. a, Schematics of the learning rule. When there is a presynaptic eligibility trace, the occurrence of a postsynaptic 
burst leads to potentiation (top) whereas an isolated postsynaptic spike leads to depression of the synapse (bottom). Ctrl, control. b–d, Net weight 
change for different pairing protocols. b, The periodic protocol consisted of 15 sequences of five pairings, separated by a 10 s interval. We used pairings 
with tpost = tpre. c, For the Poisson protocol, the pre- and postsynaptic activities were Poisson spike trains with equal rates. The protocol was repeated 
with different initial time-averaged burst probabilities (P). d, For the Burst–Poisson protocol, pre- and postsynaptic Poisson events were generated at 
a fixed rate (ER). For each event, a burst was produced with a probability that varied from 0 to 50%. e–g, Impact of distal inputs on burst probability 
and feedforward synaptic weights for constant presynaptic event rate. Positive distal input (45–70 s) increases burst probability (e) and strengthens 
feedforward synapses (f). Negative distal input (95–120 s) decreases burst probability and weakens synapses. A dendritic input to the presynaptic neuron 
(145–170 s) increases its burst probability and mildly affects its event rate (g), but does not notably change the weights (f). e, Event rate (ER, blue), burst 
probability (BP, solid red curve) and moving average of the BP (dashed red curve) for the postsynaptic population. The black dotted line indicates the 
prestimulation ER and serves as a reference for the variations of the ER with plasticity. f, Weight change relative to the initial average value of the weights. 
g, Same as e, but for the presynaptic population. For the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) 
population represent Poisson input noise; such noise is absent for the postsynaptic (light blue) population for this simulation. For e–g, the time constants 
and segment durations were selected to get a clear illustration of the learning rule. In all relevant panels, results are displayed as mean ± s.d. over 20 
realizations of the noise. Perturb., perturbation.
> Figure description (generated): This figure, titled "Poisson protocol," presents a time-course plot illustrating synaptic weight change under different initial burst probability conditions.

**1. Overall Layout & Structure:**
The figure consists of a single, large plot area displaying time-dependent changes. The structure is dominated by two overlaid line graphs representing weight change, set against a time axis (x-axis) and a normalized value axis (y-axis). Above the main plot, there are schematic representations of presynaptic and postsynaptic activity patterns.

**2. Visual Components & Symbols:**
*   **Time Axis (X-axis):** The x-axis spans from a value of '1' to '50', likely representing time units, with tick marks at 1 and 50.
*   **Value Axis (Y-axis):** The y-axis ranges from approximately -5 to 0, representing the change in synaptic weight.
*   **Activity Schematics (Top):** Above the main plot, there are two rows of vertical blue lines representing activity:
    *   The top row is labeled "Post" and shows a series of short, distinct vertical blue lines (representing postsynaptic spikes/bursts).
    *   The bottom row is labeled "Pre" and shows a series of vertical green lines (representing presynaptic spikes).
*   **Data Curves:** Two shaded, thick curves track the weight change over time:
    *   A **black line** represents one condition.
    *   A **gray shaded area/line** represents a second condition, with the central line within the shading representing the mean.
*   **Reference Line:** A horizontal dashed black line is present near $y=0$, serving as a baseline reference.

**3. Labels, Keys & Legends:**
*   **Title:** "Poisson protocol"
*   **Y-axis Label (Implicit):** The y-axis represents the change in synaptic weight, indicated by the numerical scale (-5 to 0).
*   **X-axis Label (Implicit):** The x-axis represents time, scaled from 1 to 50.
*   **Legend:** A legend in the bottom right corner specifies the conditions:
    *   $\bar{P}(0) = 30\%$ (associated with the black line/curve).
    *   $\bar{P}(0) = 50\%$ (associated with the gray shaded area/curve).

**4. Data Trends & Details:**
*   **$\bar{P}(0) = 30\%$ (Black Line):** This curve starts near $y=0$ at time $t=1$. It dips slightly below zero, reaches a minimum around $y \approx -2$ before time $t=10$, and then shows a steady, accelerating upward trend, crossing the zero line around $t=30$ and rising significantly towards positive values by $t=50$.
*   **$\bar{P}(0) = 50\%$ (Gray Shaded Area):** This curve starts significantly lower than the black line, around $y \approx -2$ at time $t=1$. It remains in the negative range for a longer period, showing a slower initial rise compared to the black line. The mean of this curve appears to cross the zero line later than the black line, and by $t=50$, it is slightly below the black curve's final value.

**5. Contextual Caption Integration:**
The caption identifies this panel as relating to the "Poisson protocol" (Panel c in the full context, though not explicitly labeled here). It specifies that for this protocol, "the pre- and postsynaptic activities were Poisson spike trains with equal rates." The legend $\bar{P}(0)$ refers to the "initial time-averaged burst probabilities (P)," indicating that the plot shows how synaptic weight change evolves based on whether the initial probability of a burst ($\bar{P}(0)$) was 30% or 50%.

> Figure caption (from PDF text): Fig. 2 | Burst-dependent plasticity rule. a, Schematics of the learning rule. When there is a presynaptic eligibility trace, the occurrence of a postsynaptic 
burst leads to potentiation (top) whereas an isolated postsynaptic spike leads to depression of the synapse (bottom). Ctrl, control. b–d, Net weight 
change for different pairing protocols. b, The periodic protocol consisted of 15 sequences of five pairings, separated by a 10 s interval. We used pairings 
with tpost = tpre. c, For the Poisson protocol, the pre- and postsynaptic activities were Poisson spike trains with equal rates. The protocol was repeated 
with different initial time-averaged burst probabilities (P). d, For the Burst–Poisson protocol, pre- and postsynaptic Poisson events were generated at 
a fixed rate (ER). For each event, a burst was produced with a probability that varied from 0 to 50%. e–g, Impact of distal inputs on burst probability 
and feedforward synaptic weights for constant presynaptic event rate. Positive distal input (45–70 s) increases burst probability (e) and strengthens 
feedforward synapses (f). Negative distal input (95–120 s) decreases burst probability and weakens synapses. A dendritic input to the presynaptic neuron 
(145–170 s) increases its burst probability and mildly affects its event rate (g), but does not notably change the weights (f). e, Event rate (ER, blue), burst 
probability (BP, solid red curve) and moving average of the BP (dashed red curve) for the postsynaptic population. The black dotted line indicates the 
prestimulation ER and serves as a reference for the variations of the ER with plasticity. f, Weight change relative to the initial average value of the weights. 
g, Same as e, but for the presynaptic population. For the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) 
population represent Poisson input noise; such noise is absent for the postsynaptic (light blue) population for this simulation. For e–g, the time constants 
and segment durations were selected to get a clear illustration of the learning rule. In all relevant panels, results are displayed as mean ± s.d. over 20 
realizations of the noise. Perturb., perturbation.
> Figure description (generated): This figure, titled "Burst–Poisson protocol," presents a graph illustrating the change in synaptic weight under different experimental conditions.

**Overall Layout & Structure:**
The figure consists primarily of a single line graph, which plots synaptic weight change over time. Above the main plot area, there is a schematic diagram illustrating the learning rule associated with this protocol.

**Visual Components & Symbols:**
1. **Schematic (Top):** This section depicts a simplified representation of neural activity:
    *   "Post" (Postsynaptic) is indicated by a row of vertical blue lines.
    *   "Pre" (Presynaptic) is indicated by a row of vertical green lines.
    *   The schematic shows the relationship between these inputs, suggesting a temporal coincidence or pairing mechanism.

2. **Main Plot (Bottom):** This is a time-series plot showing the evolution of synaptic weight change.
    *   The **x-axis** represents time, ranging from 0 to 50 (units are not explicitly labeled on the axis but contextually relate to time).
    *   The **y-axis** represents the synaptic weight change, ranging from approximately -0.5 to 2.5 (with major ticks at 0 and 2).
    *   There are two primary data curves plotted:
        *   A **black line** representing the condition "ER = 5 Hz."
        *   A **gray shaded area/line** representing the condition "ER = 10 Hz." The gray shading likely indicates variability (e.g., standard deviation).

**Labels, Keys & Legends:**
*   **Title:** "Burst–Poisson protocol"
*   **Y-axis Label (Implied):** Synaptic Weight Change (based on caption context, this is likely the weight change relative to an initial value).
*   **X-axis Label (Implied):** Time.
*   **Legend:**
    *   "ER = 5 Hz" (associated with the black line).
    *   "ER = 10 Hz" (associated with the gray shaded area/line).

**Data Trends & Details:**
*   **ER = 5 Hz (Black Line):** This curve starts near a negative value (around -0.2) and shows a gradual, steady increase over the plotted time course, ending slightly above 0.
*   **ER = 10 Hz (Gray Shaded Area):** This curve starts at a lower negative value than the 5 Hz condition. It exhibits a steeper initial rise compared to the 5 Hz curve, and the overall trend shows a stronger positive trajectory, ending at a higher value than the 5 Hz curve (approaching or exceeding 2.0). The gray shading indicates variability around the mean trend for this condition.

**Contextual Caption Integration:**
The caption identifies this figure as relating to the "Burst-dependent plasticity rule." Specifically, panel (d) in the caption refers to the "Burst–Poisson protocol," which is what this figure illustrates. The legend indicates that the curves represent the weight change for different fixed event rates (ER) of Poisson events. The caption further clarifies that this protocol involves generating pre- and postsynaptic Poisson events at a fixed rate (ER), where a burst is produced with a probability that varies.

> Figure caption (from PDF text): Fig. 2 | Burst-dependent plasticity rule. a, Schematics of the learning rule. When there is a presynaptic eligibility trace, the occurrence of a postsynaptic 
burst leads to potentiation (top) whereas an isolated postsynaptic spike leads to depression of the synapse (bottom). Ctrl, control. b–d, Net weight 
change for different pairing protocols. b, The periodic protocol consisted of 15 sequences of five pairings, separated by a 10 s interval. We used pairings 
with tpost = tpre. c, For the Poisson protocol, the pre- and postsynaptic activities were Poisson spike trains with equal rates. The protocol was repeated 
with different initial time-averaged burst probabilities (P). d, For the Burst–Poisson protocol, pre- and postsynaptic Poisson events were generated at 
a fixed rate (ER). For each event, a burst was produced with a probability that varied from 0 to 50%. e–g, Impact of distal inputs on burst probability 
and feedforward synaptic weights for constant presynaptic event rate. Positive distal input (45–70 s) increases burst probability (e) and strengthens 
feedforward synapses (f). Negative distal input (95–120 s) decreases burst probability and weakens synapses. A dendritic input to the presynaptic neuron 
(145–170 s) increases its burst probability and mildly affects its event rate (g), but does not notably change the weights (f). e, Event rate (ER, blue), burst 
probability (BP, solid red curve) and moving average of the BP (dashed red curve) for the postsynaptic population. The black dotted line indicates the 
prestimulation ER and serves as a reference for the variations of the ER with plasticity. f, Weight change relative to the initial average value of the weights. 
g, Same as e, but for the presynaptic population. For the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) 
population represent Poisson input noise; such noise is absent for the postsynaptic (light blue) population for this simulation. For e–g, the time constants 
and segment durations were selected to get a clear illustration of the learning rule. In all relevant panels, results are displayed as mean ± s.d. over 20 
realizations of the noise. Perturb., perturbation.
> Figure description (generated): This figure, labeled "Fig. 2," presents a multi-panel visualization illustrating a burst-dependent plasticity rule, comparing different pairing protocols and the impact of distal inputs. The figure is composed of several distinct plots arranged vertically, with sub-panels (b through g) detailing specific experimental results.

### Overall Layout and Structure
The figure is structured as a series of time-series plots, primarily focusing on synaptic weight changes and population activity over time. The top section (Panel a) contains schematics, while the subsequent panels (b through g) are time-course graphs.

### Panel Descriptions and Data Details

**Panel a: Schematics of the learning rule.**
This panel contains schematic representations illustrating the plasticity mechanism. It shows two scenarios:
1. **Top Schematic:** Depicts a scenario where "When there is a presynaptic eligibility trace, the occurrence of a postsynaptic burst leads to potentiation." This schematic shows an input leading to a postsynaptic event (implied burst) resulting in synaptic strengthening.
2. **Bottom Schematic:** Depicts a scenario where "an isolated postsynaptic spike leads to depression of the synapse." This shows an input leading only to a postsynaptic event (implied isolated spike) resulting in synaptic weakening.

**Panel b: Net weight change for the periodic protocol.**
This is a time-series plot showing "Weight change relative to the initial average value of the weights."
*   **X-axis:** Time (ranging from 0 to approximately 170 units, likely seconds based on the caption).
*   **Y-axis:** Weight change (ranging from approximately -0.2 to 0.4).
*   **Curves:** Two lines are present: a solid red line and a dashed red line. The caption specifies that this protocol used pairings with $t_{post} = t_{pre}$.

**Panel c: Net weight change for the Poisson protocol.**
This is a time-series plot showing "Weight change relative to the initial average value of the weights."
*   **X-axis:** Time (ranging from 0 to approximately 170 units).
*   **Y-axis:** Weight change (ranging from approximately -0.2 to 0.4).
*   **Curves:** Two lines are present, similar in style to Panel b.

**Panel d: Net weight change for the Burst–Poisson protocol.**
This is a time-series plot showing "Weight change relative to the initial average value of the weights."
*   **X-axis:** Time (ranging from 0 to approximately 170 units).
*   **Y-axis:** Weight change (ranging from approximately -0.2 to 0.4).
*   **Curves:** Two lines are present, showing the weight change under this specific protocol.

**Panel e: Event rate (ER), burst probability (BP) and moving average of the BP for the postsynaptic population.**
This plot tracks activity in the postsynaptic population.
*   **X-axis:** Time (ranging from 0 to approximately 170 units).
*   **Y-axis:** A scale is present on the right side, ranging from 0 to 5.
*   **Curves:**
    *   **Event rate (ER, blue):** A solid blue line representing the event rate.
    *   **Burst probability (BP, solid red curve):** A solid red line representing the burst probability.
    *   **Moving average of BP (dashed red curve):** A dashed red line representing the moving average of the burst probability.
*   **Annotations:** A black dotted line is present, labeled as "The black dotted line indicates the prestimulation ER and serves as a reference for the variations of the ER with plasticity."

**Panel f: Weight change.**
This plot shows "Weight change relative to the initial average value of the weights."
*   **X-axis:** Time (ranging from 0 to approximately 170 units).
*   **Y-axis:** Weight change (ranging from approximately -0.2 to 0.4).
*   **Curves:** A single black line is shown, representing the weight change under a specific condition (likely related to the distal input described in the caption).

**Panel g: Same as e, but for the presynaptic population.**
This plot tracks activity in the presynaptic population.
*   **X-axis:** Time (ranging from 0 to approximately 170 units).
*   **Y-axis:** A scale is present on the right side, ranging from 0 to 5.
*   **Curves:** Similar to Panel e, it shows the Event rate (ER) and Burst probability (BP) for the presynaptic population.

### Contextual Annotations and Legend Details
*   **Distal Input Markers:** The caption references specific time windows corresponding to distal inputs:
    *   Positive distal input (45–70 s) is associated with increased burst probability and strengthened feedforward synapses.
    *   Negative distal input (95–120 s) is associated with decreased burst probability and weakened synapses.
    *   A dendritic input to the presynaptic neuron (145–170 s) is noted as increasing burst probability but mildly affecting the event rate.
*   **Noise Representation:** The caption notes that for the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) population represent Poisson input noise, which is absent for the postsynaptic (light blue) population in this simulation.
*   **Statistical Notation:** Results are displayed as mean $\pm$ s.d. over 20 realizations of the noise in all relevant panels.

> Figure caption (from PDF text): Fig. 2 | Burst-dependent plasticity rule. a, Schematics of the learning rule. When there is a presynaptic eligibility trace, the occurrence of a postsynaptic 
burst leads to potentiation (top) whereas an isolated postsynaptic spike leads to depression of the synapse (bottom). Ctrl, control. b–d, Net weight 
change for different pairing protocols. b, The periodic protocol consisted of 15 sequences of five pairings, separated by a 10 s interval. We used pairings 
with tpost = tpre. c, For the Poisson protocol, the pre- and postsynaptic activities were Poisson spike trains with equal rates. The protocol was repeated 
with different initial time-averaged burst probabilities (P). d, For the Burst–Poisson protocol, pre- and postsynaptic Poisson events were generated at 
a fixed rate (ER). For each event, a burst was produced with a probability that varied from 0 to 50%. e–g, Impact of distal inputs on burst probability 
and feedforward synaptic weights for constant presynaptic event rate. Positive distal input (45–70 s) increases burst probability (e) and strengthens 
feedforward synapses (f). Negative distal input (95–120 s) decreases burst probability and weakens synapses. A dendritic input to the presynaptic neuron 
(145–170 s) increases its burst probability and mildly affects its event rate (g), but does not notably change the weights (f). e, Event rate (ER, blue), burst 
probability (BP, solid red curve) and moving average of the BP (dashed red curve) for the postsynaptic population. The black dotted line indicates the 
prestimulation ER and serves as a reference for the variations of the ER with plasticity. f, Weight change relative to the initial average value of the weights. 
g, Same as e, but for the presynaptic population. For the schematic on the right-hand side, black and gray axonal terminals onto the presynaptic (green) 
population represent Poisson input noise; such noise is absent for the postsynaptic (light blue) population for this simulation. For e–g, the time constants 
and segment durations were selected to get a clear illustration of the learning rule. In all relevant panels, results are displayed as mean ± s.d. over 20 
realizations of the noise. Perturb., perturbation.
> Figure description (generated): This image appears to be a schematic illustrating a plasticity rule, likely related to synaptic learning in a neural network model. It is presented as a diagrammatic representation rather than a multi-panel plot, although the caption refers to multiple panels (a-g).

### 1. Overall Layout & Structure
The visible portion of the figure is a schematic diagram focusing on synaptic plasticity, specifically illustrating two scenarios: potentiation (top) and depression (bottom). The structure is a simplified neural circuit diagram showing presynaptic and postsynaptic elements interacting.

### 2. Visual Components & Symbols
*   **Nodes/Populations:** There are two primary populations represented: a **presynaptic population** (indicated by green elements) and a **postsynaptic population** (indicated by light blue/cyan elements).
*   **Synaptic Connections:** The interaction is shown via lines connecting the presynaptic and postsynaptic elements.
*   **Potentiation Scenario (Top):** A light blue, triangular node represents the postsynaptic population. An arrow curves down from this node towards a green element representing the presynaptic activity, suggesting influence or correlation.
*   **Depression Scenario (Bottom):** A similar structure is shown below, involving a green element and an implied postsynaptic response.
*   **Presynaptic Detail:** The central focus of the lower part of the diagram is a detailed representation of the presynaptic neuron/population. This includes:
    *   A central green rectangular block, likely representing the presynaptic neuron or its activity.
    *   Multiple black lines originating from this block, terminating in small black tick marks ($\text{I}$), representing synaptic inputs or activity traces.
    *   A red, downward-pointing arrow ($\downarrow$) is positioned above the central green block, labeled "Perturb." This indicates a perturbation or change applied to the presynaptic activity.
*   **Flow/Direction:** The overall structure suggests a dependency: Presynaptic BP ($\%$) influences the outcome, which is reflected in the postsynaptic response.

### 3. Labels, Keys & Legends
*   **Y-Axis Label (Partial):** The top left corner shows a partial label: "($\%$)" indicating percentage measurement.
*   **Main Label:** A prominent vertical label on the left reads: "Presynaptic BP ($\%$)" (where BP stands for Burst Probability, as per the caption).
*   **Annotations:** The term "Perturb." is visible near the presynaptic element, indicating a perturbation.

### 4. Data Trends & Details
Since this is a schematic and not a plot, there are no quantitative data trends visible in the main diagram area. The visual elements illustrate *rules* rather than measured outcomes.

### 5. Contextual Caption Integration
The caption identifies the schematic as illustrating the **"Burst-dependent plasticity rule."**

*   The top scenario (implied by the upward curve and light blue node) corresponds to **potentiation**: "When there is a presynaptic eligibility trace, the occurrence of a postsynaptic burst leads to potentiation (top)."
*   The bottom scenario corresponds to **depression**: "...whereas an isolated postsynaptic spike leads to depression of the synapse (bottom)."
*   The green elements represent the presynaptic population, and the light blue element represents the postsynaptic population.
*   The black dotted line mentioned in the caption (though not explicitly visible as a reference line in this cropped view) would serve as a baseline for the plasticity changes.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1012


---

## Page 4

Articles
NatUrE NEUrOScIEncE

bottom-up signals), and the other to be ‘higher’ (receiving and 
communicating top-down signals) in the hierarchy. Furthermore, 
we made one key assumption in these simulations. We assumed 
that the synapses and cells that targeted the perisomatic regions 
were short-term depressing, whereas those that targeted the dis-
tal apical dendrites were short-term facilitating19. In these simula-
tions, we observed that currents injected into the lower ensemble’s 
perisomatic compartments were reflected in the event rate of these 
neurons (Fig. 3c(iii)), although with a slight phase lead due to spike 
frequency adaptation. In contrast, the currents injected into the 
distal apical dendrites of the higher ensemble were reflected in the 
burst probability of these neurons (Fig. 3b(ii)). However, we also 
observed that these signals were simultaneously propagated up and 
down. Specifically, the input to the lower ensemble’s perisomatic 
compartments was also encoded by the higher ensemble’s event 
rate (Fig. 3b(iii)), whereas the burst rate of the higher ensemble 
was encoded by the lower ensemble’s burst probability (Fig. 3c(ii)).

In this way, the lower ensemble had access to a conjunction of 
the signal transmitted to the higher ensemble’s distal apical den-
drites, as well as the higher ensemble’s event rate (see the arrow 
highlighting amplitude modulation in Fig. 3c(ii)). Thus, since the 
higher ensemble’s event rate is modulated by the lower ensemble’s 
event rate, the burst rate ultimately contains information about 
both the top-down and the bottom-up signals (Fig. 3d). Notably, 
this is important for credit assignment, as credit signals ideally are 
scaled by the degree to which a neuron is involved in processing 
a stimulus (this happens in backprop, for example). These simu-
lations demonstrate that if bottom-up connections to perisomatic 
regions and perisomatic inhibition rely on STD synapses, while 
top-down connections to apical dendrites and distal dendritic inhi-
bition use STF synapses, then ensembles of pyramidal neurons are 
capable of simultaneously processing both a top-down signal and 
a bottom-up signal using a combination of event rates, burst rates 
and burst probabilities.

1

25

Neuron

0

10

Rate (Hz)

1
2
3

Time (s)

1

25

Neuron

0

10

Rate (Hz)

0

50

Burst

probability (%)

Id (rescaled)

0

10

Rate (Hz)

Rescaled mean

0

50

Burst

probability (%)

Rescaled mean

1
2
3

Time (s)

0

10

Rate (Hz)

Is (rescaled)

(ii)

(iii)

(ii)

(iii)

b(i)

c(i)
STD
STF

STD

STF

Pop 1

Pop 2

Is

Id

Id

a

> Figure description (generated): This figure is composed of several distinct panels, combining a schematic diagram with multiple time-series plots.

### Overall Layout & Structure
The figure is structured into two main vertical sections: a schematic diagram on the left, and three sets of related plots (labeled (ii), (iii), etc.) arranged in a $2 \times 3$ grid structure, although the labeling suggests distinct groupings.

### Schematic Diagram (Left Side)
The left side features a schematic representation of a neural circuit:
1.  **Top Layer (Pop 2):** A layer labeled "Pop 2" is depicted as a collection of blue, rectangular neurons.
2.  **Middle Layer (STD):** Below Pop 2 is a layer labeled "STD" (likely representing a specific type of neuron or processing unit).
3.  **Bottom Layer (Pop 1):** At the bottom, there is a layer labeled "Pop 1," depicted as green, rectangular neurons.
4.  **Connections:** Arrows indicate connectivity:
    *   An arrow points from Pop 2 down to the STD layer.
    *   Arrows point from the STD layer down to Pop 1.
5.  **Feedback/Modulation:** There are additional elements indicating modulation:
    *   A small gray circle with a lightning bolt symbol is positioned near the STD layer, suggesting some form of input or modulation.
    *   A line connects this modulator to the STD layer, and another connection is shown from the STD layer towards Pop 1.
    *   The label "STF" is positioned near the connection between STD and Pop 1, suggesting a specific functional component or feedback loop.

### Plots (Right Side)
The right side contains multiple plots, organized into groups labeled with Roman numerals:

**Top Group (Likely related to Burst/Event Spikes):**
This section contains two plots stacked vertically, both sharing a common x-axis range (1 to 3).

*   **Top Plot:**
    *   **Y-axis Label:** "Burst probability (%)" (ranging from 0 to 50).
    *   **X-axis Label:** Unlabeled, but spans from 1 to 3.
    *   **Data Lines:** Two lines are present:
        *   A dashed black line labeled "$-I_d$ (rescaled)".
        *   A solid red line representing the data trend.
    *   **Trend:** Both lines show a cyclical pattern over the x-axis range, peaking around $x=1.5$ and $x=2.5$.

*   **Second Plot:**
    *   **Y-axis Label:** "Rate (Hz)" (ranging from 0 to 15).
    *   **X-axis Label:** Unlabeled, spanning from 1 to 3.
    *   **Data Lines:** Two lines are present:
        *   A solid blue line labeled "Rescaled mean".
        *   The plot shows a clear, high-frequency sinusoidal oscillation.

**Middle Group (Likely related to Burst/Event Spikes, different context):**
This section contains two plots stacked vertically.

*   **Third Plot:**
    *   **Y-axis Label:** "Burst probability (%)" (ranging from 0 to 50).
    *   **X-axis Label:** Unlabeled, spanning from 1 to 3.
    *   **Data Lines:** Two lines are present:
        *   A dashed black line labeled "$-I_s$ (rescaled)".
        *   A solid orange/brown line representing the data trend.
    *   **Trend:** This plot also shows a cyclical pattern, similar to the top plot.

*   **Fourth Plot:**
    *   **Y-axis Label:** "Rate (Hz)" (ranging from 0 to 15).
    *   **X-axis Label:** Unlabeled, spanning from 1 to 3.
    *   **Data Lines:** Two lines are present:
        *   A dashed black line labeled "$-I_s$ (rescaled)".
        *   A solid blue line representing the data trend.
    *   **Trend:** This plot shows a clear, lower-frequency sinusoidal oscillation compared to the second plot.

*(Note: The figure structure implies that panels (ii) and (iii) might refer to the grouping of these plots, although explicit panel labels are not present for every subplot.)*

Burst spike
Event spike

Pop 2

Pop 1

Event rate
Burst rate
Burst probability

Legend

d

Feedforward

Feedback

Is

Fig. 3 | Dendrite-dependent bursting combined with short-term plasticity supports the simultaneous propagation of bottom-up and top-down signals. 
a, Schematic of the network. Lower-level pyramidal neurons (pop 1, green) received a somatic current Is and projected with STD synapses to the somatic 
compartments of both a higher-level pyramidal neuron population (pop 2, light blue) and to a population providing disynaptic inhibition (gray disks). 
The dendritic compartments of the light blue population received a current Id. The light blue neurons innervated with STF synapses both the dendritic 
compartments of the green pyramidal neurons and a population providing disynaptic inhibition (gray squares). b(i),c(i), Raster plots of 25 of the 4,000 
neurons per pyramidal population for the light blue (b) and green (c) populations. Blue ticks show the start of an event, either a burst or an isolated spike. 
Orange ticks are the second spike in a burst; the remaining spikes in a burst are not shown. The corresponding population event rates (blue lines) and burst 
rates (orange lines) are superimposed. b(ii),(iii), Encoding performed by the light blue ensemble (pop 2). Its burst probability ((ii), dotted red line) reflects 
the applied dendritic current Id (dashed black line), whereas its event rate ((iii), dotted blue line) reflects the event rate of the green population (solid blue 
line). c(ii),(iii), Encoding performed by the green ensemble (pop 1). Its burst probability ((ii), solid red line) reflects the burst rate (dotted orange line) 
of the light blue ensemble, whereas its event rate ((iii), solid blue line) reflects the applied somatic current Is (dashed black line). Arrow highlights the 
amplitude modulation arising from the conjunction of top-down and bottom-up inputs. Results are displayed as mean ± 2 s.d. over five realizations of the 
Poisson noise applied to all neurons in the network. In each panel, the encoded input signal has been linearly rescaled so that its range matches that of the 
output. For clarity, the encoded signals in b(iii) and c(ii) are displayed using their averages only (that is, without the standard deviations). The bin size used 
in the population averages was 50 ms. The legend applies to b(i)–d inclusively. d, Schematic illustrating information propagation in the network.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1013


---

## Page 5

Articles
NatUrE NEUrOScIEncE

Combining a burst-dependent plasticity rule with short-term 
plasticity and apical dendrites can solve the credit assignment 
problem. To test whether STP, dendrite-dependent bursting and a 
burst-dependent learning rule can act simultaneously in a hierarchy 
to support learning, we built a simulation of ensembles of pyrami-
dal neurons arranged in three layers, with two ensembles of cells at 
the input, one ensemble of cells at the output and two ensembles of 
cells in the middle (the ‘hidden’ layer, Fig. 4a). The distal dendrites 
of the top ensemble received ‘teaching’ signals indicating desired 
or undesired outputs. No other teaching signal was provided to the 
network. As such, the hidden-layer ensembles were informed of the 
suitability of their output only via the signals they received from the 
output ensemble’s bursts. Currents injected into the somatic com-
partments of the input-layer populations controlled their activity 
levels in accordance with the learning task to be discussed below. 
Compared to Figs. 2 and 3, for this simulation we made a few modi-
fications to synaptic transmission and pyramidal neuron dynamics 
to streamline the burst-event multiplexing and decoding (Methods). 
Also, we included a global gating term, M(t), to prevent plasticity in 
the absence of teaching signals (Methods and equation (4)).

We trained our three-layer network on the exclusive OR (XOR) 
task, wherein the network must respond with a high output if only 
one input pool is active, and low output if neither or both input 
pools are active (Fig. 4a,b). We chose XOR as a canonical example 
of a task that requires a nonlinear hierarchy with appropriate credit 
assignment for successful learning. Before learning, the network was 
initialized such that the output pool treated any input combination 
as roughly equivalent (Fig. 4c, dashed line). To compute XOR, the 
output pool would have to learn to reduce its response to simultane-
ously active inputs and increase its response to a single active input.

We set up the network configuration to address a twofold ques-
tion. (1) Would an error signal applied to the top-layer neurons’ 
dendrites be propagated downward adequately? (2) Would the 
burst-dependent learning rule combine top-down signals with 
bottom-up information to make the hidden-layer neurons better 
feature detectors for solving XOR?

If the answers to these two questions were ‘yes’, we would expect 
that the two hidden ensembles would learn different features if they 
receive different feedback from the output. To test this, we provided 
hidden pool 1 with positive feedback from the output, and hidden

0

10

ER, input (Hz)

Input 1
Input 2

0

10

ER, output (Hz)

Before
After

0

45

90

BP, output (%)

–0.4

0

0.4

Teaching current (nA)

0

50

BP, hidden 1 (%)

Output BR (rescaled)

0

50

BP, hidden 2 (%)

Output BR (inverted and rescaled)

0

10

ER, hidden 1 (Hz)

Before

After

0

10

ER, hidden 2 (Hz)

(0, 0)
(1, 0)
(0, 1)
(1, 1)
(0, 0)
(1, 0)
(0, 1)
(1, 1)

(0, 0)
(1, 0)
(0, 1)
(1, 1)
(0, 0)
(1, 0)
(0, 1)
(1, 1)

(0, 0)
(1, 0)
(0, 1)
(1, 1)
(0, 0)
(1, 0)
(0, 1)
(1, 1)

Before

After

(0, 0)
(1, 0)
(0, 1)
(1, 1)

Teacher

Hidden 1
hidden 2
Hidden 2

Input 1
Input 2

Output

–
+

a

b

c
d

> Figure description (generated): This figure consists of two separate plots stacked vertically, presented without explicit panel labels (e.g., Panel A, B).

### Top Plot: Time-Series/State Transition Plot

**Overall Layout & Structure:**
This is a line graph displaying time-series data across discrete states defined on the x-axis.

**Visual Components & Symbols:**
*   **X-Axis:** The horizontal axis represents discrete states, labeled as $(0, 0)$, $(1, 0)$, $(0, 1)$, and $(1, 1)$. These likely represent combinations of binary variables or states.
*   **Y-Axis:** The vertical axis ranges from 0 to 10, representing a measured value (likely an activity level or metric).
*   **Data Lines:** Two distinct lines are plotted:
    1.  A **dashed blue line**, labeled "Before" in the legend, representing a baseline or pre-intervention state.
    2.  A **solid blue line**, labeled "After" in the legend, representing a post-intervention state.
*   **Reference Line:** A horizontal dashed gray line is present across the plot, positioned approximately at a Y-value of 5.

**Labels, Keys & Legends:**
*   **Legend:** Located in the lower-left corner of the top plot, it defines the line styles:
    *   "Before": represented by a dashed blue line.
    *   "After": represented by a solid blue line.
*   **Axis Labels:** The Y-axis is unlabeled but ranges from 0 to 10. The X-axis labels are the state combinations listed above.

**Data Trends & Details:**
*   **"Before" (Dashed Line):** The activity level remains relatively stable across all states, hovering slightly below the reference line (around Y=3 to 4).
*   **"After" (Solid Line):** The activity level shows a significant increase when transitioning into the state $(1, 0)$, peaking near Y=10. It remains high in states $(1, 0)$ and $(0, 1)$, before dropping back down towards the baseline level in state $(1, 1)$.

### Bottom Plot: Rescaled Output Plot

**Overall Layout & Structure:**
This is a second line graph, positioned directly below the top plot.

**Visual Components & Symbols:**
*   **X-Axis:** The horizontal axis mirrors the state transitions from the top plot: $(0, 0)$, $(1, 0)$, $(0, 1)$, and $(1, 1)$.
*   **Y-Axis:** The vertical axis ranges from 0 to 50, representing a measured output value.
*   **Data Line:** A single line is plotted, represented by small orange/yellow dots connected by a thin line.

**Labels, Keys & Legends:**
*   **Legend/Annotation:** The data line is explicitly labeled as "Output BR (rescaled)" in the lower-left area of this plot.
*   **Axis Labels:** The Y-axis is unlabeled but ranges from 0 to 50. The X-axis labels are the state combinations listed above.

**Data Trends & Details:**
*   The "Output BR (rescaled)" exhibits high variability across the states. It starts at a moderate level in $(0, 0)$, rises sharply to peaks near Y=50 in states $(1, 0)$ and $(0, 1)$, and then shows a noticeable drop in state $(1, 1)$ before potentially rising again or stabilizing near the end of the visible range.

> Figure description (generated): This figure consists of two separate plots stacked vertically, presented without explicit panel labels (like A or B), but clearly separated by a horizontal division. Both plots appear to be time-series or state-space visualizations, likely representing dynamic system behavior across different input conditions.

### Top Plot Description

**1. Overall Layout & Structure:**
The top plot is a line graph displaying two distinct curves against shared axes.

**2. Visual Components & Symbols:**
*   **Axes:** The plot has a vertical (Y) axis and a horizontal (X) axis.
*   **Curves:** Two lines are visible: one solid line and one dashed line. The solid line appears to represent the primary data, while the dashed line seems to represent a reference or derived signal.
*   **X-Axis Markers:** The X-axis is marked with four specific coordinate pairs: $(0, 0)$, $(1, 0)$, $(0, 1)$, and $(1, 1)$. These likely represent different input states or conditions.
*   **Y-Axis Scales:** There are two Y-axes displayed: a left axis ranging from 0 to 90, and a right axis ranging from -20 to 40 (though the tick marks are not fully labeled, the range is implied by the scale).

**3. Labels, Keys & Legends:**
*   No explicit legend is present within the plot area itself to distinguish the solid vs. dashed lines, but context suggests they represent different variables or transformations of the same underlying process.

**4. Data Trends & Details:**
*   **Solid Line Trend (Left Y-Axis):** The solid line hovers generally between 30 and 50 across the input states. It shows minor fluctuations, peaking slightly around $(1, 0)$ and $(0, 1)$, reaching values near 50-60.
*   **Dashed Line Trend (Right Y-Axis):** The dashed line remains relatively flat, hovering around the 0 mark on the right Y-axis scale across all input states.
*   **Transitions:** The plot shows distinct transitions between the four marked input conditions, with noticeable changes in the solid line's trajectory as the inputs change.

### Bottom Plot Description

**1. Overall Layout & Structure:**
The bottom plot is also a line graph, structurally similar to the top plot, displaying one primary curve against shared axes.

**2. Visual Components & Symbols:**
*   **Axes:** The plot has a vertical (Y) axis and a horizontal (X) axis.
*   **Curve:** A single, dashed-dotted line is plotted.
*   **X-Axis Markers:** The X-axis uses the same four coordinate pairs as the top plot: $(0, 0)$, $(1, 0)$, $(0, 1)$, and $(1, 1)$.
*   **Y-Axis Scale:** The Y-axis ranges from 0 to 50.

**3. Labels, Keys & Legends:**
*   A legend is present in the upper left corner of this plot: "$\text{Output BR (inverted and rescaled)}$" is associated with the dashed-dotted line.

**4. Data Trends & Details:**
*   **Curve Trend:** The dashed-dotted line exhibits a generally low baseline value (around 10-20) across most input states.
*   **Fluctuations:** There are noticeable peaks and troughs corresponding to the input transitions. For instance, there is a significant dip near $(1, 0)$ and a pronounced peak occurring after the transition to $(1, 1)$, reaching values near 40-50.

### Synthesis (Contextual Integration)

The figure presents two related dynamic plots. The top plot shows a system's response (solid line) relative to a baseline or reference signal (dashed line), evaluated across four distinct input states defined by binary coordinates $(x, y)$. The bottom plot specifically visualizes the "Output BR (inverted and rescaled)" signal, showing how this transformed output behaves across the same four input states.

e(i)
(ii)

f(i)
(ii)

Fig. 4 | Burst-dependent plasticity can solve the credit assignment problem for the XOR task. a, Each neuron population contained 500 pyramidal 
neurons. Feedforward connections transmitted events, while feedback connections transmitted bursts. The teacher (pink arrow) was applied by injecting 
a hyperpolarizing current into the output ensemble’s dendrites if their event rate was high in the presence of inputs that are either both active or both 
inactive. A depolarizing current was injected into the output ensemble’s dendrites if their event rate was low when only one of the inputs was active. 
The activity of the input populations was controlled by somatic current injections (gray arrows). The plus and minus symbols in circles represent the 
initialization of the feedback synaptic weights as mainly excitatory (plus) or inhibitory (minus). b, Input-layer event rates (ERs) for the four input conditions 
presented sequentially in time. The duration of each example was 8 s. c, Output ER before and after learning. The output ensemble acquired strong 
firing (event rate above the dotted line) at the input conditions associated with ‘true’ in XOR. Results are displayed as mean ± 2 s.d. over five random 
initializations of the single-neuron connectivity. In other panels, a single realization is displayed for clarity. d, During learning, the dendritic input (dashed 
pink) applied to the output ensemble’s neurons controlled their burst probability (solid red) in the last 0.8 s of the input condition. e, During learning, 
the burst rate (BR) at the output layer is encoded into the BP (solid red) of the hidden layer to propagate the error. For the hidden-2 population (ii), this 
inherited credit is inverted with respect to that in the hidden-1 population (i). f, After (solid line) versus before (dashed line) learning for the hidden layer. 
The ER decreased in the hidden-1 population (i) but increased in the hidden-2 population (ii). The bin size used in the population averages was 0.4 s.

> Figure caption (from PDF text): Fig. 4 | Burst-dependent plasticity can solve the credit assignment problem for the XOR task. a, Each neuron population contained 500 pyramidal 
neurons. Feedforward connections transmitted events, while feedback connections transmitted bursts. The teacher (pink arrow) was applied by injecting 
a hyperpolarizing current into the output ensemble’s dendrites if their event rate was high in the presence of inputs that are either both active or both 
inactive. A depolarizing current was injected into the output ensemble’s dendrites if their event rate was low when only one of the inputs was active. 
The activity of the input populations was controlled by somatic current injections (gray arrows). The plus and minus symbols in circles represent the 
initialization of the feedback synaptic weights as mainly excitatory (plus) or inhibitory (minus). b, Input-layer event rates (ERs) for the four input conditions 
presented sequentially in time. The duration of each example was 8 s. c, Output ER before and after learning. The output ensemble acquired strong 
firing (event rate above the dotted line) at the input conditions associated with ‘true’ in XOR. Results are displayed as mean ± 2 s.d. over five random 
initializations of the single-neuron connectivity. In other panels, a single realization is displayed for clarity. d, During learning, the dendritic input (dashed 
pink) applied to the output ensemble’s neurons controlled their burst probability (solid red) in the last 0.8 s of the input condition. e, During learning, 
the burst rate (BR) at the output layer is encoded into the BP (solid red) of the hidden layer to propagate the error. For the hidden-2 population (ii), this 
inherited credit is inverted with respect to that in the hidden-1 population (i). f, After (solid line) versus before (dashed line) learning for the hidden layer. 
The ER decreased in the hidden-1 population (i) but increased in the hidden-2 population (ii). The bin size used in the population averages was 0.4 s.
> Figure description (generated): This figure is a composite visualization, likely comprising multiple panels (though only one schematic and one plot are fully visible in the provided image snippet), illustrating a neural network model related to burst-dependent plasticity for solving the XOR task.

### 1. Overall Layout & Structure
The image contains two main visual components: a detailed schematic diagram of a neural circuit, and a time-series plot.

### 2. Visual Components & Symbols (Schematic Diagram)
The schematic depicts a multi-layered neural network structure:

*   **Input Layer:** Labeled "Input 1" and "Input 2." These are represented by a set of vertical black bars, suggesting populations of neurons. Below each input population, there is an arrow pointing right ($\rightarrow$), indicating the flow of information or activity.
*   **Hidden Layers:** Two hidden layers are shown: "Hidden 1" and "Hidden 2." Each layer consists of a population of green, triangular-shaped neurons (representing pyramidal neurons).
*   **Output Layer:** A single population of green, triangular-shaped neurons is positioned at the top.
*   **Connections:**
    *   **Feedforward Connections (Input $\rightarrow$ Hidden):** Lines connect the input populations to both "Hidden 1" and "Hidden 2."
    *   **Feedback Connections (Output $\rightarrow$ Hidden):** Lines connect the output layer back down to both "Hidden 1" and "Hidden 2."
    *   **Internal Connections:** Lines connect neurons within the hidden layers and to the output layer.
    *   **Synaptic Weight Initialization:** The feedback connections from the output to the hidden layers are marked with symbols in circles:
        *   A **plus sign ($\text{+}$)** is shown near the connection leading to "Hidden 1," indicating initialization as mainly excitatory.
        *   A **minus sign ($\text{-}$)** is shown near the connection leading to "Hidden 2," indicating initialization as mainly inhibitory.
*   **Activity Control:** The input populations are controlled by somatic current injections, indicated by gray arrows pointing towards the input neurons.
*   **Flow/Plasticity Indicators:** The caption mentions that "Feedforward connections transmitted events, while feedback connections transmitted bursts."

### 3. Visual Components & Symbols (Time-Series Plot)
The lower portion of the image displays a time-series plot:

*   **Axes:** The horizontal axis represents time (implied, as the caption mentions sequential presentation over 8s per example). The vertical axis represents a measured quantity, likely Event Rate (ER) or Burst Rate (BR), although specific labels are truncated.
*   **Curves:** Two distinct lines are visible:
    *   A **light blue line**, which shows fluctuating activity over time.
    *   A **darker/blue line** (or perhaps the same line representing different conditions), which shows distinct, sharp transitions between low and high activity states.

### 4. Contextual Caption Integration (Interpretation based on provided text)
The caption provides crucial context for the schematic:

*   **Neuron Count:** Each neuron population contained 500 pyramidal neurons.
*   **Plasticity Mechanism:** The model utilizes burst-dependent plasticity to solve the XOR task.
*   **Teacher Signal (Feedback):** The "teacher" signal is applied to the output ensemble's dendrites.
    *   A **hyperpolarizing current** (negative feedback) is applied if the output event rate was high when inputs were both active or both inactive.
    *   A **depolarizing current** (positive feedback) is applied if the output event rate was low when only one input was active.
*   **Input Control:** Input activity is controlled by somatic current injections (gray arrows).
*   **Plot Interpretation (Panel b):** The time-series plot likely represents "Input-layer event rates (ERs) for the four input conditions presented sequentially in time."
*   **Plot Interpretation (Panel c):** This panel shows "Output ER before and after learning," where the output ensemble acquires strong firing (ER above a dotted line) for 'true' XOR conditions.
*   **Plot Interpretation (Panel d):** This panel shows the dendritic input (dashed pink) controlling burst probability (solid red) during learning.
*   **Plot Interpretation (Panel e):** This panel shows how the burst rate (BR) at the output layer is encoded into the BP of the hidden layers to propagate error, noting an inversion in credit inheritance between Hidden-1 and Hidden-2.
*   **Plot Interpretation (Panel f):** This panel compares ER before (dashed line) and after (solid line) learning for the hidden layers, noting a decrease in ER for Hidden-1 and an increase for Hidden-2.

> Figure caption (from PDF text): Fig. 4 | Burst-dependent plasticity can solve the credit assignment problem for the XOR task. a, Each neuron population contained 500 pyramidal 
neurons. Feedforward connections transmitted events, while feedback connections transmitted bursts. The teacher (pink arrow) was applied by injecting 
a hyperpolarizing current into the output ensemble’s dendrites if their event rate was high in the presence of inputs that are either both active or both 
inactive. A depolarizing current was injected into the output ensemble’s dendrites if their event rate was low when only one of the inputs was active. 
The activity of the input populations was controlled by somatic current injections (gray arrows). The plus and minus symbols in circles represent the 
initialization of the feedback synaptic weights as mainly excitatory (plus) or inhibitory (minus). b, Input-layer event rates (ERs) for the four input conditions 
presented sequentially in time. The duration of each example was 8 s. c, Output ER before and after learning. The output ensemble acquired strong 
firing (event rate above the dotted line) at the input conditions associated with ‘true’ in XOR. Results are displayed as mean ± 2 s.d. over five random 
initializations of the single-neuron connectivity. In other panels, a single realization is displayed for clarity. d, During learning, the dendritic input (dashed 
pink) applied to the output ensemble’s neurons controlled their burst probability (solid red) in the last 0.8 s of the input condition. e, During learning, 
the burst rate (BR) at the output layer is encoded into the BP (solid red) of the hidden layer to propagate the error. For the hidden-2 population (ii), this 
inherited credit is inverted with respect to that in the hidden-1 population (i). f, After (solid line) versus before (dashed line) learning for the hidden layer. 
The ER decreased in the hidden-1 population (i) but increased in the hidden-2 population (ii). The bin size used in the population averages was 0.4 s.
> Figure description (generated): Based on the provided image and its associated caption, here is a detailed description of Figure 4.

***

**Figure 4 Description**

The figure is composed of multiple panels (a through f), presenting a combination of schematic diagrams, time-series plots, and comparative graphs illustrating the mechanism of burst-dependent plasticity for solving the XOR task.

**1. Overall Layout & Structure:**
The figure is structured into six distinct sub-panels (a, b, c, d, e, and f), each illustrating a different aspect of the learning process. Panels (a) through (e) appear to be schematic or time-course representations, while panel (f) is a comparative line graph.

**2. Visual Components & Symbols:**
*   **Schematics (Panel a):** This panel depicts a neural circuit schematic. It shows connections between neuron populations, including feedforward and feedback pathways.
    *   **Neurons/Populations:** Represented by implied populations (e.g., input, output ensemble, hidden layers).
    *   **Connections:** Arrows indicate signal flow. Feedforward connections transmit events, while feedback connections transmit bursts.
    *   **Current Injection:** Specific interventions are shown: a "teacher" (indicated by a pink arrow) is applied to the output ensemble's dendrites, and somatic current injections (gray arrows) control input population activity.
    *   **Initialization:** Circles containing '+' and '-' symbols denote the initial state of feedback synaptic weights (excitatory or inhibitory).
*   **Time-Series Plots (Panels b, c, d, e):** These panels display activity over time.
    *   **Lines/Curves:** Solid lines and dashed lines are used to represent different variables (e.g., Event Rates, Dendritic Input).
    *   **Thresholds:** Dotted lines are used to indicate thresholds (e.g., for firing rate).
*   **Comparative Plot (Panel f):** This panel compares activity before and after learning using distinct line styles.

**3. Labels, Keys & Legends (Derived from Caption):**
*   **Panel a:** Mentions "500 pyramidal neurons" per population. The teacher mechanism is defined based on the output ensemble's event rate relative to input conditions (both active/inactive vs. one active).
*   **Panel b:** Labeled as "Input-layer event rates (ERs) for the four input conditions presented sequentially in time." The duration of each example is specified as 8s.
*   **Panel c:** Shows "Output ER before and after learning." The dotted line represents a firing threshold.
*   **Panel d:** Illustrates the control of burst probability during learning, showing "dendritic input (dashed pink)" controlling "burst probability (solid red)" in the last 0.8s of an input condition.
*   **Panel e:** Describes how "burst rate (BR) at the output layer is encoded into the BP (solid red) of the hidden layer to propagate the error." It notes an inversion of inherited credit between hidden-2 (ii) and hidden-1 (i).
*   **Panel f:** Compares "After (solid line) versus before (dashed line) learning for the hidden layer."

**4. Data Trends & Details:**
*   **Panel b (Input ERs):** Shows sequential presentation of four input conditions, with the event rate fluctuating over time for each condition.
*   **Panel c (Output ER):** Displays the output event rate fluctuating over time, with a clear distinction between activity above and below the dotted threshold line.
*   **Panel d (Burst Control):** Shows a time-dependent relationship where the dashed pink line modulates the solid red line during the final 0.8s of an input condition.
*   **Panel e (Error Propagation):** Illustrates the encoding process, showing how a rate (BR) is mapped into another variable (BP), with specific references to hidden-1 and hidden-2 populations.
*   **Panel f (Hidden Layer Comparison):** This plot shows two distinct trends:
    *   In population (i) [hidden-1], the ER shows a **decrease** from before to after learning.
    *   In population (ii) [hidden-2], the ER shows an **increase** from before to after learning.

**5. Contextual Caption Integration:**
The figure demonstrates how burst-dependent plasticity solves the XOR problem. Panel (a) details the architecture involving feedforward and feedback connections, where the teacher signal is applied based on specific input patterns. Panels (b) through (e) detail the dynamic process of learning, showing how input rates are processed, how error is propagated via burst rate encoding (Panel e), and how the plasticity mechanism controls firing probability (Panel d). Panel (f) provides quantitative evidence of the resulting change in activity within the hidden layers post-training.

> Figure caption (from PDF text): Fig. 4 | Burst-dependent plasticity can solve the credit assignment problem for the XOR task. a, Each neuron population contained 500 pyramidal 
neurons. Feedforward connections transmitted events, while feedback connections transmitted bursts. The teacher (pink arrow) was applied by injecting 
a hyperpolarizing current into the output ensemble’s dendrites if their event rate was high in the presence of inputs that are either both active or both 
inactive. A depolarizing current was injected into the output ensemble’s dendrites if their event rate was low when only one of the inputs was active. 
The activity of the input populations was controlled by somatic current injections (gray arrows). The plus and minus symbols in circles represent the 
initialization of the feedback synaptic weights as mainly excitatory (plus) or inhibitory (minus). b, Input-layer event rates (ERs) for the four input conditions 
presented sequentially in time. The duration of each example was 8 s. c, Output ER before and after learning. The output ensemble acquired strong 
firing (event rate above the dotted line) at the input conditions associated with ‘true’ in XOR. Results are displayed as mean ± 2 s.d. over five random 
initializations of the single-neuron connectivity. In other panels, a single realization is displayed for clarity. d, During learning, the dendritic input (dashed 
pink) applied to the output ensemble’s neurons controlled their burst probability (solid red) in the last 0.8 s of the input condition. e, During learning, 
the burst rate (BR) at the output layer is encoded into the BP (solid red) of the hidden layer to propagate the error. For the hidden-2 population (ii), this 
inherited credit is inverted with respect to that in the hidden-1 population (i). f, After (solid line) versus before (dashed line) learning for the hidden layer. 
The ER decreased in the hidden-1 population (i) but increased in the hidden-2 population (ii). The bin size used in the population averages was 0.4 s.
> Figure description (generated): This request refers to a composite figure (Fig. 4) containing multiple sub-panels (a, b, c, d, e, f), which are described in the provided caption. Since only a single image snippet is provided without clear panel demarcation, I will describe the visual elements based on the description of the panels in the caption.

Based on the provided context, Figure 4 is a multi-part figure illustrating the mechanism of burst-dependent plasticity for solving the XOR task.

### 1. Overall Layout & Structure
The figure is structured into several distinct panels (a through f), each presenting a different aspect of the learning process, ranging from circuit schematics to time-series plots.

### 2. Visual Components & Symbols (Inferred from Caption)
*   **Neural Circuit Schematic (Panel a):** This panel likely contains diagrams representing neuron populations.
    *   **Neurons:** Pyramidal neurons are mentioned, with each population containing 500 units.
    *   **Connections:** Feedforward connections transmit events, while feedback connections transmit bursts.
    *   **Currents/Inputs:** Somatic current injections (gray arrows) control input population activity.
    *   **Teacher Signal:** A pink arrow indicates the application of a teacher signal, which is injected as either a hyperpolarizing current (if output event rate is high for 'true' conditions) or a depolarizing current (if output event rate is low for 'false' conditions).
    *   **Initialization:** Plus (+) and minus (-) symbols in circles denote the initial state of feedback synaptic weights (excitatory or inhibitory).
*   **Time-Series Plots (Panels b, c, d):** These panels display activity over time.
    *   **Input Layer Event Rates (Panel b):** Shows ERs for four input conditions presented sequentially.
    *   **Output ER (Panel c):** Compares output event rates before and after learning.
    *   **Dendritic Input/Burst Probability (Panel d):** Shows the dendritic input (dashed pink) controlling burst probability (solid red) during learning.
*   **Error Propagation Plots (Panels e, f):** These panels illustrate error propagation.
    *   **Error Encoding (Panel e):** Shows how burst rate (BR) at the output layer is encoded into BP of hidden layers.
    *   **Layer Comparison (Panel f):** Compares activity before and after learning for hidden layers.

### 3. Labels, Keys & Legends (Inferred from Caption)
*   **Variables:** Event Rate (ER), Burst Rate (BR), Dendritic Input, BP (Burst Probability).
*   **Conditions:** XOR task inputs ('true' vs. 'false').
*   **Time Markers:** Example duration is 8s; specific time points like the last 0.8s of an input condition are noted in Panel d.
*   **Statistical Notation:** Mean $\pm$ 2 s.d. (standard deviation) is used in Panel c.
*   **Layer Identification:** Hidden-1 population (i), Hidden-2 population (ii).

### 4. Data Trends & Details (Focusing on the visible plot structure)
The provided image snippet strongly resembles a time-series graph, likely corresponding to Panel b or c.

*   **Axes:** The horizontal axis represents time (implied by the sequential presentation of conditions). The vertical axis represents Event Rate (ER) or a similar measure.
*   **Curves:** There are at least two distinct curves visible: one solid line and one dashed line.
*   **Trend Observation:** The plot shows distinct shifts in the activity levels across sequential time segments, corresponding to different input conditions. For example, one curve shows a relatively low baseline activity followed by an increase or change in slope corresponding to the transition between input conditions.

### 5. Contextual Caption Integration
*   **Panel c Detail:** The output ensemble acquires strong firing (ER above the dotted line) specifically at input conditions associated with 'true' in XOR.
*   **Panel f Detail:** This panel compares activity *after* (solid line) versus *before* (dashed line) learning. It notes that the ER decreased in hidden-1 population (i) but increased in hidden-2 population (ii).
*   **Panel d Detail:** This panel specifically tracks how the dendritic input (dashed pink) modulates the burst probability (solid red) during the final 0.8s of an input condition while learning occurs.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1014


---

## Page 6

Articles
NatUrE NEUrOScIEncE

pool 2 with negative feedback (Fig. 4a, light blue symbols). With 
this configuration, adequate error propagation to the two hidden 
pools would make their responses diverge with learning, and the 
output pool would learn to take advantage of this change. Indeed, 
our results showed that the XOR task was solved in this manner 
after training (Fig. 4c, solid line).

To understand how this solution was aided by appropriate credit 
assignment, we examined the information about the top-down 
teaching signals in each layer. According to the learning rule, plas-
ticity can be steered by controlling the instantaneous propensity 
to burst with respect to a moving average of the burst probability 
(Bi −PiEi in equation (1) and Fig. 2e,f). In the output pool, the 
error signal applied to the apical dendrites induced a temporary 
decrease in the burst probability when the input pools were both 
active or both inactive, and a temporary increase when only one 
input pool was active (Fig. 4d and Methods). These changes in the 
output burst probability modified the output burst rate, which was 
propagated to the hidden pools. As mentioned above, the hidden 
pools received top-down signals with different signs (Fig. 4e(i),(ii), 
orange lines), and indeed their respective burst probabilities were 
altered in opposite directions (Fig. 4e(i),(ii), red lines). Due to these 
distinct top-down signals and the adaptive threshold Pi, the hid-
den pools’ response diverged during learning (Fig. 4f(i),(ii)). For 
instance, hidden pool 1 reduced its responses to both inputs being 
active, while hidden pool 2 increased its response. These changes 
were due to the top-down control of the plasticity of synapses 
between the input and hidden pools. We verified that solving this 
task depends on the plasticity of connections from input to hidden 
units, but only weakly on the size of the ensembles (Extended Data 
Fig. 1). Also, we verified that the task was solved when the time 
constant of the moving average was shorter (Extended Data Fig. 2), 
and when the feedback pathways had the same sign of connection 
(Extended Data Fig. 3). These results demonstrate that the propa-
gation of errors using burst multiplexing and the burst-dependent 
learning rule can combine to achieve hierarchical credit assignment 
in ensembles of pyramidal neurons.

Burst-dependent plasticity promotes linearity and alignment of 
feedback. Having demonstrated that a burst-dependent learning 
rule in pyramidal neurons enables online, local, spike-based solu-
tions to the credit assignment problem, we were interested in under-
standing the potential relationship between this algorithm and 
the gradient descent-based algorithms used for credit assignment 
in machine learning. To do this, we wanted to derive the average 
behavior of the burst-dependent learning rule at the coarse-grained, 
ensemble-level, and determine whether it provided an estimate of 
a loss-function gradient. More precisely, in the spirit of mean-field 
theory and linear–nonlinear rate models, we developed a model 
where each unit represents an ensemble of pyramidal neurons, with 
event rates, burst probabilities and burst rates as described above 
(Extended Data Fig. 4 and Methods). Specifically, for an ensemble 
of pyramidal neurons, we defined e(t), b(t) and p(t) as ensemble 
averages of the event train, burst train and burst probability, respec-
tively. (Note that ensemble-level activity-related quantities are low-
ercase (e, b, p), whereas single-neuron activities are uppercase (E, 
B, P); the weights do not follow this convention.) We then defined 
the connection weight between an ensemble of presynaptic neurons 
and an ensemble of postsynaptic neurons, Wpost,pre, as the effective 
impact of the presynaptic ensemble on the postsynaptic ensemble, 
taking into consideration potential polysynaptic interactions and 
inhibition (Supplementary Information).

Our goal was then to derive the ensemble-level weight updates 
from the burst-dependent plasticity rule (equation (1)). We 
assumed that any given pair of neurons were only weakly correlated 
on average. We further assumed that the neuron-specific moving 
average burst probability (Pi) is independent of the instantaneous

occurrence of events. Using these assumptions, it can be shown 
(Supplementary Information) that the effective weight averaged 
across both pre- and postsynaptic ensembles obeys:

dWpost,pre

dt
= ηM(t)[ppost(t) −ppost(t)]epost(t)epre(t)
(2)

where the learning rate η is different from that appearing in equa-
tion (1), ppost(t) is a ratio of moving averages for the postsynaptic 
burst rate and event rate, and M(t) is the aforementioned gating 
term preventing plasticity without a teacher. This learning rule can 
be shown to implement an approximation of gradient descent for 
hierarchical circuits, such as the backpropagation-of-error algo-
rithm17. Specifically, if we assume that the burst probabilities remain 
in a linear regime (linearity), that the feedback synapses are sym-
metric to the feedforward synapses (alignment), and that error sig-
nals are received in the dendrites of the top-level ensembles, then 
−[ppost(t) −ppost(t)]epost(t) is equivalent to the error signal sent 
backward in backpropagation (Supplementary Information and 
Supplementary Table 2).

The assumptions of feedback linearity and alignment can be sup-
ported by the presence of additional learning mechanisms. First, we 
examined learning mechanisms to keep the burst probabilities in a 
linear regime. Multiple features of the microcircuit control linearity 
(Extended Data Fig. 5), including distal apical inhibition28,43, which 
is consistent with the action of somatostatin-positive (SOM+) 
Martinotti cells in cortical circuits18,31. We used recurrent excitatory 
and inhibitory inputs to control the apical compartments’ potential 
(Fig. 5a). These dendrite-targeting inputs propagated bursts from 
neural ensembles at the same processing stage in the hierarchy, 
which provided them with the necessary information to keep the 
burst probabilities in a linear range of the burst-probability func-
tion. We found that a simple learning rule for these connections 
(Methods) could learn to keep burst probabilities in a linear regime, 
thus improving gradient estimates (Fig. 5b). Second, we explored 
the issue of weight symmetry. The symmetry between feedforward 
and feedback weights is an implicit assumption of many learn-
ing algorithms. However, such an assumption is unnecessary, as 
it is possible to learn weight symmetry29. In one classic algorithm, 
weight symmetry is obtained if feedforward and feedback weights 
are updated with the same error signals, plus some weight decay30. 
We used this algorithm here because it can be implemented locally 
in our model using the bursting of the presynaptic cells (Fig. 5c, 
Extended Data Fig. 6 and Methods). But, we note that our model 
is not tied to this specific algorithm, and other algorithms could 
be used. With weight symmetry learning, the ensemble-level weight 
updates aligned well with the true gradient (Fig. 5d). Altogether, 
these results demonstrate that the burst-dependent learning rule, 
averaged across ensembles of pyramidal neurons, can provide a 
good estimate of loss-function gradients in hierarchical networks.

Ensemble-level burst-dependent plasticity in deep networks 
can support good performance on standard machine learning 
benchmarks. We wanted to determine whether the ensemble-level 
learning rule could perform well on difficult tasks from machine 
learning. Specifically, we built a deep neural network comprising 
pyramidal ensemble units that formed a series of convolutional lay-
ers followed by fully connected layers (Fig. 6a). We then trained 
these networks on two challenging image categorization datasets 
that previous biologically plausible algorithms have struggled with: 
CIFAR-10 and ImageNet44.

The training in all components of the network used our 
burst-dependent plasticity rule and recurrent inputs for lineariza-
tion at fully connected hidden layers. For the CIFAR-10 dataset, we 
observed a classification test error rate of 20.1% after 400 epochs 
(where an epoch is a pass through all training images), similar to

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1015


---

## Page 7

Articles
NatUrE NEUrOScIEncE

the error rate achieved with full gradient descent in a standard 
artificial neural network (Fig. 6b). Training the feedback weights 
was critical for enabling this level of performance on CIFAR-10, as 
fixed feedback weights led to much worse performance, even when 
the number of units was increased to match the total number of 
trainable parameters (Supplementary Tables 3 and 4), in line with 
previous results44. Furthermore, rich unit-specific feedback signals 
were critical. A network trained using a global reward signal, plus 
activity correlations, while theoretically guaranteed to follow gradi-
ent descent on average13,14, was unable to achieve good performance 
on CIFAR-10 in a reasonable amount of time (Fig. 6b, node per-
turbation). For the ImageNet dataset, we observed a classification 
error rate of 56.1% on the top five predicted image classes with 
our algorithm, which is much better than the error rate achieved 
when keeping the feedback weights fixed and much closer to that 
of full gradient descent (Fig. 6c). The remaining gap between the 
ensemble-level burst-dependent learning rule and backprop per-
formance on ImageNet can likely be explained by the fact that we 
could not use recurrent input at convolutional layers due to mem-
ory limitations, which led to degraded linearity of feedback in the 
bottom layers (Extended Data Fig. 7). We also trained a network 
on the MNIST dataset, and achieved a similar performance of 1.1% 
error on the test set with all three algorithms (Extended Data Fig. 8). 
Therefore, these results demonstrate that the ensemble-level

burst-dependent learning rule, coupled with additional mecha-
nisms to promote multiplexing, linearity and alignment, can solve 
difficult tasks that other biologically plausible learning algorithms 
have struggled with.

Discussion
In this paper, we asked the following question: could high-frequency 
bursts in pyramidal neurons provide an instructive signal for synap-
tic plasticity that can coordinate learning across hierarchical circuits 
(Fig. 1)? We have shown that the well-known burst-dependence of 
plasticity combined with STP and regenerative dendritic activity 
turns feedback connections into a teacher (Fig. 2), which by mul-
tiplexing (Fig. 3) can coordinate plasticity across multiple syn-
aptic jumps (Fig. 4). We then showed that, with some additional 
burst-dependent learning at recurrent and feedback synapses, these 
mechanisms provide an approximation of a loss-function gradient 
for supervised learning (Fig. 5) and perform well on challenging 
image classification tasks (Fig. 6). Together, these results demon-
strate that a local, spike-based and experimentally supported learn-
ing rule that uses high-frequency bursts as an instructive signal can 
enable sophisticated credit assignment in hierarchical circuits.

Decades of research into biologically plausible learning have 
yet to produce a confluence of biological properties that permit 
efficient credit assignment. In this manuscript, we focused on the

Feedback path

Feedforward path

Recurrent

input

a
c

d
b

1.0

0

–10
0
10

–5 × 10–3
5 × 10–3
–3 × 10–5
3 × 10–5
0
0

Epoch 1

Apical feedback

1.0

0

–10
0
10

Epoch 10

Apical feedback

0

45

90
Hidden layer 1
Hidden layer 2
Hidden layer 3

> Figure description (generated): This figure presents a line graph titled "Hidden layer 2," illustrating the relationship between two variables, likely representing activation or some measure of activity across different states.

**1. Overall Layout & Structure:**
The figure consists of a single, large Cartesian coordinate plot. It is not divided into multiple panels (A, B, C, etc.). The visualization style is a standard 2D line graph.

**2. Visual Components & Symbols:**
*   **Axes:** There are two visible axes: a vertical (Y) axis and a horizontal (X) axis.
*   **Curves:** There are three distinct curves plotted on the graph:
    *   One **orange line** positioned near the top of the plot.
    *   One **dark blue/purple line** starting high on the left and decreasing steeply.
    *   A third, fainter curve (possibly a continuation or another data set) is visible near the top right, though it is less distinct than the other two.
*   **Spatial Relationship:** The orange line remains relatively high across the visible range of the X-axis. The dark blue/purple line starts at a high value on the Y-axis and exhibits a rapid, monotonic decrease as the X-value increases.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Hidden layer 2" centered above the plot area.
*   **Y-Axis Labels:** The vertical axis is labeled with numerical values: "90" and "45."
*   **X-Axis Labels:** The horizontal axis has no explicit numerical labels visible in the provided crop, but it represents the independent variable.

**4. Data Trends & Details:**
*   **Y-Axis Range Indication:** The Y-axis scale shows major ticks at 45 and 90.
*   **Orange Line Trend:** The orange line maintains a high value, hovering near the top of the plotted range (close to 90) and shows a slight downward trend as the X-axis increases.
*   **Dark Blue/Purple Line Trend:** This line demonstrates a steep, non-linear decay. It starts near the top of the Y-axis (close to 90) and drops sharply, passing below the midpoint between 45 and 90 before continuing to decrease more gradually towards the right side of the plot.

**5. Contextual Caption Integration:**
No external caption text was provided to integrate with the visual elements, so no specific contextual interpretation regarding cell types or feedback loops can be made based on external information. The figure strictly depicts the dynamic behavior of "Hidden layer 2" across an unlabelled input/state variable.

> Figure description (generated): ## Figure Description: Hidden Layer 3 Activation Plot

This figure is a single-panel line graph titled "Hidden layer 3." It displays the activation values across an unspecified range of input or iteration steps for multiple curves, likely representing different neurons or parameters within the third hidden layer of a neural network.

**1. Overall Layout & Structure:**
The figure consists of a single Cartesian coordinate plot. The structure is minimalist, focusing entirely on the relationship between two continuous variables plotted against each other.

**2. Visual Components & Symbols:**
*   **Axes:** The plot utilizes a standard two-dimensional coordinate system.
    *   The **Y-axis** represents the activation magnitude, scaled from 0 to 90. Major tick marks are present at intervals of 45 (and implicitly every 15 units).
    *   The **X-axis** is present but lacks explicit numerical labels in the visible portion of the image, suggesting it represents an independent variable (e.g., input magnitude or training epoch).
*   **Curves:** There are four distinct, smooth curves plotted on the graph. These curves exhibit a rapid initial decay followed by a gradual asymptotic approach toward a lower value.
    *   **Blue Curve:** This curve starts at the highest point (near 90) and exhibits the steepest initial decline, settling to the lowest final activation level among the four curves.
    *   **Red Curve:** This curve starts near 90, shows a rapid initial drop, and settles at an intermediate activation level, positioned above the blue curve.
    *   **Orange Curve (Upper):** This curve starts near 90, drops rapidly, and settles at a higher activation level than the red curve.
    *   **Orange Curve (Lower):** This curve is positioned between the Red and Upper Orange curves, showing a similar decay profile.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is clearly titled "Hidden layer 3" centered above the plotting area.
*   **Axis Labels:** The Y-axis is implicitly labeled by its numerical scale (0 to 90). No explicit label text is visible for the X-axis.
*   **Legend:** There is no explicit legend provided to distinguish which curve corresponds to a specific neuron or parameter set; the curves are differentiated solely by color (Blue, Red, two shades of Orange).

**4. Data Trends & Details:**
All four curves demonstrate a characteristic non-linear decay pattern:
*   **Initial State (Low X-values):** All curves begin at a high activation value, close to 90.
*   **Decay Phase:** Immediately following the start, all curves drop sharply. The blue curve shows the most aggressive initial decline.
*   **Asymptotic Phase (High X-values):** As the curves progress along the x-axis, their rate of change slows significantly. They flatten out, approaching a stable, lower activation value (the asymptote). The final resting points are ordered from lowest to highest: Blue $\rightarrow$ Red $\rightarrow$ Lower Orange $\rightarrow$ Upper Orange.

> Figure description (generated): ## Figure Description: Hidden Layer 1 Dynamics

This figure is a single-panel line graph illustrating the dynamics of "Hidden layer 1" under different input conditions.

**1. Overall Layout & Structure:**
The figure consists of a single 2D line plot. The structure is defined by two perpendicular axes: a vertical (Y) axis representing magnitude, and a horizontal (X) axis representing progression or time.

**2. Visual Components & Symbols:**
The plot contains four distinct colored lines, each representing a different experimental condition.

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to 90, marked in increments of 45 (0, 45, 90).
    *   The **X-axis** is labeled with numerical values ranging from 0 to 15, marked in increments of 5 (0, 5, 10, 15).
*   **Lines/Curves:** Four distinct colored lines are plotted:
    *   A **Red line**: Starts high and decays relatively slowly.
    *   An **Orange line**: Starts high, slightly below the red line initially, and decays more slowly than the red line.
    *   A **Blue line**: Starts high (near 90) and exhibits a very rapid initial decay.
    *   A **Purple line**: Starts high (near 90), decays rapidly, and tracks closely with the blue line initially.

**3. Labels, Keys & Legends:**
The figure includes a main title and a legend that defines the four plotted lines:

*   **Title:** "Hidden layer 1"
*   **Legend Entries (Color-coded):**
    *   Red line: "No recurrent input"
    *   Orange line: "Recurrent input"
    *   Blue line: "Learned feedback weights"
    *   Purple line: "Learned feedback weights + recurrent input"

**4. Data Trends & Details:**
The graph tracks the magnitude (Y-axis) as a function of progression/time (X-axis).

*   **Initial State (X=0):** All four lines begin at a high value, close to 90.
*   **Trends:**
    *   The **Red line ("No recurrent input")** and the **Orange line ("Recurrent input")** show a gradual, relatively slow decay across the range $X=0$ to $X=15$.
    *   The **Blue line ("Learned feedback weights")** and the **Purple line ("Learned feedback weights + recurrent input")** show a much steeper initial decline.
    *   The **Purple line** tracks almost identically to the **Blue line** for most of the plotted range, suggesting that adding recurrent input does not significantly alter the dynamics when learned feedback weights are present.
    *   By $X=15$, all lines have decayed significantly, with the blue/purple lines reaching a low value (approaching 10-20), while the red/orange lines remain at a higher residual value (around 50-60).

0
5
10
15

0

45

90

0
5
10
15

No recurrent input

Recurrent input

Learned feedback weights

Learned feedback weights
+ recurrent input

W∠Y
δ∠δBP

Epoch
Epoch
Epoch

Epoch
Epoch
Epoch

0

45

90

0
5
10
15

0

45

90

0
5
10
15

0

45

90

> Figure description (generated): This figure is a schematic diagram, likely representing a computational or biological model of a neural circuit. It features a vertically oriented, complex block structure with internal components and external inputs/outputs indicated by arrows.

### 1. Overall Layout & Structure
The diagram is dominated by a large, vertically elongated, green-bordered structure that appears to represent a functional unit or module. This main block is divided into two primary, stacked sections: an upper section and a lower section, separated by a central region. The overall structure suggests a layered or cascaded processing unit.

### 2. Visual Components & Symbols
**The Main Block:**
*   It is enclosed by a thick, green rectangular outline.
*   **Upper Section:** Contains an internal component represented by a red-bordered, stylized sigmoid or S-shaped curve enclosed within a rounded rectangle. This component is flanked by two small, grey circular nodes, each containing a '+' symbol (suggesting summation or activation).
*   **Lower Section:** Contains an internal component represented by a blue-bordered, stylized sigmoid or S-shaped curve enclosed within a rounded rectangle. This component is situated above a single, grey circular node containing a '+' symbol.
*   **Connections within the Block:** A dashed orange line connects the upper sigmoid component to the lower sigmoid component, indicating a connection or influence between the two processing stages.

**External Inputs and Outputs:**
*   **Inputs (Top):** Several arrows point into the top of the main green block. Two thin, light-blue lines enter from the upper left corner, and two thicker, orange arrows enter from the top center/right.
*   **Inputs (Side):** Arrows labeled 'p' and 'b' point into the upper section from the left side.
*   **Outputs (Side):** Arrows labeled 'e' points out from the lower section towards the left side.
*   **Feedback/External Inputs (Right):** Several purple arrows point into the right side of the main block, suggesting external inputs or feedback loops.
*   **Outputs (Bottom):** A thick orange arrow exits the bottom of the main block.
*   **External Connections (Bottom Left):** A thin blue arrow exits the bottom left corner.

### 3. Labels, Keys & Legends
The following labels are visible within or immediately adjacent to the structure:
*   **Variables/Labels:** $p$, $b$, $e$.
*   **Text Annotations (Top Right):** "Rec" and "in" are partially visible, suggesting a label like "Recurrent input."

### 4. Data Trends & Details
There are no traditional plots (x-y axes, data points) present; the diagram is purely schematic. The internal components are stylized activation functions (sigmoids), indicating non-linear processing within the model.

### 5. Contextual Caption Integration
Based on the visual structure, the diagram illustrates a multi-stage processing unit. The presence of sigmoid functions suggests activation or transformation layers, while the '+' nodes imply summation or integration of inputs. The labels $p$, $b$, and $e$ likely denote specific variables or states within the model (e.g., population activity, bias, error). The purple arrows indicate external influences or feedback mechanisms acting upon the system.

0
5
10
15

0

45

90

0
5
10
15

+

+

+
p

b

e

Hidden layer 1
Hidden layer 2
Hidden layer 3

Burst probability p

p – p
p – p

Fig. 5 | Burst-dependent plasticity of recurrent and feedback connections promotes gradient-based learning by linearizing and aligning feedback.  
a, Diagram of a hidden-layer unit in the rate model, with event rate e, burst probability p and burst rate b. Each unit (green outline) in the network 
represents an ensemble of pyramidal neurons. Recurrent inputs (purple arrows) from all ensembles in a layer control the dendritic potential. b, Throughout 
learning, recurrent weights were updated to push the burst probabilities toward the linear regime (top). This led to an overall decrease in the magnitudes 
of burst probabilities, while continuing to support positive and negative values necessary for credit assignment (bottom). c, Alignment of feedback weights 
Y and feedforward weights W for three layers in a three-hidden-layer network trained on MNIST. Each hidden layer contained 500 units. Recurrent inputs 
slightly reduce the angle between the two sets of weights, denoted W∠Y, while learning on the feedback weights dramatically improves weight alignment. 
Each datapoint is the angle between feedforward and feedback weights at the start of a training epoch. d, Angle between our weight updates (δ) and those 
prescribed by the backpropagation algorithm (δBP), for three layers in a three-hidden-layer network trained on MNIST. Recurrent inputs slightly improve the 
approximation to backpropagation, whereas learning on the feedback weights leads to a much closer correspondence. Each datapoint is the average angle 
between weight updates during a training epoch. In c and d, results are displayed as mean ± s.d. over n = 5 trials.

> Figure caption (from PDF text): Fig. 5 | Burst-dependent plasticity of recurrent and feedback connections promotes gradient-based learning by linearizing and aligning feedback.  
a, Diagram of a hidden-layer unit in the rate model, with event rate e, burst probability p and burst rate b. Each unit (green outline) in the network 
represents an ensemble of pyramidal neurons. Recurrent inputs (purple arrows) from all ensembles in a layer control the dendritic potential. b, Throughout 
learning, recurrent weights were updated to push the burst probabilities toward the linear regime (top). This led to an overall decrease in the magnitudes 
of burst probabilities, while continuing to support positive and negative values necessary for credit assignment (bottom). c, Alignment of feedback weights 
Y and feedforward weights W for three layers in a three-hidden-layer network trained on MNIST. Each hidden layer contained 500 units. Recurrent inputs 
slightly reduce the angle between the two sets of weights, denoted W∠Y, while learning on the feedback weights dramatically improves weight alignment. 
Each datapoint is the angle between feedforward and feedback weights at the start of a training epoch. d, Angle between our weight updates (δ) and those 
prescribed by the backpropagation algorithm (δBP), for three layers in a three-hidden-layer network trained on MNIST. Recurrent inputs slightly improve the 
approximation to backpropagation, whereas learning on the feedback weights leads to a much closer correspondence. Each datapoint is the average angle 
between weight updates during a training epoch. In c and d, results are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): This image displays a single plot, titled "Hidden layer 2," which appears to be part of a larger figure (likely Figure 5, based on the caption). The plot is a line graph illustrating changes in some measured quantity over an unspecified progression (likely training epochs, given the context of the caption).

**1. Overall Layout & Structure:**
The image contains one primary graph, which is a 2D line plot. The axes are clearly labeled with numerical scales.

**2. Visual Components & Symbols:**
*   **Axes:** There is a vertical (Y) axis and a horizontal (X) axis.
*   **Curves:** There are three distinct curves plotted on the graph, differentiated by color:
    *   A **blue line** starting high and rapidly decreasing.
    *   An **orange/red line** starting high and gradually decreasing.
    *   A **purple/violet line** starting low and remaining relatively flat or slightly decreasing.
*   **Scales:** The Y-axis ranges from 0 to 90, marked in increments of 45 (0, 45, 90). The X-axis has tick marks but no explicit numerical labels are visible in the cropped view, though it extends to at least 15.

**3. Labels, Keys & Legends:**
*   **Title:** The plot is titled "Hidden layer 2."
*   **Axis Labels:** While the Y-axis has numerical labels (0, 45, 90), the specific label for the Y-axis is not fully visible. The X-axis also lacks a clear label in this crop, but the caption suggests it relates to training progression.

**4. Data Trends & Details:**
*   **Blue Curve:** This curve starts near the maximum value (close to 90) and exhibits a very steep, rapid decline in its initial phase (from X=0 to approximately X=3), leveling off thereafter at a low value, close to 5.
*   **Orange/Red Curve:** This curve starts near the maximum value (close to 90) and shows a much slower, gradual decay across the entire visible range of the X-axis.
*   **Purple/Violet Curve:** This curve starts at a low value (near 0) and remains relatively flat, showing only a slight downward trend as the X-axis increases.

**5. Contextual Caption Integration:**
The provided caption (Fig. 5) describes the context of these plots:
*   Panel **b** discusses how recurrent weights were updated to push "burst probabilities toward the linear regime (top)," leading to a decrease in magnitudes, while supporting values for credit assignment "(bottom)."
*   Given the visual evidence of three distinct curves showing different rates of change, it is highly probable that these three lines correspond to the "burst probabilities" mentioned in the caption (e.g., one line representing a specific probability, another representing its change over time/epochs). The rapid decay of the blue line might correspond to a variable being driven toward linearity, while the slower decays represent other related parameters.

> Figure caption (from PDF text): Fig. 5 | Burst-dependent plasticity of recurrent and feedback connections promotes gradient-based learning by linearizing and aligning feedback.  
a, Diagram of a hidden-layer unit in the rate model, with event rate e, burst probability p and burst rate b. Each unit (green outline) in the network 
represents an ensemble of pyramidal neurons. Recurrent inputs (purple arrows) from all ensembles in a layer control the dendritic potential. b, Throughout 
learning, recurrent weights were updated to push the burst probabilities toward the linear regime (top). This led to an overall decrease in the magnitudes 
of burst probabilities, while continuing to support positive and negative values necessary for credit assignment (bottom). c, Alignment of feedback weights 
Y and feedforward weights W for three layers in a three-hidden-layer network trained on MNIST. Each hidden layer contained 500 units. Recurrent inputs 
slightly reduce the angle between the two sets of weights, denoted W∠Y, while learning on the feedback weights dramatically improves weight alignment. 
Each datapoint is the angle between feedforward and feedback weights at the start of a training epoch. d, Angle between our weight updates (δ) and those 
prescribed by the backpropagation algorithm (δBP), for three layers in a three-hidden-layer network trained on MNIST. Recurrent inputs slightly improve the 
approximation to backpropagation, whereas learning on the feedback weights leads to a much closer correspondence. Each datapoint is the average angle 
between weight updates during a training epoch. In c and d, results are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): This image displays a single plot titled "Hidden layer 3," which appears to be part of a larger figure (likely Figure 5, based on the caption).

**1. Overall Layout & Structure:**
The image consists of a single line graph plotted against two axes, representing the dynamics within "Hidden layer 3."

**2. Visual Components & Symbols:**
*   **Axes:** There is a vertical (Y) axis and a horizontal (X) axis.
*   **Curves:** There are two distinct curves plotted: one colored blue and one colored orange/red. Both curves start high on the Y-axis and decrease as they move along the X-axis.
*   **Data Points:** The curves appear continuous, suggesting a time series or epoch-based measurement.

**3. Labels, Keys & Legends:**
*   **Title:** The plot is titled "Hidden layer 3."
*   **Y-Axis Label:** The Y-axis is labeled with numerical values: 0, 45, and 90.
*   **X-Axis Label:** The X-axis label is partially visible and truncated, reading "...Epochs..." (The full label is not entirely clear but relates to training epochs).
*   **Legend/Key:** No explicit legend is present within the visible plot area to distinguish the blue and orange curves, though context from the caption suggests these might relate to different aspects of plasticity or weight alignment.

**4. Data Trends & Details:**
*   **Y-Axis Range:** The Y-axis ranges from 0 to 90.
*   **X-Axis Trend:** The X-axis represents progression through training epochs.
*   **Curve Trends:**
    *   The **orange/red curve** starts near the maximum value (close to 90) and exhibits a rapid initial decay, followed by a slower, more gradual decline towards the right side of the plot.
    *   The **blue curve** starts at a high value (around 90) but shows a steeper initial decline compared to the orange curve, settling at a lower asymptotic value than the orange curve as training progresses.

**5. Contextual Caption Integration:**
The provided caption (Fig. 5) describes multiple panels (a, b, c, d). Given the title "Hidden layer 3" and the nature of the plot (showing decay over epochs), this specific graph likely corresponds to panel **c** or **d**, which discuss weight alignment and angle changes during training. The caption mentions:
*   Panel **c**: "Alignment of feedback weights Y and feedforward weights W for three layers in a three-hidden-layer network trained on MNIST."
*   Panel **d**: "Angle between our weight updates ($\delta$) and those prescribed by the backpropagation algorithm ($\delta_{BP}$), for three layers in a three-hidden-layer network trained on MNIST."

The plot visually represents the change in some metric (likely an angle or magnitude) over training epochs for Hidden Layer 3.

> Figure caption (from PDF text): Fig. 5 | Burst-dependent plasticity of recurrent and feedback connections promotes gradient-based learning by linearizing and aligning feedback.  
a, Diagram of a hidden-layer unit in the rate model, with event rate e, burst probability p and burst rate b. Each unit (green outline) in the network 
represents an ensemble of pyramidal neurons. Recurrent inputs (purple arrows) from all ensembles in a layer control the dendritic potential. b, Throughout 
learning, recurrent weights were updated to push the burst probabilities toward the linear regime (top). This led to an overall decrease in the magnitudes 
of burst probabilities, while continuing to support positive and negative values necessary for credit assignment (bottom). c, Alignment of feedback weights 
Y and feedforward weights W for three layers in a three-hidden-layer network trained on MNIST. Each hidden layer contained 500 units. Recurrent inputs 
slightly reduce the angle between the two sets of weights, denoted W∠Y, while learning on the feedback weights dramatically improves weight alignment. 
Each datapoint is the angle between feedforward and feedback weights at the start of a training epoch. d, Angle between our weight updates (δ) and those 
prescribed by the backpropagation algorithm (δBP), for three layers in a three-hidden-layer network trained on MNIST. Recurrent inputs slightly improve the 
approximation to backpropagation, whereas learning on the feedback weights leads to a much closer correspondence. Each datapoint is the average angle 
between weight updates during a training epoch. In c and d, results are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): Based on the provided image snippet and the associated caption, here is a detailed description of the visual content:

## Figure Description Analysis

The provided image snippet appears to be a cropped portion of a multi-panel figure (likely Figure 5, as referenced in the caption). The visible portion focuses on a graph related to "Hidden layer 1."

### 1. Overall Layout & Structure
The visible content is a **line graph** or plot, suggesting the visualization of quantitative data over some progression (likely time or training epochs). The title "Hidden layer 1" indicates the specific component being analyzed.

### 2. Visual Components & Symbols
*   **Axes:** The plot features a vertical (Y) axis and a horizontal (X) axis, although the X-axis labels are not visible in the snippet.
*   **Curves/Lines:** There are at least two distinct curves plotted:
    *   A **darker, downward-sloping curve** (appearing purple or dark blue).
    *   A **lighter, nearly horizontal curve** (appearing orange/red) positioned higher on the Y-axis.
*   **Y-Axis Scale:** The visible portion of the Y-axis shows numerical markers: **90** and **45**.

### 3. Labels, Keys & Legends
*   **Title:** "Hidden layer 1" is prominently displayed above the plot area.
*   **Axis Labels:** No explicit axis labels are visible in this crop, though the Y-axis scale is present.

### 4. Data Trends & Details
*   **Dark Curve Trend:** This curve starts near the top of the visible range (close to 90) and exhibits a clear, continuous **decreasing trend** as it moves along the X-axis. It passes below 45 towards the right edge of the visible plot area.
*   **Light Curve Trend:** This curve remains relatively **flat and high**, hovering near the 90 mark, indicating a stable or slowly changing value.

### 5. Contextual Caption Integration
The caption provides crucial context for interpreting this plot, although the specific panel (a, b, c, or d) corresponding to this graph is not explicitly stated in the snippet.

*   **Caption Context:** The caption discusses "Burst-dependent plasticity," "recurrent and feedback connections," and the alignment of weights ($W$ and $Y$).
*   **Relevance to Plot:** The caption mentions: "b, Throughout learning, recurrent weights were updated to push the burst probabilities toward the linear regime (top). This led to an overall decrease in the magnitudes of burst probabilities, while continuing to support positive and negative values necessary for credit assignment (bottom)."
    *   This description strongly suggests that the **light, high curve** might represent a parameter being pushed toward a "linear regime" (the top), while the **dark, decreasing curve** might represent the magnitude of burst probabilities decreasing over training.

In summary, the visible image is a comparative line graph illustrating two distinct trends associated with "Hidden layer 1," likely tracking the evolution of network parameters (such as burst probabilities or weight alignment metrics) during a learning process.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1016


---

## Page 8

Articles
NatUrE NEUrOScIEncE

frequency dependence of LTP/LTD, STP, dendritic nonlinearities 
and inhibitory microcircuits. We focused on these aspects in part 
because the previous literature has established that these properties 
have important links with synaptic plasticity4,38, but also because 
they are very well-established properties of cortical circuits. Our 
burst-dependent learning rule itself could readily be implemented 
by previously established synaptic plasticity signaling pathways39. 
Overall, our model can be seen as a concrete implementation of a 
recent proposal from Lillicrap et al.15, which posited that differences 
in activity over time could carry gradient signals. Here, we have 
shown that differences in the probability of high-frequency bursts 
can carry gradient signals without affecting the time-dependent 
flow of sensory information. Therefore, one of the primary les-
sons from our model is that when local synaptic plasticity rules are 
sensitive to high-frequency bursts, then pyramidal neurons pos-
sess the necessary machinery for backprop-like top-down control 
of synaptic plasticity.

It is important to note that there are a number of limitations to 
our model. First, our ensemble-level models used ‘ensemble units’ 
that incorporated the activity of many pyramidal neurons. But, there 
is no reason that the algorithm could not in principle work with 
population coding45 or with time-averaged firing of single neurons. 
Second, the presence of the gating term, M(t), may be seen as an 
additional limitation in the model, since it is left in an abstract form 
and not directly motivated by biology. But, such gating mechanisms 
could be implemented by dendritic disinhibition31,38 (Extended Data 
Fig. 5b) or transient neuromodulation10. Third, we did not include 
soma-targeting recurrent connections between pyramidal neurons 
within a layer, despite the fact that such connections are known to

exist. We did this for the sake of simplicity, but again, we consider 
such recurrent connectivity to be fully compatible with our model 
and a subject for future investigations. Finally, our model makes 
some high-level assumptions about the structure of cortical cir-
cuitry. For example, we assumed that top-down signals are received 
at apical dendrites while bottom-up signals are received at basal 
dendrites. There is evidence for this structure42, but also some data 
showing that it is not always this way46. Likewise, we assumed that 
pyramidal neurons across the cortical hierarchy project reciprocally 
with one another. There is some evidence that the same cells that 
project backward in the cortical hierarchy also project forward47, 
but the complete circuitry of cortex is far from determined.

Our model makes a number of falsifiable predictions that could 
be examined experimentally. First, the model predicts that there 
should be a polarization of STP along the sensory hierarchy, with 
bottom-up synaptic projections being largely STD and top-down 
synaptic projections being largely STF. There are reports of such 
differences in thalamocortical projections33,34, which suggests that 
an important missing component of our model is the inclusion of 
thalamic circuitry. Second, because our model proposes that burst 
firing carries information about errors, there should be a relation-
ship between burst firing and progress in learning. Specifically, 
our model predicts that the variance in burst probabilities across a 
population should be correlated with the errors made during learn-
ing (Extended Data Fig. 9). Experimental evidence in other systems 
supports this view27. Third, our model predicts that the moving 
average of the number of times that a neuron emits a burst when 
it spikes (its ‘burst fraction’) should determine the threshold for 
LTP in pyramidal neurons. Thus, and consistent with the fact that

b
a

0

40

100

80

60

20

0
100
200
300
400

CIFAR-10

Test error (%)

Epoch

Backprop
Fixed feedback weights
Learned feedback weights
Node pertubation

0

40

100

> Figure description (generated): This figure presents a single line graph illustrating the decay of some measured variable over time, likely representing a dynamic process in neuroscience.

**1. Overall Layout & Structure:**
The figure consists of one primary plot area. It is a time-series graph with two axes: a vertical (Y) axis and a horizontal (X) axis.

**2. Visual Components & Symbols:**
The plot contains four distinct lines, each representing a different data trend:

*   **Purple Line:** This line starts high and remains relatively stable, showing a slight downward trend over the duration of the plot.
*   **Blue Line:** This line starts at a high value, exhibits a rapid initial decay, and then settles into a slower, more gradual decline.
*   **Black Line:** This line starts at a high value and shows a steep, rapid decay.
*   **Gray Line:** This line starts at an intermediate high value and exhibits a rapid decay, similar in shape to the black line but starting lower.

All lines are plotted against the shared axes.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label (Partial):** The vertical axis is labeled with a partial unit: "Tuning decay ($\text{s}^{-1}$)" (The full label is partially cut off but this is the visible text). The numerical scale ranges from 0 to 100, marked in increments of 20 (0, 20, 40, 60, 80, 100).
*   **X-Axis Label (Partial):** The horizontal axis is present but lacks a clear label in the visible area, though it represents time progression.
*   **Title/Annotation (Top Right):** The text "ON ART" is visible in the upper right corner, likely a figure or section title.

**4. Data Trends & Details:**
The graph displays the decay profiles of four different variables over time:

*   **Purple Line:** Starts near 90 and decays slowly to approximately 82-83.
*   **Blue Line:** Starts around 65, decays rapidly initially to about 50, and then slowly settles near 48-50.
*   **Black Line:** Starts around 85, decays very steeply to approximately 20.
*   **Gray Line:** Starts around 45, decays steeply to approximately 18-20.

**5. Contextual Caption Integration:**
No specific contextual caption is provided, so no cell types or circuit elements can be identified beyond the general measurement of "Tuning decay ($\text{s}^{-1}$)."

> Figure description (generated): This figure is a single-panel line graph illustrating the performance or stability of different feedback weight configurations over an iterative process.

**1. Overall Layout & Structure:**
The figure consists of a single 2D line plot. The axes are clearly defined, and the data is presented using three distinct colored lines corresponding to different experimental conditions.

**2. Visual Components & Symbols:**
*   **Axes:** The horizontal axis (x-axis) represents an iteration count, ranging from 0 to 400. The vertical axis (y-axis) represents a normalized value, ranging from 0 to 100.
*   **Lines:** Three distinct lines are plotted:
    *   A **blue line**, representing "Fixed feedback weights."
    *   A **red line**, representing "Learned feedback weights."
    *   A **purple/lavender line**, representing "Node perturbation."

**3. Labels, Keys & Legends:**
A legend is provided in the upper left corner of the plot area:
*   **Blue line:** Labeled "Fixed feedback weights"
*   **Red line:** Labeled "Learned feedback weights"
*   **Purple/Lavender line:** Labeled "Node perturbation"

The axes are labeled as follows:
*   **Y-axis:** Labeled with numerical ticks from 0 to 100.
*   **X-axis:** Labeled with numerical ticks from 0 to 400.

**4. Data Trends & Details:**
The plot shows the convergence behavior of the three conditions:

*   **Node Perturbation (Purple Line):** This line starts at a high value (approximately 85-90) and remains relatively flat, showing minimal decrease across the entire range of iterations (0 to 400), hovering around a value slightly above 80.
*   **Fixed Feedback Weights (Blue Line):** This line starts at a high value, slightly below the Node Perturbation line (around 70-75). It exhibits a rapid initial decrease in the first $\sim$100 iterations, dropping to around 50. After this initial drop, the decline slows significantly, and the line continues a gradual descent towards approximately 48 by iteration 400.
*   **Learned Feedback Weights (Red Line):** This line starts at the highest initial value among the three curves, around 70. It shows the steepest and most consistent decline across all iterations. By iteration 400, this line has converged to the lowest value among the three curves, approximately around 8-10.

**5. Contextual Caption Integration:**
No specific contextual information regarding cell types, layers, or feedback loops is provided within the visual elements of the graph itself; the labels refer only to the *type* of weight configuration being tested.

80

60

20

0
100
200
300
400

Train error (%)

Epoch

c

ImageNet

Test top-5 error (%)

30

50

100

80

90

70

60

40

0
10
20
30
50
40
Epoch

Backprop

Fixed feedback weights

Learned feedback weights

Train top-5 error (%)

30

50

100

80

90

70

60

40

0
10
20
30
50
40
Epoch

Input

Fully connected

Convolutional

Fig. 6 | Ensemble-level burst-dependent plasticity supports learning in deep networks. a, The deep networks consisted of an input layer, a series of 
convolutional layers and a series of fully connected layers. Layers were connected with sets of feedforward weights (blue arrows) and feedback weights 
(orange arrows). Fully connected hidden layers contained recurrent connections (purple arrows). b, Our learning rule, combined with learning of the 
feedback weights, was able to reach the performance of the backpropagation algorithm (backprop) on the CIFAR-10 classification task. c, A network 
trained using our learning rule was able to learn to classify images in the ImageNet dataset when feedback weights were also updated. In b and c, results 
are displayed as mean ± s.d. over n = 5 trials.

> Figure caption (from PDF text): Fig. 6 | Ensemble-level burst-dependent plasticity supports learning in deep networks. a, The deep networks consisted of an input layer, a series of 
convolutional layers and a series of fully connected layers. Layers were connected with sets of feedforward weights (blue arrows) and feedback weights 
(orange arrows). Fully connected hidden layers contained recurrent connections (purple arrows). b, Our learning rule, combined with learning of the 
feedback weights, was able to reach the performance of the backpropagation algorithm (backprop) on the CIFAR-10 classification task. c, A network 
trained using our learning rule was able to learn to classify images in the ImageNet dataset when feedback weights were also updated. In b and c, results 
are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): This image displays a single line graph, which appears to be Panel (c) from the referenced Figure 6, based on the provided caption context.

### 1. Overall Layout & Structure
The figure consists of a single two-dimensional line plot. The structure is purely graphical, presenting performance metrics over an unspecified progression (likely training epochs or iterations).

### 2. Visual Components & Symbols
The plot features a standard Cartesian coordinate system:
*   **Y-axis (Vertical Axis):** Represents a performance metric, ranging from 30 to 100.
*   **X-axis (Horizontal Axis):** Represents the progression of training, though specific labels are not visible in this cropped view.
*   **Data Lines:** Three distinct lines track performance, differentiated by color and line style:
    *   **Gray Line:** Represents "Backprop."
    *   **Blue Line:** Represents "Fixed feedback weights."
    *   **Red Line:** Represents "Learned feedback weights."

### 3. Labels, Keys & Legends
A legend is present in the upper left corner of the plotting area:
*   **Backprop:** Labeled next to a gray line segment.
*   **Fixed feedback weights:** Labeled next to a blue line segment.
*   **Learned feedback weights:** Labeled next to a red line segment.

### 4. Data Trends & Details
The plot tracks the performance of three different training methodologies:

*   **Backprop (Gray Line):** Starts at a high value (around 60-70) and shows a steady, gradual decline over the progression shown on the x-axis, leveling off around 40.
*   **Fixed feedback weights (Blue Line):** Starts at the highest performance level (near 95) and remains relatively flat, showing minimal decline across the observed range.
*   **Learned feedback weights (Red Line):** Starts at a high performance level (around 87-90) and exhibits a more dynamic trend. It decreases initially, then shows a noticeable drop around the middle of the x-axis range (down to approximately 57), before stabilizing at a lower level (around 56).

### 5. Contextual Caption Integration
The caption identifies this plot as displaying results from a network trained on the **ImageNet dataset** (Panel c). The lines represent performance metrics ($\text{mean} \pm \text{s.d.}$ over $n=5$ trials) for the three learning approaches: standard backpropagation, a model where feedback weights are held constant, and a model where feedback weights are actively learned.

> Figure caption (from PDF text): Fig. 6 | Ensemble-level burst-dependent plasticity supports learning in deep networks. a, The deep networks consisted of an input layer, a series of 
convolutional layers and a series of fully connected layers. Layers were connected with sets of feedforward weights (blue arrows) and feedback weights 
(orange arrows). Fully connected hidden layers contained recurrent connections (purple arrows). b, Our learning rule, combined with learning of the 
feedback weights, was able to reach the performance of the backpropagation algorithm (backprop) on the CIFAR-10 classification task. c, A network 
trained using our learning rule was able to learn to classify images in the ImageNet dataset when feedback weights were also updated. In b and c, results 
are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): Based on the provided image snippet and its associated caption, here is a detailed description of the visual contents:

## Figure Description Analysis

The provided image appears to be a composite figure, likely containing multiple panels (a, b, and c), as referenced in the caption. The visible portion primarily shows a graph/plot section, which corresponds to panel (c) based on the caption's description of ImageNet classification results.

### 1. Overall Layout & Structure
The visible portion is dominated by a line graph plotting performance metrics against an unspecified variable (likely training epochs or steps). The caption indicates the figure contains three parts:
*   **Panel (a):** A schematic diagram of a deep network architecture.
*   **Panel (b):** A plot showing performance comparison on the CIFAR-10 task.
*   **Panel (c):** A plot showing performance on the ImageNet dataset, which is the visible graph in the snippet.

### 2. Visual Components & Symbols (Focusing on the Visible Plot)
The visible area is a standard Cartesian coordinate plot:

*   **Axes:**
    *   The **Y-axis (Vertical Axis)** is labeled with numerical values ranging from 40 to 100, suggesting a performance metric (e.g., accuracy percentage).
    *   The **X-axis (Horizontal Axis)** is not fully visible but represents the progression of training or data points.
*   **Curves/Lines:** There are three distinct colored lines plotted on the graph, indicating different experimental conditions or network configurations.
    *   **Blue Line:** This line starts high (near 95-100) and remains relatively flat, showing a very high level of performance.
    *   **Red Line:** This line starts lower than the blue line (around 90) and shows a gradual, steady decline initially, followed by a slight leveling off.
    *   **Gray Line:** This line starts at the lowest initial performance (around 80) and shows a more pronounced, stepwise decline over the progression shown.

### 3. Labels, Keys & Legends
*   **Y-Axis Label:** The numerical scale is clearly marked (40, 50, 60, ..., 100).
*   **Top Right Label:** The text "ImageNet" is visible in the upper right corner, indicating the dataset being used for this specific plot (Panel c).
*   **Data Annotation:** The caption specifies that in panels (b) and (c), results are displayed as "mean $\pm$ s.d." over $n=5$ trials, implying the lines represent mean performance with standard deviation implicitly represented or omitted in this specific rendering.

### 4. Data Trends & Details (Visible Plot)
The plot illustrates the learning trajectory for three conditions on the ImageNet dataset:

*   **Blue Curve:** Exhibits high and stable performance, hovering near 95-100.
*   **Red Curve:** Starts high and shows a moderate decay, settling around the 60-65 mark towards the right side of the visible plot.
*   **Gray Curve:** Shows a steeper initial decline compared to the red curve, dropping significantly and leveling off around the 45-50 mark.

### 5. Contextual Caption Integration
The caption clarifies the context for this plot:
*   **Panel (c):** This graph specifically represents "A network trained using our learning rule was able to learn to classify images in the ImageNet dataset when feedback weights were also updated."
*   The presence of three distinct lines suggests the comparison between different network configurations or learning rule variants being tested on ImageNet.

> Figure caption (from PDF text): Fig. 6 | Ensemble-level burst-dependent plasticity supports learning in deep networks. a, The deep networks consisted of an input layer, a series of 
convolutional layers and a series of fully connected layers. Layers were connected with sets of feedforward weights (blue arrows) and feedback weights 
(orange arrows). Fully connected hidden layers contained recurrent connections (purple arrows). b, Our learning rule, combined with learning of the 
feedback weights, was able to reach the performance of the backpropagation algorithm (backprop) on the CIFAR-10 classification task. c, A network 
trained using our learning rule was able to learn to classify images in the ImageNet dataset when feedback weights were also updated. In b and c, results 
are displayed as mean ± s.d. over n = 5 trials.
> Figure description (generated): Based on the provided image snippet and its associated caption, here is a detailed description of the visual contents:

### Figure Description Analysis

The provided image snippet appears to be a schematic diagram illustrating the architecture of a deep network, likely corresponding to Panel 'a' described in the caption.

**1. Overall Layout & Structure:**
The image displays a schematic representation of a layered neural network structure, presented as a stylized circuit diagram or block diagram. The primary focus is on the internal connectivity of a network layer, showing inputs and connections flowing through nodes.

**2. Visual Components & Symbols:**
*   **Nodes/Neurons:** The network structure is represented by a series of distinct, stylized nodes arranged in two rows within a bounding shape. These nodes are depicted as small, upright, vase-like or stylized rectangular shapes (resembling simplified neurons).
*   **Input/Output Representation:** The overall structure is enclosed within a large, rounded rectangular boundary, which represents the network layer or module.
*   **Connections (Weights/Flow):** Connections between elements are indicated by arrows:
    *   **Blue Arrows:** Two prominent blue arrows point into the top row of nodes from an external source labeled 'L' (likely representing input or a specific layer). These arrows indicate feedforward connections.
    *   **Orange Arrows:** Two prominent orange arrows point into the top row of nodes from an external source, positioned near the blue arrows. These indicate feedback connections.
    *   **Internal Connections (Dots):** Small green dots are scattered between the nodes in both the top and bottom rows, suggesting internal connections or intermediate processing points within the layer.
*   **Layer Structure:** The nodes are arranged in two horizontal rows, suggesting at least two layers or processing levels within this schematic view.

**3. Labels, Keys & Legends:**
*   **External Label:** The letter 'L' is visible above the diagram, associated with the incoming arrows.
*   **Internal Label:** The text "put" is visible on the left side, likely indicating an input or processing stage.
*   **Arrow Color Coding (Inferred from Caption):** The caption clarifies the meaning of the arrows:
    *   Blue arrows represent **feedforward weights**.
    *   Orange arrows represent **feedback weights**.

**4. Data Trends & Details:**
Since this is a structural schematic and not a plot, there are no axes or data trends to describe.

**5. Contextual Caption Integration:**
The caption identifies this structure as part of a deep network: "a, The deep networks consisted of an input layer, a series of convolutional layers and a series of fully connected layers." The schematic visually represents the connectivity within one such layer, showing how inputs (implied by 'L' and "put") interact with the nodes via feedforward (blue) and feedback (orange) weights.

Nature Neuroscience | VOL 24 | JulY 2021 | 1010–1019 | www.nature.com/natureneuroscience
1017


---

## Page 9

Articles
NatUrE NEUrOScIEncE

synaptic weights have a finite range, our model predicts that if a 
neuron generally bursts whenever it spikes it will be more difficult 
to induce LTP in that neuron, and vice versa. Finally, our model 
predicts that inhibition in the distal apical dendrites serves, in part, 
to homeostatically regulate burst probabilities to promote learning. 
Thus, a fairly simple prediction from the model is that manipula-
tions of distal dendrite-targeting interneurons, such as SOM+ inter-
neurons, should lead to unusual levels of bursting in cortical circuits 
and disrupt learning. Some recent experimental evidence supports 
this prediction38.

Linking low-level and high-level computational models of learn-
ing is one of the major challenges in computational neuroscience. 
Our focus on supervised learning of static inputs was motivated by 
recent progress in this area. However, machine learning researchers 
have also been making rapid progress in unsupervised learning on 
temporal sequences in recent years. We suspect that many of the 
same mechanisms we explored here (that is, burst-dependent plas-
ticity), but also many of the mechanisms not explored here (that 
is, plasticity induced by cooperative synaptic inputs producing den-
dritic spikes48) or bursting induced by feedforward activity escaping 
feedforward inhibition49,50 could be adapted for unsupervised learn-
ing of temporal sequences in hierarchical circuits. It is likely that the 
brain combines unsupervised and supervised learning mechanisms, 
and future research should be directed toward how neurons may 
combine different rules for these purposes. Ultimately, by show-
ing that a top-down orchestration of learning is a natural result of 
a small set of experimentally observed physiological phenomena, 
our work opens the door to future approaches that use the unique 
physiology of cortical microcircuits to implement powerful learning 
algorithms on dynamic stimuli.

Online content
Any methods, additional references, Nature Research report-
ing summaries, source data, extended data, supplementary infor-
mation, acknowledgements, peer review information; details of 
author contributions and competing interests; and statements of 
data and code availability are available at https://doi.org/10.1038/
s41593-021-00857-x.

Received: 30 March 2020; Accepted: 15 April 2021;  
Published online: 13 May 2021