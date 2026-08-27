## Page 1

Neuron
Perspective

Canonical Microcircuits for Predictive Coding

Andre M. Bastos,1,2,6 W. Martin Usrey,1,3,4 Rick A. Adams,8 George R. Mangun,2,3,5 Pascal Fries,6,7 and Karl J. Friston8,*
1Center for Neuroscience
2Center for Mind and Brain
3Department of Neurology
4Department of Neurobiology, Physiology and Behavior
5Department of Psychology
University of California, Davis, Davis, CA 95618 USA
6Ernst Stru¨ ngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society, Deutschordenstraße 46, 60528 Frankfurt,
Germany
7Donders Institute for Brain, Cognition and Behaviour, Radboud University Nijmegen, Kapittelweg 29, 6525 EN Nijmegen, Netherlands
8The Wellcome Trust Centre for Neuroimaging, University College London, Queen Square, London WC1N 3BG, UK
*Correspondence: k.friston@ucl.ac.uk
http://dx.doi.org/10.1016/j.neuron.2012.10.038

This Perspective considers the inﬂuential notion of a canonical (cortical) microcircuit in light of recent theories
about neuronal processing. Speciﬁcally, we conciliate quantitative studies of microcircuitry and the func-
tional logic of neuronal computations. We revisit the established idea that message passing among hierar-
chical cortical areas implements a form of Bayesian inference—paying careful attention to the implications
for intrinsic connections among neuronal populations. By deriving canonical forms for these computations,
one can associate speciﬁc neuronal populations with speciﬁc computational roles. This analysis discloses
a remarkable correspondence between the microcircuitry of the cortical column and the connectivity implied
by predictive coding. Furthermore, it provides some intuitive insights into the functional asymmetries
between feedforward and feedback connections and the characteristic frequencies over which they operate.

Introduction
The idea that the brain actively constructs explanations for its
sensory inputs is now generally accepted. This notion builds
on a long history of proposals that the brain uses internal or
generative models to make inferences about the causes of
its sensorium (Helmholtz, 1860; Gregory, 1968, 1980; Dayan
et al., 1995). In terms of implementation, predictive coding
is, arguably, the most plausible neurobiological candidate for
making these inferences (Srinivasan et al., 1982; Mumford,
1992; Rao and Ballard, 1999). This Perspective considers the
canonical microcircuit in light of predictive coding. We focus
on the intrinsic connectivity within a cortical column and the
extrinsic connections between columns in different cortical
areas. We try to relate this circuitry to neuronal computations
by showing that the computational dependencies—implied by
predictive coding—recapitulate the physiological dependencies
implied by quantitative studies of intrinsic connectivity. This
issue is important as distinct neuronal dynamics in different
cortical layers are becoming increasingly apparent (de Kock
et al., 2007; Sakata and Harris, 2009; Maier et al., 2010; Bolli-
munta et al., 2011). For example, recent ﬁndings suggest that
the superﬁcial layers of cortex show neuronal synchronization
and spike-ﬁeld coherence predominantly in the gamma frequen-
cies, while deep layers prefer lower (alpha or beta) frequencies
(Roopun et al., 2006, 2008; Maier et al., 2010; Buffalo et al.,
2011). Since feedforward connections originate predominately
from superﬁcial layers and feedback connections from deep
layers, these differences suggest that feedforward connections
use relatively high frequencies, compared to feedback connec-
tions, as recently demonstrated empirically (Bosman et al.,
2012). These asymmetries call for something quite remarkable:

namely, a synthesis of spectrally distinct inputs to a cortical
column and the segregation of its outputs. This segregation
can only arise from local neuronal computations that are struc-
tured and precisely interconnected. It is the nature of this intrinsic
connectivity—and the dynamics it supports—that we consider.
The aim of this Perspective is to speculate about the functional
roles of neuronal populations in speciﬁc cortical layers in terms
of predictive coding. Our long-term aim is to create computa-
tionally informed models of microcircuitry that can be tested
with dynamic causal modeling (David et al., 2006; Moran et al.,
2008, 2011).
This Perspective comprises three sections. We start with an
overview of the anatomy and physiology of cortical connections,
with an emphasis on quantitative advances. The second section
considers the computational role of the canonical microcircuit
that emerges from these studies. The third section provides
a formal treatment of predictive coding and deﬁnes the requisite
computations in terms of differential equations. We then asso-
ciate the form of these equations with the canonical microcircuit
to deﬁne a computational architecture. We conclude with some
predictions about intrinsic connections and note some important
asymmetries in feedforward and feedback connections that
emerge from this treatment.

The Anatomy and Physiology of Cortical Connections
This section reviews laminar-speciﬁc connections that underlie
the notion of a canonical microcircuit (Douglas et al., 1989;
Douglas and Martin, 1991, 2004). We ﬁrst focus on mammalian
visual cortex and then consider whether visual microcircuitry
can be generalized to a canonical circuit for the entire cortex.
Both functional and anatomical techniques have been applied

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
695


---

## Page 2

to study intrinsic (intracortical) and extrinsic connections. We will
emphasize the insights from recent studies that combine both
techniques.

Intrinsic Connections and the Canonical Microcircuit
The seminal work of Douglas and Martin (1991), in the cat visual
system, produced a model of how information ﬂows through the
cortical column. Douglas and Martin recorded intracellular
potentials from cells in primary visual cortex during electrical
stimulation of its thalamic afferents. They noted a stereotypical
pattern of fast excitation, followed by slower and longer-lasting
inhibition. The latency of the ensuing hyperpolarization distin-
guished responses in supragranular and infragranular layers.
Using conductance-based models, they showed that a simple
model could reproduce these responses. Their model contained
superﬁcial and deep pyramidal cells with a common pool of
inhibitory cells. All three neuronal populations received thalamic
drive and were fully interconnected. The deep pyramidal cells
received relatively weak thalamic drive but strong inhibition
(Figure 1). These interconnections allowed the circuit to amplify
transient thalamic inputs to generate sustained activity in the
cortex, while maintaining a balance between excitation and
inhibition, two tasks that must be solved by any cortical circuit.
Their circuit, although based on recordings from cat visual
cortex, was also proposed as a basic theme that might be
present and replicated, with minor variations, throughout the
cortical sheet (Douglas et al., 1989).

Subsequent studies have used intracellular recordings and
histology to measure spikes (and depolarization) in pre- and
postsynaptic cells, whose cellular morphology can be deter-
mined. This approach quantiﬁes both the connection proba-

bility—deﬁned as the number of observed connections divided
by total number of pairs recorded—and connection strength—
deﬁned in terms of postsynaptic responses. Thomson et al.
(2002) used these techniques to study layers 2 to 5 (L2 to L5)
of the cat and rat visual systems. The most frequently connected
cells were located in the same cortical layer, where the largest
interlaminar projections were the ‘‘feedforward’’ connections
from L4 to L3 and from L3 to L5. Excitatory reciprocal ‘‘feed-
back’’ connections were not observed (L3 to L4) or less common
(L5 to L3), suggesting that excitation spreads within the column
in a feedforward fashion. Feedback connections were typically
seen when pyramidal cells in one layer targeted inhibitory cells
in another (see Thomson and Bannister, 2003 for a review).

While many studies have focused on excitatory connections,
a few have examined inhibitory connections. These are more dif-
ﬁcult to study, because inhibitory cells are less common than
excitatory cells, and because there are at least seven distinct
morphological classes (Salin and Bullier, 1995). However, recent
advances in optogenetics have made it possible to target inhib-
itory cells more easily: Ka¨ tzel and colleagues combined optoge-
netics and whole-cell recording to investigate the intrinsic
connectivity of inhibitory cells in mouse cortical areas M1, S1,
and V1 (Ka¨ tzel et al., 2011). They transgenically expressed chan-
nelrhodopsin in inhibitory neurons and activated them while
recording from pyramidal cells. This allowed them to assess
the effect of inhibition as a function of laminar position relative
to the recorded neuron.

Several conclusions can be drawn from this approach (Ka¨ tzel
et al., 2011): ﬁrst, L4 inhibitory connections are more restricted in
their lateral extent, relative to other layers. This supports the
notion that L4 responses are dominated by thalamic inputs,
while the remaining laminae integrate afferents from a wider
cortical patch. Second, the primary source of inhibition origi-
nates from cells in the same layer, reﬂecting the prevalence of
inhibitory intralaminar connections. Third, several interlaminar
motifs appeared to be general—at least in granular cortex: prin-
cipally, a strong inhibitory connection from L4 onto supragranu-
lar L2/3 and from infragranular layers onto L4. For more informa-
tion on inhibitory connections, see Yoshimura and Callaway
(2005). Figure 2 provides a summary of key excitatory and inhib-
itory intralaminar connections.

Microcircuits in the Sensorimotor Cortex
Do the features of visual microcircuits generalize to other cortical
areas? Recently, two studies have mapped the intrinsic connec-
tivity of mouse sensory and motor cortices: Lefort et al. (2009)
used multiple whole-cell recordings in mouse barrel cortex to
determine the probability of monosynaptic connections and
the corresponding connection strength. As in visual cortex, the
strongest connections were intralaminar and the strongest inter-
laminar connections were the ascending L4 to L2 and descend-
ing L3 to L5.

One puzzle about canonical microcircuits is whether motor
cortex has a local circuitry that is qualitatively similar to sensory
cortex. This question is important because motor cortex lacks
a clearly deﬁned granular L4 (a property that earns it the name
‘‘agranular cortex’’). Weiler et al. (2008) combined whole-cell
recordings in mouse motor cortex with photostimulation to

Figure 1. Douglas and Martin Model of the Canonical Microcircuit
This is a schematic of the classical microcircuit adapted from Douglas and
Martin (1991). This minimal circuitry comprises superﬁcial (layers 2 and 3) and
deep (layers 5 and 6) pyramidal cells and a population of smooth inhibitory
cells. Feedforward inputs—from the thalamus—target all cell populations but
with an emphasis on inhibitory interneurons and superﬁcial and granular
layers. Note the symmetrical deployment of inhibitory and excitatory intrinsic
connections that maintain a balance of excitation and inhibition.

696
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective


---

## Page 3

uncage Glutamate. This allowed them to systematically stimu-
late the cortical column in a grid, centered on the pyramidal
neuron from which they recorded. By recording from pyramidal
neurons in L2–L6 (L1 lacks pyramidal cells), the authors mapped
the excitatory inﬂuence that each layer exerts over the others.
They found that the L2/3 to L5A/B was the strongest connection,
accounting for one-third of the total synaptic current in the
circuit. The second strongest interlaminar connection was the
reciprocal L5A to L2/3 connection. This pathway may be homol-
ogous to the prominent L4/5A to L2/3 pathway in sensory cortex.
Also, as in sensory cortex, recurrent (intralaminar) connections
were prominent, particularly in L2, L5A/B, and L6. The largest
fraction of synaptic input arrived in L5A/B, consistent with its
key role in accumulating information from a wide range of affer-
ents, before sending its output to the corticospinal tract. In
summary, strong input layer to superﬁcial and superﬁcial to
deep connectivity, together with strong intralaminar connec-
tivity, suggests that the intrinsic circuitry of motor cortex is
similar to other cortical areas.

The Anatomy and Physiology of Extrinsic Connections
Clearly, an account of microcircuits must refer to the layers
of origin of extrinsic connections and their laminar targets.
Although the majority of presynaptic inputs arise from intrinsic
connections, cortical areas are also richly interconnected, where
the balance between intrinsic and extrinsic processing mediates
functional integration among specialized cortical areas (Engel
et al., 2010). By numbers alone, intrinsic connections appear to
dominate—95% of all neurons labeled with a retrograde tracer
lie within about 2 mm of the injection site (Markov et al., 2011).

