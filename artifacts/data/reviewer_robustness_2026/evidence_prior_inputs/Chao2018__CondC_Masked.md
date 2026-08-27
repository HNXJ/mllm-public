## 

Article

Large-Scale Cortical Networks for Hierarchical
Prediction and Prediction Error in the Primate Brain

Highlights

d A data-driven analysis (PARAFAC) recovers prediction and

prediction-error signals

d Prediction and prediction-error signals arise from different

cortical areas

d Gamma and alpha/beta bands convey distinct prediction and

prediction-error signals

d Prefrontal cortex sends signals to temporal cortex to update

next-trial predictions

Authors

Zenas C. Chao, Kana Takaura,
Liping Wang, Naotaka Fujii,
Stanislas Dehaene

Correspondence
[MASKED_EMAIL]

In Brief

Predictive-coding theory proposes that
the brain acts as a predictor of sensory
inputs. Using high-density ECoG in
monkeys, [MASKED_AUTHORS] test its core
hypothesis by identifying prediction and
prediction-errors signals at two different
hierarchical levels and examining their
interactions.

[MASKED_AUTHORS], 2018, Neuron 100, 1252-1266
December 5, 2018 ª 2018 Elsevier Inc.

---

## 

Neuron
Article

Large-Scale Cortical Networks
for Hierarchical Prediction
and Prediction Error in the Primate Brain

Zenas C. Chao,1,2,7,* Kana Takaura,2 Liping Wang,3 Naotaka Fujii,2,6 and Stanislas Dehaene4,5,6

