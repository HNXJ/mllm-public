## Page 1

Behavioral/Systems/Cognitive

A Neuronal Model of Predictive Coding Accounting for the
Mismatch Negativity

Catherine Wacongne,1,2,3 Jean-Pierre Changeux,4,5 and Stanislas Dehaene1,2,3,5

1Institut National de la Sante´ et de la Recherche Me´dicale, Unite´ 992, Cognitive Neuroimaging Unit, and 2Commissariat a` l’Energie Atomique, DSV/I2BM,
NeuroSpin Center, F-91191 Gif/Yvette, France, 3University Paris 11, F-91405 Orsay, France, 4Pasteur Institute, Centre National de la Recherche Scientifique
Unite´ de Recherche Associe´e 2182, F-75015 Paris, France, and 5Colle`ge de France, F-75005 Paris, France

Themismatchnegativity(MMN)isthoughttoindextheactivationofspecializedneuralnetworksforactivepredictionanddeviancedetection.
However,adetailedneuronalmodeloftheneurobiologicalmechanismsunderlyingtheMMNisstilllacking,anditscomputationalfoundations
remaindebated.Weproposehereadetailedneuronalmodelofauditorycortex,basedonpredictivecoding,thataccountsforthecriticalfeatures
of MMN. The model is entirely composed of spiking excitatory and inhibitory neurons interconnected in a layered cortical architecture with
distinctinput,predictive,andpredictionerrorunits.Aspike-timingdependentlearningrule,relyinguponNMDAreceptorsynaptictransmis-
sion, allows the network to adjust its internal predictions and use a memory of the recent past inputs to anticipate on future stimuli based on
transitionstatistics.WedemonstratethatthissimplearchitecturecanaccountforthemajorempiricalpropertiesoftheMMN.Theseincludea
frequency-dependent response to rare deviants, a response to unexpected repeats in alternating sequences (ABABAA. . . ), a lack of consider-
ationoftheglobalsequencecontext,aresponsetosoundomission,andasensitivityoftheMMNtoNMDAreceptorantagonists.Novelpredic-
tionsarepresented,andanewmagnetoencephalographyexperimentinhealthyhumansubjectsispresentedthatvalidatesourkeyhypothesis:
theMMNresultsfromactivecorticalpredictionratherthanpassivesynaptichabituation.

Introduction
Since it was first described at the end of 1970s, the mismatch nega-
tivity (MMN) has been largely used in theoretical and clinical re-
search (for review, see Na¨a¨ta¨nen, 2003). It was first recorded by EEG
in the context of the oddball paradigm. In the most frequently used
version of this paradigm, participants are instructed to listen to re-
peated occurrences of one sound, called the standard. This monot-
ony is disrupted at rare moments by the presentation of a different
sound, called the deviant. The difference in the responses evoked by
deviants and standards takes the form of a broadly negative wave-
form at the top of the scalp, which peaks between 100 and 200 ms
after the onset of the sound. MMNs can be elicited by differences in
sound frequency, duration (Na¨a¨ta¨nen et al., 1989), amplitude
(Na¨a¨ta¨nen et al., 1987), or interstimulus interval (ISI) (Ford
and Hillyard, 1981). MMN is resistant to manipulations of
attention and states of wakefulness (Sculthorpe et al., 2009)
even though these parameters can modulate its amplitude. An
analog of MMN was described in visual (Tales et al., 1999;
Pazo-Alvarez et al., 2003), olfactive (Krauel et al., 1999; Pause
and Krauel, 2000), and somatosensory (Kekoni et al., 1997;

Shinozaki et al., 1998) modalities, supporting a broad compu-
tational significance of MMN as a shared and automatic brain
mechanism responsive to stimulus novelty.

MMN is frequently interpreted in terms of predictive coding
(Rao and Ballard, 1999; Lee and Mumford, 2003), assuming that
the brain does not respond passively to incoming inputs but
learns the inputs regularities and uses that knowledge to actively
predict what should happen next. The auditory system would
acquire an internal model of regularities in auditory inputs, in-
cluding abstract ones, that are used to generate weighted predic-
tions about the incoming stimuli (Paavilainen et al., 1999;
Na¨a¨ta¨nen et al., 2005; Winkler, 2007). If these predictions differ
from the actual stimulus, it results in a mismatch signal.

While mathematical models of predictive coding have been pro-
posed(Garridoetal.,2007;Kiebeletal.,2008,2009),includingsome
attributing distinct functions to the various cortical layers (Friston,
2005), none of them has yet led to a precise neuronal implementa-
tion of the generators of the MMN, in terms of realistic receptors,
synapses,andspikingneurons.Norhastherebeenasystematiccom-
parison of the predictions of the models with actual experimental
results. Furthermore, not everyone accepts the predictive interpre-
tation of MMN. May and Tiitinen (2010) argue that synaptic habit-
uation(reductionoftheEPSPfollowingrepetitivestimulationofthe
same synapse) is sufficient to explain all of the properties of the
MMN and, thus, that there is no need to postulate an elaborate
prediction and comparison mechanism.

Here, we propose a neuronal network model, devoid of synaptic
habituation but comprising a detailed implementation of predictive
coding,accountingforalargeamountofdataontheMMN.Themodel
leads to the distinction of several processes that contribute to the ob-

Received Sept. 30, 2011; revised Dec. 12, 2011; accepted Jan. 4, 2012.

Author contributions: C.W., J.-P.C., and S.D. designed research; C.W. performed research; C.W. analyzed data;
C.W., J.-P.C., and S.D. wrote the paper.

This work was supported by a senior grant of the European Research Council (NeuroConsc program). The NeuroSpin
magnetoencephalographyfacilitywassponsoredbygrantsfromInstitutNationaldelaSante´etdelaRechercheMe´dicale,
Commissariat a` l’Energie Atomique, Fondation pour la Recherche Me´dicale, The Bettencourt–Schueller Foundation, and
Re´gionîle-de-France.WethankVirginieVanWassenhove,AlainDestexhe,andKarimBenchenaneforusefuldiscussions.

CorrespondenceshouldbeaddressedtoCatherineWacongne,Commissariata`l’EnergieAtomique/SAC/DSV/DRM/Neu-
roSpinCenter,Baˆt145,PointCourier156,F-91191Gif-sur-YvetteCedex,France.E-mail:catherine.wacongne@gmail.com.

DOI:10.1523/JNEUROSCI.5003-11.2012
Copyright©2012theauthors
0270-6474/12/323665-14$15.00/0

The Journal of Neuroscience, March 14, 2012 • 32(11):3665–3678 • 3665


---

## Page 2

served event-related responses, and makes new predictions, one of
which is tested here with magnetoencephalography (MEG).

Materials and Methods
Network architecture
The proposed neuronal network aims at modeling the response of pri-
mary auditory cortex to incoming sounds. Figure 1 shows an implemen-
tation of the model for an input composed of two pure tones, hereafter
called A and B. Each column of the network represents a cortical column
with its thalamic input responding maximally to one of the two frequen-
cies of the input. The two frequencies A and B are supposed to be differ-
ent enough to activate only one of the two columns.

In each column, three populations of neurons are simulated. The es-
sential component of the model is the population of neurons involved in
prediction, which we propose to be part of the supragranular layers of the
cortex. This population constantly tries to anticipate the upcoming au-
ditory inputs. A prediction of sound A consists in an increase in the
population firing rate coding for this stimulus.

At every moment, the continuously variable predictions arising from the
predictive populations of neurons are compared with the incoming inputs.

Thiscomparisonisachievedatthelevelofapopulationofneuronscalledthe
“prediction error” population, which receives two sets of inputs: excitatory
inputs coming from the thalamus and conveying the current sensory stim-
ulus, and inhibitory inputs that reflect the activity of the predictive popula-
tion. Through this scheme, whenever the thalamic input is not cancelled by
predictive signals, the prediction error population fires. The activity of the
prediction error population is transmitted to the predictive population as a
feedback and this error signal is used to adapt the internal model of this
population(seethedescriptionofthelearningrulefurtherbelow).Weshow
in Results that this error signal may account for the MMN effect.

The predictive population needs to build an internal model of the regu-
larities of the incoming stimulus to form relevant predictions. We propose
that this model is based on learning the statistical temporal dependencies
linking the stimuli within the past few hundred milliseconds. A memory of
the recent past is needed to achieve such a goal. This memory has to keep the
trace of two properties: the identity of the past inputs and the time elapsed
since they occurred. We choose to model this function in the simplest man-
ner possible, using a delay line for each frequency, where activation propa-
gates linearly from one neuron to the next as a function of time. The
relevance of this model will be discussed later.

Memory neurons are connected to both predictive subpopulations so
that predictions of one frequency (A) can be based on the recent occur-
rence of a sound of the other frequency (B). The internal model of the
predictive population is built by adapting the synaptic weights linking the
memory neurons and the predictive populations.

Detailed implementation
All subpopulations are composed of 40 neurons, except for delay lines
that are composed of 400 excitatory neurons and 100 inhibitory neurons.
All populations receive an external input Iext that is Gaussian noise of
mean equal to 0 and variance equal to 2.5 for input neurons, 2 for pre-
dictive neurons and prediction error neurons, 3.8 for interneurons.

By default, mean synaptic weight between two excitatory neurons is
wEE  1.4, between an excitatory and an inhibitory neuron wEI  4.5, and
between an inhibitory and excitatory neuron wIE  22. If a presynaptic
neuron is excitatory, wEI or wEE is the weight for AMPA-mediated cur-
rents. An NMDA receptor (NMDAr)-dependent current is added whose
weight wn is 20% of the AMPA synapse. The synaptic weights are drawn
from a Gaussian distribution with a variance of 20% of the mean. These
parameters allow a reliable transmission of activity from one population
to the other in absence of other inputs, while avoiding unrealistic syn-
chrony of neurons due to excessive homogeneity in the parameters.

The probability of a connection between thalamic inputs and prediction
error populations is p  0.9. The probability of a connection between pre-
dictivepopulationsandinterneuronsandbetweeninterneuronsandpredic-
tionerrorneurons,isp0.55.Synapsesbetweenpredictivepopulationsand
memory neurons were initialized with weight w  0.4 and variance of 20%
with a probability of connection of 0.5. Connectivity between layers is con-
sistent with neocortical local circuitry data (Thomson and Lamy, 2007).

Spiking neuron model
We used spiking neurons whose membrane potential is computed ac-
cording to the following Izhikevich (2003) equations:

dv

dt  0.04v2  5v  140  u  Isyn

du

dt  abv  u,

where v is dimensionless and represents the membrane potential and u is
a membrane recovery variable. The neurons fire if their membrane po-
tential reaches 30 mV and is then reset as follows:

if v  30 mV,
then

v 4 c
u 4 u  d.

The parameters for excitatory (respectively, inhibitory) neurons were as fol-
lows: a  0.02 (respectively, 0.06  0.04 * rand2), b  0.2  0.04 * rand2

(respectively, 0.2), c  65  10 * rand2 (respectively, 65), d  8  2 *

Figure1.
Schemeofthepredictivecodingmodelfortwosounds.Foreachlayer,twosubpopula-
tions are modeled that respond respectively to the frequencies of sounds A and B. Prediction error
activityinlayer4istheresultofthedifferencebetweenthalamicinputsandpredictiveactivityarising
fromthesupragranularlayer,whosesignisinvertedthroughinhibitoryinterneurons(blackcircles).
Predictionerroristhenfedbacktoadjusttheactivityofpredictivepopulations.Dynamicpredictions
aremadepossibleinthemodelbecausepredictiveunitssendandreceiveprojectionswitharecurrent
networkservingasashort-termmemory.NMDA-dependentplasticityadjuststhesynapticweights
onto predictive units until their dynamics matches that of the inputs and therefore minimizes the
predictionerror.

3666 • J. Neurosci., March 14, 2012 • 32(11):3665–3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity

> Figure description (generated): This figure is a multi-layered block diagram, likely representing a computational model or a hierarchical neural circuit structure. It is organized into four distinct horizontal layers, stacked vertically, with connections flowing between adjacent layers.

### 1. Overall Layout & Structure
The diagram is structured as a vertical stack of four rectangular blocks, representing different functional layers. The flow appears to be generally bottom-up or feedforward, though feedback loops are also present.

### 2. Visual Components & Symbols
**Layers (Blocks):**
1. **Top Layer:** A large, light gray rectangular block containing a circular arrow symbol ($\curvearrowright$), indicating a recurrent or feedback mechanism within this layer.
2. **Second Layer (from top):** A medium gray rectangular block containing two distinct nodes, $P(A)$ and $P(B)$.
3. **Third Layer (from top):** A medium gray rectangular block containing two dark, filled circular nodes, $\delta(A)$ and $\delta(B)$.
4. **Bottom Layer:** A light gray rectangular block containing two nodes, $I(A)$ and $I(B)$.

**Connections (Arrows/Lines):**
* **Inter-Layer Connections:** Arrows connect nodes between adjacent layers, indicating signal flow.
    * From Layer 1 to Layer 2: Multiple arrows originate from the top layer and point down into both $P(A)$ and $P(B)$.
    * From Layer 2 to Layer 3: Arrows connect $P(A)$ and $P(B)$ down to $\delta(A)$ and $\delta(B)$, respectively.
    * From Layer 3 to Layer 4: Arrows connect $\delta(A)$ and $\delta(B)$ down to $I(A)$ and $I(B)$, respectively.
* **Intra-Layer Connections (Feedback):** The top layer features a prominent curved arrow ($\curvearrowright$) within its boundary, signifying internal recurrence or feedback.
* **Cross-Layer Connections:** There are also connections shown between the nodes in Layer 2 ($P(A)$ and $P(B)$) that appear to feed back or interact with the nodes in Layer 1, although these connections are less explicitly drawn as directed arrows originating from $P(A)$ and $P(B)$ back into the top block, they are implied by the structure.

### 3. Labels, Keys & Legends
**Nodes and Variables:**
* **Top Layer:** Unlabeled block containing the recurrence symbol ($\curvearrowright$).
* **Second Layer:** $P(A)$ and $P(B)$.
* **Third Layer:** $\delta(A)$ and $\delta(B)$, represented by solid black circles.
* **Bottom Layer:** $I(A)$ and $I(B)$.

**Flow Indicators:**
* Arrows indicate the direction of information flow between layers.

### 4. Data Trends & Details
As this is a schematic diagram and not a plot, there are no axes or data trends to describe.

### 5. Contextual Caption Integration
The structure suggests a hierarchical processing model:
* The bottom layer, $I(A)$ and $I(B)$, likely represents input signals or initial states.
* The third layer, $\delta(A)$ and $\delta(B)$, processes these inputs.
* The second layer, $P(A)$ and $P(B)$, processes the output of the third layer.
* The top layer, with its internal recurrence ($\curvearrowright$), represents a higher-level processing or control mechanism that receives input from the second layer and potentially feeds back into itself.


---

## Page 3

rand2 (respectively, 2), where rand is a random number drawn from a uni-
form distribution between 0 and 1. These parameters correspond respec-
tivelytoregularspikingneuronsforexcitatoryneuronsandfastspikingones
for inhibition (Izhikevich, 2003).

AMPA, NMDA, and GABA synaptic currents are modeled according
to Brunel and Wang (2001) as follows:

Isynt  IAMPAt  INMDAt  IGABAt  Iextt

with

IAMPAt  gAMPAvt  VE

j1

CE

wj

AMPAsj

AMPAt

INMDAt 

gNMDAvt  VE
1  Mg2]exp  0.062vt/3.57

 

j1

CE

wj

NMDAsj

NMDAt

IGABAt  gGABAvt  Vi

j1

CI

wj

GABAsj

GABAt,

where VE  40 and Vi  80. The dimensionless weights wj

receptor type

represent the strength of synaptic connection associated with each recep-
tor type. The sum over j is the sum over all (CE) excitatory or (Ci) inhib-
itory presynaptic neurons. greceptor type are dimensionless variables that
represent the conductances of each receptor type with gAMPA  7.5*103,
gNMDA  2*103, and gGABA  7.5*103; [Mg2]  103. sj

receptor type is a
variable describing the opening dynamic of the receptors: AMPA and
GABA receptors have instantaneous opening and close up with time
constants AMPA  2 ms and GABA  10 ms, as follows:

dsj

AMPAt

dt


sj

AMPAt

AMPA
 

k

t  tj

k

dsj

GABAt

dt


sj

GABAt

GABA
 

k

t  tj

k.

where the sum over k represents a sum over spikes emitted by presynaptic
neuron j. NMDA receptors have slower dynamics with opening time
constant NMDA,rise  2 ms and closing time constant NMDA,decay  100
ms,   0.5 ms 1, as follows:

dsj

NMDAt

dt


sj

NMDAt
NMDA, decay  axjt1  sj

NMDAt

dxjt

dt


xjt
NMDA, rise  

k

t  tj

k.

Synaptic plasticity
To internalize the statistical regularities that relate past activity to present
stimuli, we implemented synaptic plasticity only between memory neurons
and predictive subpopulations. We used a spike timing-dependent plasticity
(STDP) rule (Bi and Poo, 1999) producing conditioning association as
follows:

If a postsynaptic spike at time t follows a presynaptic spike:

wpre,post  cpIca2  Thexp

t  tspike pre

p .

If a presynaptic spike follows a postsynaptic spike that occurred at time t:

wpre,post  cpIca2  Thexp

t  tspike post

p .

In addition, we used a long-term depression rule, which induces a small
depression of synapses whenever the presynaptic neuron spikes. This rule is
in agreement with experimental observation that synapses tend to depress
when they do not elicit postsynaptic spike (Debanne et al., 1998) as follows:

wpre,post   cd t  tspike pre).

The parameters used for the simulations presented in this paper are as
follows: cp  60, p  30 ms, cd  100, and Th  2.5.

We verified that our qualitative results were largely independent of the
fine tuning of the parameters. ICa2 is a calcium current mediated by
NMDA receptors. This current is taken equal to INMDA for each predic-
tive neuron.

Simulations
For each simulation, a new network was generated following the above
probabilistic connectivity rules. Each condition was simulated on 5–10
different networks; plotted results are averages over all simulations. In-
puts were an additional Iext current with amplitude 1.9, injected in the
thalamic subpopulation coding for the sound corresponding to the stim-
ulus presented. The input for each simulation was created by pseudoran-
domization of a set of trial containing the desired proportions of
standard and deviant stimuli. The randomization was made so that two
deviants were never consecutive. Standard stimuli immediately following
deviant stimuli were removed from analysis.

