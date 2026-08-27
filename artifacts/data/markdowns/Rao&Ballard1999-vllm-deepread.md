## Page 1

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

nature neuroscience  •  volume 2  no 1  •  january 1999
79

Neurons that respond optimally to line segments of a partic-
ular length were first reported in early studies of the cat and
monkey visual cortex1,2. These neurons, which are especially
abundant in cortical layers 2 and 3, have the curious property
of endstopping (or end-inhibition): a vigorous response to an
optimally oriented line segment is reduced or eliminated when
the same stimulus extends beyond the neuron’s classical recep-
tive field (RF). Such ‘extra-classical’ RF effects occur in sever-
al visual cortical areas, including V1 (area 17; refs 2, 3), V2
(area 18; refs 1, 4), V4 (ref. 5) and MT6. In most of these cases,
neural responses are suppressed when stimulus properties at
the center, such as orientation, velocity or direction of motion,
match those in the surrounding extra-classical RF.

Why should a neuron that responds to a stimulus stop
responding when the same stimulus extends beyond the clas-
sical RF? Some studies have postulated a role for ‘hypercom-
plex’ endstopped neurons in the detection of visual
curvature1,7. Others have suggested a role for these cells in
detecting corners and line terminations8, occlusion9, percep-
tual grouping10 and illusory contours11. However, a straight-
forward extension of these arguments to extra-classical RF
effects in different cortical areas has been difficult. We have
previously shown that a model12 based on the principle of
Kalman filtering can account for certain visual cortical respons-
es in a monkey freely viewing natural images13. It was conjec-
tured that a similar model might also account for endstopping
and other extra-classical effects.

Here we show simulations suggesting that extra-classical RF
effects may result directly from predictive coding of natural
images. The approach postulates that neural networks learn
the statistical regularities of the natural world, signaling devi-
ations from such regularities to higher processing centers. This
reduces redundancy by removing the predictable, and hence

redundant, components of the input signal. Roots of this idea
can be found in early information-theoretic approaches to sen-
sory processing14–16. More recently, it has been used to explain
the spatiotemporal response properties of cells in the reti-
na17–19 and lateral geniculate nucleus (LGN)20,21. Because
neighboring pixel intensities in natural images tend to be cor-
related, values near the image center can often be predicted
from surrounding values. Thus, the raw image-intensity value
at each pixel can be replaced by the difference between a cen-
ter pixel value and its spatial prediction from a linear weight-
ed sum of the surrounding values. This decorrelates (or
whitens) the inputs17,19 and reduces output redundancy, pro-
viding a functional explanation for center–surround receptive
fields in the retina and LGN. The values of a given pixel also
tend to correlate over time. A retinal/LGN cell’s phasic response
can thus be interpreted as the difference between the actual
input and its temporal prediction based on a linear weighted
sum of past input values19–21. Similarly, the responses of reti-
nal photoreceptors sensitive to different wavelengths are often
correlated because their spectral sensitivities overlap. Thus,
the L-cone (long-wavelength or ‘red’ receptor) response may
predict the M-cone (medium-wavelength or ‘green’ receptor)
response, and the L- and M-cone responses together may pre-
dict the S-cone (short-wavelength or ‘blue’ receptor) response.
Thus, the color-opponent (red – green) and blue – (red +
green) channels in the retina might reflect predictive coding
in the chromatic domain similar to that of the spatial and tem-
poral domains18.

Using a hierarchical model of predictive coding, we show
that visual cortical neurons with extra-classical RF properties
can be interpreted as residual error detectors, signaling the dif-
ference between an input signal and its statistical prediction
based on an efficient internal model of natural images.

articles

Predictive coding in the visual cortex: 
a functional interpretation of some
extra-classical receptive-field effects

Rajesh P. N. Rao1 and Dana H. Ballard2

1 The Salk Institute, Sloan Center for Theoretical Neurobiology and Computational Neurobiology Laboratory, 10010 N. Torrey Pines Road, 
La Jolla, California 92037, USA

2 Department of Computer Science, University of Rochester, Rochester, New York 14627-0226, USA

Correspondence should be addressed to R.P.N.R. (rao@salk.edu)

We describe a model of visual processing in which feedback connections from a higher- to a lower-
order visual cortical area carry predictions of lower-level neural activities, whereas the feedforward
connections carry the residual errors between the predictions and the actual lower-level activities.
When exposed to natural images, a hierarchical network of model neurons implementing such a
model developed simple-cell-like receptive fields. A subset of neurons responsible for carrying the
residual errors showed endstopping and other extra-classical receptive-field effects. These results
suggest that rather than being exclusively feedforward phenomena, nonclassical surround effects in
the visual cortex may also result from cortico-cortical feedback as a consequence of the visual system
using an efficient hierarchical strategy for encoding natural images.


---

## Page 2

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

80
nature neuroscience  •  volume 2  no 1  •  january 1999

Results
HIERARCHICAL PREDICTIVE CODING MODEL
Each level in the hierarchical model network (except the lowest
level, which represents the image) attempts to predict the respons-
es at the next lower level via feedback connections (Fig. 1a). The
error between this prediction and the actual response is then sent
back to the higher level via feedforward connections. This error
signal is used to correct the estimate of the input signal at each
level (see Methods and Fig. 1b), similar to some previous mod-
els22–24 (see also refs 15, 25, 26). The prediction and error-cor-
rection cycles occur concurrently throughout the hierarchy, so
top-down information influences lower-level estimates, and bot-
tom-up information influences higher-level estimates of the input
signal. Lower levels operate on smaller spatial (and possibly tem-
poral) scales, whereas higher levels estimate signal properties at
larger scales because a higher-level module predicts and estimates
the responses of several lower-level modules (for example, three
in Fig. 1c). Thus, the effective RF size of units increases progres-
sively until the highest level, where the RF spans the entire input
image. The underlying assumption here is that the external envi-
ronment generates natural signals hierarchically via interacting
hidden physical causes (object attributes such as shape, texture
and luminance) at multiple spatial and temporal scales. The goal
of a visual system then becomes optimally estimating these hid-
den causes at each scale for each input image and, on a longer
time scale, learning the parameters governing the hierarchical
generative model. Similar models have been studied by other
researchers (for example, refs 27, 28).

HIERARCHICAL PREDICTIVE CODING OF NATURAL IMAGES
Given that the visual cortex is hierarchically organized and that
cortico-cortical connections are almost always reciprocal29, the
model described above suggests the following hypothesis: feed-
back connections from a higher area to a lower area (say V2 to
V1) carry predictions of expected neural activity in V1, whereas
feedforward connections convey to V2 the residual activity in V1

that was not predicted by V2 (refs 12, 22). To test this hypothesis,
a three-level hierarchical network of predictive estimators
(Fig. 1c) was trained on image patches extracted from five nat-
ural images (Fig. 2a), the motivation being that the response
properties of visual neurons might be largely determined by the
statistics of natural images17,20,21,30. Such an approach has pre-
viously explained some important visual cortical RF proper-
ties26,31,32.

We allowed the network to learn a hierarchical internal model
of its natural image inputs by maximizing the posterior proba-
bility of generating the observed data (Methods). The internal
model is encoded in a distributed manner within the synapses
of model neurons at each level. The synaptic weights (or ‘effica-
cies’) of a neuron encode a single basis vector that in conjunc-
tion with other basis vectors predicts lower-level inputs. For
example, a given input image at the zeroth level can be predicted
as an appropriate linear combination of the first-level basis vec-
tors (Methods, Equation 2). In this linear combination, the
weighting coefficient for the kth basis vector is given by the
response of the kth neuron in the first level. The response is deter-
mined by a first-order differential equation implementing the
prediction and error-correction cycle mentioned above. This
equation, like the synaptic learning rule, is also derived by max-
imizing the posterior probability of generating the observed data
(Methods). Thus, for any given input, the network converges to
a set of neuronal responses optimal for predicting that input.
These responses are then used to adapt the synaptic basis vec-
tors. The same description applies to each level of the hierarchy,
with each level predicting the inputs at its lower level using its
set of learned basis vectors and, on a slower time scale, adapting
these basis vectors to enable more accurate prediction of the
inputs in the future.

After exposure to several thousand natural image patches, the
basis vectors learned by the network at level 1 resembled orient-
ed edges or bars (Fig. 2b), whereas the basis vectors at level 2
seemed to be composed of various combinations of the features

articles

> Figure description (generated): ## Figure Description: Hierarchical Network for Predictive Coding

This figure, labeled "Fig. 1," is divided into three distinct panels: (a), (b), and (c), illustrating different aspects of a hierarchical network for predictive coding.

### Panel (a): Predictive Coding Flowchart
Panel (a) is a block diagram illustrating the flow of information in a predictive coding scheme. It shows two parallel pathways: "Feedforward" and "Error Signal."

*   **Input:** The process begins with an **"Input"** block on the far left.
*   **Feedforward Pathway:** The input flows into a box labeled **"Predictive Estimator."** This estimator is preceded by an arrow originating from the "Input," and it is associated with a label **"Feedforward Error Signal."**
*   **Error Signal Pathway:** Simultaneously, an arrow labeled **"Error Signal"** enters a second block, also labeled **"Predictive Estimator."**
*   **Outputs:** Both estimators produce an output labeled **"Prediction,"** which flows forward. The error signal pathway also produces a final output labeled **"Prediction."**
*   **Feedback Loop:** The structure implies a feedback mechanism, as the outputs of the estimators are involved in generating predictions and errors.

### Panel (b): Neural Circuit Schematic
Panel (b) presents a schematic diagram representing the dynamics of a predictive coding module, likely involving recurrent connections.