Figure 2. The Canonical Cortical
Microcircuit
This is a simpliﬁed schematic of the key intrinsic
connections among excitatory (E) and inhibitory (I)
populations in granular (L4), supragranular (L1/
2/3), and infragranular (L5/6) layers. The excitatory
interlaminar connections are based largely on
Gilbert and Wiesel (1983). Forward connections
denote feedforward extrinsic corticocortical or
thalamocortical afferents that are reciprocated by
backward or feedback connections. Anatomical
and functional data suggest that afferent input
enters primarily into L4 and is conveyed to
superﬁcial layers L2/3 that are rich in pyramidal
cells, which project forward to the next cortical
area, forming a disynaptic route between thalamus
and secondary cortical areas (Callaway, 1998).
Information from L2/3 is then sent to L5 and L6,
which sends (intrinsic) feedback projections back
to L4 (Usrey and Fitzpatrick, 1996). L5 cells origi-
nate feedback connections to earlier cortical areas
as well as to the pulvinar, superior colliculus, and
brain stem. In summary, forward input is segre-
gated by intrinsic connections into a superﬁcial
forward stream and a deep backward stream. In
this schematic, we have juxtaposed densely in-
terconnected excitatory and inhibitory populations
within each layer.

The remaining 5% represent cells giving
rise
to
extrinsic
connections,
which,
although sparse, can be extremely effec-
tive in driving their targets. A case in point is the LGN to V1
connection: although it is only the sixth strongest connection
to V1, LGN afferents have a substantial effect on V1 responses
(Markov et al., 2011).
Hierarchies and Functional Asymmetries
Current dogma holds that the cortex is hierarchically organized.
The idea of a cortical hierarchy rests on the distinction between
three types of extrinsic connections: feedforward connec-
tions, which link an earlier area to a higher area, feedback
connections, which link a higher to an earlier area, and lateral
connections, which link areas at the same level (reviewed in
Felleman and Van Essen, 1991). These connections are distin-
guished by their laminar origins and targets. Feedforward
connections originate largely from superﬁcial pyramidal cells
and target L4, while feedback connections originate largely
from deep pyramidal cells and terminate outside of L4 (Felleman
and Van Essen, 1991). Clearly, this description of cortical hierar-
chies is a simpliﬁcation and can be nuanced in many ways: for
example, as the hierarchical distance between two areas in-
creases, the percentage of cells that send feedforward (respec-
tively feedback) projections from a lower (respectively higher)
level becomes increasingly biased toward the superﬁcial (re-
spectively deep) layers (Barone et al., 2000; Vezoli et al., 2004).

In addition to the laminar speciﬁcity of their origins and targets,
feedforward and feedback connections also differ in their
synaptic physiology. The traditional view holds that feedforward
connections are strong and driving, capable of eliciting spiking
activity in their targets and conferring classical receptive ﬁeld
properties—the prototypical example being the synaptic con-
nection between LGN and V1 (Sherman and Guillery, 1998).

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
697

Neuron
Perspective

> Figure description (generated): This figure is a schematic diagram illustrating a cyclical or recurrent neural circuit structure, likely representing cortical layers and connectivity.

**1. Overall Layout & Structure:**
The diagram is presented as a circular flow chart or circuit schematic, showing interconnected nodes (representing layers) and directional connections (arrows). The structure suggests a feedback loop or sequential processing across different functional levels.

**2. Visual Components & Symbols:**
*   **Nodes (Circles):** There are at least three visible circular nodes, labeled L2/3, L4, and L5a. These represent distinct layers within a neural structure (e.g., neocortex).
*   **Connections (Arrows):** Directed arrows indicate the flow of information between these layers.
    *   A large, sweeping, light purple/lavender arrow curves from the vicinity of L5a upwards and towards L2/3, indicating a strong recurrent or feedforward connection.
    *   A thinner, light purple arrow originates from the left side of the diagram and points towards L2/3.
    *   A distinct, bright green arrow connects the node labeled L4 to the node labeled L5a.
    *   A light purple arrow connects L2/3 to L4, indicating a feedforward connection between these layers.

**3. Labels, Keys & Legends:**
The following labels are visible on the nodes:
*   **L2/3:** Located at the top right.
*   **L4:** Located in the middle right.
*   **L5a:** Located at the bottom right.

No explicit legend or axis labels are present, as this is a schematic diagram rather than a quantitative plot.

**4. Data Trends & Details:**
As this is a schematic circuit diagram, there are no quantitative data trends to report. The visual elements convey connectivity and directionality rather than magnitude changes.

**5. Contextual Caption Integration:**
Based on the labels (L2/3, L4, L5a), this figure schematically depicts connectivity between specific layers of a neural structure. The arrows illustrate the flow of information, including recurrent connections (the large purple loop) and feedforward pathways between these defined layers.


---

## Page 4

Feedback connections are thought to modulate (extraclassi-
cal) receptive ﬁeld characteristics according to the current
context; e.g., visual occlusion, attention, salience, etc. The pro-
totypical example of a feedback connection is the cortical L6
to LGN connection. Sherman and Guillery identiﬁed several
properties that distinguish drivers from modulators. Driving
connections tend to show a strong ionotropic component in
their synaptic response, evoke large EPSPs, and respond to
multiple EPSPs with depressing synaptic effects. Modulatory
connections produce metabotropic and ionotropic responses
when stimulated, evoke weak EPSPs, and show paired-pulse
facilitation (Sherman and Guillery, 1998, 2011). These distinc-
tions were based upon the inputs to the LGN, where retinal
input is driving and cortical input is modulatory. Until recently,
little data were available to assess whether a similar distinction
applies to corticocortical feedforward and feedback connec-
tions. However, recent studies show that cortical feedback
connections express not only modulatory but also driving char-
acteristics.
Are Feedback Connections Driving, Modulatory, or
Both?
Although it is generally thought that feedback connections
are weak and modulatory (Crick and Koch, 1998; Sherman and
Guillery, 1998), recent evidence suggests that feedback con-
nections do more than modulate lower-level responses: Sher-
man and colleagues recorded cells in mouse areas V1/V2 and
A1/A2, while stimulating feedforward or feedback afferents. In
both cases, driving-like responses as well as modulatory-like
responses were observed (Covic and Sherman, 2011; De Pas-
quale and Sherman, 2011). This indicates that—for these hierar-
chically proximate areas—feedback connections can drive their
targets just as strongly as feedforward connections. This is
consistent with earlier studies showing that feedback connec-
tions can be driving: Mignard and Malpeli (1991) studied the
feedback connection between areas 18 and 17, while layer A
of the LGN was pharmacologically inactivated. This silenced
the cells in L4 in area 17 but spared activity in superﬁcial layers.
However, superﬁcial cells were silenced when area 18 was
lesioned. This is consistent with a driving effect of feedback
connections from area 18, in the absence of geniculate input.
In summary, feedback connections can mediate modulatory
and driving effects. This is important from the point of view of
predictive coding, because top-down predictions have to elicit
obligatory responses in their targets (cells reporting prediction
errors).

In predictive coding, feedforward connections convey predic-
tion errors, while feedback connections convey predictions
from higher cortical areas to suppress prediction errors in lower
areas. In this scheme, feedback connections should therefore be
capable of exerting strong (driving) inﬂuences on earlier areas to
suppress or counter feedforward driving inputs. However, as we
will see later, these inﬂuences also need to exert nonlinear or
modulatory effects. This is because top-down predictions are
necessarily context sensitive: e.g., the occlusion of one visual
object by another. In short, predictive coding requires feedback
connections to drive cells in lower levels in a context-sensitive
fashion, which necessitates a modulatory aspect to their post-
synaptic effects.

Are Feedback Connections Excitatory or Inhibitory?
Crucially, because feedback connections convey predictions,
which serve to explain and thereby reduce prediction errors in
lower levels, their effective (polysynaptic) connectivity is gener-
ally assumed to be inhibitory. An overall inhibitory effect of
feedback connections is consistent with in vivo studies. For
example, electrophysiological studies of the mismatch negativity
suggest that neural responses to deviant stimuli, which violate
sensory predictions established by a regular stimulus sequence,
are enhanced relative to predicted stimuli (Garrido et al., 2009).
Similarly, violating expectations of auditory repetition causes
enhanced gamma-band responses in early auditory cortex (To-
dorovic et al., 2011). These enhanced responses are thought
to reﬂect an inability of higher cortical areas to predict, and
thereby suppress, the activity of populations encoding predic-
tion error (Garrido et al., 2007; Wacongne et al., 2011). The
suppression of predictable responses can also be regarded as
repetition suppression, observed in single-unit recordings from
the inferior temporal cortex of macaque monkeys (Desimone,
1996). Furthermore, neurons in monkey inferotemporal cortex
respond signiﬁcantly less to a predicted sequence of natural
images, compared to an unpredicted sequence (Meyer and Ol-
son, 2011).

The inhibitory effect of feedback connections is further sup-
ported by neuroimaging studies (Murray et al., 2002, 2006; Har-
rison et al., 2007; Summerﬁeld et al., 2008, 2011; Alink et al.,
2010). These studies show that predictable stimuli evoke smaller
responses in early cortical areas. Crucially, this suppression
cannot be explained in terms of local adaptation, because the
attributes of the stimuli that can be predicted are not represented
in early sensory cortex (e.g., Harrison et al., 2007). It should be
noted that the suppression of responses to predictable stimuli
can coexist with (top-down) attentional enhancement of evoked
processing (Wyart et al., 2012): in predictive coding, attention is
mediated by increasing the gain of populations encoding pre-
diction error (Spratling, 2008; Feldman and Friston, 2010). The
resulting attentional modulation (e.g., Hopﬁnger et al., 2000)
can interact with top-down predictions to override their suppres-
sive inﬂuence, as demonstrated empirically (Kok et al., 2012).
See Buschman and Miller (2007), Saalmann et al. (2007),
Anderson et al. (2011), and Armstrong et al. (2012) for further
discussion of top-down connections in attention.

Further evidence for the inhibitory (suppressive) effect of
feedback connections comes from neuropsychology: patients
with damage to the prefrontal cortex (PFC) show disinhibition
of event-related potential (ERP) responses to repeating stimuli
(Knight et al., 1989; Yamaguchi and Knight, 1990; but see Bar-
celo´ et al., 2000). In contrast, they show reduced-amplitude
P300 ERPs in response to novel stimuli—as if there were a failure
to communicate top-down predictions to sensory cortex (Knight,
1984). Furthermore, normal subjects show a rapid adaptation to
deviant stimuli as they become predictable—an effect not seen
in prefrontal patients.

Several invasive studies complement these human studies in
suggesting an overall inhibitory role for feedback connections.
In a recent seminal study, Olsen et al. studied corticothalamic
feedback between L6 of V1 and the LGN using transgenic
expression of channelrhodopsin in L6 cells of V1. By driving

698
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective


---

## Page 5

these cells optogenetically—while recording units in V1 and the
LGN—the authors showed that deep L6 principal cells inhibited
their extrinsic targets in the LGN and their intrinsic targets in
cortical layers 2 to 5 (Olsen et al., 2012). This suppression was
powerful—in the LGN, visual responses were suppressed by
76%. Suppression was also high in V1, around 80%–84% (Olsen
et al., 2012). This evidence is in line with classical studies of cor-
ticogeniculate contributions to length tuning in the LGN, showing
that cortical feedback contributes to the surround suppression
of feline LGN cells: without feedback, LGN cells are disinhibited
and show weaker surround suppression (Murphy and Sillito,
1987; Sillito et al., 1993; but see Alitto and Usrey, 2008).
While these studies provide convincing evidence that cor-
tical feedback to the LGN is inhibitory, the evidence is more
complicated for corticocortical feedback connections (Sandell
and Schiller, 1982; Johnson and Burkhalter, 1996, 1997). Hupe´
et al. (1998) cooled area V5/MT while recording from areas V1,
V2, and V3 in the monkey. When visual stimuli were presented
in the classical receptive ﬁeld (CRF), cooling of area V5/MT
decreased unit activity in earlier areas, suggesting an excitatory
effect of extrinsic feedback (Hupe´ et al., 1998). However, when
the authors used a stimulus that spanned the extraclassical
RF, the responses of V1 neurons were, on average, enhanced
after cooling area V5, consistent with the suppressive role of
feedback connections. These results indicate that the inhibitory
effects of feedback connections may depend on (natural) stimuli
that require integration over the visual ﬁeld. Similar effects were
observed when area V2 was cooled and neurons were measured
in V1: when stimuli were presented only to the CRF, cooling V2
decreased V1 spiking activity; however, when stimuli were
present in the CRF and the surround, cooling V2 increased V1
activity (Bullier et al., 1996). Finally, others have argued for an
inhibitory effect of feedback based on the timing and spatial
extent of surround suppression in monkey V1, concluding that
the far surround suppression effects were most likely mediated
by feedback (Bair et al., 2003).

