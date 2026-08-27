## 

*For correspondence:
marinag@alleninstitute.org (MG);
shawno@alleninstitute.org (SRO)

Competing interests: The
authors declare that no
competing interests exist.

Funding: See 

Received: 19 July 2019
Accepted: 05 February 2020
Published: 26 February 2020

Reviewing editor: Brice
Bathellier, CNRS, France

Copyright Garrett et al. This
article is distributed under the
terms of the Creative Commons
Attribution License, which
permits unrestricted use and
redistribution provided that the
original author and source are
credited.

Experience shapes activity dynamics and
stimulus coding of VIP inhibitory cells

Marina Garrett*, Sahar Manavi, Kate Roll, Douglas R Ollerenshaw,
Peter A Groblewski, Nicholas D Ponvert, Justin T Kiggins, Linzy Casal, Kyla Mace,
Ali Williford, Arielle Leon, Xiaoxuan Jia, Peter Ledochowitsch, Michael A Buice,
Wayne Wakeman, Stefan Mihalas, Shawn R Olsen*

Allen Institute for Brain Science, Seattle, United States

Abstract Cortical circuits can flexibly change with experience and learning, but the effects on
specific cell types, including distinct inhibitory types, are not well understood. Here we investigated
how excitatory and VIP inhibitory cells in layer 2/3 of mouse visual cortex were impacted by visual
experience in the context of a behavioral task. Mice learned a visual change detection task with a
set of eight natural scene images. Subsequently, during 2-photon imaging experiments, mice
performed the task with these familiar images and three sets of novel images. Strikingly, the
temporal dynamics of VIP activity differed markedly between novel and familiar images: VIP cells
were stimulus-driven by novel images but were suppressed by familiar stimuli and showed ramping
activity when expected stimuli were omitted from a temporally predictable sequence. This
prominent change in VIP activity suggests that these cells may adopt different modes of processing
under novel versus familiar conditions.

Introduction
Neural circuits are dynamically shaped by experience and learned expectations (de Lange et al.,
2018; LeMessurier and Feldman, 2018; Pakan et al., 2018; Ranganath and Rainer, 2003). Visual
experience can modify cortical representations, including changes in gain, selectivity, correlations,
and population dynamics (Jurjut et al., 2017; Khan et al., 2018; Makino and Komiyama, 2015;
Poort et al., 2015; Weskelblatt and Niell, 2019; Woloszyn and Sheinberg, 2012). Moreover, sen-
sory and behavioral experience can lead to the emergence of predictive activity in the visual cortex
including reward anticipation (Poort et al., 2015; Shuler and Bear, 2006), spatial expectation
(Fiser et al., 2016; Saleem et al., 2018), anticipatory recall (Gavornik and Bear, 2014; Xu et al.,
2012) and prediction error signals (Fiser et al., 2016; Hamm and Yuste, 2016; Homann et al.,
2017).
These
learning-related
changes
in
sensory
cortex
can
involve
top-down
feedback
(Fiser et al., 2016; Makino and Komiyama, 2015; Petro et al., 2014; Zhang et al., 2014) and neu-
romodulatory inputs (Chubykin et al., 2013; Kuchibhotla et al., 2017; Pinto et al., 2013), and may
be associated with a shift in the balance of bottom-up sensory and top-down contextual signals
(Batista-Brito et al., 2018; Khan and Hofer, 2018). Inhibitory interneurons likely play a key role in
this process by dynamically regulating the flow of information (Hangya et al., 2014; Kepecs and
Fishell, 2014; Wang and Yang, 2018). Elucidating how different cell populations, particularly inhibi-
tory cells, contribute to experience-dependent changes in sensory coding is critical to understand
the dynamic nature of cortical circuits.

Vasoactive intestinal peptide (VIP) expressing cells comprise a major class of inhibitory neurons
and are well-positioned to mediate top-down and neuromodulatory influences on local circuits in
sensory cortex. VIP cells receive long-range projections from frontal areas (Lee et al., 2013;
Wall et al., 2016; Zhang et al., 2016; Zhang et al., 2014) as well as cholinergic and noradrenergic
inputs (Alitto and Dan, 2013; Fu et al., 2014). VIP cells are highly active during states of arousal

Garrett et al. eLife 2020;9:e50340. DOI: 
1 of 25

RESEARCH ARTICLE

---

## 

(Fu et al., 2014; Reimer et al., 2014), are modulated by task engagement (Kuchibhotla et al.,
2017), and are responsive to behavioral reinforcement (Krabbe et al., 2019; Letzkus et al., 2011;
Pi et al., 2013). In the local cortical circuitry, VIP cells primarily inhibit another major class of inhibi-
tory interneuron, somatostatin (SST) cells (Lee et al., 2013; Munoz et al., 2017; Pfeffer et al.,
2013; Pi et al., 2013), which can result in disinhibition of excitatory neurons (Fu et al., 2017;
Lee et al., 2013; Letzkus et al., 2011). SST cells target the apical dendrites of pyramidal neurons
(Kepecs and Fishell, 2014) and removal of this inhibition may facilitate the association of top-down
and bottom-up input by pyramidal cells (Chen et al., 2015; Larkum, 2013; Makino and Komiyama,
2015). However, little is known about how VIP cell activity is modified by visual experience.
Here we investigated how long-term behavioral experience with natural scene images alters activ-
ity of cortical VIP inhibitory and excitatory pyramidal cells in layers 2/3 of mouse visual cortex. Mice
were trained to perform a change detection task in which images were presented in a periodic man-
ner and mice were rewarded for detecting changes in image identity. Mice learned the task with one
set of eight natural images, which were viewed thousands of times and were thus highly familiar.
During subsequent 2-photon imaging, these familiar images as well as three novel image sets were
tested. Familiar images were associated with lower overall population activity in both excitatory and
VIP cells. Notably, VIP inhibitory cells had distinct activity dynamics during sessions with familiar ver-
sus novel images. VIP cells were stimulus-driven by novel images but displayed ramping activity
between presentations of familiar images and were suppressed by stimulus onset. These cells
showed even greater ramping activity when an expected stimulus was omitted from the regular
image sequence. Overall, these results show distinct experience-dependent changes in two cortical
cell classes and suggest that VIP cells may adopt different modes of processing during familiar ver-
sus novel conditions.

Results

Visual change detection task with familiar and novel images
We trained mice on a go/no-go visual change detection task with natural scene stimuli. In this task,
mice see a continuous stream of repeatedly presented images (250 ms stimulus presentation fol-
lowed by 500 ms gray screen; Figure 1A,B). On 'go' trials, the image identity changes and mice
report the change by licking a reward spout within 750 ms (Figure 1B,C). False alarms are quantified
during 'catch' trials when the image does not change. To test whether expectation signals exist in
the visual cortex due to the temporal regularity of this task, we randomly omitted ~5% of all image
presentations (not including image changes to avoid interfering with behavior performance). These
omissions appeared as an extended gray period to the mouse and corresponded to a gap in the
periodic timing of stimuli (Figure 1D).

Mice learned the task through a series training stages, starting with oriented gratings and then
progressing to natural images (Figure 1E-G; see