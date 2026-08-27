## Page 1

Behavioral/Systems/Cognitive

Predictive Coding as a Model of Response Properties in
Cortical Area V1

Michael W. Spratling
Division of Engineering, King’s College London, London WC2R 2LS, United Kingdom, and Centre for Brain and Cognitive Development, Birkbeck,
University of London, London WC1E 7JL, United Kingdom

A simple model is shown to account for a large range of V1 classical, and nonclassical, receptive field properties including orientation
tuning, spatial and temporal frequency tuning, cross-orientation suppression, surround suppression, and facilitation and inhibition by
flankers and textured surrounds. The model is an implementation of the predictive coding theory of cortical function and thus provides
a single computational explanation for a diverse range of neurophysiological findings. Furthermore, since predictive coding can be
related to the biased competition theory and is a specific example of more general theories of hierarchical perceptual inference, the
current results relate V1 response properties to a wider, more unified, framework for understanding cortical function.

Introduction
Predictive coding (PC) provides an elegant theory of how bot-
tom–up evidence is combined with top–down priors to compute
the most likely interpretation of sensory data. Specifically, PC
proposes that an internal representation of the world generates
predictions that are compared with stimulus-driven activity to
calculate the residual error between the prediction and the sen-
sory evidence. A number of previous proposals for how PC could
be implemented in cortical circuitry have all suggested that cor-
tical feedback connections carry predictions and that these act on
regions at preceding stages along an information processing
pathway to calculate the residual error, which is then propagated
via cortical feedforward connections (Mumford, 1992; Barlow,
1994; Rao and Ballard, 1999; Murray et al., 2004; Friston, 2005,
2009; Jehee et al., 2006; Kilner et al., 2007).
An alternative implementation of PC, the PC/BC model
(Spratling, 2008a,b), proposes that the calculation of the residual
error is performed by connections intrinsic to each cortical re-
gion, rather than via feedforward and feedback connection be-
tween cortical regions. When viewed in this way, PC can be
interpreted as a mechanism of competition between different
representations of the sensory world. PC/BC makes particular
predictions about the mechanism of competition operating
within each cortical area. Specifically, this interpretation of PC
requires that neurons that represent predictions (presumed to be
pyramidal cells) suppress the inputs to neighboring prediction
neurons within a cortical region. This is in contrast to most other
models of cortical inhibition, which presume that neurons sup-
press the outputs of other neurons. Furthermore, PC/BC requires

that the strength with which a prediction neuron suppresses a
particular input should be proportional to the strength of the
afferent connection that that prediction neuron receives from
that input. This has the consequence that the strength of compe-
tition between two prediction neurons is proportional to the de-
gree of overlap between their receptive fields (RFs).

The effects of competitive interactions between cortical neu-
rons have been most extensively studied in primary visual cortex.
Hence, to determine whether the particular mechanism of com-
petition proposed by the PC/BC model is consistent with com-
petitive mechanisms known to operate in cortex, PC/BC was used
to simulate the competition between neurons in a population of
V1 simple cells. The model was presented with stimuli identical
with those used in physiological investigations of V1 response
properties. Crucially, the model remained fixed across all the
experiments. Hence the model was tested in a manner analogous
to V1 with only the parameters for the stimulus (contrast, grating
wavelength, presentation time, etc.) under the experimenter’s
control. The behavior of the model is in good agreement with a
wide range of classical and nonclassical RF properties of neurons
in cortical area V1. This suggests that the PC/BC version of pre-
dictive coding is consistent with the mechanism of competition
implemented in primary visual cortex and hence that many of the
varied response properties observed in V1 neurons may simply be
a by-product of the cortex performing predictive coding.

Materials and Methods
The PC/BC model. Spratling (2008a) introduced a nonlinear model of
predictive coding (nonlinear PC/BC), illustrated in Figure 1, which is
implemented using the following equations:

eSi  ySi1 A 2  Wˆ SiTySi
(1)

ySi 4 1  ySi  WSieSi
(2)

ySi 4 ySi  1  Wˆ Si1TySi1,
(3)

where superscripts of the form Si indicate processing stage i of a hierar-
chical neural network, eSi is a (m by 1) vector of error-detecting neuron

Received Oct. 2, 2009; revised Dec. 14, 2009; accepted Jan. 23, 2010.

ThisworkwassupportedbyEngineeringandPhysicalSciencesResearchCouncilGrantEP/D062225/1.Thanksto
K. De Meyer for helpful comments on a previous draft of this article.

Correspondence should be addressed to Michael W. Spratling, Division of Engineering, King’s College London,
Strand, London WC2R 2LS, UK. E-mail: michael.spratling@kcl.ac.uk.

DOI:10.1523/JNEUROSCI.4911-09.2010
Copyright © 2010 the authors
0270-6474/10/303531-13$15.00/0

The Journal of Neuroscience, March 3, 2010 • 30(9):3531–3543 • 3531


---

## Page 2

activations, ySi is a (n by 1) vector of prediction neuron activations, WSi

is a (n by m) matrix of synaptic weight values normalized such that the
sum of each row is equal to , Wˆ Si is a matrix representing the same
synaptic weight values as W but such that the rows are normalized to have
a maximum value of , 1, 2, and c¸ are parameters, and A and R indicate
element-wise division and multiplication, respectively. These equations
are evaluated in the order 1, 2, 3, and the values of ySi given by Equation
3 are then substituted back into Equations 1 and 2 to recursively calculate
the changing neural activations at each time step.

A value of  equal to 1 has been used in previous work (Spratling,
2008a; De Meyer and Spratling, 2009; Spratling et al., 2009). Changing
the value of this particular parameter has no effect on the behavior of the
model, except to scale the activation values of the error-detecting neu-

rons by

1
. In these experiments, a value of  equal to 5000 was used to

produce error neuron activations of the same order of magnitude as the
prediction neuron activations (see supplemental material, available at
www.jneurosci.org).

Equation 1 describes the calculation of the neural activity for each
population of error-detecting neurons. These values are a function of the
activity of the prediction neurons in the preceding cortical area divisively
modulated by a weighted sum of the outputs of the prediction neurons in
the current area (Spratling et al., 2009). The activation of the error-
detecting neurons can be interpreted in two ways. First, e can be consid-
ered to represent the residual error between the input to the current
processing stage (ySi  1) and the reconstruction of the input Wˆ SiTySi
generated by the prediction neurons at the current processing stage. The
values of e indicate the degree of mismatch between the top–down re-
construction of the input and the actual input (assuming 2 is sufficiently

small to be negligible). When a value within e is greater than

1
, it indi-

cates that a particular element of the input is underrepresented in the

reconstruction; a value of less than

1
 indicates that a particular element

of the input is overrepresented in the reconstruction; and a value of

1

indicates that the top–down reconstruction perfectly predicts the bot-
tom–up stimulation. A second interpretation is that e represents the
inhibited inputs to a population of competing prediction neurons. Each
prediction neuron modulates its own inputs, which helps stabilize the
response of the prediction neurons, since a strongly (or weakly) active
prediction neuron will suppress (magnify) its inputs and hence reduce
(enhance) its own response. Prediction neurons that share inputs (i.e.,
that have overlapping RFs) will also modulate each other’s inputs. This
generates a form of competition between the prediction neurons, such
that each neuron effectively tries to block other prediction neurons from
responding to the inputs that it represents.

Equation 2 describes the updating of the prediction neuron activa-
tions. The response of each prediction neuron is a function of its activa-
tion at the previous iteration and a weighted sum of afferent inputs from
the error-detecting neurons. Equation 3 describes the effects on the pre-

diction neuron activations of top–down inputs from prediction neurons
at the next stage in the neural hierarchy. These top–down inputs are a
weighted sum of the activity of the prediction neurons at the subsequent
processing stage and have a purely modulatory effect on the current
processing stage. This feedback allows predictions generated by neurons
higher up a processing hierarchy (which have larger receptive fields) to
influence the strength of each prediction made at the current processing
stage. Equivalently, feedback can be interpreted as influencing the out-
come of the competition occurring between prediction neurons at the
current processing stage. Hence the PC/BC model can also be interpreted
as an implementation of the biased competition model of cortical func-
tion (Spratling, 2008a,b).

The V1 model. This article is concerned with modeling a single cortical
region, V1, in isolation. Hence only a single processing stage will be
modeled (Fig. 2). Furthermore, all top–down, modulatory, inputs to this
area are ignored (i.e., y V11  0), and hence Equation 3 can also be
ignored. Since there is only one processing stage in the model, the super-
scripts will be dropped, and the input to V1 will be described by a vector,
x  y V11, of inputs coming from a model of the lateral geniculate
nucleus (LGN) (see below). The model can thus be simplified to the
following two equations:

e  x A 2  Wˆ Ty
(4)

y 4 1  y  We.
(5)

These equations describe the competition occurring within one process-
ing stage (cortical area) of the PC/BC model. This mechanism of compe-
tition is called divisive input modulation (DIM) and has been shown to
have excellent pattern recognition abilities on an artificial task (Spratling
et al., 2009).

Despite the simplicity of the model, simulating a large population of
neurons receiving input from a reasonably large image is computation-
ally demanding using the matrix multiplication method described by
Equations 4 and 5. Furthermore, individually specifying the synaptic
weight values for a large population of neurons can be inconvenient. For
an application, like a model of V1, in which neurons have RFs restricted
to a small fraction of the input image, and in which the same patterns of
weights are repeated at different spatial locations, it is possible to imple-
ment DIM in a more tractable manner using linear filtering and convo-
lution, as follows:

E  X A2 

k1

p

wˆ k  Yk
(6)

Yk 4 1  Yk  wk  E,
(7)

Where E, X, and Yk are two-dimensional arrays equal in size to the input
image that represent the error-detecting neuron responses, the input
stimulus, and the prediction neuron responses, respectively; wk is a two-
dimensional kernel representing the synaptic weights for a particular
class (k) of neuron; p is the total number of kernels;  represents cross-
correlation (which is equivalent to convolution without the kernel being
rotated 180°); and  represents convolution (which is equivalent to cross-

(W  )
S2 T

x
W
W

S1 T
(W  )

S2
S1
S1
S2

S2
S1
S1
S2
e
y
e
y

Figure 1.
The PC/BC model: a reformulation of predictive coding (Rao and Ballard, 1999)
thatcanbeinterpretedasaformofbiasedcompetitionmodel.Therectanglesrepresentpopu-
lationsofneurons,withylabelingpopulationsofpredictionneuronsandelabelingpopulations
of error-detecting neurons. The open arrows signify excitatory connections, the filled arrows
indicate inhibitory connections, the crossed connections signify a many-to-many connectivity
pattern between the neurons in two populations, the parallel connections indicate a one-to-
one mapping between the neurons in two populations, and the large shaded boxes with
rounded corners indicate different cortical areas or processing stages.

> Figure caption (from PDF text): Figure 1.
The PC/BC model: a reformulation of predictive coding (Rao and Ballard, 1999)
thatcanbeinterpretedasaformofbiasedcompetitionmodel.Therectanglesrepresentpopu-
lationsofneurons,withylabelingpopulationsofpredictionneuronsandelabelingpopulations
of error-detecting neurons. The open arrows signify excitatory connections, the filled arrows
indicate inhibitory connections, the crossed connections signify a many-to-many connectivity
pattern between the neurons in two populations, the parallel connections indicate a one-to-
one mapping between the neurons in two populations, and the large shaded boxes with
rounded corners indicate different cortical areas or processing stages.


This figure presents a schematic diagram illustrating the "PC/BC model," which is described as a reformulation of predictive coding interpreted as a form of biased competition model. The structure is organized into two main, large, shaded rectangular blocks representing distinct processing stages or cortical areas.

### 1. Overall Layout & Structure
The diagram is a complex neural circuit schematic, structured horizontally across two major processing stages labeled S1 and S2. These stages are enclosed in large, rounded-corner shaded boxes. The overall flow suggests a feedforward progression from S1 to S2, accompanied by complex recurrent and lateral connections between the populations within these stages.

### 2. Visual Components & Symbols
The schematic utilizes several distinct symbols to represent neuronal populations and connectivity:

**A. Neuronal Populations (Rectangles):**
Within each stage (S1 and S2), there are two primary rectangular blocks representing populations of neurons:
*   **Prediction Neurons:** Labeled with $e^{S1}$ and $e^{S2}$. These are depicted as vertical rectangles.
*   **Error-Detecting Neurons:** Labeled with $y^{S1}$ and $y^{S2}$. These are also depicted as vertical rectangles.

**B. Connectivity (Arrows and Lines):**
The connections between these populations are represented by various types of arrows:

*   **Excitatory Connections (Open Arrows):** Open, unfilled arrows signify excitatory connections. These are visible flowing from the prediction neurons ($e$) to other elements, and also between populations in a feedforward manner.
*   **Inhibitory Connections (Filled Arrows):** Filled, solid arrows indicate inhibitory connections. These are shown originating from the error-detecting neurons ($y$) and projecting to other elements.
*   **Many-to-Many Connectivity (Crossed Connections):** A specific pattern of crossed lines connects the prediction neurons ($e$) and error-detecting neurons ($y$) within each stage (S1 and S2). This signifies a many-to-many connectivity pattern between the neurons in these two populations.
*   **One-to-One Mapping (Parallel Connections):** Parallel lines are shown connecting the populations, indicating a one-to-one mapping between neurons in two populations.

**C. Inter-Stage Connectivity (Feedback/Lateral Loops):**
Crucially, there are large, thick lines forming complex feedback loops that span across the boundary between S1 and S2:
*   A thick, curved line originates from the lower part of the S1 structure and loops down to connect with the lower parts of the S2 structure, forming a large feedback loop.
*   A similar thick line originates from the lower part of S2 and loops back toward the structure in S1, completing a large recurrent loop.

### 3. Labels, Keys & Legends
**Stage/Area Labels:**
*   The left processing stage is labeled **S1**.
*   The right processing stage is labeled **S2**.

**Population Labels:**
*   Prediction Neuron Population in S1: $e^{S1}$
*   Error-Detecting Neuron Population in S1: $y^{S1}$
*   Prediction Neuron Population in S2: $e^{S2}$
*   Error-Detecting Neuron Population in S2: $y^{S2}$

**Connectivity Notation:**
*   The crossed connection pattern between the prediction and error populations in S1 is labeled $(\bar{W}^{S1})^T$.
*   The crossed connection pattern between the prediction and error populations in S2 is labeled $(\bar{W}^{S2})^T$.

### 4. Contextual Caption Integration
The caption clarifies the functional roles of the components:
*   **Rectangles:** Represent populations of neurons.
*   **$e$ Populations (Prediction Neurons):** These are the populations responsible for generating predictions.
*   **$y$ Populations (Error-Detecting Neurons):** These are the populations responsible for detecting prediction errors.
*   **Open Arrows:** Signify excitatory connections.
*   **Filled Arrows:** Indicate inhibitory connections.
*   **Crossed Connections ($\bar{W}^T$):** Signify a many-to-many connectivity pattern between the neurons in two populations.
*   **Parallel Connections:** Indicate a one-to-one mapping between neurons in two populations.
*   **Shaded Boxes (S1, S2):** Indicate different cortical areas or processing stages.

> Figure caption (from PDF text): Figure 1.
The PC/BC model: a reformulation of predictive coding (Rao and Ballard, 1999)
thatcanbeinterpretedasaformofbiasedcompetitionmodel.Therectanglesrepresentpopu-
lationsofneurons,withylabelingpopulationsofpredictionneuronsandelabelingpopulations
of error-detecting neurons. The open arrows signify excitatory connections, the filled arrows
indicate inhibitory connections, the crossed connections signify a many-to-many connectivity
pattern between the neurons in two populations, the parallel connections indicate a one-to-
one mapping between the neurons in two populations, and the large shaded boxes with
rounded corners indicate different cortical areas or processing stages.


This figure presents a schematic diagram illustrating the "PC/BC model," which is described as a reformulation of predictive coding interpreted as a form of biased competition model. The overall structure is a single, large block diagram representing a processing unit or cortical area ($\text{v}_1$).

### 1. Overall Layout & Structure
The diagram is contained within a single, large rectangular boundary with rounded corners, labeled $\text{v}_1$. Inside this boundary, the structure is organized linearly from left to right, depicting a flow of information through distinct functional populations. The schematic uses rectangular blocks to represent neuronal populations and various types of arrows to denote connectivity patterns between these populations.

### 2. Visual Components & Symbols
The diagram features three primary functional blocks connected sequentially:

*   **Input/Prediction Population (Left):** A rectangular block labeled 'e' represents a population of neurons. Two external input lines enter this block from the left, indicating incoming sensory or predictive signals.
*   **Connectivity/Interaction Layer (Center):** Between the 'e' and 'y' blocks is a central structure representing complex connectivity. This structure features two interconnected nodes (represented by small, stylized shapes) linked by multiple arrows:
    *   A thick, curved arrow labeled $\text{w}$ connects from the 'e' block towards the central structure.
    *   A thick, curved arrow labeled $\tilde{\text{w}}^{\text{T}}$ connects from the central structure towards the 'y' block.
    *   The central nodes themselves are connected to each other via complex, multi-directional arrows.
*   **Error Detection Population (Right):** A rectangular block labeled 'y' represents another population of neurons. An output line exits this block to the right, indicating processed or error signals leaving the $\text{v}_1$ area.

**Connectivity Details (Based on Caption Interpretation):**
The caption provides a key for interpreting the arrows:
*   Open arrows signify excitatory connections.
*   Filled arrows indicate inhibitory connections (though none are explicitly colored in the provided image, this is a defined convention).
*   Crossed connections signify a many-to-many connectivity pattern between neurons in two populations.
*   Parallel connections indicate a one-to-one mapping between neurons in two populations.

The central structure, with its complex interconnections involving $\text{w}$ and $\tilde{\text{w}}^{\text{T}}$, visually represents this complex, many-to-many connectivity pattern between the prediction ('e') and error detection ('y') populations.

### 3. Labels, Keys & Legends
**Internal Labels:**
*   $\text{v}_1$: Label for the entire processing block.
*   'e': Label for the left neuronal population (Prediction Neurons, as per caption).
*   'y': Label for the right neuronal population (Error-Detecting Neurons, as per caption).
*   $\text{w}$: Label associated with a connection pathway.
*   $\tilde{\text{w}}^{\text{T}}$: Label associated with another connection pathway.

**External Annotations:**
*   The input lines entering 'e' are unlabeled but represent external inputs.
*   The output line exiting 'y' is also unlabeled but represents the final output/error signal.

### 4. Data Trends & Details
As this is a schematic diagram and not a plot, there are no axes, data trends, or quantitative measurements to report.

### 5. Contextual Caption Integration
The caption identifies the components:
*   The rectangles ('e' and 'y') represent **populations of neurons**.
*   Population 'e' represents the **population of prediction neurons**.
*   Population 'y' represents the **population of error-detecting neurons**.
*   The entire shaded box ($\text{v}_1$) indicates a **cortical area or processing stage**.
*   The connectivity patterns (arrows and central structure) are interpreted as representing the functional relationships between these populations within the model.

T
W

x
W

V1

y
e

Figure2.
ThemodelofV1implementedusingPC/BC.Thepredictionneurons(labeledy)are
assumedtocorrespondtoV1simplecellsandtheresponseofoneoftheseneuronsisrecorded.
The RFs of these prediction neurons are determined by the definition of the weight matrix W.
Predictionneuronscompetetorepresenttheinputstimulusxviadivisivefeedback,whichacts
on the error-detecting neurons (labeled e) and is carried by connections from the prediction
neuronstotheerror-detectingneurons,whichhavestrengthproportionaltothecorresponding
reciprocal weights from the error-detecting neurons to the prediction neurons.

3532 • J. Neurosci., March 3, 2010 • 30(9):3531–3543
Spratling • Predictive Coding Model of V1


---

## Page 3

correlation with a kernel rotated by 180°). Note that Equation 7 repre-
sents a family of equations, one for each kernel.

The RF of a simple cell in primary visual cortex can be accurately
modeled by a two-dimensional Gabor function (Daugman, 1980, 1988;
Marcelja, 1980; Jones and Palmer, 1987; Lee, 1996). Hence the Gabor
function was used to define the weights of each kernel wk. A definition of
a Gabor function of the form proposed by Lee (1996) was used, which
includes a term to remove the DC response of the filter as follows:

g,,,	,
  exp

x2  y/2

22 cos
2y

 	

cos	 exp





2,
(8)

where   4 (pixels) was a constant that defined the SD of the Gaussian

envelope (which determines the spatial extent of the RF),  