The empirical ﬁnding that feedback connections can both
facilitate and suppress ﬁring in lower hierarchical areas—de-
pending on the content of classical and extraclassical receptive
ﬁelds—is consistent with predictive coding: Rao and Ballard
(1999) trained a hierarchical predictive coding network to recog-
nize natural images. They showed that higher levels in the hier-
archy learn to predict visual features that extend across many
CRFs in the lower levels (e.g., tree trunks or horizons). Hence,
higher visual areas come to predict that visual stimuli will span
the receptive ﬁelds of cells in lower visual areas. In this setting,
a stimulus that is conﬁned to a CRF would elicit a strong pre-
diction error signal (because it cannot be predicted). This pro-
vides a simple explanation for the ﬁndings of Hupe´ et al. (1998)
and Bullier et al. (1996): when feedback connections are deacti-
vated, there are no top-down predictions to explain responses in
lower areas, leading to a disinhibition of responses in earlier
areas when—and only when—stimuli can be predicted over
multiple CRFs.
Feedback Connections and Layer 1
How might the inhibitory effect of feedback connections be
mediated? The established view is that extrinsic corticocortical
connections are exclusively excitatory (using glutamate as their

excitatory neurotransmitter), although recent evidence suggests
that inhibitory extrinsic connections exist and may play an impor-
tant role in synchronizing distant regions (Melzer et al., 2012).
However, one important route by which feedback connections
could mediate selective inhibition is via their termination in L1
(Anderson and Martin, 2006; Shipp, 2007): layer 1 is sometimes
referred to as acellular due to its pale appearance with Nissl
staining (the classical method for separating layers that selec-
tively labels cell bodies). Indeed, a recent study concluded that
L1 contains less than 0.5% of all cells in a cortical column (Meyer
et al., 2011). These L1 cells are almost all inhibitory and intercon-
nect strongly with each other via electrical connections and
chemical synapses (Chu et al., 2003). Simultaneous whole-cell
patch-clamp recordings show that they provide strong mono-
synaptic inhibition to L2/3 pyramidal cells, whose apical
dendrites project into L1 (Chu et al., 2003; Wozny and Williams,
2011). This means that L1 inhibitory cells are in a prime position
to mediate inhibitory effects of extrinsic feedback. The laminar
location highlighted by these studies—the bottom of L1 and
the top of L2/3—has recently been shown to be a ‘‘hotspot’’ of
inhibition in the column (Meyer et al., 2011). Indeed, a study of
rat barrel cortex, which stimulated (and inactivated) L1, showed
that it exerts a powerful inhibitory effect on whisker-evoked
responses (Shlosberg et al., 2006). These studies suggest that
corticocortical feedback connections could deliver strong inhibi-
tion, if they were to recruit the inhibitory potential of L1.

In terms of the excitatory and modulatory effect of feedback
connections, predictive input from higher cortical areas might
have an important impact via the distal dendrites of pyramidal
neurons (Larkum et al., 2009). Furthermore, there is a speciﬁc
type of GABAergic neuron that appears to control distal dendritic
excitability, gating top-down excitatory signals differentially
during behavior (Gentet et al., 2012). Table 1 summarizes the
studies we have discussed in relation to the role of feedback
connections.

Feedforward and Transthalamic Connections
While the evidence for an inhibitory effect of feedback connec-
tions has to be evaluated carefully, the evidence for an excitatory
effect of feedforward connections is unequivocal. For example,
in the monkey, V1 projects monosynaptically to V2, V3, V3a,
V4, and V5/MT (Zeki, 1978; Zeki and Shipp, 1988). In all
cases—when V1 is reversibly inactivated through cooling—
single-cell activity in target areas is strongly suppressed (Girard
and Bullier, 1989; Girard et al., 1991a, 1991b, 1992). In the cases
of V2 and V3, the result of cooling area V1 is a near-total silencing
of single-unit activity. These studies illustrate that activity in
higher cortical areas depends on driving inputs from earlier
cortical areas that establish their receptive ﬁeld properties.

Finally, while many studies have focused on extrinsic connec-
tions that project directly from one cortical area to the next, there
is mounting evidence that feedforward driving connections (and
perhaps feedback) in the cortex could be mediated by transtha-
lamic pathways (Sherman and Guillery, 1998, 2011). The stron-
gest evidence for this claim comes from the somatosensory
system, where it was shown recently that the posterior medial
nucleus of the thalamus (POm)—a higher-order thalamic nucleus
that receives direct input from cortex—can relay information

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
699

Neuron
Perspective


---

## Page 6

between S1 and S2 (Theyel et al., 2010). In addition, the thalamic
reticular nucleus has been proposed to mediate the inhibition
that might underlie crossmodal attention or top-down predic-
tions (Yamaguchi and Knight, 1990; Crick, 1984; Wurtz et al.,
2011). Furthermore, computational considerations and recent
experimental ﬁndings point to a potentially important role for
higher-order thalamic nuclei in coordinating and synchronizing
cortical responses (Vicente et al., 2008; Saalmann et al., 2012).
The degree to which cortical areas are integrated directly via
corticocortical or indirectly via cortico-thalamo-cortical connec-
tions—and the extent to which transthalamic pathways disso-
ciate feedforward from feedback connections in the same way
as we have proposed for the corticocortical connections—are
open questions.

The Canonical Microcircuit
Central to the idea of a canonical microcircuit is the notion that
a cortical column contains the circuitry necessary to perform
requisite computations and that these circuits can be replicated
with minor variations throughout the cortex. One of the clearest
examples of how cortical circuits process simple inputs—to
generate complex outputs—is the emergence of orientation
tuning in V1. Orientation tuning is a distinctly cortical phenom-
enon because geniculocortical relay cells show no orientation
preferences. A further elaboration of cortical responses can be
found in the distinction between simple and complex cells—
while simple cells possess spatially conﬁned receptive ﬁelds,
complex cells are orientation tuned but show less preference
for the location of an oriented bar. Hubel and Wiesel proposed
a model for how intrinsic and extrinsic connectivity could estab-
lish a circuit explaining these receptive ﬁeld properties. They
proposed that orientation tuning in simple cells could be gener-
ated by a single cortical cell receiving input from several ON

center-OFF surround geniculate cells arranged along a par-
ticular orientation, thereby endowing it with a preference for
bars oriented in a particular direction (Hubel and Wiesel, 1962).
Complex cells were hypothesized to receive inputs from
several simple cells—with the same orientation preference and
slightly varying receptive ﬁeld locations. Thus, complex cells
were thought not to receive direct LGN input but to be higher-
order cells in cortex. Subsequent ﬁndings supported these
predictions, showing that input layers 4Ca and 4Cb contained
the largest proportion of cells receiving monosynaptic genicu-
late input, while superﬁcial and deep layer cells contain a larger
number of cells receiving disynaptic or polysynaptic input (Bullier
and Henry, 1980). Furthermore, simple cells project mono-
synaptically onto complex cells, where they exert a strong feed-
forward inﬂuence (Alonso and Martinez, 1998; Alonso, 2002).
These models suggest that intrinsic cortical circuitry allows pro-
cessing to proceed along discrete steps that are capable of
producing response properties in outputs that are not present
in inputs.

Segregation of Processing Streams
A key property of canonical circuits is the segregation of parallel
streams of processing. For example, in primates, parvocellular
input enters the cortex primarily in layer 4Cb, whereas magno-
cellular inputs enter in 4Ca. The corticogeniculate feedback
pathway from L6 maintains this segregation, as upper L6 cells
preferentially synapse onto parvocellular cells in the LGN, while
lower L6 cells target the magnocellular LGN layers (Fitzpatrick
et al., 1994; Briggs and Usrey, 2009). Further examples of stream
segregation are also present in the dorsal ‘‘where’’ and the
ventral ‘‘what’’ pathways and in the projection from V1 to the
thick, thin, and interstripe regions of V2 (Zeki and Shipp, 1988;
Sincich and Horton, 2005).

Table 1. Electrophysiological and Neuroimaging Findings Consistent with Predictive Coding

Prediction Violated
Area Studied

Neuronal Expression of Prediction
Error
Study

Learned visual object pairings
Monkey inferotemporal cortex (IT)
Enhanced ﬁring rate
Meyer and Olson, 2011

Natural image statistics
Monkey V1, V2, V3
Enhanced ﬁring rate
Hupe´ et al., 1998; Bullier et al.,
1996; Bair et al., 2003

Repetitive auditory stream
Early human auditory cortex
Enhanced event-related potentials
(ERPs), enhanced gamma-band
power

Garrido et al., 2007, 2009;
Todorovic et al., 2011

Coherence of visual form and
motion

Human V1, V2, V3, V4, V5/MT
Enhanced BOLD response
Murray et al., 2002, 2006;
Harrison et al., 2007

Audio-visual congruence of
speech

Visual and auditory cortex
Gamma-band oscillatory activity
Arnal et al., 2011

Predictability of visual stimuli
as a function of attention

Human V1, V2, V3
Enhanced BOLD response when
unattended, reduced BOLD when
attended

Kok et al., 2012

Hierarchical expectations in
auditory sequences

Human temporal cortex
Enhanced ERPs
Wacongne et al., 2011

Expected repetition (or alternation)
of face stimuli

FFA in fMRI, parietal and central
electrodes of EEG

Enhanced BOLD response,
diminished repetition suppression
of ERP

Summerﬁeld et al., 2008, 2011

Apparent motion of visual stimulus
V1
Enhanced BOLD response
Alink et al., 2010

700
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective

> Figure description (generated): This input is a table, not a figure requiring visual description in the manner of a schematic or plot. Therefore, I will provide an exhaustive structural and content description of the provided table based on its layout and contents.

***

## Exhaustive Description of the Provided Table

The provided content is a structured, multi-column table summarizing findings related to specific cognitive phenomena and the neural correlates associated with them.

### 1. Overall Layout & Structure
The table is organized into five distinct columns, presenting a structured mapping between cognitive predictions/violations and the corresponding neuroscientific findings. The structure is highly tabular, designed for comparative data presentation.

### 2. Column Breakdown and Content
The table is divided into the following five columns:

*   **Column 1: Prediction Violated:** This column lists the specific cognitive prediction or phenomenon that is being violated or tested.
*   **Column 2: Area Studied:** This column specifies the anatomical brain region or cortical area where the study was conducted.
*   **Column 3: Error:** This column describes the type of neural response or error metric observed in the studies.
*   **Column 4: Study:** This column lists the citation(s) corresponding to the findings.

### 3. Detailed Row-by-Row Content Analysis (Data Trends & Details)
The table contains 9 distinct rows detailing different experimental findings:

**Row 1:**
*   **Prediction Violated:** Learned visual object pairings
*   **Area Studied:** Monkey inferotemporal cortex (IT)
*   **Error:** Enhanced firing rate
*   **Study:** Meyer and Olson, 2011

**Row 2:**
*   **Prediction Violated:** Natural image statistics
*   **Area Studied:** Monkey V1, V2, V3
*   **Error:** Enhanced firing rate
*   **Study:** Hupé et al., 1998; Bullier et al., 1996; Bair et al., 2003

**Row 3:**
*   **Prediction Violated:** Repetitive auditory stream
*   **Area Studied:** Early human auditory cortex
*   **Error:** Enhanced event-related potentials (ERPs), enhanced gamma-band power
*   **Study:** Garrido et al., 2007, 2009; Todorovic et al., 2011

**Row 4:**
*   **Prediction Violated:** Coherence of visual form and motion
*   **Area Studied:** Human V1, V2, V3, V4, V5/MT
*   **Error:** Enhanced BOLD response
*   **Study:** Murray et al., 2002, 2006; Harrison et al., 2007

