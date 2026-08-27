## Page 1

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
zenas.c.chao@gmail.com

In Brief

Predictive-coding theory proposes that
the brain acts as a predictor of sensory
inputs. Using high-density ECoG in
monkeys, Chao et al. test its core
hypothesis by identifying prediction and
prediction-errors signals at two different
hierarchical levels and examining their
interactions.

Chao et al., 2018, Neuron 100, 1252–1266
December 5, 2018 ª 2018 Elsevier Inc.
https://doi.org/10.1016/j.neuron.2018.10.004


---

## Page 2

Neuron
Article

Large-Scale Cortical Networks
for Hierarchical Prediction
and Prediction Error in the Primate Brain

Zenas C. Chao,1,2,7,* Kana Takaura,2 Liping Wang,3 Naotaka Fujii,2,6 and Stanislas Dehaene4,5,6

1Department of Neuroscience, Graduate School of Medicine and Faculty of Medicine, Kyoto University, Kyoto 6068501, Japan
2RIKEN Brain Science Institute, Wako, Saitama 3510198, Japan
3Institute of Neuroscience, Shanghai Institutes for Biological Sciences, Chinese Academy of Sciences, Shanghai 200031, China
4Cognitive Neuroimaging Unit, CEA DSV/I2BM, INSERM, Universite´ Paris-Sud, Universite´ Paris-Saclay, NeuroSpin Center, 91191 Gif/Yvette,
France
5Colle` ge de France, Paris 75005, France
6Senior author
7Lead Contact
*Correspondence: zenas.c.chao@gmail.com
https://doi.org/10.1016/j.neuron.2018.10.004

SUMMARY

According to predictive-coding theory, cortical areas
continuously generate and update predictions of
sensory inputs at different hierarchical levels and
emit prediction errors when the predicted and actual
inputs differ. However, predictions and prediction
errors are simultaneous and interdependent pro-
cesses, making it difﬁcult to disentangle their con-
stituent neural network organization. Here, we test
the theory by using high-density electrocorticogra-
phy (ECoG) in monkeys during an auditory ‘‘local-
global’’ paradigm in which the temporal regularities
of the stimuli were controlled at two hierarchical
levels. We decomposed the broadband data and
identiﬁed lower- and higher-level prediction-error
signals in early auditory cortex and anterior temporal
cortex, respectively, and a prediction-update signal
sent from prefrontal cortex back to temporal cortex.
The prediction-error and prediction-update signals
were transmitted via g (>40 Hz) and a/b (<30 Hz) os-
cillations, respectively. Our ﬁndings provide strong
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
framework offers a uniﬁed model of perception, action, and
attention (Clark, 2013; Friston, 2010), and even possibly psychi-
atric disorders such as schizophrenia and autism (Quattrocki
and Friston, 2014; Stephan et al., 2009).

The predictive-coding theory has been supported by a wide
range of evidence, which primarily demonstrates the effects of
a top-down prediction on facilitating behavioral and neural re-
sponses in visual perception (Egner et al., 2010; Kok et al.,
2012; Summerﬁeld et al., 2006; Summerﬁeld and Koechlin,
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
coding perspective) and how they inﬂuence each other. Here, we
speciﬁcally set out to evaluate the hypothesis by identifying
comprehensive dynamics of prediction and prediction-error sig-
nals and examine their interactions across hierarchies and
frequencies.

Empirically, prediction-error signals have been linked to neural
activity evoked by unexpected or novel stimuli, which has been
detected at both the macroscopic level (Alink et al., 2010; Be-
kinschtein et al., 2009; Egner et al., 2010; El Karoui et al., 2014;
Todorovic et al., 2011; Wacongne et al., 2011) and the

1252
Neuron 100, 1252–1266, December 5, 2018 ª 2018 Elsevier Inc.


---

## Page 3

microscopic level (Eliades and Wang, 2008; Keller et al., 2012).
To evaluate the hierarchical organization of prediction-error sig-
nals, an auditory paradigm named the ‘‘local-global’’ paradigm
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
spatially dispersed and temporally ﬁne-tuned.

To overcome the challenge, we combined the auditory local-
global paradigm with large-scale neurophysiological recordings
in non-human primates and their automatized analysis by an
objective decomposition method (Chao et al., 2015). We used
an electrocorticography (ECoG) system to acquire high-ﬁdelity
broadband neuronal signals from an entire cortical hemisphere
with balanced spatial, spectral, and temporal resolutions (Chao
et al., 2010, 2015; Fukushima et al., 2015; Yanagawa et al.,
2013). After obtaining this large-scale database of cortical activ-
ity, we used an unbiased data-driven analytical approach to
search for multiple, possibly superimposed, time-frequency
components in large-scale network dynamics (Chao et al.,
2015, 2018), and further tested whether their functional proﬁles
and their trial-by-trial interactions ﬁt with the predictive-coding
framework.

Speciﬁcally, the predictive-coding framework predicted that
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
Two macaque monkeys, identiﬁed as subjects 1 and 2, were
used in this study. During the task, monkeys listened passively
to a series of short sound sequences based on the local-global
auditory paradigm (Figure 1A). To ensure vigilance, monkeys
were required to ﬁxate during each trial (Figure 1B). Cortical
activity was recorded with a 128-channel ECoG array covering
nearly an entire right cerebral hemisphere (Figure 1C).

On each trial, a series of 5 tones were delivered (Figure 1A).
The ﬁrst 4 tones were identical, either low pitched (tone A) or
high pitched (tone B), but the ﬁfth tone could be either the
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


**Overall Layout & Structure:**
The image is a single, large drawing depicting the lateral view of a cerebral hemisphere (likely representing the cortex). The structure is highly schematic, showing the outer contour of the brain surface with numerous small circles distributed across it.

**Visual Components & Symbols:**
*   **Brain Outline:** A continuous, irregular line traces the outer boundary of a brain hemisphere.
*   **Electrodes/Nodes:** Numerous small, unfilled circles are scattered across the surface of the brain outline. These represent electrode placements (as suggested by the caption "ECoG electrodes layout").
*   **Connections/Lines:** Faint, thin lines connect some of the electrode points, suggesting connectivity or pathways across the cortical surface. These lines are not uniform; some appear to trace general sulci/gyri patterns, while others connect specific points.

**Labels, Keys & Legends:**
*   The only explicit text visible directly on the image is the title: **"Subject 2"**.
*   No axis labels, legends, or specific numerical annotations are present within the drawing itself.

**Data Trends & Details:**
Since this is a schematic map rather than a plot, there are no data trends to describe. The distribution of the small circles (electrodes) appears relatively dense across the visible cortical surface, with some clustering in specific regions.

**Contextual Caption Integration:**
The caption states: "Figure 1. Local-Global Paradigm and Experimental Setup (A) The local-global paradigm. (B) Sound sequence and task design. **(C) ECoG electrodes layout.**"
Given this context, the drawing is a visualization of the **ECoG electrode layout** for Subject 2. The small circles represent the physical locations where Electrocorticography (ECoG) electrodes were placed on the surface of the brain. The lines likely indicate the general anatomical relationships or potential functional connectivity between these recorded sites.

> Figure caption (from PDF text): Figure 1. Local-Global Paradigm and Experimental Setup
(A) The local-global paradigm.
(B) Sound sequence and task design.
(C) ECoG electrodes layout.


### Overall Layout & Structure
The figure is organized into two distinct, large rectangular blocks stacked vertically. Each block illustrates a specific paradigm involving the interplay between "Local" and "Global" standards/deviants. Arrows on the left side indicate a flow or transition into these paradigms.

### Panel (A) - Top Block
The top block illustrates the first paradigm, which is divided into two sub-scenarios:

**1. Top Sub-scenario (Local Standard / Global Standard):**
*   This scenario is represented by a sequence of symbols. The top line shows the pattern: `xx|xxx`.
*   Below this, there is a sequence of symbols representing the auditory/stimulus pattern: `x x x x x`. This sequence is depicted as a series of vertical bars (representing discrete time points or stimuli).
*   The text labels associated with this pattern are:
    *   `Local standard` (aligned above the sequence).
    *   `Global standard` (aligned below the sequence).
*   A quantitative annotation is present to the right: `x80 (80%)`, indicating that this configuration occurs 80% of the time.

**2. Bottom Sub-scenario (Local Deviant / Global Deviant):**
*   This scenario is represented by the pattern: `xY|xxx`.
*   The stimulus sequence below shows a mix of 'x' and 'y': `x x x x Y`.
*   The text labels associated with this pattern are:
    *   `Local deviant` (aligned above the sequence).
    *   `Global deviant` (aligned below the sequence).
*   A quantitative annotation is present to the right: `x20 (20%)`, indicating that this configuration occurs 20% of the time.

### Panel (B) - Bottom Block
The bottom block illustrates a second paradigm, also divided into two sub-scenarios:

**1. Top Sub-scenario (Local Deviant / Global Standard):**
*   This scenario is represented by the pattern: `xY|xY`.
*   The stimulus sequence below shows a mixed pattern: `x x x x Y`.
*   The text labels associated with this pattern are:
    *   `Local deviant` (aligned above the sequence).
    *   `Global standard` (aligned below the sequence).
*   A quantitative annotation is present to the right: `x80 (80%)`.

**2. Bottom Sub-scenario (Local Standard / Global Deviant):**
*   This scenario is represented by the pattern: `xx|xY`.
*   The stimulus sequence below shows a mixed pattern: `x x x x x`. (Note: The visual representation here seems to show a uniform 'x' sequence, but the label implies a specific configuration).
*   The text labels associated with this pattern are:
    *   `Local standard` (aligned above the sequence).
    *   `Global deviant` (aligned below the sequence).
*   A quantitative annotation is present to the right: `x20 (20%)`.

### Flow and Arrows
*   A large, thick arrow points from the left margin into the top block (Panel A).
*   A second large, thick arrow points from the left margin into the bottom block (Panel B).

### Contextual Caption Integration
The caption identifies this figure as illustrating the **Local-Global Paradigm** (Panel A) and the **Sound sequence and task design** (Panel B). The structure clearly maps out how different combinations of local vs. global standards and deviants are presented in the experimental setup.

Neuron 100, 1252–1266, December 5, 2018
1253


---

## Page 4

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
of the ﬁrst 4 tones, which is either followed or violated by the ﬁfth
tone. A global regularity is established by habituating the subject

to a speciﬁc 5-tone sequence, which is either respected or
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
and X3), and the other for processing local deviant tone Y (population Y: Y1, Y2, and Y3). On xxjxx trials (top), the ﬁfth tone x (black arrow) is predicted by P1x
(green arrow), and thus no prediction error should be generated. On xYjxx trials (bottom), PE1x and PE1Y (blue arrows) occur and propagate to the higher level
(PE2x and PE2Y).
(B) Left: Neural processes in xxxxY blocks in Full-global. On xYjxY trials, PE1x and PE1Y appear but are fully predicted by P2x and P2Y. On xxjxY trials, PE2x and
PE2Y appear, since PE1x and PE1Y expected by P2x and P2Y are mostly omitted. Middle: xxxxY blocks in Partial-global. Compared with Full-global, the reduced
P2x and P2Y induce PE2x and PE2Y on xYjxY trials and reduce PE2x and PE2Y on xxjxY trials. Right: xxxxY blocks in No-global. Without global predictions,
processes on xYjxY and xxjxY trials are identical to those on xYjxx and xxjxx trials, respectively.
(C) Appearance proﬁles of PE1 (PE1x and PE1Y) and PE2 (PE2x and PE2Y) under different comparisons (Unpredicted Local, Predicted Local, or Global) and
conditions (Full-global, Partial-global, or No-global). ‘‘*’’ indicates that the prediction-error signal appears in the corresponding comparison, and ‘‘–‘‘ indicates that
the error signal cannot be detected by the corresponding comparison.

1254
Neuron 100, 1252–1266, December 5, 2018


---

## Page 5

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
trials, the ﬁfth tone x should be predicted by the lower-level
prediction (P1x), and thus no prediction error should be gener-
ated. On xYjxx trials, error signals should occur at the lower
level since the expected tone x is omitted (PE1x) and the
observed tone Y is unpredicted (PE1Y). Such unexpected vio-
lations should continue to propagate to the next hierarchical
level (PE2x and PE2Y). On the other hand, the effects of
higher-level predictions should be speciﬁcally observed in
xxxxY blocks (Figure 2B). First, on xYjxY trials, a lower-level
prediction error should still occur, since the ﬁnal tone Y violates
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
global). It is worth noting that the term ‘‘novelty’’ is used here
to describe responses to sequences that violate the rule,
even though the sequences themselves are not novel since
they occur multiple times in a block.

Three Novelty Response Patterns Revealed by
Univariate Analysis
To test the model predictions, we compared ECoG signals from
different trial conditions to obtain novelty responses from the
three comparisons: unpredicted local novelty response (xYjxx –
xxjxx), predicted local novelty response (xYjxY – xxjxY), and
global novelty response (Rare – Frequent). The spatio-spectro-
temporal dynamics of ECoG signals were quantiﬁed by the
time-frequency representation (TFR) obtained from wavelet
transformation. Each TFR represents the in-trial cortical dy-
namics from a channel, during the time from 200 ms before the
ﬁrst tone to 600 ms after the ﬁfth tone (81 time bins), across
the frequencies between 0 and 125 Hz (125 frequency bins).

An example of the three comparisons of TFRs in channel 78,
located in early auditory cortex (rostral parabelt area), is shown
in Figure 3. A novelty response was deﬁned as a signiﬁcant
difference in TFRs under the corresponding comparison (con-
toured areas in Figure 3), detected by a nonparametric cluster-
based permutation test (a = 0.05 corrected for multiple com-
parisons, see STAR Methods). In the predicted local novelty
response (middle row in Figures 3), an early g-band power
increase (>40 Hz) appeared right after the ﬁfth tone. In the
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
appearance proﬁle of PE1 (Figure 2C). On the other hand, the
late g-band increase and b-band decease were primarily found
in the unpredicted local and global novelty responses, which
matched the expected appearance proﬁle of PE2 in the Partial-
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

Neuron 100, 1252–1266, December 5, 2018
1255


---

## Page 6

associated with PE2, and (4) the global regularity was only
partially predicted (Partial-global in Figure 2).

Three Latent Components in Comprehensive Dynamics
of Network Activity Identiﬁed by Data-Driven Analysis
To further test the hypotheses suggested by the univariate anal-
ysis, we aimed to acquire a more comprehensive view of the
novelty responses across the large space of channels, time, fre-
quencies, and conditions. This was achieved by using an unbi-
ased decomposition analysis that extracts latent components
in functional network dynamics (Chao et al., 2015) (see STAR
Methods and Figure S2). We ﬁrst pooled novelty responses
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

Three dominant components were identiﬁed from the pooled
activity (Figure S3), where each component contained a unique
ﬁngerprint
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
shown (ﬁst two columns), and the signiﬁcant
differences
between
them,
i.e.,
novelty
re-
sponses, are outlined (third column). The vertical
lines indicate the ﬁve stimuli on each trial. The
color represents the relative activation level,
measured in decibel, compared to the baseline
values (0.2–0 s).



**1. Overall Layout & Structure:**
The figure consists of a single, large illustration depicting a curved, irregular shape representing the brain's surface (likely a sagittal or lateral view of a cerebral hemisphere). The structure is overlaid with several distinct, irregularly shaped regions delineated by thin lines.

**2. Visual Components & Symbols:**
*   **Brain Outline:** The overall shape is a smooth, curved outline representing the brain tissue.
*   **Regional Divisions:** The surface is divided into several interconnected, lobar-like regions by thin black lines.
*   **Nodes/Points:** Numerous small, open circles ($\circ$) are scattered across the entire surface area within these defined regions. These likely represent individual neurons or sampling points.
*   **Specific Marker:** A single, distinct red filled circle ($\bullet$) is located within one of the central regions. This marker highlights a specific point of interest.
*   **Annotation:** The number "78" is placed in the upper left margin, outside the main brain outline.

**3. Labels, Keys & Legends:**
*   The only legible text directly associated with the diagram is the number **"78"** in the upper left corner.
*   There are no explicit axis labels, legends, or keys provided within the image itself to define what the open circles ($\circ$) or the red dot ($\bullet$) represent, nor do the regional boundaries have specific labels.

**4. Data Trends & Details:**
Since this is a schematic diagram rather than a plot, there are no quantifiable data trends to describe. The distribution of the open circles appears relatively dense across all depicted regions, with a slight concentration visible in some areas.

**5. Contextual Caption Integration:**
No caption was provided, so no contextual integration can be performed based on external information. The figure serves as a topographical map highlighting specific points (the red dot) within anatomically demarcated regions of the brain surface, populated by numerous representative points (the open circles).



**1. Overall Layout & Structure:**
The figure consists of three distinct panels stacked vertically, each representing a different condition: "$xYlxx$", "$xYl\chi Y$", and "Rare". Each panel is a 2D heatmap plot.

**2. Visual Components & Symbols:**
Each subplot utilizes color intensity to represent a variable over time and some other dimension (likely frequency or state, given the axes). The color scale ranges from deep blue/dark colors to bright red/yellow.

*   **X-axis:** Labeled "Time (s)", ranging from 0 to 1.
*   **Y-axis:** Labeled with numerical values ranging from 20 to 120, marked in increments of 20.
*   **Color Coding:** The color gradient indicates the magnitude of the measured variable:
    *   Dark blue/Black areas represent low values.
    *   Yellow and bright red areas represent high values.

**3. Labels, Keys & Legends:**
*   **Panel Titles (Top to Bottom):**
    1.  $xYlxx$
    2.  $xYl\chi Y$
    3.  Rare
*   **Axis Labels:**
    *   X-axis: "Time (s)"
    *   Y-axis: Numerical scale from 20 to 120.

**4. Data Trends & Details (Panel-by-Panel Analysis):**

*   **Top Panel ($xYlxx$):**
    *   The plot shows distinct vertical bands of activity. There are several periods where high activity (yellow/red) appears, particularly around $t \approx 0.1$ s and $t \approx 0.8-1.0$ s.
    *   In the region $y \approx 20-40$, there is a persistent, low-level blue/dark activity across the entire time course.
    *   The high-activity events are concentrated in specific vertical slices across the y-axis.

*   **Middle Panel ($xYl\chi Y$):**
    *   This panel also displays temporal dynamics. High activity (yellow/red) is visible around $t \approx 0.1$ s and again near $t \approx 0.9-1.0$ s, similar to the top panel but potentially with different spatial distribution along the y-axis.
    *   A persistent low-level activity (blue) is visible across the lower range of the y-axis ($y \approx 20-40$).

*   **Bottom Panel (Rare):**
    *   This panel shows a pattern where high activity (yellow/red) is strongly concentrated in the early time window ($t \approx 0$ to $t \approx 0.2$ s) and again in the late window ($t \approx 0.8$ to $t \approx 1.0$ s).
    *   The overall structure of the activity appears more concentrated in these specific time windows compared to the other two panels.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no interpretation regarding cell types or feedback loops can be made based on external information. The figure strictly presents three distinct temporal heatmaps comparing the dynamics under conditions labeled $xYlxx$, $xYl\chi Y$, and "Rare".



**Overall Layout & Structure:**
The figure is structured into three horizontal panels, stacked vertically. Each panel is titled with a specific condition label above the plot area. A horizontal line segment appears to the right of each panel, suggesting a comparative element or continuation across conditions.

**Visual Components & Symbols:**
Each of the three panels contains a 2D plot characterized by color intensity, suggesting a heatmap representation.

*   **X-axis:** The horizontal axis is labeled "Time (s)" and ranges from 0 to approximately 1.2 seconds, marked with tick lines at intervals (e.g., 0, 0.5, 1).
*   **Y-axis:** The vertical axis is not explicitly labeled with a variable name but represents the dimension along which the activity is measured (implied to be some feature or state).
*   **Color Coding:** The plots utilize a color gradient, ranging from dark blue/black (representing low activity or baseline) through yellow and red (representing high activity).

**Panel-Specific Details:**

1.  **Top Panel ($\text{xxlxx}$):**
    *   This panel is titled "$\text{xxlxx}$".
    *   The plot shows a distinct, localized burst of high activity (bright yellow/red) occurring early in the time course, roughly between $t=0$ and $t \approx 0.2$ seconds.
    *   Following this initial burst, there is a broader region of elevated activity (yellow/light blue) that persists across the middle section, peaking around $t=0.5$ to $t=1.0$ seconds before gradually decaying back toward the baseline blue color.

2.  **Middle Panel ($\text{xxl}x\text{Y}$):**
    *   This panel is titled "$\text{xxl}x\text{Y}$".
    *   The plot exhibits a pattern similar to the top panel but with noticeable differences. There is an initial burst of high activity around $t=0$ to $t \approx 0.2$ seconds, similar to the top panel.
    *   The subsequent activity profile appears more complex or sustained than in the $\text{xxlxx}$ panel. There is a clear, broad region of elevated activity spanning from approximately $t=0.3$ to $t=1.2$ seconds, characterized by a mix of yellow and blue hues, suggesting a sustained or modulated response.

3.  **Bottom Panel ($\text{Frequent}$):**
    *   This panel is titled "$\text{Frequent}$".
    *   The plot shows a pattern where the initial high-activity burst around $t=0$ is present, but it appears less intense or more transient compared to the other panels.
    *   The most prominent feature is a strong, broad elevation in activity occurring later in the time course, centered around $t=0.7$ to $t=1.2$ seconds, characterized by intense yellow and red coloring that spans a significant portion of the latter half of the plot.

**Summary of Trends:**
The figure visually compares three temporal activity profiles ($\text{xxlxx}$, $\text{xxl}x\text{Y}$, and $\text{Frequent}$) across a 1.2-second window, highlighting differences in the timing and duration of high-activity states (indicated by warm colors) relative to a baseline state (dark blue).



**1. Overall Layout & Structure:**
The figure is structured vertically, consisting of three distinct panels stacked one above the other. Each panel displays a 2D heatmap visualization, and all three share a common horizontal axis label at the bottom.

**2. Visual Components & Symbols:**
Each panel contains a heatmap where color intensity represents the magnitude of the measured variable. The colors range from deep blue (low values) through yellow/green (intermediate values) to red and dark red (high values).

*   **X-axis:** The horizontal axis is labeled "Time (s)" and ranges from 0 to approximately 1.2 seconds, marked with tick lines at intervals (e.g., 0, 0.5, 1).
*   **Y-axis:** The vertical axis is not explicitly labeled with a variable name but represents spatial dimensions, as indicated by the structure of the heatmaps.
*   **Color Bar/Legend:** To the right of each panel, there is a vertical color bar legend. This legend indicates the scale for the heatmap colors, ranging from blue (low values) to red (high values). The numerical scale shown on the color bar ranges from 0 up to 6.

**3. Labels, Keys & Legends:**
The figure is divided into three main sections, each titled:
*   **Top Panel Title:** "Unpred. Local"
*   **Middle Panel Title:** "Pred. Local"
*   **Bottom Panel Title:** "Global"

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
ately after the ﬁfth tone and in the g
frequency band (>40 Hz) (Figure 5B, top)
(see the temporal and spectral proﬁles in
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
ures 5D–5F).

The data-driven results supported our hypothesis in all three
dimensions. Anatomically (Figures 5A and 5D), component 1
was located around early auditory cortex, in agreement with
its role in the processing of local prediction error, and compo-
nents 2 and 3 were located in higher-order cortices, in agree-
ment with roles in higher-order sequence-level processing
Dynamically (Figures 5B and 5E), the activation timings and
spectral proﬁles indicated that a bottom-up process (compo-
nent 1) was activated right after the ﬁfth tone, followed by
another bottom-up process (component 2) and a subsequent
top-down process (component 3). Functionally (Figures 5C
and 5F), the components’ contributions to the novelty re-
sponses were consistent with the Partial-global model (Fig-
ure 2C) and the results from the univariate analysis (Figure 4B),

1256
Neuron 100, 1252–1266, December 5, 2018


---

## Page 7

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
ﬁed by spectral Granger causality (GC) (see STAR Methods),
which uses the phase differences between signals from two
cortical areas to infer their asymmetric causal dependence (Bro-
velli et al., 2004; Kaminski et al., 2001). Each GC represents the
in-trial spectro-temporal dynamics of corticocortical interactions
for a given pair of electrodes, during the time from 200 ms before
the ﬁrst tone to 600 ms after the ﬁfth tone (81 time bins), and
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
connectivity was identiﬁed (Figure S5).

For both subjects, the principal connectivity component
involved connections from PFC to the temporal cortex (Fig-
ure 6A), about 200 ms after the ﬁfth tone and in the a and b
frequency bands (<30 Hz) (Figure 6B), and appeared only in
the unpredicted local and global novelty responses (Figure 6C).
To further visualize the connectivity patterns, we quantiﬁed the
causal density and causal outﬂow of the interactions (Figure 6D).
Causal density is the sum of all outgoing and incoming interac-
tions for each channel, showing areas with busy interactions.
Causal outﬂow is the net outgoing interactions of each channel,
indicating the source and sink areas of interactions. Busy inter-
actions were found in the connections from DLPFC to early audi-
tory cortex, anterior temporal cortex, and OFC (in subject 1).

The principal connectivity component could represent the
sameprocess as component 3, since they shared similar anatom-
ical, dynamic, and functional proﬁles. Spatially, both involved
PFC, early auditory cortex, anterior temporal cortex, and OFC
(in subject 1); spectrally, both appeared in the lower-frequency

A
B



**Overall Layout & Structure:**
The figure consists of a single, vertical bar chart. The bars are grouped vertically, suggesting different experimental conditions or variables being compared across a quantitative measure on the x-axis.

**Visual Components & Symbols:**
The chart uses three distinct colors for the bars: red, blue, and green. The bars are arranged in clusters corresponding to different labels on the y-axis (though the full y-axis labels are partially truncated or obscured, they appear to be related to "local" and "global").

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


### 1. Overall Layout & Structure
The figure is organized into three stacked panels, each depicting a different type of novelty response pattern for Subject 1. The overall structure is a series of three brain surface renderings, arranged vertically.

### 2. Visual Components & Symbols
Each panel features a schematic representation of a brain surface (likely the lateral view of a hemisphere). Overlaid on this surface are numerous small markers representing electrode channels, and specific colored circles highlight the locations exhibiting particular spectral changes.

**General Elements:**
*   **Brain Surface Outline:** A gray, curved outline represents the cortical surface.
*   **Gray Dots:** Small, scattered gray dots are present across all three panels. According to the caption, these "Gray dots indicate the locations of all 128 channels."
*   **Colored Circles (Markers):** Specific colored circles are used to denote the locations of channels exhibiting specific spectral changes:
    *   **Red Circles:** Indicate channels containing "early g-band power increases."
    *   **Blue Circles:** Indicate channels containing "late g-band power increases."
    *   **Green Circles:** Indicate channels containing "late b-band power decreases."

**Panel Specifics (Top to Bottom):**
*   **Top Panel:** Labeled implicitly as the "unpredicted local novelty response." It shows a dense distribution of red, blue, and green circles clustered in the central-superior region of the depicted cortex.
*   **Middle Panel:** Labeled implicitly as the "predicted local novelty response." This panel shows a sparser distribution, with several red circles clustered in the posterior-central region. Blue and green markers are less prominent or absent compared to the top panel.
*   **Bottom Panel:** Labeled implicitly as the "global novelty response." This panel shows a more widespread distribution of markers, with clusters of red, blue, and green circles visible across the superior and posterior regions.

### 3. Labels, Keys & Legends
The figure itself lacks explicit axis labels or a formal legend within the image frame. However, the caption provides the necessary context:
*   **Title:** "Subject 1" (at the top).
*   **Contextual Labels (from Caption):** The three panels correspond to:
    1.  Top panel: "the unpredicted local novelty response"
    2.  Middle panel: "the predicted local novelty response"
    3.  Bottom panel: "the global novelty response"
*   **Color Key (from Caption):**
    *   Red circles $\rightarrow$ early g-band power increases.
    *   Blue circles $\rightarrow$ late g-band power increases.
    *   Green circles $\rightarrow$ late b-band power decreases.

### 4. Data Trends & Details
The visual data demonstrates a clear shift in the spatial distribution of spectral changes across the three response types:
*   **Unpredicted Local Novelty (Top):** Shows a high density of all three marker types, suggesting widespread involvement in this response type.
*   **Predicted Local Novelty (Middle):** Shows a concentration primarily of red markers in a localized area, suggesting a more constrained spatial pattern compared to the top panel.
*   **Global Novelty (Bottom):** Exhibits a broader, more distributed pattern across the cortex compared to the middle panel, while still showing distinct clusters of all three marker types.

### 5. Contextual Caption Integration
The caption clarifies that the figure illustrates the spatial distribution of three specific spectral signatures (early g-band increase, late g-band increase, and late b-band decrease) across the 128 channels for Subject 1. The distinction between "local" (unpredicted and predicted) and "global" novelty responses is mapped onto the three panels, allowing for a visual comparison of how different types of novelty processing engage specific cortical areas.

> Figure caption (from PDF text): Figure 4. Spatial Distribution of Different Novelty Response Patterns
(A) The channels contained early g-band power increases (red circles), late g-band power increases (blue), and/or late b-band power decreases (green) in novelty
responses (top: the unpredicted local novelty response, middle: the predicted local novelty response; bottom: the global novelty response) are shown for subjects
1 (left) and 2 (right). Gray dots indicate the locations of all 128 channels.
(B) The number of channels shown early g-band power increases (red), late g-band power increases (blue), and/or late b-band power decreases (green) in
different novelty responses are shown for subjects 1 (top) and 2 (bottom). The spectro-temporal patterns of all novelty responses are shown in Figure S1.


### 1. Overall Layout & Structure
The figure consists of three separate, anatomically oriented brain maps stacked vertically. Each map depicts a lateral view of the cerebral cortex (likely representing the outer surface, or gyri/sulci). The overall structure is a series of three panels corresponding to different experimental conditions.

### 2. Visual Components & Symbols
*   **Brain Outline:** A light gray, schematic outline of a brain hemisphere is present in each panel.
*   **Channel Locations (Gray Dots):** Small, faint gray dots are scattered across the cortical surface in all three panels. The caption indicates these represent "the locations of all 128 channels."
*   **Activity Markers (Colored Circles):** Colored circles are overlaid on the brain map, indicating specific channel locations exhibiting particular spectral changes.
    *   **Red Circles:** Represent channels containing "early g-band power increases."
    *   **Blue Circles:** Represent channels containing "late g-band power increases."
    *   **Green Circles:** Represent channels containing "late b-band power decreases."

### 3. Panel-Specific Descriptions (Mapping to Caption)
Based on the caption, these three panels correspond to:
*   **Top Panel:** The unpredicted local novelty response.
*   **Middle Panel:** The predicted local novelty response.
*   **Bottom Panel:** The global novelty response.

#### **Top Map (Unpredicted Local Novelty Response):**
This map shows a distribution of colored circles across the cortical surface. There is a noticeable cluster of red and blue circles in the central-superior region, with some green markers scattered more broadly.

#### **Middle Map (Predicted Local Novelty Response):**
This map shows a more concentrated distribution of activity. There is a prominent cluster of red circles in the central-superior region, with fewer blue and green markers compared to the top panel.

#### **Bottom Map (Global Novelty Response):**
This map shows a distribution that appears more spread out across the inferior and posterior regions of the cortex, featuring clusters of blue and red circles in the lower portion of the visible hemisphere.

### 4. Labels, Keys & Legends
*   **Title:** The figure is titled "Subject 2."
*   **Legend/Key (Inferred from Caption):** The colors are defined by the caption:
    *   Red circles $\rightarrow$ early g-band power increases.
    *   Blue circles $\rightarrow$ late g-band power increases.
    *   Green circles $\rightarrow$ late b-band power decreases.
*   **Annotations:** No specific numerical axes or labels are present on the maps themselves, relying entirely on the external caption for interpretation.

> Figure caption (from PDF text): Figure 4. Spatial Distribution of Different Novelty Response Patterns
(A) The channels contained early g-band power increases (red circles), late g-band power increases (blue), and/or late b-band power decreases (green) in novelty
responses (top: the unpredicted local novelty response, middle: the predicted local novelty response; bottom: the global novelty response) are shown for subjects
1 (left) and 2 (right). Gray dots indicate the locations of all 128 channels.
(B) The number of channels shown early g-band power increases (red), late g-band power increases (blue), and/or late b-band power decreases (green) in
different novelty responses are shown for subjects 1 (top) and 2 (bottom). The spectro-temporal patterns of all novelty responses are shown in Figure S1.


**1. Overall Layout & Structure:**
The figure consists of a single bar chart, which is structured vertically to represent three distinct types of novelty responses: "local" (top), "local" (middle), and "global" (bottom). The chart uses horizontal bars to represent the count of channels exhibiting specific spectral changes.

**2. Visual Components & Symbols:**
*   **Bars:** Three sets of horizontal bars are present, corresponding to the three response types. Each set contains multiple colored bars: red, blue, and green.
*   **Color Coding:**
    *   **Red Bars:** Represent channels containing early g-band power increases.
    *   **Blue Bars:** Represent channels containing late g-band power increases.
    *   **Green Bars:** Represent channels containing late b-band power decreases.
*   **Axes:** The horizontal axis (x-axis) represents the "Number of channels," scaled from 0 to 25. The vertical axis (y-axis) is implicitly segmented by the labels identifying the response type.

**3. Labels, Keys & Legends:**
*   **Title:** "Subject 2" is displayed at the top.
*   **X-Axis Label:** The horizontal axis is labeled "Number of channels."
*   **Y-Axis Labels (Response Types):** The vertical groupings are labeled:
    *   Top grouping: "local" (corresponding to the unpredicted local novelty response, based on the caption).
    *   Middle grouping: "local" (corresponding to the predicted local novelty response, based on the caption).
    *   Bottom grouping: "global" (corresponding to the global novelty response, based on the caption).

**4. Data Trends & Details (Specific Bar Heights):**
The chart displays the following approximate values for Subject 2:

*   **Top "local" Response (Unpredicted Local Novelty):**
    *   Red Bar: Extends to approximately 16.
    *   Blue Bar: Extends to approximately 15.
    *   Green Bar: Extends to approximately 21.

*   **Middle "local" Response (Predicted Local Novelty):**
    *   Red Bar: Extends to approximately 14.
    *   Blue Bar: Not visible or zero length (no blue bar is present).
    *   Green Bar: Extends to a very small value, approximately 1.

*   **Bottom "global" Response (Global Novelty):**
    *   Red Bar: Extends to approximately 4.
    *   Blue Bar: Extends to approximately 15.
    *   Green Bar: Extends to approximately 7.

**5. Contextual Caption Integration:**
The caption clarifies that the colors correspond to specific spectral changes: red = early g-band power increases, blue = late g-band power increases, and green = late b-band power decreases. The three groupings correspond to the unpredicted local novelty response (top), predicted local novelty response (middle), and global novelty response (bottom).

Neuron 100, 1252–1266, December 5, 2018
1257


---

## Page 8

bands (<30 Hz); and, functionally, both were absent from the pre-
dicted local novelty response. Therefore, component 3 could be
indeed associated with top-down information ﬂow triggered by
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



### Overall Layout & Structure
The figure is composed of three panels, stacked one above the other. Each panel displays a simplified outline of a brain hemisphere (likely representing a cortical surface map). The panels are visually separated, and each panel is accompanied by a vertical color bar legend on the right side.

### Visual Components & Symbols
**Brain Outline:** In each panel, a light gray outline represents the cortical surface. Numerous small, unfilled circles ($\circ$) are scattered across this outline, likely representing sampling points or nodes.

**Data Points/Nodes:** Superimposed on the cortical outline are several filled circles of varying sizes and colors. These colored nodes appear to represent localized activity or connectivity strength at specific locations on the cortex.

**Color Coding and Legend:**
A vertical color bar is present to the right of each panel. This legend indicates a continuous scale, ranging from yellow/light colors at the bottom to deep red/dark colors at the top. This color gradient strongly suggests a quantitative measure, such as activation level, connectivity strength, or functional correlation.

**Panel-Specific Observations:**

*   **Top Panel:** Shows several colored nodes clustered in the posterior/parietal region of the outline. The colors range from yellow to dark red, indicating a gradient of measured values across these localized points.
*   **Middle Panel:** Similar to the top panel, this shows a cluster of colored nodes in the posterior region. The distribution and intensity of colors appear slightly different compared to the top panel, though the general spatial location is similar.
*   **Bottom Panel:** This panel displays a broader distribution of colored nodes, particularly concentrated towards the posterior and superior aspects of the outline. The color intensity gradient is visible across these points, showing a range from yellow to dark red.

### Labels, Keys & Legends
*   **Color Bar:** The legend on the right side of each panel uses a continuous color gradient (Yellow $\rightarrow$ Orange $\rightarrow$ Red). While no numerical scale is provided next to the color bar, its function is clearly to map the intensity of the colored nodes.
*   **Text/Annotations:** There are no explicit labels, axis titles, or mathematical notations within the brain outlines themselves. The small unfilled circles ($\circ$) are not labeled but serve as background markers on the cortical surface.

### Data Trends & Details
The figure does not contain traditional plots with labeled axes (X and Y). Instead, it presents spatial data visualization. The trend observed across the three panels is a change in the distribution and intensity of high-value nodes (dark red) across different conditions or time points, as suggested by the sequential presentation of Panel 1, Panel 2, and Panel 3. The color intensity directly correlates with the value indicated by the adjacent legend scale (higher values correspond to darker red).



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



**Overall Layout & Structure:**
The figure is composed of three distinct plots, arranged one above the other. Each plot shares a common structure: a horizontal time axis (x-axis) and a vertical axis representing some normalized or scaled variable (y-axis). A color bar is positioned to the right of each plot, indicating the mapping between color and the measured variable.

**Visual Components & Symbols:**
*   **Plots (Panels):** There are three main plots. The top plot, middle plot, and bottom plot represent different conditions or measurements over time.
*   **Axes:**
    *   The **x-axis** in all three plots is labeled "Time (s)" and ranges from approximately -0.2 s to 1.2 s, with major tick marks at intervals of 0.2 s (e.g., -0.2, 0, 0.2, ..., 1.2).
    *   The **y-axis** in all three plots ranges from 0 to 120, with major tick marks at intervals of 20 (e.g., 20, 40, 60, ..., 120).
*   **Color Coding:** The plots use a color gradient where different colors correspond to different values of the measured variable. A vertical color bar is present next to each plot, showing a transition from deep blue/cyan (low values) through green and yellow, up to bright red (high values).

**Data Trends & Details:**
*   **Top Panel:** Shows a relatively low level of activity (predominantly green/cyan) across most of the time course. A distinct, intense burst of high activity (bright red/yellow) is visible centered around $t \approx 0.7$ s to $t \approx 1.0$ s, localized in the upper half of the y-axis range (roughly between 80 and 120).
*   **Middle Panel:** Exhibits a more widespread pattern of activity compared to the top panel. There are several localized areas of elevated activity (yellow/red) appearing around $t \approx 0.7$ s to $t \approx 1.0$ s, similar in timing to the top panel but potentially more diffuse across the y-axis.
*   **Bottom Panel:** Shows a pattern dominated by lower activity levels (green/cyan) for most of the duration. A small, localized area of elevated activity (blue/light cyan) is visible near the bottom of the y-axis range around $t \approx 1.0$ s to $t \approx 1.2$ s.

**Labels, Keys & Legends:**
*   The x-axis label is consistently "Time (s)".
*   The y-axis labels are numerical values ranging from 0 to 120.
*   The color bars on the right side of each panel serve as legends, mapping colors to intensity levels. No specific variable name is provided for the color scale itself within the visible area of the figure, only the numerical range implied by the axis labels.

D
E
F

Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D–F) The same as (A)–(C), but the results are from subject 2.

> Figure caption (from PDF text): Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D–F) The same as (A)–(C), but the results are from subject 2.


### 1. Overall Layout & Structure
The figure is organized vertically into three panels: (A), (B), and (C). Each panel displays a lateral view of the brain, represented by a light gray outline suggesting cortical folding. Scattered across this surface are numerous small circles representing electrode locations or data points.

### 2. Visual Components & Symbols
**Brain Schematic:** A simplified, lateral view of the brain is shown in each panel. The surface is dotted with small, uniform black circles, representing a dense array of recording sites (electrodes).

**Activity Components:** Within each panel, there are three distinct clusters of colored circles. These colored circles represent the "Principal Activity Components" being analyzed.
*   **Size and Color:** The size of these colored circles varies, and their color ranges from yellow/light orange to deep red.
*   **Color Bar:** To the right of each panel, there is a vertical color bar (legend) that spans from yellow/light colors at the bottom to deep red at the top. This color bar indicates the "activation level (arbitrary unit)," as specified in the caption.

**Spatial Distribution:**
*   **Panel (A):** Shows three distinct clusters of colored circles. One cluster is located more anteriorly and superiorly, another centrally, and a third slightly posterior/inferior.
*   **Panel (B):** Shows three clusters, spatially distributed differently from Panel A. The cluster distribution appears slightly more posterior compared to (A).
*   **Panel (C):** Shows three clusters, which appear more posteriorly located compared to Panels A and B.

### 3. Labels, Keys & Legends
**Internal Annotations:** There are no explicit labels pointing to specific anatomical regions (e.g., prefrontal cortex, parietal lobe) on the brain schematic itself; the representation is purely topographical.

**External Legends/Keys:**
*   A color bar is present next to each panel, indicating the mapping of color intensity to activation level.
*   The caption clarifies that the size and color of each circle represent the activation level (arbitrary unit).

### 4. Data Trends & Details
Since these are topographical maps rather than quantitative plots, trends are described based on spatial distribution and color intensity:
*   **Activation Level Trend:** The presence of deep red circles indicates the highest activation levels within each component, while yellow/light orange circles indicate lower activation levels.
*   **Component Differentiation:** The three components are visually differentiated by their distinct spatial locations on the cortical surface, even though they share a common color scale.

### 5. Contextual Caption Integration
The caption provides crucial context:
*   **Figure Title:** "Principal Activity Components in Novelty Responses."
*   **Panel Interpretation (A, B, C):** These panels represent the "anatomical dimension of the three components in subject 1."
*   **Color/Size Meaning:** The size and color of the circles quantify the "activation level (arbitrary unit)" at the corresponding electrode.
*   **Subsequent Panels:** The caption notes that panels (D–F) present the same data structure but for "subject 2."

> Figure caption (from PDF text): Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D–F) The same as (A)–(C), but the results are from subject 2.


### Overall Layout & Structure
The figure is composed of three stacked plots, arranged vertically. Each plot appears to be a heatmap or time-frequency representation, characterized by color gradients representing activation levels over time.

### Visual Components & Symbols
Each of the three plots shares a consistent structure:
1.  **X-axis (Horizontal):** Labeled "Time (s)", ranging from approximately -0.2 s to 1.2 s, with major tick marks at intervals of 0.2 seconds (e.g., -0.2, 0, 0.2, ..., 1.2).
2.  **Y-axis (Vertical):** Labeled with numerical values ranging from 0 to 120, likely representing some anatomical or functional dimension (as per the caption).
3.  **Color Map:** A color bar is present to the right of each plot, indicating activation level. The colors transition from cooler tones (greens/blues) to warmer tones (yellows, oranges, reds), suggesting increasing activation intensity.

### Labels, Keys & Legends
*   **X-axis Label:** "Time (s)" is present below the horizontal axis of all three plots.
*   **Y-axis Labels:** Numerical markers (20, 40, 60, 80, 100, 120) are present along the vertical axis of all three plots.
*   **Color Bar:** A color scale is visible to the right of each plot, showing a gradient corresponding to activation level.

### Data Trends & Details (Panel-by-Panel Analysis)

**Top Plot (Likely Panel A: Anatomical Dimension):**
*   The plot shows a predominantly green background across most of the time range.
*   A distinct area of high activation (yellow/red) appears starting around $t \approx 0.7$ s and extending to $t \approx 1.2$ s, concentrated in the upper half of the Y-axis range (roughly between 80 and 120).
*   There are some localized patches of activation visible in the middle range of the Y-axis around $t \approx 0.8$ s.

**Middle Plot (Likely Panel B: Dynamic Dimension):**
*   This plot shows a more widespread and intense activation pattern compared to the top plot.
*   A strong, broad area of high activation (bright red/orange) dominates the region from $t \approx 0.9$ s to $t \approx 1.2$ s, spanning a significant portion of the Y-axis range (from approximately 40 up to 120).
*   The activation appears more temporally sustained and spatially broader than in the top plot.

**Bottom Plot (Likely Panel C: Functional Dimension):**
*   This plot exhibits the lowest overall activation intensity compared to the middle plot.
*   Activation is primarily confined to a lower region of the Y-axis (below 40) and appears more transient, peaking around $t \approx 1.0$ s before decaying.
*   The background remains largely green, indicating low activation levels across most of the time-frequency space.

### Contextual Caption Integration
The caption identifies these plots as representing "Principal Activity Components in Novelty Responses" for Subject 1.
*   The top plot corresponds to **(A) The anatomical dimension** of the three components.
*   The middle plot corresponds to **(B) The dynamic dimension** of the three components.
*   The bottom plot corresponds to **(C) The functional dimension** of the three components.
*   The color intensity represents the "activation level (arbitrary unit) at the corresponding electrode."

> Figure caption (from PDF text): Figure 5. Principal Activity Components in Novelty Responses
(A) The anatomical dimension of the three components in subject 1. The size and color of each circle represent the activation level (arbitrary unit) at the
corresponding electrode.
(B) The dynamic dimension of the three components in subject 1.
(C) The functional dimension of the three components in subject 1.
(D–F) The same as (A)–(C), but the results are from subject 2.


### Overall Layout & Structure
The figure is composed of three distinct panels, stacked vertically. Each panel is a horizontal bar chart displaying activation levels for different components.

### Visual Components & Symbols
Each panel features a horizontal bar chart structure:
*   **Y-Axis Representation:** The vertical axis implicitly represents different components, labeled as "local" and "global."
*   **X-Axis Representation:** The horizontal axis represents the magnitude of activation, labeled "Activation (a.u.)" at the bottom of each plot.
*   **Bars:** Solid blue horizontal bars represent the measured activation level for the respective component ("local" or "global").

### Labels, Keys & Legends
**Axes and Titles:**
*   The horizontal axis label for all three plots is **"Activation (a.u.)"**.
*   The vertical labels on the left side of each plot are **"local"** and **"global"**.

**Data Trends & Details (Panel by Panel):**

**Top Plot:**
*   The bar corresponding to **"local"** extends significantly further than the "global" bar, reaching an activation level near 300 a.u.
*   The bar corresponding to **"global"** is shorter, reaching an activation level around 150 a.u.

**Middle Plot:**
*   The bar corresponding to **"local"** is the longest, extending past 300 a.u., reaching approximately 325 a.u.
*   The bar corresponding to **"global"** is significantly shorter, reaching an activation level around 180 a.u.

**Bottom Plot:**
*   The bar corresponding to **"local"** is the longest in this panel, extending past 150 a.u., reaching approximately 175 a.u.
*   The bar corresponding to **"global"** is the shortest, reaching an activation level around 80 a.u.

### Contextual Caption Integration
The provided caption, "Figure 5. Principal Activity Components in Novelty Responses," clarifies the context:
*   The three panels shown correspond to **(A) The anatomical dimension**, **(B) The dynamic dimension**, and **(C) The functional dimension** of the three components in Subject 1.
*   The labels "local" and "global" on the y-axis likely refer to these distinct dimensions or components being analyzed.
*   The caption notes that panels (D–F) show the same data for Subject 2, but these three plots specifically represent Subject 1.

1258
Neuron 100, 1252–1266, December 5, 2018


---

## Page 9

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

To evaluate these hypotheses, we ﬁrst estimated how much
each multidimensional component contributed to individual
trials. This was achieved by projecting the TFR of each trial
onto the spatio-spectro-temporal pattern (the ﬁrst two dimen-
sions) of each component (see STAR Methods). As result, how
much each component contributed to the novelty response on
a given trial was represented by a single scalar, i.e., its projection
value. Examples of contributions of the three components during
xxjxx and xYjxx trials are shown in Figure S6. We then evaluated
whether the contribution of one component correlated with the
contribution of another component (full statistics in Table S1).
Signiﬁcant correlations under all trial conditions in both subjects
are illustrated in Figure 7A.

The functional correlations strongly supported the proposed
predictive-coding model. First, no correlation was found on xxjxx
trials, which is consistent with the model where no prediction
error arises on xxjxx trials. Second, signiﬁcant correlations
between components 1 and 2 were found on xYjxx and xYjxY tri-
als, which is consistent with the model where PE2 (component 2)
was causally induced by PE1 (component 1) on xYjxx and xYjxY
trials. Lastly, signiﬁcant correlations were found between com-
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
level (PE2) and/or at the lower level (PE1). One ﬁnal predic-
tion is that this model update would affect the processing of
subsequent trials. Speciﬁcally, trial-by-trial ﬂuctuations in the
strength of activation of component 3 should affect the amount

0

0.005

0.01

0.015

Time (s)

Freq (Hz)

−0.2
0
0.2
0.4
0.6
0.8
1
1.2

20

40

60

80

100

120

−0.05

0

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



**1. Overall Layout & Structure:**
The figure consists of a single main illustration set against a white background. The primary visual element is a simplified, outline drawing of a brain in sagittal section, overlaid with directional arrows and a color gradient legend positioned to the right.

**2. Visual Components & Symbols:**
*   **Brain Outline:** A light gray, contour-like drawing represents the lateral view of a brain hemisphere.
*   **Directional Arrows:** Multiple thick, elongated arrows are superimposed over the cortical outline, indicating directionality or flow. These arrows vary in color intensity and size, suggesting varying levels of activity or strength.
*   **Color Coding:** The arrows transition across a spectrum of colors, ranging from dark red/maroon to bright yellow/orange. This color gradient is explicitly linked to the legend on the right.
*   **Legend/Color Bar:** To the upper right of the brain schematic, there is a vertical color bar. This bar transitions from dark red at the top to bright yellow/white at the bottom, indicating a quantitative scale (likely representing intensity or magnitude).

**3. Labels, Keys & Legends:**
*   No specific text labels are present directly on the brain schematic itself (e.g., anatomical regions).
*   The color bar lacks explicit numerical labels or units, but its presence implies a quantitative scale associated with the arrow colors.

**4. Data Trends & Details:**
The arrows show a general pattern of flow within the cortical region depicted:
*   Several prominent, thick arrows point generally superiorly and posteriorly across the visualized cortex.
*   The color intensity of these arrows varies: some are deep red (suggesting high magnitude according to the legend), while others towards the lower/anterior parts are more yellow (suggesting lower magnitude).
*   The arrows appear to originate from or interact within a specific, localized area of the cortex shown in the diagram.

**5. Contextual Caption Integration:**
Since no caption was provided, this description relies solely on the visual elements. The schematic strongly suggests a visualization of directed neural pathways or functional connectivity, where arrow thickness and color intensity map to the strength or magnitude of the represented signal/flow.



**1. Overall Layout & Structure:**
The figure consists of a single main plot area, which is a color-coded heatmap. The axes are clearly labeled for time and an unspecified vertical variable (implied by the y-axis scale).

**2. Visual Components & Symbols:**
*   **Heatmap:** The main body of the plot is filled with colors ranging from deep blue/cyan to yellow, orange, and red. The color intensity represents the magnitude of the measured variable.
*   **Vertical Lines:** There are four distinct, thin, black vertical lines superimposed across the plot area. These lines appear to demarcate specific time intervals or events within the recorded data.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled "Time (s)". The scale ranges from approximately -0.2 s to 1.3 s, with major ticks marked at intervals like -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0, and 1.2 s.
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0 to 120, though the label for this axis is truncated or missing in the provided crop.
*   **Color Bar/Legend:** To the right of the main plot, there is a vertical color bar (legend). This legend maps colors to values. The scale ranges from deep blue at the bottom to bright red at the top, indicating a gradient of measured intensity.

**4. Data Trends & Details:**
*   The plot shows a generally low-activity state (indicated by green/cyan colors) across most of the time course.
*   There is a distinct region of high activity (indicated by yellow, orange, and red) concentrated towards the right side of the plot, specifically between approximately $t=0.9$ s and $t=1.2$ s, and across a specific range on the y-axis (roughly between 10 and 30).
*   The vertical black lines appear to segment the time axis, with notable changes in color intensity occurring around these markers.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no interpretation based on external context can be offered. The figure visually represents a time-series measurement where activity peaks significantly in the latter half of the recorded period.

Subject 2

0

0.5

1

1.5

−0.5

0

0.5

0

0.5

1

1.5

−0.5

0

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
0
0.2
0.4
0.6
0.8
1
1.2

20

40

60

80

100

120

−0.05

0

0.05

0
50
100
150
200
250
Activation (a.u.)



**1. Overall Layout & Structure:**
The figure consists of a single, large schematic representation of a brain slice or cortical area. The overall style is a simplified neural circuit diagram overlaid onto a representation of the cerebral cortex, viewed from the side (sagittal view).

**2. Visual Components & Symbols:**
*   **Cortical Outline:** A light gray, irregularly shaped outline represents the general structure of the brain/cortex.
*   **Neural Activity Representation:** Within this outline, there are multiple representations of neural pathways or activity streams. These are depicted as thick, elongated arrows originating from and converging toward a specific region in the lower-middle portion of the cortex.
*   **Color Coding (Activity Intensity):** The arrows are color-coded, indicating varying levels of activity or strength.
    *   The colors range from bright yellow/light orange to deep red, suggesting a gradient of intensity.
    *   The arrows pointing toward the lower region are predominantly colored in shades of red and orange, indicating high activity.
*   **Directionality:** The arrows generally show a flow of information: some appear to originate from superior/posterior regions and project downwards, while others show convergence into a localized area.
*   **Color Bar/Legend:** To the right of the main schematic, there is a vertical color bar. This bar transitions from deep red at the top to bright yellow/white at the bottom, serving as a legend for the color-coding used in the neural pathways.

**3. Labels, Keys & Legends:**
*   **Color Bar Legend:** The color bar itself lacks explicit numerical labels but visually represents a spectrum, likely corresponding to the intensity scale used in the arrows.
*   **Internal Labels:** There are no explicit anatomical labels (e.g., layers, gyri) or functional annotations directly on the schematic itself, other than the implied representation of cortical structure.

**4. Data Trends & Details:**
Since this is a schematic diagram rather than a quantitative plot, there are no axes or numerical data trends to report. The visual detail focuses on the *pattern* of connectivity: a dense convergence of high-intensity (red/orange) pathways into a specific subregion.

**5. Contextual Caption Integration:**
No caption text was provided, so no specific contextual integration can be performed. The figure visually represents a localized area of high functional connectivity or strong input/output within the cortex, as indicated by the dense, color-coded arrows converging in a specific region.



**1. Overall Layout & Structure:**
The figure consists of a single, large plot area with axes labeled for time and an implicit vertical axis (which is not explicitly labeled but represents the state variable). A color bar legend is positioned to the right of the main plot area.

**2. Visual Components & Symbols:**
*   **Main Plot Area:** The plot uses a color gradient to represent intensity or magnitude across the time-state space.
*   **Color Coding:** The color scale ranges from deep blue/cyan (low values) through green, yellow, and culminates in bright red/orange (high values).
*   **Structure:** The plot is divided vertically by several thin, dark gray lines, suggesting discrete bins or segments along the horizontal (Time) axis.

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled "Time (s)".
*   **Y-Axis Scale:** The vertical axis ranges from 0 to 120, with major tick marks every 20 units (0, 20, 40, 60, 80, 100, 120). The label for the Y-axis is truncated or missing in the provided view, but its numerical scale is clear.
*   **Color Bar Legend:** A vertical color bar is present on the right side, corresponding to the intensity scale. It shows a gradient from dark blue at the bottom to bright red at the top, indicating the range of the measured variable.

**4. Data Trends & Details:**
*   **General Activity:** The majority of the plot area is colored in shades of light green, indicating moderate or baseline activity.
*   **Low Activity Regions:** There are patches of cyan/light blue visible, particularly in the region around $t = -0.2$ s and scattered throughout the plot at lower intensity levels.
*   **High Activity Region:** A distinct, localized region of high activity (bright yellow and red) is visible towards the right side of the plot. This peak activity occurs roughly between $t = 0.9$ s and $t = 1.2$ s, centered around a specific value on the vertical axis (approximately between 20 and 30).

**5. Contextual Caption Integration:**
No specific contextual caption was provided, so no interpretation based on external labels (like cell types or feedback loops) can be made. The figure visually represents the temporal evolution of a variable (Y-axis) as a function of time (X-axis), highlighting transient periods of high activity.

0
50
100
150
200
Activation (a.u.)

Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outﬂow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outﬂow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information ﬂow, respectively.

> Figure caption (from PDF text): Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outﬂow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outﬂow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information ﬂow, respectively.


**1. Overall Layout & Structure:**
The figure presents a lateral view schematic of the human brain, specifically depicting cortical regions. The visualization uses colored circles overlaid onto this anatomical outline to represent connectivity metrics. A color bar/legend is positioned to the right of the brain schematic, indicating a scale related to the data represented by the circles.

**2. Visual Components & Symbols:**
*   **Anatomical Outline:** A simplified, white outline of a lateral view of the brain is shown.
*   **Data Points (Circles):** Multiple colored circles are scattered across the cortical surface, representing specific channels or regions of interaction.
    *   **Color Coding:** The circles exhibit a gradient of colors, ranging from yellow/light orange to deep red.
    *   **Size Variation:** The circles vary in size, suggesting that both color and size encode information about the connectivity.
*   **Color Bar/Legend:** To the right of the brain, there is a vertical color gradient bar. This bar transitions from yellow/light colors at the bottom to deep red at the top, corresponding to the color scale used for the circles.

**3. Labels, Keys & Legends:**
*   **Title Fragment:** The visible text fragment above the image is "Causal density".
*   **Color Bar Interpretation (Inferred from Caption):** The caption states: "For causal density, the size and color of each circle represent the sum of all outgoing and incoming interactions at the corresponding channel." This indicates that color and size together encode the total interaction strength (sum of incoming and outgoing interactions).

**4. Data Trends & Details:**
The data points are clustered in specific areas of the cortex:
*   **Posterior/Parietal Region:** There is a cluster of medium-to-large, reddish circles located towards the upper posterior aspect of the visible cortex.
*   **Temporal/Inferior Region:** A more concentrated cluster of large, dark red circles is visible in the lower-middle section of the cortex.
*   **Scattered Points:** Smaller, yellow/orange circles are distributed more sparsely across the remaining cortical surface.

**5. Contextual Caption Integration:**
The caption identifies this specific visualization as representing the **"Causal density"** of a connectivity component (Figure 6(D)). The description confirms that the visual encoding is:
*   **Size and Color:** Represent the *sum of all outgoing and incoming interactions* at that channel.
*   The color bar visually maps this summed interaction strength, with deeper reds likely corresponding to higher density values.

> Figure caption (from PDF text): Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outﬂow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outﬂow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information ﬂow, respectively.


**1. Overall Layout & Structure:**
The figure is dominated by a single, large anatomical rendering of a brain surface (likely the lateral view of the cerebral cortex). This visualization is overlaid with several colored circular markers, and a color bar legend is positioned to the right of the brain rendering. Based on the provided caption, this specific panel corresponds to **Panel (D)** of a larger figure set.

**2. Visual Components & Symbols:**
*   **Anatomical Rendering:** A light gray, curved surface representing the brain cortex is shown in a lateral view.
*   **Nodes/Channels:** Multiple small, colored circles are scattered across the surface of the brain rendering. These represent specific channels or regions of interest (ROIs).
*   **Color Coding:** The circles exhibit a gradient of colors, ranging from red to blue.
    *   The color bar legend on the right indicates a continuous scale: **Red** corresponds to high values (up to 1.5), transitioning through orange/white, and ending in **Blue** for low values (down to 0).
    *   The caption specifies that for "Causal Outflow," the color represents the net outgoing interactions. **Red channels represent source areas of information flow, and blue channels represent sink areas.**
*   **Size Coding:** The size of the circles varies. The caption states that for "Causal Outflow," the **size** of each circle represents the net outgoing interactions of that channel.

**3. Labels, Keys & Legends:**
*   **Title/Panel Label:** The visible title fragment is "Causal Outflow."
*   **Color Bar Legend:** A vertical color bar is present on the right side, ranging from a deep red at the top to a deep blue at the bottom. Numerical markers are visible along this bar: **0, 0.5, 1, and 1.5**.
*   **Contextual Annotation (from Caption):** The caption clarifies that for "Causal Outflow," the size and color of each circle represent the net outgoing interactions.

**4. Data Trends & Details:**
The visualization shows a distribution of activity across the cortical surface:
*   **High Outflow (Red/Orange):** Several nodes in the superior and posterior regions of the visible cortex display larger, redder circles (e.g., near the top right).
*   **Low Outflow/Sink Areas (Blue):** Several nodes, particularly in the inferior and central regions of the visible cortex, display smaller or blue circles.
*   **Intermediate Activity:** Nodes in between exhibit intermediate sizes and colors (e.g., light orange/blue).

**5. Contextual Caption Integration:**
The caption identifies this visualization as representing the **"Causal outflow of the connectivity component in subject 1 (left) and 2 (right)."** Since only one brain rendering is shown, this specific image likely represents the data for Subject 1 or a composite view. The key interpretation provided is:
*   **Red channels $\rightarrow$ Source areas of information flow.**
*   **Blue channels $\rightarrow$ Sink areas of information flow.**

> Figure caption (from PDF text): Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outﬂow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outﬂow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information ﬂow, respectively.


### 1. Overall Layout & Structure
The figure presents a single, large schematic map of the cortical surface (a lateral view of a brain hemisphere). The visualization uses colored circles overlaid onto this anatomical outline to represent localized measures of "Causal density."

### 2. Visual Components & Symbols
*   **Anatomical Outline:** A simplified, gray outline depicts the lateral surface of a brain hemisphere.
*   **Nodes/Channels:** Multiple colored circles are distributed across the cortical surface, representing specific channels or regions of interaction.
*   **Color Coding (Causal Density):** The color of the circles corresponds to a continuous scale indicated by a vertical color bar located on the right side of the image.
    *   The scale ranges from dark red/maroon (at the top of the bar) through orange, yellow, and finally to a lighter color/white (at the bottom of the bar).
    *   The caption specifies that for "Causal density," **the size and color of each circle represent the sum of all outgoing and incoming interactions at the corresponding channel.**
*   **Specific Node Characteristics:**
    *   Most nodes are small to medium-sized circles.
    *   There is one prominent, large black circle located towards the posterior/inferior aspect of the visualized cortex.
    *   The colors observed include deep red, orange, yellow, and a few lighter nodes.

### 3. Labels, Keys & Legends
*   **Title:** The visible title fragment is "Causal density."
*   **Color Bar/Legend:** A vertical color bar is present on the right edge of the image. It transitions from dark red at the top to yellow/light color at the bottom, indicating the scale for causal density.
*   **Caption Reference:** The caption identifies this visualization as representing "Causal density and causal outflow of the connectivity component in subject 1 (left) and 2 (right)," implying this specific image likely represents one of these subjects or a composite view.

### 4. Data Trends & Details
The distribution shows clusters of high-density activity (indicated by red/orange circles) concentrated in the superior and posterior regions of the visualized cortex. There is a distinct, large, dark node located in a more inferior/posterior area, which stands out significantly from the surrounding nodes. The density appears heterogeneous across the cortical surface.

> Figure caption (from PDF text): Figure 6. Principal Connectivity Component
(A) The anatomical dimension of the principal connectivity component in subjects 1 (top) and 2 (bottom). The width and color of each arrow represent the
activation level (arbitrary unit) in the corresponding connection.
(B) The dynamic dimension of the connectivity component.
(C) The functional dimension of the connectivity component.
(D) Causal density and causal outﬂow of the connectivity component in subject 1 (left) and 2 (right). For causal density, the size and color of each circle represent
the sum of all outgoing and incoming interactions at the corresponding channel. For causal outﬂow, the size and color of each circle represent the net outgoing
interactions of each channel, where red and blue channels represent source and sink areas of the information ﬂow, respectively.


**1. Overall Layout & Structure:**
The visualization is a single, sagittal-like rendering of a cortical surface (a brain hemisphere view). It does not appear to be divided into labeled panels (A, B, C, D) within this specific crop, but the context provided by the caption suggests it corresponds to Panel (D) of a larger figure. The visualization uses colored circles overlaid onto the cortical surface map to represent specific data points related to causal outflow.

**2. Visual Components & Symbols:**
*   **Cortical Surface Map:** A light gray outline depicts the curved surface of a brain hemisphere.
*   **Data Points (Circles):** Multiple colored circles are scattered across the cortical surface map. These circles represent specific channels or regions of interaction within the connectivity component.
*   **Color Coding:** The circles exhibit a gradient color scheme ranging from deep red to light orange/yellow, and also shades of blue.
*   **Scale Bar/Legend:** To the right of the main visualization, there is a vertical color bar (legend) that spans from deep red at the top to deep blue at the bottom. This legend is associated with a numerical scale ranging from 0 to 1.5 on the left side of the map, suggesting that the color intensity corresponds to a quantitative measure (likely activation level or net interaction strength).

**3. Labels, Keys & Legends:**
*   **Title:** "Causal Outflow" is displayed above the visualization.
*   **Y-Axis Scale (Left):** A numerical scale runs vertically along the left side of the map, marked with values: 0, 0.5, 1, and 1.5. This scale likely corresponds to the quantitative measure represented by the color gradient in the legend.
*   **Color Legend:** The vertical bar on the right acts as a color key, mapping colors to values.

**4. Data Trends & Details:**
The distribution of the colored circles shows clustering:
*   **Red/Orange Areas (Source):** There is a concentration of red and orange circles in the posterior-superior region of the visualized cortex. These areas correspond to higher values on the scale (approaching 1.5).
*   **Blue Areas (Sink):** There are distinct clusters of blue circles, particularly in the inferior and posterior regions. These correspond to lower values on the scale (approaching 0).
*   **Mixed Areas:** Intermediate colors (light orange, light blue) are scattered throughout the map.

**5. Contextual Caption Integration:**
The caption identifies this visualization as representing **"Causal outflow of the connectivity component in subject 1 (left) and 2 (right)"** under Panel (D).
*   The caption specifies that for "causal outflow," **"the size and color of each circle represent the net outgoing interactions of each channel."**
*   Crucially, it defines the color meaning: **"red and blue channels represent source and sink areas of the information flow, respectively."** This confirms that red indicates a net outgoing interaction (source), and blue indicates a net incoming interaction (sink). The color bar likely quantifies the magnitude of this net flow.

Neuron 100, 1252–1266, December 5, 2018
1259


---

## Page 10

of changes in top-down predictions and affect prediction-error
signals on subsequent trials. We therefore predicted that the
activation level of component 3, on a global deviant trial, should
determine the activation levels on component 2 (PE2) and/or
component 1 (PE1) on the next trial (which is always a global
standard).

Similar to the previous analysis, each single-trial response was
ﬁrst projected to the three components to capture each compo-
nent’s contribution. We then evaluated whether the contribution
of component 3 on the global deviant trials, in both xxxxx block
(i.e., xYjxx trials) and xxxxY block (i.e., xxjxY trials), was corre-
lated to the contributions of components 1 and 2 on the corre-
sponding post-deviant trials. Examples of each component’s
contribution in xxxxx block are shown in Figure S7.

The correlations were observed as predicted by the hierar-
chical predictive-coding model (full statistics in Table S2).
Particularly, the activation level of component 3 on xYjxx trials
was signiﬁcantly correlated to the post-deviant activation levels
of components 1 and 2, and the activation level of component 3
on xxjxY trials was signiﬁcantly correlated to the post-deviant
activation level of component 2 (Figure 7B). These results indi-
cated that when both local and global regularities were violated
(as on xYjxx trials, Figure 2A), component 3 inﬂuenced both
PE1 and PE2 on the next trial. On the other hand, when only
global regularity was violated (as on xxjxY trials, Figure 2B),
component 3 inﬂuenced only PE2 on the next trial.

Extraction of Partial Global Prediction Signals
The results from our analyses all supported the model of partial
global prediction (Partial-global). To further examine how the

prediction of global regularity was established, we switched
our focus to the ﬁrst 20 repetitive xxxxY trials in xxxxY blocks.
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
compared the TFRs from the ﬁrst 3 trials (Early, trials 1–3) to
the TFRs from the last 3 trials (Late, trials 18–20). The signiﬁcant
difference in TFRs between Early and Late trials (Late – Early) was
detected by the same nonparametric cluster-based permutation
test used in Figure 3 (a = 0.05 corrected for multiple compari-
sons). All the identiﬁed signiﬁcant differences are shown in
Figure 8. In subject 1, the signiﬁcant differences were found
primarily in DLPFC and the frontopolar area 10, secondarily in
the dorsal premotor cortex (PMd) (particularly the premotor
area F2), and also the area Ts2 in the superior temporal gyrus
(Figure 8A, left). In subject 2, the signiﬁcant differences were
found primarily in DLPFC, and secondarily in PMd (the area F2)
and the ventral premotor cortex (PMv) (the area F5) (Figure 8A,
right). In both subjects, the signiﬁcant differences were found
in the a/b-band power (<30 Hz) as early as the end of the ﬁrst
tone (Figure 8B).

Based on the model in Figure 2, if the global prediction was
fully established in Late trials, the signiﬁcant difference (Late –
Early) should contain not only the higher-level predictions (P2x
and P2Y, present in Late trials), but also the higher-level predic-
tion errors (PE2x and PE2Y, present in Early trials) (compare

A

B

C

Figure 7. Evaluation of Functional Correlations between Activity Components within and across Trials
(A) Illustration of the functional correlations between the components within a trial in different trial types. Each black line indicates a signiﬁcant correlation
(p < 0.05), and the corresponding correlation coefﬁcient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of
the components, not their functional causality. See full statistics in Table S1.
(B) Illustration of the functional correlations between component 3 on the global deviant trials (left: xYjxx: global deviants in xxxxx block; right: xxjxY: global
deviants in xxxxY block) and components 1 and 2 on the following standard trials (post-deviant). Each black line indicates a signiﬁcant correlation (p < 0.05), and
the corresponding correlation coefﬁcient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of the components,
not their functional causality. See full statistics in Table S2.
(C) Schematics of the proposed hierarchy of cortical signals coding for PE1 (component 1), PE2 (component 2), and prediction updates (component 3) and their
corresponding cortical areas and frequency channels.

> Figure caption (from PDF text): Figure 7. Evaluation of Functional Correlations between Activity Components within and across Trials
(A) Illustration of the functional correlations between the components within a trial in different trial types. Each black line indicates a signiﬁcant correlation
(p < 0.05), and the corresponding correlation coefﬁcient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of
the components, not their functional causality. See full statistics in Table S1.
(B) Illustration of the functional correlations between component 3 on the global deviant trials (left: xYjxx: global deviants in xxxxx block; right: xxjxY: global
deviants in xxxxY block) and components 1 and 2 on the following standard trials (post-deviant). Each black line indicates a signiﬁcant correlation (p < 0.05), and
the corresponding correlation coefﬁcient is labeled and represented by its thickness. The direction of each arrow indicates the temporal order of the components,
not their functional causality. See full statistics in Table S2.
(C) Schematics of the proposed hierarchy of cortical signals coding for PE1 (component 1), PE2 (component 2), and prediction updates (component 3) and their
corresponding cortical areas and frequency channels.


## Figure Description

The provided image snippet appears to be an illustration related to functional correlations between activity components, likely part of a larger figure (Figure 7). The visible portion shows a schematic diagram illustrating temporal relationships between distinct components.

### 1. Overall Layout & Structure
The visible portion displays a schematic flow diagram, characterized by nodes (representing activity components) connected by directional arrows. This structure suggests a temporal sequence or functional progression between different states or events within an experimental trial.

### 2. Visual Components & Symbols
*   **Nodes (Components):** There are at least three distinct, irregularly shaped nodes visible in the sequence. These nodes appear to be stylized representations of brain activity components (e.g., ERP/ERF components).
    *   The top node is partially visible and contains a small, orange/red circular marker.
    *   The middle node is clearly visible and also contains a small, orange/red circular marker.
    *   The bottom node is partially visible at the base of the flow.
*   **Connections (Arrows):** Thick, dark green arrows connect these nodes sequentially, indicating temporal order.
    *   An arrow originates from the top node and points downward toward the middle node.
    *   A second, longer arrow originates from the middle node and points downward toward the bottom node.
*   **Lines/Correlations:** The caption mentions that "Each black line indicates a significant correlation," suggesting that the connections shown might represent these correlations, although in this specific snippet, only thick green arrows are prominent.

### 3. Labels, Keys & Legends
*   **Text Annotations:** To the right of the flow diagram, there are partial text labels:
    *   "Co" (likely part of a larger word like "Correlation").
    *   "Pre" (likely indicating 'Pre-trial' or a preceding state).
    *   "(a/p" (likely indicating 'alpha/beta' or a similar frequency band).
*   **Internal Markers:** The small orange/red circles within the nodes likely serve as markers or identifiers for specific components (e.g., Component 1, Component 2, etc.).

### 4. Data Trends & Details
As this is a schematic diagram and not a plot, there are no axes or quantitative data trends visible in the snippet. The visual emphasis is on the *direction* and *sequence* of the components, as indicated by the arrows.

### 5. Contextual Caption Integration
The caption provides crucial context:
*   **Figure 7:** The overall figure concerns the "Evaluation of Functional Correlations between Activity Components within and across Trials."
*   **Panel (A) Context:** The visible schematic aligns with the description of Panel (A), which illustrates "the functional correlations between the components within a trial in different trial types."
*   **Arrow Interpretation:** The caption explicitly states: "The direction of each arrow indicates the temporal order of the components, **not their functional causality**." This confirms that the green arrows represent a sequence in time.
*   **Correlation Representation:** The caption notes that "Each black line indicates a significant correlation (p < 0.05), and the corresponding correlation coefficient is labeled and represented by its thickness." While the snippet shows thick green arrows, this confirms that line thickness is used to represent correlation strength.

1260
Neuron 100, 1252–1266, December 5, 2018


---

## Page 11

xYjxY in Full-global and No-global). On the other hand, if the
global prediction was only partially established, where the
higher-level prediction errors also appear in Late trials, the signif-
icant difference should primarily reﬂect the higher-level predic-
tions (compare xYjxY in Partial-global and No-global). Since the
higher-level prediction error should appear in the g band and
no signiﬁcant g-band responses were observed (Figure 8B),
we concluded that, during the emergence of the rule in the ﬁrst
20 trials of a block, brain activity was dominated by the establish-
ment of a partial prediction for the global regularity.

We further performed a similar comparison between the ﬁrst 3
xxxxY trials after the 20 repetitions (around trials 21–23, xxxxx
trials were skipped) and the 3 xxxxY trials after a comparable
20-trial period (around trials 38–40, xxxxx trials were skipped).
Most of the prediction signals identiﬁed in the ﬁrst 20 trials was
not found in the following 20 trials (Figure S8). This indicated
that the identiﬁed prediction signals were not an artifact of drift
in neural activity, and the learning of global regularity occurred
primarily during the ﬁrst 20 repetitions. Furthermore, it is worth
noting that our task only required the subjects to passively listen
to the stimuli and thus provided no behavioral assessment for
this internal learning process.

DISCUSSION

To evaluate the hierarchical predictive-coding model during the
local-global paradigm, we used a data-driven approach to extract
emergent network components in cortical activity and cortico-
cortical connectivity, which were further tested by hypothesis-
driven analyses. Our ﬁndings revealed the presence of three
distinct cortical processing stages for auditory novelty and deter-
mined their functional correlations and hierarchy (summarized in
Figure 7C). Based on our results, we proposed that prediction-
error signals are transmitted in the g frequency band, where the
local-levelprediction-errorsignalissentfromearlyauditorycortex
to the anterior temporal cortex, and the global-level prediction-
error signal is sent from the anterior temporal cortex to PFC. On
the other hand, the local- and global-level prediction signals are
transmitted in the a/b band, between the same corresponding
areas but in the opposite directions. Furthermore, if a local-level
prediction error is not fully cancelled out by the global-level pre-
diction, then a prediction-update signal is triggered in the a/b
band and broadcasted from PFC back to the anterior temporal
cortex and early auditory cortex, which are the target areas of
the global- and local-level prediction signals, respectively.

A



**1. Overall Layout & Structure:**
The figure is a single, large illustration depicting a lateral view of a cerebral hemisphere (a cortical surface map). The structure is drawn as an outline representing the brain's gyri and sulci, divided into distinct regions by faint lines. The overall style is a simplified anatomical map overlaid with numbered markers.

**2. Visual Components & Symbols:**
*   **Cortical Outline:** The main structure is a gray, continuous line forming the boundary of the cortex. Internal lines delineate major sulci and gyral boundaries.
*   **Nodes/Markers:** Several small, dark, filled circles (nodes) are placed across the cortical surface. These nodes are annotated with numbers.
*   **Spatial Distribution:** The nodes are distributed across the visible surface, clustered in different areas.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Subject 1" at the top center.
*   **Numbered Nodes:** The following numbered nodes are visible on the map: 1, 2, 3, 4, 9, 10, 14, 15, 22, 23, 96, and 97.

**4. Data Trends & Details:**
Since this is a static anatomical map rather than a plot, there are no axes or data trends to describe. The nodes represent discrete locations on the cortex for Subject 1.

**5. Contextual Caption Integration:**
No specific caption text was provided to integrate, so the description relies solely on the visual elements present in the image. The nodes (e.g., 1, 2, 4, 97) represent specific points of interest on the cortical surface for Subject 1.



This figure presents a lateral view schematic map of the cerebral cortex for "Subject 2." The visualization is a simplified, outline drawing representing the gyri and sulci of the brain surface.

**1. Overall Layout & Structure:**
The figure consists of a single, large anatomical illustration depicting the lateral surface of a brain hemisphere. The representation is schematic rather than photorealistic, showing major cortical folds (gyri and sulci) as continuous lines defining the surface contours.

**2. Visual Components & Symbols:**
The primary components are the cortical outline and a set of numbered markers placed directly onto this surface.

*   **Cortical Outline:** The brain outline is drawn in black lines, showing the general curvature and major divisions of the cortex.
*   **Markers (Nodes):** There are several small, solid black circles scattered across the cortical surface. These markers are labeled with numerical identifiers (1 through 56).
*   **Spatial Distribution:** The markers are not uniformly distributed. A cluster of high-numbered points (10, 11, 13, 14, 17, 18, 19) is concentrated towards the anterior/superior aspect of the visible cortex. Other points (e.g., 2, 3, 4, 9) are located near this cluster, while points like 56 are situated more posteriorly/inferiorly.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Subject 2" at the top center.
*   **Numerical Labels:** The most prominent labels are the numbers associated with the black markers: 1, 2, 3, 4, 9, 10, 11, 13, 14, 17, 18, 19, and 56. These numbers serve as identifiers for specific locations on the cortex.

**4. Data Trends & Details:**
As this is a static anatomical map and not a plot, there are no axes or data trends to describe. The distribution of the numbered markers indicates specific sampling locations across the cortical surface for Subject 2.

**5. Contextual Caption Integration:**
The figure serves as a topographical map, using the numbered markers (1-56) to denote specific points of interest or recording sites on the cortex of Subject 2. The clustering of markers in certain regions suggests localized areas of interest or high density of data collection for this subject.

B

Figure 8. Emergence of Global Prediction Signals within the First 20 Trials of a Block
(A) Channels with a signiﬁcant difference in TFRs between Early and Late trials (Late – Early) are shown with large black circles with the channel numbers labeled.
Non-signiﬁcant channels are indicated by small gray dots.
(B) Time-frequency representations of the identiﬁed signiﬁcant differences. Each panel represents a signiﬁcant channel shown in (A) (the channel number is
shown). Same format as Figure 3. Axis labels and color bar are shown in the lower-left corner.

Neuron 100, 1252–1266, December 5, 2018
1261


---

## Page 12

Signiﬁcance of the Hierarchical Structure
According to the hierarchical predictive-coding framework (Fris-
ton, 2005), higher levels of the cortical hierarchy predict the error
residual from the lower level rather than the sensory data itself.
Another possible model is a predictive but not hierarchical
design, where one top-down process predicts the local regular-
ity, as in the hierarchical model, and the other process directly
predicts the global regularity in the input sequence. According
to this alternative non-hierarchical model, the top-down process
should directly predict the ﬁfth tone x in xxxxx block and the ﬁfth
tone Y in xxxxY block; therefore, the novelty response in xxxxx
block (xYjxx – xxjxx) should be equivalent to the novelty response
in xxxxY block (xxjxY – xYjxY). However, this is disproved by our
results, which showed that xYjxx – xxjxx (the unpredicted local
novelty response) and xxjxY – xYjxY (the negative of the pre-
dicted local novelty response) contained different components
and were always different. The key advantage of having hierar-
chies in a bidirectional structure is to allow information related
to regularities at different spatial and temporal scales to merge
into a coherent unity, because each hypothesis about the hidden
causes of sensory inputs is called upon only if the sensory data
cannot be explained at a lower level; such a hierarchical organi-
zation may therefore result in an internally consistent model of
the causal structure of the sensory world (Clark, 2013; Fris-
ton, 2010).

Dissecting Complex Multi-Dimensional Brain
Responses
Neurophysiological responses can be dissected into at least
four dimensions: anatomical site, temporal dynamics, fre-
quency selectivity, and stimulus responsivity. Here, we show
how a comprehensive description of such complex brain re-
sponses, indexing neural processes that are multi-dimensional,
simultaneous, and interdependent, can be achieved by using
the PARAFAC method of tensor decomposition. PARAFAC is
one of several methods to decompose a multi-dimensional
data into a set of latent components that can describe the
data in a more condensed form. Other commonly used
methods are the Tucker3 method (Kroonenberg, 1983) and sim-
ply unfolding of the multi-dimensional data to a 2D matrix and
then performing standard two-way methods such as PCA.
Among these methods, PARAFAC uses fewer degrees of
freedom to model the data (Kiers, 1991) and does not require
matrix unfolding, which will mix up the variables and destroy
their interactions (Harshman and Lundy, 1994). Those features
make PARAFAC simpler, more robust, and ideal to extract
latent patterns in the data for easier interpretation. PARAFAC
has proved to be a powerful analytical tool for electroencepha-
lography (EEG) (Miwakeichi et al., 2004; Mørup et al., 2006),
ECoG (Chao et al., 2015; Yanagawa et al., 2013), and fMRI
(Beckmann and Smith, 2005) and is well suited to dissect brain
responses that consist of multiple superimposed network
dynamics (Chao et al., 2015, 2018).

Brain Areas Associated with Local and Global Novelty
Our result shows that lower- and higher-order auditory predic-
tion errors are represented in the temporal and frontal cortices,
respectively. This is consistent with previous evidence from

both monkey and human studies using the local-global paradigm
or its variations. Human studies with ECoG, EEG, MEG, and fMRI
show that local error signals are conﬁned to the primary auditory
cortex, while global error signals propagate to distributed areas
in the frontal cortex (Bekinschtein et al., 2009; Chennu et al.,
2013; El Karoui et al., 2014; Wacongne et al., 2011). Similar re-
sults have been found in monkeys, where fMRI responses to
local and global violations are identiﬁed in the auditory cortex
and a distributed frontoparietal network, respectively (Uhrig
et al., 2014). In the framework of predictive coding, temporal cor-
tex has been suggested to be involved in the learning and storing
of transition probabilities, which sufﬁce to detect local deviants
(Wacongne et al., 2011). Frontal cortex, on the other hand, was
found to encode more global and abstract properties of the
entire sequence, including numerical patterns (‘‘there should
be 5 items’’) and sequential patterns (‘‘the last item should be
different’’) in both monkeys and humans (Wang et al., 2015),
compatible with its present activation to global deviants.

In our study, the higher-order error and update signals were
found primarily in the frontopolar PFC (area 10) and DLPFC.
Among prefrontal areas in macaque monkeys, the frontopolar
area 10 has the densest interconnection with auditory associa-
tion areas: it receives information from nearly all levels of auditory
processing in the superior temporal gyrus, from the early sensory
processing in the belt and parabelt areas to the higher-order pro-
cessing of conspeciﬁc communication in the temporal polar
areas (Medalla and Barbas, 2014; Romanski and Averbeck,
2009) and is also the main source of connections back to auditory
cortices (Barbas et al., 2005). Functionally, both the frontopolar
area 10 and DLPFC are important for working memory (Curtis
and D’Esposito, 2003; Gilbert et al., 2006). The present results
suggest that those brain structures generate and hold an internal
representation of the entire sequence of stimuli, sufﬁcient to
generate error signals when an unexpected sequence is heard.

The ventrolateral PFC (VLPFC) is another key area for process-
ing
auditory
sequences,
particularly
those
with
higher
complexity (Wilson et al., 2017). Previous studies with the
local-global paradigm have shown that global novelty responses
can be found in VLPFC in both monkeys and humans (Uhrig
et al., 2014; Wang et al., 2015). In agreement with those ﬁndings,
our univariate analysis identiﬁed several electrodes in VLPFC
in subject 1 that showed late g-band power increases and
b-band power decreases in the global novelty response (Fig-
ure 4A), although the responses were smaller than those in the
frontopolar area 10 and DLPFC (Figure 5A). In subject 2, unfortu-
nately, the role of VLPFC could not be evaluated since electrode
placement failed to cover the area (Figure 1B). In contrast to the
frontopolar cortex and DLPFC, which showed signals associ-
ated with both the global prediction (Figure 8) and its updates,
VLPFC was only found involved in the update process. This sug-
gested a distinctive modulatory role of VLPFC in auditory
sequence encoding and storage. Further research, using record-
ings speciﬁcally focused on this region and using a greater
variety of auditory sequences will be needed to evaluate the hy-
pothesis that inferior frontal cortex acts as a conserved
sequence processor in humans and monkeys (Wilson et al.,
2017), and the possibility that its representational scheme has
expanded in human evolution (Dehaene et al., 2015).

1262
Neuron 100, 1252–1266, December 5, 2018


---

## Page 13

Brain Signals and Areas Associated with Global
Prediction
Analysis of the evolution of brain signals during the ﬁrst 20 trials in
a block showed how the partial global prediction signals built up
during the repetitions of xxxxY. Using this approach, we found
that global prediction signals appeared as early as the end of
the ﬁrst tone in the sequence (Figure 8B). This result suggests
that global prediction is not based on a static pattern of neural
activity that would be maintained throughout the xxxxY block,
but on a dynamic, trial-speciﬁc signal. Global prediction signals
could have been launched by an attention engagement triggered
by the ﬁxation onset, which occurred 200–300 ms before the ﬁrst
tone (see STAR Methods and Figure 1A). Alternatively, global pre-
diction signals could have been directly triggered by the ﬁrst tone,
suggesting the existence of another bottom-up pathway that
launched the global prediction from the onset of a sensory
sequence.

Global prediction signals were found primarily in PFC and the
premotor cortex (Figure 8A). Among those areas, DLPFC and
the frontopolar area 10 were also involved in the processing of
higher-order errors and prediction updates (Figures 5A and 6B).
This ﬁnding suggests that PFC was thecore structure maintaining
an internal representation of the entire xxxxY sequence and could
receive global-level prediction-error signals from the lower hier-
archy and send prediction-update signals to the lower hierar-
chies when the global deviant occurred (xxxxx). On the other
hand, the premotor cortex was found to be activated in humans
during the monitoring of auditory violations in a serial prediction
task (Schubotz et al., 2003), predicting musical rhythms (Chen
et al., 2008; Chen et al., 2006; Zatorre et al., 2007), and speech
perception (Meister et al., 2007; Pulverm€uller and Fadiga,
2010). The identiﬁed involvement of the premotor cortex sup-
ports the view that sound and action are often intrinsically linked
(the sounds we hear reﬂect actions, and the sounds we make
result from actions), and that motor signals are therefore involved
in the prediction of sensory events (Lima et al., 2016; Morillon and
Baillet, 2017; Schubotz, 2007).

Gamma and Alpha/Beta Oscillations in Predictive
Coding
Neural oscillations are thought to be a means for neuronal pop-
ulations to communicate within and between cortical areas,
where
different
frequency
channels
are
associated
with
different types of neural computations (Fries, 2005). This notion
is supported by recent studies of the human and primate cor-
tex, which have shown that feedforward and feedback hierar-
chical communication between cortical areas are exerted
through by g- and a/b-band oscillations, respectively, in both
vision (Bastos et al., 2015b; Michalareas et al., 2016; van Ker-
koerle et al., 2014) and audition (D€urschmid et al., 2016; Fonto-
lan et al., 2014; Sedley et al., 2016). In the present study, we
examined this view in the context of predictive coding and
demonstrated that ascending information about prediction er-
rors and descending information about predictions and predic-
tion updates were indeed processed in the g and a/b frequency
bands, respectively. This ﬁnding suggests the signiﬁcance of
directional frequency-speciﬁc multiplexing in cortical informa-
tion processing.

Numerous human ECoG and MEG studies have demonstrated
the correlation between prediction errors and the magnitude of
g-band oscillations in audition (D€urschmid et al., 2016; Edwards
et al., 2005; Todorovic et al., 2011), vision (Brodski et al., 2015),
and audiovisual interactions (Arnal et al., 2011). To further
examine the hierarchical structure in prediction errors, a human
ECoG study with the local-global paradigm shows that local nov-
elty evokes early high-g responses (60120 Hz) in the temporal
cortex, whereas global novelty induces a sustained decrease in
the b-band power (13–25 Hz) within the frontal lobe (El Karoui
et al., 2014). With the same paradigm, we obtained similar results
in monkeys. However, we found that prediction errors at the local
and global levels are both represented in the g oscillations, but
with slightly different frequency proﬁles (Figure S4). This ‘‘fre-
quency ordering’’ suggests that bottom-up error signals could
be carried by slightly different frequency channels depending
on their level in the hierarchy. Furthermore, we found that the
b-power decrease in the global novelty response is not associ-
ated with prediction errors, but with a top-down prediction
update.

Although their role in top-down versus bottom-up signaling is
well established (Bastos et al., 2015b; Michalareas et al., 2016),
evidence linking a/b-band responses to prediction signals is
limited (Arnal and Giraud, 2012). A recent human ECoG study,
using a semi-predictable sequence of sounds to force the sub-
jects to continuously update their predictions, provided the ﬁrst
direct evidence that b-band oscillations are involved in updating
the content of sensory predictions (Sedley et al., 2016). Our
results concur and further show that prediction updates are
linked to a b-power decrease, which suggests that b-band oscil-
lations are associated with the maintenance of predictions, and
thus need to be removed or reduced when updates are required.

Limitations and Further Tests of the Theory
Here, we propose several future directions that could help further
verify the predictive-coding theory, particularly at the meso-
scopic level. One limitation of the present experiment is that it
could not fully isolate the prediction signals, since predictions
and prediction errors were always intertwined. Global prediction
signals could only be identiﬁed by their change during the ﬁrst 20
trials of a block. In the future, a more direct approach would be to
systematically manipulate the local and global prediction
strengths (see discussion below). Another useful strategy would
be to probe the network response with omission trials (e.g.,
4-tone sequence xxxx) (Wacongne et al., 2011), which could pro-
vide crucial information about the spontaneous timing of the pre-
diction signals when no external stimuli are presented and allow
us to examine the possible difference between an omitted error
(e.g., PE1x) and an unpredicted error (e.g., PE1Y).

Another limitation is that our analysis only explored the func-
tional correlation between prediction-error and prediction-
update signals and thus cannot fully evaluate the causal links
between the underlying processes. One analytical approach to
further probe the relations between prediction and prediction-er-
ror signals across hierarchies would be to model the data with dy-
namic causal modeling (DCM) (Friston et al., 2003). DCM is a
method designed to make and estimate inferences about the
coupling among brain areas, which has been implemented to

Neuron 100, 1252–1266, December 5, 2018
1263


---

## Page 14

reveal possible canonical circuits in the context of predictive cod-
ing (Auksztulewicz and Friston, 2015; Bastos et al., 2015a; Brown
and Friston, 2012). A more direct experimental approach would
be to systematically controls local- and global-level prediction
strengths by independently manipulating sequence length and
sequence frequency. Furthermore, prediction strengths could
be altered in a seamless manner using probabilistic rather than
deterministic rules (Sedley et al., 2016). This would allow to
examine how predictions and prediction errors are dynamically
coupled, and to monitor how predictions at different hierarchies
are established and altered by the sensory inputs.

Finally, to probe the proposed hierarchical cortical organiza-
tion, additional experiments could vary the complexity of the reg-
ularities at larger temporal scales, using as a guideline the
recently proposed hierarchy of sequence knowledge (Dehaene
et al., 2015). More complex rules could, however, become signif-
icantly more difﬁcult to detect. Other alternatives are using
speech stimuli that introduce multi-level syntactic structures, vi-
sual stimuli in which hierarchical features can be more easily
deﬁned according to both their sequential and spatial conﬁgura-
tions, or multi-modal audiovisual stimuli. Last but not least, in
future work, the information content carried by the prediction
signals should be assessed, for instance, by taking advantage
of electrophysiological or optical methods for multiple single-
unit recordings. To further understand predictive coding in the
brain, it will be essential to decode the neural representations
of predictions across hierarchies, which collectively could reveal
how the brain encodes its internal models of the world.

In summary, our ﬁndings support the hierarchical predictive-
coding theory by providing a high-resolution dynamic descrip-
tion of how prediction and prediction-error signals at different
hierarchies interact with each other over distinct cortical areas
and frequency bands. The combination of large-scale neuronal
recordings with data-driven and hypothesis-driven analyses al-
lows a systematic exploration of mesoscopic cortical dynamics,
which provides potential target brain areas and communication
channels for future mechanistic study of predictive coding,
particularly, the study on how prediction and prediction-error
signals are created at the cellular level and how they causally
interact in microcircuits.

STAR+METHODS

Detailed methods are provided in the online version of this paper
and include the following:

d KEY RESOURCES TABLE

d CONTACT FOR REAGENT AND RESOURCE SHARING

d EXPERIMENTAL MODEL AND SUBJECT DETAILS

B Subjects and experimental setup

B Electrode implant

B Stimulus design and experimental protocol

B Data analysis

SUPPLEMENTAL INFORMATION

Supplemental Information includes eight ﬁgures and two tables and can be
found with this article online at https://doi.org/10.1016/j.neuron.2018.10.004.

ACKNOWLEDGMENTS

We thank Naomi Hasegawa and Tomonori Notoya for providing veterinary care
and technical support. This work was supported by the Brain Science Project
of the Center for Novel Science Initiatives (CNSI), National institute of Natural
Science (NINS; Grant Number BS261006), and Ministry of Education, Culture,
Sports, Science, and Technology Grant in Aid for Scientiﬁc Research on Inno-
vative Areas (21118002). S.D. was supported by Inserm, CEA, Colle` ge de
France, the Canadian Institute for Advanced Research (CIFAR), and the Euro-
pean Research Council (ERC).

AUTHOR CONTRIBUTIONS

Conceptualization, S.D. and Z.C.C.; Methodology, Z.C.C., S.D., L.W., and
K.T.; Formal Analysis, Z.C.C.; Investigation, K.T. and Z.C.C.; Resources,
N.F.; Writing – Original Draft, Z.C.C.; Writing – Review & Editing, Z.C.C.,
S.D., and K.T.; Visualization, Z.C.C.; Funding Acquisition, N.F. and S.D.

DECLARATION OF INTERESTS

The authors declare no competing interests.

Received: May 4, 2018
Revised: August 29, 2018
Accepted: October 2, 2018
Published: October 25, 2018