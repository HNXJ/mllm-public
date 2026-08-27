## 

Hierarchical substrates of prediction in visual 
cortical spiking

Jacob A. Westerberg1,2,†, Yihan S. Xiong1,†, Eli Sennesh1, Hamed Nejat1, David Ricci1, Séverine 
Durand3, Ben Hardcastle3, Hannah Cabasco3, Hannah Belski3, Ahad Bawany3, Ryan Gillis3, Henry 
Loeffler3, Carter R. Peene3, Warren Han3, Katrina Nguyen3, Vivian Ha3, Tye Johnson3, Conor Grasso3, 
Ahrial Young3, Jackie Swapp3, Ben Ouellette3, Shiella Caldejon3, Ali Williford3, Peter A. Groblewski3, 
Shawn R. Olsen3, Carly Kiselycznyk3, Christof Koch3, Jerome A. Lecoq3, Alexander Maier1, and André 
M. Bastos1,*

1Department of Psychology, Vanderbilt Brain Institute, Vanderbilt Vision Research Center, Vanderbilt University, Nashville, US 
2Department of Vision and Cognition, Netherlands Institute for Neuroscience, Royal Netherlands Academy of Arts and Sciences, 
Amsterdam, The Netherlands 
3Allen Institute for Neural Dynamics, Seattle, US 
*Corresponding author. Email: andre.bastos@vanderbilt.edu  
†These authors contributed equally to this work

Predictive processing models have recently flourished in neuroscience1-9. Feedforward and feedback modulation are at the 
heart of these hierarchical predictive processing models. Previous experimental studies using fMRI, EEG/MEG, and 
LFP1,10,11 could not reliably resolve feedback modulation from local computations and feedforward outputs. Here, using 
open-science9, multi-species, multi-area, high-density12, laminar neurophysiology13, we empirically test whether 
predictive processing is a key component shaping sensation. To isolate sensory information processing and eliminate 
motor/reward confounders1,10,11, we use a no-report task. Our task leveraged so-called global oddballs (GO) as 
unpredictable, deviant stimuli that circumvent low-level adaptation. We examined their responses relative to local 
oddballs (LO) that we habituated into highly predictable priors. Four surprising findings in this dataset challenge many 
existing predictive processing models. First, passively evoked GO responses were exclusive to higher-order, more 
cognitive areas rather than early-to-mid sensory cortex. Second, interneuron-targeted optogenetics revealed no evidence 
for a subtractive mechanism in both primates and mice. Third, highly predictable LO responses dominated in over 50% of 
all neurons, including in higher-order cortex which should have anticipated them, indicating limited evidence for 
predictive suppression. Lastly, prediction errors followed a feedback, rather than a feedforward signature. These results 
reveal circuit dynamics that govern the shaping of sensory processing by prediction, which will motivate new, neurally-
constrained predictive processing models.   
Introduction  
Predictive Processing (PP) models state that brains have 
evolved to model the sensory statistical regularities in the 
world2,14,15. Deviations from these internal predictions are 
neuronally signaled with prediction error responses16. These 
models (see Extended Data Table 1 and Extended Data Fig. 
1) make specific hypotheses about the neuronal circuitry that 
implements prediction and prediction error computations.

Sequence-based oddball paradigms have been widely used 
to test PP models1. Subjects are exposed to a repeated pattern 
of sensory inputs to implicitly learn the statistical 
regularities of hidden rules governing the sensory inputs. 
Violations to the rule are used to test for neuronal signaling 
of prediction errors. Studies of brain activity during oddball 
tasks using fMRI, MEG/EEG, and LFP have been largely 
consistent with PP models1,10,11,13,17-21 and have documented 
neuronal signatures of prediction errors both in higher-order 
areas (e.g., prefrontal cortex) as well as sensory areas, 
including primary and secondary auditory and visual 
cortex13. However, because these neuronal recording 
techniques cannot resolve feedback modulation from local

