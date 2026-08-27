## 

Behavioral/Systems/Cognitive

Predictive Coding as a Model of Response Properties in
Cortical Area V1

Michael W. Spratling
Division of Engineering, King's College London, London WC2R 2LS, United Kingdom, and Centre for Brain and Cognitive Development, Birkbeck,
University of London, London WC1E 7JL, United Kingdom

A simple model is shown to account for a large range of V1 classical, and nonclassical, receptive field properties including orientation
tuning, spatial and temporal frequency tuning, cross-orientation suppression, surround suppression, and facilitation and inhibition by
flankers and textured surrounds. The model is an implementation of the predictive coding theory of cortical function and thus provides
a single computational explanation for a diverse range of neurophysiological findings. Furthermore, since predictive coding can be
related to the biased competition theory and is a specific example of more general theories of hierarchical perceptual inference, the
current results relate V1 response properties to a wider, more unified, framework for understanding cortical function.

Introduction
Predictive coding (PC) provides an elegant theory of how bot-
tom-up evidence is combined with top-down priors to compute
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
wavelength, presentation time, etc.) under the experimenter's
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

Correspondence should be addressed to Michael W. Spratling, Division of Engineering, King's College London,
Strand, London WC2R 2LS, UK. E-mail: michael.spratling@kcl.ac.uk.

-09.2010
Copyright © 2010 the authors
0270-6474/10/303531-13$15.00/0

The Journal of Neuroscience, March 3, 2010 • 30(9):3531-3543 • 3531

---

## 

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
values of e indicate the degree of mismatch between the top-down re-
construction of the input and the actual input (assuming 2 is sufficiently

small to be negligible). When a value within e is greater than

, it indi-

cates that a particular element of the input is underrepresented in the

reconstruction; a value of less than

 indicates that a particular element

of the input is overrepresented in the reconstruction; and a value of


indicates that the top-down reconstruction perfectly predicts the bot-
tom-up stimulation. A second interpretation is that e represents the
inhibited inputs to a population of competing prediction neurons. Each
prediction neuron modulates its own inputs, which helps stabilize the
response of the prediction neurons, since a strongly (or weakly) active
prediction neuron will suppress (magnify) its inputs and hence reduce
(enhance) its own response. Prediction neurons that share inputs (i.e.,
that have overlapping RFs) will also modulate each other's inputs. This
generates a form of competition between the prediction neurons, such
that each neuron effectively tries to block other prediction neurons from
responding to the inputs that it represents.

Equation 2 describes the updating of the prediction neuron activa-
tions. The response of each prediction neuron is a function of its activa-
tion at the previous iteration and a weighted sum of afferent inputs from
the error-detecting neurons. Equation 3 describes the effects on the pre-

diction neuron activations of top-down inputs from prediction neurons
at the next stage in the neural hierarchy. These top-down inputs are a
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
modeled (Fig. 2). Furthermore, all top-down, modulatory, inputs to this
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

## 

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
  0-157.5° in steps of
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

## 

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
model described above is available at 
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

3534 • J. Neurosci., March 3, 2010 • 30(9):3531-3543
Spratling • Predictive Coding Model of V1

---

## 

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

Orientation (degrees)

−50

0.25 0.5 0.75 1 1.25 1.5
Diameter (degrees)
Diameter (degrees)

2 3

5 6 7

Spatial Freq. (cycles/degree)

0.3

Spatial Freq. (cycles/degree)

0.1
0.8
0.3

Drift Rate (cycles/second)

−50

Orientation (degrees)

Response

x10−3

−50

x 10

−3

5 10 15 20 25 30

8x 10
−3

Diameter (pixels)

5 10 15 20 25 30

Diameter (pixels)

x10−3

0.05
0.1
0.2
0.5

Spatial Freq. (cycles/pixel)

x10−3

0.1
0.2
0.3

Spatial Freq. (cycles/pixel)

x10−3

0.005
0.05
0.5

x 10

−3

Drift Rate (cycles/iteration)

0.005
0.05
0.5

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
J. Neurosci., March 3, 2010 • 30(9):3531-3543 • 3535

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