*   **Nodes:** There are four primary nodes represented by circles: $U$, $r$, $U^T$, and a final output node.
*   **Inputs/Outputs:** An input signal, denoted by the arrow labeled **$I$**, enters the system.
*   **Connections:**
    *   The input $I$ connects to a summation node (represented by a circle with a plus sign) which feeds into the $U$ node.
    *   The $U$ node connects to a summation node that also receives input from the $r^T d - r$ term.
    *   The $U$ node also connects to the $r$ node via a directed arrow.
    *   The $r$ node connects to the summation node that generates the final output, which is labeled **$\mathbf{r} - \mathbf{r}^{td}$**.
    *   The $U^T$ node is connected to the summation node that generates the term $\mathbf{r}^{td}$.
*   **Labels:** The diagram includes variables such as $I$, $U$, $r$, $U^T$, $\mathbf{r}^{td}$, and the difference term $\mathbf{r} - \mathbf{r}^{td}$.

### Panel (c): Hierarchical Network Diagram
Panel (c) illustrates a multi-level hierarchical network structure, organized into distinct levels.

*   **Levels:** The diagram is structured across three horizontal tiers: **Level 0**, **Level 1**, and **Level 2**.
*   **Nodes/Modules:** Each level contains interconnected modules represented by rectangular boxes labeled **"PE"** (Predictive Estimator).
    *   Level 0 contains one PE module.
    *   Level 1 contains two PE modules, labeled $PE$ and another unlabeled module.
    *   Level 2 contains two PE modules, labeled $PE$ and another unlabeled module.
*   **Connections:**
    *   There are directed arrows indicating information flow between levels, suggesting a top-down (prediction) and bottom-up (error/feedback) flow.
    *   The caption notes that the responses $\mathbf{r}$ of all three level-I modules were input to the level-2 module.
*   **Annotations:** The diagram includes dashed lines and arrows labeled **"$\ll$ PE"**, indicating the presence or influence of Predictive Estimator modules across different levels.

Fig. 1. Hierarchical network for predictive coding. (a) General
architecture of the hierarchical predictive coding model. At each
hierarchical level, feedback pathways carry predictions of neural
activity at the lower level, whereas feedforward pathways carry
residual errors between the predictions and actual neural activity.
These errors are used by the predictive estimator (PE) at each level
to correct its current estimate of the input signal and generate the
next prediction. (b) Components of a PE module, composed of
feedforward neurons encoding the synaptic weights UT, neurons
whose responses r maintain the current estimate of the input signal,
feedback neurons encoding U and conveying the prediction f(Ur) to
the lower level, and error-detecting neurons computing the differ-
ence (r – rtd) between the current estimate r and its top-down prediction rtd from a higher level. (c) A three-level hierarchical network used
in the simulations. An input image was analyzed by three level-1 PE modules, each predicting its own local image patch. The responses r of all
three level-1 modules were input to the level-2 module. This convergence of lower-level inputs to a higher-level module increases receptive-
field size of neurons as one ascends the hierarchy, with the receptive field at the highest level spanning the entire input image.

a
b

c


---

## Page 3

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

nature neuroscience  •  volume 2  no 1  •  january 1999
81

represented at level 1 (Fig. 2c). The basis vectors can be regarded
as approximate ‘receptive fields’ of the feedforward model neu-
rons because they are the primary determinants of the neurons’
feedforward responses26,32. These RFs at level 1 are reminiscent of
oriented Gabor or difference-of-Gaussian filters that have been
used to model simple-cell RFs in primary visual cortex (for exam-
ple, ref. 7). We used a Gaussian weighting profile to model the
input dendritic arbor of the model neurons so that each set of
the level 1 neurons only sees a localized portion of the entire input
image. However, the model also learns localized receptive fields
without a Gaussian spatial window if we impose the additional
constraint of sparseness on the model neuron responses (Meth-
ods; Fig. 2d)26,32. In this case, the wavelet-like basis vectors code
for local oriented structures rather than being centered in the
input window as in Fig. 2b. These basis vectors and their level-2
counterparts were used for the simulations in Fig. 6, whereas all
other simulations used the basis vectors in Fig. 2b and c.

ENDSTOPPED RESPONSES INTERPRETED AS ERROR SIGNALS
Given an input image, the initial predictions at any given level
are based on an arbitrary random combination of the basis vec-
tors, giving large error signals. To minimize this error, the net-
work converges to the responses that best predict the current
input by subtracting the prediction from the input (via inhibi-
tion) and propagating the residual error signal to the neurons at
the next level, which integrate this error and generate a better
prediction (Methods).

The model neurons carrying the error signal (the ‘error-
detecting’ neurons) send feedforward connections from the lower
level to the higher level. In the visual cortex, feedforward con-

nections to a higher area generally arise from the superficial lay-
ers (such as layer 2/3). A relatively large number of neurons in
layer 2/3 of striate cortex (V1) show endstopping and related
extra-classical effects2,3,33. To ascertain whether these observed
neuronal responses can be functionally interpreted as residual
error signals, we recorded the responses of level-1 error-detecting
neurons in the simulated network, when exposed to the image
of a short dark bar lying within their RF (Fig. 3a). The solid box
in the first panel (‘Input’) represents the RF size of the level-1
neurons (16 × 16 pixels), whereas the dotted box represents the
level-2 RFs (16 × 26 pixels). The last two panels show the two
components that determine the error signal. Many of the error-
detecting neurons showed significant non-zero responses,
demonstrating that feedback from level 2 could not completely
predict the responses at level 1.

On the other hand, when the bar stimulus extends beyond
the classical receptive field into the flanking regions (Fig. 3b),
the same error-detecting neurons showed little or no response
because the predictions from level 2 were much more accurate,
with prediction errors close to zero. Why are the level 2 predic-
tions much more accurate for the longer bar than for the short
bar? Recall that the network was trained on natural images. In
natural images, short bars seldom occur in isolation; rather, a
bar in a small region of an image is usually part of a longer bar
that extends into neighboring regions. Because the network was
optimized for natural image statistics, the most accurate predic-
tions are generated when the input’s properties match those of
natural images. The continuation of the bar into the surrounding
region provides the necessary context for the bar in the center to
be predicted, much as in the case of retinal center-surround pre-

articles

> Figure description (generated): ## Figure Description

This figure is divided into four main panels: **a**, **b**, **c**, and **d**.

**Panel a:**
This panel displays a photographic image, likely representing natural scenes or stimuli. The image shows a landscape featuring trees and what appears to be an animal (possibly a deer or similar creature) in the foreground, set against a backdrop of foliage and sky.

**Panel b:**
This panel presents a grid of small, grayscale images arranged in two rows. The top row is labeled **"Level 1"** and the bottom row is labeled **"Level 2"**. Each level contains a sequence of small, localized receptive field representations. The images in both rows appear to be Gabor-like filters or feature detectors, showing varying orientations and spatial frequencies.

**Panel c:**
This panel also displays a grid of small, grayscale images arranged in two rows. The top row is labeled **"Level 1"** and the bottom row is labeled **"Level 2"**. Similar to Panel b, these are receptive field representations. The arrangement suggests a progression or comparison between levels of processing.

**Panel d:**
This panel displays a large grid composed entirely of small, grayscale images, representing receptive fields. This entire section is labeled **"Level 1 (with sparse prior distribution)"**. The grid structure suggests a large set of feature detectors being presented.

**Contextual Caption Integration (Referencing the provided text):**
The caption states: "Fig. 2. Receptive fields of feedforward model neurons after training on natural images. (a) Five natural images used for training the three-level hierarchical network of Fig. 1c (Methods). The two upper boxes in the bottom right corner show relative sizes ($16 \times 16$ and $16 \times 26$ pixels) of level-1 and level-2 receptive fields respectively. (b) Learned synaptic weights (RF weighting profiles) of 20 of the 32 feedforward model neurons in the level-1 module analyzing the central image region. Flanking image regions were analyzed by two other level-1 modules (Fig. 1c), each with 32 feedforward model neurons (Methods). Values for these synapses, which form rows of the matrix $U^T$, can be positive (excitatory, bright regions) or negative (inhibitory, dark regions). These RF profiles resemble classical oriented-edge/bar detectors characteristic of simple cells$^2$. (c) RF profiles of 12 of the 128 level-2 feedforward model neurons. (d) Localized RF profiles resembling Gabor wavelets obtained by using a sigmoidal nonlinearity in the generative model, along with a sparse kurtotic prior distribution for the network activities (Methods). All 32 level-1 feedforward model neurons are shown; Gaussian windowing of inputs (as in b) was not necessary in this case."

**Detailed Interpretation based on Caption:**
*   Panel **a** shows the five natural images used for training.
*   The receptive field sizes mentioned in the caption ($16 \times 16$ and $16 \times 26$ pixels) correspond to the representations shown in Panels **b** and **c**, distinguishing between Level 1 and Level 2 receptive fields.
*   Panel **b** specifically shows the RF weighting profiles for 20 neurons in the Level-1 module analyzing a central image region. The visual representation (bright/dark regions) corresponds to positive (excitatory) or negative (inhibitory) synaptic weights, resembling oriented-edge/bar detectors.
*   Panel **c** shows the RF profiles for 12 neurons in the Level-2 module.
*   Panel **d** displays localized RF profiles resembling Gabor wavelets, derived using a sigmoidal nonlinearity and a sparse kurtotic prior distribution.