computations and feedforward output22, they could not test 
key hypotheses made by the PP models.  
In this work we test three of the main hypotheses made by 
PP models. The first hypothesis is that predictions are 
generated in higher-order areas of the brain and feed back to 
lower-order areas, where they are compared with and 
subtracted from sensory inputs (Fig. 1, Hypothesis 1). In the 
second hypothesis, prediction errors are hypothesized to 
flow in the opposite direction. They feed forward up the 
hierarchy to update internal models to make better 
predictions (Fig. 1, Hypothesis 2). The subtractive feedback 
predictions are thought to be implemented via the activity of 
local inhibitory interneurons2,4,23 (Fig. 1, Hypothesis 1). 
Predictable stimuli are uninformative, so they are 
hypothesized to drive less overall neuronal activity to save 
energy3. By contrast, surprising/unpredictable stimuli evoke 
prediction errors which enhance neuronal activity. In the 
third hypothesis, PP models stated that brains construct 
complex models that are compared to sensory inputs at 
multiple levels of cortical processing (Fig. 1, Hypothesis 3). 
Computational instantiations of PP models have proposed

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

---

## 

prediction error computations to occur both in early sensory 
as well as higher-order levels of neuronal circuits, even for 
high-level predictions11,24,25.

So far, studies of spiking activity have been more equivocal, 
with different results depending on species, paradigm, 
cortical area, and methodology4,13,21,26-30. Importantly, no 
study has yet used large-scale high-density neuronal 
electrophysiological 
recording 
methods 
in 
multiple 
connected brain regions to test PP models. Brain recordings 
with this level of detail are necessary to experimentally test 
PP because these models make use of multiple stages of 
cortical processing, with distinct cell types, cortical layers, 
areas, and directions of feedforward/feedback processing 
contributing to the hypothesized computations.  
We tested the above hypotheses regarding PP using Multi-
Area, high-Density, Laminar-resolved Neurophysiology 
(MaDeLaNe) recordings of thousands of spiking neurons in 
mice and monkeys throughout the visual cortex (areas V1, 
LM, RL, AL, PM, AM in mice and areas V1, V2, V3, V4, 
MT, MST in monkeys) and prefrontal cortex (areas 8A and

lateral PFC in monkeys). We used a habituation-based no-
report variation21,31 of the global-local oddball task1, thereby 
avoiding motor and reward related confounds on sensory 
responses. This paradigm allowed us to disentangle short-
term stimulus repetition from prediction. We found four 
surprising findings which challenge many aspects of current 
PP models (Extended Data Table 1, Extended Data Fig. 1). 
First, global oddballs evoked neuronal spiking responses 
consistent with a prediction error signal, but these responses 
were restricted to higher-order cortical areas in both species. 
Second, we used cell-type specific optogenetics in both 
species to observe whether inhibitory interneurons 
performed predictive inhibition as proposed. Global 
oddballs did not modulate the inhibitory interneuron 
populations we studied. Third, highly expected local 
oddballs did not evoke a reduced neuronal response 
compared to the same sequence when it was contextually 
deviant. Fourth, global oddballs evoked a laminar- and area-
wise pattern of activity more consistent with feedback, 
rather than feedforward processing.

Fig. 1 | Predictive Processing (PP) hypotheses, Local/global oddball paradigm, and experimental setup.  a, Schematic for sensory processing via 
hierarchical predictive processing. Stimulus information enters the cortical hierarchy through layer 4, and prediction error is computed in superficial 
layers 2/3, with inhibitory cell involvement in the subtractive process (H1). Prediction error is then fed forward (H2) via superficial layers to higher-
order areas. Higher-order areas provide a feedback prediction from deep layers. Error signals emerge early and propagate throughout cortical 
hierarchy (H3) b, Visual stimuli were presented in 4-stimulus sequences consisting of 2-oriented, drifting gratings symbolized as 'x' or 'y'. Animals 
were habituated to the x-x-x-y sequence (counterbalanced over sessions/animals with y-y-y-x). In the main block of a recording session, animals were 
presented with 80% x-x-x-y and 20% x-x-x-x (global oddballs). Control blocks consisted of x-x-x-x (control for global oddball, 50% of trials) and y-
y-y-y (control for local oddball, 50% of trials). c, Neuropixels were introduced into 6 visual cortical regions in all mice (V1, LM, RL, AL, PM, AM). 
128-channel or 32-channel laminar probes were introduced into 8 cortical regions in 2 monkeys (V1, V2, V3, V4, MT, MST, 8A, PFC).  d, Monkeys 
viewed sequences of drifting grating stimuli while fixating centrally. Mice viewed sequences of full-screen drifting grating stimuli. Trace shows 
example population average response to the 4-stimulus sequences with the GO in red and the LO in green.

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