1
2 was a

constant that defined the aspect ratio of the Gaussian envelope (which
determines the ellipticity of the RF),   6 (pixels) was a constant that
defined the wavelength of the sinusoid, 	 was the phase of the sinusoid,
and x  x cos(
)  y sin(
) and y  x sin(
)  y cos(
), where 
defined the orientation of the RF. Note that the size of the RF of a model
neuron is measured in pixels. This value should have a direct linear

relationship with the size of the RF of a cortical
cell measured in degrees of visual angle. Differ-
ent neurophysiological experiments are per-
formed with cells that have different RF sizes.
To simulate these different experiments, it
would be possible to scale parameters  and 
to fit the model to each specific cortical neuron.
Alternatively, it is possible to keep the model
fixed and change the size of the image. The
latter approach was taken in the simulations
reported in this article.

A family of 32 Gabor functions (Fig. 3a) with
eight orientations (
  0–157.5° in steps of
22.5°) and four phases (	  0, 90, 180, and
270°) were used to define the RFs of the neu-
rons in the model. The cross-correlation and
convolution performed in Equations 6 and 7
mean that neurons with these RFs are repro-
duced at every pixel location in the image, and
consequently, that the size of the population of
V1 cells simulated varies with image size. For an a  b pixel image, the
model simulates the response of 32ab prediction neurons (for the exper-
iments reported in Results, an image is typically 51  51 pixels, so
80,000 prediction neurons were simulated).

The PC/BC model requires non-negative weights. Hence the weights
were separated into distinct ON and OFF channels, which represented
the positive and negative parts of the Gabor function using separate sets
of non-negative weights (Fig. 3b). These separate channels result in the
model illustrated in Figure 4 and described by the following equations:

Eo  Xo A2 

k1

p

wˆ ok  Yk
(9)

Yk 4 1  Yk 

o wok  Eo,
(10)

where o 
 [ON,OFF]. The kernels wON,k and wOFF,k were normalized so
that sum of all the weights in both the ON and OFF channel was equal to
, and wˆ ON,k and wˆ OFF,k were normalized so that the maximum value
across both the ON and OFF channel was equal to .

For each new input image, the prediction neuron responses (Y) were
initialized to zero, and then the above equations were iterated to record
the response of Y for a number of iterations (t). This recording time, t,
was the only parameter (apart from the input image) that was varied
during the experiments reported in Results. The response of the predic-
tion neurons on the first iteration is given by the following:

Yk 

1
2

o wok  Xo.
(11)

The bracketed term on the right-hand side of Equation 11 represents the
output produced by a set of linear filters when applied to the image. This

initial, linear, response is scaled by the ratio

1
2. To ensure that this initial

transient did not dominate the recorded responses, values of 1  0.0001
and 2  50 were used. Given the large value of  used here, these values
are similar to those used previously to simulate the interactions between
attention and long-range lateral connections in V1 (De Meyer and
Spratling, 2009).

Results from neurophysiological studies are generally presented by
showing how the mean evoked firing rate of the recorded neuron changes
as a particular parameter of the input stimulus is varied. Results from the
model were generated in the same way by recording the activity of a single
prediction neuron, in response to each input image, for a number of
iterations (t) of the PC/BC algorithm. The average response was then
calculated by simply taking the mean activity of the recorded prediction
neuron over the t iterations that the stimulus was presented. As for typical
physiological experiments, the stimulus parameters other than the one
being varied during the experiment were matched to the preferred pa-

Figure 3.
The synaptic weights used in the PC/BC model of V1. a, A family of 32 Gabor functions (8 orientation and 4 phases)
usedtodefinetheRFsoftheneuronsinthemodel.b,Theactualsynapticweightsofthemodelneuronswerecreatedbyseparating
thepositiveandnegativepartsoftheGaborfunctionintoseparate(non-negative)ONandOFFweights(shownforthebottomright
Gaborfunctiononly).EachGaborkernelis2121pixels,andhenceeachpredictionneuroninthemodelreceives21212
882 synaptic weights.

> Figure caption (from PDF text): Figure 3.
The synaptic weights used in the PC/BC model of V1. a, A family of 32 Gabor functions (8 orientation and 4 phases)
usedtodefinetheRFsoftheneuronsinthemodel.b,Theactualsynapticweightsofthemodelneuronswerecreatedbyseparating
thepositiveandnegativepartsoftheGaborfunctionintoseparate(non-negative)ONandOFFweights(shownforthebottomright
Gaborfunctiononly).EachGaborkernelis2121pixels,andhenceeachpredictionneuroninthemodelreceives21212
882 synaptic weights.


This figure, labeled as "Figure 3," illustrates the synaptic weights used in a PC/BC model of V1. It is divided into two main parts, labeled **a** and **b**, presented side-by-side.

### Panel a: Gabor Functions
Panel **a** displays a grid of 32 distinct visual kernels, which are identified in the caption as "A family of 32 Gabor functions."

*   **Layout:** The kernels are arranged in a $4 \times 8$ grid (4 rows and 8 columns).
*   **Visual Content:** Each individual kernel is a small, grayscale image patch. These patches represent Gabor functions, which are characterized by specific orientations and phases. The kernels exhibit varying patterns of light and dark intensity, corresponding to different spatial frequencies and orientations (e.g., horizontal, vertical, diagonal gratings).
*   **Dimensions:** The caption specifies that each Gabor kernel is $21 \times 21$ pixels.

### Panel b: Separated Synaptic Weights
Panel **b** shows a representation of the actual synaptic weights derived from the Gabor functions in Panel **a**.

*   **Layout:** This panel is positioned to the right of Panel **a**, connected by a large black arrow pointing from the grid in **a** towards the representation in **b**.
*   **Visual Content:** Panel **b** displays two small, grayscale patches side-by-side. These represent the separation of the Gabor function into positive and negative components:
    *   The left patch is labeled **ON**.
    *   The right patch is labeled **OFF**.
*   **Color/Intensity Scale:** A color bar or legend is provided adjacent to Panel **b**, indicating the range of synaptic weights. This scale ranges from $-0.01$ (darker/negative) to $0.01$ (lighter/positive), with a neutral gray representing zero weight.
*   **Contextual Detail:** The caption clarifies that the ON and OFF weights are derived by separating the positive and negative parts of a specific Gabor function (shown for the bottom-right kernel in Panel **a**).

### Structural Relationships and Flow
A large, bold black arrow connects the entire array in Panel **a** to the representation in Panel **b**, indicating a transformation or derivation process: the Gabor functions (Panel **a**) are used to create the separated ON and OFF synaptic weights (Panel **b**).

### Summary of Annotations
*   **Labels:** The panels are labeled **a** and **b**.
*   **Text Annotations (from Caption):** The caption identifies the content: "a, A family of 32 Gabor functions (8 orientation and 4 phases) used to define the RFs of the neurons in the model." and "b, The actual synaptic weights of the model neurons were created by separating the positive and negative parts of the Gabor function into separate (non-negative) ON and OFF weights."
*   **Scale Bar:** The scale bar in Panel **b** is labeled with values $0.01$ and $-0.01$.

> Figure caption (from PDF text): Figure 3.
The synaptic weights used in the PC/BC model of V1. a, A family of 32 Gabor functions (8 orientation and 4 phases)
usedtodefinetheRFsoftheneuronsinthemodel.b,Theactualsynapticweightsofthemodelneuronswerecreatedbyseparating
thepositiveandnegativepartsoftheGaborfunctionintoseparate(non-negative)ONandOFFweights(shownforthebottomright
Gaborfunctiononly).EachGaborkernelis2121pixels,andhenceeachpredictionneuroninthemodelreceives21212
882 synaptic weights.


### 1. Overall Layout & Structure
The diagram is a complex, multi-stage block diagram representing signal flow through the visual cortex area designated as V1. The structure shows inputs feeding into distinct processing pathways (ON and OFF), which then interact with a set of output neurons ($\text{Y}$).

### 2. Visual Components & Symbols
**Inputs (Left Side):**
*   The input signal, labeled **I**, enters the system from the far left. It is connected to two distinct input processing blocks via arrows originating from a central point marked with an asterisk ($\text{*}$).
*   These two input paths are associated with small, square-like blocks containing a central circle (representing receptive fields or filters).
*   The top input path leads to a block labeled $\text{X}_{\text{ON}}$.
*   The bottom input path leads to a block labeled $\text{X}_{\text{OFF}}$.

**Processing Layers (Inside V1):**
The core processing within the shaded box $\text{V1}$ involves parallel pathways:

*   **ON Pathway (Top):**
    *   The signal from $\text{X}_{\text{ON}}$ feeds into a block labeled $\text{E}_{\text{ON}}$.
    *   $\text{E}_{\text{ON}}$ is connected to a series of stacked, rectangular blocks representing the receptive fields or kernels. These kernels are depicted as varying shapes (some solid black ovals, some outlined) and appear to be arranged in a sequence.
    *   An arrow flows from the output of this kernel stack towards the final output layer $\text{Y}$.

*   **OFF Pathway (Bottom):**
    *   The signal from $\text{X}_{\text{OFF}}$ feeds into a block labeled $\text{E}_{\text{OFF}}$.
    *   $\text{E}_{\text{OFF}}$ is also connected to a series of stacked, rectangular blocks representing kernels. These kernels are visually similar to those in the ON pathway but are positioned below it.
    *   An arrow flows from this kernel stack towards the final output layer $\text{Y}$.

**Interactions and Outputs:**
*   **Cross-Pathway Connections:** There are bidirectional arrows connecting the $\text{E}_{\text{ON}}$ block and the $\text{E}_{\text{OFF}}$ block, indicating interaction or cross-talk between the ON and OFF pathways.
*   **Output Layer ($\text{Y}$):** A vertical stack of rectangular blocks represents the output neurons, labeled $\text{Y}$.
*   **Feedback/Interaction:** The kernel stacks associated with both the ON and OFF pathways have arrows pointing towards or interacting with the $\text{Y}$ layer. Furthermore, there is a distinct arrow originating from the kernel stack in the bottom right corner that loops back towards the $\text{Y}$ layer, suggesting a complex interaction or feedback mechanism.

### 3. Labels, Keys & Legends
*   **Main Container:** $\text{V1}$ (The visual cortex area).
*   **Input Labels:** $\text{I}$, $\text{X}_{\text{ON}}$, $\text{X}_{\text{OFF}}$.
*   **Intermediate Processing Labels:** $\text{E}_{\text{ON}}$, $\text{E}_{\text{OFF}}$.
*   **Output Label:** $\text{Y}$.
*   **Annotations:** Asterisks ($\text{*}$) are used near the input stage and within the kernel stacks, likely indicating specific points of processing or weight application.

### 4. Data Trends & Details
As this is a schematic diagram and not a plot, there are no quantitative axes or data trends to describe. The visual detail focuses on the *structure* of the connections and the representation of the kernels (the stacked rectangles).

### 5. Contextual Caption Integration
The caption clarifies that the diagram illustrates "The synaptic weights used in the PC/BC model of V1."
*   The kernels shown are derived from a "family of 32 Gabor functions (8 orientation and 4 phases)."
*   The caption specifies that the synaptic weights are separated into "positive and negative parts of the Gabor function into separate (non-negative) ON and OFF weights," which corresponds to the $\text{X}_{\text{ON}}$ and $\text{X}_{\text{OFF}}$ pathways.
*   The kernels are noted to be $21 \times 21$ pixels, leading each prediction neuron in the model ($\text{Y}$) to receive $21 \times 21 \times 2 \times 882$ synaptic weights (the factor of 2 likely accounts for ON/OFF separation).

Figure4.
ThePC/BCmodelofV1implementedusingconvolutionandwithseparateONand
OFF channels. The input image I is preprocessed by convolution with a circular-symmetric on-
center/off-surround kernel (to generate the input to the ON channel of the V1 model) and a
circular-symmetric off-center/on-surround kernel (to generate the input to the OFF channel of
the V1 model). The prediction neurons (labeled Y), which represent V1 simple cells, generate
theresponsesthatwererecordedduringtheexperiments.Theseresponsesweregeneratedby
convolvingtheoutputsofthe(ONandOFFchannelsofthe)error-detectingneurons(labeledE)
with (the ON and OFF channels of) a number of kernels representing V1 RFs. This convolution
processeffectivelyreproducesthesameRFsateverypixellocationintheimage.Theresponses
oftheerror-detectingneuronsareinfluencedbydivisivefeedbackfromthepredictionneurons,
which is also calculated by convolving the prediction neuron outputs with the weight kernels.

Spratling • Predictive Coding Model of V1
J. Neurosci., March 3, 2010 • 30(9):3531–3543 • 3533


---

## Page 4

rameters of the neuron under test (e.g., the stimulus was centered over
the RF at the preferred orientation, spatial frequency, temporal fre-
quency, etc., of the recorded neuron). Furthermore, the range of gray-
scale values in the input image I were set equal to the fractional Michelson
contrast used for the presentation of stimuli in the corresponding phys-
iological experiment, if this value was reported.

The LGN model (image preprocessing). The input to the model of V1,
described above, was an input image (I) preprocessed by convolution
with a LoG (Laplacian-of-Gaussian) filter (l) with SD equal to 1. This is
virtually identical with the DoG (difference-of-Gaussians) filter that has
traditionally been used to model circular RFs in LGN. The output from
this filter was subject to a saturating nonlinearity, such that

X  tanh	2I  l
.
(12)

The positive and rectified negative responses were separated into two
images XON and XOFF simulating the outputs of cells in retina and LGN
with circular-symmetric on-center/off-surround and off-center/on-
surround RFs. This preprocessing is illustrated in Figure 4. Consistent
with neurophysiological data (Reid and Alonso, 1995), the ON-center
LGN neurons provided input to the ON subfield of the model V1 simple
cells, whereas the OFF-center LGN neurons provided input to the OFF
subfield of the model V1 neurons.

In most experiments, static stimuli were used. Hence I and the values
of XON and XOFF remained constant throughout each experiment. How-
ever, in some experiments, it was necessary to simulate moving stimuli.
To do this, the input image was changed, and new XON and XOFF values
were calculated, for each iteration of the PC/BC algorithm. The amount
the input image changed between consecutive iterations reflected the
speed of the temporally changing stimulus. For example, to simulate an
object moving at 10 pixels per iteration, the object would be displaced by
10 pixels in one image compared with the previous one. Since moving
stimuli in the experiments reported here were sinusoidal gratings, speed
was measured in cycles per iteration, where the number of cycles refers to
the phase shift between sinusoids in consecutive images.

Code. Software, written in MATLAB, which implements the PC/BC
model described above is available at http://www.corinet.org/mike/
code.html.

Results
The following sections present simulations of a number of exper-
iments performed to assess the response properties of cells in V1.
These experiments cover basic tuning preferences (orientation
tuning, size tuning, spatial frequency tuning, and temporal fre-
quency tuning), suppression attributable to additional stimuli
appearing within the classical receptive field (cross-orientation
suppression) andoutsidetheclassicalreceptivefield(surroundsup-
pression, and suppression attributable to textured surrounds), and
facilitation attributable to flankers.

Basic tuning properties
Simple cells in V1 are selective for a number of stimulus proper-
ties such as color, orientation, direction of motion, spatial fre-
quency, temporal frequency, eye of origin, binocular disparity,
and stimulus size and location. The model presented here is re-
stricted to grayscale pixel values coming from a single image and
has no mechanism for distinguishing direction of motion. How-
ever, it generates behavior that closely matches typical tuning
properties of V1 cells for those properties that it does model,
namely, orientation, spatial frequency, temporal frequency,
and size.

Orientation tuning was measured by presenting, at various
orientations, a sinusoidal grating centered over the RF of the
recorded neuron (Fig. 5a). Both the V1 neuron and the model
neuron showed selectivity for a particular stimulus orientation,
with the response falling quickly as the orientation of the stimulus
diverged from the preferred orientation. This selectivity was

unaltered by stimulus contrast, with a stimulus far from the pre-
ferred orientation producing a weak response even when pre-
sented at high contrast. Orientation tuning in the model was
partially attributable to the alignment of the strongest afferent
weights along a specific orientation. However, tuning was sharp-
ened by the competition occurring between neurons in the
model. This can be seen by observing the orientation tuning pro-
duced when competition was removed from the model (Fig. 5a,
inset). Without competition, the neuron had the same orienta-
tion preference but was much more broadly tuned producing a
strong response (42% of the maximum) at all orientations,
even at 90° from the preferred orientation (data not shown).

Both V1 and the model show the same pattern of results when
tested with circular sinusoidal gratings of various diameters (Fig.
5b). At small stimulus diameters, the response increased with
increasing stimulus size. However, it reached a peak at a certain
diameter, defining the summation field (SF) (Angelucci et al.,
2002), after which the response became increasingly suppressed
before reaching a plateau at large stimulus diameters. In the
model, the initial increase in response with stimulus size is attrib-
utable to more of the RF of the recorded neuron being stimulated.
However, as the stimulus becomes larger, more neurons neigh-
boring the recorded neuron also become stimulated. These neu-
rons engage in a competition to represent the input, and this
ongoing competition reduces the recorded response. The plateau
is reached when all the neighboring neurons that have RFs that
overlap with the recorded neuron are stimulated by the input. For
both V1 and the model, response decreased as the inner diameter
of an annular grating increased (Fig. 5b). In both cases, response
converged to a minimum at a diameter slightly larger than the
diameter of the SF. In the model, this behavior is caused by the
partial activation of the RF of the recorded neuron at small diam-
eters, and a reduction in the area of the RF stimulated with in-
creasing diameter. In V1, the extent of the SF is known to change
with contrast (Fig. 5c, top). The model shows a similar pattern of
response (Fig. 5c, bottom), but the expansion of the SF in the
model is much smaller than in V1.

Spatial frequency tuning was measured by presenting opti-
mally oriented sinusoidal gratings with different wavelengths.
The model produced behavior in close agreement with the em-
pirical data (Fig. 5d), with a sharp peak in response to interme-
diate spatial frequencies. The weak response of the model neuron
at low spatial frequencies is attributable to weak input from the
LGN since center-surround cells produce little response to small
contrast gradients. The small response at high spatial frequencies
results from the stimulus only partially matching the RF of the
recorded neuron and hence only partially activating it. The high-
frequency stimulus also partially activates more neurons, and
hence there is increased competition further suppressing the re-
corded response. In both V1 and the model, spatial frequency
preference was unaffected by stimulus contrast (Fig. 5e).

Increasing the temporal frequency of a drifting grating re-
duced the response of a neuron both in V1 and in the model (Fig.
5f). In the model, this effect is attributable to a fast moving grat-
ing only matching the RF of the recorded neuron part of the time
and hence producing a weaker temporally averaged response. A
fast-moving grating also activates many other neurons (since the
stimulus matches the RFs of different neurons at different times),
and hence there is increased competition further suppressing the
response of the recorded neuron. In effect, the response to the
stimulus becomes distributed across many neurons and the sum
of the responses of all neurons in the model remains almost con-
stant with changing drift rate (Fig. 5f, inset).

3534 • J. Neurosci., March 3, 2010 • 30(9):3531–3543
Spratling • Predictive Coding Model of V1


---

## Page 5

Cross-orientation suppression
The previous section considered behavior when a single grating
was present in the RF of the recorded neuron. When a second
grating (the mask) is superimposed on the stimulus, this leads to
partial suppression of the response (Fig. 6a). For both V1 and the
model, suppression was weakest for mask orientations close to
the preferred orientation of the neuron, and strongest for masks
presented at orientations that did not evoke a response when such
a grating was presented in isolation. In the model, neurons rep-
resenting different orientations at the same spatial location have
overlapping RFs and hence compete to respond to stimuli ap-
pearing within this overlapping region. When the stimulus con-
sists of two gratings with significantly different orientations, the
two sets of neurons representing these orientations are both ac-
tive, but the ongoing competition to respond to the inputs they
share reduces the response of neurons in both sets. When the
stimulus consists of two gratings at similar orientations, compe-
tition is even stronger as the neurons representing similar orien-
tation at the same location have RFs that overlap more. However,
the effective contrast of the stimulus also increases, and hence the
recorded neuron receives a stronger afferent input, which in-
creases its response despite the competition.

Figure 6, b and c, show the effects of changing the contrasts of
two superimposed orthogonal gratings. In both V1 and the
model, increasing the contrast of the optimally orientated grating
increases the response, and the response rises more quickly for
lower mask contrasts. Equivalently, increasing the contrast of the
mask reduces the response. In the model, the former effect is