Fig. 2. Receptive fields of feedforward model neurons after
training on natural images. (a) Five natural images used for
training the three-level hierarchical network of Fig. 1c
(Methods). The two upper boxes in the bottom right corner
show relative sizes (16 x 16 and 16 x 26 pixels) of level-1 and
level-2 receptive fields respectively. (b) Learned synaptic
weights (RF weighting profiles) of 20 of the 32 feedforward
model neurons in the level-1 module analyzing the central image
region. Flanking image regions were analyzed by two other
level-1 modules (Fig. 1c), each with 32 feedforward model
neurons (Methods). Values for these synapses, which form rows
of the matrix UT, can be positive (excitatory, bright regions) or
negative (inhibitory, dark regions). These RF profiles resemble

classical oriented-edge/bar detectors charac-
teristic of simple cells2. (c) RF profiles of 12
of the 128 level-2 feedforward model neu-
rons. (d) Localized RF profiles resembling
Gabor wavelets obtained by using a sigmoidal
nonlinearity in the generative model, along
with a sparse kurtotic prior distribution for
the network activities (Methods). All 32
level-1 feedforward model neurons are
shown; Gaussian windowing of inputs (as in
b) was not necessary in this case.

a

b

Level 1

c

Level 2

d

Level 1 (with sparse prior distribution)


---

## Page 4

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

82
nature neuroscience  •  volume 2  no 1  •  january 1999

diction mechanisms. Without this contextual information in the
surrounding region, the higher level cannot accurately predict
the bar in the center. The short bar thus elicits a relatively large
response from the error-detecting neurons as compared to the
longer bar.

This argument suggests that the autocorrelation along a dom-
inant orientation in a local region in natural images extends over
reasonably large distances. We tested this hypothesis on a set of
natural images (Fig. 4a). Random locations were selected in these
images, and the local oriented energy was computed by summing
the squared outputs of quadrature pairs of filters. The orienta-
tion that maximized this energy measure was selected as the dom-
inant orientation. Correlations in the dominant orientation
direction and in the opposite direction in the natural image were
then calculated along three different orientation directions (ver-
tical, horizontal and diagonal) for several thousand random
image locations (Fig. 4b). The average correlations along the
dominant directions, especially the vertical and horizontal direc-
tions, remain relatively high for distances of up to plus or minus
50 pixels as compared to the correlations in the opposite direc-
tion. As a control, we repeated the experiment for three differ-
ent natural image sizes (968 × 968, 484 × 484 and 242 × 242
pixels). In all three cases, higher correlations were observed in
the dominant direction as compared to the opposite direction.
(Results for a random white-noise image are shown in Fig. 4c.)

To compare model neuron responses to neurophysiological
data, we computed the tuning curves of model error-detecting
neurons to bars of increasing length (Fig. 3c). The prediction

from level 2 falls short of the actual level-1 responses for shorter
bar lengths but gradually matches the actual response as the
length of the bar is increased. This determines the model length-
tuning curves, which closely resemble the tuning curves of layer
2/3 neurons in cat striate cortex (Fig. 5a). The model tuning curve
is a parameter-free prediction of the data in the sense that it is
determined by the statistics of the input natural images rather
than by the physiological data. Thus, the close similarity between
the model and physiological tuning curves is noteworthy. In the
model, the average length of the bar eliciting maximal response
was found to be approximately 4.5 pixels, the absolute RF sizes
being approximately 5 × 10 pixels. For comparison, ref. 3 reports
RF sizes of 1° × 1.75° and 0.5° × 1.5° for two visual cortical neu-
rons. These were maximally responsive to bars of length 1° and
0.5°, respectively.

PREDICTIVE FEEDBACK AND EXTRA-CLASSICAL RF EFFECTS
The removal of feedback from level 2 to level 1 in the model
caused previously endstopped neurons to continue to respond
to bars of increasing lengths (Fig. 5a), supporting the hypothesis
that predictive feedback is important in mediating endstopping
in the level-1 model neurons. To quantify this result, we com-
puted the distribution of endstopping (Fig. 5b) in all 32 model
layer 2/3 (error-detecting) neurons in the central level-1 module
(see Fig. 1c) with and without feedback from level 2. The degree
of endstopping was quantified as the percentage difference
between peak response and average plateau response for lengths
greater than 18 pixels: (peak – plateau)/peak × 100. Model neu-

articles

Fig. 3. Endstopping in the model net-
work. (a) Responses of the 32 error-
detecting model neurons in the central
level-1 module to a dark bar. (Positive val-
ues are upward bars; negative values are
downward bars.) Although not modeled
here, positive and negative values may be
coded by separate neurons in the cortex.
(b) Reduction in the level-1 residual
errors due to increase in top-down pre-
diction accuracy as the bar extends
beyond the classical RF (solid box), up to
the size of the level-2 RF (dashed box).
This reduced prediction error manifests
itself as endstopping in the error-detect-
ing model neurons. (c) Length-tuning
curves for two error-detecting model
neurons at level 1 with even-symmetric
(left) and odd-symmetric (right) RF pro-
files. Both model neurons show the
decrease in response characteristic of
endstopping as the bar extends beyond
the classical RF. The dashed line repre-
sents the corresponding response r at
level 1, and the dotted line represents the
predictive feedback rtd from level 2.

> Figure description (generated): ## Figure Description

This figure, labeled "Fig. 3," is divided into three main panels: (a), (b), and (c).

### Panel (a): Schematic Diagram of Neural Processing
Panel (a) presents a schematic diagram illustrating a multi-level neural processing structure.

*   **Structure:** The panel is divided into three main sections arranged horizontally: "Input," a central processing block, and an output/feedback section.
*   **Input Section:** This section shows two levels: "Level 1 Receptive Field" and "Level 2 Receptive Field." Each level is represented by a small, black rectangular box.
*   **Central Processing Block:** An arrow flows from the "Level 1 Receptive Field" box into a central processing area. This area is associated with two plots:
    *   **Left Plot (Error):** Titled "Error ($r-r^{td}$)," this is a line graph. The x-axis ranges from 1 to 32, labeled with discrete points (1, 16, 32). The y-axis is not explicitly labeled with units but shows a range around zero.
    *   **Right Plot (Response):** Titled "Response," this is a line graph. The x-axis ranges from 1 to 32, mirroring the error plot's scale. The y-axis shows a range from -0.1 to 0.2.
*   **Feedback/Output:** An arrow flows from the central processing area towards a final output representation, which is not fully detailed in this schematic.

### Panel (b): Schematic Diagram of Stimulus and Response
Panel (b) presents a schematic illustrating the relationship between stimulus input and neural response.

*   **Structure:** This panel is structured around a central comparison between stimulus input and neural response.
*   **Stimulus Input:** On the left, a block labeled "Bar Stimulus" is shown. Below this label, there is a horizontal bar graphic representing the stimulus, with a shaded region indicating the active area.
*   **Response Plot:** To the right of the stimulus, there is a line graph titled "Neuron number."
    *   The x-axis ranges from 1 to 32, labeled with discrete points (1, 16, 32).
    *   The y-axis is labeled "Response" and ranges from -0.1 to 0.2.
    *   A line graph shows a response profile across the neuron numbers, starting near zero and showing fluctuations.

### Panel (c): Model Plots for Neuron 1 and Neuron 2
Panel (c) contains two side-by-side line graphs, comparing model predictions for "Neuron 1" and "Neuron 2."

**Left Plot (Model neuron 1):**
*   **Title:** "Model neuron 1"
*   **X-axis:** Labeled "Bar length (pixels)," ranging from 0 to 25.
*   **Y-axis:** Labeled "Response," ranging from 0 to 0.06.
*   **Curves:** Two curves are plotted:
    1.  A solid line labeled "$r$" (Response). This curve rises sharply, peaks around 10-15 pixels, and then decays.
    2.  A dashed line labeled "$r^{td}$" (Predictive feedback). This curve is lower than $r$ and also shows a peak, though less pronounced.
*   **Annotation:** A small, shaded rectangular region labeled "RF" is positioned near the peak of the response curve.

**Right Plot (Model neuron 2):**
*   **Title:** "Model neuron 2"
*   **X-axis:** Labeled "Bar length (pixels)," ranging from 0 to 25.
*   **Y-axis:** Labeled "Response," ranging from 0 to 0.03.
*   **Curves:** Two curves are plotted:
    1.  A solid line labeled "$r$" (Response). This curve rises, peaks around 10-15 pixels, and decays.
    2.  A dashed line labeled "$r^{td}$" (Predictive feedback). This curve is lower than $r$ and also shows a peak.
*   **Annotation:** A small, shaded rectangular region labeled "RF" is positioned near the peak of the response curve.

a

b

0
5
10
15
20
25
0

0.005

0.01

0.015

0.02

0.025

0.03

0
5
10
15
20
25

c

Input
Error
(r-rtd)

Level 1 reponses

r

Predictive feedback

rtd

Response
Response

Neuron number

Model neuron 1
Model neuron 2

Bar length (pixels)
Bar length (pixels)

Response


---

## Page 5

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

nature neuroscience  •  volume 2  no 1  •  january 1999
83

rons were classified into 10 categories according to their degree of
endstopping, with 100% inhibition denoting a plateau response
of zero to long bars. If we define endstopping as greater than 50%
inhibition, 28 of the 32 model error-detecting neurons were end-
stopped with feedback intact. Disabling the feedback connec-
tions eliminated endstopping in all but 5 of these neurons, a
reduction of 82%. The five neurons that continued to show some
degree of endstopping after removal of feedback were those whose
receptive field orientations were not completely aligned with that
of the bar used for testing.

OTHER EXTRA-CLASSICAL RF EFFECTS IN THE MODEL
Several neurophysiological studies have reported nonclassical
surround effects due to orientation contrast between the stimuli
in the central classical RF region and the surrounding
region33,35,36. To investigate whether some of these effects could
result from the extended positive correlations along dominant
orientation directions in natural images (Fig. 4), we trained a