This figure is divided into four main panels: **a**, **b**, **c**, and **d**.

## 

Isolating sensation and establishing priors

We first extensively habituated animals to the local oddball 
x-x-x-y stimulus sequence for 2000-3000 trials over several 
days (Fig. 1b and Extended Data Fig. 2). The "x" and "y" 
stimuli within a sequence denote drifting gratings at 135° or 
45° from horizontal and were counterbalanced across 
animals. The unpredictable global oddball x-x-x-x stimulus 
sequence was never presented during habituation and 
introduced only on neural recording sessions (Fig. 1c), on 
20% of trials in the main block (Fig. 1b). This long 
habituation period ensured that animals could learn to 
predict the x-x-x-y (local oddball) stimulus sequence. 
Pupillary responses suggested that animals recognized the 
violation of this sequence during unpredicted x-x-x-x global 
oddballs (Extended Data Fig. 3).  
To investigate the neuronal signaling underlying these 
predictions, we compared responses in the main block to a 
control block where the x-x-x-x sequence alternated with y-
y-y-y and thus the sequence was predictable after the first 
stimulus (Fig. 1b). To analyze global and local oddballs, we 
compared spiking responses to the fourth component in the 
sequence (P4) to the same stimulus in the same sequence 
position of the control block (vertical dotted lines in Fig. 1b). 
To account for cross-session firing rate drift which occurs 
even in well-isolated single units32, we normalized responses 
to the third component in the sequence (P3). Our main 
contrast was therefore P4-P3 in the main block vs. P4-P3 in 
the control block. For global oddballs, this contrast should 
reveal prediction errors while controlling for short-term 
adaptation. For local oddballs, this contrast should reveal the 
release of adaptation caused by changing the stimulus after 
a few repetitions. Neurons responded to these sequences 
with robust firing rate increases in all recorded areas (Fig. 
1d, Extended Data Fig. 4, 5). Significant oddball detection 
was determined by comparing the neuronal spiking response 
for each oddball type using a nonparametric, cluster-based 
permutation test33 (at P < 0.05, corrected for multiple 
comparisons, see Methods).