attributable to increasing the afferent input to the recorded neu-
ron as the contrast of the grating at the preferred orientation
increases. The latter effect is attributable to increased competi-
tion from other neurons that receive increased afferent input as
the contrast of the mask increases.

Changing the spatial frequency of an orthogonal mask also
affects the strength of the suppression generated (Fig. 6d). In the
model, neurons show spatial frequency tuning (Fig. 5d). Hence
neurons selective to the orientation of the mask were only stim-
ulated, and hence only generated suppression, when the spatial
frequency of the mask was close to the preferred spatial frequency
of those neurons.

Stimuli presented at high temporal frequencies also generate
weak responses in the model and in V1 (Fig. 5f). It might there-
fore be expected that a mask presented at a high temporal fre-
quency would be ineffective (Carandini et al., 2002). However,
this is not the case (Fig. 6e). Even when the temporal frequency of
the mask grating was high, the response to the plaid stimulus was
much weaker than the response to the optimal grating, and hence
there was strong cross-orientation suppression. This occurred
even at temporal frequencies in which the mask, presented alone,
produced very little response in a neuron tuned to the orientation
of the mask (Fig. 5f). However, the total activity across all neu-
rons remains approximately constant with temporal frequency
(Fig. 5f, inset); hence the total inhibition received also remains
approximately constant. The current model thus suggests that it
is only the distribution of the source of suppression, rather than
its total strength, that changes with temporal frequency and this

Response

40

20

Orientation (degrees)

50
0
−50

0
0

100

75

50

25

0.25 0.5 0.75 1 1.25 1.5
Diameter (degrees)
Diameter (degrees)
0
0
1
2 3
4
5 6 7

50

100

150

Spatial Freq. (cycles/degree)

0.3
1
2
10
0

20

40

60

20

40

30

20

10

0

Spatial Freq. (cycles/degree)

0.1
0.8
0.3

20

10

0

Drift Rate (cycles/second)

5
10
2
20

−50
0
50
0

10

20

Orientation (degrees)

Response

x10−3

−50
0
50
0

2

4

6

8

x 10

−3

5 10 15 20 25 30
0

2

4

6

8x 10
−3

Diameter (pixels)

5 10 15 20 25 30
0

5

10

15

Diameter (pixels)

x10−3

0.05
0.1
0.2
0.5
0

5

10

Spatial Freq. (cycles/pixel)

x10−3

0.1
0.2
0.3
0

10

20

Spatial Freq. (cycles/pixel)

x10−3

0.005
0.05
0.5
0

1

2

3

4

5

x 10

−3

Drift Rate (cycles/iteration)

0.005
0.05
0.5
0

2

4

6

8

10

a

b

c
d
e
f

Figure5.
Basictuningproperties.ThetoprowshowsneurophysiologicaldatafromrepresentativesinglecellsinV1,andthebottomrowshowscorrespondingsimulationresults.a,Responseas
afunctionofgratingorientationrelativetothepreferredorientationoftheneuron.NeurophysiologicaldataforasimplecellincatV1[adaptedfromSkottunetal.(1987),theirFig.3a].Thethickness
of each line corresponds to the contrast of the stimulus used as follows: 5% (thin), 20% (medium), and 80% (thick). The inset to the simulation data shows the response of the model without
competition, created by recording the linear response generated at the first iteration of the algorithm (see Materials and Methods). b, Response as a function of the diameter of a circular grating
(filledcircles)andasafunctionoftheinnerdiameterofanannulargrating(opencircles).NeurophysiologicaldataforacellinprimateV1[adaptedfromJonesetal.(2001),theirFig.1].c,Response
asafunctionofgratingdiameterwithvariablegratingcontrast.ShownareneurophysiologicaldataforacellinprimateV1[adaptedfromCavanaughetal.(2002a),theirFig.8].Thethicknessofeach
linecorrespondstothecontrastofthestimulususedasfollows:6%(thinnest),13,25,50,and100%(thickest).d,Responseasafunctionofgratingspatialfrequency.Shownareneurophysiological
dataforacellinprimateV1[adaptedfromWebbetal.(2005),theirFig.2a].e,Responseasafunctionofgratingspatialfrequencywithvariablegratingcontrast.Shownareneurophysiologicaldata
forasimplecellincatV1[adaptedfromSkottunetal.(1987),theirFig.4a].Thethicknessofeachlinecorrespondstothecontrastofthestimulususedasfollows:5%(thin),20%(medium),and80%
(thick).f,Responseasafunctionofgratingtemporalfrequency.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3c].Theinsettothesimulation
data shows the response summed over all neurons within 11 pixels of the neuron recorded in the main figure.

Spratling • Predictive Coding Model of V1
J. Neurosci., March 3, 2010 • 30(9):3531–3543 • 3535



### Overall Layout & Structure
The figure consists of four panels:
1. **Top-Left Panel:** A line graph showing a relationship between orientation and response.
2. **Top-Right Panel:** A line graph showing a relationship between diameter and response, featuring two distinct y-axes.
3. **Bottom-Left Panel:** A line graph showing a relationship between orientation and response, similar in structure to the top-left panel.
4. **Bottom-Right Panel:** A line graph showing a relationship between diameter (in pixels) and response, also featuring two distinct y-axes.

### Visual Components & Symbols
All panels utilize standard Cartesian coordinate systems with lines connecting data points to illustrate trends.

### Labels, Keys & Legends
**Panel 1 (Top-Left):**
*   **X-axis Label:** Orientation (degrees)
*   **Y-axis Label:** Response

**Panel 2 (Top-Right):**
*   **X-axis Label:** Diameter (degrees)
*   **Left Y-axis Label:** (No explicit label visible, but scale runs from 0 to 100)
*   **Right Y-axis Label:** (No explicit label visible, but scale runs from 0 to 150)

**Panel 3 (Bottom-Left):**
*   **X-axis Label:** Orientation (degrees)
*   **Y-axis Label:** Response ($\times 10^{-3}$)

**Panel 4 (Bottom-Right):**
*   **X-axis Label:** Diameter (pixels)
*   **Left Y-axis Label:** ($\times 10^{-3}$) (Scale runs from 0 to $\approx 8$)
*   **Right Y-axis Label:** (Scale runs from 0 to $\approx 1.5$)

### Data Trends & Details

**Panel 1 (Top-Left):**
*   Shows a unimodal, bell-shaped curve peaking around $0^\circ$ orientation.
*   The response starts low near $-50^\circ$, rises sharply to a maximum around $45$ units at $0^\circ$, and then decreases symmetrically towards $-50^\circ$.
*   Two distinct curves are present, one peaking higher (around 45 units) and another lower (peaking around 20 units).

**Panel 2 (Top-Right):**
*   Displays two curves plotted against Diameter (degrees).
*   The curve associated with the left Y-axis shows a rapid increase, peaking near $100$ units around $0.75^\circ$, followed by a decrease.
*   The curve associated with the right Y-axis shows a generally lower response, starting around $50$ units at $0.25^\circ$, decreasing to a minimum near $10$ units around $1.25^\circ$.

**Panel 3 (Bottom-Left):**
*   Shows two curves plotted against Orientation (degrees).
*   Both curves exhibit a clear, sharp peak centered at $0^\circ$.
*   The upper curve reaches a maximum response of approximately $20 \times 10^{-3}$ at $0^\circ$.
*   The lower curve reaches a maximum response of approximately $15 \times 10^{-3}$ at $0^\circ$.
*   A small inset graph is present within this panel, showing a very low response curve peaking slightly above $0^\circ$ with a maximum value around $7 \times 10^{-3}$.

**Panel 4 (Bottom-Right):**
*   Displays two curves plotted against Diameter (pixels).
*   The curve associated with the left Y-axis shows a peak response of approximately $3.5 \times 10^{-3}$ around $10$ pixels, followed by a decline.
*   The curve associated with the right Y-axis shows a response that peaks around $1.2$ units near $5$ pixels and then gradually decreases.



**1. Overall Layout & Structure:**
The figure consists of a single plot area containing multiple data series represented by distinct lines. The structure is a standard Cartesian coordinate graph.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Data Series:** There are at least four distinct data series plotted, each represented by a line connecting discrete data points. These lines appear to be color-coded or differentiated, although specific colors are not discernible in this grayscale description.
*   **Data Points:** Each line is marked by specific data points corresponding to the values on the axes.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled "Diameter (degrees)". The tick marks are visible at 0, 1, 2, 3, 4, 5, 6, and 7.
*   **Y-Axis Labels:** There are two sets of vertical axis labels, suggesting dual y-axes or different scales for the plotted data.
    *   The left vertical axis has major tick marks labeled 0, 50, 100, and 150.
    *   The right vertical axis has major tick marks labeled 20, 40, and 60 (though the full scale is not entirely clear).
*   **Annotations:** There are no visible legends or explicit keys defining which line corresponds to which variable, although the context suggests multiple conditions are being compared.

**4. Data Trends & Details:**
The data shows a general trend of increasing values as the diameter increases from 0 to approximately 3 degrees, followed by a gradual decrease or plateauing for larger diameters.

*   **Highest Curve (Top Line):** This curve starts near zero at 0 degrees, rises sharply to a peak around 1.5–2 degrees (reaching approximately 140 on the left y-axis), and then gradually declines, ending around 85–90 at 7 degrees.
*   **Second Highest Curve:** This line also rises steeply, peaking around 2–3 degrees (reaching approximately 105 on the left y-axis), and then shows a moderate decline, ending around 80 at 7 degrees.
*   **Third Curve:** This line shows a more moderate rise, peaking around 2–3 degrees (reaching approximately 75 on the left y-axis), and then declines more steadily, ending around 40 at 7 degrees.
*   **Lowest Curve:** This line shows the lowest values, rising to a peak around 2–3 degrees (reaching approximately 50 on the left y-axis), and then declines slowly, ending around 30 at 7 degrees.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided to integrate, so no interpretation regarding cell types or feedback loops can be made based on external context. The figure strictly displays quantitative relationships between Diameter (degrees) and the measured parameter(s).



**1. Overall Layout & Structure:**
The figure consists of a single Cartesian coordinate plot, featuring two axes and one plotted data series represented by discrete points connected by lines.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal (x-axis) and a vertical (y-axis).
*   **Data Points:** Several distinct data points are marked on the plot. These points appear to be connected by a line, forming a curve that peaks and then declines.
*   **Scale Markers:** Tick marks are present along both axes, indicating numerical values.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled "Spatial Freq. (cycles/degree)".
*   **Y-Axis Label:** The vertical axis does not have a fully legible label in the provided crop, but numerical markings are present.
*   **Numerical Annotations:**
    *   The x-axis displays values such as 0.3, 1, 2, and 10 (with intermediate ticks).
    *   The y-axis displays values such as 0, 20, 40, and 60 (with intermediate ticks).

**4. Data Trends & Details:**
The plot shows a clear unimodal distribution:
*   At the lowest visible x-value (0.3 cycles/degree), the data point is low, near 5 on the y-axis scale.
*   The value increases sharply as the spatial frequency increases to 1 cycle/degree, reaching approximately 20 on the y-axis.
*   The curve continues to rise steeply, reaching its maximum peak at an x-value of 2 cycles/degree. The corresponding y-value for this peak is approximately 68 (based on the visible scale).
*   Following the peak, the data points decrease rapidly. At 10 cycles/degree, the value drops significantly to a low level, near 5 on the y-axis.
*   The trend suggests a peak sensitivity or response centered around 2 cycles/degree.

**5. Contextual Caption Integration:**
No specific contextual caption text is provided to interpret the meaning of the plotted data points (e.g., what the y-axis represents, such as firing rate or contrast sensitivity). The figure title/label provided is "Spatial Freq. (cycles/degree)".



**1. Overall Layout & Structure:**
The figure is a 2D line graph, presenting quantitative data across a continuous range on the x-axis. The plot area is dominated by two curves, each marked with data points.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Curves/Lines:** Two distinct curves are plotted: one appearing higher and more peaked, and another lower and less pronounced.
*   **Data Points:** Both curves are marked with discrete data points connected by lines, indicating measured values at specific spatial frequencies.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled "Spatial Freq. (cycles/degree)".
*   **Y-Axis Labels:** There are two sets of y-axis labels, suggesting dual Y-axes or a shared scale with annotations for different metrics. The left y-axis has numerical markings (e.g., 0, 10, 20, 30, 40). The right y-axis has numerical markings (e.g., 10, 20, 30).
*   **Annotations:** The figure includes a partial label on the right side, which appears to be part of a legend or axis annotation, showing values like "20" and "30".

**4. Data Trends & Details:**
*   **X-Axis Range:** The spatial frequency ranges from approximately 0.1 to 0.8 cycles/degree.
*   **Upper Curve (Higher Amplitude):** This curve starts low, rises steeply to a peak around 0.3 cycles/degree (reaching approximately 45 on the left y-axis scale), and then declines sharply, dropping back down towards zero by 0.8 cycles/degree.
*   **Lower Curve (Lower Amplitude):** This curve remains at a much lower amplitude throughout the range. It shows an initial rise, peaks around 0.25 cycles/degree (reaching approximately 23 on the right y-axis scale), and then gradually decreases, leveling off near zero by 0.8 cycles/degree.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no elements can be identified based on external context. The figure visually compares two different responses (represented by the two curves) as a function of spatial frequency.



### Panel (a): Drift Rate vs. Cycles/Second Plot
Panel (a) is a scatter plot with connected data points, illustrating the relationship between two variables.

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to approximately 25, though the tick marks are not fully labeled in the provided crop.
    *   The **X-axis** is explicitly labeled as "Drift Rate (cycles/second)" and displays values at 1, 2, 3, 5, 10, and 20.
*   **Data Trend:** A curve is plotted connecting several data points:
    *   The plot starts high, with a point near $x=1$ and $y \approx 20$.
    *   The curve rises sharply to a peak around $x=2$, where the y-value is at its maximum (approximately 25).
    *   The curve then drops steeply, passing through a point near $x=3$ with a y-value around 10.
    *   The decline continues rapidly, reaching near zero values for $x=5$, $x=10$, and $x=20$.

### Panel (b): Drift Rate vs. Cycles/Iteration Plot
Panel (b) is a more complex visualization, featuring a main plot and an inset graph.

#### Main Plot (Panel b)
*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to approximately 5, marked in units of $10^{-3}$ (i.e., $\times 10^{-3}$).
    *   The **X-axis** is labeled as "Drift Rate (cycles/iteration)" and displays values at 0.005, 0.05, and 0.5.
*   **Data Trend:** A curve is plotted showing a decreasing trend:
    *   The plot starts at $x=0.005$ with a y-value around 4.8 (or $4.8 \times 10^{-3}$).
    *   The curve drops significantly as the drift rate increases, passing through a point near $x=0.05$ with a y-value around 1.2 (or $1.2 \times 10^{-3}$).
    *   The curve continues to decrease, leveling off near $x=0.5$ at a very low y-value (approximately $0.4 \times 10^{-3}$).

#### Inset Graph (Within Panel b)
An inset graph is positioned in the upper right quadrant of Panel (b).

*   **Axes:**
    *   The **Y-axis** ranges from 0 to 10, with tick marks at intervals of 2.
    *   The **X-axis** ranges from 0 to 0.5, with tick marks at intervals of 0.05.
*   **Data Trend:** This inset shows a relatively flat, slightly increasing trend:
    *   The data points hover around $y=7$ to $y=8$. The line appears mostly horizontal, suggesting stability across the displayed range of the x-axis.

### Structural Elements
Below Panel (b), there is a horizontal bar graphic, which appears to be a schematic representation:
*   This bar consists of alternating vertical stripes. The left section is shaded in a dark gray/black, while the right section is shaded in a lighter gray. This structure suggests a division or transition between two states or regions, possibly related to the dynamics described in the plots above.



**1. Overall Layout & Structure:**
The figure consists primarily of a single, large set of overlaid line plots. There are two distinct y-axes indicated, suggesting that the data might be normalized or presented in different units/scales. The x-axis is common to all plotted lines.

**2. Visual Components & Symbols:**
*   **Axes:** The horizontal axis (x-axis) is labeled "Diameter (pixels)". The vertical axes are scaled differently.
*   **Data Curves:** There are multiple distinct curves plotted, each represented by a different marker shape (solid circle $\bullet$ and open circle $\circ$).
*   **Markers:** The legend indicates two types of markers: a solid black circle ($\bullet$) and an open white circle ($\circ$).
*   **Inset Images:** Below the main plot area, there are three small grayscale images arranged horizontally. These appear to be examples of stimuli or receptive field responses, showing concentric rings or patterns.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** "Diameter (pixels)"
*   **Y-Axes Labels:** There are two vertical axes. The left y-axis is labeled with units of $\times 10^{-3}$ (ranging from 0 to 15). The right y-axis is present but lacks a clear label in the visible portion of the image, though it shares the same vertical space.
*   **Legend:** A small legend is present near the left side of the plot area, showing:
    *   A solid black circle ($\bullet$) corresponding to one data series.
    *   An open white circle ($\circ$) corresponding to another data series.

**4. Data Trends & Details (Line Plots):**
The plots show several distinct curves, suggesting different conditions or parameters are being tested.

*   **X-Axis Range:** The diameter ranges from approximately 2 pixels up to 30 pixels.
*   **Y-Axis Trends (Left Scale):**
    *   The uppermost curve (represented by solid markers, $\bullet$) shows a sharp increase starting around 5 pixels, peaking near 12-15 pixels (reaching approximately $14 \times 10^{-3}$), and then gradually decreasing as the diameter increases further.
    *   Several other curves follow, showing similar bell-shaped or peaked responses, but at lower magnitudes. For instance, the curve represented by open markers ($\circ$) shows a peak around 10-15 pixels, reaching values between $3 \times 10^{-3}$ and $7 \times 10^{-3}$.
    *   The lowest curves show a much flatter response across the diameter range.

**5. Contextual Caption Integration:**
The provided context suggests these plots relate to stimulus size (Diameter) and a measured response. The small grayscale images below the graph likely represent examples of stimuli or receptive field profiles corresponding to different conditions tested in the experiment.



**1. Overall Layout & Structure:**
The figure is structured with a main graphical plot occupying the upper portion, and several smaller visual examples or stimuli displayed beneath it. The primary plot is a 2D line/scatter graph, and there are implied sub-panels or examples below the main plot area.

**2. Visual Components & Symbols:**
*   **Main Plot:** The upper section features a standard Cartesian coordinate system plot. Data points are marked, and they appear to be connected by lines (though the connection style is not perfectly clear, it represents a distribution).
*   **Lower Examples:** Below the main plot, there are several small grayscale images arranged horizontally. These likely represent different spatial frequency patterns or stimuli corresponding to the data shown in the plot above.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label (Left Plot):** $\times 10^{-3}$
*   **X-Axis Label (Left Plot):** Spatial Freq. (cycles/pixel)
*   **Y-Axis Label (Right Plot - Partially Visible):** Spat... (The full label is cut off, but it relates to the vertical axis of the right-hand plot).
*   **Legend/Key (Left Side):** A vertical stack of small, filled circles is present on the far left margin, suggesting a legend or different data series being tracked.

**4. Data Trends & Details (Focusing on the Left Plot):**
*   **X-Axis Range:** The x-axis spans from approximately 0.05 to 0.5 cycles/pixel.
*   **Y-Axis Range:** The y-axis ranges from 0 to $10 \times 10^{-3}$ (and potentially higher, given the scale).
*   **Data Points/Trend:** The plot shows a distribution curve peaking sharply.
    *   At Spatial Freq. $\approx 0.1$ cycles/pixel, the value is low (around $2 \times 10^{-3}$).
    *   The curve rises steeply to a maximum peak around Spatial Freq. $\approx 0.18$ cycles/pixel, where the value reaches approximately $12 \times 10^{-3}$.
    *   The curve then drops sharply, passing through a local minimum around Spatial Freq. $\approx 0.25$ cycles/pixel (value around $1 \times 10^{-3}$).
    *   The curve continues to decrease towards the right edge of the plot.

**5. Contextual Caption Integration:**
The visual elements below the main graph are grayscale images representing spatial patterns. These likely correspond to the input stimuli whose response is being measured by the plot above, illustrating different spatial frequencies. The visible patterns include:
*   A low-frequency pattern (large, smooth transitions).
*   Intermediate frequency patterns with distinct alternating bands.
*   Higher frequency patterns (finer, more rapid transitions).



**1. Overall Layout & Structure:**
The figure is structured primarily around a set of two overlaid line graphs, positioned above several small visual examples. The graph area occupies the upper portion, while the stimuli examples are arranged below it.