Various paradigms were simulated by modifying the sequence of A
and B inputs in different stimulus blocks. The classical oddball paradigm
was simulated as a sequence of 2000 tones, where 5, 10, 20, or 30% of the
tones were B tones (deviants) and other tones were A, with a stimulus
onset asynchrony (SOA) of 200 ms. The connectivity matrix was saved
after each tone, 100 ms after the onset of the tone. The mean connectivity
matrix that we report in Figure 4 represents the average connection
strength between the memory neurons and the predictive population. It
was obtained by averaging these matrices over each subpopulation of
predictive neurons and over all tones except the first 200. Alternate se-
quences were composed of 1500 pairs of alternating tones (ABAB. . . ;
ISI  200 ms). The reproduction of the local-global paradigm (Bekin-
schtein et al., 2009; Wacongne et al., 2011) was made by starting with 20
standard sequences (100% AAAAB; ISI  150 ms) followed by 100 se-
quences comprising 70% standards (AAAAB), 20% deviants (AAAAA),
and 10% omissions (AAAA). For the omission effect, a simulation of
1500 pairs of sounds (AA; ISI  200 ms) was also performed, with 10% of
pairs replaced by single tones (A). We compared this with the response to
500 single tones (A).

MEG experiment
Participants. Five healthy volunteers (three males, two females; mean age,
22) with no neurological or psychiatric problems were studied. All par-
ticipants gave their written informed consent to participate to this study,
which was approved by the local ethical committee.

Auditory stimulation. Pairs of 50-ms-duration sounds were presented
via headphones with an intensity of 45 dB and 200 ms SOA between
sounds. Each sound was a pure sinusoidal tone (either 800 Hz, low; or
1600 Hz, high).
Sounds were organized in two blocks. In each block, the frequent pair,
comprising two distinct sounds (AB), was first presented 10 times, with
1 s SOA between pairs. A total of 120 pairs was then presented, with SOA
varying between 10 and 20 s, and with 70% of frequent AB pairs, 10% of
rare AA pairs, 10% of rare BB pairs, and 10% of rare BA pairs. The
identity of the A and B tones was swapped between blocks. The pairs were
pseudorandomized so that two rare pairs were never consecutive. Fre-
quent pairs following immediately a rare pair are excluded from the
analysis. All stimuli were presented using E-prime software, version 1.1
(Psychology Software Tools).

MEG/EEG recordings. Measurements were performed with the Elekta
Neuromag MEG system (Elekta Neuromag Oy) installed at the NeuroS-
pin center (Saclay, France), which comprises 204 planar gradiometers
and 102 magnetometers in a helmet-shaped array. ECG as well as EOG
(horizontal and vertical) were simultaneously recorded as auxiliary
channels. MEG and auxiliary channels were low-pass filtered at 330 Hz,

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665–3678 • 3667


---

## Page 4

high-pass filtered at 0.1 Hz, and sampled at 1 kHz. The head position with
respect to the sensor array was determined by four head position indica-
tor coils attached to the participant’s scalp. The locations of the coils and
EEG electrode positions were digitized with respect to three anatomical
landmarks (nasion and preauricular points) with a 3D digitizer (Pol-
hemus Isotrak system). Then, head position with respect to the device
origin was acquired before each MEG/EEG recording session.

Each participant was recorded for 1 h, 15 min: two sessions of 33 min
duration separated by a short resting period. Participants were asked to
keep their eyes open and to avoid eyes movements by staring at a fixation
cross. Participants were instructed to pay attention to the auditory stim-
uli. Importantly, although subjects were attending to the stimuli, which
may generate additional attention-dependent components such as N2b,
these components typically do not contribute to MEG signals (Alho et al.,
1998). At the end of the recording, a question list was submitted to the
participant. This list aimed to determine which regularities the partici-
pant was able to report after recording.

Postprocessing. Artifacts arising from outside the sensor array, such as
those stemming from limb movement or other ambient magnetic distur-
bances, were greatly reduced by the signal space separation method (SSS)
(Taulu et al., 2004). Gradiometers and magnetometers with amplitudes
continuously exceeding 3000 fT/cm 2 and 3000 fT, respectively, were set
as bad channels and excluded from further analysis. SSS correction, head
movement compensation, and bad channels correction were applied us-
ing the MaxFilter Software (Elekta Neuromag).

A principal-component analysis (PCA) was used for PCA-based re-
moval of EEG and EOG artifacts. Signal was averaged around artifacts for
each channel type (EEG, axial and longitudinal gradiometers, and mag-
netometers) and a PCA was performed. Main components were saved.

