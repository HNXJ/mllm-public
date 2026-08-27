## 

Behavioral/Systems/Cognitive

A Neuronal Model of Predictive Coding Accounting for the
Mismatch Negativity

Catherine Wacongne,1,2,3 Jean-Pierre Changeux,4,5 and Stanislas Dehaene1,2,3,5

1Institut National de la Sante´ et de la Recherche Me´dicale, Unite´ 992, Cognitive Neuroimaging Unit, and 2Commissariat a` l'Energie Atomique, DSV/I2BM,
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
Commissariat a` l'Energie Atomique, Fondation pour la Recherche Me´dicale, The Bettencourt-Schueller Foundation, and
Re´gionîle-de-France.WethankVirginieVanWassenhove,AlainDestexhe,andKarimBenchenaneforusefuldiscussions.

CorrespondenceshouldbeaddressedtoCatherineWacongne,Commissariata`l'EnergieAtomique/SAC/DSV/DRM/Neu-
roSpinCenter,Baˆt145,PointCourier156,F-91191Gif-sur-YvetteCedex,France.E-mail:catherine.wacongne@gmail.com.

-11.2012
Copyright©2012theauthors
0270-6474/12/323665-14$15.00/0

The Journal of Neuroscience, March 14, 2012 • 32(11):3665-3678 • 3665

---

## 

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
"prediction error" population, which receives two sets of inputs: excitatory
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

3666 • J. Neurosci., March 14, 2012 • 32(11):3665-3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity

## 

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
probabilistic connectivity rules. Each condition was simulated on 5-10
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
J. Neurosci., March 14, 2012 • 32(11):3665-3678 • 3667

---

## 

high-pass filtered at 0.1 Hz, and sampled at 1 kHz. The head position with
respect to the sensor array was determined by four head position indica-
tor coils attached to the participant's scalp. The locations of the coils and
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
(). Trials were epoched for each trial type be-
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

populations during 10 ms. The first stimulus ("sound A") was pre-
sented most of the time (standard tone), and the other one ("sound
B") more rarely, with a parametrically variable frequency (deviant
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
neurons increases with the delay coded (approximating Weber's
law). Essentially, the activity of a neuron in a delay line codes for
two properties of past inputs: the identity of a past stimulus and
the time elapsed since the occurrence of that stimulus. The par-
ticular choice we made for the implementation of this double
function (delay lines) is not fully physiologically realistic but was

3668 • J. Neurosci., March 14, 2012 • 32(11):3665-3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity

---

## 

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

### Axes and Scales
**Y-Axes:**
* **Top Plots (Synaptic Currents):** The y-axis ranges from 0 to 8.
* **Bottom Plots (Firing Rates):** The y-axis ranges from 0 to 8.

**X-Axes:**
* **Both Plot Types:** The x-axis represents time, though specific units are not labeled on the visible portion of the axes.

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

## 

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
dynamics, as in "reservoir" or echo state networks models (Maass
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
memorytracearereorderedsothatthepropagationoftheactivityinasynfirechainwayismadeobvious."n-1,""n-2,"and"n-3"
arrowed boxes refer to past stimuli whose activity is propagating in the delay lines initiated. In the left column, "n" and "n1"
arrowed boxes point to the initiation of a new memory trace following synchronous activity of the predictive population corre-
sponding to the prediction of the stimuli n and n1 ("p1" and "p2" arrows). In the right column, the "n1" arrowed box shows
the initiation of a new memory trace following synchronous activity of the predictive population corresponding to the prediction
errorsignalofthen1(deviant)stimulus.Afterlearning(Fig.4),areproduciblepatternofactivationinmemorytraceproducesa
depolarizationinthepredictivelayer(blackarrows)viaapopulationofinterneurons(notdisplayedhere).Theactivityinpredictive
layerinducesanhyperpolarizationinthepredictionerrorlayer("e2"arrow)attheapproximatetimewhenanAsoundisexpected.
At t  0, both prediction and input belong to the same column, resulting in a cancellation of excitation and inhibition inside the
predictionerrorlayer("e1"arrow).Att150ms,whenadeviantstimulusBispresented,adepolarizationofthepredictionerror
population selective to the deviant ("e3" arrow) can be observed in parallel to the hyperpolarization of the predictive population
selective to the standard ("e2" arrow). This depolarization is transmitted to the predictive ("p3" arrow) and memory (left column
"n1" arrow) populations.

> Figure caption (from PDF text): Figure 3.
Simulated pattern of neural firing and membrane voltage during a single trial of the oddball paradigm. The figure
shows a typical response to a standard tone (t  0 ms) followed by a deviant tone (t  150 ms). Left column, Subpopulations
selectivetotoneA;rightcolumn,subpopulationsselectivetotoneB.Foreachlayer,thetoppartofthepanelrepresentssingle-unit
membranevoltage(onelinepersimulatedneuron);thebottompartistheaveragevoltageoverthepopulation.Theneuronsofthe
memorytracearereorderedsothatthepropagationoftheactivityinasynfirechainwayismadeobvious."n-1,""n-2,"and"n-3"
arrowed boxes refer to past stimuli whose activity is propagating in the delay lines initiated. In the left column, "n" and "n1"
arrowed boxes point to the initiation of a new memory trace following synchronous activity of the predictive population corre-
sponding to the prediction of the stimuli n and n1 ("p1" and "p2" arrows). In the right column, the "n1" arrowed box shows
the initiation of a new memory trace following synchronous activity of the predictive population corresponding to the prediction
errorsignalofthen1(deviant)stimulus.Afterlearning(Fig.4),areproduciblepatternofactivationinmemorytraceproducesa
depolarizationinthepredictivelayer(blackarrows)viaapopulationofinterneurons(notdisplayedhere).Theactivityinpredictive
layerinducesanhyperpolarizationinthepredictionerrorlayer("e2"arrow)attheapproximatetimewhenanAsoundisexpected.
At t  0, both prediction and input belong to the same column, resulting in a cancellation of excitation and inhibition inside the
predictionerrorlayer("e1"arrow).Att150ms,whenadeviantstimulusBispresented,adepolarizationofthepredictionerror
population selective to the deviant ("e3" arrow) can be observed in parallel to the hyperpolarization of the predictive population
selective to the standard ("e2" arrow). This depolarization is transmitted to the predictive ("p3" arrow) and memory (left column
"n1" arrow) populations.

This figure, labeled as **Figure 3**, presents a simulated pattern of neural firing and membrane voltage across two distinct experimental conditions, organized into columns. The overall structure is a multi-panel visualization displaying time-series data for neural activity, likely representing the response to an oddball paradigm.

## 

the repetition of a five-tone sequence AAAAB, the final B sound
continues to elicit a MMN even though the occurrence of this
sound is perfectly predictable based on the prior occurrence of
four A sounds. In other words, the MMN seems to be "blind" to
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
population "A" responded to the onset of the stimulus, and the
"B" population to the offset. On a rare 10% of trials, the duration

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

In summary, the figure uses four stacked heatmaps to visually compare how input transition statistics evolve over time lags ($dt$) against the learned synaptic weights, across different levels of oddball deviation (5%, 10%, 20%, and 30%).

> Figure caption (from PDF text): Figure 4.
Correspondence between the transition statistics of the inputs (left) and the synaptic weights learned by the model
(right).Ineachpanel,thestatisticsaregivenforsimulationswith5,10,20,and30%ofdeviantsoundsBinanoddballparadigm.
Leftcolumn,Conditionalprobabilitiesofreceivingagivensound(AorB)attimet,giventherecenthistoryofpastinputsattimes
t-dt(dtrangingfrom0to400ms).Rightcolumn,Correspondingsynapticweightsinthesimulationattheendoflearning.Thegray
levels indicate the mean synaptic weights between neurons of the recurrent memory network spiking on average at the time dt
after the occurrence of an A or B sound, and the predictive neurons coding for the arrival of an A or B sound.

Wacongne et al. • A Neuronal Model of Mismatch Negativity
J. Neurosci., March 14, 2012 • 32(11):3665-3678 • 3671

---

## 

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

## 

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

### Labels and Annotations
*   **Top Left:** The text fragment "RuleA RuleAB" is visible, suggesting the panels might correspond to different experimental conditions or rules.
*   **Bottom Right:** The text fragment "RuleB" is visible, suggesting the bottom plot corresponds to a different condition.
*   **Axis Labels:** The axes are labeled with numerical scales as described above, but no explicit variable names (e.g., "Firing Rate," "Voltage") are legible on the axes themselves in the provided crop, only the numerical ticks.

---

## 

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
sors (subject 1: Grad, 121-206 ms, p 
 1e-16; Mag, 131-231 ms;

subject 2: Grad, 131-186 ms, p  0.028; Mag, 157-204 ms, p 
0.044; subject 3: Grad, 127-226 ms, p  0.003; Mag, 126-264 ms,
p  0.004; subject 4: Grad, 109-177 ms, p  0.006; Mag, 110-230
ms, p  0.001; subject 5: Grad, 120-164 ms, p  0.04; Mag,
116-260 ms, p  0.01), as well as at the group level (Grad, 108-
232 ms, p 
 1e-16; Mag, 145-193 ms, p 
 1e-16). The topogra-
phy of the effect was similar to the classical MEG-MMN
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
A-A delay of 200 ms is much shorter than the AB-AB delay of 10 s
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

3674 • J. Neurosci., March 14, 2012 • 32(11):3665-3678
Wacongne et al. • A Neuronal Model of Mismatch Negativity

---

## 

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

## 

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
ify the issue of whether the MMN reflects "rule-based learning,"
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
enough training exemplars, our network will learn the "rule" and
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
The idea that the brain is not a passive input-output device but
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