**2. Visual Components & Symbols:**
*   **Graphs:** There are two distinct curves plotted against shared axes. One curve is represented by a solid line connecting data points, and the other appears to be another set of connected data points.
*   **Axes:** The horizontal axis (x-axis) is labeled "Spatial Freq. (cycles/pixel)". The vertical axis (y-axis) on the left is labeled with units of $\times 10^{-3}$. A second, independent vertical axis is present on the right side of the graph area.
*   **Stimuli Examples:** Below the graphs, there are several small grayscale images representing different spatial frequency patterns. These include a uniform gray field (low/zero frequency), concentric rings, and striped patterns of varying frequencies.

**3. Labels, Keys & Legends:**
*   **X-axis Label:** "Spatial Freq. (cycles/pixel)"
*   **Left Y-axis Label:** $\times 10^{-3}$ (The specific variable name for this axis is not fully legible but relates to the plotted data).
*   **Right Y-axis Label:** A label is present on the right axis, though its full text is truncated or illegible in the provided crop.
*   **Stimuli Labels:** Below the stimuli, there are labels that appear to correspond to different types of visual input (e.g., "..." and a pattern labeled with vertical lines).

**4. Data Trends & Details (Graph Analysis):**
The graph displays two distinct frequency response curves:

*   **Upper Curve (Higher Amplitude):** This curve shows a clear peak. It starts low, rises steeply to reach a maximum value near $20 \times 10^{-3}$ at a spatial frequency around $0.15$ cycles/pixel, and then decreases symmetrically towards zero as the spatial frequency increases further.
*   **Lower Curve (Lower Amplitude):** This curve also shows a peak, but at a significantly lower amplitude. It rises to a maximum value near $9 \times 10^{-3}$ at a spatial frequency slightly below the peak of the upper curve (around $0.15$ cycles/pixel), and then decreases.

**5. Contextual Caption Integration:**
The provided context suggests this figure relates to frequency analysis, likely in the context of visual processing or neural responses. The stimuli examples below the graph illustrate the input patterns corresponding to different spatial frequencies being tested by the plotted functions.


---

## Page 6

argues against suggestions that cortex is not a source of the suppres-
sion generated by high temporal frequency stimuli (Carandini et al.,
2002; Li et al., 2006; Priebe and Ferster, 2006).
The experiments described above consider the effects of a
non-optimally oriented grating on the response to a grating at the
preferred orientation of the recorded neuron. Figure 7 shows the
effects of a mask on the response to a grating at a range of orien-
tations, not just the preferred orientation. For both V1 and the

model, the response to the plaid is approximately the average of
the responses generated by each grating when presented in isola-
tion. In the model, this effect is attributable to the competition
that occurs between neurons tuned to different orientations at
the same spatial location. These neurons are both activated by the
plaid stimulus but they compete to respond to that part of the
input that they both represent. This competition reduces the re-
sponse of both neurons compared with their responses when only

Orientation (degrees)

0
−100
100

Response

1

0
0

Test Contrast

0.1
0.5 1

20

40

60

0
0

Mask Contrast

1
0.5
0.1

20

0

40

60

0.1
1
3
0

10

20

30

Spatial Freq. (cycles/degree)

0

Drift Rate (cycles/second)

1

Suppression Index

20
5
10
2

−100
0
100
0

2

4

6

8

10

Orientation (degrees)

Response

x10−3

0.1
0.5 1
0

2

4

6

8

10

Test Contrast

x10−3

0.1
0.5 1
0

2

4

6

8

10

Mask Contrast

x10−3

0.05
0.2
0.5
0

1

2

3

x 10

−3

Spatial Freq. (cycles/pixel)

0.005
0.05
0.5
0

2

4

6

8x 10
−3

Drift Rate (cycles/iteration)

a

b
c
d
e

Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.

> Figure caption (from PDF text): Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.


### Overall Layout & Structure
The figure is structured as two separate graphs, one on top and one below. The caption indicates that the top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.

### Top Plot (Neurophysiological Data)
This plot displays a function of orientation for two different types of grating stimuli.

*   **Axes:**
    *   The **Y-axis** is labeled "Response" and ranges from 0 to 1.
    *   The **X-axis** is labeled "Orientation (degrees)" and ranges from -100 to 100.
*   **Data Representation:** Two sets of data points are plotted:
    1.  **Squares ($\square$):** Represent the response as a function of the orientation of a single grating. These points form a curve that peaks near 0 degrees, showing a characteristic tuning curve shape.
    2.  **Circles ($\circ$):** Represent the response as a function of the orientation of a mask grating additively superimposed on an optimally orientated grating. These points also form a curve, peaking near 0 degrees, but the overall shape suggests suppression compared to the squares.

### Bottom Plot (Simulation Results)
This plot displays a response function, likely related to the suppression index mentioned in the caption.

*   **Axes:**
    *   The **Y-axis** is labeled with units of $\times 10^{-3}$ and ranges from -10 to 10.
    *   The **X-axis** is labeled "Orientation (degrees)" and ranges from -100 to 100.
*   **Data Representation:** Multiple lines are plotted, representing different contrast levels of the mask grating.
    *   The data points form a characteristic tuning curve shape, peaking near 0 degrees.
    *   There are multiple lines visible, differentiated by thickness, corresponding to different mask contrasts as detailed in the caption: 0% (thinnest), 6, 12, 25, and 50% (thickest). The lines show a clear trend where increasing mask contrast leads to a reduction in the peak response (i.e., stronger suppression).

### Contextual Caption Integration
The caption provides crucial context for interpreting the visual elements:

*   **Top Plot (a):** This plot shows "Response as a function of the orientation of a single grating (squares) and as a function of the orientation of a mask grating additively superimposed on an optimally orientated grating (circles)." It is identified as neurophysiological data from a cell in cat V1.
*   **Bottom Plot (b):** This plot shows "Response as a function of the contrast of the optimally orientated grating for several different orthogonal mask contrasts." The line thickness corresponds to the mask grating contrast (0% to 50%). It is also identified as neurophysiological data from a cell in cat V1.

*(Note: The caption references panels c, d, and e which are not fully visible or clearly delineated in the provided image crop, but the description focuses on the two primary plots shown.)*

> Figure caption (from PDF text): Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.


### Overall Layout & Structure
The figure is divided into two main panels: a top panel and a bottom panel. Both panels are line graphs plotting a response metric against "Test Contrast" on the x-axis.

### Top Panel Description
The top panel displays a set of curves illustrating a response as a function of test contrast.

*   **X-Axis Label:** "Test Contrast"
*   **Y-Axis Label:** No explicit label is provided for the y-axis in this cropped view, but based on the caption context (Figure 6a/b), it represents a response measure.
*   **Data Representation:** Multiple lines are plotted, showing an increasing trend as the Test Contrast increases.
*   **Trends:** The curves generally rise steeply, indicating a positive relationship between contrast and response. There are several distinct lines, suggesting different conditions or parameters being tested.

### Bottom Panel Description
The bottom panel displays a second set of curves, also plotting a response against test contrast.

*   **X-Axis Label:** "Test Contrast"
*   **Y-Axis Label:** $\times 10^{-3}$ (indicating the units of the response).
*   **Data Representation:** Multiple lines are plotted, showing a more gradual increase compared to the top panel.
*   **Trends:** The curves show a clear, non-linear increase in response as the Test Contrast increases.

### Contextual Caption Integration (Inferred from provided text)
The caption indicates that the top row shows neurophysiological data, and the bottom row shows corresponding simulation results.

*   **Top Panel Context:** Corresponds to data described in Figure 6a, showing "Response as a function of the orientation of a single grating (squares) and a function of the orientation of mask grating additively superimposed on an optimally orientated grating (circles)."
*   **Bottom Panel Context:** Corresponds to data described in Figure 6b, showing "Response as a function of the contrast of the optimally orientated grating for several different orthogonal mask contrasts." The thickness of the lines in this context corresponds to specific mask contrast levels: 0% (thinnest), 6, 12, 25, and 50% (thickest).

In summary, the figure presents two comparative plots: the top plot likely shows neurophysiological data related to orientation response modulation, and the bottom plot presents simulation results showing how response changes with contrast under specific masking conditions.

> Figure caption (from PDF text): Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.


### Overall Layout & Structure
The figure is divided into two distinct graphical sections: a top plot and a bottom plot. The caption indicates that the top row shows neurophysiological data, and the bottom row shows corresponding simulation results.

### Top Plot (Neurophysiological Data)
This plot displays a function of orientation contrast, likely representing the response of a single cell.

*   **Axes:**
    *   The **Y-axis** is unlabeled with specific units but ranges from 0 to approximately 70, representing the cell response.
    *   The **X-axis** is labeled "Mask Contrast" and ranges from 0 to 1.

*   **Data Representation:** The plot contains multiple curves, each representing a different condition (likely varying the contrast of an optimally oriented grating).
    *   There are several distinct lines plotted. The curves generally show a decreasing trend as the Mask Contrast increases, indicating suppression.
    *   The lines are differentiated by thickness, corresponding to different mask contrasts according to the caption: "The thickness of each line corresponds to the contrast of the mask grating as follows: 0% (thinnest), 6, 12, 25, and 50% (thickest)."
    *   The curves start high on the left (low mask contrast) and drop towards zero as the Mask Contrast approaches 1.

### Bottom Plot (Simulation Results)
This plot displays a function of mask contrast, likely representing the simulation results corresponding to the top panel.

*   **Axes:**
    *   The **Y-axis** is labeled with units $\times 10^{-3}$ and ranges from 0 to 10.
    *   The **X-axis** is labeled "Mask Contrast" and ranges from 0 to 1.

*   **Data Representation:** This plot also contains multiple curves, differentiated by line thickness, corresponding to different contrasts of the optimally oriented grating.
    *   The caption specifies: "The thickness of each line corresponds to the contrast of the optimally oriented grating as follows: 0% (thinnest), 6, 12, 25, and 50% (thickest)."
    *   The curves generally show a decreasing trend as the Mask Contrast increases, similar to the top plot.
    *   The lines appear to be clustered and show a clear pattern of suppression across the range of mask contrasts.

### Contextual Caption Integration
The caption provides crucial context:
*   **Top Row:** Shows neurophysiological data from representative single cells in V1.
*   **Bottom Row:** Shows corresponding simulation results.
*   The data presented in both plots are described as a "suppression index," where 0 means no suppression and values $<0$ mean stronger suppression (though the plots appear to show positive values, suggesting the index might be normalized or presented differently in the visual representation).
*   The caption also mentions that for the model data (bottom plot), horizontal lines show the response to the optimally oriented grating in the absence of the mask, and that the mask generates strong suppression across a range of temporal frequencies.

> Figure caption (from PDF text): Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.


### Overall Layout & Structure
The figure consists of two distinct plots: a larger, upper plot and a smaller, lower plot. The caption suggests these panels correspond to different experimental conditions (a-e), although the visual structure provided here only shows two main graphs.

### Upper Plot Description
The upper plot is a line graph displaying data across varying spatial frequencies.

*   **Y-Axis:** Labeled with numerical values ranging from 0 to 30, representing a measured response magnitude.
*   **X-Axis:** Labeled "Spatial Freq. (cycles/degree)" and scaled from 0.1 to 3, with tick marks at intervals of 0.1 (e.g., 0.1, 0.2, ..., 3).
*   **Data Representation:** The plot contains multiple data points connected by lines, suggesting a measurement across different conditions.
    *   There is a horizontal line drawn near the top of the plot, around $Y \approx 27$, which likely represents a baseline or maximum response.
    *   Several distinct data points are plotted:
        *   At Spatial Freq. $\approx 0.1$, the response is high ($\approx 26$).
        *   At Spatial Freq. $\approx 0.15$, the response drops significantly ($\approx 17$).
        *   At Spatial Freq. $\approx 0.2$, the response is low ($\approx 8$).
        *   At Spatial Freq. $\approx 0.3$, the response is slightly higher ($\approx 10$).
        *   At Spatial Freq. $\approx 0.5$, the response is around $12$.
        *   At Spatial Freq. $\approx 0.75$, the response is high ($\approx 24$).
        *   At Spatial Freq. $\approx 1.0$, the response is high ($\approx 23$).
        *   At Spatial Freq. $\approx 1.5$, the response is around $20$.
        *   At Spatial Freq. $\approx 2.5$, the response is around $23$.

### Lower Plot Description
The lower plot is a line graph displaying data across varying spatial frequencies, scaled differently.

*   **Y-Axis:** Labeled with numerical values ranging from 0 to 3, and scaled by a factor of $10^{-3}$ (i.e., $\times 10^{-3}$).
*   **X-Axis:** Labeled "Spatial Freq. (cycles/pixel)" and scaled from 0.05 to 0.5, with tick marks at intervals like 0.05, 0.1, 0.2, etc.
*   **Data Representation:** This plot shows a curve with several distinct points:
    *   At Spatial Freq. $\approx 0.05$, the response is high ($\approx 1.9 \times 10^{-3}$).
    *   At Spatial Freq. $\approx 0.1$, the response dips ($\approx 1.5 \times 10^{-3}$).
    *   At Spatial Freq. $\approx 0.2$, the response is at its lowest point ($\approx 0.8 \times 10^{-3}$).
    *   At Spatial Freq. $\approx 0.3$, the response rises ($\approx 1.5 \times 10^{-3}$).
    *   At Spatial Freq. $\approx 0.4$, the response is higher ($\approx 1.9 \times 10^{-3}$).
    *   At Spatial Freq. $\approx 0.5$, the response is around $1.7 \times 10^{-3}$.

### Contextual Integration (Based on Caption)
The caption indicates that the data presented relates to **Cross-orientation suppression**.

*   The upper plot likely corresponds to neurophysiological data from a cell in cat V1, showing response as a function of spatial frequency (Panel d).
*   The lower plot likely corresponds to simulation results or another specific measurement related to spatial frequency (Panel d, if the upper plot is Panel d).
*   The caption notes that physiological data are presented as a **suppression index**, where 0 means no suppression and values $<0$ mean stronger suppression. This suggests the plotted values might represent this index, although the axes labels do not explicitly state "Suppression Index."
*   The caption also mentions that for model data, horizontal lines show the response to the optimally oriented grating in the absence of a mask.

> Figure caption (from PDF text): Figure 6.
Cross-orientation suppression. The top row shows neurophysiological data from representative single cells in V1, and the bottom row shows corresponding simulation results.
a,Responseasafunctionoftheorientationofasinglegrating(squares)andasafunctionoftheorientationofamaskgratingadditivelysuperimposedonanoptimallyorientatedgrating(circles).
Shown are neurophysiological data for a cell in cat V1 [data from Bonds (1989); figure adapted from Schwartz and Simoncelli (2001), their Fig. 5]. b, Response as a function of the contrast of the
optimallyorientatedgratingforseveraldifferentorthogonalmaskcontrasts.Thethicknessofeachlinecorrespondstothecontrastofthemaskgratingasfollows:0%(thinnest),6,12,25,and50%
(thickest). Shown are neurophysiological data for a cell in cat V1 [adapted from Freeman et al. (2002), their Fig. 2]. c, The data in b replotted to show response as a function of the contrast of the
orthogonalmaskgratingforseveraldifferentoptimallyorientedgratingcontrasts.Thethicknessofeachlinecorrespondstothecontrastoftheoptimallyorientedgratingasfollows:0%(thinnest),
6,12,25,and50%(thickest).d,Responseasafunctionofthespatialfrequencyofanorthogonalmaskgrating.ShownareneurophysiologicaldataforasimplecellincatV1[adaptedfromDeAngelis
etal.(1992),theirFig.3b].Thehorizontallinesshowtheresponsetotheoptimallyorientedgratingpresentedinisolation.e,Responseasafunctionofthetemporalfrequencyofanorthogonalmask
grating.ShownareneurophysiologicaldataforacellincatV1[adaptedfromFreemanetal.(2002),theirFig.3e].Notethatthephysiologicaldataarepresentedintheformofasuppressionindex:
avalueof0correspondstonosuppressionandvalues0correspondtostrongersuppression.Forthemodeldata,thehorizontallineshowstheresponsetotheoptimallyorientatedgatinginthe
absence of the mask; hence the mask generates strong suppression across a range of temporal frequencies, consistent with the neurophysiological data.


### Overall Layout & Structure
The figure is composed of two separate graphs, one positioned above the other. The top graph displays a relationship between "Suppression Index" and "Drift Rate (cycles/second)," while the bottom graph displays a relationship between an unspecified response measure and "Drift Rate (cycles/iteration)."

### Top Graph Analysis
**Type:** Line plot.
**Y-Axis Label:** Suppression Index (ranging from 0 to slightly above 1).
**X-Axis Label:** Drift Rate (cycles/second) (with labeled ticks at 2, 5, 10, and 20).

**Data Trend:** The plot shows a generally increasing trend in the Suppression Index as the Drift Rate increases from 2 to approximately 10 cycles/second. The index rises from a value around 0.5 at 2 cycles/second to nearly 1.0 at 10 cycles/second. After peaking near 1.0 around 12-15 cycles/second, the index slightly decreases before rising again near 20 cycles/second.

### Bottom Graph Analysis
**Type:** Line plot (or scatter plot with connecting lines).
**Y-Axis Label:** A numerical scale ranging from 0 to 8, with a multiplier indicated as $\times 10^{-3}$.
**X-Axis Label:** Drift Rate (cycles/iteration) (with labeled ticks at 0.005, 0.05, and 0.5).

**Data Trend:** This plot shows a generally increasing trend in the measured response as the Drift Rate (cycles/iteration) increases. The data points appear relatively flat between 0.005 and 0.05 cycles/iteration, hovering around a value slightly above $3 \times 10^{-3}$. The response then shows a more pronounced increase between 0.05 and 0.5 cycles/iteration, reaching approximately $4.5 \times 10^{-3}$ at the highest plotted drift rate.

### Contextual Caption Integration
The caption identifies these plots as representing "Cross-orientation suppression." It specifies that the top row (which corresponds to the upper graph) shows "neurophysiological data from representative single cells in V1," and the bottom row (corresponding to the lower graph) shows "corresponding simulation results."

The caption further clarifies that the physiological data are presented in the form of a **suppression index**, where 0 indicates no suppression and values approaching 1 indicate stronger suppression. For the model data (the simulation results, likely the bottom plot), horizontal lines show the response to the optimally oriented grating in the absence of the mask, indicating that the mask generates strong suppression across a range of temporal frequencies.

Response

20

90
135
45
0

10

0
180
Orientation (degrees)

20

10

0
90
135
180
45
0
Orientation (degrees)

20

10

00
90
135
180
Orientation (degrees)

45
0

10

20

90
135
180
45
0
Orientation (degrees)

0
45
90
135 180
0

0.01

Orientation (degrees)

Response

0
45
90
135 180
0

0.01

Orientation (degrees)

0
45
90
135 180
0

0.01

Orientation (degrees)

0
45
90
135 180
0

0.01

Orientation (degrees)

Figure 7.
Cross-orientation suppression with varying orientation. Response as a function of grating orientation for two gratings presented in isolation (dashed lines) and for both gratings
presentedsimultaneously(solidlines).ThetoprowshowsresponsesfromasinglecellintreeshrewV1[adaptedfromMacEvoyetal.(2009),theirFig.4],andthebottomrowshowsresponsesfrom
the model. The angle between the two gratings increases from left to right: 22.5° (left column), 45, 67.5, and 90° (right column).

> Figure caption (from PDF text): Figure 7.
Cross-orientation suppression with varying orientation. Response as a function of grating orientation for two gratings presented in isolation (dashed lines) and for both gratings
presentedsimultaneously(solidlines).ThetoprowshowsresponsesfromasinglecellintreeshrewV1[adaptedfromMacEvoyetal.(2009),theirFig.4],andthebottomrowshowsresponsesfrom
the model. The angle between the two gratings increases from left to right: 22.5° (left column), 45, 67.5, and 90° (right column).


### Overall Layout and Structure
The figure is structured into two rows and two columns, resulting in four distinct panels. The top row displays responses from a single cell in the shrew V1, while the bottom row shows responses derived from a model. The columns represent increasing angular separation between two gratings: the left column corresponds to $22.5^\circ$, the middle-left panel is for $45^\circ$, the middle-right panel is for $67.5^\circ$, and the right column is for $90^\circ$.

### Visual Components & Symbols
Each panel contains a standard Cartesian coordinate plot. The data is represented by two types of lines:
1. **Dashed Lines ($\text{---}$)**: Represent the response when gratings are presented in isolation.
2. **Solid Lines ($\text{---}$)**: Represent the response when both gratings are presented simultaneously.