1Department of Neuroscience, Graduate School of Medicine and Faculty of Medicine, Kyoto University, Kyoto 6068501, Japan
2[MASKED_INSTITUTION], Wako, Saitama 3510198, Japan
3Institute of Neuroscience, Shanghai Institutes for Biological Sciences, Chinese Academy of Sciences, Shanghai 200031, China
4Cognitive Neuroimaging Unit, CEA DSV/I2BM, INSERM, Universite´ Paris-Sud, Universite´ Paris-Saclay, NeuroSpin Center, 91191 Gif/Yvette,
France
5Colle` ge de France, Paris 75005, France
6Senior author
7Lead Contact
*Correspondence: [MASKED_EMAIL]

SUMMARY

According to predictive-coding theory, cortical areas
continuously generate and update predictions of
sensory inputs at different hierarchical levels and
emit prediction errors when the predicted and actual
inputs differ. However, predictions and prediction
errors are simultaneous and interdependent pro-
cesses, making it difficult to disentangle their con-
stituent neural network organization. Here, we test
the theory by using high-density electrocorticogra-
phy (ECoG) in monkeys during an auditory ''local-
global'' paradigm in which the temporal regularities
of the stimuli were controlled at two hierarchical
levels. We decomposed the broadband data and
identified lower- and higher-level prediction-error
signals in early auditory cortex and anterior temporal
cortex, respectively, and a prediction-update signal
sent from prefrontal cortex back to temporal cortex.
The prediction-error and prediction-update signals
were transmitted via g (>40 Hz) and a/b (<30 Hz) os-
cillations, respectively. Our findings provide strong
support for hierarchical predictive coding and outline
how it is dynamically implemented using distinct
cortical areas and frequencies.

INTRODUCTION

The predictive-coding theory states that the brain constantly
learns statistical regularities in the sensory environment and
actively generates predictions that are confronted to incoming
sensory inputs (Friston, 2005; Mumford, 1992; Rao and Ballard,
1999; Srinivasan et al., 1982). This is achieved by a bidirectional
cascade of cortical processes, where higher-level structures
attempt to predict inputs from lower-level ones through top-

down connections, and error signals are sent back through bot-
tom-up connections in order to update the internal models that
lead to those predictions. This hierarchical predictive-coding
framework offers a unified model of perception, action, and
attention (Clark, 2013; Friston, 2010), and even possibly psychi-
atric disorders such as schizophrenia and autism (Quattrocki
and Friston, 2014; Stephan et al., 2009).

The predictive-coding theory has been supported by a wide
range of evidence, which primarily demonstrates the effects of
a top-down prediction on facilitating behavioral and neural re-
sponses in visual perception (Egner et al., 2010; Kok et al.,
2012; Summerfield et al., 2006; Summerfield and Koechlin,
2008), auditory perception (Todorovic et al., 2011), and audiovi-
sual speech perception (Blank and Davis, 2016). However, one
core hypothesis derived from the predictive-coding model has
not yet been directly evaluated: the existence of simultaneous
and interdependent computations of predictions and prediction
errors, carried out by distinct and hierarchically organized
neuronal populations (as proposed by Friston, 2005), and trans-
mitted between hierarchical levels via cortical oscillations of
distinct frequency channels (as proposed by Arnal and Giraud,
2012; Bastos et al., 2012; Wang, 2010). Recent studies have
shown that bottom-up and top-down signaling utilizes different
frequency channels in both visual processing (Bastos et al.,
2015b; Michalareas et al., 2016; van Kerkoerle et al., 2014) and
auditory processing (D€urschmid et al., 2016; Fontolan et al.,
2014; Sedley et al., 2016), but it remains unclear what kind of in-
formation is carried in these frequency channels (in the predictive
coding perspective) and how they influence each other. Here, we
specifically set out to evaluate the hypothesis by identifying
comprehensive dynamics of prediction and prediction-error sig-
nals and examine their interactions across hierarchies and
frequencies.

Empirically, prediction-error signals have been linked to neural
activity evoked by unexpected or novel stimuli, which has been
detected at both the macroscopic level (Alink et al., 2010; Be-
kinschtein et al., 2009; Egner et al., 2010; El Karoui et al., 2014;
Todorovic et al., 2011; Wacongne et al., 2011) and the

Neuron 100, 1252-1266, December 5, 2018 ª 2018 Elsevier Inc.

---

## 

microscopic level (Eliades and Wang, 2008; Keller et al., 2012).
To evaluate the hierarchical organization of prediction-error sig-
nals, an auditory paradigm named the ''local-global'' paradigm
was created (Bekinschtein et al., 2009), which introduces two
types of temporal regularities (tone-to-tone transition probability
versus overall multi-tone sequence) and uses their violations to
probe novelty responses at two distinct levels of the cortical
hierarchy (Figure 1). The paradigm has been used to investigate
hierarchical auditory processing in humans and non-human pri-
mates (El Karoui et al., 2014; Strauss et al., 2015; Uhrig et al.,
2014; Wacongne et al., 2011; Wang et al., 2015); however, the
precise contributions of prediction and prediction-error signals
in the hierarchical novelty responses remain unclear, due to
the challenge of unwinding the underlying network dynamics
that are not only simultaneous and interdependent, but also
spatially dispersed and temporally fine-tuned.

To overcome the challenge, we combined the auditory local-
global paradigm with large-scale neurophysiological recordings
in non-human primates and their automatized analysis by an
objective decomposition method ([MASKED_AUTHORS], 2015). We used
an electrocorticography (ECoG) system to acquire high-fidelity
broadband neuronal signals from an entire cortical hemisphere
with balanced spatial, spectral, and temporal resolutions (Chao
et al., 2010, 2015; Fukushima et al., 2015; Yanagawa et al.,
2013). After obtaining this large-scale database of cortical activ-
ity, we used an unbiased data-driven analytical approach to
search for multiple, possibly superimposed, time-frequency
components in large-scale network dynamics ([MASKED_AUTHORS],
2015, 2018), and further tested whether their functional profiles
and their trial-by-trial interactions fit with the predictive-coding
framework.

Specifically, the predictive-coding framework predicted that
(1) violations of local transition probability would arise early on,
in a bottom-up manner, from early auditory cortex; (2) violations
of the overall sequence would arise later, still in a bottom-up
manner, from higher-order cortices; (3) the latter violations
would
require
revising
the
mental
representation
of
the
sequence in the higher-level system, thought to involve the pre-
frontal cortex (PFC) (Bekinschtein et al., 2009; Chennu et al.,
2013; El Karoui et al., 2014; Uhrig et al., 2014; Wacongne
et al., 2011), and sending top-down messages updating the
predictions for the next trial in lower-level sensory areas.
Furthermore, our design offered a novel means of testing the
hypothesis that bottom-up and top-down cortical signaling is
achieved, respectively, by message-passing in g versus a/b fre-
quency bands.

RESULTS

Local-Global Paradigm to Establish Hierarchical
Auditory Regularities
Two macaque monkeys, identified as subjects 1 and 2, were
used in this study. During the task, monkeys listened passively
to a series of short sound sequences based on the local-global
auditory paradigm (Figure 1A). To ensure vigilance, monkeys
were required to fixate during each trial (Figure 1B). Cortical
activity was recorded with a 128-channel ECoG array covering
nearly an entire right cerebral hemisphere (Figure 1C).

On each trial, a series of 5 tones were delivered (Figure 1A).
The first 4 tones were identical, either low pitched (tone A) or
high pitched (tone B), but the fifth tone could be either the
same (AAAAA or BBBBB, jointly denoted by xxxxx) or different

Fixation

Tone

200 ~ 300ms
50ms
150ms
> 600ms

x
x
x
x
x

x
x
x
x
Y

x
x
x
x
x

x
x
x
x
Y

x
x
x
x
Y

x
x
x
x
x

×20 (habituation)

×20 (habituation)

×80 (80%)

×20 (20%)

×80 (80%)

×20 (20%)

xxxxx

block

xxxxY

block

xx |xx

xY |xx

xY |xY

xx |xY

B

A

Subject 1

Subject 2

C

ECoG on lateral surface
ECoG on OFC

Local standard
Global standard

This figure presents a schematic illustration of the cortical surface, depicting the placement locations of Electrocorticography (ECoG) electrodes for "Subject 1."

**1. Overall Layout & Structure:**
The figure consists of a single, large anatomical drawing representing the lateral view of a human brain hemisphere. The representation is a simplified outline map, not a detailed histological slice.

**2. Visual Components & Symbols:**
*   **Brain Outline:** A continuous, dark gray line traces the contour of the cerebral cortex in a lateral view.
*   **ECoG Electrode Markers:** Two distinct types of markers are used to denote electrode placement:
    *   **Open Circles ($\circ$):** These markers are scattered across the majority of the cortical surface, representing ECoG electrodes placed on the lateral surface. These are distributed widely across the superior and middle regions of the cortex shown.
    *   **Solid Black Circles ($\bullet$):** A small cluster of solid black circles is located in the posterior-most, inferior region of the depicted cortex. These represent a distinct group of electrode placements.
*   **Cortical Divisions:** Faint, curved lines are drawn across the brain outline, suggesting major sulci or gyral boundaries, dividing the cortical surface into several regions.

**3. Labels, Keys & Legends:**
A legend is provided beneath the main illustration:
*   **$\circ$ ECoG on lateral surface:** This key explicitly defines the open circle symbol.

**4. Data Trends & Details:**
As this is a schematic map rather than a plot, there are no axes or quantitative data trends to describe. The distribution shows a high density of electrodes across the general cortical area, with a localized cluster in one specific posterior region.

**5. Contextual Caption Integration:**
The title above the figure is "Subject 1." The legend clarifies that all markers represent ECoG electrode placements, distinguishing between the general placement ($\circ$) and a specific cluster of placements ($\bullet$).

Local deviant
Global deviant

Local deviant
Global standard

Local standard
Global deviant

Figure 1. Local-Global Paradigm and Experimental Setup
(A) The local-global paradigm.
(B) Sound sequence and task design.
(C) ECoG electrodes layout.

> Figure caption (from PDF text): Figure 1. Local-Global Paradigm and Experimental Setup
(A) The local-global paradigm.
(B) Sound sequence and task design.
(C) ECoG electrodes layout.

### Flow and Arrows
*   A large, thick arrow points from the left margin into the top block (Panel A).
*   A second large, thick arrow points from the left margin into the bottom block (Panel B).

## 

(AAAAB or BBBBA, jointly denoted by xxxxY). Auditory stimuli
were delivered in blocks of 120 trials within which one auditory
sequence was frequent while another was rare. In xxxxx blocks,
20 xxxxx trials were initially delivered to establish the rule; then,
there was a random mixture of 80 xxxxx trials (denoted by xxjxx:
xxxxx trial in xxxxx block) randomly mixed with 20 trials of the
deviant sequence xxxxY (xYjxx: xxxxY trial in xxxxx block).
Conversely, in xxxxY block, 20 trials of xxxxY were initially deliv-
ered, followed by a random mixture of 80 xxxxY trials (xYjxY:
xxxxY trial in xxxxY block) and 20 xxxxx trials (xxjxY: xxxxx trial
in xxxxY block).

This paradigm was designed to contrast two levels of regular-
ity. A local regularity is established within a trial by the repetition
of the first 4 tones, which is either followed or violated by the fifth
tone. A global regularity is established by habituating the subject

to a specific 5-tone sequence, which is either respected or
violated by subsequent sequences. Local and global regularities
are orthogonally varied, yielding four trials types: local and global
standards (xxjxx), local and global deviants (xYjxx), local deviant
but global standard (xYjxY), and local standard but global
deviant (xxjxY).

A Hierarchical Predictive-Coding Model of Local and
Global Novelty
The predictive-coding theory suggests that the brain generates
predictions about the possible incoming sensory events, and
that the difference between the prediction and actual sensory
input, i.e., prediction error, propagates forward throughout
the cortical hierarchy. Figure 2 shows how the predictive-cod-
ing framework may provide qualitative predictions about neural

A

xx|xx
xY|xx

xY|xY
xx|xY

B

X1

X2

X3

x

Y1

Y2

Y3

P1x

Y

PE1x

PE2x

PE1Y

PE2Y

C

)

Unpred. Local (xY|xx − xx|xx)

Pred. Local (xY|xY − xx|xY)

Global (Rare − Frequent)

Full-global

Y

P1x

P2x
P2Y

PE1x
PE1Y

x

PE2x
PE2Y

Full-global

PE1
(PE1x + PE1Y)

PE2
(PE2x + PE2Y
**--
***

Partial-global

Y

PE1x

PE2x

PE1Y

PE2Y

P1x

P2x
P2Y

PE2x
PE2Y

x

Partial-global

PE1
(PE1x + PE1Y)

PE2
(PE2x + PE2Y )
**--
*--
*

No-global

No-global

PE1
(PE1x + PE1Y)

PE2
(PE2x + PE2Y)
**--
**--

Y

PE1x

PE2x

PE1Y

PE2Y

x

P1x

Figure 2. A Predictive-Coding Model of the Local-Global Paradigm
(A) Proposed neural processes in xxxxx blocks. Two hierarchical neuronal populations are shown: one for processing local standard tone x (population X: X1, X2,
and X3), and the other for processing local deviant tone Y (population Y: Y1, Y2, and Y3). On xxjxx trials (top), the fifth tone x (black arrow) is predicted by P1x
(green arrow), and thus no prediction error should be generated. On xYjxx trials (bottom), PE1x and PE1Y (blue arrows) occur and propagate to the higher level
(PE2x and PE2Y).
(B) Left: Neural processes in xxxxY blocks in Full-global. On xYjxY trials, PE1x and PE1Y appear but are fully predicted by P2x and P2Y. On xxjxY trials, PE2x and
PE2Y appear, since PE1x and PE1Y expected by P2x and P2Y are mostly omitted. Middle: xxxxY blocks in Partial-global. Compared with Full-global, the reduced
P2x and P2Y induce PE2x and PE2Y on xYjxY trials and reduce PE2x and PE2Y on xxjxY trials. Right: xxxxY blocks in No-global. Without global predictions,
processes on xYjxY and xxjxY trials are identical to those on xYjxx and xxjxx trials, respectively.
(C) Appearance profiles of PE1 (PE1x and PE1Y) and PE2 (PE2x and PE2Y) under different comparisons (Unpredicted Local, Predicted Local, or Global) and
conditions (Full-global, Partial-global, or No-global). ''*'' indicates that the prediction-error signal appears in the corresponding comparison, and ''-'' indicates that
the error signal cannot be detected by the corresponding comparison.

Neuron 100, 1252-1266, December 5, 2018

---

## 

responses in the local-global paradigm. We hypothesize a
model with two hierarchical levels of predictions and prediction
errors interacting in two neuronal populations: one for process-
ing the local standard tone x, and the other for processing the
local deviant tone Y. The lower-level system predicts tones
solely based on their transition probabilities (Meyniel et al.,
2016); the higher-level system uses the learned sequence to
predict error signals from the lower level when local deviants
are expected by the global rule, and thus to reduce or abolish
the propagation of those error signals up to a higher level.

This model predicts that a two-step propagation of error sig-
nals should be observed in xxxxx blocks (Figure 2A). On xxjxx
trials, the fifth tone x should be predicted by the lower-level
prediction (P1x), and thus no prediction error should be gener-
ated. On xYjxx trials, error signals should occur at the lower
level since the expected tone x is omitted (PE1x) and the
observed tone Y is unpredicted (PE1Y). Such unexpected vio-
lations should continue to propagate to the next hierarchical
level (PE2x and PE2Y). On the other hand, the effects of
higher-level predictions should be specifically observed in
xxxxY blocks (Figure 2B). First, on xYjxY trials, a lower-level
prediction error should still occur, since the final tone Y violates
the transition probability established by the previous stream of
xxxx. But because this local violation is now expected by the
higher-level predictions (P2x and P2Y), its propagation to the
higher-level should be completely canceled out if the global
regularity is fully learned (Full-global), or be reduced if the
global regularity is only partially learned (Partial-global). If the
global regularity is completely unlearned (No-global), the local
violation should continue to propagate as on xYjxx trials. Sec-
ond, on xxjxY trials, only a higher-order violation should be
observed, caused by the unexpected absence of an expected
local violation.

The model further predicts that different hierarchical pro-
cesses can be isolated by comparing brain activity evoked by
different stimuli (Figure 2C). By contrasting xYjxx and xxjxx tri-
als, we can isolate novelty responses that arise when both local
and global regularities are violated, i.e., a local novelty
response that is also unpredicted by the global rule (unpre-
dicted local novelty response, or Unpredicted Local). Similarly,
by contrasting xYjxY and xxjxY trials, we can capture the local
novelty response that is predicted by the global rule (predicted
local novelty response, or Predicted Local). Finally, by contrast-
ing rare trials (Rare, includes xYjxx and xxjxY) and frequent trials
(Frequent, includes xxjxx and xYjxY), we can isolate the global
novelty response (global novelty response, or Global). Based
on the model (as in Figures 2A and 2B), lower-level predic-
tion-error signals (PE1, includes PE1x and PE1Y) should appear
in the unpredicted and predicted local novelty responses but
not in the global novelty response, and higher-level predic-
tion-error signals (PE2, includes PE2x and PE2Y) should appear
in all novelty responses (in Full-global), only in the unpredicted
local and global novelty responses (in Partial-global), or only in
the unpredicted and predicted local novelty responses (in No-
global). It is worth noting that the term ''novelty'' is used here
to describe responses to sequences that violate the rule,
even though the sequences themselves are not novel since
they occur multiple times in a block.

Three Novelty Response Patterns Revealed by
Univariate Analysis
To test the model predictions, we compared ECoG signals from
different trial conditions to obtain novelty responses from the
three comparisons: unpredicted local novelty response (xYjxx -
xxjxx), predicted local novelty response (xYjxY - xxjxY), and
global novelty response (Rare - Frequent). The spatio-spectro-
temporal dynamics of ECoG signals were quantified by the
time-frequency representation (TFR) obtained from wavelet
transformation. Each TFR represents the in-trial cortical dy-
namics from a channel, during the time from 200 ms before the
first tone to 600 ms after the fifth tone (81 time bins), across
the frequencies between 0 and 125 Hz (125 frequency bins).

An example of the three comparisons of TFRs in channel 78,
located in early auditory cortex (rostral parabelt area), is shown
in Figure 3. A novelty response was defined as a significant
difference in TFRs under the corresponding comparison (con-
toured areas in Figure 3), detected by a nonparametric cluster-
based permutation test (a = 0.05 corrected for multiple com-
parisons, see STAR Methods). In the predicted local novelty
response (middle row in Figures 3), an early g-band power
increase (>40 Hz) appeared right after the fifth tone. In the
unpredicted local and global novelty responses (top and
bottom rows, respectively), the g-band power increase ap-
peared not only in the early phase, but also extended to a later
phase, where the early and late g-band power increases jointly
lasted more than 300 ms. Other than the g-band power
increases, the unpredicted local novelty response also con-
tained a b-band power decease (1030 Hz) with a longer la-
tency (top row).

These spectro-temporal patterns (the early g-band increase,
late g-band increase, and late b-band decease) were also
observed in other channels in both subjects (see novelty re-
sponses from all 128 channels in both subjects in Figure S1).
A simple univariate analysis was used to identify the patterns
across all channels (Figure 4A). Most responses were found at
the temporal and frontal sites, and, in subject 1, the orbitofrontal
cortex (OFC) and each spectro-temporal pattern showed distinct
spatial distribution. To see how each response pattern contrib-
uted to different novelty responses, we counted the total number
of channels that contained the response pattern (Figure 4B). In
both subjects, the early g-band increase appeared more in the
unpredicted and predicted local novelty responses than in the
global novelty response, which closely matched the expected
appearance profile of PE1 (Figure 2C). On the other hand, the
late g-band increase and b-band decease were primarily found
in the unpredicted local and global novelty responses, which
matched the expected appearance profile of PE2 in the Partial-
global model (Figure 2C). Moreover, the late g-band increase
and b-band decease could represent opposite hierarchical
signaling in the processing of PE2, since the g and b bands are
thought to subserve bottom-up and top-down communications,
respectively (see Discussion).

In summary, our initial univariate analysis suggested that (1)
the early g-band power increase represented a bottom-up PE1
processing, (2) the late g-band power increase represented
a subsequent bottom-up PE2 processing, (3) the late b-band
power decrease represented a top-down modulation process

Neuron 100, 1252-1266, December 5, 2018

---

## 

associated with PE2, and (4) the global regularity was only
partially predicted (Partial-global in Figure 2).

Three Latent Components in Comprehensive Dynamics
of Network Activity Identified by Data-Driven Analysis
To further test the hypotheses suggested by the univariate anal-
ysis, we aimed to acquire a more comprehensive view of the
novelty responses across the large space of channels, time, fre-
quencies, and conditions. This was achieved by using an unbi-
ased decomposition analysis that extracts latent components
in functional network dynamics ([MASKED_AUTHORS], 2015) (see STAR
Methods and Figure S2). We first pooled novelty responses
from all channels and all comparisons to create a broadband
library. To organize and visualize this dataset, we created a
tensor with three dimensions: Channel (cortical area), Time-Fre-
quency (in-trial dynamics), and Comparison (novelty response),
for the anatomical, dynamic, and functional aspects of the
data, respectively. The dimensionality of the tensor was 128
(channels) by 10,125 (125 time windows and 81 frequency
bins) by 3 (comparisons). To extract structured information
from the dataset, we factorized the 3D tensor into multiple
components by performing parallel factor analysis (PARAFAC),
a generalization of principal-component analysis (PCA) to
higher-order arrays (Harshman and Lundy, 1994) and measured
the consistency of factorization under different iterations of
PARAFAC (Bro and Kiers, 2003) (see STAR Methods).

Three dominant components were identified from the pooled
activity (Figure S3), where each component contained a unique
fingerprint
of
network
anatomy,
dynamics,
and
function,
described by its composition in the three tensor dimensions (Fig-
ure 5). The three components matched the three response

Figure 3. Examples of Partially Superim-
posed Local and Global Novelty Responses
Comparisons of TFRs in channel 78 (red circle).
Averaged
TFRs
in
different
trial
types
are
shown (fist two columns), and the significant
differences
between
them,
i.e.,
novelty
re-
sponses, are outlined (third column). The vertical
lines indicate the five stimuli on each trial. The
color represents the relative activation level,
measured in decibel, compared to the baseline
values (0.2-0 s).

The common axis labels are:
*   X-axis label: "Time (s)"
*   Color bar scale values: 0, 3, 6.

**4. Data Trends & Details (Panel-by-Panel Analysis):**

*   **Unpred. Local Panel:** This heatmap shows a broad distribution of activity across the time axis, with moderate yellow/green values dominating most of the plot. A distinct area of high activity (red/dark red) is visible towards the right side, concentrated around $t \approx 0.8$ to $1.2$ seconds, and slightly offset vertically from the main body of activity.
*   **Pred. Local Panel:** This heatmap shows a more constrained pattern compared to the top panel. The high-activity region (red/dark red) is localized more sharply and vertically towards the right side, appearing as a narrow vertical band of high values around $t \approx 0.9$ to $1.2$ seconds.
*   **Global Panel:** This heatmap displays the most structured high-activity region. The red/dark red activity is concentrated in a distinct, elongated cluster located towards the right side of the plot ($t \approx 0.8$ to $1.2$ seconds). This cluster appears more complex or structured in its vertical extent compared to the other two panels.

In summary, the figure compares three different predictive models by visualizing spatio-temporal activity patterns using color-coded heatmaps across a time course.

patterns found in the initial univariate anal-
ysis. For subject 1, component 1 was
associated with the early g-band power
increase. It was activated mainly in early
auditory cortex (particularly the rostral
parabelt area) (Figure 5A, top), immedi-
ately after the fifth tone and in the g
frequency band (>40 Hz) (Figure 5B, top)
(see the temporal and spectral profiles in
Figure S4). Furthermore, it appeared
mostly in the unpredicted and predicted
local novelty responses (Figure 5C, top).
Component 2 was associated with the
late
g-band
power
increase.
It
was
activated primarily in the anterior temporal cortex (particularly
areas Ts1 and Ts2 in thesuperior temporal gyrus) and secondarily
in PFC (particularly the frontopolar area 10) and the OFC
(Figure 5A, middle), slightly after component 1 but also in the g
frequency band (Figure 5B, middle), and appeared mostly in
the unpredicted local and global novelty responses (Figure 5C,
middle). Component 3 was associated with the late b-band
power decease. It was activated primarily in PFC (partic-
ularly the frontopolar area 10) and secondarily in the superior
temporal cortex and OFC (Figure 5A, bottom), slightly after
component 2 and with a decrease in a/b-band power (<30 Hz)
(Figure 5B, bottom), and appeared mostly in the unpre-
dicted local and global novelty responses as in component 2 (Fig-
ure 5C, bottom). Remarkably similar components were found in
subject 2, except the strong activations in PFC were found in
the dorsolateral PFC (DLPFC), and OFC was not recorded (Fig-
ures 5D-5F).

The data-driven results supported our hypothesis in all three
dimensions. Anatomically (Figures 5A and 5D), component 1
was located around early auditory cortex, in agreement with
its role in the processing of local prediction error, and compo-
nents 2 and 3 were located in higher-order cortices, in agree-
ment with roles in higher-order sequence-level processing
Dynamically (Figures 5B and 5E), the activation timings and
spectral profiles indicated that a bottom-up process (compo-
nent 1) was activated right after the fifth tone, followed by
another bottom-up process (component 2) and a subsequent
top-down process (component 3). Functionally (Figures 5C
and 5F), the components' contributions to the novelty re-
sponses were consistent with the Partial-global model (Fig-
ure 2C) and the results from the univariate analysis (Figure 4B),

Neuron 100, 1252-1266, December 5, 2018

---

## 

again suggesting that component 1 represented the processing
of PE1, and components 2 and 3 were related to the processing
of PE2.

Component 3 as a Top-Down Process Tested by
Directional Network Connectivity
Our results consistently linked components 1 and 2 to PE1 and
PE2, respectively, while component 3 as a top-down process
was so far a speculation based on its frequency characteristics.
To verify that component 3 indeed indexed a top-down process,
we examined the directionality of corticocortical interactions in
the novelty responses. Corticocortical interactions were quanti-
fied by spectral Granger causality (GC) (see STAR Methods),
which uses the phase differences between signals from two
cortical areas to infer their asymmetric causal dependence (Bro-
velli et al., 2004; Kaminski et al., 2001). Each GC represents the
in-trial spectro-temporal dynamics of corticocortical interactions
for a given pair of electrodes, during the time from 200 ms before
the first tone to 600 ms after the fifth tone (81 time bins), and
across frequencies between 0 and 125 Hz (125 frequency bins).

Similar to the activity analysis on TFRs, we compared GCs
across different trial conditions in order to examine changes in
connectivity induced by novelty stimuli. We then pooled novelty
connectivity responses from all connections and all comparisons
to create a tensor with three dimensions: Channel-Channel

(cortical connection), Time-Frequency (in-trial dynamics), and
Comparison (novelty response). For each subject, the dimen-
sionality of the tensor was 16,256 (connections) by 10,125
(125 time windows and 81 frequency bins) by 3 (comparisons).
We then factorized the 3D connectivity tensor by performing
PARAFAC, and only one principal component from the pooled
connectivity was identified (Figure S5).

For both subjects, the principal connectivity component
involved connections from PFC to the temporal cortex (Fig-
ure 6A), about 200 ms after the fifth tone and in the a and b
frequency bands (<30 Hz) (Figure 6B), and appeared only in
the unpredicted local and global novelty responses (Figure 6C).
To further visualize the connectivity patterns, we quantified the
causal density and causal outflow of the interactions (Figure 6D).
Causal density is the sum of all outgoing and incoming interac-
tions for each channel, showing areas with busy interactions.
Causal outflow is the net outgoing interactions of each channel,
indicating the source and sink areas of interactions. Busy inter-
actions were found in the connections from DLPFC to early audi-
tory cortex, anterior temporal cortex, and OFC (in subject 1).

The principal connectivity component could represent the
sameprocess as component 3, since they shared similar anatom-
ical, dynamic, and functional profiles. Spatially, both involved
PFC, early auditory cortex, anterior temporal cortex, and OFC
(in subject 1); spectrally, both appeared in the lower-frequency

A
B

There are three distinct groupings of bars visible:
1. **Top Grouping:** Contains a red bar, a blue bar, and a green bar.
2. **Middle Grouping:** Contains a red bar, a blue bar, and a green bar (though the green bar is not fully visible or present in the same configuration as the others).
3. **Bottom Grouping:** Contains a red bar, a blue bar, and a green bar.

**Labels, Keys & Legends:**
*   **Title:** The figure is titled "Subject 1" at the top.
*   **X-Axis Label:** The horizontal axis is labeled "Number of epochs." This indicates the quantitative measure represented by the length of the bars. The scale ranges from 0 to 80, with major tick marks at intervals of 20 (0, 20, 40, 60, 80).
*   **Y-Axis Labels:** The y-axis labels are partially visible and appear to be categorical. Visible fragments include:
    *   "...ocal" (likely referring to "local") associated with the top grouping.
    *   "...ocal" (likely referring to "local") associated with the middle grouping.
    *   "...obal" (likely referring to "global") associated with the bottom grouping.

**Data Trends & Details:**
The data trends are as follows for each visible grouping:

*   **Top Grouping (Associated with "...ocal"):**
    *   Red Bar: Extends to approximately 15 on the x-axis.
    *   Blue Bar: Extends to approximately 12 on the x-axis.
    *   Green Bar: Extends significantly further, reaching approximately 75 on the x-axis.

*   **Middle Grouping (Associated with "...ocal"):**
    *   Red Bar: Extends to approximately 10 on the x-axis.
    *   Blue Bar: A very short bar, extending slightly past 0 (less than 5).
    *   Green Bar: Not clearly visible or present in the same configuration.

*   **Bottom Grouping (Associated with "...obal"):**
    *   Red Bar: Extends to approximately 8 on the x-axis.
    *   Blue Bar: Extends to approximately 20 on the x-axis.
    *   Green Bar: Extends to approximately 38 on the x-axis.

Figure 4. Spatial Distribution of Different Novelty Response Patterns
(A) The channels contained early g-band power increases (red circles), late g-band power increases (blue), and/or late b-band power decreases (green) in novelty
responses (top: the unpredicted local novelty response, middle: the predicted local novelty response; bottom: the global novelty response) are shown for subjects
1 (left) and 2 (right). Gray dots indicate the locations of all 128 channels.
(B) The number of channels shown early g-band power increases (red), late g-band power increases (blue), and/or late b-band power decreases (green) in
different novelty responses are shown for subjects 1 (top) and 2 (bottom). The spectro-temporal patterns of all novelty responses are shown in Figure S1.

> Figure caption (from PDF text): Figure 4. Spatial Distribution of Different Novelty Response Patterns
(A) The channels contained early g-band power increases (red circles), late g-band power increases (blue), and/or late b-band power decreases (green) in novelty
responses (top: the unpredicted local novelty response, middle: the predicted local novelty response; bottom: the global novelty response) are shown for subjects
1 (left) and 2 (right). Gray dots indicate the locations of all 128 channels.
(B) The number of channels shown early g-band power increases (red), late g-band power increases (blue), and/or late b-band power decreases (green) in
different novelty responses are shown for subjects 1 (top) and 2 (bottom). The spectro-temporal patterns of all novelty responses are shown in Figure S1.

#### **Top Map (Unpredicted Local Novelty Response):**
This map shows a distribution of colored circles across the cortical surface. There is a noticeable cluster of red and blue circles in the central-superior region, with some green markers scattered more broadly.

#### **Middle Map (Predicted Local Novelty Response):**
This map shows a more concentrated distribution of activity. There is a prominent cluster of red circles in the central-superior region, with fewer blue and green markers compared to the top panel.

#### **Bottom Map (Global Novelty Response):**
This map shows a distribution that appears more spread out across the inferior and posterior regions of the cortex, featuring clusters of blue and red circles in the lower portion of the visible hemisphere.

## 

bands (<30 Hz); and, functionally, both were absent from the pre-
dicted local novelty response. Therefore, component 3 could be
indeed associated with top-down information flow triggered by
PE2, compatible with a role in updating predictions and resolving
errors arising in the lower-level auditory cortices.

Coordination among Activity Components Tested by
Within-Trial Functional Correlations
To further verify the postulated roles of the three components,
we examined their coordination by evaluating how their activa-
tions co-varied with each other within individual trials under

A
B
C

### **Top Plot**

*   **Type:** Horizontal Bar Chart.
*   **Y-Axis Categories (Implicit):** Two categories, labeled "local" and "global."
*   **X-Axis Label:** Activation (a.u.). The scale ranges from 0 to 400, with major ticks at intervals of 100.
*   **Data Representation:** Two horizontal blue bars are present:
    *   The bar corresponding to **"local"** extends significantly further along the x-axis, reaching approximately 350 a.u.
    *   The bar corresponding to **"global"** is shorter, extending to approximately 200 a.u.

### **Middle Plot**

*   **Type:** Horizontal Bar Chart.
*   **Y-Axis Categories (Implicit):** Two categories, labeled "local" and "global."
*   **X-Axis Label:** Activation (a.u.). The scale ranges from 0 to 500, with major ticks at intervals of 100.
*   **Data Representation:** Two horizontal blue bars are present:
    *   The bar corresponding to **"local"** is the longest, extending close to 450 a.u.
    *   The bar corresponding to **"global"** is shorter, extending to approximately 300 a.u.

### **Bottom Plot**

*   **Type:** Horizontal Bar Chart.
*   **Y-Axis Categories (Implicit):** Two categories, labeled "local" and "global."
*   **X-Axis Label:** Activation (a.u.). The scale ranges from 0 to 400, with major ticks at intervals of 100.
*   **Data Representation:** Two horizontal blue bars are present:
    *   The bar corresponding to **"local"** extends to approximately 325 a.u.
    *   The bar corresponding to **"global"** is the shortest, extending to approximately 125 a.u.

In summary, the figure presents three comparative bar charts illustrating activation levels under "local" versus "global" conditions across three different experimental contexts, with the x-axis consistently representing Activation in arbitrary units (a.u.).

D
E
F

Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D-F) The same as (A)-(C), but the results are from subject 2.

> Figure caption (from PDF text): Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D-F) The same as (A)-(C), but the results are from subject 2.

## 

different trial conditions. The predictive-coding model predicts
that the activation level of component 1 (PE1) should determine
the activation level of component 2 (PE2), especially on xYjxx
trials where PE2 is directly caused by PE1 (Figure 2A), and on
xYjxY trials where PE2 was the residue of PE1 after partial global
prediction P2 (Figure 2B). Furthermore, the activation level of
component 2 should determine the activation level of compo-
nent 3 (the prediction updates induced by PE2), especially on
xYjxx trials where PE2 propagates to the higher level (Figure 2A),
and on xYjxY and xxjxY trials where smaller PE2 is generated due
to partial global prediction P2 (Figure 2B).

To evaluate these hypotheses, we first estimated how much
each multidimensional component contributed to individual
trials. This was achieved by projecting the TFR of each trial
onto the spatio-spectro-temporal pattern (the first two dimen-
sions) of each component (see STAR Methods). As result, how
much each component contributed to the novelty response on
a given trial was represented by a single scalar, i.e., its projection
value. Examples of contributions of the three components during
xxjxx and xYjxx trials are shown in Figure S6. We then evaluated
whether the contribution of one component correlated with the
contribution of another component (full statistics in Table S1).
Significant correlations under all trial conditions in both subjects
are illustrated in Figure 7A.

The functional correlations strongly supported the proposed
predictive-coding model. First, no correlation was found on xxjxx
trials, which is consistent with the model where no prediction
error arises on xxjxx trials. Second, significant correlations
between components 1 and 2 were found on xYjxx and xYjxY tri-
als, which is consistent with the model where PE2 (component 2)
was causally induced by PE1 (component 1) on xYjxx and xYjxY
trials. Lastly, significant correlations were found between com-
ponents 2 and 3 on xYjxx, xYjxY, and xxjxY trials, which sug-
gested that PE2 always led to a top-down prediction update
(component 3). Furthermore, the correlations were stronger on
xYjxx trials than on xYjxY and xxjxY trials, as predicted by
the model.

Component 3 as Prediction Updates Tested by Across-
Trial Functional Correlations
We demonstrated that component 3 represented a top-down
process that was triggered by the higher-level error PE2. Our
hypothesis is that component 3 represents a prediction update
process that resolved prediction errors at the same hierarchical
level (PE2) and/or at the lower level (PE1). One final predic-
tion is that this model update would affect the processing of
subsequent trials. Specifically, trial-by-trial fluctuations in the
strength of activation of component 3 should affect the amount

0.005

0.01

0.015

Time (s)

Freq (Hz)

−0.2

0.2
0.4
0.6
0.8

1.2

−0.05

0.05

0.005
0.01
0.015
0.02
0.025
0.03

Global

Pred. Local

Unpred. Local

Global

Pred. Local

Unpred. Local

In-trial dynamics

Time-Frequency
Corticocortical connection

Channel-Channel

Novelty response

Comparison

Subject 1

A
B
C

Subject 2

0.5

1.5

−0.5

0.5

0.5

1.5

−0.5

0.5

D
Subject 1

Causal density
Causal outflow

Subject 2

Causal density
Causal outflow

Time (s)

Freq (Hz)

−0.2

0.2
0.4
0.6
0.8

1.2

−0.05

0.05

Activation (a.u.)

Activation (a.u.)

Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outflow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outflow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information flow, respectively.

> Figure caption (from PDF text): Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outflow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outflow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information flow, respectively.

## 

of changes in top-down predictions and affect prediction-error
signals on subsequent trials. We therefore predicted that the
activation level of component 3, on a global deviant trial, should
determine the activation levels on component 2 (PE2) and/or
component 1 (PE1) on the next trial (which is always a global
standard).

Similar to the previous analysis, each single-trial response was
first projected to the three components to capture each compo-
nent's contribution. We then evaluated whether the contribution
of component 3 on the global deviant trials, in both xxxxx block
(i.e., xYjxx trials) and xxxxY block (i.e., xxjxY trials), was corre-
lated to the contributions of components 1 and 2 on the corre-
sponding post-deviant trials. Examples of each component's
contribution in xxxxx block are shown in Figure S7.

The correlations were observed as predicted by the hierar-
chical predictive-coding model (full statistics in Table S2).
Particularly, the activation level of component 3 on xYjxx trials
was significantly correlated to the post-deviant activation levels
of components 1 and 2, and the activation level of component 3
on xxjxY trials was significantly correlated to the post-deviant
activation level of component 2 (Figure 7B). These results indi-
cated that when both local and global regularities were violated
(as on xYjxx trials, Figure 2A), component 3 influenced both
PE1 and PE2 on the next trial. On the other hand, when only
global regularity was violated (as on xxjxY trials, Figure 2B),
component 3 influenced only PE2 on the next trial.

Extraction of Partial Global Prediction Signals
The results from our analyses all supported the model of partial
global prediction (Partial-global). To further examine how the

prediction of global regularity was established, we switched
our focus to the first 20 repetitive xxxxY trials in xxxxY blocks.
We hypothesized that the global prediction was absent or
weak in the early trials and gradually established over the repe-
titions. Therefore, neural processes during the early trials should
be similar to xYjxY in No-global, and neural processes during the
later trials should be similar to xYjxY in either Full-global or
Partial-global (Figure 2B).

To
extract
the
global
prediction
signals,
we
therefore
compared the TFRs from the first 3 trials (Early, trials 1-3) to
the TFRs from the last 3 trials (Late, trials 18-20). The significant
difference in TFRs between Early and Late trials (Late - Early) was
detected by the same nonparametric cluster-based permutation
test used in Figure 3 (a = 0.05 corrected for multiple compari-
sons). All the identified significant differences are shown in
Figure 8. In subject 1, the significant differences were found
primarily in DLPFC and the frontopolar area 10, secondarily in
the dorsal premotor cortex (PMd) (particularly the premotor
area F2), and also the area Ts2 in the superior temporal gyrus
(Figure 8A, left). In subject 2, the significant differences were
found primarily in DLPFC, and secondarily in PMd (the area F2)
and the ventral premotor cortex (PMv) (the area F5) (Figure 8A,
right). In both subjects, the significant differences were found
in the a/b-band power (<30 Hz) as early as the end of the first
tone (Figure 8B).

Based on the model in Figure 2, if the global prediction was
fully established in Late trials, the significant difference (Late -
Early) should contain not only the higher-level predictions (P2x
and P2Y, present in Late trials), but also the higher-level predic-
tion errors (PE2x and PE2Y, present in Early trials) (compare

A

B

C

Figure 7. Evaluation of Functional Correlations between Activity Components within and across Trials
(A) Illustration of the functional correlations between the components within a trial in different trial types. Each black line indicates a significant correlation
(p < 0.05), and the corresponding correlation coefficient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of
the components, not their functional causality. See full statistics in Table S1.
(B) Illustration of the functional correlations between component 3 on the global deviant trials (left: xYjxx: global deviants in xxxxx block; right: xxjxY: global
deviants in xxxxY block) and components 1 and 2 on the following standard trials (post-deviant). Each black line indicates a significant correlation (p < 0.05), and
the corresponding correlation coefficient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of the components,
not their functional causality. See full statistics in Table S2.
(C) Schematics of the proposed hierarchy of cortical signals coding for PE1 (component 1), PE2 (component 2), and prediction updates (component 3) and their
corresponding cortical areas and frequency channels.

> Figure caption (from PDF text): Figure 7. Evaluation of Functional Correlations between Activity Components within and across Trials
(A) Illustration of the functional correlations between the components within a trial in different trial types. Each black line indicates a significant correlation
(p < 0.05), and the corresponding correlation coefficient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of
the components, not their functional causality. See full statistics in Table S1.
(B) Illustration of the functional correlations between component 3 on the global deviant trials (left: xYjxx: global deviants in xxxxx block; right: xxjxY: global
deviants in xxxxY block) and components 1 and 2 on the following standard trials (post-deviant). Each black line indicates a significant correlation (p < 0.05), and
the corresponding correlation coefficient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of the components,
not their functional causality. See full statistics in Table S2.
(C) Schematics of the proposed hierarchy of cortical signals coding for PE1 (component 1), PE2 (component 2), and prediction updates (component 3) and their
corresponding cortical areas and frequency channels.

## Figure Description

The provided image snippet appears to be an illustration related to functional correlations between activity components, likely part of a larger figure (Figure 7). The visible portion shows a schematic diagram illustrating temporal relationships between distinct components.