three-level hierarchical network, similar to the one used
for the endstopping simulations, on ten different natural
images. Rather than using a Gaussian window to localize
receptive fields as in the endstopping experiments, we
allowed the network to learn localized receptive fields by

imposing a sparse prior distribution32 on the network
responses (Methods). A total of nine level-1 modules
arranged in three rows and three columns analyzed a local
image patch (14 × 14 pixels). The outputs of these nine
modules were input to the single level-2 module.

An oriented grating in the classical RF produced a
robust response in a level-1 error-detecting model neu-
ron in the simulated network (Fig. 6a). This steady-state
response was suppressed 85.3% when a grating at the
same orientation was introduced in the surrounding
extra-classical region, consistent with a reduction in the
residual error signal due to better prediction from level 2 based
on the surrounding context. Introducing an orientation contrast
between the center and the surrounding region increased the
model neuron response by 19.1% over the classical RF response,
reflecting an increase in the residual error. Similar increases in
neuronal responses due to cross-oriented grating stimuli have
been reported in primary visual cortex36. An optimally oriented
grating restricted only to the surround elicited little response in
the model neuron. We determined the response of a model neu-
ron (Fig. 6b) to four different texture stimuli previously used in
a macaque V1 study35. The largest response was elicited by the
‘pop-out’ texture stimulus (compare with Fig. 4 of ref. 35 show-
ing a similar response in a V1 neuron). For these stimuli, the spa-
tial displacement of the central and surrounding bars in a
particular direction sometimes modified a response from sup-
pression to enhancement or vice versa, an effect attributable to
the localized nature of the level-1 receptive fields (Fig. 2d). We
also tested the response of an error-detecting model neuron

articles

> Figure description (generated): ## Figure Description

This figure is composed of three main panels: **(a)**, **(b)**, and **(c)**.

### Panel (a): Image Examples
Panel (a) displays a set of photographic images, likely illustrating the input data for the analysis.
*   **Top Row:** Contains two grayscale images side-by-side, appearing to be high-magnification views of biological tissue or structures.
*   **Bottom Row:** Contains two smaller, cropped grayscale images below the top row, also showing detailed structures.
*   **Scale Bar:** A vertical scale bar labeled "100 pixels" is present on the left side, adjacent to the images.

### Panel (b): Correlation Plots
Panel (b) consists of three separate line graphs, arranged horizontally, each corresponding to a different orientation: "Vertical ($90^\circ$)", "Horizontal ($0^\circ$)", and "Diagonal ($135^\circ$)".

**General Structure of Plots in Panel (b):**
Each plot shares a similar structure:
*   **Y-axis:** Labeled "Correlation," ranging from 0.0 to 1.0, with tick marks at intervals of 0.2.
*   **X-axis:** Labeled "Distance (in pixels)," ranging from 0 to 50, with tick marks at intervals of 10.
*   **Legend/Scale:** Each plot includes a small inset box indicating the scale used for the analysis.

**Specific Plot Details:**
1.  **Vertical ($90^\circ$) Plot (Left):**
    *   The inset scale reads: "Scale 0.84 $\times$ 968".
    *   The plot shows a curve peaking near the center of the x-axis (around 0 pixels) and decaying symmetrically as distance increases.
2.  **Horizontal ($0^\circ$) Plot (Center):**
    *   The inset scale reads: "Scale 0.84 $\times$ 242".
    *   The plot shows a curve peaking near the center of the x-axis and decaying symmetrically.
3.  **Diagonal ($135^\circ$) Plot (Right):**
    *   The inset scale reads: "Scale 0.84 $\times$ 242".
    *   The plot shows a curve peaking near the center of the x-axis and decaying symmetrically.

### Panel (c): Correlation Plot
Panel (c) contains a single line graph, structurally similar to those in Panel (b).

**Specific Plot Details:**
*   **Y-axis:** Labeled "Correlation," ranging from 0.0 to 1.0, with tick marks at intervals of 0.2.
*   **X-axis:** Labeled "Distance (in pixels)," ranging from 0 to 50, with tick marks at intervals of 10.
*   **Inset Scale:** The inset scale reads: "Scale 0.84 $\times$ 484".
*   **Curve Trend:** The plot displays a single curve that peaks sharply near 0 pixels and exhibits a clear, smooth decay as the distance increases.

Fig. 4. Autocorrelation along dominant orientation direc-
tions in natural images. (a) Three natural images from the
Sweeney/Rubin Ansel Adams Fiat Lux collection (repro-
duced with permission from the California Museum of
Photography, University of California, Riverside). Each image
was filtered with quadrature pairs of oriented filters for
computing oriented energy. Three of these oriented filters
are shown at the bottom alongside the arrows. The bottom
row shows examples of oriented structures extending over
relatively large distances in three natural image patches. 
(b) Average correlations in the natural images along the
dominant orientation direction and the orthogonal direc-
tion, shown here for three different orientation directions
(horizontal, vertical and diagonal) and for three different
natural image sizes. Correlations were computed by choos-
ing a 16 x 16 image patch at a randomly selected location in
a natural image and translating the correlation window up to
plus and minus 50 pixels along the dominant orientation
direction and the orthogonal direction. The dominant orien-
tation was chosen to be the one that maximized the local
oriented energy as given by the sum of squared outputs of
the quadrature pairs of filters. Correlations along the domi-
nant directions remained positive for distances of up to plus
or minus 50 pixels, supporting the hypothesis that oriented
structures in natural images on the average tend to extend
over reasonably large distances. (c) Results of applying the
same procedure to a randomly generated white-noise image.

a

b
Vertical (90°)
Horizontal (0°)
Diagonal (135°)

Distance (in pixels)

Correlation

c

Correlation

Distance (in pixels)


---

## Page 6

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

84
nature neuroscience  •  volume 2  no 1  •  january 1999

(Fig. 6c) to random texture stimuli used in a study of contextu-
al modulation in alert macaque V1 (ref. 33). The tonic phase of
the model neuron response reveals a large positive difference
(93.5%) developing over time for the orientation-contrast tex-
ture as compared to the homogeneous texture. This modulation
in response resembles the type of contextual modulation observed
in V1 neurons (compare with Fig. 2 of ref. 33).

Discussion
Our simulation results suggest that certain extra-classical RF
effects could be an emergent property of the cortex using an effi-
cient hierarchical and predictive strategy for encoding natural
images. In this model, cortical neurons showing extra-classical
effects are interpreted as error-detecting neurons that signal the
difference between an input and its prediction from a higher visu-
al area. In particular, the layer 2/3 neurons that send axons to the
higher visual area are posited to be likely candidates for this func-
tion. In the model, predictions are made based on progressively
larger spatial contexts as one ascends the visual hierarchy. As a
result, when the stimulus properties in a neuron’s receptive field
match the stimulus properties in the surrounding region, little
response is evoked from the error-detecting neurons because the
‘surround’ can predict the ‘center.’ On the other hand, when the
stimulus occurs in isolation, such a prediction fails, eliciting a
relatively large response. This behavior can be viewed as a refine-
ment of the types of predictive coding observed at the retina17–19
and the LGN20,21 involving spatiotemporal prediction based on
weighted averages of spatially/temporally local pixels and sub-
traction of this prediction from current pixel values.

The model predicts that layer 2/3 neurons will respond most
vigorously to stimuli whose statistics differ in certain drastic ways
from natural image statistics (as in, for example, Fig. 6). This
raises the interesting possibility of discovering novel extra-classical
RF effects by explicitly constructing stimuli that deviate from
natural image statistics. In addition, termination of cortical feed-

back should disinhibit the responses of layer 2/3 neurons that are
suppressed by extra-classical stimuli under normal conditions.
In anesthetized monkeys, inactivation of higher-order visual cor-
tical areas disinhibits responses to surround stimuli in lower-area
neurons37 (see also Hupé, J. M. et al., Soc. Neurosci. Abstr. 23,
1031, 1997 and James, A. C. et al., Soc. Neurosci. Abstr. 21, 904,
1995), consistent with the predictive coding model. In the cat,
removal of feedback from visual cortical areas 17 and 18 to the
LGN strongly reduces the degree of end-inhibition in LGN cells38.
Also, extra-classical RF effects in layer 2/3 neurons in alert mon-
key V1 often manifest themselves only 80–100 milliseconds after
stimulus onset, suggesting that feedback from higher areas may be
involved in mediating these effects33.

The simulation results show that extra-classical RF effects can
occur in the predictive coding model under either Gaussian
(Figs 3 and 5) or sparse kurtotic (Fig. 6) prior distributions for
the network activities. The issue of prior distributions has been
much discussed12,31,32, with kurtotic distributions being favored
because they can produce localized receptive fields and sparse
codes. Our results suggest that the effects can be obtained under
both sparse and non-sparse prior distributions, as long as one
interprets the effects as being caused due to residual errors in pre-
diction based on an internal model of natural image statistics.

The predictive coding model does not rule out the possibility
that certain extra-classical contextual effects may result from
recurrent lateral inhibition mediated by long-range horizontal
connections within the same visual area39. In fact, the equation
for the dynamics of the network can be rewritten such that some
of the effects of feedback are replaced by recurrent lateral inter-
actions (Methods, Equation 8; refs 32, 40). In addition, the repet-
itive subtraction of neighboring neuronal activities (Equation 8)
may produce a net effect similar to divisive normalization41, an
operation that reproduces certain extra-classical effects in sim-
ulations (Simoncelli, E. P., results presented at the 1998 Center
for Visual Science Symposium, Rochester, New York, 1998).

articles