In addition to the plots, there is a small shaded gray box located in the upper right corner of each panel, which likely indicates the angular separation being tested for that column.

### Labels, Keys & Legends
**Axes Labels:**
*   **Y-axis (Vertical):** Labeled "Response" on the left side of the top row and implicitly on the bottom row. The scale ranges from 0 to 20 in the top row and 0 to 0.01 in the bottom row, indicating different units or scales for the neural data versus the model output.
*   **X-axis (Horizontal):** Labeled "Orientation (degrees)" across the bottom of all panels, ranging from $0^\circ$ to $180^\circ$.

**Contextual Annotations (from Caption):**
*   The top row shows responses from a single cell in the shrew V1.
*   The bottom row shows responses from "the model."
*   The angular separation between the two gratings increases across the columns: $22.5^\circ$ (left column), $45^\circ$, $67.5^\circ$, and $90^\circ$ (right column).

### Data Trends & Details
**Top Row (Shrew V1 Responses):**
*   **Left Panel ($22.5^\circ$ separation):** Both the dashed and solid lines show a peak response centered around $45^\circ$ orientation. The suppression effect (difference between dashed and solid lines) appears minimal or slight at this small angle.
*   **Middle-Left Panel ($45^\circ$ separation):** The peak response shifts slightly, and the suppression effect becomes more pronounced.
*   **Middle-Right Panel ($67.5^\circ$ separation):** The peak response is clearly visible, and the suppression effect between the dashed (isolation) and solid (simultaneous) lines is evident.
*   **Right Panel ($90^\circ$ separation):** The response curves show a clear pattern of suppression, with the solid line (simultaneous presentation) exhibiting lower peak responses compared to the dashed line (isolation).

**Bottom Row (Model Responses):**
*   The scale on the Y-axis is much smaller ($0.01$). The general trend mirrors the top row, showing changes in peak response and suppression as the angular separation increases from left to right.
*   The curves exhibit characteristic peaks corresponding to specific orientations, demonstrating the modeled behavior of orientation selectivity and cross-orientation suppression.

**Shaded Boxes:**
The shaded gray boxes in the upper right corner of each panel visually correspond to the angular separation being tested for that column, confirming the progression from $22.5^\circ$ to $90^\circ$.

> Figure caption (from PDF text): Figure 7.
Cross-orientation suppression with varying orientation. Response as a function of grating orientation for two gratings presented in isolation (dashed lines) and for both gratings
presentedsimultaneously(solidlines).ThetoprowshowsresponsesfromasinglecellintreeshrewV1[adaptedfromMacEvoyetal.(2009),theirFig.4],andthebottomrowshowsresponsesfrom
the model. The angle between the two gratings increases from left to right: 22.5° (left column), 45, 67.5, and 90° (right column).


### Overall Layout and Structure
The figure is divided into two rows and two columns, resulting in four distinct panels.

*   **Top Row:** Contains two plots showing responses from a single cell in V1 (adapted from MacEvoy et al. 2009, Fig. 4).
*   **Bottom Row:** Contains two plots showing responses from a model.

The columns represent different angular separations between the two gratings:
*   **Left Column:** Corresponds to an angle of $22.5^\circ$.
*   **Right Column:** Corresponds to an angle of $90^\circ$ (based on the caption, though the intermediate angles are also implied by the structure).

### Visual Components and Data Trends (Plots)

All four panels are line graphs plotting response magnitude against grating orientation.

**Y-Axis (Vertical Axis):**
The y-axis in the top row ranges from 0 to 20. The y-axis in the bottom row ranges from 0 to $0.01$.

**X-Axis (Horizontal Axis):**
The x-axis in all panels represents "Orientation (degrees)" and ranges from $0^\circ$ to $180^\circ$, marked at intervals of $45^\circ$.

**Line Types and Data Representation:**
In all plots, two types of lines are used to represent different experimental/mode conditions:
1.  **Dashed Lines:** Represent the response when gratings are presented in isolation.
2.  **Solid Lines:** Represent the response when both gratings are presented simultaneously.

#### Top Row (Single Cell in V1)
*   **Top-Left Panel ($22.5^\circ$ separation):** Shows the response curves for $22.5^\circ$ separation. The dashed lines show peaks at specific orientations, and the solid lines show a suppression effect compared to the isolated presentation.
*   **Top-Right Panel ($90^\circ$ separation):** Shows the response curves for $90^\circ$ separation. Similar to the left panel, it displays the effect of cross-orientation suppression.

#### Bottom Row (Model)
*   **Bottom-Left Panel ($22.5^\circ$ separation):** Shows the model's response curves for $22.5^\circ$ separation, using a logarithmic scale on the y-axis (ranging from 0 to $0.01$).
*   **Bottom-Right Panel ($90^\circ$ separation):** Shows the model's response curves for $90^\circ$ separation, also using a logarithmic scale on the y-axis.

**Annotations:**
In the top row, there is a small gray square icon in the upper right corner of each panel. In the bottom row, there is a similar small gray square icon in the upper right corner of each panel.

### Contextual Caption Integration
The caption clarifies that:
*   The **top row** displays responses from a single cell in V1.
*   The **bottom row** displays responses from the model.
*   The angular separation between the two gratings increases across the columns: $22.5^\circ$ (left column), $45^\circ$, $67.5^\circ$, and $90^\circ$ (right column). The figure explicitly shows the $22.5^\circ$ and $90^\circ$ cases, implying the intermediate angles are part of the full dataset referenced.
*   The dashed lines represent responses when gratings are presented **in isolation**.
*   The solid lines represent responses when both gratings are presented **simultaneously**, demonstrating cross-orientation suppression.

3536 • J. Neurosci., March 3, 2010 • 30(9):3531–3543
Spratling • Predictive Coding Model of V1


---

## Page 7

a single grating is presented. When the contrasts of the two grat-
ings are unequal, the response to the plaid is biased toward that
generated when the higher contrast grating is presented in isola-
tion (Fig. 8). In the model, this effect is attributable to the neu-
rons representing the higher contrast grating receiving the
stronger input and being able to more effectively compete to
represent the stimulus.

Surround suppression
Another form of suppression that has been widely studied in V1 is
that attributable to one grating surrounding (rather than being
superimposed on) another. The effects of such surrounds can be
either suppressive or facilitatory. Jones et al. (2002) observed five
distinct patterns of behavior (Fig. 9). “Orientation contrast sup-
pression” and “non-orientation-specific suppression” occurred
most frequently when the center-surround border was within the
RF of the recorded neuron. “Mixed general suppression” oc-
curred most frequently when the border diameter matched, or
was smaller than, the diameter of the RF. “Orientation alignment
suppression” was most common when the border diameter
matched, or was larger than, the diameter of the RF. Finally,
“orientation contrast facilitation” occurred most frequently
when the center-surround border was outside the RF. In these
experiments, the RF was measured by taking the maximum value
found using a variety of techniques, including the measurement
of the SF. At the contrast used for the simulations (50%), the
model neuron had a SF diameter of 12 pixels (Fig. 5c). The
diameter of the border between the center and surround used to
simulate each of these classes of behavior (Fig. 9) thus correlates
well with the diameters at which the different behaviors were
most frequently observed in the neurophysiological data. Note,
however, that in the model the facilitation attributable to a non-
iso-oriented surround at the largest diameter is much weaker
than that recorded for the V1 cell.

The pattern of results generated by the model can be explained
as follows. The values of the dashed lines at 0° orientation corre-
spond to the different points along the size tuning curve (Fig. 5b).
Hence, moving from Figure 9a–e, there is a rise and fall in the size
of the peak as the diameter of the grating increases. In each case,
as the orientation of the grating deviates from the preferred ori-

entation of the recorded neuron, so the response falls. When the
surround is iso-oriented, the stimulus is effectively a single large
grating at the preferred orientation of the neuron. Hence the
values of the solid lines at 0° orientation correspond to the pla-
teau of the size tuning curve (Fig. 5b), and the response is approx-
imately constant with changing diameter. When the surround is
not iso-oriented, the response increases as the diameter of the
center increases (Fig. 9, from a to e). This is attributable to the
afferent excitation received by the recorded neuron increasing as
the center diameter increases.

Reducing the contrast of the center stimulus, in relation to the
contrast of the surround stimulus, can affect the orientation se-
lectivity of surround suppression. Specifically, Levitt and Lund
(1997) found that for 21% of cells surround suppression oc-
curred over a wider range of surround orientations when using a
low-contrast center, even though the same cell was subject to
surround suppression only with a near iso-oriented surround
when the center was presented at high contrast (Fig. 10a, top).
The same behavior is observed in the model (Fig. 10a, bottom).
This is attributable to the low-contrast center stimulus when pre-
sented in isolation, at the preferred orientation, still producing a
strong response from the recorded neuron (Fig. 5a). However, in
the presence of a high-contrast surround at any orientation, the
neurons representing this high-contrast surround receive a
stronger input and are more effective at competing to represent
the stimulus and so are more effective at suppressing the response
of the recorded neuron. As for 75% of the recorded cells (Levitt
and Lund, 1997), the orientation of the surround that generated
the greatest suppression in the model was the same for high- and
low-contrast centers.

For both V1 and the model, the strength of response increases
with the contrast of the center in the presence of an iso-oriented
surround (Fig. 10b). This is unsurprising since the strength of the
afferent stimulation received by the recorded neuron increases
with contrast. As the contrast of the surround increases, so does
the suppression (Fig. 10b). In the model, this is attributable to
increased competition from neurons representing the surround
partially suppressing the response of the recorded neuron. For
both V1 and the model, at all center contrasts an orthogonal
surround produces weaker suppression than that produced by an
iso-oriented surround (Fig. 10c). In the model, this behavior is
attributable to the recorded neuron having an RF that overlaps
less with neurons representing the orthogonal surround com-
pared with neurons representing the iso-oriented surround.
Hence the recorded neuron is suppressed less in the former con-
dition than the latter. For both V1 and the model, suppression
increases with surround contrast and suppression attributable to
an orthogonal surround is weaker than suppression attributable
to an iso-oriented surround (Fig. 10d). As in the preceding ex-
periment, this is attributable to the recorded neuron having an
RF that overlaps less with neurons representing the orthogonal
surround compared with neurons representing the iso-oriented
surround. In either condition, increasing the contrast of the sur-
round increases the afferent input to neurons representing the
surround and hence increases the strength of suppression.

The suppressive influence of an iso-oriented surround can be
reduced by superimposing on the surround a second grating with
an orthogonal orientation (Fig. 10e). For both V1 and the model,
the degree of suppression varies with the contrast of the orthog-
onal surround grating. Suppression is strongest (weakest) when
the contrast of the orthogonal surround is lower (higher) than the
contrast of the iso-oriented surround. In the model, this effect is
attributable to the neurons responding to the iso-oriented sur-

0

0.5

1

90
45
0
135
180

Response

Orientation (degrees)

0.5

1

0

Orientation (degrees)

90
135
180
45
0

0
45
90
135 180
0

0.01

Orientation (degrees)

Response

0
45
90
135 180
0

0.01

Orientation (degrees)

Figure8.
Cross-orientationsuppressionwithvaryingorientationandcontrast.Responseas
a function of grating orientation for two gratings presented in isolation (dashed lines) and for
both gratings presented simultaneously (solid lines). The top row shows population responses
measured using intrinsic signal optical imaging in tree shrew V1 [adapted from MacEvoy et al.
(2009), their Fig. 3], and the bottom row shows responses from a single neuron in the model.
The angle between the two gratings was 90°. One grating was presented at a lower contrast
thantheother:fortheleftcolumn,thecontrastswere0.5and0.25,andfortherightcolumn,the
contrasts were 0.5 and 0.125.

Spratling • Predictive Coding Model of V1
J. Neurosci., March 3, 2010 • 30(9):3531–3543 • 3537



### Overall Layout & Structure
The figure is organized into four panels: two in the top row and two in the bottom row. All plots share a common structure featuring an x-axis representing "Orientation (degrees)" and a y-axis representing normalized values, ranging from 0 to 1.

### Panel Descriptions (Top Row)

**Top-Left Plot:**
*   **Type:** Line graph.
*   **X-axis Label:** Orientation (degrees), ranging from 0 to 180.
*   **Y-axis Label:** Unlabeled, ranging from 0 to 1.
*   **Data Trends:** Two distinct lines are plotted:
    1.  A solid line showing a peak around 45 degrees, reaching approximately 0.8, followed by a decrease towards 90 degrees, and then another rise peaking around 135 degrees before decreasing again.
    2.  A dashed line showing a broader, lower peak around 45 degrees (reaching approximately 0.7), and another significant peak around 135 degrees (reaching approximately 0.8).
*   **Inset:** A small, square grayscale image is positioned in the upper right corner of this panel.

**Top-Right Plot:**
*   **Type:** Line graph.
*   **X-axis Label:** Orientation (degrees), ranging from 0 to 180.
*   **Y-axis Label:** Unlabeled, ranging from 0 to 1.
*   **Data Trends:** Two distinct lines are plotted:
    1.  A solid line showing a sharp peak around 45 degrees, reaching approximately 0.9, followed by a decline towards 135 degrees.
    2.  A dashed line showing a lower, broader peak around 45 degrees (reaching approximately 0.6), and another smaller rise towards 180 degrees (reaching approximately 0.5).
*   **Inset:** A small, square grayscale image is positioned in the upper right corner of this panel.

### Panel Descriptions (Bottom Row)

**Bottom-Left Plot:**
*   **Type:** Line graph.
*   **X-axis Label:** Orientation (degrees), ranging from 0 to 180.
*   **Y-axis Label:** Unlabeled, ranging from 0 to 0.01 (with major ticks at 0 and 0.01).
*   **Data Trends:** Two distinct lines are plotted:
    1.  A solid line showing a sharp peak around 45 degrees, reaching approximately $0.008$.
    2.  A dashed line showing a peak around 45 degrees (reaching approximately $0.007$), and another smaller rise near 135 degrees.
*   **Inset:** A small, square grayscale image is positioned in the upper right corner of this panel.

**Bottom-Right Plot:**
*   **Type:** Line graph.
*   **X-axis Label:** Orientation (degrees), ranging from 0 to 180.
*   **Y-axis Label:** Unlabeled, ranging from 0 to 0.01 (with major ticks at 0 and 0.01).
*   **Data Trends:** Two distinct lines are plotted:
    1.  A solid line showing a sharp peak around 45 degrees, reaching approximately $0.009$.
    2.  A dashed line showing a lower peak around 45 degrees (reaching approximately $0.006$), and another small rise near 135 degrees.
*   **Inset:** A small, square grayscale image is positioned in the upper right corner of this panel.


---

## Page 8

round (which most strongly suppress the response of the re-
corded neuron) being themselves suppressed by the responses of
neurons to the orthogonal surround at high contrast (there is
cross-orientation suppression between the neurons responding
to the surround).

The strength of surround suppression is also influenced by the
phase of an iso-oriented surround grating (Fig. 10f). For both V1
and the model, the suppression is weakest when the surround is
out of phase with the center stimulus and strongest when the
surround and center gratings are in phase. In the model, there is
strong competition between neurons with collinear RFs at over-
lapping locations. When the surround is at the same phase as the
center, neurons with RFs collinear with the recorded neuron are
activated and suppress its response. In contrast, when the sur-
round is out of phase with the center, neurons with RFs collinear
to the recorded neuron are not activated by the surround stimu-
lus; they thus do not inhibit the recorded neuron, which gener-
ates a stronger response.

Flankers and textured surrounds
The interaction between center and surround has also been ex-
plored using isolated bars rather than gratings (Fig. 11a,b). A pair
of collinear flankers, or a single collinear flanker, increases the
response to a bar presented at the center of the RF, even though
these flanking stimuli produce little response when presented
alone. Furthermore, the enhancement attributable to a collinear
flanker can be blocked by a perpendicular bar separating the
central bar from the flanker. In contrast to collinear flankers,
parallel flankers suppress the response to the central bar. The
model produces behavior that is mostly consistent with the phys-
iological data (Fig. 11f). The results of the model can be explained
as follows. The collinear flankers partially activate the RF of the

recorded neuron, and hence its response is enhanced because of
increased afferent input. Hence the model suggests that some
nonclassical RF effects may result from the inadvertent stimula-
tion of the classical RF. The collinear flankers when presented in
isolation are much better represented by other neurons, and
hence the response of the recorded neuron is suppressed. When a
collinear flanker is presented together with an orthogonal
flanker, the recorded neuron receives greater afferent input, but
there is also stronger competition to represent that input (from
neurons selective for the orthogonal bar) so this configuration
has little overall effect on the response. Finally, the parallel flankers
activate neighboring neurons, which compete with the recorded
neuron, suppressing its response. In the neurophysiological data,
the effects were highly dependent on the positioning of the con-
textual stimuli relative to the central stimulus (Kapadia et al.,
1995, 2000). The model shows a similar dependence (data not
shown): the facilitation generated by a collinear flanker is re-
duced and is eventually abolished as (1) the spacing between the
flanker and the central stimulus increases, (2) the flanker is tilted
relative to the central stimulus, and (3) the flanker is laterally
offset from the central stimulus.

Rather than using single bars, experiments have also been
performed using surrounding textures created from many
equally spaced bars (Knierim and van Essen, 1992; Nothdurft et
al., 1999; Hegde´ and Felleman, 2003). Nothdurft et al. (1999)
observed two different patterns of behavior: for “orientation con-
trast” cells, the response to a central, optimally oriented, bar was
suppressed by an iso-oriented surrounding texture, but not an
orthogonal surround (Fig. 11c); for “uniform” cells, the response
to the central bar was suppressed by textures at either orientation,
but most strongly by an orthogonal surround (Fig. 11d). The
model can produce results consistent with both these behaviors

Orientation (degrees)

0
45
90
−45
−90
0

20

40

60

Response

Orientation (degrees)

0
−45
−90
0
45
90

20

40

60

Orientation (degrees)

0
45
90
−45
−90

20

40

60

0

Orientation (degrees)

0
45
90
−45
−90

0

60

40

20

Orientation (degrees)

0
45
90
−45
−90
0

20

40

60

−90 −45
0
45
90
0

0.01

0.02

Orientation (degrees)

Response

−90 −45
0
45
90
0

0.01

0.02

Orientation (degrees)

−90 −45
0
45
90
0

0.01

0.02

Orientation (degrees)

−90 −45
0
45
90
0

0.01

0.02

Orientation (degrees)

−90 −45
0
45
90
0

0.01

0.02

Orientation (degrees)

a
b
c
d
e

Figure9.
Surroundsuppressionwithvariablesurroundorientation.ThetoprowshowsneurophysiologicaldatafromrepresentativesinglecellsinprimateV1[adaptedfromJonesetal.(2002),
their Fig. 1], and the bottom row shows corresponding simulation results. a–e, Each column shows a different pattern of behavior identified by Jones et al. (2002) as follows: orientation contrast
suppression (a), non-orientation-specific suppression (b), mixed general suppression (c), orientation alignment suppression (d), and orientation contrast facilitation (e). In each case, response is
plotted as a function of grating orientation relative to the preferred orientation of the neuron for a central grating presented in isolation (dashed lines) and as a function of the orientation of a
surroundingannulusinthepresenceofanoptimallyorientedcentralgrating(solidlines).Notethatfortheneurophysiologicaldataina,butnottheotherplots,onlytheresponseat0°isshownfor
theconditioninwhichthecenterispresentedinisolation(circularmarker).Theresultsforthemodelweregeneratedusingacenterdiameterofthefollowing:7pixels(a),11pixels(b),13pixels(c),
17 pixels (d), and 19 pixels (e). The inner diameter of the surrounding annulus was equal to the center diameter in each case.

3538 • J. Neurosci., March 3, 2010 • 30(9):3531–3543
Spratling • Predictive Coding Model of V1



### **Top Graph**

This graph displays a function plotted against orientation.

*   **Axes:**
    *   The **Y-axis** is labeled "Responses" and ranges from 0 to 40, with major tick marks every 20 units (0, 20, 40).
    *   The **X-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90, with major tick marks every 45 degrees (-90, -45, 0, 45, 90).
*   **Data Trend:** A single line plot shows the response as a function of orientation. The response is low (near zero) at orientations of -90, -45, 45, and 90 degrees. The response peaks sharply at an orientation of $0$ degrees, reaching a maximum value slightly above 10 (approximately 12-14). The curve is relatively narrow around the peak.

### **Bottom Graph**