**Row 5:**
*   **Prediction Violated:** Audio-visual congruence of speech
*   **Area Studied:** Visual and auditory cortex
*   **Error:** Gamma-band oscillatory activity
*   **Study:** Arnal et al., 2011

**Row 6:**
*   **Prediction Violated:** Predictability of visual stimuli as a function of attention
*   **Area Studied:** Human V1, V2, V3
*   **Error:** Enhanced BOLD response when unattended, reduced BOLD when attended
*   **Study:** Kok et al., 2012

**Row 7:**
*   **Prediction Violated:** Hierarchical expectations in auditory sequences
*   **Area Studied:** Human temporal cortex
*   **Error:** Enhanced ERPs
*   **Study:** Wacongne et al., 2011

**Row 8:**
*   **Prediction Violated:** Expected repetition (or alternation) of face stimuli
*   **Area Studied:** FFA in fMRI, parietal and central electrodes of EEG
*   **Error:** Enhanced BOLD response, diminished repetition suppression of ERP
*   **Study:** Summerfield et al., 2008, 2011

**Row 9:**
*   **Prediction Violated:** Apparent motion of visual stimulus
*   **Area Studied:** V1
*   **Error:** Enhanced BOLD response
*   **Study:** Alink et al., 2010

### Summary of Visual Elements
The table uses standard text formatting. There are no graphical elements, color coding (beyond standard black text), or complex symbols; the structure relies entirely on clear textual categorization across five defined columns.


---

## Page 7

Superﬁcial and deep layers are anatomically interconnected,
but mounting evidence suggests that they constitute functionally
distinct processing streams: in an elegant experiment, Roopun
et al. (2006) showed that L2/3 of rat somatomotor cortex shows
prominent gamma oscillations that are coexpressed with beta
oscillations in L5. Both rhythms persisted when superﬁcial and
deep layers were disconnected at the level of L4. Maier et al.
(2010) used multilaminar recordings to show strong local ﬁeld
potential (LFP) coherence among sites within the superﬁcial
layers (the superﬁcial compartment), as well as strong coher-
ence among sites in deep layers (the deep compartment) but
weak intercompartment coherence. These studies indicate a
segregation of—potentially autonomous—supragranular and
infragranular dynamics. Maier et al. (2010) found that supragra-
nular sites had higher broadband gamma power than infragranu-
lar sites. This pattern was reversed in the alpha and beta range,
with greater power in the infragranular and granular layers.
Finally, the spiking activity of neurons in the superﬁcial layers
of visual cortex are more coherent with gamma-frequency oscil-
lations in the local ﬁeld potential, while neurons in deep layers are
more coherent with alpha-frequency oscillations (Buffalo et al.,
2011). This ﬁnding is consistent with an earlier study by Living-
stone (1996) showing that 50% of cells in L2/3 of squirrel monkey
V1 expressed gamma oscillations, compared to less than 20%
of cells in L4C and infragranular layers. The different spectral
behavior of superﬁcial and deep layers has led to the interesting
proposal that feedforward and feedback signaling may be medi-
ated by distinct (high and low) frequencies (reviewed in Wang,
2010; see also Buschman and Miller, 2007), a proposal that
has recently received experimental support, at least for the feed-
forward connections (Bosman et al., 2012; see also Gregoriou
et al., 2009).
Integration and Segregation within Canonical Circuits
Given this functional and anatomical segregation into parallel
streams, the question naturally arises, how are these streams
integrated? It has been previously suggested that integration
occurs through the synchronized ﬁring of multiple neurons that
form a neural ensemble (Gray et al., 1989; Singer, 1999), while
others have emphasized interareal phase synchronization or
coherence (Varela et al., 2001; Fries, 2005; Fujisawa and Buz-
sa´ ki, 2011). While a full treatment of this question is beyond
the scope of the current Perspective, we propose that the canon-
ical microcircuit contains a clue for how the dialectic between
segregation and integration might be resolved. While top-down
and bottom-up inputs and outputs may be segregated in layers,
streams, and frequency bands, the canonical microcircuit spec-
iﬁes the circuitry for how the basic units of cortex are intercon-
nected and therefore how the intrinsic activity of the cortical
column is entrained by extrinsic inputs. This intrinsic connectivity
speciﬁes how the cells of origin and termination of extrinsic
projections are interconnected and thus determines how top-
down and bottom-up streams are integrated within each cortical
column.

Spatial Segregation and Cortical Columns
The notion of a canonical microcircuit implicitly assumes that
each circuit is distinct from its neighbors, which could presum-
ably carry out computations in parallel. Therefore, the canonical

microcircuit speciﬁes the spatial scale over which processing is
integrated. The most likely candidate for this spatial scale is the
cortical column, which can vary over three orders of magnitude
between minicolumns, columns, and hypercolumns. Minicol-
umns are only a few cells wide, estimated to be about 50–
60 mm in diameter by Mountcastle (1997) and are seen in Nissl
sections of cortex as slight variations in cell density. Minicolumns
were originally proposed as elementary units of cortex by Lor-
ente de No (1949) and appear to reﬂect the migration of cells
from the ventricular zone to the cortical sheet during fetal devel-
opment (reviewed in Horton and Adams, 2005). Hubel and Wie-
sel estimated that orientation columns were on this order of
magnitude, about 25–50 mm wide, although they failed to estab-
lish a correspondence between orientation columns observed
physiologically and the minicolumns seen in Nissl sections
(Hubel and Wiesel, 1974). A cortical column was classically
deﬁned as a vertical alignment of cells containing neurons with
similar receptive ﬁeld properties, such as orientation preference
and ocular dominance in V1 or touch in somatosensory cortex
(Mountcastle, 1957; Hubel and Wiesel, 1972). These columns
were suggested by Mountcastle to encompass a number of
minicolumns, with a width of 300–400 mm (Mountcastle, 1997).
Finally, Hubel and Wiesel deﬁned a hypercolumn to be the unit
of cortex necessary to traverse all possible values of a particular
receptive ﬁeld property, such as orientation or eye dominance,
estimated to be between 0.5 and 1 mm wide (Hubel and Wiesel,
1974).
Columns, Connections, and Computations
So is the cortical column the basic unit of cortical computation?
Some authors emphasize that even within a dendrite, there
are all the necessary biophysical mechanisms for performing
surprisingly advanced computations, such as direction selec-
tivity, coincidence detection, or temporal integration (Ha¨ usser
and Mel, 2003; London and Ha¨ usser, 2005). Others argue that
single neurons can process their inputs at the dendrite, soma,
and initial segment, such that the output spike trains of just
two interconnected cells could mediate computations like
independent components analysis (Klampﬂet al., 2009). Others
posit that cortical columns form the basic computational unit
(Mountcastle, 1997; Hubel and Wiesel, 1972; but see Horton
and Adams, 2005). Donald Hebb proposed that neurons distrib-
uted over several cortical areas could form a functional compu-
tational unit called a neural assembly (Hebb, 1949). This view
has re-emerged in recent years, with the development of the
requisite recording and analytic techniques for evaluating this
proposal (Buzsa´ ki, 2010; Canolty et al., 2010; Singer et al.,
1997; Lopes-dos-Santos et al., 2011).
Computational
modeling
studies
indicate
that
cortical
columns with structured connectivity are computationally more
efﬁcient than a network containing the same number of neurons
but with random connectivity (Haeusler and Maass, 2007).
Others suggest that this circuitry allows the cortex to organize
and integrate bottom-up, lateral, and top-down information (Ull-
man, 1995; Raizada and Grossberg, 2003). Douglas and Martin
suggest that the rich anatomical connectivity of L2/3 pyramidal
cells allows them to collect information from top-down, lateral,
and bottom-up inputs, and—through processing in the dendritic
tree—select the most likely interpretation of its inputs. More

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
701

Neuron
Perspective


---

## Page 8

recently, George and Hawkins have suggested that the canon-
ical microcircuit implements a form of Bayesian processing
(George and Hawkins, 2009). In the following section, we pursue
similar ideas but ground them in the framework of predictive
coding and propose a cortical circuit that could implement
predictive coding through canonical interconnections. In partic-
ular, we ﬁnd that the proposed circuitry agrees remarkably well
with quantitative characterizations of the canonical microcircuit
(Haeusler and Maass, 2007).

A Canonical Microcircuit for Predictive Coding
This section considers the computational role of cortical micro-
circuitry in more detail. We try to show that the computations
performed by canonical microcircuits can be speciﬁed more
precisely than one might imagine and that these computations
can be understood within the framework of predictive coding.
In brief, we will show that (hierarchical Bayesian) inference about
the causes of sensory input can be cast as predictive coding.
This is important because it provides formal constraints on the
dynamics one would expect to ﬁnd in neuronal circuits. Having
established these constraints, we then attempt to match them
with the neurobiological constraints afforded by the canonical
microcircuit. The endpoint of this exercise is a canonical micro-
circuit for predictive coding.

Predictive Coding and the Free Energy Principle
It might be thought impossible to specify the computations per-
formed by the brain. However, there are some fairly fundamental
constraints on the basic form of neuronal dynamics. The argu-
ment goes as follows—and can be regarded as a brief summary
of the free energy principle (see Friston, 2010 for details).

d Biological systems are homeostatic (or allostatic), which

means that they minimize the dispersion (entropy) of their
interoceptive and exteroceptive states.

d Entropy is the average of surprise over time, which means

that biological systems minimize the surprise associated
with their sensory states at each point in time.

d In statistics, surprise is the negative logarithm of Bayesian

model evidence, which means that biological systems—
like the brain—must continually maximize the Bayesian
evidence for their (generative) model of sensory inputs.

d Maximizing Bayesian model evidence corresponds to

Bayesian ﬁltering of sensory inputs. This is also known as
predictive coding.

These arguments mean that by minimizing surprise, through
selecting appropriate sensations, the brain is implicitly maximizing
the evidence for its own existence—this is known as active infer-
ence. In other words, to maintain a homeostasis, the brain must
predict its sensory states on the basis of a model. Fulﬁlling those
predictions corresponds to accumulating evidence for that
model—and the brain that embodies it. The implicit maximization
of Bayesian model evidence provides an important link to the
Bayesian brain hypothesis (Hinton and van Camp, 1993; Dayan
et al., 1995; Knill and Pouget, 2004) and many other compelling
proposals about perceptual synthesis, including analysis by
synthesis (Neisser, 1967; Yuille and Kersten, 2006), epistemolog-
ical automata (MacKay, 1956), the principle of minimum redun-

dancy (Attneave, 1954; Barlow, 1961; Dan et al., 1996), the Info-
max principle (Linsker, 1990; Atick, 2011; Kay and Phillips,
2011),andperceptionashypothesistesting(Gregory,1968,1980).
The most popular scheme—for Bayesian ﬁltering in neuronal
circuits—is predictive coding (Srinivasan et al., 1982; Buchs-
baum and Gottschalk, 1983; Rao and Ballard, 1999). In this
context, surprise corresponds (roughly) to prediction error. In
predictive coding, top-down predictions are compared with
bottom-up sensory information to form a prediction error.
This prediction error is used to update higher-level representa-
tions, upon which top-down predictions are based. These opti-
mized predictions then reduce prediction error at lower levels.

To predict sensations, the brain must be equipped with a
generative model of how its sensations are caused (Helmholtz,
1860). Indeed, this led Geoffrey Hinton and colleagues to
propose that the brain is an inference (Helmholtz) machine (Hin-
ton and Zemel, 1994; Dayan et al., 1995). A generative model
describes how variables or causes in the environment conspire
to produce sensory input. Generative models map from (hidden)
causes to (sensory) consequences. Perception then corre-
sponds to the inverse mapping from sensations to their causes,
while action can be thought of as the selective sampling of
sensations. Crucially, the form of the generative model dictates
the form of the inversion—for example, predictive coding. Fig-
ure 3 depicts a general model as a probabilistic graphical
model. A special case of these models are hierarchical dynamic
models (see Figure 4), which grandfather most parametric
models in statistics and machine learning (see Friston, 2008).
These models explain sensory data in terms of hidden causes
and states. Hidden causes and states are both hidden variables
that cause sensations but they play slightly different roles:
hidden causes link different levels of the model and mediate
conditional dependencies among hidden states at each level.
Conversely, hidden states model conditional dependencies
over time (i.e., memory) by modeling dynamics in the world. In
short, hidden causes and states mediate structural and dynamic
dependencies, respectively.