Predictable local oddballs are widely signaled 
Because of extensive habituation, local oddballs were non-
surprising stimuli and, according to multiple PP models, 
should be suppressed and explained away (H1). However, 
we observed that neuronal signaling of local oddballs was 
ubiquitous (present in all areas and both species, Fig. 2a), 
signaled early and fed forward up the visual cortical 
hierarchy (within the first ~150 ms of stimulus processing, 
Fig. 2b), strong (local oddball responses by area were on 
average 60-98% above the control stimulus in mice, and 
43%-93% in monkeys, Fig. 2c),  and involved more than 
50% of all recorded neurons (median across areas in mice: 
51%, median across areas in monkeys: 65%, Fig 2d). In mice 
but not monkeys, local oddball signaling gradually increased 
in strength with ascending cortical hierarchy (Linear

correlation between local oddball response and hierarchical 
area, R2 = 0.83, P=5.75e-5, Fig. 2c, left subpanel). In 
monkeys, the local oddball response was strongest in area 
MT (ANOVA, p<0.001, Fig. 2c, right subpanel). In V1 of 
both species, local oddball signaling was most prominent 
amongst neurons in L2/3 neurons (Fig. 2e; for details on 
layer identification, see Methods and Extended Data Fig. 6).  
Can these local oddball responses, representing local signal 
change, be considered a simple form of prediction error 
signaling? To examine this, we compared the local oddballs 
in contexts that differed in their relative probability (local 
oddball sequence probability varied between 100%, 80%, 
and 12.5%, see Extended Data Fig. 2). If they represent 
prediction errors, local oddball responses should scale 
according to their deviance (H1). We found that local 
oddball signaling did not scale as a function of deviance in 
most areas (Extended Data Fig. 7, area V4 was an 
exception). Instead, we observed the opposite pattern just as 
often, and most prominently in V1 of mice (Extended Data 
Fig. 7b). The enhanced neuronal responses to more 
predictable local oddballs in mouse V1 may have been 
caused by learning-driven potentiation34. To summarize, 
local oddball sequences (x-x-x-y) release most neurons from 
adaptation and increase excitability independent of 
prediction, even though animals had been exposed to these 
sequences thousands of times. 
Unpredictable 
global 
oddballs 
do 
not 
generate 
feedforward prediction error  
Next, we tested whether highly surprising global oddballs 
(x-x-x-x) drive neuronal spiking consistent with prediction 
error signaling. We found that global oddball signaling was 
restricted to only a few higher-order brain areas (LM, AM, 
and PM in mice; V3, MT, 8A, and PFC in monkeys, Fig. 
3a). At the individual neuron level, although we identified a 
handful of neurons/areas that responded to global oddballs 
(Extended Data Fig. 4, 5), the percentage of units signaling 
global oddballs in each area was sparse (median across areas 
in mice: 7%, median across areas in monkeys: 8%, Fig. 3b), 
contradicting H3. Unlike local oddballs, which showed a 
clear temporal progression of latencies across the hierarchy 
(Fig. 2c), the latency at which neurons signaled global 
oddballs did not scale with hierarchy (Fig. 3c).  
We next examined global oddballs within L2/3 pyramidal 
neurons, which according to multiple PP models should 
transmit prediction error (H2). In mice, we found that 
putative layer 2/3 pyramidal cells did not signal global 
oddballs (Extended Data Fig. 8a). In addition, current source 
density analysis of synaptic activity in L2/3 of mice did not 
reveal any reliable changes in synaptic activation (Extended 
Data Fig. 9a, b) during global oddballs. In monkeys, L2/3 
spiking activity did not signal global oddballs in area V3 
(Extended Data Fig. 8b). There was L2/3 involvement in 
global oddballs in area MT, but this came 116 ms later than

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

---

## 

in area PFC, supporting a feedback35,36 rather than 
feedforward putative error computation (Extended Data Fig. 
8b).  
Without the hypothesized L2/3-specific signal, we 
investigated alternative sources for global oddball signaling. 
We limited the analysis to the areas with population global 
oddball signaling. We grouped areas into higher- and lower-
order (higher-order areas AM and PM vs. lower-order area

LM in mice; higher-order area PFC vs. lower-order areas V3 
and MT in monkeys). We first divided the units into granular 
(L4) vs. extragranular (L2/3 and L5/6) compartments, which 
anatomically separate feedforward vs. feedback input37. In 
mice, we observed global oddball signaling only in the 
extragranular (feedback-associated) layers and later in the 
lower-order cortex (401 ms post-stimulus, Fig. 3b, left 
subpanels) than in the higher-order cortex (337 ms post-
stimulus). In monkey visual areas V3 and MT, we observed