This graph also displays a function plotted against orientation, but it appears to represent two related datasets.

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to 0.02, with major tick marks at 0, 0.01, and 0.02.
    *   The **X-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90, with major tick marks at -90, -45, 0, 45, and 90.
*   **Data Trends:** Two distinct line plots are visible:
    1.  **Dashed Line ($\text{--}\text{-}$):** This line shows a response that is low near $\pm 90$ degrees. It rises to a peak at $0$ degrees, reaching a value slightly below 0.01 (approximately 0.009).
    2.  **Dotted Line ($\text{...}$):** This line follows a very similar pattern to the dashed line. It is low at $\pm 90$ degrees, rises to a peak at $0$ degrees, and reaches a maximum value slightly above 0.01 (approximately 0.01).

Both curves in the bottom graph exhibit a strong tuning curve centered at $0$ degrees orientation.



### Top Plot
This plot is a line graph displaying data across an angular range.

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to 60, marked in increments of 20 (0, 20, 40, 60).
    *   The **X-axis** is labeled "Orientation (degrees)" and spans from -90 to 90, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
*   **Data Representation:** There are two distinct lines plotted:
    1.  A **solid line (likely representing one condition)**, which hovers generally between 10 and 20 across the orientation range.
    2.  A **dashed line (likely representing a second condition)**, which shows a clear peak centered around 0 degrees. This dashed line rises significantly above the solid line, reaching a maximum value near 25-30 at $0^\circ$. The dashed line generally remains above the solid line in the central region.

### Bottom Plot
This plot is also a line graph, positioned directly below the top plot.

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values ranging from 0 to 0.02, marked in increments of 0.01 (0, 0.01, 0.02).
    *   The **X-axis** is labeled "Orientation (degrees)" and spans from -90 to 90, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
*   **Data Representation:** Similar to the top plot, there are two lines:
    1.  A **solid line**, which shows a relatively low, fluctuating baseline across the orientation range, generally staying below 0.01.
    2.  A **dashed line**, which exhibits a sharp, pronounced peak centered precisely at $0^\circ$. This dashed line reaches its maximum value around 0.012 to 0.013 at $0^\circ$, significantly higher than the solid line in that region.

### Legend/Key Area (Bottom Right)
In the bottom right corner, there is a small legend area containing graphical elements and associated labels:

*   There are three distinct visual keys presented horizontally, each consisting of a pattern swatch and an associated label (though the labels are partially obscured or too small to read definitively, they appear to correspond to the line styles used in the plots).
    *   The first key shows a pattern resembling horizontal lines (solid/striped texture).
    *   The second key shows a pattern resembling vertical lines (dashed/striped texture).
    *   The third key shows a pattern resembling diagonal hatching.

*(Note: Due to the low resolution of the legend area, specific textual labels associated with these patterns cannot be transcribed accurately.)*



### Top Graph
This graph displays two distinct line plots against an orientation axis.

*   **Axes:**
    *   The **x-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
    *   The **y-axis** is numerical and ranges from 0 to 60, marked in increments of 20 (0, 20, 40, 60).
*   **Data Series:** Two lines are plotted:
    1.  **Solid Line (Lower/Smoother):** This line shows a relatively low, undulating trend. It starts around 30 at -90 degrees, dips slightly to about 25 near -45 degrees, rises slightly to around 30 at 0 degrees, dips again to approximately 17 near 45 degrees, and rises slightly to about 32 at 90 degrees.
    2.  **Dashed Line (Upper/Spikier):** This line exhibits a highly peaked, bimodal-like pattern centered around 0 degrees. It starts near 0 at -90 degrees, rises sharply to a peak exceeding 60 (around 63) at 0 degrees, and then drops sharply back down to near 0 by 90 degrees.

### Bottom Graph
This graph also displays two distinct line plots against an orientation axis, but the y-axis scale is much smaller.

*   **Axes:**
    *   The **x-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
    *   The **y-axis** is numerical and ranges from 0 to 0.02, marked in increments of 0.01 (0, 0.01, 0.02).
*   **Data Series:** Two lines are plotted:
    1.  **Solid Line (Lower/Smoother):** This line shows a relatively low, fluctuating trend. It starts around 0.012 at -90 degrees, rises slightly to about 0.013 near -45 degrees, dips slightly below 0.01 at 0 degrees, rises again to about 0.012 near 45 degrees, and ends around 0.01 at 90 degrees.
    2.  **Dashed Line (Upper/Spikier):** This line shows a sharp, narrow peak centered at 0 degrees. It remains near 0 across the negative orientations (e.g., close to 0 at -90 and -45 degrees), rises sharply to a peak of approximately 0.02 at 0 degrees, and then drops back down to near 0 across the positive orientations (e.g., close to 0 at 45 and 90 degrees).



### Top Plot (Panel 1)

This plot is a line graph showing data across an angular range.
*   **X-Axis:** Labeled "Orientation (degrees)," ranging from -90 to 90 degrees, with major tick marks at intervals of 45 degrees (-90, -45, 0, 45, 90).
*   **Y-Axis:** Labeled with numerical values ranging from 0 to 60, marked in increments of 20 (0, 20, 40, 60).
*   **Data Lines:** Two distinct lines are plotted:
    1.  A solid line (likely representing one condition or measurement) that starts high on the left, dips significantly around -45 degrees, rises sharply to a peak near 0 degrees (around 20-25), and then continues to rise towards the right, reaching approximately 40 by 90 degrees.
    2.  A dashed line (likely representing a second condition or measurement) that starts near zero at -90 degrees, rises steeply to a peak around 0 degrees (reaching approximately 38-40), and then drops sharply towards zero by 90 degrees.

### Bottom Plot (Panel 2)

This plot is also a line graph, positioned directly below the top plot.
*   **X-Axis:** Labeled "Orientation (degrees)," ranging from -90 to 90 degrees, with major tick marks at intervals of 45 degrees (-90, -45, 0, 45, 90).
*   **Y-Axis (Left):** Labeled with numerical values ranging from 0 to 0.02, marked in increments of 0.01 (0, 0.01, 0.02).
*   **Y-Axis (Right):** A secondary Y-axis is present on the right side, though no specific labels are clearly legible for it in this cropped view.
*   **Data Lines:** Two distinct lines are plotted:
    1.  A solid line that remains relatively flat and high across the entire range, hovering around 0.013 to 0.014 on the left Y-axis.
    2.  A dashed line that is centered around 0 degrees orientation. It starts near zero at -90 degrees, rises sharply to a peak slightly above 0.01 on the left Y-axis at 0 degrees, and then drops back down to near zero by 90 degrees.

### Bottom Image Strip (Panel 3)

Below the two plots, there is a narrow strip containing several small, stylized images arranged horizontally. These appear to be visual stimuli or representations of orientations:
*   The strip shows a sequence of small, patterned images. These patterns appear to be oriented gratings or bars, suggesting they represent different orientations used in the experiments depicted by the plots above. The patterns vary in their orientation across the visible sequence.



### Top Graph Description

**1. Overall Layout & Structure:**
The top graph is a 2D line plot showing data as a function of orientation.

**2. Visual Components & Symbols:**
*   **Axes:** It features a horizontal x-axis and a vertical y-axis.
*   **Lines:** There are two distinct lines plotted: one solid line and one dashed line.
*   **Data Points:** Both lines appear to be connected by markers, although the resolution makes specific marker shapes difficult to discern; they are clearly continuous curves.

**3. Labels, Keys & Legends:**
*   **Y-axis Label:** The vertical axis is labeled with numerical values ranging from 0 to 60, marked in increments of 20 (0, 20, 40, 60).
*   **X-axis Label:** The horizontal axis is labeled "Orientation (degrees)" and spans from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).

**4. Data Trends & Details:**
*   **Solid Line Trend (Upper Curve):** This line starts high on the left, around a value of 45 at -90 degrees. It decreases steeply to a minimum near the center (around 0 degrees), reaching approximately 10-15. It then increases sharply, rising to nearly 60 at 90 degrees.
*   **Dashed Line Trend (Lower Curve):** This line remains very close to the zero baseline across most of the range. It shows a slight increase around 0 degrees, peaking slightly above zero (perhaps around 15-20) at 0 degrees, and then drops back down close to zero towards the edges.

### Bottom Graph Description

**1. Overall Layout & Structure:**
The bottom graph is also a 2D line plot, structurally similar to the top graph.

**2. Visual Components & Symbols:**
*   **Axes:** It features a horizontal x-axis and a vertical y-axis.
*   **Lines:** There are two distinct lines plotted: one solid line and one dashed line.

**3. Labels, Keys & Legends:**
*   **Y-axis Label:** The vertical axis is labeled with numerical values ranging from 0 to 0.02, marked in increments of 0.01 (0, 0.01, 0.02).
*   **X-axis Label:** The horizontal axis is labeled "Orientation (degrees)" and spans from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).

**4. Data Trends & Details:**
*   **Solid Line Trend (Upper Curve):** This line remains relatively flat across the orientation range. It hovers around a value of 0.012 to 0.014, showing minor fluctuations but maintaining a generally stable level across all orientations shown.
*   **Dashed Line Trend (Lower Curve):** This line is near zero for most of the range. It shows a distinct peak centered at 0 degrees, reaching approximately 0.01 on the y-axis before dropping back down to near zero at -45 and 45 degrees.


---

## Page 9

by using different spacings between the bars in the stimuli (Fig.
11g,h). The spacings used in the model are consistent with the
range of spacings used in the neurophysiological experiments.
Nothdurft et al. (1999) report that changing texture spacing af-
fects the strength of suppression but do not report a correlation
between texture spacing and the orientation contrast and uni-
form patterns of suppression. The behavior of the model can be
explained by the overlap of the surrounding texture with the RF
of the recorded neuron. The initial, linear, response of the model
to the texture with smaller spacing (Fig. 11g, inset) shows that
the iso-oriented texture provides slightly less afferent input to the
recorded neuron than the orthogonal texture, whereas for the
texture with larger spacing the initial, linear, response (Fig. 11h,
inset) shows that the iso-oriented texture provides more afferent
input than the orthogonal texture. In the full model, there is
strong competition to represent the contextual stimuli, which
results in a weaker response from the recorded neuron. However,
the average response still reflects the relative magnitudes of the
initial, linear, responses to each texture configuration. When the
surrounding texture is presented alone, the recorded neuron is a
poor representation of the input, so it quickly loses the competi-
tion and produces a very weak response.

Differences between the center and surround along other fea-
ture dimensions, such as contrast polarity, have also been found
to diminish the suppression caused by a textured surround (Fig.

11e). Consistent with the empirical data, the model shows (Fig.
11i) that center-surround differences in both dimensions (orien-
tation and contrast polarity) do not generate a greater reduction
in suppression than that generated by a single dimension. In the
model, changing the contrast polarity of the surround only has
the effect of changing the identity of those neurons that are most
strongly activated by that surround. The two sets of neurons
activated by the surround at each contrast polarity both have RFs
that overlap with the RF of the recorded neuron to a similar
degree, and hence both conditions generate a similar degree of
suppression in the recorded neuron.

Discussion
Previous work (Rao and Ballard, 1999) has shown that PC is
capable of modeling end-stopping behavior (similar to the result
shown in Fig. 5b) and texture “pop out” (similar to the result
shown in Fig. 11g). However, this previous work did not explore
whether PC could account for other V1 response properties, per-
haps because that work assumed that predictions arise from feed-
back from extrastriate areas and hence are only likely to be
involved in nonclassical RF properties. The interpretation of PC
described in this article assumes that predictions arise within V1
and that PC can be viewed as a form of competition. This inter-
pretation suggests that PC should also account for classical, as

60

Orientation (degrees)

0
90
−90
−45
45

Response

0

120

Centre Contrast

0.13
0.5
0 0.03
0

30

60

90

Centre Contrast

1
0.1
0.01
0

40

80

Surround Contrast

0.1
1
0.01
0

20

40

60

Contrast
0
0.01
0.1
1
0

10

20

Phase (degrees)

180
270
90
0

40

60

20

0
360

−90 −45
0
45
90
0

0.01

0.02

0.03

Orientation (degrees)

Response

0
0.03
0.13
0.5
0

0.01

0.02

Centre Contrast

0.01
0.1
1
0

0.01

0.02

0.03

Centre Contrast

0.01
0.1
1
0

0.01

0.02

0.03

Surround Contrast

0
0.01
0.1
1
0

0.01

0.02

0.03

Contrast

0
90
180 270 360
0

0.02

0.04

0.06

Phase (degrees)

a

b
c
d
e
f

Figure10.
Surroundsuppressionwithvariablecontrastandvariablesurroundphase.ThetoprowshowsneurophysiologicaldatafromrepresentativesinglecellsinV1,andthebottomrowshows
correspondingsimulationresults.a,Responseplottedasafunctionofgratingorientationrelativetothepreferredorientationoftheneuronforacentralgratingpresentedinisolation(dashedline),
as a function of the orientation of a surrounding annulus in the presence of an optimally oriented central grating (solid line), and as a function of surround orientation for a center contrast much
smallerthanthesurroundcontrast(dash-dotline).Thehorizontallinesshowtheresponsetothelow-contrastcenterstimuluspresentedaloneatthepreferredorientation.Shownareneurophys-
iologicaldataforacellinprimateV1[adaptedfromLevittandLund(1997),theirFig.1d].b,Responseasafunctionofthecontrastofthecentralgratinginthepresenceofaniso-orientedsurround.
ShownareneurophysiologicaldataforacellinprimateV1[adaptedfromCavanaughetal.(2002a),theirFig.5b].Thethicknessofeachlinecorrespondstothecontrastofthegratingintheannular
surround:0%(thinnest),3,6,12,25,and50%(thickest).c,Responseasafunctionofthecontrastofthecentralgratingwithnosurround(filledcircles),aniso-orientedsurround(opencircles),and
anorthogonalsurround(squares);inthelattertwocases,thesurroundcontrastwasfixedat50%.ShownareneurophysiologicaldataforasimplecellinprimateV1[adaptedfromCavanaughetal.
(2002b), their Fig. 5a]. d, Response as a function of the contrast of the surround grating with an iso-oriented surround (circles), and an orthogonal surround (squares); in both cases, the center
contrast was fixed at 40%. Shown are neurophysiological data for a cell in primate V1 [adapted from Webb et al. (2005), their Fig. 6]. e, Response as a function of the contrast of an orthogonal
surroundgratingsuperimposedonaniso-orientedsurroundgratinginthepresenceofanoptimallyorientedcenter.ShownareneurophysiologicaldataforacellincatV1[adaptedfromWalkeret
al. (2002), their Fig. 2b]. The contrast of the center and the iso-oriented surround were fixed at 30%. The horizontal lines indicate the response to the central grating in isolation. f, Response as a
functionofthephaseofthegratinginthesurround.ShownareneurophysiologicaldataforacellinprimateV1[adaptedfromXuetal.(2005),theirFig.2a].Thehorizontallinesindicatetheresponse
to the central grating in isolation.

Spratling • Predictive Coding Model of V1
J. Neurosci., March 3, 2010 • 30(9):3531–3543 • 3539



### 1. Top Graph (Upper Panel)
This panel displays a line graph with two sets of data plotted against orientation.

*   **Axes:**
    *   The **x-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
    *   The **left y-axis** is labeled "Response" and ranges from 0 to 120, marked in increments of 30 (0, 30, 60, 90, 120).
    *   The **right y-axis** is also labeled "Response" and ranges from 0 to 90, marked in increments of 30 (0, 30, 60, 90).

*   **Data Lines:** Two distinct lines are plotted:
    1.  A solid line (likely representing one response measure) shows a peak near 0 degrees, reaching approximately 90 on the right y-axis scale. It starts around 75 (left axis) at -90 degrees, dips to about 30 near -45 degrees, peaks around 85 at 0 degrees (using the right axis scale), and then rises again to about 90 at 45 degrees, before slightly decreasing towards 90 degrees.
    2.  A dashed line (likely representing a second response measure) shows a pattern that is generally lower than the solid line. It starts near 20 at -90 degrees, dips slightly below 10 around -45 degrees, peaks near 80 at 0 degrees (using the right axis scale), and then decreases towards 30 at 90 degrees.

### 2. Middle Graph (Middle Panel)
This panel displays a second line graph, similar in structure to the top one.

*   **Axes:**
    *   The **x-axis** is labeled "Orientation (degrees)" and ranges from -90 to 90 degrees, marked at intervals of 45 degrees (-90, -45, 0, 45, 90).
    *   The **left y-axis** is labeled "Response" and ranges from 0 to 0.03, marked in increments of 0.01 (0, 0.01, 0.02, 0.03).
    *   The **right y-axis** is also labeled "Response" and ranges from 0 to 0.02, marked in increments of 0.01 (0, 0.01, 0.02).

*   **Data Lines:** Two distinct lines are plotted:
    1.  A solid line shows a response that is relatively flat, hovering around 0.02 at -90 degrees and 90 degrees, with a slight dip near -45 degrees.
    2.  A dashed line shows a response that is low at the extremes (-90 and 90 degrees), dips to near zero around -45 degrees, peaks sharply near 0 degrees (reaching approximately 0.025 on the left axis scale, or slightly above 0.02 on the right axis scale), and then drops again towards zero at 90 degrees.

### 3. Bottom Panel (Stimuli Array)
This panel, labeled with the letter 'a', displays an array of visual stimuli.

*   **Structure:** The stimuli are arranged in a grid-like fashion, though the exact dimensions are not explicitly numbered.
*   **Stimuli Description:** The stimuli consist of patterns composed of parallel lines, presented in shades of gray against a lighter background.
    *   The array contains multiple small square patches, each displaying a different orientation or pattern of lines.
    *   Some stimuli show vertical lines, some horizontal lines, and others at intermediate angles (e.g., diagonal lines).
    *   The stimuli appear to be organized in rows and columns, showcasing variations in line orientation.
    *   To the far right of this array, there is a small cropped image showing a highly contrasted pattern, likely representing an extreme or specific stimulus condition.



### **Upper Plot Description**

**1. Overall Layout & Structure:**
The upper plot is a standard 2D line graph showing multiple data series plotted against a continuous x-axis.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Data Series:** There are multiple distinct lines, each representing a different data condition or measurement. These lines generally show an increasing trend as the x-axis value increases.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** "Centre Contrast"
*   **Y-Axis Label (Partial):** The y-axis scale is visible, ranging from 0 to approximately 95. A partial label on the right side indicates values like "80" and "60".
*   **X-Axis Ticks:** Labeled values include 0, 0.03, 0.13, and 0.5.

**4. Data Trends & Details:**
*   The data points for all plotted lines start near zero on the y-axis when the Centre Contrast is 0.
*   As the Centre Contrast increases, all lines exhibit a steep, positive correlation with the y-axis variable.
*   The lines diverge slightly as contrast increases, suggesting different rates of increase across the conditions represented by the multiple curves.

### **Lower Plot Description**

**1. Overall Layout & Structure:**
The lower plot is also a standard 2D line graph, positioned directly beneath the upper plot.

**2. Visual Components & Symbols:**
*   **Axes:** It features a horizontal x-axis and a vertical y-axis.
*   **Data Series:** Similar to the upper plot, there are multiple distinct lines representing different data series.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** "Centre Contrast" (Identical to the upper plot).
*   **Y-Axis Label (Partial):** The y-axis scale is visible, ranging from 0 to approximately 0.025. Partial labels on the right side indicate values like "0.02" and "0.01".
*   **X-Axis Ticks:** Labeled values include 0, 0.03, 0.13, and 0.5 (Identical to the upper plot).

**4. Data Trends & Details:**
*   The data points for all plotted lines start near zero on the y-axis when the Centre Contrast is 0.
*   Similar to the upper plot, all lines show a strong, positive correlation with the x-axis variable.
*   The curves appear to rise more gradually initially compared to the upper plot, but maintain a steep upward trajectory as Centre Contrast approaches 0.5.



### Overall Layout & Structure
The figure is structured into at least two main rows of plots, with the top row containing two distinct line graphs and the bottom row also containing at least two line graphs. The plots are presented side-by-side, suggesting a comparison between different experimental conditions or measures.

### Visual Components & Symbols
The plots utilize standard Cartesian coordinate systems with distinct axes for each graph. Data is represented by connected lines, suggesting continuous measurement or progression across the x-axis variable. Different data series are distinguished by different line styles and/or markers (though specific marker details are not fully discernible, the presence of multiple lines is clear).