Fig. 5. Predictive feedback and endstopping. (a) Effect of
inactivating feedback from level 2 in the model. Plotted on
the left are the length tuning curves for a ‘layer 2/3’ error-
detecting model neuron at level 1 with and without feed-
back from level 2 (solid and dotted line respectively).
Tuning curves for a layer 2/3 complex cell in cat striate cor-
tex (V1) (redrawn from Fig. 3 in ref. 3) are shown on the
right for comparison. Disabling top-down feedback elimi-
nated endstopping in the model neuron in a manner quali-
tatively similar to that observed in the cortical neuron after
inactivation of layer 6 (dotted line). Elimination of feedback
from V2 dramatically affects neural responses in layer 6 of
V1 in the squirrel monkey34. (b) Histograms summarizing
the distribution of length tuning in all 32 model layer 2/3
neurons in the central level 1 module with feedback (left)
and without feedback (right) from level 2. Endstopping was
quantified as the percentage difference between peak
response and average plateau response for lengths greater
than 18 pixels. Model neurons were classified into ten cate-
gories according to their degree of endstopping. Disabling
feedback connections eliminated endstopping (defined as
greater than 50% inhibition) in 82% of the model layer 2/3
neurons.

> Figure description (generated): ## Figure Description

This figure is divided into two main parts, **Panel a** and **Panel b**, presenting comparative data related to neural responses.

### Panel a: Response Curves Comparison (Plots)

Panel **a** consists of two side-by-side line graphs comparing the response profiles of "Model neuron" and "Cortical neuron."

**Left Plot: Model Neuron Response**
*   **Title/Context:** Labeled "Model neuron."
*   **Y-axis Label:** "% maximum response," ranging from 0% to 100%.
*   **X-axis Label:** "Bar length (pixels)," ranging from 0 to 20.
*   **Data Curves:** Two distinct curves are plotted:
    1.  A solid line labeled "Without feedback," showing a bell-shaped curve peaking around 80-90% response at approximately 6 pixels.
    2.  A dashed line labeled "With feedback," showing a curve that is generally lower than the "Without feedback" curve, peaking slightly earlier and at a lower maximum response.

**Right Plot: Cortical Neuron Response**
*   **Title/Context:** Labeled "Cortical neuron." This plot is further subdivided by layer information.
*   **Y-axis Label:** "% maximum response," ranging from 0% to 100%.
*   **X-axis Label:** "Bar length (deg)," ranging from 0 to 8.
*   **Data Curves/Annotations:** Two distinct conditions are shown:
    1.  A curve associated with "Layer 6 inactivated." This curve shows a response profile across the bar lengths.
    2.  A curve associated with "Layer 6 intact." This curve also shows a response profile across the bar lengths.

### Panel b: Endstopping Distribution (Histogram)

Panel **b** consists of two side-by-side histograms illustrating the distribution of endstopping percentages.

**Left Histogram: Model with feedback**
*   **Title/Context:** Labeled "Model with feedback."
*   **Y-axis Label:** "Number of neurons," ranging from 0 to 12.
*   **X-axis Label:** "Degree of endstopping (%)," ranging from 0 to 100, with labeled bins at 0, 10, 20, ..., 100.
*   **Data Distribution:** The histogram shows a distribution where the highest frequency (peak) occurs in the bin corresponding to approximately 60-70% endstopping.

**Right Histogram: Model without feedback**
*   **Title/Context:** Labeled "Model without feedback."
*   **Y-axis Label:** "Number of neurons," ranging from 0 to 12.
*   **X-axis Label:** "Degree of endstopping (%)," ranging from 0 to 100, with labeled bins at 0, 10, 20, ..., 100.
*   **Data Distribution:** The histogram shows a distribution where the frequencies are generally lower and more spread out compared to the left plot, with noticeable counts across multiple bins.

### Contextual Caption Integration (Figure 5)

The caption provides context for the elements:
*   **Panel a:** Refers to "Predictive feedback and endstopping." It specifies that the plots show the effect of inactivating feedback from level 2 in the model.
    *   The left plot (Model neuron) is related to the "layer 2/3 error-detecting model neuron."
    *   The right plot (Cortical neuron) is related to the "layer 2/3 complex cell in cat striate cortex (V1)."
    *   The labels "Layer 6 inactivated" and "Layer 6 intact" in the right plot correspond to specific experimental conditions.
*   **Panel b:** Refers to "Histograms summarizing the distribution of length tuning in all 32 model layer 2/3 neurons."
    *   The comparison between the two histograms relates to the presence or absence of feedback.

0
1
2
3
4
5
6
7
8
0

10

20

30

40

50

60

70

80

90

100

0
2
4
6
8
10
12
14
16
18
20
0

10

20

30

40

50

60

70

80

90

100

Layer 6 intact

Without feedback

Layer 6 inactivated

Bar Length (pixels)
Bar Length (deg)

Cortical Neuron
Model Neuron

% Maximum Response

With feedback

0
10 20 30 40 50 60 70 80 90 100
0

2

4

6

8

10

12

0
10 20 30 40 50 60 70 80 90 100
0

2

4

6

8

10

12
Model With Feedback

Max
Min
Max
Degree of Endstopping (%)

Number of Neurons

Min

Degree of Endstopping (%)

Model Without Feedback

a

b

Model neuron
Cortical neuron

% maximum response

Bar length (pixels)
Bar length (deg)

Model with feedback
Model without feedback

Number of neurons

Degree of endstopping (%)


---

## Page 7

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

nature neuroscience  •  volume 2  no 1  •  january 1999
85

Some extra-classical RF effects involve facilitatory rather than
inhibitory responses39. In other words, the presence of a stimulus
in the surround may facilitate rather than inhibit the neural
response elicited by a stimulus in the center alone. Some examples
of such facilitatory effects in the model are shown in Fig. 6, but
other facilitatory effects may reflect a bipolar strategy for encod-
ing prediction errors. Because these errors can be either positive
or negative, the cortex may use two distinct populations of neu-
rons to signal errors, one for positive and another for negative
errors, in analogy with the existence of on-center, off-surround
and off-center, on-surround cells in the early visual pathway.

Although we have focused on interpreting responses in V1,
the general idea of predictive coding may help explain certain
responses in other brain regions as well. For example, some neu-
rons in MT are suppressed when the direction of stimulus motion
in the surrounding region matches that in the center of the clas-
sical RF6. This suggests a hierarchical predictive coding strategy
for motion analogous to the one suggested here for image fea-
tures. Although the precise details of such a strategy are far from
clear, a testable prediction of such a model would be a significant
reduction in extra-classical effects in layer 2/3 neurons in MT
upon inactivation of feedback from a higher area such as MST.
Certain neurons in the anterior inferotemporal (IT) cortex of
alert behaving monkeys fire vigorously whenever a presented test
stimulus does not match the item held in memory, though show-
ing little or no response in the case of a match42. This suggests
an interpretation of these responses in terms of residual error
signals between a test stimulus and a predicted item from mem-
ory. Whether such a model can also account for the very specif-
ic face and view-sensitive cells in IT43,44 remains unclear
(however, see ref. 45). A third example suggestive of predictive
coding is the generation and subtraction of sensory expectations

from actual inputs in cerebellum-like structures in several dis-
tinct classes of fishes46. In this case, the sensory prediction is gen-
erated using not only recent sensory inputs but also corollary
discharge or proprioceptive signals associated with motor com-
mands. Finally, the responses of dopaminergic neurons project-
ing to the cortex and striatum from the midbrain can often be
characterized as encoding reward prediction errors: large respons-
es are elicited whenever actual rewards do not match the pre-
dicted rewards in a behavioral task47. These examples suggest
that the general idea of predictive coding may be applicable across
different brain regions and modalities, providing a useful frame-
work for understanding the general structure and function of
the neocortex22,48.

Methods
HIERARCHICAL GENERATIVE MODEL. Consider an image I represented as a
vector of n pixels. We assume that the cortex tries to represent the image
in terms of hypothetical causes, as represented by a vector r. We charac-
terize the relationship between the causes r and the image I using the
function f and a matrix U:

where n is a stochastic noise process characterizing the differences
between I and f(Ur). Note that

where Uj are columns of U, representing basis vectors for generating
images. Thus, each image I is assumed to be generated by a linear super-
position of the basis vectors followed by a possible nonlinearity f. In
terms of a neural network, the coefficients rj correspond to the activities
or firing rates of neurons, whereas the basis vectors Uj correspond to the
synaptic weights of neurons. The function f(x) is the neuronal activa-

articles

> Figure description (generated): ## Figure Description

This figure, labeled with panels **a**, **b**, and **c**, presents three distinct visual representations related to neural responses, likely derived from experimental data or models.

### Panel a: Orientation Contrast Grating Response Plot
Panel **a** displays a bar graph illustrating the response to orientation contrast gratings.

*   **Y-axis:** Labeled "Response," ranging from 0 to 1.
*   **X-axis:** Represents different conditions, indicated by distinct bars.
*   **Data Representation:** There are five sets of bars shown:
    1.  The first bar shows a response near 0.2.
    2.  The second bar shows the highest response, approximately 0.75.
    3.  The third bar is very low, near 0.1.
    4.  The fourth bar shows a response around 0.25.
    5.  The fifth bar is very low, near 0.1.
*   **Contextual Annotation:** Above the graph, there is a schematic representation of an orientation contrast grating pattern. This pattern consists of alternating black and white bars, with a clear horizontal orientation indicated by the structure. The caption identifies this as relating to "Orientation contrast grating."

### Panel b: Pop-out Texture Response Plot
Panel **b** displays a bar graph illustrating the response to "Pop-out texture."

*   **Y-axis:** Labeled "Response," ranging from 0 to 1.4.
*   **X-axis:** Represents different conditions, indicated by distinct bars.
*   **Data Representation:** There are four sets of bars shown:
    1.  The first bar shows a high response, approximately 1.0.
    2.  The second bar is very low, near 0.05.
    3.  The third bar shows a response around 1.2.
    4.  The fourth bar is very low, near 0.05.