The details of the graph in Figure 3 are not important; it just
provides a way of describing conditional dependencies among
hidden states and causes responsible for generating sensory
input. These dependencies mean that we can interpret neuronal
activity as message passing among the nodes of a generative
model, in which each canonical microcircuit contains represen-
tations or expectations about hidden states and causes. In other
words, the form of the underlying generative model deﬁnes
the form of the predictive coding architecture used to invert the
model. This is illustrated in Figure 4, where each node has a single
parent. We will deal with this simple sort of model because it
lends itself to an unambiguous description in terms of bottom-
up (feedforward) and top-down (feedback) message passing.
We now look at how perception or model inversion—recovering
the hidden states and causes of this model given sensory data—
might be implemented at the level of a microcircuit.

Predictive Coding and Message Passing
In predictive coding, representations (or conditional expecta-
tions) generate top-down predictions to produce prediction
errors. These prediction errors are then passed up the hierarchy

702
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective


---

## Page 9

in the reverse direction, to update conditional expectations. This
ensures an accurate prediction of sensory input and all its inter-
mediate representations. This hierarchal message passing can
be expressed mathematically as a gradient descent on the
(sum of squared) prediction errors xðiÞ = PðiÞ~εðiÞ, where the predic-
tion errors are weighted by their precision (inverse variance):

_~m

ðiÞ

v = D~mðiÞ

v  v~v~εðiÞ,xðiÞ  xði + 1Þ

v

_~m

ðiÞ

x = D~mðiÞ

x  v~x~εðiÞ,xðiÞ

xðiÞ

v = PðiÞ

v ~εðiÞ

v = PðiÞ

v



~mði1Þ

v
 gðiÞ

~mðiÞ

x ; ~mðiÞ

v



xðiÞ

x = PðiÞ

x ~εðiÞ

x = PðiÞ

x



D~mðiÞ

x  fðiÞ

~mðiÞ

x ; ~mðiÞ

v



:
(1)

The ﬁrst pair of equalities just says that conditional expecta-
tions about hidden causes and states ð~mðiÞ

v ; ~mðiÞ

x Þ are updated
based upon the way we would predict them to change—the ﬁrst
term—and subsequent terms that minimize prediction error. The
second pair of equations simply expresses prediction error
ðxðiÞ

v ; xðiÞ

x Þ as the difference between conditional expectations
about hidden causes and (the changes in) hidden states and their
predicted values, weighed by their precisions ðPðiÞ

v ; PðiÞ

x Þ. These
predictions are nonlinear functions of conditional expectations
ðgðiÞ; fðiÞÞ at each level of the hierarchy and the level above.

It is difﬁcult to overstate the generality and importance of
Equation (1)—it grandfathers nearly every known statistical esti-
mation scheme, under parametric assumptions about additive
noise. These range from ordinary least squares to advanced
Bayesian ﬁltering schemes (see Friston, 2008). In this general

“A bird in song”

Figure 3. Hierarchical Generative Models
This schematic shows an example of a generative model. Generative models describe how (sensory) data are caused. In this ﬁgure, sensory states (blue circles on
the periphery) are generated by hidden variables (in the center). Left: the model as a probabilistic graphical model, in which unknown variables (hidden causes and
states) are associated with the nodes of a dependency graph and conditional dependencies are indicated by arrows. Hidden states confer memory on the model
by virtue of having dynamics, while hidden causes connect nodes. A graphical model describes the conditional dependencies among hidden variables generating
data. These dependencies are typically modeled as (differential) equations with nonlinear mappings and random ﬂuctuations ~uðiÞ with precision (inverse variance)
PðiÞ (see the equations in the insert on the left). This allows one to specify the precise form of the probabilistic generative model and leads to a simple and efﬁcient
inversion scheme (predictive coding; see Figure 4). Here ~vpaðiÞ denotes the set of hidden causes that constitute the parents of sensory ~sðiÞ or hidden ~xðiÞ states. The
‘‘’’ indicates states in generalized coordinates of motion: ~x = ðx; x0; x00; .Þ. Right: an intuitive version of the model: here, we imagine that a singing bird is the cause
of sensations, which—through a cascade of dynamical hidden states—produces modality-speciﬁc consequences (e.g., the auditory object of a bird song and the
visual object of a song bird). These intermediate causes are themselves (hierarchically) unpacked to generate sensory signals. The generative model therefore
maps from causes (e.g., concepts) to consequences (e.g., sensations), while its inversion corresponds to mapping from sensations to concepts or represen-
tations. This inversion corresponds to perceptual synthesis, in which the generative model is used to generate predictions. Note that this inversion implicitly
resolves the binding problem by explaining multisensory cues with a single cause.

> Figure caption (from PDF text): Figure 3. Hierarchical Generative Models
This schematic shows an example of a generative model. Generative models describe how (sensory) data are caused. In this ﬁgure, sensory states (blue circles on
the periphery) are generated by hidden variables (in the center). Left: the model as a probabilistic graphical model, in which unknown variables (hidden causes and
states) are associated with the nodes of a dependency graph and conditional dependencies are indicated by arrows. Hidden states confer memory on the model
by virtue of having dynamics, while hidden causes connect nodes. A graphical model describes the conditional dependencies among hidden variables generating
data. These dependencies are typically modeled as (differential) equations with nonlinear mappings and random ﬂuctuations ~uðiÞ with precision (inverse variance)
PðiÞ (see the equations in the insert on the left). This allows one to specify the precise form of the probabilistic generative model and leads to a simple and efﬁcient
inversion scheme (predictive coding; see Figure 4). Here ~vpaðiÞ denotes the set of hidden causes that constitute the parents of sensory ~sðiÞ or hidden ~xðiÞ states. The
‘‘’’ indicates states in generalized coordinates of motion: ~x = ðx; x0; x00; .Þ. Right: an intuitive version of the model: here, we imagine that a singing bird is the cause
of sensations, which—through a cascade of dynamical hidden states—produces modality-speciﬁc consequences (e.g., the auditory object of a bird song and the
visual object of a song bird). These intermediate causes are themselves (hierarchically) unpacked to generate sensory signals. The generative model therefore
maps from causes (e.g., concepts) to consequences (e.g., sensations), while its inversion corresponds to mapping from sensations to concepts or represen-
tations. This inversion corresponds to perceptual synthesis, in which the generative model is used to generate predictions. Note that this inversion implicitly
resolves the binding problem by explaining multisensory cues with a single cause.
> Figure description (generated): ## Detailed Figure Description: Hierarchical Generative Models

This figure, titled "Figure 3. Hierarchical Generative Models," is divided into two distinct conceptual panels: a formal probabilistic graphical model on the left, and an intuitive, concept-driven diagram on the right.

### 1. Overall Layout & Structure

The figure is structured horizontally, presenting two complementary views of a generative model:
*   **Left Panel:** A complex probabilistic graphical model, represented as a dependency graph. This panel is highly technical and uses mathematical notation to denote variables and dependencies.
*   **Right Panel:** An intuitive, conceptual diagram illustrating the hierarchical flow from high-level causes (concepts) down to sensory consequences.

### 2. Visual Components & Symbols (Left Panel: Probabilistic Graphical Model)

The left panel depicts a network of interconnected nodes representing variables.

*   **Nodes:** Nodes are represented by circles, differentiated by color and position:
    *   **Blue Circles (Periphery):** Labeled as "Sensory states." These are located on the outer edges of the diagram.
    *   **Black Circles (Center/Intermediate):** Labeled as "Hidden states." These form the core of the network.
    *   **Black Circles (Upper/Lower):** Labeled as "Hidden causes." These are positioned higher and lower in the structure, suggesting different levels of abstraction or causation.
*   **Connections (Arrows):** Directed arrows indicate conditional dependencies, showing the flow of influence from causes/states to sensory outputs.
*   **Structure:** The model exhibits a hierarchical structure, with variables at the top (causes) influencing intermediate states, which in turn generate sensory data at the periphery.

### 3. Visual Components & Symbols (Right Panel: Intuitive Model)

The right panel presents a more metaphorical, flow-based representation.

*   **Central Concept:** A large cloud shape labeled **"A bird in song"** sits at the top, representing a high-level concept.
*   **Hierarchical Flow:** The diagram flows downward from this central concept through several layers of intermediate causes and sensory modalities.
*   **Nodes/Boxes:** Various nodes represent different levels of abstraction:
    *   **Top Level:** The "A bird in song" concept.
    *   **Intermediate Causes/States:** Nodes are connected sequentially, representing a cascade of dynamical hidden states.
    *   **Sensory Modalities:** Specific sensory inputs are shown at the bottom, linked to their respective intermediate causes.
*   **Sensory Representations:** Specific sensory inputs are illustrated with small images:
    *   An image representing **Auditory sensations** (sound waves/waveform).
    *   An image representing **Visual sensations** (a picture of a bird on a branch).
    *   A small image representing **Auditory percept** (implied sound/waveform context).
    *   A small image representing **Visual percept** (a bird in flight/song context).
*   **Labels:** Key labels define the flow: **"Interception," "Concept," "Auditory percept," "Visual percept," "Auditory sensations,"** and **"Visual sensations."**

### 4. Labels, Keys & Legends (Mathematical Notations - Left Panel)

The left panel includes specific mathematical notations associated with the nodes and connections:

*   **Variables:** Nodes are labeled using superscripts indicating time steps or states, e.g., $\tilde{x}^{(t)}$, $\tilde{\nu}_{pa}^{(i)}$.
*   **Dependencies:** The caption explains that $\tilde{v}_{pa}^{(i)}$ denotes the set of hidden causes that constitute the parents of sensory $\tilde{s}_{di}$ or hidden $\tilde{x}_{di}$ states.
*   **Coordinates:** The notation $\tilde{x} = (\dot{x}; x_0; \ddot{x}_0, \dots)$ indicates states in generalized coordinates of motion.
*   **Equations (Referenced):** The caption refers to equations in an insert on the left, mentioning nonlinear mappings and random fluctuations $\sim u_{di}$ with precision $P_{di}$.

### 5. Contextual Caption Integration (Functional Explanation)

The caption provides functional context for the visual elements:

*   **Generative Function:** The model describes how (sensory) data are caused.
*   **Left Panel Interpretation:** It is a probabilistic graphical model where unknown variables (hidden causes and states) are nodes, and arrows indicate conditional dependencies. Hidden states confer memory via dynamics, while hidden causes connect nodes.
*   **Right Panel Interpretation:** This is an intuitive version where a singing bird (the cause) generates modality-specific consequences (auditory and visual sensations) through a cascade of dynamical hidden states.
*   **Inversion:** The generative model maps from causes $\rightarrow$ consequences (sensations); its inversion corresponds to mapping sensations $\rightarrow$ concepts/representations, which is identified as perceptual synthesis.
*   **Binding Problem:** The caption notes that this inversion implicitly resolves the binding problem by explaining multisensory cues with a single cause.

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
703

Neuron
Perspective


---

## Page 10

setting, Equation (1) minimizes variational free energy and corre-
sponds to generalized predictive coding. Under linear models, it
reduces to linear predictive coding, also known as Kalman-Bucy
ﬁltering (see Friston, 2010 for details).