Fig. 2 | Predictable local oddball response is widespread, emerges early, and feeds forward. a, Local oddball detection across cortical areas in 
mice and monkeys. Bands are 95% confidence intervals across units in an area. Unit responses are normalized by dividing instantaneous firing rate 
by average firing rate at the single-unit level in mice and via a z-score method for the multiunit data in monkeys (see Methods). Green bands are the 
P4-P3 local oddball in the main block; gray bands are the P4-P3 local oddball in the control block. For non-subtracted neuronal activity, see 
Extended Data Fig. 4. Yellow highlights reflect significant population local oddball detection periods, P<0.05, corrected using nonparametric, 
cluster-based permutation tests. Local oddball signaling in mice was accompanied by a stimulus-induced temporal modulation corresponding to the 
drifting grating presentation rate of 4 Hz (upper subpanel). This oscillatory component was much less prominent in monkeys (lower subpanel). b, 
Average onset time for significant local oddball effect across hierarchy in mice and monkeys. Error bars indicate 2 SEM across units. Linear 
regression shows significant relationship between hierarchical position and onset timing (R2 = 0.83, P=0.006 in mice; R2 = 0.88, P= 0.004 in 
monkeys), indicating a feedforward progression. c, Percent response increase to local oddball across cortical areas in mice and monkeys. Error bars 
indicate 2 SEM across units. Local oddball effects show significant feedforward enhancement in mice along the cortical hierarchy. d, Percentage of 
local oddball encoding units along cortical hierarchy in mice and monkeys. Signaling of predictable local oddballs is robust (>50% of all cortical 
areas) and widespread (observed in all cortical areas) e, Local oddball responses are more pronounced in L2/3 in V1 in both mice and monkeys 
compared to units in other layers, suggesting feedforward signaling.

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

This figure is composed of three main panels (a, b, and c), presenting data related to the organization of cortical areas and the influence of stimulus predictability on neural responses.

## 

global oddball signaling only in the extragranular (feedback-
associated) layers (135 ms post-stimulus), later in time than 
the extragranular layers of higher-order area PFC (111 ms 
post-stimulus, Fig. 3b, right subpanels). These latency and 
laminar effects collectively support prediction error

propagation from higher to lower areas of the hierarchy, 
contradicting H2. 
Finally, we also analyzed whether global oddballs were 
more consistently signaled in the first few trials when they 
occurred early in the main block, when putative prediction

Fig. 3 | Unpredictable global oddball emerges in higher-order cortex and is fed back. a, Global oddball detection across cortical areas in mice 
and monkeys. Bands are 95% confidence intervals across units in an area. Red bands are P4-P3 in the GLO block; gray bands are P4-P3 in the 
control block. For non-subtracted neuronal activity, see Extended Data Fig. 4. Yellow highlights reflect periods of significant population global 
oddball detection, P<0.05, corrected for multiple comparisons using nonparametric, cluster-based permutation tests. b, Percentage of significant 
global oddball encoding units/channels along the cortical hierarchy in mice and monkey. c, Onset times of significance for global oddball effect 
along the cortical hierarchy in mice and monkeys. Linear regressions show no significant change along cortical hierarchy, suggesting no strong 
feedforward signaling of global oddball prediction error. d, Granular versus extra-granular global oddball detection in areas with significant 
population-level detection in mice and monkeys. Red bands are P4-P3 in the GLO block; gray bands are P4-P3 in the control block. Yellow 
highlights reflect periods of significant population global oddball detection in the layer grouping, with the latency indicated.

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

This figure is composed of three distinct panels: **a**, **b**, and **c**, presenting different types of data visualizations related to cortical hierarchy and GO (Global Oddball) processing.

---

## 

errors should be strongest. Although area V4 in monkeys 
and PM in mice exhibited a profile consistent with a putative 
prediction error signal, areas before or after them in the 
hierarchy did not (Extended Data Fig. 10), inconsistent with 
the hypothesized feedforward (H2) or ubiquitous (H3) 
prediction error signal.  
Directed connectivity of global oddballs does not indicate 
feedforward error propagation 
In multiple PP models, prediction errors are sent 
feedforward (Fig. 1a, H2). Hence, neurons earlier in the 
hierarchy should increase their drive onto neurons later in 
the hierarchy to signal prediction error. We tested this by 
computing Granger causality between spiking activity time 
courses. Granger causality tests whether neuronal activity in 
area A can statistically predict activity in area B above and 
beyond predictions made by activity in area B alone37. If so, 
then area A "Granger-causes" B. By comparing the A-to-B 
vs. the B-to-A directions of Granger causality38 where A is 
below B in the hierarchy, we tested whether local and global 
oddballs evoked feedforward processing. In mice, compared 
to pre-stimulus baseline (Extended Data Fig. 11a), the 
hierarchy became more feedforward-dominated in both