*   **Contextual Annotation:** Above the graph, there is a schematic representation of textures. Two rows of small squares are shown: one row with solid black squares (representing a texture) and another row with white/empty spaces, suggesting a contrast or pop-out effect. The caption identifies this as relating to "Pop-out texture."

### Panel c: Time Course Plots
Panel **c** contains two separate plots stacked vertically, both showing a response over time.

*   **Top Plot (Orientation Contrast):**
    *   **Y-axis:** Labeled "Response," ranging from 0 to 0.08.
    *   **X-axis:** Labeled "Time (number of iterations)," ranging from 0 to 70.
    *   **Data Representation:** This plot shows a single line tracing the response over time. The response starts low and gradually increases, showing a positive trend across the 70 iterations.
    *   **Legend:** A legend in the top right corner indicates "Orientation Contrast."

*   **Bottom Plot (Homogeneous Texture):**
    *   **Y-axis:** Labeled "Response," ranging from 0 to 0.08.
    *   **X-axis:** Labeled "Time (number of iterations)," ranging from 0 to 70.
    *   **Data Representation:** This plot shows a single line tracing the response over time, which remains consistently low across all 70 iterations.
    *   **Legend:** A legend in the top right corner indicates "Homogeneous."

The caption further clarifies that Panel **c** compares the response to "Orientation contrast" versus "Homogeneous" stimulus over time.

Fig. 6. Nonclassical surround effects in the model. (a) Responses
of an error-detecting model neuron to oriented gratings in the
classical (center region) and extra-classical RF (surrounding
region)36. An oriented grating in the classical RF produced a
robust response (first bar in the bar graph), which was sup-
pressed when a grating at the same orientation was introduced in
the surrounding extra-classical region (second bar). Introducing
an orientation contrast between center and surround increased
the response beyond the center-only response (third bar). An
optimally oriented grating in the surround only elicited a small
response (fourth bar). (b) Responses of an error-detecting model
neuron to texture stimuli used in ref. 35. The largest response
was elicited by the ‘pop-out’ texture stimulus (compare with Fig.
4 of ref. 35). (c) Extra-classical contextual modulation in the tem-
poral response of an error-detecting model neuron, when
exposed to the random texture stimuli used in ref. 33. The tonic phase of the response reveals a large positive difference developing over
time for the orientation-contrast texture as compared to the homogeneous stimulus (compare with Fig. 2 of ref. 33).

0

0.2

0.4

0.6

0.8

1

Response

Grating
Orientation Contrast

0

0.2

0.4

0.6

0.8

1

1.2

1.4

Response

Pop-Out Texture

0
10
20
30
40
50
60
70
0

0.02

0.04

0.06

0.08

Homogeneous

Orientation Contrast

Time (number of iterations)

Response

Orientation Contrast

Homogeneous
Random Texture

a
b

c

Response
Response

Response

Time (number of iterations)

Orientation contrast

grating
Pop-out texture

Orientation contrast

Homogeneous
random texture

I = f (Ur) + n
(1)

f (Ur) = f (∑Ujrj)
(2)
k

> Figure description (generated): The provided image snippet contains a mathematical equation and surrounding text, not a complex figure with multiple panels, plots, or schematics. Therefore, the description will focus on the mathematical notation presented.

**1. Overall Layout & Structure:**
The content is a textual excerpt containing an equation, presented in a standard academic typesetting format. It does not constitute a multi-panel figure or a complex diagram.

**2. Visual Components & Symbols:**
The primary visual component is the mathematical equation labeled (2).

*   **Equation Structure:** The equation defines a function $f(Ur)$.
*   **Mathematical Notation:**
    *   $f(\cdot)$: Represents a function $f$.
    *   $Ur$: Represents the input to the function, which is a vector or sum.
    *   $\sum_{j=1}^{k} U_j r_j$: This is the summation term inside the function.
        *   $\sum_{j=1}^{k}$: Indicates a summation starting from index $j=1$ up to $k$.
        *   $U_j$: Represents the $j$-th element of a set or vector $U$.
        *   $r_j$: Represents the $j$-th element of a set or vector $r$.
        *   The multiplication between $U_j$ and $r_j$ implies a dot product or weighted sum.

**3. Labels, Keys & Legends:**
*   **Equation Number:** The equation is explicitly labeled as **(2)** on the right margin.
*   **Variables:** $f$, $U$, $r$, $k$, and $j$ are used as variables.

**4. Data Trends & Details:**
As this is a mathematical definition, there are no data trends or axes to describe.

**5. Contextual Caption Integration:**
The surrounding text provides context for the variables:
*   The preceding text mentions a relationship "between I and $f(Ur)$."
*   The subsequent text states: "where $U_j$ are columns of $U$ representing basis vectors for generating..." (The sentence is cut off). This context implies that $U$ is a matrix whose columns are basis vectors, and the equation describes how the function $f$ operates on a linear combination of these basis vectors weighted by components of $r$.

j=1


---

## Page 8

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

86
nature neuroscience  •  volume 2  no 1  •  january 1999

tion function, typically a sigmoidal function such as tanh(x). The coef-
ficients rj can be regarded as the network’s internal representation of the
spatial characteristics of the image I, as interpreted using the internal
model defined by the basis vectors Uj.

To make this model hierarchical, we assume that the causes r them-
selves can be represented as a set of higher-level causes rh representing
more abstract stimulus properties than the lower level. This yields the
equation:

where rtd = f(Uh rh) is the ‘top-down’ prediction of r, and ntd is a sto-
chastic noise process.

Because the dendritic arbors of neurons can only span a finite spatial
extent, we limit the size of I at the lowest level so that only a local por-
tion of the actual image is being generated by a given set of causes r. The
higher-level vector rh, however, generates several sets of these causes r
associated with local neighboring image regions. Thus, a given image is
generated by groups of local causes r, several groups being generated by
a single higher-level vector rh, several of which are in turn generated by an
even higher level of causes until the entire image is accounted for. This
results in increasing receptive field size as one ascends the hierarchy, sim-
ilar to that observed in the occipitotemporal visual pathway29. To allow
prediction in time for time-varying images, the model can be extended
using a set of recurrent synaptic weights V that recursively transform the
vector r(t) at time t to the predicted vector r(t+1) at time t+1: r(t+1) =
f(Vr(t)) + m where m is a noise process. Because static images sufficed
for our simulation results, we did not use the temporal prediction com-
ponent, but the interested reader is referred to refs 12 and 49 for more
details.

OPTIMIZATION FUNCTION. The goal is to estimate, for each hierarchical
level, the coefficients r for a given image and, on a longer time scale, learn
appropriate basis vectors Uj for each hierarchical level. Assuming that
the noise terms n and ntd are Gaussian with zero mean and variances σ2
and σtd2 respectively, one can write the following optimization function:

where the superscript T denotes the transpose of a vector or matrix. Note
that E1 is the negative logarithm of the probability of the data given the
parameters. It is the sum of squared prediction errors for level 1 and level
2, each term being weighted by the respective inverse variances. Taking
into account the prior distributions of r and U, one obtains the opti-
mization function:

where g(r) and h(U) are the negative logarithms of the prior probabilities of
r and U respectively. For the endstopping simulations, we used Gaussian
prior distributions for both these model parameters because this was suffi-
cient to illustrate the properties of the model. This results in g(r) = α Σi ri2 and
h(U) = λ Σi,j Ui,j2 where α and λ are positive constants related to the vari-
ance of the Gaussian prior distributions. Localized receptive fields can be
obtained by using sparse kurtotic prior distributions for r (refs 26,31), e.g.,

This choice was used for the extra-classical surround experiments in Fig.
6. Note that by Bayes Theorem, minimizing E is equivalent to maximiz-
ing the posterior probability of the model parameters given the input
data. In the context of information theory, E can be interpreted as rep-
resenting the cost of coding the errors and parameters in bits (in base e).
Thus, minimizing E is equivalent to using the minimum description
length principle50, which requires solutions to be not only accurate but
also cheap in terms of coding length.

NETWORK DYNAMICS AND SYNAPTIC LEARNING. An optimal estimate of r can
be obtained by performing gradient descent on E with respect to r:

where k1 is a positive constant governing the rate of descent towards a
minimum for E, x = Ur, and g´ is the derivative of g with respect to r. In
the linear case (f(x) = x),

is the identity matrix and in the case where f(x) = tanh(x),

= (1 – tanh(x)2).

Similarly, for a Gaussian prior distribution, g´(r) = 2α r and for the kur-
totic prior distribution in Equation 6, g´(ri) = 2α ri /(1+ ri2) (ref. 32).

To modify r toward the optimal estimate (Equation 7), one needs the
‘bottom-up’ residual error (I – f(Ur)) and the ‘top-down’ error (rtd – r).
The bottom-up error is multiplied by the transpose of the gradient and
the basis matrix UT, and a decay term g´(r) due to the prior probability of
r is subtracted. Note that all the information required is available local-
ly at each level. The weight accorded to the top-down and bottom-up
errors is inversely proportional to their respective noise variances: the
larger the noise variance, the smaller the weight (see ref. 12). In a neur-
al implementation (Fig. 1b), each row of the matrix UT corresponds to
the synaptic weights of a single neuron.

In the linear case (f(x) = x), the above dynamics can be rewritten to
allow lateral interactions32,40:

where W = UTU. In this implementation, the neural responses r under-
go recurrent lateral inhibition due to the term

Wr,

where the ith row of W represents the lateral weights for the ith neuron
that maintains the estimate ri. Such lateral connections between neurons
maintaining r may thus also be involved in mediating some of the extra-
classical RF effects observed in the visual cortex (see Discussion).