### Labels, Keys & Legends
**Axes Labels:**
*   The x-axis across all visible plots is labeled **"Centre Contrast"**. The scale appears to be logarithmic, ranging from $0.01$ up to $1$.
*   The y-axes vary between the panels:
    *   In the top-left plot, the left y-axis ranges from $0$ to approximately $100$.
    *   In the top-right plot, both the left and right y-axes range from $0$ to $60$.
    *   In the bottom-left plot, the left y-axis ranges from $0$ to $0.03$.
    *   In the bottom-right plot, both the left and right y-axes range from $0$ to $0.03$.

**Data Trends & Details (Focusing on the visible plots):**

**Top-Left Plot:**
*   This plot shows multiple lines rising as the Centre Contrast increases. The data points appear to cluster around different levels, suggesting distinct conditions being compared.
*   The lines show a clear positive correlation: as Centre Contrast increases from $0.01$ towards $1$, the measured value on the y-axis generally increases for all plotted lines.

**Top-Right Plot:**
*   This plot displays at least two distinct curves plotted against Centre Contrast.
*   One curve (likely represented by the higher values) shows a steep increase, reaching near $60$ as contrast approaches $1$.
*   Another curve shows a more gradual increase, reaching around $40$ at the highest contrast levels.

**Bottom-Left Plot:**
*   This plot shows multiple lines tracking a small range on the y-axis (up to $0.03$).
*   Similar to the top plots, these lines exhibit a positive trend as Centre Contrast increases.

**Bottom-Right Plot:**
*   This plot also shows multiple lines tracking a small range on the y-axis (up to $0.03$).
*   The curves demonstrate a clear, non-linear increase in the measured variable as Centre Contrast increases.

### Contextual Caption Integration
The figure includes small inset images below the plots, which appear to be schematic representations of visual stimuli (e.g., patterns or gratings) corresponding to the different contrast levels, although these are not explicitly linked via labels in the provided view. The presence of multiple plots strongly suggests a comparative analysis across different experimental parameters (e.g., stimulus type, neural population response).



### Top Graph Description

**1. Overall Layout & Structure:**
The top section is a standard 2D line plot comparing two different datasets across a range of values on the x-axis.

**2. Visual Components & Symbols:**
*   There are two distinct data series plotted, represented by different markers and lines.
*   The x-axis is horizontal, and the y-axis is vertical.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** "Surround Contrast" (The scale ranges from 0.01 to 1, marked logarithmically).
*   **Y-Axis Label (Left):** No explicit label is visible, but the scale ranges from 0 to 60.
*   **Y-Axis Label (Right):** A secondary y-axis is present on the right side, with a scale ranging from 0 to approximately 25 (though the tick marks are small).

**4. Data Trends & Details:**
*   **Series 1 (Upper Curve):** This series is represented by a line connecting data points, likely marked with squares or circles (though markers are small). It starts high on the left (around 55-60 at Contrast = 0.01) and shows a general decreasing trend as Surround Contrast increases, leveling off around 40 at Contrast = 1.
*   **Series 2 (Lower Curve):** This series is represented by a line connecting data points. It starts lower than Series 1 (around 50 at Contrast = 0.01) and exhibits a steeper decline than Series 1, dropping significantly as Contrast increases, reaching values near 5-10 at Contrast = 1.

### Bottom Graph Description

**1. Overall Layout & Structure:**
The bottom section is another 2D line plot, structurally identical to the top graph.

**2. Visual Components & Symbols:**
*   Two distinct data series are plotted.
*   The x-axis is horizontal, and the y-axis is vertical.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** "Surround Contrast" (The scale ranges from 0.01 to 1, marked logarithmically).
*   **Y-Axis Label (Left):** No explicit label is visible, but the scale ranges from 0 to 0.03.
*   **Y-Axis Label (Right):** A secondary y-axis is present on the right side, with a scale ranging from 0.0 to 0.1 (with major ticks at 0.0, 0.05, and 0.1).

**4. Data Trends & Details:**
*   **Series 1 (Upper Curve):** This series starts around 0.02 at Contrast = 0.01 and shows a gradual, shallow decline across the range, ending near 0.015 at Contrast = 1.
*   **Series 2 (Lower Curve):** This series starts around 0.018 at Contrast = 0.01 and shows a more pronounced, steady decline across the range, ending near 0.005 at Contrast = 1.



### Top Plot Description
The top plot is a scatter/line graph displaying data across varying contrast levels.

*   **Axes:**
    *   The **x-axis** is labeled "Contrast" and uses a logarithmic scale, ranging from 0 to 1.
    *   The **y-axis** is numerical, ranging from 0 to approximately 25 (with major ticks at 0, 10, and 20).
*   **Data Representation:** A series of data points connected by a line is plotted. The curve exhibits a sigmoidal or S-shaped trend:
    *   At low contrast values (e.g., 0 to $\approx 0.03$), the data points are clustered near the baseline (y-values close to 0).
    *   As contrast increases past $\approx 0.1$, the curve rises steeply, showing a rapid increase in the measured variable (y-axis value).
    *   At the highest contrast shown ($\approx 0.5$ to $1.0$), the curve appears to plateau or continue rising moderately, reaching a peak value around 12-13.
*   **Annotations:** There is a horizontal line drawn across the top of the plotting area, positioned at a high y-value (around 25), which may represent a saturation or maximum threshold.

### Bottom Plot Description
The bottom plot is also a scatter/line graph, structurally similar to the top plot but displaying different data trends.

*   **Axes:**
    *   The **x-axis** is labeled "Contrast" and uses a logarithmic scale, ranging from 0 to 1.
    *   The **y-axis** is numerical, ranging from 0 to approximately 0.03 (with major ticks at 0, 0.01, 0.02, and 0.03).
*   **Data Representation:** A series of data points connected by a line is plotted. This curve shows a much shallower, more gradual increase compared to the top plot:
    *   At low contrast values (e.g., 0 to $\approx 0.1$), the data points are relatively flat, hovering around a baseline value slightly above zero (approximately 0.007 to 0.008).
    *   As contrast increases beyond $\approx 0.1$, the curve begins a slow, steady ascent.
    *   At the highest contrast shown ($\approx 0.5$ to $1.0$), the curve reaches its peak, approaching a value around 0.015.
*   **Annotations:** Similar to the top plot, there is a horizontal line drawn across the top of this plotting area, positioned at $y=0.03$, likely indicating a maximum threshold for this measurement.



### Panel 1: Top Line Graph
This panel displays a line graph showing a cyclical trend.

*   **Axes:**
    *   The **x-axis** is labeled "Phase (degrees)" and ranges from 0 to 360, marked in increments of 90 degrees.
    *   The **y-axis** is scaled from 0 to 60, with major tick marks at intervals of 20 (0, 20, 40, 60).
*   **Data Trend:** A single curve is plotted. The data starts low, rises sharply to a peak around 120-180 degrees (reaching approximately 55-60 on the y-axis), and then gradually declines, reaching a lower value near 360 degrees.
*   **Annotations:** A horizontal black line is drawn across the top of the plot, positioned near the 60 mark on the y-axis.

### Panel 2: Middle Line Graph
This panel also displays a line graph, showing another cyclical trend.

*   **Axes:**
    *   The **x-axis** is labeled "Phase (degrees)" and ranges from 0 to 360, marked in increments of 90 degrees.
    *   The **y-axis** is scaled from 0 to 0.06, with major tick marks at intervals of 0.02 (0, 0.02, 0.04, 0.06).
*   **Data Trend:** A single curve is plotted. This curve shows a rise from near zero at 0 degrees, peaks around 120-180 degrees (reaching approximately 0.045 on the y-axis), and then declines symmetrically, returning close to zero by 360 degrees.
*   **Annotations:** A horizontal black line is drawn across the top of this plot, positioned near the 0.05 mark on the y-axis.

### Panel 3: Bottom Schematic Diagram
This panel contains a schematic representation, likely illustrating neural activity or connectivity across different phases.

*   **Structure:** It consists of a horizontal arrangement of four distinct, rectangular/square-like modules or regions.
*   **Internal Elements:** Each module contains a gray background with internal patterns:
    *   The first module (leftmost) has a pattern of small, light gray circles on a darker background.
    *   The second module has a pattern of horizontal black and white stripes.
    *   The third module has a pattern of small, light gray circles on a darker background (similar to the first).
    *   The fourth module has a pattern of diagonal black and white stripes.
*   **Contextual Elements:** Above the modules, there are small, faint gray circles positioned above each module, suggesting points of interest or activity associated with the modules below.


---

## Page 10

well as nonclassical, RF properties, as has
been demonstrated here.

The specific predictive coding model
implemented in this article (PC/BC) em-
ploys a divisive mechanism to calculate
the residual error between the predictions
and the sensory input. This mechanism
can be interpreted as a form of divisive
normalization like that proposed by the
normalization model (Albrecht and Geisler,
1991; Heeger, 1991, 1992; Carandini and
Heeger, 1994; Wainwright et al., 2001).
However, unlike the normalization model,
in PC/BC the normalization pool for each
neuron is restricted to the population of
neurons that have overlapping RFs, and
the normalization is applied to the inputs
to the population of competing neurons
rather than the outputs. The normaliza-
tion model is capable of simulating a sub-
set of the results presented here (Heeger,
1994; Heeger et al., 1996; Schwartz and
Simoncelli, 2001) and has also been re-
cently extended (Reynolds and Heeger,
2009) to model a subset of the atten-
tional data that can be simulated by
PC/BC (Spratling, 2008a). However,
since the weights used to pool the re-
sponses, and so calculate the strength of
normalization, are not specified by the
normalization model, it has many more
free parameters than PC/BC. As with the
normalization model (Schwartz and Simoncelli, 2001; Wain-
wright et al., 2001), PC/BC reduces redundancy between neu-
ral representations (Fig. 12).