early (100-300 ms) and late (300-500 ms) periods of local 
oddball processing (Extended Data Fig. 11a, b; Wilcoxon 
rank sum test, P<0.01). This feedforward activity 
propagated from V1 to the highest levels of the visual 
hierarchy, area PM. In contrast, during global oddballs, there 
was no change in feedforward vs. feedback asymmetry 
compared to baseline (Extended Data Fig. 11b-d, Wilcoxon 
rank sum test of GC asymmetry values across mice vs. pre-
oddball baseline, all comparisons, P>0.01). To summarize, 
the latency, hierarchical areas of significant signaling, 
laminar, and Granger analyses collectively contradicted H2; 
namely, global oddballs did not drive feedforward 
processing. Instead, the data supported a feedback model for 
processing prediction errors evoked by global oddballs. 
Global oddballs: A release from predictive inhibition? 
In multiple PP models, predictions are hypothesized to 
subtract away predictable stimuli (H1), leaving sensory 
cortex less excited. We tested this by assessing whether 
predictions are neuronally instantiated by inhibitory 
interneuron activity. We used optogenetics to identify 
Somatostatin- (SST) and Parvalbumin- (PV) expressing 
interneurons in mice, and a viral vector tool that restricted

Fig. 4 | Optotagged inhibitory cells in mice and monkeys do not carry out hypothesized predictive coding functions. a, Optical stimulation 
with 40 Hz sinusoidal modulation of laser power. Tagged SST (magenta, n=215 neurons) and PV (cyan, n=262 neurons) responses are normalized 
by their average firing rate. In primates, an opsin targeting all GABAergic inhibitory cells was used; responses shown were computed as a weighted 
mean (green, n=21 neurons), where each cell is weighted by its modulation strength (average firing rate change from baseline, divided by the sum of 
baseline and laser-timed response). b, Relative proportion of each inhibitory interneuron type, which have synapses at largely different sites on 
pyramidal cells (schematized here), across areas and layers in mice (left and middle). Average waveform shape and spike width in primate data 
(right) are consistent with that of narrow-spiking interneurons. c, Population average spiking response to the oddball sequences for these inhibitory 
interneurons. P1 to P3 in black, local oddball P4 in green, and global oddball P4 in red. d, Lack of global oddball detection in SST and PV cell 
subpopulations in mice and in pan-inhibitory cell populations in monkeys. Bands are 95% confidence intervals across units. Top, the red band is P4-
P3 in the main block; the gray band is P4-P3 in the control block. For P3 and P4 before subtraction, see Extended Data Fig. 4B.

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

This figure, labeled "Fig. 4," presents a multi-part visualization detailing the activity of optotagged inhibitory cells in mice and monkeys, combining schematic diagrams, raster plots, and waveform traces.

## 