A synaptic learning rule for adapting the basis matrix U can be
obtained by performing gradient descent on E with respect to U:

where k2 is a positive parameter determining the learning rate of the net-
work and x = Ur. Note that this learning rule is a form of Hebbian adap-
tation, the presynaptic activity being r and the postsynaptic activity being
the residual error (I – f (Ur)) (see Fig. 1b).

Although the top-down feedback rtd does not appear explicitly in the
learning rule for U, it nevertheless influences the estimation of r (see
Equation 7) and hence, also U.

SIMULATIONS. For the endstopping simulations, five natural images of dif-
ferent sizes (Fig. 2a) were first filtered using a center-surround difference-
of-Gaussians operator to approximate processing at the levels of the retina
and the LGN (see also ref. 26). During the training phase, three 16 × 16
overlapping Gaussian-windowed image patches (offset by 5 pixels hori-
zontally) were input to the three level-1 modules (Fig. 1c). The respons-
es from the level-1 modules at each time instant were input as a single
vector to the level-2 module. The effective level-2 RF thus encompassed a
16 × 26 image region spanned by the three overlapping circles (Fig. 2a).
For simplicity, a linear generative model (f(x) = x) was used in the end-
stopping simulations. Each level-1 module consisted of 32 feedforward
neurons representing UT (size 32 × 256), 32 neurons that maintained r
(according to equation 7), 32 error-detecting neurons that propagated to
level 2 the top-down residual (r – rtd), and a set of 256 feedback neurons
whose synaptic efficacies encoded the rows of U and that conveyed the
prediction Ur to level 0. The level-2 module consisted of 128 feedforward
neurons receiving inputs from the three level-1 modules, 128 neurons for
maintaining rh, and 96 feedback neurons whose synapses encoded rows
of Uh and which conveyed the prediction Uhrh to level 1. Parameter values:
k1 = 0.5, σ2 = 1, σtd2 = 10, α = 1 for level 1 and 0.05 for level 2, and λ =
0.02. The learning rate k2 was initially set to 1 and decreased gradually by
dividing with 1.015 after every 40 training inputs.

articles

r = rtd + ntd
(3)

E1 =       (I – f (Ur))T (I – f (Ur)) +       (r – rtd)T (r – rtd)
(4)
1—
σ2

1—
σtd2

E = E1+ g(r) + h(U)
(5)

g(r) = α ∑log(1 + ri2)
(6)
i

= –            =      UT
(I – f (Ur)) +      (rtd – r) –      g´(r)
(7)
dr
—
dt

k1
—2

∂E
—
∂r

k1
—
σ2

∂f T

—
∂x

k1
—
σtd2

k1
—2

=      UTI +      (rtd – r) –      g´(r) –      Wr
(8)
dr
—
dt

k1
—
σ2

k1
—
σtd2

k1
—2

k1
—
σ2

= –            =            (I – f (Ur))rT – k2λU
(9)
dU
—
dt

k2
—
σ2
k2
—2

∂f T

—
∂x
∂E
—
∂U

∂f T

—
∂x

∂f—
∂x

> Figure description (generated): The provided image contains a single mathematical equation, presented as an inline formula rather than a complex graphical figure with multiple panels or plots.

**1. Overall Layout & Structure:**
The content is a single, complex mathematical equation displayed centrally on the page. It is presented in standard academic typesetting format.

**2. Visual Components & Symbols:**
The equation consists of derivatives, variables, constants, and mathematical operators:

*   **Left Side:** $\frac{dr}{dt}$ (A derivative of variable $r$ with respect to time $t$).
*   **Right Side:** A sum of four terms, separated by plus ($+$) and minus ($-$) signs.
    *   **Term 1:** $\frac{k_1}{2}\mathbf{U}^T\mathbf{I}$
    *   **Term 2:** $+\frac{k_1}{2\sigma_{td}^2}(r^{td} - r)$
    *   **Term 3:** $-\frac{k_1}{2}g'(r)$
    *   **Term 4:** $-\frac{k_1}{2\sigma^2}\mathbf{Wr}$

**3. Labels, Keys & Legends:**
The equation contains numerous variables and constants:
*   $r$: A variable, likely representing a state or response.
*   $t$: Time.
*   $k_1, k_1/2$: Constants or scaling factors.
*   $\mathbf{U}, \mathbf{I}$: Matrices or vectors (indicated by bold font).
*   $\sigma_{td}^2, \sigma^2$: Variance terms.
*   $r^{td}$: A target or reference value for $r$.
*   $g'(r)$: The derivative of a function $g$ evaluated at $r$.
*   $\mathbf{W}$: A matrix or weight term.

**4. Data Trends & Details:**
As this is a differential equation, there are no plotted data trends; it describes the rate of change ($\frac{dr}{dt}$) based on the current state ($r$) and system parameters.

**5. Contextual Caption Integration:**
Immediately following the equation, there is accompanying text that provides context for the variables:

*   **Text:** "where $\mathbf{W} = \mathbf{U}^T\mathbf{U}$. In this implementation, the neural responses $r$ under..."

This text clarifies that $\mathbf{W}$ is defined as the product of the transpose of $\mathbf{U}$ and $\mathbf{U}$. It also introduces the context that $r$ represents "neural responses" within a specific implementation.

k1
—
σ2

> Figure description (generated): The provided image contains a single mathematical equation, not a complex figure with multiple panels, plots, or schematics.

**Detailed Description:**

1.  **Overall Layout & Structure**: The content is a single, centered mathematical equation presented in standard academic typesetting.
2.  **Visual Components & Symbols**: The equation consists of mathematical symbols, variables, superscripts, subscripts, and standard operators.
3.  **Labels, Keys & Legends**: The equation is:
    $$E_1 = \frac{1}{2\sigma^2} (I - f(Ur))^T (I - f(Ur)) + \frac{1}{2\sigma_{td}^2} (r - r^{td})^T (r - r^{td}) \quad (4)$$
    *   **Variables/Terms**: $E_1$ (the objective function), $\sigma^2$, $\sigma_{td}^2$, $I$ (likely an identity matrix or a related term), $f(\cdot)$ (a function), $Ur$, $r$, and $r^{td}$.
    *   **Operators**: Equality sign ($=$), addition operator ($+$), transpose symbol ($\text{T}$), and fractions.
    *   **Equation Number**: The equation is labeled with the number **(4)** on the right margin.
4.  **Data Trends & Details**: As this is an algebraic expression, there are no data trends or axes to describe.
5.  **Contextual Caption Integration**: The text immediately preceding the equation mentions $\sigma_{td}$ and refers to "the following optimization function," confirming that Equation (4) represents an objective or cost function ($E_1$) being minimized.

> Figure description (generated): The provided input is a snippet of text describing a mathematical function and its application, not an actual figure.

The text reads:
> obtained by using sparse kurtotic prior distributions for $r$ (refs 26,31), e.g.,
> $$g(r) = \alpha \sum_i \log(1 + r_i^2)$$ (6)
> This choice was used for the extra-classical surround experiments in Fig.

Since there is no visual figure provided, I cannot perform the requested detailed description of its layout, components, labels, or data trends.

**Conclusion:** Please provide the actual image/figure you wish me to describe.

> Figure description (generated): The provided image contains a single mathematical equation, presented as an isolated block of text rather than a complex figure with multiple panels or graphical elements.

**1. Overall Layout & Structure:**
The content is a single, numbered mathematical equation displayed centrally on the page. It does not feature panels (A, B, C), flow charts, or plots; it is a symbolic representation of a differential equation.

**2. Visual Components & Symbols:**
The primary components are mathematical symbols, variables, operators, and superscripts/subscripts.

*   **Left Side:** $\frac{dU}{dt}$ (The rate of change of $U$ with respect to time, $t$).
*   **Right Side (Equation 9):** The expression is structured as a fraction:
    $$\frac{dU}{dt} = -\frac{k_2}{2} \frac{\partial E}{\partial U} = -\frac{k_2}{2\sigma^2} \frac{\partial f^T}{\partial x}(I - f(Ur))r^T - k_2\lambda U$$

    *   **Operators:** $\frac{d}{dt}$ (derivative with respect to time), $=$ (equals sign), $\partial$ (partial derivative operator).
    *   **Variables/Parameters:** $U$, $t$, $k_2$, $E$, $\sigma^2$, $f$, $r$, $\lambda$.
    *   **Matrix/Vector Notation:** Superscripts like $T$ (transpose) are used on $f$ and $r$. Parentheses $(\cdot)$ denote grouping.

**3. Labels, Keys & Legends:**
The equation is explicitly labeled with the number **(9)** on the right margin, indicating its sequential placement in the document.

**4. Data Trends & Details:**
As this is an equation and not a plot, there are no axes or data trends to describe.

**5. Contextual Caption Integration:**
Immediately following the equation, there is accompanying text that provides context for the variables:

> "where $k_2$ is a positive parameter determining the learning rate of the net-"

This text clarifies that $k_2$ is a positive parameter related to the learning rate of a network (implied by "net-").


---

## Page 9

© 1999 Nature America Inc. • http://neurosci.nature.com

© 1999 Nature America Inc. • http://neurosci.nature.com

nature neuroscience  •  volume 2  no 1  •  january 1999
87

For the extra-classical RF simulations in Fig. 6, a nonlinear hierarchical
generative model (f(x) = tanh(x)) was used at levels 1 and 2 of the three-
level hierarchical network, along with a kurtotic prior distribution for r
(Equation 6). Nine level-1 modules, each with 32 feedforward model neu-
rons and each analyzing a local 8 × 8 pixel image region, were arranged
in a 3 × 3 overlapping configuration to analyze a 14 × 14 pixel image
region. The level-2 module included 64 feedforward model neurons. The
network was trained on ten prewhitened natural images and during train-
ing, the gain of each basis vector in U was adapted so as to maintain equal
variance on each ri (see ref. 26 for more details). The level-1 basis vectors
were learned first, followed by the level-2 basis vectors.