In neuronal network terms, Equation (1) says that prediction
error units receive messages from the same level and the level
above. This is because the hierarchical form of the model only
requires conditional expectations from neighboring levels to
form prediction errors, as can be seen schematically in Figure 4.
Conversely, expectations are driven by prediction error from the
same level and the level below—updating expectations about
hidden states and causes respectively. These constitute the
bottom-up and lateral messages that drive conditional expecta-
tions to provide better predictions—or representations—that
suppress prediction error. This updating corresponds to an accu-
mulation of prediction errors, in that the rate of change of condi-
tionalexpectationsisproportionaltopredictionerror.Electrophys-
iologically, this means that one would expect to see a transient
prediction error response to bottom-up afferents (in neuronal
populations encoding prediction error) that is suppressed to
baseline ﬁring rates by sustained responses (in neuronal popu-
lations encoding predictions). This is the essence of recurrent
message passing between hierarchical levels to suppress predic-
tion error (see Friston, 2008 for a more detailed discussion).

The nature of this message passing is remarkably consistent
with the anatomical and physiological features of cortical hierar-
chies. An important prediction is that the nonlinear functions of
the generative model—modeling context-sensitive dependen-
cies among hidden variables—appear only in the top-down
and lateral predictions. This means, neurobiologically, we would
predict feedback connections to possess nonlinear or neuromo-
dulatory characteristics, in contrast to feedforward connections
that mediate a linear mixture of prediction errors. This functional
asymmetry is exactly consistent with the empirical evidence
reviewed above. Another key feature of Equation (1) is that the
top-down predictions produce prediction errors through sub-
traction. In other words, feedback connections should exert
inhibitory effects, of the sort seen empirically. Table 2 summa-
rizes the features of extrinsic connectivity (reviewed in the pre-
vious section) that are explained by predictive coding. In the

remainder of this Perspective, we focus on intrinsic connections
and cortical microcircuits.

The Cortical Microcircuit and Predictive Coding
We now try to associate the variables in Equation (1) with speciﬁc
populations in the canonical microcircuit. Figure 5 illustrates
a remarkable correspondence between the form of Equation
(1) and the connectivity of the canonical microcircuit. Further-
more, the resulting scheme corresponds almost exactly to the
computational architecture proposed by Mumford (1992). This
correspondence rests upon the following intuitive steps.

d First, we divide the excitatory cells in the superﬁcial

and deep layers into principal (pyramidal) cells and excit-
atory interneurons. This accommodates the fact that (in
macaque V1) a signiﬁcant percentage of superﬁcial L2/3
cells (about half) and deep L5 excitatory cells (about
80%) do not project outside the cortical column (Callaway
and Wiser, 1996; Briggs and Callaway, 2005).

d Second, we know that the superﬁcial and deep pyramidal

cells provide feedforward and feedback connections,
respectively. This means that superﬁcial pyramidal cells
must encode and broadcast prediction errors on hidden
causes xði + 1Þ

v
, while deep pyramidal cells must encode
conditional expectations ð~mðiÞ

v ; ~mðiÞ

x Þ so that they can elabo-
rate feedback predictions.

d Third, we know that the (spiny stellate) excitatory cells in

the granular layer receive feedforward connections encod-
ing prediction errors xðiÞ

v on the hidden causes of the level
below.

d This leaves the inhibitory interneurons in the granular layer,

which, for symmetry, we associate with prediction errors
on the hidden states.

d The remaining populations are the excitatory and inhibi-

tory interneurons in the supragranular layer, to which we
assign expectations about hidden causes and states,
respectively. These are mapped through descending
(intrinsic) feedforward connections to cells in the deep
layers that generate predictions. We do not suppose that
this is a simple one-to-one mapping—rather it mediates

Figure 4. Hierarchical Inference and
Predictive Coding
This
ﬁgure
describes
the
predictive
coding
scheme associated with a simple hierarchical
model shown on the left. In this model each node
has a single parent. The ensuing inversion or
generalized predictive coding scheme is shown on
the right. The key quantities in this scheme are
(conditional) expectations of the hidden states and
causes and their associated prediction errors. The
basic architecture—implied by the inversion of the
graphical
(hierarchical)
model—suggests
that
prediction errors (caused by unpredicted ﬂuctua-
tions in hidden variables) are passed up the hier-
archy to update conditional expectations. These
conditional expectations now provide predictions
that are passed down the hierarchy to form
prediction errors. We presume that the forward
and backward message passing between hierarchical levels is mediated by extrinsic (feedforward and feedback) connections. Neuronal populations encoding
conditional expectations and prediction errors now have to be deployed in a canonical microcircuit to understand the computational logic of intrinsic
connections—within each level of the hierarchy—as shown in the next ﬁgure.

704
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective

> Figure description (generated): This figure presents a schematic diagram illustrating a sequential or hierarchical flow, likely representing a computational model or a neural processing pipeline.

**1. Overall Layout & Structure:**
The diagram is structured horizontally, depicting a progression from left to right. It consists of two main layers of nodes: an upper layer containing input/driving signals, and a lower layer representing the core processing sequence. The flow is directional, indicated by arrows connecting nodes across these layers.

**2. Visual Components & Symbols:**
The diagram utilizes circular nodes of varying colors to represent states or variables, connected by directed arrows indicating the flow of information.

*   **Upper Layer Nodes (Input/Driving Signals):** There are five nodes in the top row. These nodes are colored light red/pink and contain mathematical notations:
    *   $\tilde{\omega}_v^{(3)}$ (Far left)
    *   $\tilde{\omega}_x^{(2)}$
    *   $\tilde{\omega}_v^{(2)}$
    *   $\tilde{\omega}_x^{(1)}$
    *   $\tilde{\omega}_v^{(1)}$ (Far right)

*   **Lower Layer Nodes (Processing Sequence):** There are four primary nodes in the bottom row, representing sequential processing steps:
    *   $\tilde{\nu}^{(2)}$ (Far left) - Black outline, white fill.
    *   $\tilde{\chi}^{(2)}$ - Orange fill.
    *   $\tilde{\nu}^{(1)}$ - Black outline, white fill.
    *   $\tilde{\chi}^{(1)}$ - Orange fill.
    *   $\tilde{\nu}^{(0)}$ (Far right) - Blue outline, white fill.

*   **Connections and Flow:**
    *   Arrows flow from the upper layer nodes down to the corresponding lower layer nodes. For example, $\tilde{\omega}_v^{(3)}$ points down to $\tilde{\nu}^{(2)}$.
    *   The lower layer nodes are connected sequentially by arrows: $\tilde{\nu}^{(2)} \rightarrow \tilde{\chi}^{(2)} \rightarrow \tilde{\nu}^{(1)} \rightarrow \tilde{\chi}^{(1)} \rightarrow \tilde{\nu}^{(0)}$.
    *   A large, shaded gray area encompasses the sequence from $\tilde{\chi}^{(2)}$ through $\tilde{\nu}^{(0)}$, suggesting a specific processing block or regime.
    *   A faint, light blue arrow extends horizontally from $\tilde{\nu}^{(0)}$ towards the right edge of the figure, suggesting an output or continuation beyond the depicted sequence.

**3. Labels, Keys & Legends:**
The labels are mathematical variables denoted by $\tilde{\cdot}$ (tilded variable) followed by a subscript indicating the index or stage, and sometimes superscripts for dimensionality (e.g., $(3), (2), (1), (0)$).

**4. Data Trends & Details:**
As this is a schematic diagram and not a plot, there are no axes or data trends to describe. The structure itself implies a temporal or hierarchical progression from index 3 down to index 0.

**5. Contextual Caption Integration:**
The figure structure strongly suggests a multi-stage dynamical system or recurrent network where $\tilde{\omega}$ represents driving inputs (indexed by $v$ and $x$), while the sequence $\tilde{\nu}^{(2)} \rightarrow \tilde{\chi}^{(2)} \rightarrow \tilde{\nu}^{(1)} \rightarrow \tilde{\chi}^{(1)} \rightarrow \tilde{\nu}^{(0)}$ represents the core state evolution across different time steps or layers (indexed 2 down to 0). The color coding distinguishes between the $\tilde{\nu}$ nodes (black outline) and the $\tilde{\chi}$ nodes (orange fill).

> Figure description (generated): This figure appears to be a schematic diagram illustrating a dynamic system, likely representing recurrent neural network dynamics or state evolution over discrete time steps.

### 1. Overall Layout & Structure
The diagram is structured horizontally, depicting a sequence of states or time steps progressing from left to right. The overall structure resembles a flow chart or a state transition diagram, contained within a large, shaded, tapering gray area that suggests progression over time or depth.

### 2. Visual Components & Symbols
The diagram features several distinct nodes (circles) representing different states or variables, and directed arrows indicating transitions between these states.

**Nodes (States):**
The nodes are color-coded and labeled with Greek letters ($\zeta$ or $\tilde{\mu}$):

*   **Blue Nodes (e.g., $\tilde{\mu}_v^{(0)}$):** These nodes are located at the beginning of the sequence and represent a specific state variable, $\tilde{\mu}_v$.
*   **Orange Nodes (e.g., $\tilde{\mu}_x^{(1)}$):** These nodes represent another state variable, $\tilde{\mu}_x$, appearing sequentially.
*   **Black Nodes (e.g., $\tilde{\mu}_v^{(1)}$):** These nodes represent the state variable $\tilde{\mu}_v$ at later time steps.

The sequence progresses through indexed states:
*   Time Step 0: $\tilde{\mu}_v^{(0)}$ (Blue)
*   Time Step 1: $\tilde{\mu}_x^{(1)}$ (Orange), $\tilde{\mu}_v^{(1)}$ (Black)
*   Time Step 2: $\tilde{\mu}_x^{(2)}$ (Orange), $\tilde{\mu}_v^{(2)}$ (Black)
*   Time Step 3: $\zeta_x^{(3)}$ (Red), $\tilde{\mu}_v^{(3)}$ (Black)

**Connections and Flow:**
1.  **Forward Progression:** There are implied transitions moving from left to right, indicated by the overall structure and connections between adjacent time steps.
2.  **Internal Connections (Within a Step):** Within the sequence, there are connections showing how states influence each other at subsequent steps.
3.  **Feedback/Cross-Layer Connections:** Several curved arrows indicate non-sequential or feedback connections between nodes across different time steps.

**Specific Connections Observed:**
*   From $\tilde{\mu}_v^{(0)}$ (Blue) to $\zeta_v^{(1)}$ (Red).
*   From $\tilde{\mu}_x^{(1)}$ (Orange) to $\zeta_v^{(2)}$ (Red).
*   From $\tilde{\mu}_v^{(1)}$ (Black) to $\zeta_x^{(2)}$ (Red).
*   From $\tilde{\mu}_x^{(2)}$ (Orange) to $\zeta_v^{(3)}$ (Red).
*   From $\tilde{\mu}_v^{(2)}$ (Black) to $\zeta_x^{(3)}$ (Red).

**Arrows:**
*   Thin, light-colored arrows connect the nodes. These represent directed influence or flow between states.
*   The connections are complex, showing multiple inputs feeding into subsequent nodes (e.g., $\tilde{\mu}_v^{(2)}$ receives input from multiple preceding states).

### 3. Labels, Keys & Legends
**Variables/Labels:**
*   $\tilde{\mu}_v^{(t)}$: State variable $\mu_v$ at time step $t$.
*   $\tilde{\mu}_x^{(t)}$: State variable $\mu_x$ at time step $t$.
*   $\zeta_v^{(t)}$: State variable $\zeta_v$ at time step $t$.
*   $\zeta_x^{(t)}$: State variable $\zeta_x$ at time step $t$.

**Color Coding:**
*   Blue: $\tilde{\mu}_v^{(0)}$ (Initial state)
*   Orange: $\tilde{\mu}_x$ states
*   Black: $\tilde{\mu}_v$ states (later steps)
*   Red: $\zeta_x$ and $\zeta_v$ states

**Annotations:**
*   A large, light gray, tapering shaded area spans the bottom and middle of the diagram, suggesting a temporal or structural progression.
*   A small green rectangular bar is visible at the very bottom, likely indicating a specific layer or parameter setting.

### 4. Data Trends & Details
Since this is a schematic diagram and not a plot, there are no axes or quantitative data trends to describe. The structure illustrates the *connectivity* and *sequence* of states rather than a quantitative evolution over time.