optogenetic expression to inhibitory interneurons in 
monkeys39 (Fig. 4a and Extended Data Fig. 12). In both 
species, we utilized Channelrhodopsin-2 to drive the 
inhibitory interneurons to fire during light stimulation (see 
Methods). In mice, PV+/SST+ units were identified across 
all recorded areas and in monkeys, inhibitory interneurons 
were identified in areas MT/MST, PFC, and 8A (Fig. 4b). In 
monkeys, opto-tagged neurons had on average narrow 
waveforms, additional confirmatory evidence40 that these 
opto-tagged neurons were inhibitory (Fig. 4b). In both 
species, these inhibitory cell populations responded to the 
stimulus sequence and increased their spike rates during P4 
of local oddballs (Fig. 4c). However, we did not observe a 
significant response to global oddballs at the population 
average of these subpopulations (Fig. 4d; for P3 and P4 
components see Extended Data Fig. 4b). This indicates a 
minor role, if any, for these inhibitory interneuron sub-
populations in signaling global oddballs, failing to support 
H1 and indicating a putative excitatory mechanism for 
feedback-driven GO modulation. 
Discussion 
To test the neuronal implementation of PP, we performed an 
extensive survey of cortical spiking in mice and monkeys 
observing predictable or unpredictable stimulus sequences. 
We used MaDeLaNe (Multi-Area, high-Density, Laminar 
Neurophysiology) recordings13 and optogenetics to isolate 
different cortical layers, areas, and neuron types previously 
hypothesized to play a role in PP2-4,41. We tested whether 
neuronal spiking responses could be described as prediction 
error signals resulting from a release from predictive 
suppression (H1), and that triggers feedforward processing 
(H2) with a ubiquitous signature (H3).  
PP models (Extended Data Table 1) have hypothesized that 
prediction errors constitute a core, feedforward cortical 
computation2-4,41. Our subjects were habituated to a 
particular sequence (x-x-x-y) for thousands of trials such 
that its violation (x-x-x-x) should drive robust spike 
signaling of prediction error. In PP, the habituated (and 
highly predictable) local oddballs (x-x-x-y) should be 
suppressed, driving less activity42. We found the exact 
opposite: spiking responses robustly signaled unsurprising 
local oddballs (engaging over 50% of all recorded neurons) 
but weakly signaled surprising global oddballs (engaging 
less than 10% of all recorded neurons). Local oddballs 
emerged early in the hierarchy at fast latencies in layers 2/3 
and fed forward up the cortical hierarchy (Fig. 5a). However, 
contradicting the interpretation of these signals as prediction 
errors, local oddball responses did not consistently scale 
with increased sequence deviance, and did not trigger a 
release 
of 
inhibition 
from 
inhibitory 
interneurons 
(contradicting H1). Therefore, local oddball detection is 
most likely a release from neuronal adaptation.

Multiple PP models hypothesized that L2/3 pyramidal 
neurons transmit feedforward prediction errors. Global 
oddballs, which should have triggered this hypothesized 
feedforward flow, emerged late in the sensory response and 
in higher-order areas first, then lower-order regions (Fig. 
5b). Putative excitatory pyramidal neurons in L2/3 (which 
project feedforward connections) and their associated 
current sinks did not signal global oddballs in mice and only 
signaled weakly in one area (monkey area MT) and later 
than in PFC. Instead, global oddballs were found to emerge 
at the population level in the non-granular, feedback-
recipient layers. Feedforward neuronal communication 
assessed by Granger causality amongst spiking neurons was 
not observed during global oddballs. Therefore, we failed to 
detect feedforward processing during global oddballs by 
four independent metrics: hierarchical area, temporal order, 
Granger 
causality, 
and 
laminar 
compartment 
of 
spiking/transmembrane current flow (Fig. 5b, contradicting 
H2). Further, global oddballs did not emerge because of a 
release of inhibition from PV/SST+ interneurons in mice or 
inhibitory interneurons in monkeys (contradicting H1). Our 
results speak against the proposed ubiquity of prediction 
error signaling in sensory cortex (contradicting H3).

Fig. 5 | Schematic of findings represented in the canonical 
cortical connections. a, highly predictable local oddball resulted in 
robust and widespread feedforward response. The timings of onset 
of significance as well as granger causality results suggest strong 
feedforward processing. Thick green arrows represent strong 
cortical activity across layers and widespread across cortical 
hierarchy. b, highly unpredictable global oddball resulted in limited 
feedback response, particularly in select higher order areas. We did 
not observe L2/3 prediction error signals in mice and found non-
specific L2/3 (compared to L5/6, except for in PFC at top of the 
hierarchy) prediction error signals in monkeys. Furthermore, 
optotagged inhibitory cells do not exhibit suppression specific to 
predictable stimuli.

Westerberg and Xiong et al.

.
CC-BY-NC-ND 4.0 International license
available under a
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

The copyright holder for this preprint
this version posted September 25, 2025. 
; 

doi: 
bioRxiv preprint

This figure, presented in two panels (a and b), is a schematic diagram illustrating different modes of cortical processing related to "oddball" stimuli, organized according to the ascending cortical hierarchy.

## 