Acknowledgements
We thank Christof Koch for comments on the manuscript and Mary Hayhoe,
Terrence Sejnowski and members of the Computational Neurobiology Lab at the
Salk Institute for discussions. This work was supported by research grants from
the National Institute of Health (NIH), the National Science Foundation (NSF)
and the Alfred P. Sloan Foundation.

RECEIVED 29 JUNE; ACCEPTED 18 NOVEMBER 1998

1.
Hubel, D. H. & Wiesel, T. N. Receptive fields and functional architecture in
two non-striate visual areas (18 and 19) of the cat. J. Neurophysiol. 28,
229–289 (1965).
2.
Hubel, D. H. & Wiesel, T. N. Receptive fields and functional architecture of
monkey striate cortex. J. Physiol. (Lond.) 195, 215–243 (1968).
3.
Bolz, J. & Gilbert, C. D. Generation of end-inhibition in the visual cortex via
interlaminar connections. Nature 320, 362–365 (1986).
4.
Hubel, D. H. & Livingstone, M. S. Segregation of form, color, and stereopsis
in primate area 18. J. Neurosci. 7, 3378–3415 (1987).
5.
Desimone, R. & Schein, S. J. Visual properties of neurons in area V4 of the
macaque: sensitivity to stimulus form. J. Neurophysiol. 57, 835–868 (1987).
6.
Allman, J., Miezin, F. & McGuinness, E. Stimulus specific responses from
beyond the classical receptive field: Neurophysiological mechanisms for
local-global comparisons in visual neurons. Annu. Rev. Neurosci. 8, 407–429
(1985).
7.
Dobbins, A., Zucker, S. W. & Cynader, M. S. Endstopped neurons in the
visual cortex as a substrate for calculating curvature. Nature 329, 438–441
(1987).
8.
Bolz, J., Gilbert, C. D. & Wiesel, T. N. Pharmacological analysis of cortical
circuitry. Trends Neurosci. 12, 292–296 (1989).
9.
Peterhans, E. & von der Heydt, R. in Representations of Vision. Trends and
Tacit Assumptions (eds Gorea, A., Frégnac, Y., Kapoulis, Z. & Findlay, J.)
111–124 (Cambridge Univ. Press, Cambridge, UK, 1991).
10. Grossberg, S., Mingolla, E. & Ross, W. D. Visual brain and visual perception: how
does the cortex do perceptual grouping? Trends Neurosci. 20, 106–111 (1997).
11. Peterhans, E. & von der Heydt, R. Subjective contours—bridging the gap
between psychophysics and physiology. Trends Neurosci. 14, 112–119 (1991).
12. Rao, R. P. N. & Ballard, D. H. Dynamic model of visual recognition predicts
neural response properties in the visual cortex. Neural Comput. 9, 721–763
(1997).
13. Gallant, J. L., Connor, C. E. & Van Essen, D. C. Neural activity in areas V1, V2
and V4 during free viewing of natural scenes compared to controlled viewing.
Neuroreport 9, 2153–2158 (1998).
14. Attneave, F. Some informational aspects of visual perception. Psychol. Rev. 61,
183–193 (1954).
15. MacKay, D. M. in Automata Studies (eds Shannon, C. E. & McCarthy, J.)
235–251 (Princeton Univ. Press, Princeton, NJ, 1956).
16. Barlow, H. B. in Sensory Communication (ed. Rosenblith, W. A.) 217–234
(MIT Press, Cambridge, MA, 1961).
17. Atick, J. J. Could information theory provide an ecological theory of sensory
processing? Network Comput. Neural Sys. 3, 213–251 (1992).
18. Buchsbaum, G. & Gottschalk, A. Trichromacy, opponent colours coding and
optimum colour information transmission in the retina. Proc. R. Soc. Lond. B
Biol. Sci. 220, 89–113 (1983).
19. Srinivasan, M. V., Laughlin, S. B. & Dubs A. Predictive coding: A fresh view of

inhibition in the retina. Proc. R. Soc. Lond. B Biol. Sci. 216, 427–459 (1982).
20. Dan, Y., Atick, J. J. & Reid, R. C. Efficient coding of natural scenes in the
lateral geniculate nucleus: experimental test of a computational theory. J.
Neurosci. 16, 3351–3362 (1996).
21. Dong, D. W. & Atick, J. J. Temporal decorrelation: a theory of lagged and
nonlagged responses in the lateral geniculate nucleus. Network Comput.
Neural Sys. 6, 159–178 (1995).
22. Mumford, D. On the computational architecture of the neocortex. II. The
role of cortico-cortical loops. Biol. Cybern. 66, 241–251 (1992).
23. Pece, A. E. C. in Artificial Neural Networks 2 (eds Aleksander, I. & Taylor, J.)
865–868 (Elsevier, Amsterdam, 1992).
24. Softky, W. R. in Advances in Neural Information Processing Systems 8 (eds
Touretzky, D., Mozer, M. & Hasselmo, M.) 809–815 (MIT Press, Cambridge,
MA, 1996).
25. Ullman, S. in Large-Scale Neuronal Theories of the Brain (eds Koch, C. &
Davis, J. L.) 257–270 (MIT Press, Cambridge, MA, 1994).
26. Olshausen, B. A. & Field, D. J. Sparse coding with an overcomplete basis set:
A strategy employed by V1? Vision Res. 37, 3311–3325 (1997).
27. Dayan, P., Hinton, G.E., Neal, R.M. & Zemel, R.S. The Helmholtz machine.
Neural Comput. 7, 889–904, (1995).
28. Luettgen, M. R. & Willsky, A. S. Likelihood calculation for a class of
multiscale stochastic models, with application to texture discrimination.
IEEE Trans. Image Proc. 4, 194–207 (1995).
29. Felleman, D. J. & Van Essen, D. C. Distributed hierarchical processing in the
primate cerebral cortex. Cereb. Cortex 1, 1–47 (1991).
30. Field, D. J. Relations between the statistics of natural images and the response
properties of cortical cells. J. Opt. Soc. Am. A 4, 2379–2394 (1987).
31. Bell, A. J. & Sejnowski, T. J. The “independent components” of natural scenes
are edge filters. Vision Res. 37, 3327–3338 (1997).
32. Olshausen, B. A. & Field, D. J. Emergence of simple-cell receptive field
properties by learning a sparse code for natural images. Nature 381, 607–609
(1996).
33. Zipser, K., Lamme, V. A. F. & Schiller, P. H. Contextual modulation in
primary visual cortex. J. Neurosci. 16, 7376–7389 (1996).
34. Sandell, J. H. & Schiller, P. H. Effect of cooling area 18 on striate cortex cells in
the squirrel monkey. J. Neurophysiol. 48, 38–48 (1982).
35. Knierim, J. & Van Essen, D. C. Neural responses to static texture patterns in
area V1 of the alert macaque monkey. J. Neurophysiol. 67, 961–980 (1992).
36. Sillito, A. M., Grieve, K. L., Jones, H. E., Cudeiro, J. & Davis, J. Visual cortical
mechanisms detecting focal orientation discontinuities. Nature 378, 492–496
(1995).
37. Hupé, J. M. et al. Cortical feedback improves discrimination between figure
and background by V1, V2 and V3 neurons. Nature 394, 784–787 (1998).
38. Murphy, P. C. & Sillito, A. M. Corticofugal feedback influences the generation
of length tuning in the visual pathway. Nature 329, 727–729 (1987).
39. Gilbert, C. D. Adult cortical dynamics. Physiol. Rev. 78, 467–485 (1998).
40. Lee, D. D. & Seung, H. S. in Advances in Neural Information Processing
Systems 9 (eds Mozer, M., Jordan, M. & Petsche, T.) 515–521 (MIT Press,
Cambridge, MA, 1997).
41. Heeger, D. J., Simoncelli, E. P. & Movshon, J. A. Computational models of
cortical visual processing. Proc. Natl. Acad. Sci. USA 93, 623–627 (1996).
42. Miller, E. K., Li, L. & Desimone, R. A neural mechanism for working and
recognition memory in inferior temporal cortex. Science 254, 1377–1379
(1991).
43. Gross, C. G. & Sergent, J. Face recognition. Curr. Opin. Neurobiol. 2, 156–161
(1992).
44. Logothetis, N. K. & Pauls, J. Psychophysical and physiological evidence for
viewer-centered object representations in the primate. Cereb. Cortex 5,
270–288 (1995).
45. Poggio, T. & Edelman, S. A network that learns to recognize 3D objects.
Nature 343, 263–266 (1990).
46. Bell, C., Bodznick, D., Montgomery, J. & Bastian, J. The generation and
subtraction of sensory expectations within cerebellum-like structures. Brain
Behav. Evol. 50 Suppl. 1, 17–31 (1997).
47. Schultz, W. et al. in Models of Information Processing in the Basal Ganglia (eds
Houk, J. C., Davis, J. L. & Beiser, D. G.) 233–248 (MIT Press, Cambridge,
MA, 1995).
48. Creutzfeldt, O. D. Generality of the functional structure of the neocortex.
Naturwissenschaften 64, 507–517 (1977).
49. Rao, R. P. N. An optimal estimation approach to visual perception and
learning. Vision Res. (in press).
50. Rissanen, J. Stochastic Complexity in Statistical Inquiry (World Scientific,
Singapore, 1989).

articles