The rest of the preprocessing was performed using Fieldtrip software
(http://fieldtrip.fcdonders.nl/). Trials were epoched for each trial type be-
tween200msbeforeand800msaftertheonsetofthefirstsound.Alow-pass
filter at 40 Hz was applied and PCA correction of cardiac and EOG artifacts
was performed using the PCA components previously computed. The trials
were baseline corrected using the first 200 ms of the epoch.

After visual rejection of jump and pronounced trend artifacts, the data
were averaged per condition and per participant. The latitudinal and
longitudinal gradiometers were combined by computing the mean
square root of signal at each sensor position.

Statistics. Statistics were performed using Fieldtrip cluster-based sta-
tistics. To examine differences between experimental conditions, paired t
tests were performed with a threshold set at p  0.05. Significant samples
were clustered in connected sets on the basis of temporal and spatial
proximity. Cluster statistics were calculated by taking the sum of t values
in every cluster. To obtain a p value corrected for the size of the search
space (time X sensors), a Monte Carlo method was used to evaluate how
extreme the cluster statistics of the two conditions were compared with
random partitions of the samples. The proportion of random partitions
that resulted in larger cluster statistics than the observed one was the p
value. The threshold was fixed to corrected p  0.05.

Statistics on the difference between the frequent AB condition and the
rare AA condition were computed between 0 and 300 ms after the onset
of the second sound.

Response amplitude. The amplitude of the response to each of the two
tones was defined as the average response over all magnetometers in the
time window of the peak response for each sound (i.e., between 95 and
125 ms after the onset of the first tone and between 135 and 160 ms after
the onset of the second tone). The amplitudes were normalized for each
subject by the response to the first sound averaged over all conditions.

Results
Oddball paradigm and MMN
We first simulated the response of the network to the classical odd-
ball paradigm. For this simulation, the network received as inputs
two stimuli A and B, corresponding to sounds of frequencies distant
enough to activate nonoverlapping populations of neurons. The in-
put neurons were supposed to be selective only to the onset of the
sound and were thus stimulated by an extra input current on input

populations during 10 ms. The first stimulus (“sound A”) was pre-
sented most of the time (standard tone), and the other one (“sound
B”) more rarely, with a parametrically variable frequency (deviant
tone).

The left panels of Figure 2 show the response to the standard
and deviant tones, averaged over all analyzed presentations, in
the specific case in which the deviant has a 10% probability of
occurrence. One can immediately observe that both the firing
rates and the synaptic currents of the prediction and prediction
error neurons (but not the sensory neurons) are higher on devi-
ant than on standard trials. The detailed neuronal mechanisms of
this mismatch effect are the following. First, note that the predic-
tive population coding for the sound A starts firing shortly before
the occurrence of both standard and deviant sounds (top panel,
red curve). This activity originates from the EPSCs coming from
the memory neurons: the network predicts the forthcoming oc-
currence of a sound A. This activity inhibits the prediction error
layer via an interneuron population. If a sound A is actually pre-
sented, it cancels most of the excitation coming from thalamic
inputs, resulting in a minimal prediction error response. As seen
in Figure 2, only a small proportion of prediction error neurons
still fire on standard trials, primarily due to stochastic fluctua-
tions in the onset and strength of delay and predictive neurons,
which therefore fails to fully cancel the incoming signal. On the
contrary, when a deviant sound B is presented, the prediction of
an A sound does not cancel the input for a B sound. This results in
a large prediction error response, which is relayed to the predic-
tive subpopulation coding for B to adapt the predictive model. It
forces the neurons of the predictive layer to discharge and causes
a large NMDAr-dependent current that results in NMDAr-
dependent plasticity. This plasticity leads to an adaptation of the
internal model of the network, reinforcing the synapses coming
from the delay lines that discharged just before the prediction
error signal.

The MMN is the result of a subtraction of the event-related
potentials (ERPs) to standard and deviant stimuli. The ERPs are
believed to be the result of a weighted integration of postsynaptic
currents. As a simplified proxy for local field potentials or EEG
responses, we calculated the difference in the sum of currents
received by each layer for standard or deviant sound. The third
column of Figure 2 shows the result of that operation. We can
observe that there is indeed a difference in the currents between
the two stimuli. For convenience, we will call this analog of the
experimental phenomenon the simulated MMN or sMMN.

Behavior of the memory neurons
The memory neurons play an important role in the model. The
stimulation of the network results in the activation of the predic-
tive population either because the incoming stimulus is predicted
or because of the transmission of prediction error. When the
predictive population is active, it triggers the set of delay-line
neurons (Fig. 3). The activity propagates linearly in the popula-
tion, such that there is a direct relationship between the indices of
the neurons in the delay line and the temporal information coded
by their activity. The precision of timing changes as a function of
the interval coded: the jitter in the exact time of activation of the
neurons increases with the delay coded (approximating Weber’s
law). Essentially, the activity of a neuron in a delay line codes for
two properties of past inputs: the identity of a past stimulus and
the time elapsed since the occurrence of that stimulus. The par-
ticular choice we made for the implementation of this double
function (delay lines) is not fully physiologically realistic but was

3668 • J. Neurosci., March 14, 2012 • 32(11):3665–3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity


---

## Page 5

made for the sake of clarity and computational economy (see
Discussion).

Layer distribution of current sources
We proposed a tentative localization for each functional popula-
tion within the cortical layers, according to which prediction er-
ror populations correspond to granular layer and predictive
populations belong to supragranular layer. Javitt et al. (1996)
provided relevant intracortical local field potential data on the
cortical origins of the MMN in primates. They showed in partic-
ular that the MMN mainly originates from supragranular layers
of the cortex. The results of our simulations are consistent with
these data, as they show that the sMMN primarily originates from
synaptic currents impinging upon prediction neurons (and aris-
ing from prediction error neurons). Importantly, note that, even
though there is a major difference in the firing rate of the predic-
tion error population between the two stimuli, it does not involve
a difference in the sum of synaptic inputs received by this layer as
a whole, but rather a different distribution of these inputs on
neurons coding for sounds A and B.

Studies in mice (Ehrlichman et al., 2008), rats (Tikhonravov et
al., 2008, 2010), and monkeys (Javitt et al., 1996) also showed that
MMN is strongly affected by NMDAr inhibitors. In our simula-
tions, the sMMN results essentially from NMDAr-dependent
currents, which is consistent with this observation.

Effect of deviant probability
The vast literature on the MMN describes a broad set of proper-
ties (for review, see Na¨a¨ta¨nen et al., 2007). To evaluate the range
of validity of this model, we next simulated the response of the
model in various conditions mimicking classical experimental
paradigms. Our first test concerned the effect of the proportion of

deviants in the standard oddball paradigm. Sato et al. (2000)
described a systematic and parametric dependency of MMN am-
plitude on the probability of occurrence of a deviant sound. They
showed that amplitude of the MMN increases as the frequency of
the deviants decreases. We simulated the network for various
proportions of deviant in the oddball paradigm (10, 20, and
30%). Results are plotted in the third column of Figure 2. We can
see that the amplitude of sMMN indeed increases with the rarity
of the deviants. This reduction in sMMN comes from the in-
creased activity of the predictive population coding for B, as a
result of its more frequent occurrence after an A, combined with
a slightly lower prediction of the A sound that increases the aver-
age prediction error to A. This finding closely matches the exper-
imentally recorded ERP data.

The frequency effect shows that MMN is not an all-or-none
phenomenon, but a graded response whose amplitude reflects a
parametric quantification of the amount of surprise conveyed by
the stimulus, given the past stimuli. It is consistent with an inter-
nal model that takes into account statistical regularities.

Internal model of the temporal statistics in the input
The simplicity of the population of memory neurons used in our
model allows us to visualize the statistical information learned by
the network (Fig. 4). The only plasticity in the model occurs at
synapses between the memory neurons and the predictive sub-
populations. The information coded in these synaptic weights
can be directly compared with the actual conditional probabili-
ties in the actual input sequences. Figure 4 shows the mean
synaptic weights between the delay lines and the predictive
subpopulations as a function of the probability of occurrence of a
deviant. They are compared with the actual statistics of transition
probabilities in the inputs. Even though the plasticity rule was not

Figure 2.
SimulatingtheMMNinanoddballparadigm:meansynapticcurrentsandfiringrates.Thefigureshowsthemeansimulatedresponsetoastandardtone(firstcolumn),adevianttone(second
column),andtheirdifference(thirdcolumn)after200learningtrialsinanoddballparadigm.Eachlineshowstheresponseofadifferentlayerofunitsinthemodel(organizedasinFig.1).Foreachlayer,thetop
partoftheplotrepresentsthesynapticcurrentsreceivedbythesubpopulation,separatelyforthedifferenttypesofpostsynapticreceptorsthatmediatethesecurrents:AMPA(continuousline),NMDA(dashed
line),orGABA(dottedline).Thebottompartofeachplotdisplaysthemeanfiringrateofeachsubpopulation.Inthefirstandsecondcolumns,subpopulationsrespondingtothefrequentAsound(90%oftrials)
arerepresentedinred,andthoserespondingtotherareBsound(10%)inblue.Thethirdcolumnshowstheresultsofsimulationsinwhichthepercentageofdeviantswasvaried(10,20,or30%).

> Figure caption (from PDF text): Figure 2.
SimulatingtheMMNinanoddballparadigm:meansynapticcurrentsandfiringrates.Thefigureshowsthemeansimulatedresponsetoastandardtone(firstcolumn),adevianttone(second
column),andtheirdifference(thirdcolumn)after200learningtrialsinanoddballparadigm.Eachlineshowstheresponseofadifferentlayerofunitsinthemodel(organizedasinFig.1).Foreachlayer,thetop
partoftheplotrepresentsthesynapticcurrentsreceivedbythesubpopulation,separatelyforthedifferenttypesofpostsynapticreceptorsthatmediatethesecurrents:AMPA(continuousline),NMDA(dashed
line),orGABA(dottedline).Thebottompartofeachplotdisplaysthemeanfiringrateofeachsubpopulation.Inthefirstandsecondcolumns,subpopulationsrespondingtothefrequentAsound(90%oftrials)
arerepresentedinred,andthoserespondingtotherareBsound(10%)inblue.Thethirdcolumnshowstheresultsofsimulationsinwhichthepercentageofdeviantswasvaried(10,20,or30%).
> Figure description (generated): This figure, labeled "Figure 2," presents a set of simulated results from the MMN (Mismatch Negativity) in an oddball paradigm, displayed across multiple panels. The structure appears to be organized into columns representing different conditions (Standard Tone, Deviant Tone, and Difference) across multiple layers of units.

### Overall Layout & Structure
The figure is composed of at least two main vertical sections, each containing multiple plots stacked vertically. Based on the caption, these represent different layers of units in the model (organized as in Fig. 1). Each major section appears to be divided into three columns:
1. **First Column:** Response to the standard tone (90% of trials).
2. **Second Column:** Response to the deviant tone (10% of trials).
3. **Third Column:** The difference between the responses.

Within each column, there are two distinct plotting regions stacked vertically:
1. **Top Plot:** Represents the mean synaptic currents received by a subpopulation, separated by postsynaptic receptor type.
2. **Bottom Plot:** Represents the mean firing rate of that subpopulation.

The figure displays data for multiple layers, indicated by different line styles and colors across the stacked plots.

### Visual Components & Symbols
**Plot Elements:**
* **Lines (Top Plots):** Different line styles represent different postsynaptic receptor types:
    * **Continuous Line:** Represents AMPA currents.
    * **Dashed Line:** Represents NMDA currents.
    * **Dotted Line:** Represents GABA currents.
* **Bars (Bottom Plots):** Vertical bars represent the mean firing rate for specific subpopulations.
* **Color Coding:** Color is used to distinguish subpopulations based on the tone they respond to:
    * **Red:** Subpopulations responding to the frequent sound (Standard Tone).
    * **Blue:** Subpopulations responding to the rare sound (Deviant Tone).

**Annotations/Markers:**
* **Vertical Dashed Line:** A prominent vertical dashed line is present in the top plots, likely indicating a specific time point or event within the simulation.
* **Vertical Solid Line:** A vertical solid line is present in the bottom plots, also marking a specific time point.

### Axes and Scales
**Y-Axes:**
* **Top Plots (Synaptic Currents):** The y-axis ranges from 0 to 8.
* **Bottom Plots (Firing Rates):** The y-axis ranges from 0 to 8.

**X-Axes:**
* **Both Plot Types:** The x-axis represents time, though specific units are not labeled on the visible portion of the axes.

### Data Trends & Details (Interpreting Specific Plots)
The caption specifies that the figure shows responses after 200 learning trials.

**Top Plots (Synaptic Currents):**
* **General Trend:** The plots show dynamic changes in synaptic currents over time.
* **Color/Line Interpretation (Example):** In the first column (Standard Tone), the red lines/curves show the response of subpopulations responding to the frequent sound. The blue lines/curves show the response of those responding to the deviant tone, even during standard tone presentation.
* **Receptor Dynamics:** The relative heights and shapes of the AMPA (continuous), NMDA (dashed), and GABA (dotted) lines indicate how different receptor types contribute to the total synaptic current for each subpopulation.

**Bottom Plots (Firing Rates):**
* **General Trend:** These plots show the mean firing rate.
* **Color/Bar Interpretation (Example):** In the first column, red bars indicate firing rates for subpopulations tuned to the standard tone. Blue bars indicate tuning to the deviant tone.
* **Third Column Detail:** The caption notes that in the third column, simulations were run varying the percentage of deviants (10%, 20%, or 30%), suggesting that differences in the height of the bars/curves across this column reflect these varying parameters.

### Contextual Caption Integration
The caption clarifies the following:
* **Purpose:** The figure simulates the MMN in an oddball paradigm.
* **Columns:** Column 1 = Standard Tone response; Column 2 = Deviant Tone response; Column 3 = Difference between responses.
* **Lines/Receptors:** AMPA (continuous), NMDA (dashed), GABA (dotted).
* **Colors/Tuning:** Red = responding to frequent sound; Blue = responding to rare sound.
* **Bottom Plots:** Display the mean firing rate.

> Figure caption (from PDF text): Figure 2.
SimulatingtheMMNinanoddballparadigm:meansynapticcurrentsandfiringrates.Thefigureshowsthemeansimulatedresponsetoastandardtone(firstcolumn),adevianttone(second
column),andtheirdifference(thirdcolumn)after200learningtrialsinanoddballparadigm.Eachlineshowstheresponseofadifferentlayerofunitsinthemodel(organizedasinFig.1).Foreachlayer,thetop
partoftheplotrepresentsthesynapticcurrentsreceivedbythesubpopulation,separatelyforthedifferenttypesofpostsynapticreceptorsthatmediatethesecurrents:AMPA(continuousline),NMDA(dashed
line),orGABA(dottedline).Thebottompartofeachplotdisplaysthemeanfiringrateofeachsubpopulation.Inthefirstandsecondcolumns,subpopulationsrespondingtothefrequentAsound(90%oftrials)
arerepresentedinred,andthoserespondingtotherareBsound(10%)inblue.Thethirdcolumnshowstheresultsofsimulationsinwhichthepercentageofdeviantswasvaried(10,20,or30%).
> Figure description (generated): This figure, labeled "Figure 2," presents a set of comparative plots illustrating the simulated response in an oddball paradigm. The overall structure consists of two main vertical sections, each containing a set of three related plots stacked vertically.

### Overall Layout and Structure
The figure is organized into two major horizontal blocks, each representing a different condition or comparison. Within each block, there are three distinct vertical panels arranged side-by-side (columns).

*   **Top Block:** Shows the simulated response to a standard tone.
*   **Bottom Block:** Shows the simulated response to a deviant tone.

Each of these three columns (Standard Tone, Deviant Tone, Difference) contains two sub-plots stacked vertically:
1.  **Top Sub-plot:** Displays synaptic currents received by a subpopulation.
2.  **Bottom Sub-plot:** Displays the mean firing rate of that same subpopulation.

A vertical dashed line is present in all six plots, likely indicating a specific temporal point or threshold.

### Visual Components and Data Representation

**Synaptic Current Plots (Top Sub-plots):**
These plots show continuous lines representing synaptic currents. The caption specifies that different line styles represent different postsynaptic receptors:
*   **AMPA:** Continuous line.
*   **NMDA:** Dashed line.
*   **GABA:** Dotted line.

The lines are color-coded based on the stimulus type:
*   **Red Lines:** Represent subpopulations responding to the frequent sound (90% of trials).
*   **Blue Lines:** Represent subpopulations responding to the rare sound (10% of trials).

**Firing Rate Plots (Bottom Sub-plots):**
These plots display discrete bar graphs representing the mean firing rate. The color coding (Red for frequent sound, Blue for rare sound) is maintained here as well.

**X-Axis and Temporal Context:**
The x-axis across all plots represents time, though specific units are not labeled on the axes themselves. The vertical dashed line serves as a critical temporal marker.

### Detailed Panel Analysis (Interpreting the Columns)

**1. First Column (Standard Tone):**
*   **Top Plot:** Shows the synaptic currents for the standard tone. Red and blue lines (AMPA, NMDA, GABA) are visible, showing baseline activity around the dashed line.
*   **Bottom Plot:** Shows the mean firing rates for the standard tone, depicted as low-level bars.

**2. Second Column (Deviant Tone):**
*   **Top Plot:** Shows the synaptic currents for the deviant tone. The lines exhibit a more pronounced response compared to the first column, particularly around the dashed line.
*   **Bottom Plot:** Shows a clear increase in firing rate (taller bars) for the subpopulations responding to the deviant tone, concentrated around the dashed line.

**3. Third Column (Difference):**
*   This column represents the difference between responses, where the percentage of deviants was varied (10%, 20%, or 30%).
*   **Top Plot:** Shows the difference in synaptic currents. The lines here appear to represent the differential response across different deviant percentages, although specific legends for these variations are not explicitly detailed on the plot itself.
*   **Bottom Plot:** Shows the difference in mean firing rates, again showing bars whose height likely corresponds to the differential response across the varied deviant percentages.

### Contextual Caption Integration
The caption clarifies that:
*   The top part of the plot shows **synaptic currents** received by a subpopulation, separated by receptor type (AMPA/continuous, NMDA/dashed, GABA/dotted).
*   The bottom part of the plot shows the **mean firing rate** of each subpopulation.
*   The color coding (Red/Blue) distinguishes subpopulations responding to the frequent sound vs. the rare sound, respectively.
*   The third column specifically illustrates results where the percentage of deviants was manipulated (10%, 20%, or 30%).

> Figure caption (from PDF text): Figure 2.
SimulatingtheMMNinanoddballparadigm:meansynapticcurrentsandfiringrates.Thefigureshowsthemeansimulatedresponsetoastandardtone(firstcolumn),adevianttone(second
column),andtheirdifference(thirdcolumn)after200learningtrialsinanoddballparadigm.Eachlineshowstheresponseofadifferentlayerofunitsinthemodel(organizedasinFig.1).Foreachlayer,thetop
partoftheplotrepresentsthesynapticcurrentsreceivedbythesubpopulation,separatelyforthedifferenttypesofpostsynapticreceptorsthatmediatethesecurrents:AMPA(continuousline),NMDA(dashed
line),orGABA(dottedline).Thebottompartofeachplotdisplaysthemeanfiringrateofeachsubpopulation.Inthefirstandsecondcolumns,subpopulationsrespondingtothefrequentAsound(90%oftrials)
arerepresentedinred,andthoserespondingtotherareBsound(10%)inblue.Thethirdcolumnshowstheresultsofsimulationsinwhichthepercentageofdeviantswasvaried(10,20,or30%).
> Figure description (generated): This figure, labeled as Figure 2, presents a set of time-course plots simulating the Mean Matching Network (MMN) in an oddball paradigm. The figure is structured into two main rows of plots, each row containing three distinct columns, resulting in six primary panels.

### Overall Layout and Structure
The figure is organized into two horizontal sections (implied by the vertical spacing, though not explicitly labeled as Panel A/B in the visible crop) and three vertical columns. Each column represents a different experimental condition:
1. **First Column:** Response to the standard tone (frequent sound).
2. **Second Column:** Response to the deviant tone (rare sound).
3. **Third Column:** The difference between the standard and deviant responses, with varying percentages of deviants (10%, 20%, or 30%).

Each column contains two sub-plots stacked vertically:
*   **Top Sub-plot:** Represents the mean synaptic currents received by a subpopulation.
*   **Bottom Sub-plot:** Represents the mean firing rate of that same subpopulation.

### Visual Components and Data Trends (Focusing on the visible plots)

**X-Axis:** For all plots, the horizontal axis is labeled **"time (s)"**, ranging from 0 to approximately 0.25 seconds.

**Y-Axes:**
*   **Top Sub-plots (Synaptic Currents):** The vertical axis ranges from 0 to 2.
*   **Bottom Sub-plots (Firing Rates):** The vertical axis ranges from 0 to 10.

#### Synaptic Current Plots (Top Row)
These plots display multiple lines representing different types of postsynaptic receptors:
*   **AMPA:** Represented by a **continuous line**.
*   **NMDA:** Represented by a **dashed line**.
*   **GABA:** Represented by a **dotted line**.

In the first and second columns, different colors denote subpopulations:
*   **Red:** Subpopulations responding to the frequent sound (90% of trials).
*   **Blue:** Subpopulations responding to the rare B sound (10% of trials).

In the third column, the lines likely represent different simulation conditions based on the percentage of deviants (10%, 20%, or 30%).

**Observed Trends:**
*   In the first and second columns, a clear transient increase in synaptic currents is visible shortly after $t=0.1$ seconds, peaking around $t \approx 0.15$ s for the deviant tone (second column).
*   The third column shows a pattern where the response magnitude changes across the different conditions (10%, 20%, 30% deviant percentage).

#### Firing Rate Plots (Bottom Row)
These plots display the mean firing rate for each subpopulation.

**Observed Trends:**
*   In the first and second columns, a transient increase in firing rate is visible corresponding to the synaptic current peaks.
*   The bottom plots also show distinct color coding (red and blue) corresponding to the subpopulations responding to standard vs. deviant sounds, respectively.

### Contextual Caption Integration
The caption clarifies the meaning of these visual elements:
*   **Top Plot:** Shows mean synaptic currents received by a subpopulation, separated by receptor type (AMPA=continuous, NMDA=dashed, GABA=dotted).
*   **Bottom Plot:** Displays the mean firing rate of each subpopulation.
*   **Color Coding (Columns 1 & 2):** Red indicates subpopulations responding to the frequent sound (90% trials); Blue indicates those responding to the rare B sound (10%).
*   **Third Column:** Represents simulations where the percentage of deviants was varied (10%, 20%, or 30%).
*   **Layer Representation:** Each line represents the response of a different layer of units in the model, organized as described in Figure 1 (not visible here).

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665–3678 • 3669


---

## Page 6

specifically designed to converge onto a
conditional transition probability, we can
observe a close correspondence between
the learned synaptic weights and the con-
ditional information contained in the in-
put. The peaks of synaptic strength
coincide with the temporal intervals be-
tween the stimuli, and their amplitude is
proportional to the probability of a tran-
sition between two stimuli almost regard-
less of the probability of occurrence of the
first stimulus. Thus, this observation pro-
vides a very simple picture of what our
model does: it stores, within its synaptic
strengths, the conditional probability of ob-
servingasecondstimulusatacertainlatency
after the first. Our claim is that the MMN
reflects,inaquantitativemanner,thedegree
of violation of such transition probabilities.

Importantly, the present model relies on
STDPplasticitytointernalizethestatisticsof
the input. Data show that the MMN devel-
ops rapidly within few presentations of the
standards (Winkler et al, 1996). To account
for the MMN with such a mechanism, it is
criticalthatplasticityoccursonashorttime-
scale of a few seconds. To our knowledge,
there are no data testing this prediction
by trying to induce STDP on short time-
scales using ecological stimulation, and
this hypothesis is therefore a prediction
of the model that remains to be tested
experimentally.

The time span over which the stimulus
transitions can be learned is strictly lim-
ited by the capacity of the memory. Here,
we adopted as a simplifying assumption
the hypothesis that the memory trace
abruptly vanishes after 400 ms. Despite
this artificially abrupt transition, we ob-
serve that synaptic weights get progres-
sively weaker for more distant delays, due
to the increased jitter in the coding of in-
creasingly longer temporal intervals. In a
more realistic memory network, the arti-
ficial delay lines that we used could be re-
placed by more realistic chaotic temporal
dynamics, as in “reservoir” or echo state networks models (Maass
et al., 2002; Buonomano, 2005; Buonomano and Laje, 2010; Pas-
canu and Jaeger, 2011). The memory trace would then become
increasingly diluted with elapsed time, thus explaining that, in
the standard oddball paradigm, a partially preserved but increas-
ingly reduced MMN is observed as the time interval between
tones is increased (Pegado et al., 2010).

MMN to repetition in an alternate signal
To further assess the properties of the model, we simulated the
response to sequences where two stimuli are presented in an al-
ternate fashion (ABABA . . .). On rare occasions, sound B is re-
placed by sound A. Horva´th and Winkler (2004) showed
experimentally that, in this condition, a MMN is now observed to
the unexpected repetition of a stimulus B, in a context in which
an alternation (ABABA . . .) was expected. This result is counter-

intuitive for habituation models, but entirely compatible with
predictive-coding models. Indeed, we simulated the response of
the network for an input constituted by a regular alternation of A
and B every 150 ms. Rarely, sound B was replaced by sound A,
resulting in the succession of three As in a row. Results are plotted
in Figure 5. An sMMN is observed, showing that the unexpected
repeated sound behaves as a deviant in the standard oddball para-
digm. Indeed, the predictive population coding for B increases its
activity 150 ms after an A occurred. In other words, the network
learns to predict that after an A comes a B at 150 ms. This internal-
ization of input statistics can also be seen in the synaptic weights.

Blindness to global regularities
Experimentally, the MMN is known to be blind to some global
regularities in the stimulus sequence. For example, Bekinschtein
et al. (2009) showed that, when participants are presented with

p1
p2
p3

e1
e2
e3

Figure 3.
Simulated pattern of neural firing and membrane voltage during a single trial of the oddball paradigm. The figure
shows a typical response to a standard tone (t  0 ms) followed by a deviant tone (t  150 ms). Left column, Subpopulations
selectivetotoneA;rightcolumn,subpopulationsselectivetotoneB.Foreachlayer,thetoppartofthepanelrepresentssingle-unit
membranevoltage(onelinepersimulatedneuron);thebottompartistheaveragevoltageoverthepopulation.Theneuronsofthe
memorytracearereorderedsothatthepropagationoftheactivityinasynfirechainwayismadeobvious.“n-1,”“n-2,”and“n-3”
arrowed boxes refer to past stimuli whose activity is propagating in the delay lines initiated. In the left column, “n” and “n1”
arrowed boxes point to the initiation of a new memory trace following synchronous activity of the predictive population corre-
sponding to the prediction of the stimuli n and n1 (“p1” and “p2” arrows). In the right column, the “n1” arrowed box shows
the initiation of a new memory trace following synchronous activity of the predictive population corresponding to the prediction
errorsignalofthen1(deviant)stimulus.Afterlearning(Fig.4),areproduciblepatternofactivationinmemorytraceproducesa
depolarizationinthepredictivelayer(blackarrows)viaapopulationofinterneurons(notdisplayedhere).Theactivityinpredictive
layerinducesanhyperpolarizationinthepredictionerrorlayer(“e2”arrow)attheapproximatetimewhenanAsoundisexpected.
At t  0, both prediction and input belong to the same column, resulting in a cancellation of excitation and inhibition inside the
predictionerrorlayer(“e1”arrow).Att150ms,whenadeviantstimulusBispresented,adepolarizationofthepredictionerror
population selective to the deviant (“e3” arrow) can be observed in parallel to the hyperpolarization of the predictive population
selective to the standard (“e2” arrow). This depolarization is transmitted to the predictive (“p3” arrow) and memory (left column
“n1” arrow) populations.

> Figure caption (from PDF text): Figure 3.
Simulated pattern of neural firing and membrane voltage during a single trial of the oddball paradigm. The figure
shows a typical response to a standard tone (t  0 ms) followed by a deviant tone (t  150 ms). Left column, Subpopulations
selectivetotoneA;rightcolumn,subpopulationsselectivetotoneB.Foreachlayer,thetoppartofthepanelrepresentssingle-unit
membranevoltage(onelinepersimulatedneuron);thebottompartistheaveragevoltageoverthepopulation.Theneuronsofthe
memorytracearereorderedsothatthepropagationoftheactivityinasynfirechainwayismadeobvious.“n-1,”“n-2,”and“n-3”
arrowed boxes refer to past stimuli whose activity is propagating in the delay lines initiated. In the left column, “n” and “n1”
arrowed boxes point to the initiation of a new memory trace following synchronous activity of the predictive population corre-
sponding to the prediction of the stimuli n and n1 (“p1” and “p2” arrows). In the right column, the “n1” arrowed box shows
the initiation of a new memory trace following synchronous activity of the predictive population corresponding to the prediction
errorsignalofthen1(deviant)stimulus.Afterlearning(Fig.4),areproduciblepatternofactivationinmemorytraceproducesa
depolarizationinthepredictivelayer(blackarrows)viaapopulationofinterneurons(notdisplayedhere).Theactivityinpredictive
layerinducesanhyperpolarizationinthepredictionerrorlayer(“e2”arrow)attheapproximatetimewhenanAsoundisexpected.
At t  0, both prediction and input belong to the same column, resulting in a cancellation of excitation and inhibition inside the
predictionerrorlayer(“e1”arrow).Att150ms,whenadeviantstimulusBispresented,adepolarizationofthepredictionerror
population selective to the deviant (“e3” arrow) can be observed in parallel to the hyperpolarization of the predictive population
selective to the standard (“e2” arrow). This depolarization is transmitted to the predictive (“p3” arrow) and memory (left column
“n1” arrow) populations.
> Figure description (generated): ## Detailed Figure Description

This figure, labeled as **Figure 3**, presents a simulated pattern of neural firing and membrane voltage across two distinct experimental conditions, organized into columns. The overall structure is a multi-panel visualization displaying time-series data for neural activity, likely representing the response to an oddball paradigm.

### 1. Overall Layout & Structure
The figure is divided into two main vertical columns, corresponding to different selective populations:
*   **Left Column:** Labeled as "Subpopulations selective to tone A."
*   **Right Column:** Labeled as "Subpopulations selective to tone B."

Within each column, the data is presented in two stacked sections:
1.  **Upper Section:** Represents single-unit membrane voltage, depicted as a raster plot or time-series visualization.
2.  **Lower Section:** Represents the average voltage over the population, shown as a trace or plot below the raster data.

The entire visualization spans across time (implied on the horizontal axis, with specific time points mentioned in the caption) and activity/voltage (implied on the vertical axis).

### 2. Visual Components & Symbols
**A. Raster Plot (Upper Section):**
*   This section displays a dense, grayscale pattern representing neural firing. The intensity or darkness of the pixels likely corresponds to activity level or voltage fluctuation over time for individual simulated neurons.
*   The data is organized vertically, with each horizontal line representing a single simulated neuron's activity.
*   **Annotations:** Several specific elements are marked with arrowed boxes:
    *   Boxes labeled "n-1," "n-2," and "n-3" are present, indicating past stimuli whose activity is propagating in delay lines.
    *   In the **Left Column**, boxes labeled "n" and "n+1" point to the initiation of a new memory trace following synchronous activity.
    *   In the **Right Column**, a box labeled "n+1" points to the initiation of a new memory trace following prediction error signaling.

**B. Average Voltage Plot (Lower Section):**
*   This section displays a continuous trace representing the average voltage across the population. It shows dynamic changes in membrane potential over time.
*   **Annotations:** Several specific events are marked with arrows pointing to the trace:
    *   An arrow labeled "e1" is visible in the left column, indicating a cancellation of excitation and inhibition.
    *   An arrow labeled "e2" is visible in the left column, indicating hyperpolarization.
    *   An arrow labeled "e3" is visible in the right column, indicating depolarization.
    *   Arrows labeled "p1," "p2," and "p3" are present, indicating the initiation or propagation of activity.

### 3. Labels, Keys & Legends
**Column Headers:**
*   "Subpopulations selective to tone A" (Left)
*   "Subpopulations selective to tone B" (Right)

**Internal Annotations/Labels:**
*   $t \approx 0 \text{ ms}$ (Indicates the time of a standard tone).
*   $t \approx 150 \text{ ms}$ (Indicates the time of a deviant tone).
*   "n-1," "n-2," "n-3" (Referencing past stimuli).
*   "p1," "p2" (Arrows in the left column indicating memory trace initiation).
*   "e1," "e2," "e3" (Arrows indicating specific voltage events: cancellation, hyperpolarization, depolarization).
*   "p3" (Arrow indicating activity propagation in the right column).

### 4. Data Trends & Details
The visualization captures dynamic changes over time, centered around $t=0$ ms and $t=150$ ms.

*   **At $t \approx 0 \text{ ms}$ (Standard Tone):** In the left column, the activity appears synchronized leading up to and around $t=0$, corresponding to the "e1" arrow, suggesting a cancellation event in the prediction error layer.
*   **At $t \approx 150 \text{ ms}$ (Deviant Tone):**
    *   In the left column, an event labeled "e2" (hyperpolarization) is observed in parallel with the expected sound timing.
    *   In the right column, an event labeled "e3" (depolarization) is observed in parallel to the hyperpolarization ("e2"). This depolarization then propagates via "p3" and initiates a memory trace (indicated by the "n+1" arrow).

### 5. Contextual Caption Integration
The caption clarifies the functional meaning of the observed patterns:
*   **Layers:** The figure represents activity in different layers, including a "predictive layer," a "prediction error layer" ($\text{e1}, \text{e2}, \text{e3}$), and a "memory trace."
*   **Activity Flow:** The activity propagation is visualized in a "synfire chain way."
*   **Learning Effects (Post-Fig. 4):** The caption notes that after learning, the predictive layer induces depolarization via interneurons, which in turn causes hyperpolarization in the prediction error layer ($\text{e2}$ arrow) when a sound is expected.
*   **Event Interpretation:** The depolarization ($\text{e3}$ arrow) observed at $t=150 \text{ ms}$ in the right column (deviant stimulus) is transmitted to the predictive ($\text{p3}$) and memory populations.

> Figure caption (from PDF text): Figure 3.
Simulated pattern of neural firing and membrane voltage during a single trial of the oddball paradigm. The figure
shows a typical response to a standard tone (t  0 ms) followed by a deviant tone (t  150 ms). Left column, Subpopulations
selectivetotoneA;rightcolumn,subpopulationsselectivetotoneB.Foreachlayer,thetoppartofthepanelrepresentssingle-unit
membranevoltage(onelinepersimulatedneuron);thebottompartistheaveragevoltageoverthepopulation.Theneuronsofthe
memorytracearereorderedsothatthepropagationoftheactivityinasynfirechainwayismadeobvious.“n-1,”“n-2,”and“n-3”
arrowed boxes refer to past stimuli whose activity is propagating in the delay lines initiated. In the left column, “n” and “n1”
arrowed boxes point to the initiation of a new memory trace following synchronous activity of the predictive population corre-
sponding to the prediction of the stimuli n and n1 (“p1” and “p2” arrows). In the right column, the “n1” arrowed box shows
the initiation of a new memory trace following synchronous activity of the predictive population corresponding to the prediction
errorsignalofthen1(deviant)stimulus.Afterlearning(Fig.4),areproduciblepatternofactivationinmemorytraceproducesa
depolarizationinthepredictivelayer(blackarrows)viaapopulationofinterneurons(notdisplayedhere).Theactivityinpredictive
layerinducesanhyperpolarizationinthepredictionerrorlayer(“e2”arrow)attheapproximatetimewhenanAsoundisexpected.
At t  0, both prediction and input belong to the same column, resulting in a cancellation of excitation and inhibition inside the
predictionerrorlayer(“e1”arrow).Att150ms,whenadeviantstimulusBispresented,adepolarizationofthepredictionerror
population selective to the deviant (“e3” arrow) can be observed in parallel to the hyperpolarization of the predictive population
selective to the standard (“e2” arrow). This depolarization is transmitted to the predictive (“p3” arrow) and memory (left column
“n1” arrow) populations.
> Figure description (generated): ## Figure Description: Simulated Neural Firing and Membrane Voltage

This figure presents a simulation of neural activity across two distinct populations, visualized in a time-series format. The overall structure is divided into two main vertical columns, representing different selective populations, and each column contains multiple horizontal panels detailing neural activity.

### 1. Overall Layout & Structure
The figure is structured into two primary vertical sections: the **Left Column** and the **Right Column**. Each column appears to represent a different population selective to specific tones (Tone A in the left, Tone B in the right). Within each column, there are multiple horizontal panels stacked vertically.

The caption specifies that for *each layer*, the **top part of the panel** represents single-unit membrane voltage (one line per simulated neuron), while the **bottom part** shows the average voltage over the population.

### 2. Visual Components & Symbols
The visual data within the panels consists of grayscale representations, likely representing membrane voltage over time.

*   **Time Axis (X-axis):** The horizontal axis represents time, with specific markers indicating stimulus presentation times: $t=0$ ms (Standard Tone) and $t=150$ ms (Deviant Tone).
*   **Voltage Axis (Y-axis):** The vertical axis represents voltage. Specific numerical markers are visible on the left margin, including $-50$ and $30$.
*   **Activity Representation:** The grayscale intensity within the panels represents neural activity. Darker/brighter areas likely correspond to higher or lower voltage states, depending on the specific encoding convention (though this is not explicitly defined for the raw data).
*   **Annotations and Arrows:** Several specific annotations are present, particularly in the lower sections of the panels:
    *   **Arrowed Boxes:** Several boxes are pointed to by arrows, labeled with indices like "$n-1$", "$n-2$", and "$n-3$". These refer to past stimuli whose activity is propagating in delay lines.
    *   **Specific Event Markers:** Arrows point to specific initiation events:
        *   In the **Left Column**: "$n$" and "$n+1$" arrowed boxes point to the initiation of a new memory trace following synchronous activity related to predictions $n$ and $n+1$ ("p1" and "p2" arrows).
        *   In the **Right Column**: The "$n+1$" arrowed box shows the initiation of a new memory trace following synchronous activity related to prediction errors from the deviant stimulus.
    *   **Layer-Specific Markers (Described in Caption):** The caption references specific layers and associated arrows:
        *   "Black arrows" indicate depolarization in the predictive layer.
        *   The "$e2$" arrow indicates hyperpolarization in the prediction error layer.
        *   The "$e1$" and "$e3$" arrows denote specific depolarization events in the prediction error layer.
        *   The "$p3$" arrow indicates transmission to the predictive population.

### 3. Labels, Keys & Legends
**Axis/Scale Labels:**
*   The vertical axis shows numerical markers: $30$, $10$, and $-50$.
*   The horizontal axis is implicitly time-based, marked by $t=0$ ms and $t=150$ ms.

**Column Labels (Implied):**
*   Left Column: "Subpopulations selective to Tone A"
*   Right Column: "Subpopulations selective to Tone B"

**Internal Annotations (from Caption):**
*   "$n-1$", "$n-2$", "$n-3$": Refer to past stimuli activity propagation.
*   "p1", "p2": Arrows pointing to the initiation of a new memory trace in the left column.
*   "$e1$", "$e2$", "$e3$": Arrows indicating specific activity patterns in the prediction error layer.
*   "p3": Arrow indicating transmission to the predictive population.

### 4. Data Trends & Details
The figure displays dynamic changes over time, corresponding to the presentation of a standard tone ($t=0$ ms) followed by a deviant tone ($t=150$ ms).

*   **Activity Pattern:** The activity appears highly structured, showing bursts and sustained patterns across the time course.
*   **Prediction vs. Deviance:** The caption describes distinct behaviors:
    *   At $t=0$ ms (Standard Tone): Excitation and inhibition cancel out in the prediction error layer ("e1" arrow).
    *   At $t=150$ ms (Deviant Tone): A depolarization in the prediction error population selective to the deviant ("e3" arrow) occurs parallel to hyperpolarization in the predictive population selective to the standard ("e2" arrow). This depolarization then propagates forward ("p3" arrow) and into the memory population.

### 5. Contextual Caption Integration
The figure illustrates a single trial of the oddball paradigm, comparing responses in populations selective to Tone A (Left) and Tone B (Right). The structure separates single-unit voltage (top panel) from population average voltage (bottom panel) for each layer. The annotations detail the propagation of activity through a simulated memory trace, specifically highlighting how prediction errors (e.g., "$e3$") drive the formation of new memory traces following a deviant stimulus, contrasting with the cancellation observed during standard tone presentation ("e1").

3670 • J. Neurosci., March 14, 2012 • 32(11):3665–3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity

> Figure description (generated): This figure displays a schematic representation, likely illustrating signal processing or neural dynamics related to auditory perception, given the context of "the standard tone."

**1. Overall Layout & Structure:**
The figure is structured as a single, large block diagram or schematic visualization. It features an input section on the left feeding into a central processing area, which is represented by a time-series or spectrogram-like visualization.

**2. Visual Components & Symbols:**
*   **Input Section (Left):** On the far left, there are three distinct input lines or arrows originating from a vertical stack of labels: `[3]`, `[2]`, and `[1]`. These inputs feed into the main processing block.
*   **Processing Block (Center):** The core of the figure is a large rectangular area representing the processing mechanism. This block contains a visual representation that resembles a spectrogram or time-frequency plot, characterized by horizontal bands of varying intensity (shades of gray).
    *   This central area is segmented vertically by two prominent, thick black vertical bars. These bars appear to demarcate specific time points or events within the processing window.
    *   Within this central area, there are annotations pointing to specific points in time: `n` and `n+1`. These labels are associated with small, square-like markers or indicators positioned near the vertical bars.
*   **Output/Contextual Elements (Right):** To the right of the main block, there are truncated labels suggesting further context or output stages: `...ox` and `ean`.

**3. Labels, Keys & Legends:**
*   **Top Annotation:** The text fragment visible above the main block reads: "the standard tone".
*   **Input Labels:** The input lines are labeled `[3]`, `[2]`, and `[1]` from top to bottom.
*   **Internal Annotations:** Inside the central block, there are labels `n` and `n+1`, each associated with a small square symbol.
*   **Right-Side Labels:** The right edge shows partial labels: `...ox` and `ean`.

**4. Data Trends & Details:**
The central visualization exhibits horizontal striations or bands of varying gray intensity across the time axis (implied horizontally). The pattern suggests a structured signal, possibly representing frequency modulation or temporal firing patterns. The vertical black bars mark specific moments in time where the signal structure is highlighted or analyzed relative to indices $n$ and $n+1$.

**5. Contextual Caption Integration:**
The labels `[3]`, `[2]`, and `[1]` likely denote different input channels, frequency bands, or levels of processing. The presence of $n$ and $n+1$ strongly suggests a temporal sequence or sequential processing step, consistent with analyzing dynamic auditory events like the "standard tone."

> Figure description (generated): This figure appears to be a visualization, likely a spectrogram or a time-frequency plot, given the axes and grayscale representation.

**1. Overall Layout & Structure:**
The figure consists of a single, large plot area occupying the majority of the visible space. The visualization style is that of a 2D intensity plot, where intensity (represented by grayscale) varies across two dimensions.

**2. Visual Components & Symbols:**
*   **Plot Area:** The main body is a rectangular plot area filled with varying shades of gray.
*   **Axes:** There are visible axes defining the dimensions of the plot. The vertical axis (Y-axis) is labeled with numerical values, and the horizontal axis (X-axis) is also present but less clearly detailed in the provided crop.
*   **Annotations:** Several annotations are placed near the plot area:
    *   A small, stylized box containing the notation $\text{[n+1]}$ is located in the lower right quadrant of the plot area.
    *   Two dashed vertical lines are present, one positioned toward the left side and another closer to the right side of the plot area.
*   **Color/Intensity:** The grayscale intensity varies across the plot. There is a generally uniform, medium-gray background tone, but there are discernible horizontal bands of slightly different intensity. A faint, low-intensity feature appears near the bottom edge of the plot area.

**3. Labels, Keys & Legends:**
*   **Y-Axis Labels (Partial):** Visible numerical labels on the left side include: $300$, $200$, $100$, and $-50$.
*   **X-Axis Labels (Partial):** No clear labels are visible for the horizontal axis in this crop.
*   **External Text/Caption Snippets:** Above the plot, there is text that reads: "the deviant tone".
*   **Internal Notation:** The notation $\text{[n+1]}$ is present near the bottom right.

**4. Data Trends & Details:**
*   The plot exhibits horizontal banding, suggesting periodicity or frequency content across the vertical axis. The intensity appears relatively stable across most of the plot, with some subtle variations in the lower region.
*   The dashed lines demarcate specific regions along the horizontal axis, suggesting critical points or boundaries in the data being displayed.

**5. Contextual Caption Integration:**
The visible text snippet, "the deviant tone," suggests that the data being plotted relates to auditory processing or spectral analysis involving a specific stimulus, likely representing the frequency content over time (or vice versa) of an auditory event. The notation $\text{[n+1]}$ likely refers to a specific time step or iteration within the experimental paradigm.

> Figure description (generated): This figure presents a visualization, likely representing neural activity or connectivity patterns over time/space.

**1. Overall Layout & Structure:**
The figure is composed of two main visual sections stacked vertically, separated by a horizontal line. The upper section is a dense matrix or raster plot, while the lower section appears to be a summary or derived visualization.

**2. Visual Components & Symbols:**
*   **Upper Section (Raster Plot):** This section is a large, rectangular grid structure. The background appears grayscale, suggesting intensity or firing rate. Within this matrix, there are distinct vertical lines of high activity (brighter/darker streaks) corresponding to specific time points or trials.
    *   Two prominent downward-pointing arrows, labeled $\downarrow p1$ and $\downarrow p2$, point down onto the upper matrix, indicating specific events or points of interest.
    *   The structure suggests a time-series representation where the vertical axis likely represents individual units (e.g., neurons) and the horizontal axis represents time or trials.
*   **Lower Section:** This section is separated from the upper plot and contains text labels, suggesting a summary or derived metric related to the activity shown above.

**3. Labels, Keys & Legends:**
*   **Annotations on the Upper Plot:**
    *   $\downarrow p1$: An arrow pointing down onto the upper matrix.
    *   $\downarrow p2$: An arrow pointing down onto the upper matrix, positioned to the right of $\downarrow p1$.
*   **Labels on the Right Side (Partial):** Text fragments are visible along the right edge, including "pourquoi index" and "mean," suggesting metrics derived from the data.
*   **Labels on the Lower Plot:** The lower section contains text fragments, including "mean" and what appears to be a stylized representation of activity or a summary plot below the main matrix.

**4. Data Trends & Details:**
*   **Upper Plot Detail:** The raster plot shows sparse, transient bursts of activity. There are clear vertical alignments of these active streaks corresponding to the locations indicated by $\downarrow p1$ and $\downarrow p2$. The activity appears clustered in specific rows (units) at these marked time points.
*   **Lower Plot Detail:** The lower section shows a more abstract visualization, possibly representing the mean activity or correlation across units.

**5. Contextual Caption Integration:**
The labels $\downarrow p1$ and $\downarrow p2$ mark specific temporal or experimental events that are being highlighted within the neural activity matrix shown in the upper panel. The presence of "mean" and "pourquoi index" suggests that the figure is comparing raw activity (upper panel) with derived statistical measures (lower panel).

> Figure description (generated): This figure presents a two-part visualization, structured vertically, likely representing data or model output related to neural activity.

**1. Overall Layout & Structure:**
The figure is divided into two main horizontal sections, stacked vertically. The upper section appears to be a raster plot or similar time-series visualization, while the lower section is a quantitative plot.

**2. Visual Components & Symbols:**
*   **Upper Section (Raster Plot):** This section is a dense, grayscale matrix. The vertical axis represents discrete units (likely neurons or time bins), and the horizontal axis represents time, though no explicit x-axis labels are visible for this section. The matrix is filled with small, dark vertical marks (spikes or events) against a lighter gray background.
    *   An annotation, $\downarrow \text{p3}$, is placed above the upper plot, pointing down towards a specific vertical line or region within the raster.
*   **Lower Section (Plot):** This section is a standard Cartesian coordinate plot with labeled axes.
    *   The vertical axis (y-axis) is labeled with numerical values: $-50$, $10$, $20$, and $30$ (though the scale seems to be centered around zero, with negative values shown).
    *   The horizontal axis (x-axis) has tick marks and labels, though the full context is truncated.
    *   There are two distinct vertical dashed lines visible in this lower plot, suggesting specific time points or thresholds.
    *   A prominent, sharp, inverted 'V' shaped peak (a distribution or function) is visible in the lower plot, centered near the right dashed line.

**3. Labels, Keys & Legends:**
*   **Annotations:** $\downarrow \text{p3}$ is present above the upper plot.
*   **Y-Axis Labels (Lower Plot):** $-50$, $10$, $20$.
*   **X-Axis Labels (Lower Plot):** Partial labels are visible below the plot, including text fragments like "$\text{p3}$" and other truncated labels.

**4. Data Trends & Details:**
*   **Upper Plot:** The raster plot shows a high density of activity across the displayed time window. The annotation $\downarrow \text{p3}$ points to a specific vertical slice where the activity pattern might be of interest.
*   **Lower Plot:** The plot displays a distribution that peaks sharply near the right dashed line. This peak is highly localized, suggesting a specific event or measurement time point. The overall shape suggests a probability density function or a similar localized measure.

**5. Contextual Caption Integration:**
No external caption text was provided, so no specific contextual interpretation can be made regarding cell types or feedback loops based on external information. The figure visually contrasts a high-density temporal activity map (upper panel) with a localized quantitative measurement (lower panel), linked by the annotation $\text{p3}$.

> Figure description (generated): This figure consists of two stacked panels, presented vertically.

**Panel 1 (Upper Panel):**
This panel displays a grayscale heatmap or raster plot, representing some form of spatio-temporal data. The background is uniformly gray, suggesting a dense matrix or grid structure.
*   **Annotations:** Two downward-pointing arrows are present, labeled $\text{e1}$ and $\text{e2}$.
    *   The arrow labeled $\text{e1}$ points down onto the upper-left quadrant of the heatmap.
    *   The arrow labeled $\text{e2}$ points down onto the upper-right quadrant of the heatmap.
*   **Data Features:** Within the gray field, there are several distinct, thin, horizontal white lines scattered across the central region of the plot. These lines appear to represent specific events or activity spikes occurring at different time points (implied by the horizontal nature) across various spatial locations (implied by the vertical position).

**Panel 2 (Lower Panel):**
This panel is positioned directly beneath the first panel and appears to be a schematic or summary plot, though it is partially obscured.
*   **Structure:** It contains two vertical dashed lines that align roughly beneath the positions where $\text{e1}$ and $\text{e2}$ are indicated in Panel 1.
*   **Labels:** To the right of this panel, there is text that begins with "expi..." and ends with "...mean," suggesting a label related to an exponential decay or mean calculation.

**Overall Structure:**
The figure is divided into two distinct visual sections, with the upper section being a detailed data visualization (heatmap/raster plot) and the lower section providing context or summary information related to the events marked in the upper panel.

> Figure description (generated): This figure consists of two distinct, vertically stacked plots, presented side-by-side in a single composite image.

### 1. Overall Layout & Structure
The figure is divided into two main panels: an upper panel and a lower panel. Both panels appear to be heatmaps or raster plots, characterized by grayscale intensity variations across a two-dimensional space.

### 2. Visual Components & Symbols
**Upper Panel:**
*   This panel is a large, rectangular heatmap. The intensity varies across the plot area, ranging from dark gray/black to light gray/white.
*   A prominent annotation, $\text{e3}$, is placed above the upper right quadrant of this panel, with a downward-pointing arrow originating near the top edge and pointing towards the right side of the heatmap.
*   The horizontal axis (x-axis) is not explicitly labeled with units, but the vertical axis (y-axis) has numerical markings.

**Lower Panel:**
*   This panel is also a heatmap, positioned directly below the upper panel. It shares a similar structure but displays different data patterns.
*   It features several dashed vertical lines, suggesting specific temporal or spatial markers.
*   There is a distinct, localized peak of high intensity (bright white) visible in the lower right quadrant.
*   A small, dark triangular symbol ($\blacktriangle$) is visible in the lower left quadrant.

### 3. Labels, Keys & Legends
**Axes Labels:**
*   The vertical axis (y-axis) is labeled with numerical values: $-50$, $10$, $20$, and $30$. These labels span across both the upper and lower panels, suggesting a shared or related vertical scale.
*   The horizontal axis (x-axis) lacks explicit numerical labels in the visible portion of the figure.

**Annotations:**
*   The label $\text{e3}$ is present in the upper panel.

### 4. Data Trends & Details
**Upper Panel:**
*   The heatmap shows a generally diffuse pattern of activity across the entire plot.
*   A noticeable gradient or concentration of higher intensity (brighter areas) appears to be accumulating along the right edge, particularly as the y-values approach $30$.

**Lower Panel:**
*   The activity pattern is more localized. There are distinct vertical lines marking specific points in the horizontal dimension.
*   The most striking feature is a sharp, high-amplitude peak of activity located near the right side of the plot, corresponding to a specific y-value (around $-50$).
*   The presence of the dashed lines and the peak suggests a time-locked or event-related response being visualized.

### 5. Contextual Caption Integration
No external caption was provided, so no contextual integration can be performed based on the prompt's instructions. The description is strictly limited to the visual elements present in the image itself.


---

## Page 7

the repetition of a five-tone sequence AAAAB, the final B sound
continues to elicit a MMN even though the occurrence of this
sound is perfectly predictable based on the prior occurrence of
four A sounds. In other words, the MMN seems to be “blind” to
the overall sequence, and sensitive primarily to local transition
probabilities, which favor the A3A transition over the A3B
transition. Figure 6 shows the result of the simulation of our
network on this paradigm. A total of 150 sequences of five inputs
with ISI of 150 ms was presented. Seventy percent were AAAAB
sequences, 20% AAAAA, and 10% AAAA (omission of the last
sound, not analyzed here). The SOA between two sequences was
1.2 s. The average response to a frequent sequence is plotted in
Figure 6. Note first that the first element of the sequence is not
predicted. The time elapsed since the last sound is superior to the
span of the delay line. It is consistent with data showing that no
MMN exists on the first element of a sequence or for very long ISI
(Ma¨ntysalo and Na¨a¨ta¨nen, 1987; Cowan et al., 1993). Second, the
final B sound elicits a stronger prediction error (sMMN) than the
previous sounds. This effect arises because (1) the transition
probabilities favor the prediction of an A sound following an A
sound; and (2) the network cannot use the past occurrence of a B
sound to predict a new B sound, because the temporal interval
between them (1200 ms) exceeds the time span of the memory
neurons. Both the increased response to the first sound and the
final MMN tightly reproduced experimental scalp and intracra-
nial recordings (Bekinschtein et al., 2009; Wacongne et al., 2011).

Using a closely related, yet importantly different paradigm,
Sussman et al. (1998) showed that the MMN to the deviant sound
B in circular sequences AAAABAAAAB. . . actually disappears if
the SOA is small (100 ms) and B is presented at regular intervals.
This observation is actually consistent with the model we pro-
pose. If the time between two B sounds is short enough, the

network is able to learn the transition be-
tween two consecutive Bs, and the sMMN
disappears. Our simulated network pre-
dicts that the MMN should reappear as
soon as the temporal prediction of B is
made impossible, either by spacing the B
presentations beyond the capacity of the
memory neurons, or by making B appear
at irregular time intervals.

MMN to omission
One of the most remarkable properties of
the auditory system is that it can generate
evoked responses to an absent but ex-
pected stimulus (Joutsiniemi and Hari,
1989; Raij et al., 1997; Yabe et al., 1997;
Hughes et al., 2001; Todorovic et al., 2011;
Wacongne et al., 2011). We similarly
tested the response of our network to the
omission of an expected sound. We simu-
lated the response of the network to pairs
of AB sounds (ISI  150 ms) separated by
500 ms, and rarely (10% of trials) omitted
the second tone of the pair. We compared
the response to such omissions to the re-
sponse to identical single A tones pre-
sented every 500 ms in a block in which
they were the only stimulus, and therefore
no second stimulus was expected. As
shown in Figure 7, the predictive currents
anticipated the arrival of a second B sound
and therefore produced a response to a nonexisting sound, as
experimentally observed. Indeed, our results are tightly consis-
tent with MEG and intracranial data obtained on a similar pro-
tocol (Hughes et al., 2001; Todorovic et al., 2011).

Interestingly, although this omission response is frequently
called an MMN in the literature, our model proposes that it does
not have exactly the same computational significance as the clas-
sic oddball MMN. In a predictive coding model, the omission
response reflects solely a predictive component and not a predic-
tion error per se (i.e., it does not reflect late, NMDA-dependent,
prediction error currents, but early predictive currents). In the
oddball paradigm, the main origin of the difference is an NMDA-
dependent supragranular current, whereas the model predicts
that the omission response should be resistant to competitive
antagonists of NMDA channels, once the transition probabilities
are learned.

MMN to changes in duration
Until now, we only simulated the onset of the input sounds.
However, in primary auditory cortex, there are also populations
of neurons that respond to sound offset (Volkov and Galazjuk,
1991; Chimoto et al., 2002). In a predictive coding perspective,
the mechanism that we describe should capture not only how the
onset of one sound can be predicted from the onset of another but
also how the offset of one sound can be predicted based on the onset
ofthesamesound.Inthepresentsection,weshowthatthiseffectcan
explain the observation of a MMN to a change in sound duration.

We stimulated our network with sounds of 150 ms duration,
separated by a 300 ms ISI. We now assumed that the neural
population “A” responded to the onset of the stimulus, and the
“B” population to the offset. On a rare 10% of trials, the duration

Figure 4.
Correspondence between the transition statistics of the inputs (left) and the synaptic weights learned by the model
(right).Ineachpanel,thestatisticsaregivenforsimulationswith5,10,20,and30%ofdeviantsoundsBinanoddballparadigm.
Leftcolumn,Conditionalprobabilitiesofreceivingagivensound(AorB)attimet,giventherecenthistoryofpastinputsattimes
t-dt(dtrangingfrom0to400ms).Rightcolumn,Correspondingsynapticweightsinthesimulationattheendoflearning.Thegray
levels indicate the mean synaptic weights between neurons of the recurrent memory network spiking on average at the time dt
after the occurrence of an A or B sound, and the predictive neurons coding for the arrival of an A or B sound.

> Figure caption (from PDF text): Figure 4.
Correspondence between the transition statistics of the inputs (left) and the synaptic weights learned by the model
(right).Ineachpanel,thestatisticsaregivenforsimulationswith5,10,20,and30%ofdeviantsoundsBinanoddballparadigm.
Leftcolumn,Conditionalprobabilitiesofreceivingagivensound(AorB)attimet,giventherecenthistoryofpastinputsattimes
t-dt(dtrangingfrom0to400ms).Rightcolumn,Correspondingsynapticweightsinthesimulationattheendoflearning.Thegray
levels indicate the mean synaptic weights between neurons of the recurrent memory network spiking on average at the time dt
after the occurrence of an A or B sound, and the predictive neurons coding for the arrival of an A or B sound.
> Figure description (generated): This figure, labeled as Figure 4, presents a set of four heatmaps arranged vertically. These panels illustrate the correspondence between transition statistics of inputs and learned synaptic weights in a model, specifically for simulations involving 5%, 10%, 20%, and 30% deviants in an oddball paradigm.

**Overall Layout & Structure:**
The figure consists of four distinct, horizontally oriented heatmaps stacked one above the other. Based on the caption, each panel likely represents a specific condition (e.g., 5%, 10%, 20%, or 30% deviants), and within each panel, there are two conceptual columns: the left column representing "Conditional probabilities of receiving a given sound (A or B) at time $t$, given the recent history of past inputs at times $t-dt$," and the right column representing "Corresponding synaptic weights in the simulation at the end of learning."

**Visual Components & Symbols:**
Each panel is a 2D heatmap where the intensity of gray shading represents the magnitude of the measured statistic (probability or synaptic weight).

*   **Axes:**
    *   The **Y-axis** is labeled with numerical values: 5, 10, 20, and 30. These likely correspond to different time points or states within the network dynamics (as suggested by the caption referring to "time $dt$").
    *   The **X-axis** is labeled with time in milliseconds (ms): 0, 50, 100, 150, 200, 250, 300, 350, and 400. This represents the time lag $dt$.

*   **Color/Shading:** The shading ranges from white (low magnitude) to dark gray/black (high magnitude).

**Data Trends & Details (Panel by Panel):**

1.  **Top Panel:** Shows a pattern of high activity concentrated around $dt=150$ ms to $200$ ms, particularly in the central region of the heatmap.
2.  **Second Panel:** Exhibits a more diffuse pattern compared to the top panel, with noticeable activity centered around $dt=150$ ms and a broader spread of moderate intensity across the time axis.
3.  **Third Panel:** Displays very distinct, high-intensity vertical features (darker columns) centered around $dt=150$ ms and another strong feature towards the right side, likely corresponding to the learned synaptic weights.
4.  **Bottom Panel:** This panel appears largely uniform and light gray, suggesting low or negligible activity/weights across the measured time lags ($dt$).

**Contextual Caption Integration:**
The caption clarifies that:
*   The **Left column** (implied by the structure, though not explicitly separated in these merged heatmaps) shows conditional probabilities.
*   The **Right column** shows corresponding synaptic weights.
*   The gray levels indicate the *mean synaptic weights* between neurons of the recurrent memory network spiking on average at time $dt$ after an A or B sound, and the predictive neurons coding for the arrival of A or B.

In summary, the figure uses four stacked heatmaps to visually compare how input transition statistics evolve over time lags ($dt$) against the learned synaptic weights, across different levels of oddball deviation (5%, 10%, 20%, and 30%).

> Figure caption (from PDF text): Figure 4.
Correspondence between the transition statistics of the inputs (left) and the synaptic weights learned by the model
(right).Ineachpanel,thestatisticsaregivenforsimulationswith5,10,20,and30%ofdeviantsoundsBinanoddballparadigm.
Leftcolumn,Conditionalprobabilitiesofreceivingagivensound(AorB)attimet,giventherecenthistoryofpastinputsattimes
t-dt(dtrangingfrom0to400ms).Rightcolumn,Correspondingsynapticweightsinthesimulationattheendoflearning.Thegray
levels indicate the mean synaptic weights between neurons of the recurrent memory network spiking on average at the time dt
after the occurrence of an A or B sound, and the predictive neurons coding for the arrival of an A or B sound.
> Figure description (generated): This figure, labeled as Figure 4, presents a set of four panels illustrating the correspondence between input transition statistics and learned synaptic weights in a model. The structure is organized into two columns: the left column displays conditional probabilities of receiving a given sound, and the right column shows corresponding synaptic weights. Each panel represents simulations conducted with different percentages of deviant sounds in an oddball paradigm (5%, 10%, 20%, and 30%).

**Overall Layout:**
The figure consists of four distinct plots arranged vertically, suggesting a progression or comparison across different simulation conditions. Each plot is divided conceptually into two halves (left and right), corresponding to the input statistics and synaptic weights, respectively.

**Visual Components & Axes:**
All four panels share a common structure:
*   **Y-axis (Vertical Axis):** Labeled "in simulation," this axis ranges from 0 to 30, marked in increments of 5. This likely represents time or a related metric within the simulation context.
*   **X-axis (Horizontal Axis):** Labeled "dt (ms)," this axis represents time delay in milliseconds. The scale ranges from 0 to 400 ms, with major ticks at 50, 100, 150, 200, 250, 300, 350, and 400 ms.

**Panel-Specific Observations (Reading from Top to Bottom):**

1.  **Top Panel:**
    *   **Left Side (Input Statistics):** Shows a dark, high-intensity block centered around $dt \approx 150$ ms. The intensity gradually decreases towards the edges, suggesting a localized probability distribution.
    *   **Right Side (Synaptic Weights):** Mirrors the left side, displaying a dark, high-intensity block centered around $dt \approx 150$ ms. The gray levels indicate the mean synaptic weights.

2.  **Second Panel:**
    *   **Left Side (Input Statistics):** Shows a lighter, more diffuse distribution compared to the top panel. There are visible gray areas centered around $dt \approx 150$ ms and another lighter area towards the right side, possibly around $dt \approx 350$ ms.
    *   **Right Side (Synaptic Weights):** Corresponds to the left side, showing lighter gray areas corresponding to the input distribution.

3.  **Third Panel:**
    *   **Left Side (Input Statistics):** Features a very dark, high-intensity block centered around $dt \approx 150$ ms.
    *   **Right Side (Synaptic Weights):** Shows a dark, high-intensity block centered around $dt \approx 150$ ms, mirroring the left side.

4.  **Bottom Panel:**
    *   **Left Side (Input Statistics):** Appears mostly white/light gray across the entire range, indicating low probability or uniform distribution.
    *   **Right Side (Synaptic Weights):** Shows a distinct, localized gray area appearing towards the right side of the plot, centered around $dt \approx 350$ ms.

**Contextual Interpretation (Based on Caption):**
The caption clarifies that the left column represents "Conditional probabilities of receiving a given sound (A or B) at time $t$, given the recent history of past inputs at times $t-dt$ (ranging from 0 to 400ms)." The right column represents "Corresponding synaptic weights in the simulation at the end of learning." The gray levels denote the mean synaptic weights between neurons spiking on average at time $dt$ after an A or B sound, and the predictive neurons. The different panels correspond to simulations with 5%, 10%, 20%, and 30% deviant sounds.

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665–3678 • 3671


---

## Page 8

of the sound, that is, the interval between the onset and the offset
of the sound, was changed to 200 ms. We also simulated the
converse situations in which standard sounds were 200 ms long
and deviants, 150 ms long. Results are plotted in Figure 8, in
which we compare the response to two physically identical
sounds (150 ms duration) that act as standards or as deviants.

When the input duration deviates from expectations, the internal
model generates a prediction later than the actual arrival of the
stimulus. The response to the offset is not cancelled and the pre-
diction error is bigger. This prediction error signal is followed by
another component, corresponding to the response to the omis-
sion of the later onset. Together, these responses capture the

Figure 5.
Simulating the MMN in response to an unexpected repetition among alternating stimuli. Left column, Mean response of the model to a frequent AB alternation in a ABABABA. . .
stimulus.Middlecolumn,MeanresponsetotherareAArepetition.Rightcolumn,ThedifferencebetweentherarerepetitionandthefrequentalternationshowsaMMNelicitedbytherepeatedsound
AA. This prediction distinguishes predictive coding models.

> Figure caption (from PDF text): Figure 5.
Simulating the MMN in response to an unexpected repetition among alternating stimuli. Left column, Mean response of the model to a frequent AB alternation in a ABABABA. . .
stimulus.Middlecolumn,MeanresponsetotherareAArepetition.Rightcolumn,ThedifferencebetweentherarerepetitionandthefrequentalternationshowsaMMNelicitedbytherepeatedsound
AA. This prediction distinguishes predictive coding models.
> Figure description (generated): This figure, titled "Figure 5," presents a comparative visualization of neural responses under different stimulus conditions: alternating versus repetition. The figure is structured into three main columns, each containing two stacked plots (upper and lower), resulting in six distinct panels.

### Overall Layout & Structure
The figure is organized into three vertical columns: "alternance" (left), "repetition" (middle), and a third column without an explicit title but showing the difference between the two conditions (right). Each of these columns contains a pair of plots: an upper plot showing synaptic currents and a lower plot showing firing rates.

### Visual Components & Symbols
**Plot Types:** All panels utilize line graphs for synaptic currents (upper plots) and bar/histogram-like representations or low-frequency traces for firing rates (lower plots).

**Color Coding and Line Styles (Synaptic Currents - Upper Plots):**
The legend indicates the following components, which are represented by distinct line styles and colors:
*   **GABA:** Represented by a dashed red line.
*   **AMPA:** Represented by a solid blue line.
*   **NMDA:** Represented by a dashed black line (or potentially a different color/style not fully detailed in the legend snippet, but present as a line).

**Firing Rate Representation (Lower Plots):**
The lower plots show discrete events or averaged rates, represented by vertical bars or spikes.

### Labels, Keys & Legends
**Column Titles:**
*   Left Column: "alternance"
*   Middle Column: "repetition"

**Axis Labels:**
*   Y-axis for upper plots (Synaptic currents): Labeled "Synaptic currents" with numerical scales ranging from 0 to 8 (left column) or 0 to 1.5 (right column).
*   Y-axis for lower plots (Firing rates): Labeled "Rate" with numerical scales ranging from 0 to 30 (left and middle columns) or 0 to 1.5 (right column).
*   X-axis: Not explicitly labeled with units, but represents time progression across the stimuli.

**Legend (Bottom Right):**
The legend identifies the components:
*   GABA (dashed red line)
*   AMPA (solid blue line)
*   NMDA (dashed black line, implied by context/plot structure)

### Data Trends & Details

**Left Column ("alternance"):**
*   **Upper Plot (Synaptic Currents):** Shows responses to a "frequent AB alternation in a ABABABA" stimulus. Multiple peaks are visible across the time axis, corresponding to alternating stimuli presentation. The currents (GABA, AMPA, NMDA) fluctuate rhythmically with the stimulus pattern.
*   **Lower Plot (Rate):** Shows corresponding firing rate activity, exhibiting periodic bursts synchronized with the alternating stimuli.

**Middle Column ("repetition"):**
*   **Upper Plot (Synaptic Currents):** Shows responses to a "rare AA repetition" stimulus. The current traces show distinct patterns, particularly around the time of the repeated stimuli (AA).
*   **Lower Plot (Rate):** Shows firing rate activity, which appears to be significantly different from the alternating pattern, showing distinct responses during the repetition event.

**Right Column (Difference):**
*   **Upper Plot (Synaptic Currents Difference):** This plot shows the difference between the response to rare repetition and frequent alternation. It displays a clear, transient peak in synaptic current activity (around 0.3 on the x-axis) that is significantly higher than baseline, indicating a specific MMN (Mismatch Negativity) effect elicited by the repetition.
*   **Lower Plot (Rate Difference):** This plot shows the difference in firing rates, which appears relatively flat or low compared to the synaptic current difference.

### Contextual Caption Integration
The caption clarifies that:
1.  The left column simulates the model's response to a **frequent AB alternation** (ABABABA).
2.  The middle column simulates the model's response to **rare AA repetition**.
3.  The right column illustrates the **difference** between these two conditions, demonstrating an MMN elicited by the repeated sound AA. This difference is stated to distinguish predictive coding models.

Figure 6.
Simulating the lack of sensitivity of the MMN to global regularities that cannot be captured by local transition statistics. Left column, Mean response to a frequent AAAAB stimulus.
Middle column, Mean response to the rare AAAAA stimulus. Right column, Difference between rare and frequent sequences. An MMN continues to be elicited by the final B sound of the standard
AAAAB stimulus. Although the global sequence AAAAB is frequent and predictable, the MMN effect is driven primarily by the rarity of the local transition A3B.

> Figure caption (from PDF text): Figure 6.
Simulating the lack of sensitivity of the MMN to global regularities that cannot be captured by local transition statistics. Left column, Mean response to a frequent AAAAB stimulus.
Middle column, Mean response to the rare AAAAA stimulus. Right column, Difference between rare and frequent sequences. An MMN continues to be elicited by the final B sound of the standard
AAAAB stimulus. Although the global sequence AAAAB is frequent and predictable, the MMN effect is driven primarily by the rarity of the local transition A3B.
> Figure description (generated): This figure, titled "standard," presents a set of time-series plots arranged in two rows and three columns, illustrating neural responses to different auditory stimuli. The overall structure is a $2 \times 3$ grid of plots, with each plot containing two distinct sub-panels stacked vertically.

### Overall Layout and Structure
The figure is composed of six main plotting areas, organized into two rows. Each row contains three columns, corresponding to different stimulus conditions:
*   **Left Column:** Mean response to a frequent AAAAB stimulus.
*   **Middle Column:** Mean response to the rare AAAAA stimulus.
*   **Right Column:** Difference between rare and frequent sequences.

Within each of the six main areas, there are two stacked plots: an upper plot and a lower plot.

### Visual Components & Symbols
The plots use line graphs to represent neural activity over time (implied by the horizontal axis, though not explicitly labeled with units).

**Upper Plots:**
*   These plots show continuous or pulsed activity represented by lines.
*   There are multiple colored lines: **Red dashed lines**, **Blue solid lines**, and a **Black line** (which appears to be the baseline or zero activity).
*   The y-axis for these plots is labeled "Synaptic currents" and ranges from 0 to 6.

**Lower Plots:**
*   These plots show discrete, pulsed activity represented by vertical bars (spikes or bursts).
*   The y-axis for these plots is also labeled "Synaptic currents" and ranges from 0 to 30.
*   There are distinct vertical bars colored **Red** and **Blue**.

### Labels, Keys & Legends
*   **Title:** "standard" is centered above the entire figure.
*   **Y-Axis Labels (Upper Plots):** "Synaptic currents" (ranging 0 to 6).
*   **Y-Axis Labels (Lower Plots):** "Synaptic currents" (ranging 0 to 30).
*   **Column Labels (Inferred from Caption):**
    *   Left Column: Mean response to a frequent AAAAB stimulus.
    *   Middle Column: Mean response to the rare AAAAA stimulus.
    *   Right Column: Difference between rare and frequent sequences.

### Data Trends & Details (Detailed Analysis by Panel)

**Row 1 (Upper Plots - Synaptic Currents 0-6):**
*   **Left Panel (Frequent AAAAB):** Shows multiple peaks. The red dashed lines exhibit several distinct, transient increases in synaptic current, peaking around 2 to 4 units. The blue solid line shows a lower baseline activity.
*   **Middle Panel (Rare AAAAA):** Shows similar transient peaks in the red dashed lines, but potentially with different temporal characteristics compared to the left panel.
*   **Right Panel (Difference):** Shows a pattern where the red dashed lines and blue solid lines show distinct, often synchronized peaks, indicating differential activity between the rare and frequent stimuli.

**Row 2 (Lower Plots - Synaptic Currents 0-30):**
*   **Left Panel (Frequent AAAAB):** Displays numerous, sharp vertical red bars distributed across the time axis, indicating frequent bursts of activity. There are also some blue pulses visible.
*   **Middle Panel (Rare AAAAA):** Shows a pattern of red bars, which appear less frequent or perhaps more clustered compared to the left panel.
*   **Right Panel (Difference):** This plot shows a clear difference in the timing and magnitude of the pulses. Notably, there is a prominent blue pulse near the right edge that appears significantly larger than the red pulses in the corresponding location, consistent with the caption stating an MMN effect driven by local transition rarity.

### Contextual Caption Integration
The caption explains the interpretation of these visual elements:
*   The **Left Column** represents the response to the frequent sequence (AAAAB).
*   The **Middle Column** represents the response to the rare sequence (AAAAA).
*   The **Right Column** shows the difference between these two responses.
*   The caption specifically notes that an MMN (Mismatch Negativity) effect is elicited by the final 'B' sound of the standard AAAAB stimulus, and that this MMN effect is driven primarily by the rarity of the local transition **A3B**, despite the global sequence AAAAB being frequent. This suggests that the differences observed in the right column plots reflect this local transition sensitivity.

> Figure caption (from PDF text): Figure 6.
Simulating the lack of sensitivity of the MMN to global regularities that cannot be captured by local transition statistics. Left column, Mean response to a frequent AAAAB stimulus.
Middle column, Mean response to the rare AAAAA stimulus. Right column, Difference between rare and frequent sequences. An MMN continues to be elicited by the final B sound of the standard
AAAAB stimulus. Although the global sequence AAAAB is frequent and predictable, the MMN effect is driven primarily by the rarity of the local transition A3B.
> Figure description (generated): This figure, titled "deviant," consists of two distinct sets of plots stacked vertically. Each set appears to be a time-series or response plot, likely representing neural activity related to auditory processing.

### Overall Layout & Structure
The figure is divided into two main horizontal sections, each containing three vertically aligned plots. The top section shows a set of three related plots, and the bottom section also shows a set of three related plots.

### Visual Components & Symbols
All plots utilize a similar structure: a horizontal baseline with multiple superimposed lines representing different responses.

**General Plot Elements:**
*   **Horizontal Lines/Baseline:** A dark, solid horizontal line runs across the bottom of each plot area, likely representing a baseline or zero response level.
*   **Data Traces:** Multiple colored lines are plotted above this baseline:
    *   A **blue line** (often appearing as a thicker, smoother trace) is present in all plots.
    *   A **red line** (often appearing as a thinner, more spiky trace) is present in all plots.
    *   A **dashed black line** is visible in the top row of plots, particularly prominent in the middle and right panels.

**Top Panel (First Set of Plots):**
This panel contains three plots arranged horizontally: Left, Middle, and Right.

1.  **Top-Left Plot:** Shows a baseline with superimposed blue and red traces, along with the dashed black line. The activity appears relatively low overall compared to the middle plot.
2.  **Top-Middle Plot:** Shows a more pronounced activity pattern, characterized by distinct peaks in the red and dashed black traces.
3.  **Top-Right Plot:** Shows a pattern similar to the top-middle plot, but potentially with different relative amplitudes or temporal characteristics.

**Bottom Panel (Second Set of Plots):**
This panel also contains three plots arranged horizontally: Left, Middle, and Right.

1.  **Bottom-Left Plot:** Shows a pattern of activity similar to the top row, with distinct peaks in the red trace.
2.  **Bottom-Middle Plot:** Displays highly prominent, sharp peaks in both the red and dashed black traces.
3.  **Bottom-Right Plot:** Shows a pattern of activity, again featuring distinct peaks, though perhaps less intense than the bottom-middle plot.

### Labels, Keys & Legends
No explicit axis labels (e.g., time in ms or response magnitude) are visible on the plots themselves, nor is there a formal legend defining what the blue, red, or dashed lines represent within the image frame.

### Data Trends & Details (Inferred from Caption)
The provided caption clarifies the context of these plots:

*   **Top Row (Left Column):** Represents the "Mean response to a frequent AAAAB stimulus."
*   **Top Row (Middle Column):** Represents the "Mean response to the rare AAAAA stimulus."
*   **Top Row (Right Column):** Represents the "Difference between rare and frequent sequences."
*   The caption further explains that in the top-right plot, "An MMN continues to be elicited by the final B sound of the standard AAAAB stimulus. Although the global sequence AAAAB is frequent and predictable, the MMN effect is driven primarily by the rarity of the local transition A3B."

The bottom row likely corresponds to a different experimental condition or analysis, though the caption does not explicitly label the bottom plots.

In summary, the figure presents a comparative visualization of neural responses (likely MMN related) across different stimulus conditions—frequent vs. rare sequences, and the difference between them—using time-series plots featuring blue, red, and dashed black traces.

> Figure caption (from PDF text): Figure 6.
Simulating the lack of sensitivity of the MMN to global regularities that cannot be captured by local transition statistics. Left column, Mean response to a frequent AAAAB stimulus.
Middle column, Mean response to the rare AAAAA stimulus. Right column, Difference between rare and frequent sequences. An MMN continues to be elicited by the final B sound of the standard
AAAAB stimulus. Although the global sequence AAAAB is frequent and predictable, the MMN effect is driven primarily by the rarity of the local transition A3B.
> Figure description (generated): This figure, labeled as Figure 6, presents a set of three time-series plots arranged horizontally, comparing different stimulus conditions related to the MMN (Mismatch Negativity).

**1. Overall Layout & Structure:**
The figure consists of three distinct plots arranged side-by-side in a single row. Each plot shares the same horizontal axis range (from 0 to 1) and has a vertical y-axis ranging from -10 to 1 on the left plot, and from -10 to 1 on the other two plots. The vertical lines visible across all three panels appear to represent discrete time points or stimulus boundaries, marked by short black vertical ticks.

**2. Visual Components & Symbols:**
*   **Plots:** Each panel displays a fluctuating line graph representing a mean response over time (x-axis).
*   **Y-Axis:** The vertical axis represents the response magnitude, scaled from -10 to 1.
*   **X-Axis:** The horizontal axis represents time, scaled from 0 to 1.
*   **Lines/Curves:** The data is represented by continuous, fluctuating green lines.

**3. Labels, Keys & Legends:**
No explicit legends or titles are present within the plot area itself, but the caption identifies the content of each column:
*   **Left Column:** Mean response to a frequent AAAAB stimulus.
*   **Middle Column:** Mean response to the rare AAAAA stimulus.
*   **Right Column:** Difference between rare and frequent sequences.

**4. Data Trends & Details (Panel-by-Panel Analysis):**

*   **Left Plot (Frequent AAAAB Stimulus):**
    *   The response hovers near zero for most of the duration (0 to approximately 0.8).
    *   A noticeable dip occurs towards the end of the sequence (around $x \approx 0.8$ to $1.0$), dropping significantly below zero, reaching approximately -5 or lower before recovering slightly.
    *   The overall trend shows a small, late-stage deviation from baseline.

*   **Middle Plot (Rare AAAAA Stimulus):**
    *   The response remains relatively close to zero across the entire time course (0 to 1).
    *   There are minor fluctuations, but no large, sustained deviation is visible compared to the left plot.

*   **Right Plot (Difference between Rare and Frequent Sequences):**
    *   This plot shows the difference in response. It mirrors the pattern seen in the left plot, indicating that the deviation observed in the frequent stimulus (Left Plot) is being isolated here.
    *   The response remains near zero for most of the duration.
    *   A clear, negative deflection is visible towards the end of the sequence (around $x \approx 0.8$ to $1.0$), mirroring the dip in the left plot, suggesting that this late-stage effect is what drives the MMN.

**5. Contextual Caption Integration:**
The caption explains that the figure illustrates the lack of sensitivity of MMN to global regularities not captured by local transition statistics. Specifically:
*   The **Left Column** shows the response to a frequent sequence (AAAAB).
*   The **Middle Column** shows the response to a rare sequence (AAAAA).
*   The **Right Column** isolates the difference.
*   The caption notes that an MMN effect *is* elicited by the final 'B' sound of the standard AAAAB stimulus, even though the global sequence is predictable. This effect is attributed primarily to the rarity of the local transition $\text{A}^3\text{B}$.

3672 • J. Neurosci., March 14, 2012 • 32(11):3665–3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity


---

## Page 9

experimentally observed MMN to duration deviants (Jacobsen
and Schro¨ger, 2003).

Note that, in our model, the change in duration is formally
equivalent to a change in ISI: predictions that are focused in time
fail to cancel incoming inputs that are shifted in time. Therefore,
the model also reproduces the experimentally observed MMN to
ISI deviants (Ford and Hillyard, 1981; Nordby et al., 1988).

Prediction versus habituation: an experimental test of
the model
We have shown that a model exclusively based on predictive
coding principles can explain, on a parsimonious basis, the major
properties of the experimentally observed MMN. However, this
is not the only theory proposed in the literature. May and Tiitinen
(2010) defend the theory that MMN would only be the result of

Figure7.
SimulatingtheMMNtotheomissionofanexpectedsound.Firstcolumn,MeanresponsetoafrequentABpair.ThenetworklearnsthepredictablelocaltransitionA3B,whichresults
inareducedresponsetothepredictableBsound(seearrow).Secondcolumn,MeanresponsetoarareAsoundpresentedinisolationinthesamecontext.Thenetworkgeneratesaresponsetothe
omissionoftheexpectedsoundB(arrow).Thirdcolumn,ResponsetothesameisolatedsoundA,inadifferentcontextwhereitisthefrequentstimulus.Althoughthestimulusisphysicallyidentical
tothesecondcolumn,thepredictiveresponsetotheomittedBsoundisnolongerseen.Fourthcolumn,Differencebetweenthesecondandthirdcolumns,isolatingthesimulatedMMNtoomission.

Figure 8.
Simulating the MMN to a duration deviant. Blue and red now represent subpopulations selectively responsive, respectively, to sound onset and offset. Left column, Response to a
frequent150-ms-longsound.Middlecolumn,Responsetothesamephysical150mssoundwhenitservesastheraredeviantinanoddballparadigmwherethefrequentsoundis200mslong.Right
column, Difference between these two responses, isolating the MMN evoked by an unexpected change in duration.

> Figure caption (from PDF text): Figure 8.
Simulating the MMN to a duration deviant. Blue and red now represent subpopulations selectively responsive, respectively, to sound onset and offset. Left column, Response to a
frequent150-ms-longsound.Middlecolumn,Responsetothesamephysical150mssoundwhenitservesastheraredeviantinanoddballparadigmwherethefrequentsoundis200mslong.Right
column, Difference between these two responses, isolating the MMN evoked by an unexpected change in duration.
> Figure description (generated): This figure, labeled Figure 8, presents a set of time-series plots illustrating the simulation of the MMN (Mismatch Negativity) response to a duration deviant. The figure is organized into three main columns, each containing two subplots (one upper and one lower), resulting in a $3 \times 2$ grid of plots, though the bottom row is partially visible/cropped.

### Overall Layout & Structure
The figure consists of three vertical columns, representing different experimental conditions:
1. **Left Column:** Response to a frequent 150-ms-long sound.
2. **Middle Column:** Response to the same physical 150ms sound when it serves as a rare deviant in an oddball paradigm (where the frequent sound is 200ms long).
3. **Right Column:** The difference between the responses from the left and middle columns, isolating the MMN evoked by an unexpected change in duration.

Each column contains two plots stacked vertically:
*   **Upper Plot:** Shows the neural response (likely firing rate or activity) over time.
*   **Lower Plot:** Shows a corresponding count or histogram, likely representing the number of spikes or events.

### Visual Components & Symbols
**Color Coding:**
*   **Blue lines/bars:** Represent subpopulations selectively responsive to **sound onset**.
*   **Red lines/bars:** Represent subpopulations selectively responsive to **sound offset**.

**Plot Elements:**
*   **Upper Plots (Time Series):** These plots show continuous curves representing the activity over time.
*   **Lower Plots (Counts):** These plots show discrete bars representing counts at specific time points.
*   **Vertical Dashed Lines:** These lines mark critical temporal events, likely the onset and offset of the sounds being analyzed.

### Labels, Keys & Legends
**Axis Labels (Visible):**
*   **Y-axis (Upper Plots):** Labeled "Synaptic currents" (ranging from 0 to 8).
*   **Y-axis (Lower Plots):** Labeled with numerical values, including 0, 15, and 30 (though the scale is not fully consistent across all plots).
*   **X-axis:** Not explicitly labeled with units, but represents time progression.

**Caption Integration (Contextual Explanation):**
The caption clarifies the meaning of the color coding: "Blue and red now represent subpopulations selectively responsive, respectively, to sound onset and offset."

### Data Trends & Details (By Column)

**Left Column: Response to a frequent 150-ms-long sound.**
*   **Upper Plot:** Shows low, baseline activity. There are small peaks corresponding to the onset and offset markers (dashed lines). The blue and red curves remain close to zero.
*   **Lower Plot:** Shows very low counts, with small bars appearing near the onset and offset markers.

**Middle Column: Response to the same physical 150ms sound when it serves as a rare deviant in an oddball paradigm (where the frequent sound is 200ms long).**
*   **Upper Plot:** Shows a more pronounced response compared to the left column. There are clear, distinct peaks in both blue (onset) and red (offset) activity coinciding with the sound events. The peak heights are notably higher than in the left column, particularly around the onset marker.
*   **Lower Plot:** Shows higher counts than in the left column, with distinct bars appearing at the onset and offset markers.

**Right Column: Difference between these two responses, isolating the MMN evoked by an unexpected change in duration.**
*   **Upper Plot:** This plot shows the difference (Middle Column response minus Left Column response). It exhibits clear, transient peaks corresponding to the onset and offset markers. The blue and red curves show significant positive deviations from zero, indicating a robust MMN-like response isolated by subtraction.
*   **Lower Plot:** Shows the corresponding difference in counts, with distinct bars appearing at the onset and offset markers, reflecting the isolated MMN activity.

*(Note: The bottom row of plots is present but too cropped to provide a detailed analysis.)*

> Figure caption (from PDF text): Figure 8.
Simulating the MMN to a duration deviant. Blue and red now represent subpopulations selectively responsive, respectively, to sound onset and offset. Left column, Response to a
frequent150-ms-longsound.Middlecolumn,Responsetothesamephysical150mssoundwhenitservesastheraredeviantinanoddballparadigmwherethefrequentsoundis200mslong.Right
column, Difference between these two responses, isolating the MMN evoked by an unexpected change in duration.
> Figure description (generated): This figure, labeled as Figure 8, presents a set of time-series plots illustrating the neural response to different auditory stimuli. The figure is organized into two main rows, each containing three distinct columns of plots, suggesting a comparison across different experimental conditions.

### Overall Layout and Structure
The figure is structured as a $2 \times 3$ grid of plots. Each row appears to represent a different experimental context, and the three columns within each row compare responses under specific conditions.

### Visual Components & Data Trends (Row 1)
The top row consists of three plots, all sharing a similar structure:

*   **Y-Axis:** The vertical axis is labeled with numerical values ranging from approximately -1 to 1 (or slightly beyond).
*   **X-Axis:** The horizontal axis represents time, though specific labels are not visible in the cropped view.
*   **Plot Content:** Each plot displays time-series data, likely representing neural activity (e.g., firing rate or voltage).
    *   **Plot 1 (Left Column):** Shows a relatively flat baseline response near zero, with minor fluctuations. Two vertical dashed lines mark specific time points of interest.
    *   **Plot 2 (Middle Column):** Shows a response that is generally near zero, but exhibits a distinct transient increase in activity centered around the time marked by the dashed lines.
    *   **Plot 3 (Right Column):** Shows a response that is generally near zero, but exhibits a clear, transient peak of activity (a positive deflection) occurring after the stimulus presentation time points indicated in the other plots.

### Visual Components & Data Trends (Row 2)
The bottom row also consists of three plots, maintaining the $Y$-axis scale (ranging from approximately -5 to 1) and time-series format.

*   **Y-Axis:** The vertical axis is labeled with numerical values ranging from -5 to 1.
*   **X-Axis:** The horizontal axis represents time, with a visible label "Time (s)" at the bottom center.
*   **Plot Content:**
    *   **Plot 1 (Left Column):** Shows a baseline response near zero, with minor fluctuations. Two vertical dashed lines mark specific time points.
    *   **Plot 2 (Middle Column):** Shows a response that is generally near zero, but exhibits a clear, transient increase in activity (a positive deflection) centered around the time marked by the dashed lines.
    *   **Plot 3 (Right Column):** Shows a response that is generally near zero, but exhibits a clear, transient peak of activity (a positive deflection) occurring after the stimulus presentation time points.

### Contextual Caption Integration
The provided caption explains the experimental context for these plots:

*   **Color Coding:** "Blue and red now represent subpopulations selectively responsive, respectively, to sound onset and offset." (This implies that the lines/traces in the plots likely represent these two subpopulations, although specific color coding is not discernible without higher resolution or a legend.)
*   **Column Interpretation:**
    *   **Left Column:** "Response to a frequent 150-ms-long sound."
    *   **Middle Column:** "Response to the same physical 150-ms sound when it serves as the rare deviant in a oddball paradigm where the frequent sound is 200ms long."
    *   **Right Column:** "Difference between these two responses, isolating the MMN evoked by an unexpected change in duration."

In summary, the figure visually compares neural responses (likely MMN-related activity) across three conditions: response to a frequent sound, response to the same sound when it is an unexpected deviant in an oddball paradigm, and the difference isolating the MMN effect. The plots display time-locked activity traces for these conditions.

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665–3678 • 3673

> Figure description (generated): This figure consists of two separate plots stacked vertically, presented side-by-side in a manner that suggests they might be related conditions or comparisons. Both plots share the same general structure: a set of overlaid line graphs against a shared y-axis scale, with vertical black lines superimposed on the x-axis.

### Overall Layout & Structure
The figure is composed of two distinct panels, stacked vertically. Both panels are line graphs displaying time-series data (implied by the nature of synaptic current plots) against an unspecified horizontal axis, which is segmented by vertical black lines.

### Visual Components & Symbols
**Graphs:** Each panel contains multiple overlaid line graphs, suggesting different conditions or types of synaptic currents.
*   **Line Styles/Colors:** There are at least three distinct line types visible in each panel:
    *   A **solid red line** (or a set of closely related red lines).
    *   A **dashed blue line**.
    *   A **solid black/dark line** (often near the baseline).
*   **Vertical Markers:** Both panels feature several thin, vertical black lines distributed across the horizontal axis. These likely denote specific time points or experimental events.
*   **Baseline/Zero Line:** A horizontal line is present at the value '0' on the y-axis in both plots.

### Labels, Keys & Legends
**Title:** The title above the top panel reads: "Rule : AB".

**Y-Axis Labels (Both Panels):**
The vertical axis is labeled: "rate synaptic currents". The scale ranges from 0 to 6 (or higher, depending on the panel).

**X-Axis Labels:**
The horizontal axis does not have explicit numerical labels, but the vertical black lines segment the time course.

**Panel-Specific Annotations:**
*   **Top Panel (Rule : AB):** The y-axis scale ranges from 0 to 6.
*   **Bottom Panel:** The y-axis scale ranges from 0 to 6, and there is an additional label below the main plot area: "40" followed by a smaller scale indicator (likely representing a secondary or related measurement, though its exact meaning is unclear without context).

### Data Trends & Details (Detailed Analysis)

**Top Panel (Rule : AB):**
*   **Red Line:** Shows a sharp, transient peak around the first vertical marker, reaching approximately 4.5 units, followed by a smaller subsequent peak near the third marker, reaching around 2 units.
*   **Dashed Blue Line:** Shows a moderate initial rise, peaking around 3 units near the first marker, and then exhibits smaller fluctuations.
*   **Baseline/Black Line:** Remains close to or at 0 for most of the duration.
*   **Vertical Markers:** The peaks in the red and blue lines are clearly aligned with specific vertical markers.

**Bottom Panel:**
*   **Red Line:** Exhibits a very sharp, high peak near the first vertical marker, reaching close to 6 units. It then shows a smaller subsequent transient peak.
*   **Dashed Blue Line:** Shows a clear, sustained rise and peak around the second vertical marker, reaching approximately 5 units.
*   **Baseline/Black Line:** Remains near the zero line.
*   **Secondary Scale (Bottom):** Below the main plot area, there is a secondary scale labeled "40" with associated bars/markers that appear to correspond temporally to the main plot events, suggesting a secondary measurement or count rate.

In summary, the figure compares synaptic current dynamics under two conditions (implied by the panel separation), showing distinct temporal patterns of activation for different current types (red vs. blue lines) relative to specific experimental time points marked by vertical lines.

> Figure description (generated): This figure consists of two distinct panels, stacked vertically, both appearing to be line graphs or histograms displaying data related to a process labeled "Rule: AB" at the top.

### Overall Layout & Structure
The figure is divided into two main sub-panels, one above the other. Each panel contains multiple overlaid plots, suggesting a comparison of different data distributions or time courses under the specified rule.

### Visual Components & Symbols
Both panels feature multiple lines plotted against an implied horizontal axis (likely representing time or some continuous variable) and a vertical axis (representing magnitude or frequency).

**Common Elements in Both Panels:**
*   **Vertical Dashed Line:** A prominent vertical dashed line is present in both panels, marking a specific point on the horizontal axis.
*   **Horizontal Baseline:** A solid black line appears near the bottom of both plots, likely representing a baseline or zero value.
*   **Multiple Curves/Histograms:** Several colored lines and shaded areas are present, indicating different data sets.

**Top Panel Details:**
*   This panel contains at least three distinct plotted elements:
    1.  A **red dashed line** showing a sharp, high peak immediately preceding the vertical dashed line, followed by a decay.
    2.  A **blue solid line** showing a lower, broader peak centered near or slightly after the vertical dashed line.
    3.  A **blue shaded area/curve** that overlaps with the blue solid line, showing a distribution shape.
*   The overall appearance suggests comparisons of activity profiles (e.g., firing rates or concentration changes) across different conditions.

**Bottom Panel Details:**
*   This panel also contains multiple plotted elements:
    1.  A **red solid line** showing a very sharp, high peak immediately preceding the vertical dashed line.
    2.  A **blue dotted/dashed line** showing a broader, lower peak following the vertical dashed line.
    3.  A **blue solid line** showing a lower, more sustained activity level.
    4.  A **red histogram-like bar** located significantly to the left of the vertical dashed line, indicating a distinct event or distribution prior to the marked point.

### Labels, Keys & Legends
*   **Title:** The text "Rule: AB" is positioned above the entire figure, serving as a general title or condition identifier.
*   **Axes Labels:** No explicit axis labels (e.g., "Time," "Rate") are legible in the provided image crop, though the structure strongly implies quantitative axes.
*   **Color Coding:** Red and Blue are used to distinguish different data traces across both panels.

### Data Trends & Details
**Top Panel:**
*   The red dashed line exhibits a rapid, high-amplitude transient event occurring just before the vertical marker.
*   The blue traces show a more sustained, lower-amplitude activity profile following the vertical marker.

**Bottom Panel:**
*   The red solid line shows a very sharp, high-amplitude transient event immediately preceding the vertical marker.
*   The blue dotted/dashed line shows a broader, lower-amplitude response following the vertical marker.
*   The presence of the distinct red bar on the left side suggests a pre-stimulus or baseline event that differs significantly from the activity shown in the top panel.

In summary, the figure presents a comparative analysis across two scenarios (top vs. bottom), likely illustrating temporal dynamics or probability distributions associated with a specific rule ("Rule: AB"), using overlaid line plots to contrast different behavioral or physiological responses (represented by red vs. blue traces) relative to a critical time point marked by the vertical dashed line.

> Figure description (generated): This figure consists of two distinct plots, stacked vertically, labeled implicitly as Panel A and a subsequent panel (which we will refer to as the lower plot). Both plots appear to be time-series graphs, likely representing neural activity or some form of dynamic measurement.

### Overall Layout & Structure
The figure is composed of two separate, vertically aligned line graphs. Each graph has a shared structure: a horizontal axis (implied time or some continuous variable) and a vertical axis representing magnitude.

### Visual Components & Symbols
**Axes:**
*   Both plots feature a vertical axis (Y-axis) with numerical markings, though the specific scale is partially obscured or truncated. The right side of both plots shows a Y-axis labeled with values like '1' and '0'.
*   Both plots feature a horizontal axis (X-axis) which is not explicitly labeled with units but represents the progression of the measured variable.

**Lines and Markers:**
Each plot contains multiple lines, distinguished by color and line style:
1.  **Solid Black Line:** A baseline or reference trace, appearing relatively flat across the visible range in both plots.
2.  **Dashed Red Line:** A fluctuating trace, showing a peak response in both plots.
3.  **Solid Blue Line:** Another fluctuating trace, generally lower than the dashed red line in both plots.
4.  **Solid Red Line (Spike/Bar):** A sharp, transient vertical spike or bar representing a discrete event.

**Annotations:**
*   Both plots feature thin, vertical dashed lines positioned above the main traces. These likely mark specific time points or events of interest.

### Data Trends & Details (Panel A - Upper Plot)
*   **Y-Axis:** Marked with '1' and '0' on the right side.
*   **X-Axis:** Unlabeled, representing progression.
*   **Trends:**
    *   The **Dashed Red Line** shows a clear, sharp peak response occurring shortly after the first vertical dashed line. This peak reaches a high value (approaching or exceeding 1).
    *   The **Solid Blue Line** remains relatively low, showing a slight elevation concurrent with the red peak but remaining significantly below it.
    *   The **Solid Red Spike** occurs slightly later than the peak of the dashed red line, showing a very sharp, transient increase.
    *   The **Solid Black Line** remains near the baseline (near 0).

### Data Trends & Details (Lower Plot)
*   **Y-Axis:** Marked with '1' and '0' on the right side.
*   **X-Axis:** Unlabeled, representing progression.
*   **Trends:**
    *   The **Dashed Red Line** shows a prominent, sharp peak response occurring near the first vertical dashed line.
    *   The **Solid Blue Line** shows a response that is slightly elevated compared to the upper plot's blue line, though still lower than the red peak.
    *   The **Solid Red Spike** is present, appearing slightly later than the main red peak.
    *   The **Solid Black Line** remains near the baseline.

### Contextual Caption Integration
The figure is titled "Rule 7.A". While no specific legend or detailed axis labels are provided beyond the numerical markers (0, 1), the structure strongly suggests a comparison of dynamic responses across two conditions or time points (Upper Plot vs. Lower Plot) under the context defined by "Rule 7.A." The distinct lines likely represent different measured variables (e.g., firing rate, calcium transients) or different components of a neural model being tested against the rule.

> Figure description (generated): This figure consists of two separate plots, labeled implicitly as Panel A and Panel B based on the visible text fragments. Both panels appear to be time-series plots displaying activity over a normalized time course (x-axis).

### Overall Layout & Structure
The figure is composed of two vertically stacked plots. Both plots share a similar structure: they are line graphs with defined axes, displaying multiple traces of activity.

### Panel A Description (Top Plot)
**Axes:**
*   **Y-axis:** Labeled with numerical values ranging from -5 to 1.5, marked in increments of 0.5 (i.e., -5, -2.5, 0, 0.5, 1.0, 1.5).
*   **X-axis:** Labeled with numerical values ranging from 0 to 0.5, marked in increments of 0.1 (i.e., 0, 0.1, 0.2, ..., 0.5).

**Visual Components & Data Trends:**
The plot contains several distinct traces:
1.  **Solid Black Line (Baseline/Reference):** This line hovers very close to the $y=0$ level across the entire time course, representing a baseline or control activity.
2.  **Dashed Black Line:** This line also hovers near $y=0$, slightly fluctuating around the baseline.
3.  **Green Trace (Activity):** This trace shows a clear, transient increase in activity. It remains near zero until approximately $x=0.15$. Between $x \approx 0.2$ and $x \approx 0.35$, the activity rises sharply, peaking around $y=0.7$ to $y=1.0$. Following the peak, the activity decays back towards zero by $x \approx 0.45$.
4.  **Vertical Black Lines (Markers):** There are several vertical black lines superimposed on the plot, indicating specific time points. These markers appear at $x \approx 0.1$, $x \approx 0.2$, and $x \approx 0.3$.

### Panel B Description (Bottom Plot)
**Axes:**
*   **Y-axis:** Labeled with numerical values ranging from -5 to 1.5, marked in increments of 0.5 (i.e., -5, -2.5, 0, 0.5, 1.0, 1.5).
*   **X-axis:** Labeled with numerical values ranging from 0 to 0.5, marked in increments of 0.1 (i.e., 0, 0.1, 0.2, ..., 0.5).

**Visual Components & Data Trends:**
This plot also contains multiple traces and vertical markers:
1.  **Solid Black Line (Baseline/Reference):** This line hovers very close to the $y=0$ level.
2.  **Dashed Black Line:** This line also hovers near $y=0$, showing slight fluctuations.
3.  **Green Trace (Activity):** This trace exhibits a transient increase in activity, similar to Panel A but potentially with different dynamics. It remains near zero until approximately $x=0.15$. Between $x \approx 0.2$ and $x \approx 0.35$, the activity rises, peaking slightly higher than in Panel A (approaching $y=1.5$). The activity then decays back towards zero by $x \approx 0.45$.
4.  **Vertical Black Lines (Markers):** Similar to Panel A, there are vertical black lines indicating specific time points. These markers appear at $x \approx 0.1$, $x \approx 0.2$, and $x \approx 0.3$.

### Labels and Annotations
*   **Top Left:** The text fragment "RuleA RuleAB" is visible, suggesting the panels might correspond to different experimental conditions or rules.
*   **Bottom Right:** The text fragment "RuleB" is visible, suggesting the bottom plot corresponds to a different condition.
*   **Axis Labels:** The axes are labeled with numerical scales as described above, but no explicit variable names (e.g., "Firing Rate," "Voltage") are legible on the axes themselves in the provided crop, only the numerical ticks.


---

## Page 10

synaptic habituation, that is to say, the reduction of the ampli-
tude of EPSPs as a result of repeated stimulation of the same
synapse. Indeed, synaptic adaptation and short-term plasticity
are commonly observed in vivo and in vitro in cortex (for review,
see Calford, 2002), and more specifically in auditory cortex (Con-
don and Weinberger, 1991; Brosch and Schreiner, 2000), and it is
likely that a complete theory of MMN should ultimately take such
effects into account. However, is synaptic habituation sufficient
to explain all MMN findings? In their review of MMN findings,
May and Tiitinen (2010) suggest that all current MMN para-
digms remain compatible with a habituation mechanism and
argue that there is therefore no decisive evidence in favor of pre-
dictive coding models of the MMN. Contrariwise, our model
leads us to propose one such critical test separating the predictive
coding and habituation interpretations.

To provide a direct test of the two models, we decided to
present pairs of closely consecutive sounds AB (200 ms SOA),
separated by a broad temporal interval (	10 s). Occasionally,
instead of the frequent AB pair (70% of trial), a deviant AA pair is
presented in 10% of the trials, in which the same sound is re-
peated twice. The predictions of our model are straightforward:
the first A sound predicts the second B sound in the frequent AB
pair, and a mismatch negativity should therefore be generated
whenever the unexpected A sound is heard instead (i.e., when the
rare AA pair is presented instead of the frequent AB pair). We
confirmed this prediction through simulations (the results are
essentially identical to the alternation case ABABA. . . described
earlier).

The habituation model, however, makes the opposite predic-
tion: due to synaptic habituation, the second A sound in the AA
pair should always elicit a reduced activity compared with the B
sound in the AB pair, which solicits nonhabituated synapses. It
could be argued that some higher-order neurons might habituate
to the presentation of the frequent AB pair as a whole. Indeed, this
is how May and Tiitinen (2010) account for the above-described
alternation paradigm (ABABA. . . ). However, experimentally,
the recovery time of synaptic depression is generally of the order
of a few seconds (Varela et al., 1997; Ulanovsky et al., 2004). Thus,
by making the temporal interval between pairs as long as 10 s, we
should render this putative effect of synaptic habituation at the
level of the whole pair quite negligible, especially compared with
the short-term adaptation to the individual sounds A in the pair
AA, which are only separated by 200 ms. In this case, the habitu-
ation model can only predict a reduced brain response to the
infrequent AA pair (i.e., the converse of a mismatch negativity).

As a further control, we introduced two additional rare devi-
ants, the BB and BA pairs, which were also presented in 10% of
the trials each. These pairs have the same structure as the AA pairs
and AB pairs, but are presented with equal probability. In our
model, as the transition probabilities B3B and B3A are the
same, the predicted evoked responses should be the same. Thus,
our model predicts a lack of any difference here, whereas the
synaptic habituation model again predicts a reduced response to
the repeated pair BB compared with the nonrepeated pair BA.

We recorded MEG signals while five healthy participants were
instructed to listen to these stimuli. Each subject listened to two
blocks of 120 pairs of sounds. The frequencies of the two sounds
were 800 and 1600 Hz, and were counterbalanced between
blocks. Figure 9 shows the results. In every subject, the second
tone of the rare AA pairs elicited a MMN compared with the
frequent AB pairs. The difference between the two conditions was
significant for each individual subject and for both types of sen-
sors (subject 1: Grad, 121–206 ms, p 
 1e-16; Mag, 131–231 ms;

subject 2: Grad, 131–186 ms, p  0.028; Mag, 157–204 ms, p 
0.044; subject 3: Grad, 127–226 ms, p  0.003; Mag, 126–264 ms,
p  0.004; subject 4: Grad, 109–177 ms, p  0.006; Mag, 110–230
ms, p  0.001; subject 5: Grad, 120–164 ms, p  0.04; Mag,
116–260 ms, p  0.01), as well as at the group level (Grad, 108–
232 ms, p 
 1e-16; Mag, 145–193 ms, p 
 1e-16). The topogra-
phy of the effect was similar to the classical MEG–MMN
topography, with bilateral temporal activations.

Our model predicted that no difference should exist between
the two control stimuli BA and BB. Indeed, no significant differ-
ence was observed between the two control stimuli (rare BB and
rare BA pairs, presented with equal probability). In fact, a non-
significant trend existed in the direction opposite to the one pre-
dicted by the synaptic habituation model (greater brain response
to BA). This finding can be explained by the fact that the identity
of the sounds serving as A and B was counterbalanced between
the two halves of the experiment. As a result, the rare BA pair of
the second run was the frequent AB pair of the first run. We
reasoned that the transition that was well learned during the first
block of trials could have continued to prevail in the second
block, especially as the pairs BB and BA were presented for a very
small number of times (12 each), thus largely preventing relearn-
ing of the actual equiprobability of the B3A and B3B transi-
tions. We confirmed this hunch by separately analyzing the first
and second halves of our experiment. When restricted to the first
half, the two control stimuli BA and BB did not present any
identifiable difference, whereas the same two conditions pre-
sented a stronger (yet nonsignificant) difference in the second
half. Note again that the latter difference (stronger response to
BB) was in the direction opposite to that expected from a habit-
uation mechanism.

The experimental data are therefore consistent with the pre-
dictions of our model in great detail and in every single subject.
To explain the data with synaptic habituation, one would have to
postulate the existence of neurons that (1) respond specifically to
the transition between the AB sounds; (2) present significant
habituation after 10 s; and (3) whose habituation to AB pairs is
strong enough to override the countereffect of habituation to the
AA pair for neurons that respond only to frequency A. The latter
assumption is particularly implausible because neurons respon-
sive to A alone are likely to be much more numerous than neu-
rons responsive to the AB pair as a whole, and because their
habituation would be likely to be much stronger, given that the
A–A delay of 200 ms is much shorter than the AB–AB delay of 10 s
or more. Furthermore, the responses to BA and BB pairs provide
no support for a habituation to individual B sounds. We there-
fore conclude that any habituation account of our data seems
highly implausible.

Discussion
In this study, we developed a spiking neuron model of mismatch
negativity, based on a predictive coding approach. We identified
key properties of the mismatch effect and simulated the network
response to a variety of test sequences. In particular, our model
reproduced the known reduction in MMN amplitude when the
frequency of the deviants increases, the MMN to repetition in an
alternate sequence, and the response to the omission of an ex-
pected sound. Without any additional assumption, the model
was able to account for the MMN to a change in stimulus dura-
tion or in interstimulus interval. We proposed a precise cortical
localization of the neuronal populations postulated in the model
and showed that our simulated current sources were consistent
with actual electrophysiological data. We also showed that the

3674 • J. Neurosci., March 14, 2012 • 32(11):3665–3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity


---

## Page 11

model acquired a quantitative synaptic
representation of transition probabilities.
An alternative model hypothesizes that
MMN arises purely from synaptic habitu-
ation. We identified a precise experimen-
tal context where the two models lead to
opposite predictions and showed that
MEG data from human participants fully
support our predictions, with no evidence
of a synaptic habituation effect.

Predictions versus synaptic habituation
In the present study, we showed that a
model based on pure predictive coding,
without any synaptic habituation compo-
nent, could account for a large range of
effects. It is important to note that, even
though the habituation and predictive/
memory accounts of MMN have been
often opposed (Na¨a¨ta¨nen et al., 2005;
Winkler, 2007; May and Tiitinen, 2010),
the two hypotheses are not logically exclu-
sive. It remains possible that the two pro-
cesses concur to the final MMN effect,
possibly in different proportions accord-
ing to the paradigm. However, the conclu-
sions of the MEG experimental test of our
model are fully consistent with a purely
predictive account of MMN and argue
against a strong contribution of habitua-
tion effects.

Other recent studies argue in favor of a
negligible role of habituation in the MMN
effect. Recent human MEEG recordings
indicate that the omission response ob-
served when an expected sound fails to
occurconformstothepredictionsofhierar-
chicalpredictivecodingmodels(Wacongne
et al., 2011). In rodents, Farley et al. (2010)
showed that stimulus-specific adaptation is
indeed observed in auditory cortex but that
itspropertiesdiffersharplyfromthoseofthe
MMN, in terms of sensitivity to NMDA an-
tagonistsorelicitationofanoveltyresponse.
Together, these results provide strong evi-

A

B

C

D

E

F

Figure 9.
Experimental test of the model using magnetoencephalography. A, Experimental design. Each block of trials begins
with10identicalpairsoftones(AfollowedbyB).AandBarepuretonesof50msandfrequency800and1600Hz,counterbalanced
betweenblocksandsubjects.Thesubjectthenlistenedto120pairsoftones:70%offrequentABpairs,and10%ofeachoftherare
pairsAA,BA,andBB.B,Comparisonbetweentherelativeresponseamplitudepredictedbythehabituationmodel,thepredictive
coding model, and the data. In the habituation model (left column), response amplitude is minimal to a repeated tone. In our
predictivecodingmodel(middlecolumn),responseamplitudedependsontransitionprobabilitiesbetween the first and second

> Figure caption (from PDF text): Figure 9.
Experimental test of the model using magnetoencephalography. A, Experimental design. Each block of trials begins
with10identicalpairsoftones(AfollowedbyB).AandBarepuretonesof50msandfrequency800and1600Hz,counterbalanced
betweenblocksandsubjects.Thesubjectthenlistenedto120pairsoftones:70%offrequentABpairs,and10%ofeachoftherare
pairsAA,BA,andBB.B,Comparisonbetweentherelativeresponseamplitudepredictedbythehabituationmodel,thepredictive
coding model, and the data. In the habituation model (left column), response amplitude is minimal to a repeated tone. In our
predictivecodingmodel(middlecolumn),responseamplitudedependsontransitionprobabilitiesbetween the first and second
> Figure description (generated): This figure, labeled Figure 9, presents a comparison between predictions from different models (Habituation and Predictive Coding) and experimental data obtained via magnetoencephalography (MEG). The figure is divided into several panels: a table comparing model predictions and data (top section), and three subsequent panels (C, E, F) showing topographical maps and time-course plots.

### Top Section: Model Comparison Table (Panel B)

This section is a table comparing the predicted relative response amplitudes across three models: "model" (Habituation model), "coding model" (Predictive Coding model), and "data." The rows correspond to different tone sequences: "freq AB," "rare AA," "rare BB," and "rare BA."

**Color Coding:**
*   Blue represents the response for "freq AB."
*   Red represents the response for "rare AA" and "rare BB."
*   Green represents the response for "rare BA."

**Table Structure:**
The table has three columns: `model`, `coding model`, and `data`.

*   **Row 1 (freq AB):** All three columns show a bar graph representation. The bars are blue, indicating a positive response amplitude (indicated by the scale below).
*   **Row 2 (rare AA):** All three columns show a bar graph representation. The bars are red, indicating a positive response amplitude.
*   **Row 3 (rare BB):** All three columns show a bar graph representation. The bars are red, indicating a positive response amplitude.
*   **Row 4 (rare BA):** All three columns show a bar graph representation. The bars are green, indicating a positive response amplitude.

**Scale Bar:**
Below the table is a horizontal color bar labeled with numerical values: $\text{-3. } 10^{-13}$ to $\text{3. } 10^{-13} \text{ pA}\cdot\text{m}$. This scale indicates the magnitude of the response amplitude.

### Panel C: Topographical Map (MEG)

Panel C displays a scalp map, likely representing the spatial distribution of the measured response amplitude.
*   **Visualization:** It is a circular map overlaid on a schematic human head outline.
*   **Color Coding:** The colors correspond to the response magnitude, ranging from cooler tones (blue/green) in some areas to warmer tones (yellow/red) in others.
*   **Hotspots:** There is a prominent area of high activity (yellow/red) centered over the central-parietal region of the head.

### Panel E: Topographical Map (MEG)

Panel E also displays a scalp map, similar in structure to Panel C.
*   **Visualization:** It is a circular map overlaid on a schematic human head outline.
*   **Color Coding:** The color scale appears similar to Panel C, showing spatial distribution of activity.
*   **Hotspots:** There is a distinct area of high activity (red/yellow) localized over the central-parietal region.

### Panel F: Time Course Plot (MEG)

Panel F presents a time-series plot showing the response amplitude over time.
*   **Y-Axis Label:** $\text{EM } (\times 10^{-13})$ (likely representing the measured response amplitude in units of $10^{-13}$).
*   **X-Axis Label:** $\text{Time (s)}$. The axis ranges from approximately $-0.4$ to $0.4$ seconds.
*   **Data Lines:** Multiple colored lines are plotted, corresponding to the different conditions (though specific line assignments are not explicitly labeled in the plot itself, they correspond to the colors used previously).
*   **Annotations:**
    *   A vertical dashed line is present at $t=0.0$ s, likely marking the onset of a critical event or stimulus presentation.
    *   A vertical dashed line is present at $t=0.2$ s, marking another temporal reference point.
    *   Statistical significance markers are present: $p=0$ (for the overall trend or a specific comparison) and $p=0.14$.

**Contextual Note from Caption:**
The caption clarifies that the experiment involves 120 pairs of tones: 70% "freq AB" and 10% each of the rare pairs (AA, BA, BB). The models compare response amplitudes based on habituation (minimal response to repeated tones) versus predictive coding (response dependent on transition probabilities).

4

toneofthepair.Thetwomodelsgeneratequalitativelydiffer-
ent prediction for the AB and AA pairs. Observed group level
responses(rightcolumn)tothetwotonesofeachpairfitwith
predictive-coding predictions (for details, see Materials and
Methods). Error bars represent the SEM. C–F, MEG results for
magnetometers for one representative subject (left) and for
the average over all subjects (right). C and E show the sensor-
level topography of the average difference in magnetic field
between the rare AA and the frequent AB pairs, 170 ms after
the onset of the second sound. The most significant cluster of
sensorsatthistimeisindicatedbydots.DandFshowthetime
course of the average response to all conditions within these
sensors.Thetwotoneswerepresentedat0.2and0s(black
squares). The line colors correspond to the brackets surround-
ing the stimuli in A. The black line above the curves indicates
theintervalwhereasignificantdifferencewasfoundbetween
AA and AB.

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665–3678 • 3675

> Figure description (generated): This figure presents a schematic diagram illustrating different patterns of temporal relationships, likely related to neural activity or behavioral sequences, organized into four distinct rows. The overall structure is a vertical stack of four independent schematic blocks, each representing a different pattern type.

### Overall Layout & Structure
The figure is composed of four horizontal panels, stacked vertically. Each panel depicts a sequence or transition pattern using musical note symbols ($\text{♫}$) enclosed within colored brackets, connected by a double-headed horizontal arrow indicating a time duration.

### Visual Components & Symbols
**1. Musical Note Symbols ($\text{♫}$):** These symbols represent discrete events or states within the sequence. In each panel, there are two such symbols.
**2. Brackets and Color Coding:** Each sequence is framed by colored brackets:
    *   **Top Panel (Blue):** Uses blue brackets.
    *   **Second Panel (Red):** Uses red brackets.
    *   **Third Panel (Red):** Uses red brackets.
    *   **Bottom Panel (Green):** Uses green brackets.
**3. Temporal Arrow:** A double-headed horizontal arrow ($\leftrightarrow$) is positioned between the two note symbols in each panel. This arrow spans a specific time duration, indicating the temporal relationship between the two events.

### Labels, Keys & Legends
The labels provide specific context for each pattern:

**Panel 1 (Blue):**
*   The sequence is labeled **"frequent AB"**.
*   The time duration indicated by the arrow is **"10 - 20s"**.
*   To the right, there are parenthetical annotations: **"70 (8 tri..."** (The text is truncated).

**Panel 2 (Red):**
*   The sequence is labeled **"rare AA"**.
*   The time duration indicated by the arrow is **"10 - 20s"**.
*   To the right, there are parenthetical annotations: **"10 (1 tri..."** (The text is truncated).

**Panel 3 (Red):**
*   The sequence is labeled **"rare BB"**.
*   The time duration indicated by the arrow is **"10 - 20s"**.
*   To the right, there are parenthetical annotations: **"10 (1 tri..."** (The text is truncated).

**Panel 4 (Green):**
*   The sequence is labeled **"rare BA"**.
*   The time duration indicated by the arrow is **"10 - 20s"**.
*   To the right, there are parenthetical annotations: **"10 (1 tri..."** (The text is truncated).

### Data Trends & Details
Since this is a schematic diagram and not a plot, there are no axes or data trends to describe. The primary detail conveyed is the *type* of sequence (AB, AA, BB, BA) and its associated temporal window (10-20s), categorized by frequency ("frequent" vs. "rare").

### Contextual Caption Integration
The labels (e.g., "frequent AB," "rare AA") define the specific pattern being illustrated, where A and B likely represent distinct states or events (represented by the two note symbols). The color coding differentiates these patterns, and the accompanying text fragments on the right likely provide quantitative metrics (e.g., frequency counts or trial numbers) associated with each pattern type.


---

## Page 12

dence against a predominant role of synaptic habituation in the
MMN effect and argue for the predictive coding hypothesis. Similar
conclusions have been recently reached by other groups (Todorovic
et al., 2011).

Extensions and limits of the model
In this study, we limited our simulations to two cortical columns
coding for features distinct enough that thalamic inputs did not
stimulate both columns at the same time. The model could be
easily extended to a more continuous coding of tone frequency,
in which each neuronal population codes for one preferred fre-
quency but also responds more weakly to neighboring frequen-
cies. This would give an account of the increase of MMN
amplitude with the difference in frequency between standards
and deviants (Sams et al., 1985).

Predictive coding requires that a memory of the recent past be
used to predict the future. For the sake of simplicity, we adopted
here the simplest hypothesis for a neural memory: a delay line.
Although this assumption may not seem very realistic, we only
argue here that there must be neural populations whose activity
contains information about both the identity of recent stimuli
and the time elapsed since they occurred. As noted by Buono-
mano (2005), these neurons need not be ordered in cortical
space, but could be intermixed and arise from the partially cha-
otic temporal dynamics of cortical activation spread. Electro-
physiological recordings from auditory cortex slices suggest that
such a code might exist within the auditory cortex (Buonomano,
2003): when cortical neurons were stimulated, they triggered
other neurons with reliable delays, without any correlation be-
tween response delays and the cortical distance from the neuron
initially stimulated. Such a code would be ideal to support a
memory of the recent past, as required in our model. It would
allow the same neuronal populations to code tonotopically for
the present and nontonopically for the past.

According to this hypothesis, our entire model would fit
within a single cortical column and could constitute a basic build-
ing block for sensory predictive learning in various sensory sys-
tems. As noted by Friston et al. (2005), the closely similar
neuronal architecture of cortical layers throughout the cerebral
cortex supports the view that a similar computational principle of
predictive coding may apply to the multiple hierarchical levels of
the cortical areas of the brain. Thus, our model may be used to
account for higher-order instances of mismatch responses, such
as the distinct MMNs evoked by a change in phoneme versus
speaker (Giard et al., 1995; Dehaene-Lambertz, 1997), or the mis-
match responses observed outside the auditory modality, either
in visual (Tales et al., 1999; Pazo-Alvarez et al., 2003), olfactive
(Krauel et al., 1999; Pause and Krauel, 2000), and somatosensory
(Kekoni et al., 1997; Shinozaki et al., 1998) modalities or even in
a crossmodal context (Arnal et al., 2011).

Our model makes clear predictions as to the kind of regulari-
ties that should be reflected by the MMN. The model is only able
to predict incoming stimuli by acquiring an internal representa-
tion of the transition probabilities between their onsets and off-
sets, over a window of a few hundreds of milliseconds. Thus, it
fails to detect deviance from a rule that cannot be described at the
level of transition probabilities. This statement should help clar-
ify the issue of whether the MMN reflects “rule-based learning,”
which is often confused in the present literature.

For example, Sussman et al. (1998) showed that when the
oddball paradigm was slightly modified so that deviant sounds B
occurred regularly at short-enough intervals between the stan-
dards (AAAABAAAABAAAAB. . . ), the MMN disappeared. Yet

in a seemingly contradictory finding, using a minimally different
paradigm, Bekinschtein et al. (2009) showed that an AAAAB rule
could not be acquired by low-level sensory processing, since the
final B sound continued to elicit a MMN even when the entire
AAAAB sequence was fully predictable. According to our model,
the main difference between the two protocols is the long addi-
tional temporal gap between two five-tone sequences that exist in
the Bekinschtein paradigm, and which disrupts any recent mem-
ory capable of predicting the final B sound. Thus, the apparent
inconsistency in the results is easily understandable if we consider
the size of the memory delay needed for temporal prediction.
This example stresses the importance of carefully assessing the
matrix of transition probabilities when trying to design experi-
ments probing rule learning.

An MMN-like response was also recorded for deviance from
more abstract kinds of regularities such as tone repetition or
ascending/descending tones (Paavilainen et al., 1999; Korzyukov
et al., 2003; Endress et al., 2007). Whether or not such rules are
learnable by our network depends on the specifics of the experi-
mental design. To make the rule unlearnable by transition prob-
abilities, the design should reserve a broad frequency band never
presented during training, or over which the probabilities of as-
cending and descending tones are equal. Otherwise, given
enough training exemplars, our network will learn the “rule” and
even generalize to frequencies that are novel but close enough to
the training frequencies. These conditions were not fulfilled in
many previous papers. If they were, however, and if the MMN
resisted to such a control, this would provide definitive evidence
that the mechanisms underlying the MMN go beyond our basic
transition-probability model. The model might be extended,
however, by postulating higher-order neurons sensitive to me-
lodic contours (e.g., any ascending contour). In general, the cod-
ing properties of the input neural populations will have a crucial
impact on the kind of regularities that can be detected by our
model.

Conclusion
The idea that the brain is not a passive input–output device but
acts as a predictive system capable of anticipating on the future,
has a long history in ethology, psychology, and neuroscience, and
has been proven useful in many distinct domains of perception,
cognition, and action (Dehaene and Changeux, 1991; Schultz et
al., 1997; Sutton and Barto, 1998; Hosoya et al., 2005). Under-
standing the neural mechanisms by which the brain generates
predictions is therefore an important goal for neuroscience. Pre-
dictive coding models of the MMN have been previously pro-
posed (Friston, 2005; Friston et al., 2006; Garrido et al., 2009;
Spratling, 2010) but only as abstract mathematical descriptions
without a precise neurobiological implementation (Marreiros et
al., 2009; but see Fiorillo, 2008). The present model resolves the
difficulties associated with a neurobiological implementation of
predictive coding. We show how the subtraction of observed ver-
sus predicted signals can be implemented through a specific ar-
chitecture of inhibitory interneurons. We also show that a
NMDA-dependent STDP plasticity rule is well adapted for learn-
ing of stimulus associations, leading to the prediction of a precise
and essential contribution of NDMA receptors to predictive cod-
ing. The proposed architecture could generalize much beyond
the specific domain of the MMN for which it was presently tested.