There are many other models that can simulate individual
results presented here (Douglas and Martin, 1991; Ben-Yishai et
al., 1995; Somers et al., 1995; Carandini and Ringach, 1997;
Troyer et al., 1998; Adorja´n et al., 1999; Dragoi and Sur, 2000;

0

10

20

30

Response

a

0

10

20

30

40

50

b

0

10

20

30

c

0

10

20

30

d

0

0.5

1

Normalized Response

e

0

1

2

3

4

5
x 10

−3

Response

f

0

0.5

1

1.5

x 10

−3

g

0

0.5

1

1.5

x 10

−3

h

0

0.5

1

1.5

x 10

−3

Response

i

Figure11.
Theeffectofflankersandtexturedsurroundsonneuralresponse.a,ResponsetoonesetofflankerconfigurationsofasinglecellinprimateV1[adaptedfromKapadiaetal.(2000),their
Fig.7a].b,ResponsetoasecondsetofflankerconfigurationsofadifferentcellinprimateV1[adaptedfromKapadiaetal.(1995),theirFig.11a].c,Averageresponseof28cellsinprimateV1that
were classified as orientation contrast cells [adapted from Nothdurft et al. (1999), their Fig. 4a]. d, Average response of 14 cells in primate V1 that were classified as uniform cells [adapted from
Nothdurftetal.(1999),theirFig.4b].e,Averageresponseof124cellsinprimateV1totexturedsurroundswithvaryingcontrast[adaptedfromvanderSmagtetal.(2005),theirFig.4a].f,Response
ofamodelneurontobothsetsofflankerconfigurationsshowninaandb.g,Responseofamodelneurontotexturepatternslikethoseincandd,inwhichthespacingbetweenbarswas1.6times
thebarlength.h,Responseofamodelneurontosimilartexturepatternscreatedusingaspacingoftwotimesthebarlength.Theinsetstogandhshowthelinearresponseofthemodelforthetwo
differenttexturespacings.i,Responseofamodelneurontotexturepatternswithvaryingcontrast,asusedine.Note:Theiconsusedtorepresentthestimulusconfigurationsinc–eandg–ishow
only the central portion of the actual images used in the experiments.

0
0.002 0.004

0.004

0.002

0
0
0.002 0.004

0.004

0.002

0
0
0.002 0.004

0.004

0.002

0

Response neuron 2

0
0.004 0.009

0.009

0.004

0

Response neuron 1

0
0.004 0.009

0.009

0.004

0
0
0.007 0.014

0.014

0.007

0

Figure 12.
Conditional probability histograms of responses to a natural image. In each histogram, a column indicates the
probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the
magnitude shown on the abscissa. A dark pixel indicates a high conditional probability. Each column in each histogram has been
independentlyrescaledtofillthefullrangeofintensityvalues.Thetoprowshowshistogramsfortheinitiallinearresponseofthe
model (without competition). The bottom row shows histograms for the model including inhibition. Histograms in the left-hand
column are for two neurons tuned to the same orientation but 2 pixels apart, so that RFs are parallel. Histograms in the
middle column are for two neurons tuned to the same orientation but 6 pixels apart, so that RFs are parallel. Histograms in
theright-handcolumnarefortwoneuronstunedtoorthogonaldirectionsatthesamelocation.Itcanbeseenthat,without
competition, the responses are correlated such that the higher the response at the first neuron, the higher the response is
likely to be from the second neuron. It is also the case that all neurons tend to generate strong responses. After competition
has occurred, the responses are much more sparse (fewer neurons generate strong responses), and the dependency
between different neurons is substantially reduced, and for neurons at the same location (bottom-right histogram) the
correlationiseliminated.Theimageusedtogeneratethesehistogramswasimagenumber23fromthestillimagedatabase
used in the study by van Hateren and van der Schaaf (1998).

> Figure caption (from PDF text): Figure 12.
Conditional probability histograms of responses to a natural image. In each histogram, a column indicates the
probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the
magnitude shown on the abscissa. A dark pixel indicates a high conditional probability. Each column in each histogram has been
independentlyrescaledtofillthefullrangeofintensityvalues.Thetoprowshowshistogramsfortheinitiallinearresponseofthe
model (without competition). The bottom row shows histograms for the model including inhibition. Histograms in the left-hand
column are for two neurons tuned to the same orientation but 2 pixels apart, so that RFs are parallel. Histograms in the
middle column are for two neurons tuned to the same orientation but 6 pixels apart, so that RFs are parallel. Histograms in
theright-handcolumnarefortwoneuronstunedtoorthogonaldirectionsatthesamelocation.Itcanbeseenthat,without
competition, the responses are correlated such that the higher the response at the first neuron, the higher the response is
likely to be from the second neuron. It is also the case that all neurons tend to generate strong responses. After competition
has occurred, the responses are much more sparse (fewer neurons generate strong responses), and the dependency
between different neurons is substantially reduced, and for neurons at the same location (bottom-right histogram) the
correlationiseliminated.Theimageusedtogeneratethesehistogramswasimagenumber23fromthestillimagedatabase
used in the study by van Hateren and van der Schaaf (1998).


## Figure Description

The image displays a set of conditional probability histograms, arranged in a grid structure. Although the full layout is not visible, the snippet shows at least two rows and multiple columns of these histograms.

### 1. Overall Layout & Structure
The figure is composed of multiple small, heat-map style plots (histograms). The caption indicates a $2 \times N$ arrangement, where the rows differentiate between model conditions (with and without competition), and the columns differentiate based on the spatial arrangement of the neurons being compared.

*   **Rows:** The top row represents histograms for the "initial linear response of the model (without competition)." The bottom row represents histograms for the "model including inhibition" (competition).
*   **Columns:** The columns represent different spatial configurations:
    *   Left-hand column: Two neurons tuned to the same orientation but 2 pixels apart (parallel RFs).
    *   Middle column: Two neurons tuned to the same orientation but 6 pixels apart (parallel RFs).
    *   Right-hand column: Two neurons tuned to orthogonal directions at the same location.

### 2. Visual Components & Symbols
Each individual plot is a 2D heatmap representing conditional probability:

*   **Axes:** The horizontal axis (abscissa) represents the output magnitude of Neuron 1. The vertical axis represents the output magnitude of Neuron 2.
*   **Color Coding:** The plots use a grayscale color scale, where "A dark pixel indicates a high conditional probability." This suggests that darker shades correspond to higher probabilities.
*   **Data Representation:** The plots are histograms, showing $P(\text{Neuron 2 output} | \text{Neuron 1 output})$.

### 3. Labels, Keys & Legends
*   **Axes Labels (Partial):** The x-axis labels visible in the snippet range from $0$ to $0.009$. The y-axis labels are partially visible, showing values like $0$ and $0.04$, up to $0.09$.
*   **Annotations:** The caption clarifies the meaning of the axes: "a column indicates the probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the magnitude shown on the abscissa."

### 4. Data Trends & Details (Based on Visible Snippet)
The visible portion of the plots shows distinct trends:

*   **Bottom Row (With Inhibition):** The bottom-most visible histogram shows a very dark, dense band concentrated near the zero output magnitude on both axes. This suggests that when competition is present, there is a high probability of low responses for both neurons in the configuration shown.
*   **Top Row (Without Competition):** The top-most visible histogram shows a lighter, more diffuse distribution compared to the bottom row.

### 5. Contextual Caption Integration
The caption provides critical interpretation of the observed trends:

*   **Without Competition (Top Row):** Responses are correlated; higher response in Neuron 1 is likely associated with a higher response from Neuron 2. Furthermore, all neurons tend to generate strong responses (implied by the overall distribution).
*   **With Competition (Bottom Row):** Responses become "much more sparse" (fewer strong responses), the dependency between neurons is substantially reduced, and for neurons at the same location (bottom-right histogram), the correlation is eliminated.
*   **Normalization:** It is noted that "Each column in each histogram has been independently rescaled to fill the full range of intensity values."

> Figure caption (from PDF text): Figure 12.
Conditional probability histograms of responses to a natural image. In each histogram, a column indicates the
probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the
magnitude shown on the abscissa. A dark pixel indicates a high conditional probability. Each column in each histogram has been
independentlyrescaledtofillthefullrangeofintensityvalues.Thetoprowshowshistogramsfortheinitiallinearresponseofthe
model (without competition). The bottom row shows histograms for the model including inhibition. Histograms in the left-hand
column are for two neurons tuned to the same orientation but 2 pixels apart, so that RFs are parallel. Histograms in the
middle column are for two neurons tuned to the same orientation but 6 pixels apart, so that RFs are parallel. Histograms in
theright-handcolumnarefortwoneuronstunedtoorthogonaldirectionsatthesamelocation.Itcanbeseenthat,without
competition, the responses are correlated such that the higher the response at the first neuron, the higher the response is
likely to be from the second neuron. It is also the case that all neurons tend to generate strong responses. After competition
has occurred, the responses are much more sparse (fewer neurons generate strong responses), and the dependency
between different neurons is substantially reduced, and for neurons at the same location (bottom-right histogram) the
correlationiseliminated.Theimageusedtogeneratethesehistogramswasimagenumber23fromthestillimagedatabase
used in the study by van Hateren and van der Schaaf (1998).


## Figure Description

The image displays a set of conditional probability histograms, arranged in a grid structure. Although the full layout is not visible, the caption describes a $2 \times 3$ arrangement of histograms (two rows and three columns).

### 1. Overall Layout & Structure
The figure is composed of multiple individual histograms, organized into rows and columns to compare different experimental conditions.
*   **Rows:** The caption specifies two rows: the top row represents histograms for the model *without competition*, and the bottom row represents histograms for the model *including inhibition*.
*   **Columns:** The caption specifies three columns, each representing a different spatial arrangement of the neurons being analyzed:
    *   Left-hand column: Two neurons tuned to the same orientation but 2 pixels apart (parallel RFs).
    *   Middle column: Two neurons tuned to the same orientation but 6 pixels apart (parallel RFs).
    *   Right-hand column: Two neurons tuned to orthogonal directions at the same location.

### 2. Visual Components & Symbols
Each individual panel is a heatmap or binned histogram, where the color intensity represents probability.

*   **Color Coding:** The caption states: "A dark pixel indicates a high conditional probability." This implies that the color scale ranges from light/white (low probability) to dark/black (high probability).
*   **Axes:** Each histogram has an abscissa (x-axis) and a vertical axis (y-axis).
    *   **X-Axis (Abscissa):** Represents the magnitude of the output from Neuron 1. The visible tick marks show values ranging from $0$ up to $0.009$.
    *   **Y-Axis:** Represents the magnitude of the output from Neuron 2. The visible tick marks show values ranging from $0$ up to $0.09$.

### 3. Labels, Keys & Legends
*   **Axis Labels:** The x-axis is labeled with numerical values (e.g., $0, 0.004, 0.009$). The y-axis is labeled with numerical values (e.g., $0, 0.04, 0.09$).
*   **Annotations:** The caption provides the context for interpreting these axes: "a column indicates the probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the magnitude shown on the abscissa."
*   **Rescaling Note:** The caption notes that "Each column in each histogram has been independently rescaled to fill the full range of intensity values."

### 4. Data Trends & Details (Based on Visible Snippet)
The visible snippet shows a section of the histograms, particularly focusing on the lower range of the axes.

*   **General Trend (Visible):** In the visible panels, there is a clear gradient of color intensity across both axes. The darkest pixels (highest probability) appear concentrated near the bottom edge ($y \approx 0$) and across a range of x-values.
*   **Top Row vs. Bottom Row:** The caption implies a qualitative difference between the top row (no competition) and the bottom row (with inhibition), which would be observable by comparing the overall distribution of dark pixels between the two rows.
*   **Correlation Observation (from Caption):** The caption highlights that *without competition* (top row), responses are correlated such that higher response in Neuron 1 leads to a higher likelihood of response from Neuron 2. *After competition* (bottom row), responses are described as much more sparse, and dependency is substantially reduced.

### 5. Contextual Caption Integration
The figure illustrates the conditional probability distributions $P(\text{Neuron 2 output} | \text{Neuron 1 output})$ under different model conditions (with/without inhibition) and spatial configurations of the neurons. The data is derived from a specific natural image (image number 23).

> Figure caption (from PDF text): Figure 12.
Conditional probability histograms of responses to a natural image. In each histogram, a column indicates the
probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the
magnitude shown on the abscissa. A dark pixel indicates a high conditional probability. Each column in each histogram has been
independentlyrescaledtofillthefullrangeofintensityvalues.Thetoprowshowshistogramsfortheinitiallinearresponseofthe
model (without competition). The bottom row shows histograms for the model including inhibition. Histograms in the left-hand
column are for two neurons tuned to the same orientation but 2 pixels apart, so that RFs are parallel. Histograms in the
middle column are for two neurons tuned to the same orientation but 6 pixels apart, so that RFs are parallel. Histograms in
theright-handcolumnarefortwoneuronstunedtoorthogonaldirectionsatthesamelocation.Itcanbeseenthat,without
competition, the responses are correlated such that the higher the response at the first neuron, the higher the response is
likely to be from the second neuron. It is also the case that all neurons tend to generate strong responses. After competition
has occurred, the responses are much more sparse (fewer neurons generate strong responses), and the dependency
between different neurons is substantially reduced, and for neurons at the same location (bottom-right histogram) the
correlationiseliminated.Theimageusedtogeneratethesehistogramswasimagenumber23fromthestillimagedatabase
used in the study by van Hateren and van der Schaaf (1998).


## Figure Description

The image displays a set of conditional probability histograms, arranged in a grid structure. Although the full grid is not visible, the provided snippet shows at least one row and a portion of the x-axis scale.

### 1. Overall Layout & Structure
The figure is composed of multiple histograms arranged in a matrix format, as described by the caption: "The top row shows histograms for the initial linear response of the model (without competition). The bottom row shows histograms for the model including inhibition." Furthermore, there are three columns of these histograms:
*   **Left-hand column:** For two neurons tuned to the same orientation but 2 pixels apart (parallel RFs).
*   **Middle column:** For two neurons tuned to the same orientation but 6 pixels apart (parallel RFs).
*   **Right-hand column:** For two neurons tuned to orthogonal directions at the same location.

The visible snippet shows a single histogram, which represents one specific condition within this matrix structure.

### 2. Visual Components & Symbols
The primary visual element is a histogram represented by colored pixels, where the intensity of the color indicates probability.
*   **Color Coding:** The caption specifies that "A dark pixel indicates a high conditional probability." The visible histogram shows a gradient: the left side is light gray/white, transitioning to a dark black bar on the right.
*   **Axes:** The plot uses standard Cartesian coordinates:
    *   The **x-axis (abscissa)** represents the magnitude of the output from Neuron 1.
    *   The **y-axis** represents the conditional probability (though the scale is not fully visible, it ranges from 0 up to a maximum value).

### 3. Labels, Keys & Legends
*   **X-Axis Labeling:** The x-axis is labeled with numerical values: `0`, `0.007`, and `0.014`.
*   **Y-Axis Labeling:** The y-axis shows numerical markers: `0` and `0.07`, with a higher tick mark visible at `0.14`.
*   **Annotation:** The caption clarifies the meaning of the axes: "In each histogram, a column indicates the probability that neuron 2 generates an output of the given magnitude given that neuron 1 has generated an output of the magnitude shown on the abscissa."

### 4. Data Trends & Details (Visible Snippet)
The visible histogram exhibits a clear trend:
*   For low magnitudes on the x-axis (near 0), the conditional probability is very low (light gray/white).
*   As the magnitude on the x-axis increases, the conditional probability rises sharply, culminating in a dark black bar spanning from approximately $x \approx 0.01$ to $x = 0.014$. This indicates a high conditional probability for Neuron 2 to generate a strong output when Neuron 1 generates a large output, particularly in the condition represented by this specific plot.

### 5. Contextual Caption Integration
The caption provides crucial context for interpreting the visual data:
*   **Data Type:** The histograms show **Conditional probability distributions**.
*   **Normalization:** "Each column in each histogram has been independently rescaled to fill the full range of intensity values."
*   **Interpretation (General):** The caption notes that *without competition* (top row), responses are correlated such that "the higher the response at the first neuron, the higher the response is likely to be from the second neuron."
*   **Interpretation (Post-Competition):** *After competition* (bottom row), responses are "much more sparse," and the dependency between neurons is "substantially reduced."
*   **Specific Example:** The image used to generate these histograms was "image number 23 from the still image database used in the study by van Hateren and van der Schaaf (1998)."

3540 • J. Neurosci., March 3, 2010 • 30(9):3531–3543
Spratling • Predictive Coding Model of V1



**1. Overall Layout & Structure:**
The figure consists of a single plot area, which is a grayscale heatmap. The axes are clearly defined with numerical labels indicating the range of the variables being plotted.

**2. Visual Components & Symbols:**
The plot uses a grayscale color gradient where darker shades (approaching black) indicate higher values or density, and lighter shades (approaching white) indicate lower values. The intensity distribution is not uniform; it shows a clear gradient pattern across the plotted domain.

**3. Labels, Keys & Legends:**
*   **Y-Axis Labeling:** The vertical axis is labeled with numerical values: `0`, `0.02`, and `0.04`. The unit or variable represented by this axis is not explicitly labeled in the visible portion of the image.
*   **X-Axis Labeling:** The horizontal axis is labeled with numerical values: `0`, `0.002`, and `0.004`. The unit or variable represented by this axis is not explicitly labeled in the visible portion of the image.

**4. Data Trends & Details:**
The heatmap displays a distinct trend:
*   In the upper-left quadrant (low X, high Y), the color is predominantly dark gray to black, indicating high values.
*   As one moves towards the bottom-right corner (high X, low Y), the color transitions to very light gray and white, indicating low values.
*   There is a clear diagonal gradient sloping from the upper-left to the lower-right, suggesting that the relationship between the two variables is inversely correlated or that the density decreases as both variables increase.

**5. Contextual Caption Integration:**
No caption text was provided, so no specific contextual integration can be performed. The description is limited to the visual elements present in the image itself.



**1. Overall Layout & Structure:**
The figure consists of a single plot area, which is a grayscale heatmap. The axes are clearly defined with numerical labels, indicating that the plot visualizes data as a function of two continuous variables.

**2. Visual Components & Symbols:**
The plot uses grayscale intensity to represent data values:
*   **Darker Shades (Black/Dark Gray):** Represent higher values or higher density in the visualized data.
*   **Lighter Shades (White/Light Gray):** Represent lower values or lower density.
*   The data distribution is concentrated in the upper-left quadrant of the plotted area, showing a gradient where intensity decreases as both x and y values increase.

**3. Labels, Keys & Legends:**
*   **Y-Axis Labeling (Vertical Axis):** The y-axis is labeled with numerical values: `0`, `0.02`, and `0.04`. The unit is not explicitly stated next to the axis label, but the values suggest a normalized or scaled quantity.
*   **X-Axis Labeling (Horizontal Axis):** The x-axis is labeled with numerical values: `0`, `0.002`, and `0.004`. The unit is not explicitly stated next to the axis label.

**4. Data Trends & Details:**
The plot exhibits a clear gradient:
*   The highest intensity (darkest gray/black) is observed near the origin, specifically in the region where $y$ is close to $0.04$ and $x$ is close to $0$.
*   As the x-value increases (moving right), the intensity rapidly decreases, transitioning from dark gray to light gray/white.
*   As the y-value increases (moving up), the intensity remains high in the upper region ($y \approx 0.04$) before gradually fading towards lighter shades as $y$ approaches $0.02$.

**5. Contextual Caption Integration:**
No specific contextual caption or legend is provided alongside the image, so no interpretation regarding cell types, layers, or specific variables can be made beyond what is visible on the axes. The figure strictly displays a bivariate distribution map where high values are concentrated in the upper-left corner of the plotted domain.



**1. Overall Layout & Structure:**
The figure consists of a single plot area, structured as a matrix or heatmap. It does not contain multiple panels (A, B, C, etc.). The visualization style is a grayscale intensity plot.

**2. Visual Components & Symbols:**
The primary visual component is the color gradient filling the plotting area. The intensity ranges from dark black to white, indicating varying levels of a measured variable across the defined axes.

*   **Color Gradient:** The color transitions from dark (high intensity) in the upper-left corner to light/white (low intensity) towards the bottom-right.
*   **Data Distribution:** The highest concentration of data (darkest shades) is clustered in the upper-left quadrant, while the intensity rapidly decreases as one moves down and to the right.

**3. Labels, Keys & Legends:**
The figure includes labeled axes:

*   **Y-axis (Vertical Axis):** The axis is scaled with numerical values. Visible ticks include $0$, $0.02$, and $0.04$. The label for this axis is not explicitly provided in the visible area but represents a continuous variable.
*   **X-axis (Horizontal Axis):** The axis is scaled with numerical values. Visible ticks include $0$, $0.002$, and $0.004$. The label for this axis is not explicitly provided in the visible area but represents a continuous variable.

**4. Data Trends & Details:**
The plot clearly shows a strong negative correlation or decay trend:

*   **High Values Region:** The region where the Y-axis value is high (approaching $0.04$) and the X-axis value is low (approaching $0$) exhibits the highest data density, represented by dark gray/black shading.
*   **Low Values Region:** As the X-axis value increases (moving towards $0.004$) or as the Y-axis value decreases (moving towards $0$), the intensity rapidly fades to white, indicating low data density or magnitude.

**5. Contextual Caption Integration:**
No caption text was provided, so no specific contextual elements (like cell types or feedback loops) can be identified. The description is based purely on the visual structure of the heatmap plot.



**1. Overall Layout & Structure:**
The figure consists of a single plot area featuring two vertical axes: a primary Y-axis on the left and a secondary Y-axis on the right. The X-axis represents distinct categories, each associated with a bar structure that includes both a dark gray upper portion and a light gray lower portion.

**2. Visual Components & Symbols:**
*   **Bars:** There are five distinct vertical bar structures along the X-axis. Each structure is composed of two stacked rectangular segments: a dark gray segment on top and a light gray segment at the bottom.
*   **Axes:** The X-axis is categorical, showing five positions. The Y-axes are numerical scales.
*   **Color Coding:** Dark gray represents the primary measured value, while light gray appears to represent a baseline or secondary measurement.

**3. Labels, Keys & Legends:**
*   **Y-Axis (Left):** Labeled "troopcombo" with numerical markings at 0, 10, 20, and 30.
*   **Y-Axis (Right):** Labeled with numerical markings at 0, 10, 20, 30, 40, and 50.
*   **X-Axis Labels:** The categories along the X-axis are not explicitly labeled with text in the provided crop, but they correspond to five distinct data points.

**4. Data Trends & Details:**
The height of the bars indicates the measured values:

*   **Bar 1 (Leftmost):** The dark gray portion reaches approximately 16 on the left Y-axis. The light gray portion is very small, near zero.
*   **Bar 2:** This bar shows the highest value. The dark gray portion reaches approximately 34 on the left Y-axis, and the light gray portion is also present but smaller than the dark segment.
*   **Bar 3:** The dark gray portion reaches approximately 12 on the left Y-axis. The light gray portion is small, near zero.
*   **Bar 4:** This bar shows a very low value; the dark gray portion is near zero, and the light gray portion is also minimal.
*   **Bar 5 (Rightmost):** The dark gray portion reaches approximately 8 on the left Y-axis. The light gray portion is small, near zero.

**5. Contextual Caption Integration:**
No specific contextual caption information is provided to interpret the meaning of "troopcombo" or the nature of the stacked segments, so interpretation is limited to structural description.



**1. Overall Layout & Structure:**
The figure consists of a single plot, which is a vertical bar chart. The data is presented across multiple categories along the horizontal axis (x-axis), and the magnitude of the measured variable is represented by the height of the bars along the vertical axis (y-axis).

**2. Visual Components & Symbols:**
*   **Bars:** There are six distinct vertical bars, grouped sequentially along the x-axis. The bars appear to be dark gray/black in color.
*   **X-Axis Annotations:** Below each bar, there is a small label indicating the experimental condition. These labels consist of a dash ($\text{-}$) or a plus sign ($\text{+}$) enclosed within a light gray rectangular box.
*   **Y-Axis:** The vertical axis is labeled with numerical values, ranging from 0 up to 50. Tick marks are present at intervals of 10 (0, 10, 20, 30, 40, 50).
*   **Secondary Y-Axis:** To the right of the main plot, there is a secondary vertical axis with numerical labels (e.g., 10, 20, 30), suggesting a second scale or measurement is being referenced, although no corresponding data lines are visible against this axis in the provided crop.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label (Left):** The primary vertical axis is labeled with numerical values: 0, 10, 20, 30, 40, 50.
*   **X-Axis Labels (Conditions):** The conditions below the bars are:
    1.  $\text{-}$
    2.  $\text{--}$ (Double dash)
    3.  $\text{+}$
    4.  $\text{|}$ (Vertical bar/pipe symbol)
    5.  $\text{-}$
    6.  $\text{-}$

**4. Data Trends & Details:**
The heights of the bars indicate the following approximate values:
*   Bar 1 ($\text{-}$): Approximately 26 units.
*   Bar 2 ($\text{--}$): The tallest bar, reaching approximately 51 units.
*   Bar 3 ($\text{+}$): Approximately 24 units.
*   Bar 4 ($\text{|}$): Very low, close to 1 unit.
*   Bar 5 ($\text{-}$): Very low, slightly above 0 (approximately 1 unit).
*   Bar 6 ($\text{-}$): Very low, similar to Bar 5 (approximately 1 unit).

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no interpretation based on external context can be offered. The figure visually compares a measured quantity across six distinct experimental conditions defined by the symbols ($\text{-}$, $\text{--}$, $\text{+}$, $\text{|}$).


---

## Page 11

Stetter et al., 2000) (for review, see Ferster and Miller, 2000; Serie`s
et al., 2003), and many of these models employ mechanisms sim-
ilar to those used by PC/BC. However, the PC/BC model differs
from these previous models in providing a computational expla-
nation for the behavior of V1 neurons as well as providing a
unified account of a number of processes that are currently con-
sidered, and modeled, in isolation. The model also makes testable
predictions that are described in the supplemental material
(available at www.jneurosci.org).

Consistent with previous models and neurophysiological re-
sults (Pei et al., 1994; Sompolinsky and Shapley, 1997; Xing et al.,
2005), orientation tuning in the PC/BC model results from
broadly tuned afferent excitation being sharpened by intracorti-
cal competition. This is also consistent with evidence that block-
ing inhibitory effects across a local population of cortical cells
greatly reduces orientation selectivity (Sillito, 1975; Tsumoto et
al., 1979; Sato et al., 1996). In the model, blockade of inhibition
from neurons with a specific orientation preference should cause
neighboring prediction neurons to show increased response to
that orientation, rather than simply causing a general disinhibi-
tion to all orientations. Such effects have been recorded in V1
(Crook et al., 1998), and analogous data have been obtained from
cortical area TE (Wang et al., 2000). The current model is also
consistent with neurophysiological evidence that the strength of
lateral inhibition peaks for stimuli presented at the preferred ori-
entation of the recorded cortical cell (Ferster, 1986; Douglas et al.,
1991; Sato et al., 1996; Sompolinsky and Shapley, 1997). In the
model, the strength of inhibition between any two prediction
neurons is proportional to the degree of overlap between the RFs.
Those neurons with orthogonal orientation preferences at a spe-
cific location overlap less than neurons with similar orientation
preferences and consequently produce less inhibition.

In the PC/BC model, inhibition from neurons tuned to near
orthogonal orientations is still significant and gives rise to cross-
orientation suppression. Evidence that suppression occurs for
masks with a high temporal frequency has cast doubt on the idea
that intracortical inhibition is responsible for cross-orientation
suppression (Carandini et al., 2002). This is because the very
weak responses evoked by high-frequency stimuli seem insuffi-
cient to produce strong suppression. However, the current model
does show strong suppression for masks presented at high tem-
poral frequencies. This is attributable to the many neurons
weakly activated by the high-frequency mask generating similar
suppression as the few neurons strongly activated by the mask
when it is presented at a low temporal frequency. In V1, strong
cross-orientation suppression requires that both the optimally
oriented grating and the mask grating be presented to the same
eye even for binocular cells (DeAngelis et al., 1992; Walker et al.,
1998). Such behavior is consistent with neurons competing to
receive inputs, rather than to produce outputs, as is proposed by
the PC/BC model.

Influences from neurons responding to stimuli placed outside
the RF of the recorded neuron enable PC/BC to simulate nonclas-
sical RF effects, such as surround suppression, and contextual
modulation by flankers and textures. Rather than explaining
these behaviors in terms of cortical feedback, which is not sup-
ported by the biological evidence (Hupe´ et al., 2001), the PC/BC
model explains these behaviors in terms of competition to repre-
sent inputs that are common to the RFs of the recorded neuron
and those neurons representing the contextual stimulation.

The extent of the long-range horizontal projections from a V1
cell are commensurate with the size of the SF of that cell measured
with a low-contrast grating (Angelucci et al., 2002; Angelucci and

Bullier, 2003), which is in turn two to four times larger than the
SF measured at high contrast (Sceniak et al., 1999; Angelucci et
al., 2002). For the model implemented for this article, the region
of the image from which a prediction neuron receives connec-
tions with nonzero synaptic weights has a diameter of 21 pixels,
which is approximately double the high-contrast SF diameter
(Fig. 5b). Thus, the model is compatible with the idea that the
long- and short-range lateral connections in V1 are responsible
for performing the type of competition proposed by the PC/BC
model.

The current model does not incorporate mechanisms to sim-
ulate many properties of V1 such as selectivity for color, direction
of motion, and disparity. However, the model should be easy to
extend by simply including prediction neurons with RFs selective
for these additional stimulus properties. The model is also defi-
cient in certain specific aspects of its behavior [e.g., it fails to show
adaptation to a stationary input, it fails to produce sufficiently
strong orientation contrast facilitation (Fig. 9e), and it does not
show sufficient expansion of the SF at low contrast (Fig. 5c)].
These deficiencies may be more challenging to overcome and are
likely to require modification to the mathematics of the model.
Another limitation of the current implementation is that it mod-
els V1 as a completely homogeneous sheet of processing units. No
account is taken of variations between individual neurons in their
RF properties (such as RF size, exact orientation preference, etc.).
Furthermore, no account has been taken of changes in V1 RF
properties across cortical layers, between locations in the cortical
map, with eccentricity from fovea, species, or age. Including such
factors in the model might enable it to account for a greater range
of empirical data. Despite this, the model produces a remarkably
good fit to a wide range of data (taken from different species,
cortical layers, etc.), suggesting that PC is a ubiquitous property
of V1. Another omission from the current implementation is
feedback connection from extrastriate cortical areas. The model
has operated without receiving any top–down or contextual pre-
dictions from other parts of the cortex. The influence of such
connections is defined by Equation 3 and hence could easily be
simulated. The inclusion of predictive inputs from other parts of
the cortex may enable to model to simulate nonclassical RF ef-
fects that occur for contextual inputs placed sufficiently far from
the RF of the recorded neuron that they cannot be explained
using the mechanisms implemented in the current model.

In conclusion, this article has shown that the mechanism of
competition proposed by the predictive coding model can ac-
count for a very wide range of V1 response properties. This sug-
gests that many of the diverse behaviors observed in V1 may
simply be explained as a consequence of V1 performing predic-
tive coding: minimizing the error between the observed sensory
input and the expectations stored in the synaptic weights of V1
cells.