### 5. Contextual Caption Integration
The labels $\tilde{\mu}_v$, $\tilde{\mu}_x$, $\zeta_v$, and $\zeta_x$ strongly suggest this diagram models the interaction between different latent variables or neural representations ($\mu$ and $\zeta$) across discrete time steps ($t=0, 1, 2, 3$). The flow indicates a dynamic system where the state at time $t$ is influenced by states from previous times, forming a recurrent or sequential model structure.


---

## Page 11

the nonlinear transformation of expectations to predictions
required by the earlier cortical level.

This arrangement accommodates the fact that the dependen-
cies among hidden states are conﬁned to each node (by the
nature of graphical models), which means that their expectations
and prediction errors should be encoded by interneurons.
Furthermore, the splitting of excitatory cells in the upper layers
into two populations (encoding expectations and prediction
errors on hidden causes) is sensible, because there is a one-
to-one mapping between the expectations on hidden causes
and their prediction errors.

The ensuing architecture bears a striking correspondence to
the microcircuit in Haeusler and Maass (2007) in the left panel
of Figure 5, in the sense that nearly every connection required
by the predictive coding scheme appears to be present in terms
of quantitative measures of intrinsic connectivity. However, there
are two exceptions that both involve connections to the inhibi-
tory cells in the granular layer (shown as dotted lines in Figure 5).
Predictive coding requires that these cells (which encode predic-
tion errors on hidden states) compare the expected changes in
hidden states with the actual changes. This suggests that there
should be interlaminar projections from supragranular (inhibitory)
and infragranular (excitatory) cells. In terms of their synaptic
characteristics, one would predict that these intrinsic connec-
tions would be of a feedback sort, in the sense that they convey
predictions. Although not considered in this Haeusler and Maass
scheme, feedback connections from infragranular layers are
an established component of the canonical microcircuit (see
Figure 2).

Functional Asymmetries in the Microcircuit
The circuitry in Figure 5 appears consistent with the broad
scheme of ascending (feedforward) and descending (feedback)
intrinsic connections: feedforward prediction errors from a
lower cortical level arrive at granular layers and are passed
forward to excitatory and inhibitory interneurons in supragranular
layers, encoding expectations. Strong and reciprocal intralami-
nar connections couple superﬁcial excitatory interneurons and
pyramidal cells. Excitatory and inhibitory interneurons in supra-
granular layers then send strong feedforward connections to
the infragranular layer. These connections enable deep pyra-
midal cells and excitatory interneurons to produce (feedback)
predictions, which ascend back to L4 or descend to a lower
hierarchical level. This arrangement recapitulates the functional
asymmetries between extrinsic feedforward and feedback con-
nections and is consistent with the empirical characteristics of
intrinsic connections.

If we focus on the superﬁcial and deep pyramidal cells, the
form of the recognition dynamics in Equation (1) tells us some-
thing quite fundamental: we would anticipate higher frequencies
in the superﬁcial pyramidal cells, relative to the deep pyramidal
cells. One can see this easily by taking the Fourier transform of
the ﬁrst equality in Equation (1):

ðjuÞ~mðiÞ

v ðuÞ = D~mðiÞ

v ðuÞ  v~v~εðiÞ,xðiÞðuÞ  xði + 1Þ

v
ðuÞ:
(2)

This equation says that the contribution of any (angular)
frequency u in the prediction errors (encoded by superﬁcial pyra-
midal cells) to the expectations (encoded by the deep pyramidal
cells) is suppressed in proportion to that frequency (Friston,

Table 2. The Functional Correlates of the Anatomy and Physiology of Cortical Hierarchies and Their Extrinsic Connections

Anatomy and Physiology
Functional Correlates

Hierarchical organization of cortical areas (Zeki and Shipp, 1988;
Felleman and Van Essen, 1991; Barone et al., 2000; Vezoli et al., 2004).

Encoding of conditional dependencies in terms of a graphical model
(Mumford, 1992; Rao and Ballard, 1999; Friston, 2008).

Distinct (laminar-speciﬁc) neuronal responses (Douglas et al., 1989;
Douglas and Martin, 1991).

Encoding expected states of the world (superﬁcial pyramidal cells) and
prediction errors (deep pyramidal cells) (Mumford, 1992; Friston, 2008).

Distinct (laminar-speciﬁc) extrinsic connections (Zeki and Shipp,
1988; Felleman and Van Essen, 1991; Barone et al., 2000; Vezoli et al.,
2004; Markov et al., 2011).

Forward connections convey prediction error (from superﬁcial
pyramidal cells) and backward connections convey predictions (from
deep pyramidal cells) (Mumford, 1992; Friston, 2008).

Reciprocal extrinsic connectivity (Zeki and Shipp, 1988; Felleman
and Van Essen, 1991; Barone et al., 2000; Vezoli et al., 2004;
Markov et al., 2011).

Recurrent dynamics are intrinsically stable because they are trying to
suppress prediction error (Crick and Koch, 1998; Friston, 2008).

Feedback extrinsic connections are (driving and) modulatory
(Mignard and Malpeli, 1991; Bullier et al., 1996; Sherman and Guillery,
1998; Covic and Sherman, 2011; De Pasquale and Sherman, 2011).

Forward (driving) and backward (driving and modulatory) connections
mediate the (linear) inﬂuence of prediction errors and the (linear and
nonlinear) construction of predictions (Friston, 2008, 2010).

Feedback extrinsic connections are inhibitory (Murphy and Sillito,
1987; Sillito et al., 1993; Chu et al., 2003; Olsen et al., 2012; Meyer
et al., 2011; Wozny and Williams, 2011).

Top-down predictions suppress or counter prediction errors
produced by bottom-up inputs (Mumford, 1992; Rao and Ballard,
1999; Friston, 2008).

Differences in neuronal dynamics of superﬁcial and deep layers
(de Kock et al., 2007; Sakata and Harris, 2009; Maier et al., 2010;
Bollimunta et al., 2011; Buffalo et al., 2011).

Principal cells elaborating predictions (deep pyramidal cells) may
show distinct (low-pass) dynamics, relative to those encoding error
(superﬁcial pyramidal cells) (Friston, 2008).

Dense intrinsic and horizontal connectivity (Thomson and Bannister,
2003; Ka¨ tzel et al., 2011).
Lateral predictions and prediction errors mediating winnerless
competition and competitive lateral dependencies (Desimone, 1996;
Friston, 2010).

Predominance of nonlinear synaptic (dendritic and neuromodulatory)
infrastructure in superﬁcial layers (Ha¨ usser and Mel, 2003; London
and Ha¨ usser, 2005; Gentet et al., 2012).

Required to scale prediction errors, in proportion to their precision,
affording a form of cortical bias or gain control that encodes
uncertainty (Feldman and Friston, 2010; Spratling, 2008).

Neuron 76, November 21, 2012 ª2012 Elsevier Inc.
705

Neuron
Perspective

> Figure description (generated): Since no image was provided, I cannot generate the detailed description. Please provide the figure you would like me to describe.

Once you provide the image, I will structure my response according to your requirements:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details** (If applicable)
5. **Contextual Caption Integration**

I look forward to analyzing the figure!


---

## Page 12

2008). In other words, high frequencies should be attenuated
when passing from superﬁcial to deep pyramidal cells. There is
nothing mysterious about this attenuation—it is a simple conse-
quence of the fact that conditional expectations accumulate
prediction errors, thereby suppressing high-frequency ﬂuctua-
tions to produce smooth estimates of hidden causes. This
smoothing—inherent in Bayesian ﬁltering—leads to an asym-
metry in frequency content of superﬁcial and deep cells: for
example, superﬁcial cells should express more gamma relative
to beta, and deep cells should express more beta relative to
gamma (Roopun et al., 2006, 2008; Maier et al., 2010).

Figure 6 provides a schematic illustration of the spectral asym-
metry predicted by Equation 2. Note that predictions about the
relative amplitudes of high and low frequencies in superﬁcial
and deep layers pertain to all frequencies—there is nothing in
predictive coding per se to suggest characteristic frequencies
in the gamma and beta ranges. However, one might speculate

that the characteristic frequencies of canonical microcircuits
have evolved to model and—through active inference—create
the sensorium (Berkes et al., 2011; Engbert et al., 2011; Friston,
2010). Indeed, there is empirical evidence to support this notion
in the visual (Lakatos et al., 2008; Meirovithz et al., 2012; Bosman
et al., 2012) and motor (Gwin and Ferris, 2012) domain.

In summary, predictions are formed by a linear accumulation
of prediction errors. Conversely, prediction errors are nonlinear
functions of predictions. This means that the conversion of
prediction errors into predictions (Bayesian ﬁltering) necessarily
entails a loss of high frequencies. However, the nonlinearity in
the mapping from predictions to prediction errors means that
high frequencies can be created (consider the effect of squar-
ing a sine wave, which would convert beta into gamma). In
short, prediction errors should express higher frequencies than
the predictions that accumulate them. This is another ex-
ample of a potentially important functional asymmetry between

Figure 5. A Canonical Microcircuit for Predictive Coding
Left: the canonical microcircuit based on Haeusler and Maass (2007), in which we have removed inhibitory cells from the deep layers because they have very little
interlaminar connectivity. The numbers denote connection strengths (mean amplitude of PSPs measured at soma in mV) and connection probabilities (in
parentheses) according to Thomson et al. (2002). Right: the proposed cortical microcircuit for predictive coding, in which the quantities of the previous ﬁgure have
been associated with various cell types. Here, prediction error populations are highlighted in pink. Inhibitory connections are shown in red, while excitatory
connections are in black. The dotted lines refer to connections that are not present in the microcircuit on the left (but see Figure 2). In this scheme, expectations
(about causes and states) are assigned to (excitatory and inhibitory) interneurons in the supragranular layers, which are passed to infragranular layers. The
corresponding prediction errors occupy granular layers, while superﬁcial pyramidal cells encode prediction errors that are sent forward to the next hierarchical
level. Conditional expectations and prediction errors on hidden causes are associated with excitatory cell types, while the corresponding quantities for hidden
states are assigned to inhibitory cells. Dark circles indicate pyramidal cells. Finally, we have placed the precision of the feedforward prediction errors against the
superﬁcial pyramidal cells. This quantity controls the postsynaptic sensitivity or gain to (intrinsic and top-down) presynaptic inputs. We have previously discussed
this in terms of attentional modulation, which may be intimately linked to the synchronization of presynaptic inputs and ensuing postsynaptic responses (Feldman
and Friston, 2010; Fries et al., 2001).

> Figure caption (from PDF text): Figure 5. A Canonical Microcircuit for Predictive Coding
Left: the canonical microcircuit based on Haeusler and Maass (2007), in which we have removed inhibitory cells from the deep layers because they have very little
interlaminar connectivity. The numbers denote connection strengths (mean amplitude of PSPs measured at soma in mV) and connection probabilities (in
parentheses) according to Thomson et al. (2002). Right: the proposed cortical microcircuit for predictive coding, in which the quantities of the previous ﬁgure have
been associated with various cell types. Here, prediction error populations are highlighted in pink. Inhibitory connections are shown in red, while excitatory
connections are in black. The dotted lines refer to connections that are not present in the microcircuit on the left (but see Figure 2). In this scheme, expectations
(about causes and states) are assigned to (excitatory and inhibitory) interneurons in the supragranular layers, which are passed to infragranular layers. The
corresponding prediction errors occupy granular layers, while superﬁcial pyramidal cells encode prediction errors that are sent forward to the next hierarchical
level. Conditional expectations and prediction errors on hidden causes are associated with excitatory cell types, while the corresponding quantities for hidden
states are assigned to inhibitory cells. Dark circles indicate pyramidal cells. Finally, we have placed the precision of the feedforward prediction errors against the
superﬁcial pyramidal cells. This quantity controls the postsynaptic sensitivity or gain to (intrinsic and top-down) presynaptic inputs. We have previously discussed
this in terms of attentional modulation, which may be intimately linked to the synchronization of presynaptic inputs and ensuing postsynaptic responses (Feldman
and Friston, 2010; Fries et al., 2001).
> Figure description (generated): ## Figure Description: Comparison of Neural Circuit Models