Altogether, our results challenge multiple aspects of current 
PP models2-4,41.  
We found that PP is largely a property of neurons in higher-
order cortex (PFC in primates, and late stages of visual 
processing in both species). These higher-order areas, in 
which we found population level coding of global 
oddballs13,21,31,43, contain neurons with long timescales44 and 
therefore may be able to represent the relatively long 
duration of a sequence and its context, necessary elements 
to drive PP in this task. In contrast, neurons early in the 
visual sensory cortex have rigidly-defined receptive field 
properties refined during brain development45 with less 
plasticity in the mature brain. Neurons in sensory cortex also 
respond to fast changes in the environment and are therefore 
ill-suited for predictive computations that require flexible re-
mapping of responses and contextual processing over longer 
time scales. Neurons in higher-order areas are more flexible 
in their response preferences. These higher-order neurons 
can re-map their activity in real-time based on experience-
dependent learning and display mixed-selectivity. This 
property is necessary for predictive processing because 
predictions need to be sensitive to the statistical structure of 
a changing and context-dependent environment11,22,46. We 
hypothesize that mixed selectivity neurons flexibly remap 
cognitive spaces to signal predictions. Functionally, such

neurons could form dynamic ensembles via neuronal 
oscillations21,47 to guide sensory processing.  
Although our empirical findings failed to support multiple 
aspects of current PP models (Extended Data Table 1, 
Extended Fig. 1), some PP models hypothesized circuit 
elements which were supported by our data. For example, 
Nejad et al.6 propose that both deep and superficial layers 
cooperate for prediction error computations, an effect highly 
aligned with our laminar results. Higher-order areas 
participated in PP, although the computation was sparse 
across neurons. This supports models that have proposed 
that PFC and higher-order areas are involved in building 
flexible prediction in real-time21,31 along sub-spaces of 
neuronal activity (rather than engaging prediction errors 
widely in a core computation). Our result on global oddballs 
being more consistent with feedback (rather than 
feedforward) processing has yet to be considered in the PP 
model family, as far as we are aware. In addition, not all 
aspects of the proposed PP models have been tested. With 
our full dataset now openly available, this will be a rich 
resource as a community effort to establish the PP principles 
and circuitry that are more consistent with MaDeLaNe data. 
Using novel approaches to model building48 we suggest that 
PP models9 mature to be constrained and grounded in these 
and other emerging MaDeLaNe neuronal recordings12,13,49.

Acknowledgments | This work was funded by the US National Institutes of Health (NIH) [grant numbers: R00MH116100 (AMB), 
U24NS113646 (JAL, CrK)], the Dutch Research Council (NWO) [grant number: VI.Veni.232.110 (JAW)], the International Human 
Frontier Program Organization (HFSPO) [grant number: LT0001/2023-L], the Vanderbilt Faculty Fellow Award (AMB), and Vanderbilt 
University Startup Funding (AMB). The Neuropixels dataset was obtained at the Allen Brain Observatory as part of the OpenScope 
program, which is operated by the Allen Institute, Neural Dynamics program. We thank the OpenScope steering committee for their 
support, the Allen Institute founder, Paul G. Allen and Karel Svoboda, for their vision, encouragement, and support.

Author contributions | Conceptualization: JAW, AM, AMB; Data curation: JAW, AB, SD, BH, JAL; Formal analysis: JAW, YSX, 
ES, AMB; Funding acquisition: JAW, JAL, AMB; Investigation (NHP studies): JAW, YSX, HN, AMB; Investigation (rodent studies): 
SD, BH, HC, HB, HL, WH, KN, VH, TJ, CG, AY, JS, RG, BO, SC, AW, PAG; Project administration: JAW, CaK, JAL, AM, AMB; 
Software: JAW, AB, CRP; Supervision: SRO, ChK JAL, AM, AMB; Validation: JAW, AB, CRP, JAL; Visualization: JAW, YSX; 
Writing - original draft: JAW, AM, AMB; Writing - review, and editing: all authors

Competing interests | Authors declare that they have no competing interests.

Supplementary information | Methods included below. Supplementary information includes Supplementary text, Extended Data Table 
1, Extended Data Figs. 1-12, and References 50-92.