This figure presents a side-by-side comparison of two neural circuit models: the canonical microcircuit based on Haeusler and Maass (2007) on the left, and a proposed cortical microcircuit for predictive coding on the right.

### 1. Overall Layout & Structure
The figure is divided into two distinct schematic panels, positioned horizontally next to each other. Both panels depict hierarchical neural connectivity, suggesting a layered cortical organization. The left panel is labeled "Haeusler and Maass (2007)," while the right panel is titled "Canonical microcircuit for predictive coding."

### 2. Visual Components & Symbols (Left Panel: Haeusler and Maass, 2007)
The left panel illustrates a layered structure with nodes representing different cortical areas.

*   **Layers/Regions:** The vertical axis implies a hierarchy, ranging from "Lower cortical areas and thalamus" at the bottom to "Higher cortical areas" at the top.
*   **Nodes:** Nodes are represented by circles, indicating populations or regions. These nodes are organized into distinct layers: L2/3-E (Excitatory), L4-E, and L5-E.
*   **Connectivity:** Arrows indicate directional flow of information. The connections are annotated with numerical values representing connection strengths (mean amplitude of PSPs in mV) and connection probabilities (in parentheses).
*   **Input/Output:** Arrows labeled "Input (feedback) stream 2" and "Input (feedforward) stream 1" enter the system, suggesting external or recurrent inputs.
*   **Numerical Annotations:** Specific connection strengths and probabilities are listed near the arrows connecting the layers (e.g., $1.7\ (26\%)$ between L2/3-E and L4-E).

### 3. Visual Components & Symbols (Right Panel: Canonical Microcircuit for Predictive Coding)
The right panel depicts a more complex, functionally defined microcircuit.

*   **Nodes:** Nodes are represented by circles. Some nodes are explicitly marked with a dark circle, which the caption identifies as pyramidal cells.
*   **Color Coding:** Color is used to denote functional roles:
    *   Pink nodes represent "prediction error populations."
    *   Excitatory connections are shown in black.
    *   Inhibitory connections are shown in red.
*   **Functional Grouping:** Nodes appear to be grouped into functional roles related to prediction and error.
*   **Flow/Loops:** The diagram shows complex feedback loops:
    *   A loop labeled "Forward prediction error" flows from the top right towards the center.
    *   A loop labeled "Backward predictions" flows from the bottom right upwards.
    *   The flow between layers is indicated by arrows, showing both feedforward and feedback pathways.
*   **Variables:** Mathematical notations are used to label the nodes, such as $\hat{z}^{(i)}$, $s_v$, and $\mu_x^{(i)}$.
*   **Dotted Lines:** Dotted lines indicate connections that are present in the predictive coding model but *not* in the Haeusler and Maass (2007) microcircuit.

### 4. Labels, Keys & Legends Integration
The caption provides crucial context for interpreting the symbols:

*   **Left Panel:** The numbers denote connection strengths (mean amplitude of PSPs measured at soma in mV) and connection probabilities (in parentheses), referencing Thomson et al. (2002).
*   **Right Panel:**
    *   Prediction error populations are highlighted in pink.
    *   Excitatory connections are black; inhibitory connections are red.
    *   Dark circles denote pyramidal cells.
    *   Expectations (about causes and states) are assigned to interneurons in supragranular layers, passed to infragranular layers.
    *   Prediction errors occupy granular layers.
    *   Superficial pyramidal cells encode prediction errors sent forward hierarchically.
    *   Conditional expectations/prediction errors on hidden causes are associated with excitatory cell types, while corresponding quantities for hidden states are assigned to inhibitory cells.
    *   The precision of feedforward prediction errors is placed against superficial pyramidal cells, controlling postsynaptic sensitivity/gain.

### 5. Specific Notations and Flow (Right Panel Detail)
The right panel illustrates the flow of prediction and error:

*   **Top Flow:** A pathway labeled "Forward prediction error" moves downwards, interacting with nodes like $\hat{z}^{(i+1)}$ and $s_v$.
*   **Bottom Flow:** A pathway labeled "Backward predictions" moves upwards, interacting with nodes like $\hat{z}^{(i)}$ and $s_x$.
*   **Interactions:** There are explicit connections between nodes representing expectations ($\mu$) and prediction errors ($\hat{z}$), mediated by variables like $s_v$ (likely related to sensitivity/gain) and $\hat{z}^{(i+1)}$ vs. $\hat{z}^{(i)}$. The red inhibitory connections suggest error signaling or modulation between specific functional units.

706
Neuron 76, November 21, 2012 ª2012 Elsevier Inc.

Neuron
Perspective


---

## Page 13

feedforward and feedback message passing that emerges under
predictive coding. It is particularly interesting given recent evi-
dence that feedforward connections may use higher frequencies
than feedback connections (Bosman et al., 2012).

Conclusion
In conclusion, there is a remarkable correspondence between
the anatomy and physiology of the canonical microcircuit and
the formal constraints implied by generalized predictive coding.
Having said this, there are many variations on the mapping
between computational and neuronal architectures: even if
predictive coding is an appropriate implementation of Bayesian
ﬁltering, there are many variations on the arrangement shown
in Figure 5. For example, feedback connections could arise
directly from cells encoding conditional expectations in supra-
granular layers. Indeed, there is emerging evidence that feed-
back connections between proximate hierarchical levels origi-
nate from both deep and superﬁcial layers (Markov et al.,
2011). Note that this putative splitting of extrinsic streams is
only predicted in the light of empirical constraints on intrinsic
connectivity.

One of our motivations—for considering formal constraints on
connectivity—was to produce dynamic causal models of canon-
ical microcircuits. Dynamic causal modeling enables one to
compare different connectivity models, using empirical elec-
trophysiological responses (David et al., 2006; Moran et al.,
2008, 2011). This form of modeling rests upon Bayesian model

Figure 6. Spectral Asymmetries in
Superﬁcial and Deep Cells
This schematic illustrates the functional asymme-
try between the spectral activity of superﬁcial and
deep cells predicted theoretically. In this illustra-
tive example, we have ignored the effects of
inﬂuences on the expectations of hidden causes
(encoded by deep pyramidal cells), other than the
prediction error on causes (encoded by superﬁcial
pyramidal cells). The bottom panel shows the
spectral density of deep pyramidal cell activity,
given the spectral density of superﬁcial pyramidal
cell activity in the top panel. The equation ex-
presses the spectral density of the deep cells as
a function of the spectral density of the superﬁcial
cells, using Equation (2). This schematic is meant
to illustrate how the relative amounts of low (beta)-
and high (gamma)-frequency activity in superﬁcial
and deep cells can be explained by the evidence
accumulation implicit in predictive coding.

> Figure caption (from PDF text): Figure 6. Spectral Asymmetries in
Superﬁcial and Deep Cells
This schematic illustrates the functional asymme-
try between the spectral activity of superﬁcial and
deep cells predicted theoretically. In this illustra-
tive example, we have ignored the effects of
inﬂuences on the expectations of hidden causes
(encoded by deep pyramidal cells), other than the
prediction error on causes (encoded by superﬁcial
pyramidal cells). The bottom panel shows the
spectral density of deep pyramidal cell activity,
given the spectral density of superﬁcial pyramidal
cell activity in the top panel. The equation ex-
presses the spectral density of the deep cells as
a function of the spectral density of the superﬁcial
cells, using Equation (2). This schematic is meant
to illustrate how the relative amounts of low (beta)-
and high (gamma)-frequency activity in superﬁcial
and deep cells can be explained by the evidence
accumulation implicit in predictive coding.
> Figure description (generated): ## Figure Description: Spectral Asymmetries in Superficial and Deep Cells

This figure presents a schematic illustration comparing the spectral activity between superficial and deep cells, likely representing different layers or types of pyramidal neurons in a cortical model. The figure is dominated by two distinct spectral density plots, one implied for superficial cells and the other explicitly shown for deep cells.

### 1. Overall Layout & Structure
The figure is structured as a comparative visualization, primarily consisting of two overlapping or adjacent spectral density plots plotted against frequency. The mathematical relationship governing the deep cell activity is explicitly stated at the top of the visual field, linking the two spectral representations.

### 2. Visual Components & Symbols
*   **Mathematical Equation:** At the top, a key equation is displayed:
    $$\left|\tilde{\mu}_v^{(i)}(\omega)\right|^2 = \frac{1}{\omega^2} |\tilde{\xi}_v^{(i+1)}(\omega)|^2$$
    This equation relates the spectral density of one component ($\tilde{\mu}_v^{(i)}(\omega)$) to another ($\tilde{\xi}_v^{(i+1)}(\omega)$).
*   **Spectral Plots:** The main body of the figure consists of two overlapping, shaded spectral density plots. These plots show power distribution across a frequency range.
*   **Color Coding:** The spectral activity is represented by large, overlapping areas filled with a solid green color.
*   **Annotations:** Two distinct frequency bands are labeled within the plots using Greek letters: $\beta$ and $\gamma$.

### 3. Labels, Keys & Legends
*   **Mathematical Variables:** The equation uses variables such as $\tilde{\mu}_v^{(i)}(\omega)$, $\tilde{\xi}_v^{(i+1)}(\omega)$, and the angular frequency $\omega$.
*   **Frequency Labels:** The plots are annotated with labels indicating specific frequency bands: $\beta$ and $\gamma$.
*   **Axes Labels:** The horizontal axis (x-axis) is labeled with frequency units, showing markings up to 120. The vertical axis (y-axis) represents spectral density, marked with numerical values 0, 1, and 2.

### 4. Data Trends & Details
The figure displays two primary spectral profiles:

*   **Low-Frequency Activity ($\beta$ band):** A prominent, broad peak is visible in the lower frequency range, labeled $\beta$. This activity appears to be significant across a wide band, peaking around 15-20 on the x-axis.
*   **High-Frequency Activity ($\gamma$ band):** A second, narrower peak is visible at higher frequencies, labeled $\gamma$. This activity peaks around 60-70 on the x-axis.

The visual representation suggests that both spectral components ($\beta$ and $\gamma$) are present in the system being modeled. The caption clarifies that this schematic illustrates the relative amounts of low ($\beta$) and high ($\gamma$)-frequency activity in superficial and deep cells.

### 5. Contextual Caption Integration
The caption provides critical context:
*   **Purpose:** The schematic illustrates the functional asymmetry between the spectral activity of superficial and deep cells predicted theoretically.
*   **Modeling Assumption:** The illustration ignores influences on the expectations of hidden causes (encoded by deep pyramidal cells), focusing only on prediction error on causes (encoded by superficial pyramidal cells).
*   **Interpretation:** The equation provided relates the spectral density of deep cells to that of superficial pyramidal cell activity.
*   **Conclusion:** The figure is intended to explain how the relative amounts of low ($\beta$) and high ($\gamma$)-frequency activity in superficial and deep cells can be explained by the evidence accumulation implicit in predictive coding.

comparison and allows one to assess
the evidence for one microcircuit relative
to another. In principle, this provides
a way to evaluate different microcircuit
models, in terms of their ability to explain
observed activity. One might imagine that
the
particular
circuits
for
predictive
coding presented in this paper will be
nuanced as more anatomical and physio-
logical information becomes available.
The ability to compare competing models
or
microcircuits—using
optogenetics,
local ﬁeld potentials, and electroencephalography—may be
important for reﬁning neurobiologically informed microcircuits.
In short, many of the predictions and assumptions we have
made about the speciﬁc form of the microcircuit for predictive
coding may be testable in the near future.

ACKNOWLEDGMENTS

This work was supported by the Wellcome Trust and the NSF Graduate
Research Fellowship under Grant 2009090358 to A.M.B. Support was also
provided by NIH grants MH055714 (G.R.M.) and EY013588 (W.M.U.), and
NSF grant 1228535 (G.R.M and W.M.U). The authors would like to thank Julien
Vezoli, Will Penny, Dimitris Pinotsis, Stewart Shipp, Vladimir Litvak, Conrado
Bosman, Laurent Perrinet, and Henry Kennedy for helpful discussions. We
would also like to thank our reviewers for helpful comments and guidance.