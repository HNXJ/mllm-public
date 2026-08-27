## Page 1

*For correspondence:
marinag@alleninstitute.org (MG);
shawno@alleninstitute.org (SRO)

Competing interests: The
authors declare that no
competing interests exist.

Funding: See page 21

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

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
1 of 25

RESEARCH ARTICLE


---

## Page 2

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
lowed by 500 ms gray screen; Figure 1A,B). On ‘go’ trials, the image identity changes and mice
report the change by licking a reward spout within 750 ms (Figure 1B,C). False alarms are quantified
during ‘catch’ trials when the image does not change. To test whether expectation signals exist in
the visual cortex due to the temporal regularity of this task, we randomly omitted ~5% of all image
presentations (not including image changes to avoid interfering with behavior performance). These
omissions appeared as an extended gray period to the mouse and corresponded to a gap in the
periodic timing of stimuli (Figure 1D).

Mice learned the task through a series training stages, starting with oriented gratings and then
progressing to natural images (Figure 1E–G; see Materials and methods for additional details about
training procedure). During the natural image stage, mice were trained with one set of eight images
(image set A) for an extended number of sessions (range = 6–46 sessions with image set A,
median = 17 sessions; Figure 1H, Figure 1—figure supplement 1A). On average, mice viewed each
of the eight images from the familiar set 10,350 times prior to the 2-photon imaging stage (range:
944–26,784 individual stimulus presentations per image).
During the 2-photon imaging portion of the experiment, mice performed the task with either the
familiar image set or one of three additional novel image sets (Figure 1F). Hit rates, false alarm
rates, and reaction times (lick latency) were similar across image sets (Figure 1I,J). During the task,
mice are free to run on a circular disk and typically stop running to lick. There was no difference in
running behavior between novel and familiar image sessions (Figure 1—figure supplement 1B,C).
Licking behavior around the time of omission was also similar across image sets (Figure 1—figure
supplement 1E,F). Together these results show that mouse behavior was similar for novel and famil-
iar images.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
2 of 25

Research article
Neuroscience


---

## Page 3

0
2
4
time after change (sec)

0

50

100

150

200

250

trial #

change aligned lick raster

epoch 1

example task flow and behavior performance

epoch 2
epoch 3

0
10
20
30
40
50
60
time (seconds)

epoch 4

licks
rewards

visual
stimuli

stage 1
stage 5
stage 4
stage 3
stage 2
stage 7
stage 6

im061
im062
im063
im065

im066
im069
im077
im085

image set A - familiar

im012
im013
im036
im044

im047
im057
im078
im115

image set B - novel

im000
im031
im035
im045

im054
im073
im075
im106

image set C - novel

im005
im024
im034
im072

im087
im091
im104
im114

image set D - novel

1
2
3
4
5
6
7
training stage

0

20

40

# sessions

sessions per stage (n=21 mice)

1
3
5
7
9
11 13 15 17 19
session number

0

2

mean d-prime

mouse M409259

go
catch
trial type

0.00

0.25

0.50

0.75

1.00

response rate

A
B
C
D
image set

0.0

0.2

0.4

0.6

reaction time (sec)

A
B

F

D

E

C

J
I
H
G

Figure 1. Natural image change detection task with familiar and novel images. (A) Schematic of stimulus presentation during the task. Images are
presented for 250 ms followed by 500 ms of gray screen. (B) Trial structure. Colors represent different images. On go trials, the image identity changes
and mice must lick within the 750 ms response window to receive a water reward. On catch trials no image change occurs and the behavioral response
is measured to quantify guessing behavior. (C) Example lick raster, aligned to the image change time. Purple dots indicate rewards and green ticks are
reward consumption licks. Red ticks indicate incorrect licking responses outside the response window. (D) Example behavior performance over four
minutes of one session, separated into one-minute epochs. Colored vertical bars indicate stimulus presentations (different colors are different images).
Green tick marks indicate licks, purple triangles indicate rewards. 5% of all non-change image flashes are omitted, visible as a gap in the otherwise
regular stimulus sequence. (E) Training stages. Mice are initially trained with gratings of 2 orientations, first with no intervening gray screen (stage 1),
then with a 500 ms inter-stimulus delay (stage 2). Next, mice perform change detection with eight natural scene images (stage 3, image set A). During
the 2-photon imaging portion of the experiment, mice are tested with image set A as well as three novel image sets (B, C, D) on subsequent days. (F)
The four sets of 8 natural images. Image set A is the familiar training set, and image sets B, C and D were the novel sets shown for the first time during
2-photon imaging. (G) Example training time course of one mouse. (H) Number of sessions spent in each stage across mice. Mean ± 95% confidence
intervals in color, individual mice in gray. (I) Response rates for go and catch trials are similar across image sets. Individual behavior sessions are shown
in gray and average ± 95% confidence intervals across sessions for each image set are shown in color. (J) Reaction times, measured as latency to first
lick, are not significantly different across image sets. Mean ± 95% confidence intervals in color, individual sessions in gray.
The online version of this article includes the following figure supplement(s) for figure 1:

> Figure caption (from PDF text): Figure 1. Natural image change detection task with familiar and novel images. (A) Schematic of stimulus presentation during the task. Images are
presented for 250 ms followed by 500 ms of gray screen. (B) Trial structure. Colors represent different images. On go trials, the image identity changes
and mice must lick within the 750 ms response window to receive a water reward. On catch trials no image change occurs and the behavioral response
is measured to quantify guessing behavior. (C) Example lick raster, aligned to the image change time. Purple dots indicate rewards and green ticks are
reward consumption licks. Red ticks indicate incorrect licking responses outside the response window. (D) Example behavior performance over four
minutes of one session, separated into one-minute epochs. Colored vertical bars indicate stimulus presentations (different colors are different images).
Green tick marks indicate licks, purple triangles indicate rewards. 5% of all non-change image flashes are omitted, visible as a gap in the otherwise
regular stimulus sequence. (E) Training stages. Mice are initially trained with gratings of 2 orientations, first with no intervening gray screen (stage 1),
then with a 500 ms inter-stimulus delay (stage 2). Next, mice perform change detection with eight natural scene images (stage 3, image set A). During
the 2-photon imaging portion of the experiment, mice are tested with image set A as well as three novel image sets (B, C, D) on subsequent days. (F)
The four sets of 8 natural images. Image set A is the familiar training set, and image sets B, C and D were the novel sets shown for the first time during
2-photon imaging. (G) Example training time course of one mouse. (H) Number of sessions spent in each stage across mice. Mean ± 95% confidence
intervals in color, individual mice in gray. (I) Response rates for go and catch trials are similar across image sets. Individual behavior sessions are shown
in gray and average ± 95% confidence intervals across sessions for each image set are shown in color. (J) Reaction times, measured as latency to first
lick, are not significantly different across image sets. Mean ± 95% confidence intervals in color, individual sessions in gray.
The online version of this article includes the following figure supplement(s) for figure 1:


**1. Overall Layout & Structure:**
The figure is a single-panel line graph plotting data over time, likely representing performance across sequential trials or epochs.

**2. Visual Components & Symbols:**
*   **X-axis:** Represents time, marked with numerical labels from 1 to 19. These likely correspond to epochs or trials.
*   **Y-axis:** Represents a quantitative measure, ranging from 0 to approximately 3. The axis is labeled with numerical ticks (0, 2).
*   **Data Points:** A series of connected data points are plotted. These points vary in color and shape, suggesting different conditions or image sets were tested sequentially.
    *   The points are connected by lines, forming a fluctuating trend line.
    *   The colors observed include shades of blue/purple and reddish-brown/maroon.
    *   The data points are generally clustered around the 1 to 3 range on the y-axis.

**3. Labels, Keys & Legends:**
*   **Title:** "mouse M409259" is centered above the plot.
*   **Axes Labels:** No explicit labels are provided for the X and Y axes in this cropped view, although context suggests the X-axis is time/trial number and the Y-axis represents a performance metric (e.g., response rate or accuracy).

**4. Data Trends & Details:**
The plot shows a dynamic trend:
*   Starting near $Y \approx -0.5$ at $X=1$.
*   The value rapidly increases, peaking around $X=5$ and $X=6$, reaching the highest point near $Y \approx 3.0$.
*   Following this peak, the value generally decreases through $X=7$ to $X=13$, fluctuating between approximately 2.0 and 2.5.
*   From $X=13$ onwards, the trend continues to fluctuate, showing a slight dip around $X=14$, followed by a rise toward $X=17$ (reaching $\approx 2.5$), and then a final decline towards $X=19$ (ending around $Y \approx 1.5$).

**5. Contextual Caption Integration:**
Based on the caption, this graph likely represents "Example behavior performance over four minutes of one session," as described in Panel (D) of Figure 1. The colored vertical bars mentioned in the caption would correspond to the sequence of data points shown here, where different colors indicate different stimulus presentations (image sets A, B, C, or D). The fluctuating line represents the measured behavior (e.g., lick rate) over time/epochs.

> Figure caption (from PDF text): Figure 1. Natural image change detection task with familiar and novel images. (A) Schematic of stimulus presentation during the task. Images are
presented for 250 ms followed by 500 ms of gray screen. (B) Trial structure. Colors represent different images. On go trials, the image identity changes
and mice must lick within the 750 ms response window to receive a water reward. On catch trials no image change occurs and the behavioral response
is measured to quantify guessing behavior. (C) Example lick raster, aligned to the image change time. Purple dots indicate rewards and green ticks are
reward consumption licks. Red ticks indicate incorrect licking responses outside the response window. (D) Example behavior performance over four
minutes of one session, separated into one-minute epochs. Colored vertical bars indicate stimulus presentations (different colors are different images).
Green tick marks indicate licks, purple triangles indicate rewards. 5% of all non-change image flashes are omitted, visible as a gap in the otherwise
regular stimulus sequence. (E) Training stages. Mice are initially trained with gratings of 2 orientations, first with no intervening gray screen (stage 1),
then with a 500 ms inter-stimulus delay (stage 2). Next, mice perform change detection with eight natural scene images (stage 3, image set A). During
the 2-photon imaging portion of the experiment, mice are tested with image set A as well as three novel image sets (B, C, D) on subsequent days. (F)
The four sets of 8 natural images. Image set A is the familiar training set, and image sets B, C and D were the novel sets shown for the first time during
2-photon imaging. (G) Example training time course of one mouse. (H) Number of sessions spent in each stage across mice. Mean ± 95% confidence
intervals in color, individual mice in gray. (I) Response rates for go and catch trials are similar across image sets. Individual behavior sessions are shown
in gray and average ± 95% confidence intervals across sessions for each image set are shown in color. (J) Reaction times, measured as latency to first
lick, are not significantly different across image sets. Mean ± 95% confidence intervals in color, individual sessions in gray.
The online version of this article includes the following figure supplement(s) for figure 1:


### Overall Layout & Structure
The figure is organized into a grid-like structure, with panels A through J arranged sequentially. Panels A and B illustrate the basic stimulus presentation and trial structure, while C and D show examples of behavioral data. Panels E through H detail the training stages and image sets used. Panels I and J present quantitative behavioral results (response rates and reaction times).

### Detailed Panel Descriptions

**Panel A: Schematic of Stimulus Presentation**
*   This panel is a schematic illustrating the timing sequence. It shows an image presentation followed by a gray screen interval.
*   **Timing:** Images are presented for **250 ms**, followed by a **500 ms** gray screen.

**Panel B: Trial Structure**
*   This panel illustrates the structure of a single trial. It differentiates between "go trials" and "catch trials."
*   **Go Trials:** The image identity changes, and mice must lick within a **750 ms response window** to receive a water reward.
*   **Catch Trials:** No image change occurs, and the response is measured to quantify guessing behavior.
*   **Color Coding:** Different colors represent different images used in the experiment.

**Panel C: Example Lick Raster**
*   This panel displays an example lick raster, aligned to the image change time.
*   **Symbols:**
    *   Purple dots indicate **rewards**.
    *   Green ticks represent **reward consumption licks**.
    *   Red ticks indicate **incorrect licking responses** outside the response window.

**Panel D: Example Behavior Performance**
*   This panel shows example behavior performance over four minutes of one session, divided into one-minute epochs.
*   **Visual Elements:**
    *   Colored vertical bars indicate stimulus presentations (with different colors corresponding to different images).
    *   Green tick marks indicate licks.
    *   Purple triangles indicate rewards.
    *   A note specifies that **5% of all non-change image flashes are omitted**, visible as a gap in the otherwise regular stimulus sequence.

**Panel E: Training Stages**
*   This panel outlines the progression of training stages.
*   **Stages:**
    1.  Initial training with gratings of 2 orientations, **without** an intervening gray screen (Stage 1).
    2.  Training with a **500 ms inter-stimulus delay** (Stage 2).
    3.  Change detection using **eight natural scene images (Image set A)** (Stage 3).
*   **2-Photon Imaging:** During this phase, mice are tested with Image set A and three novel image sets (**B, C, D**) on subsequent days.

**Panel F: The Four Sets of 8 Natural Images**
*   This panel displays the four sets of natural images.
*   **Labeling:** Image set A is identified as the **familiar training set**. Image sets B, C, and D are designated as the **novel sets** shown for the first time during 2-photon imaging.

**Panel G: Example Training Time Course**
*   This panel shows an example time course for one mouse's training.

**Panel H: Number of Sessions Spent in Each Stage**
*   This panel presents data on the number of sessions spent in each training stage across mice.
*   **Data Representation:** Mean values are shown in color, with $\pm 95\%$ confidence intervals indicated. Individual mice data is shown in gray.

**Panel I: Response Rates**
*   This panel compares response rates for go and catch trials across image sets.
*   **Data Representation:** Individual behavior sessions are shown in gray, and the average $\pm 95\%$ confidence intervals across sessions for each image set are shown in color. The caption notes that response rates are similar across image sets.

**Panel J: Reaction Times**
*   This panel displays reaction times, measured as latency to first lick.
*   **Data Representation:** Mean $\pm 95\%$ confidence intervals are shown in color, while individual sessions are shown in gray. The caption notes that reaction times are not significantly different across image sets.

Figure supplement 1. Behavior is similar across image sets.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
3 of 25

Research article
Neuroscience



**Overall Layout & Structure:**
The figure is structured horizontally, representing the progression of time from left to right. It features two parallel timelines or tracks, one labeled "GO" and the other labeled "CATCH," running concurrently.

**Visual Components & Symbols:**
1. **Timeline Markers:** The diagram uses a horizontal axis representing time progression. Key temporal markers are indicated: "trial start," "change time," and the duration of the "response window."
2. **Stimulus Representation:** Rectangular blocks (colored purple) represent the presentation of a stimulus.
3. **Screen State:** A section labeled "gray screen" indicates a period where no stimulus is presented.
4. **Response Window:** A shaded, light gray rectangular area indicates the "response window," which is where a response can be made.
5. **Timing Markers:** A vertical dashed line marks the "change time," separating the initial stimulus presentation phase from the response window.

**Detailed Sequence Breakdown (Left to Right):**

*   **Trial Start:** The sequence begins at "trial start."
    *   Both the GO and CATCH timelines show an initial purple stimulus block occurring at this point.
    *   Following the first stimulus, both timelines show a period labeled "500 ms gray screen."
*   **Change Time:** A vertical dashed line marks the "change time," which occurs after the 500 ms gray screen period.
*   **Response Window:** Following the "change time," a light gray shaded area labeled "response window" begins.
    *   **GO Timeline:** During the response window, a purple stimulus block appears, followed by another purple stimulus block.
    *   **CATCH Timeline:** During the response window, a single purple stimulus block appears.
*   **Post-Response Window:** After the response window concludes, both timelines show a final purple stimulus block.

**Labels and Annotations:**
*   **Timeline Labels (Top Right):** The two parallel tracks are explicitly labeled: **GO** and **CATCH**.
*   **Temporal Labels:** Key time points are labeled: "trial start," "change time," and "response window."
*   **Stimulus/Screen Labels:** Text labels indicate the duration of specific phases: "250 ms stimulus" (associated with the initial block) and "500 ms gray screen."

**Contextual Interpretation (Based on Structure):**
The diagram visually contrasts the timing of events between two experimental conditions. The "GO" condition appears to involve a sequence where stimuli are presented both before and during the response window, whereas the "CATCH" condition shows a different pattern of stimulus presentation relative to the change time and response window.



This figure illustrates a temporal progression, likely representing developmental or physiological change over time. It is structured as a sequence of visual snapshots arranged along a directional arrow labeled "time."

**1. Overall Layout & Structure:**
The figure is organized linearly, showing a sequence of four distinct visual states arranged vertically and horizontally along a prominent diagonal arrow. The overall structure functions as a timeline or developmental progression diagram.

**2. Visual Components & Symbols:**
*   **Progression Arrow:** A thick, black arrow originates from the upper left and points diagonally down and to the right, explicitly labeled with the text "time" positioned along its path. This arrow dictates the direction of change shown by the sequence of images.
*   **Visual States (Images):** Four distinct visual panels are presented sequentially along the path of the "time" arrow. These panels appear to be microscopic or close-up photographs, likely depicting biological structures (e.g., plant tissue or floral development).
    *   **State 1 (Top Left):** The first image shows a dark, textured structure with some lighter, possibly filamentous or cellular material visible.
    *   **State 2 (Upper Middle):** The second image shows a structure similar to the first, but perhaps slightly more defined or advanced in its morphology.
    *   **State 3 (Lower Middle):** The third image shows a structure that appears more complex than the previous two, with clearer differentiation in its texture or form.
    *   **State 4 (Bottom Right):** The final image displays a cluster of fully formed, light-colored flowers against a darker background.

**3. Labels, Keys & Legends:**
*   The only explicit label within the diagram is **"time,"** written in black text adjacent to the main directional arrow.
*   There are no numerical axes, legends, or specific annotations within the image panels themselves.

**4. Data Trends & Details:**
Since the figure consists of sequential images rather than a plot, the "data trend" is qualitative: the visual evidence demonstrates a progression from an early, less differentiated state (State 1) through intermediate morphological changes (States 2 and 3) to a mature, fully developed state characterized by open flowers (State 4).

**5. Contextual Caption Integration:**
No external caption was provided, so no contextual integration can be performed based on that information. The figure visually represents a developmental sequence over time, transitioning from an initial structure to mature floral structures.



**1. Overall Layout & Structure:**
The figure is structured as a horizontal timeline or block diagram, divided into two major sequential sections: "training" on the left and "behavior + 2P imaging" on the right. Each major phase is further subdivided into sequential stages, represented by distinct rectangular blocks.

**2. Visual Components & Symbols:**
The diagram uses a series of horizontally aligned, colored rectangular blocks to represent different experimental stages. Arrows or implied progression indicate the flow from one stage to the next across both phases.

**3. Labels, Keys & Legends:**
The primary labels are:
*   **Overall Title/Header:** "E" (indicating the panel letter).
*   **Phase 1 Header:** "training" (written above the first set of blocks).
*   **Phase 2 Header:** "behavior + 2P imaging" (written above the second set of blocks).

**Detailed Stage Breakdown:**

**A. Training Phase (Left Side):**
This phase consists of three sequential stages:
*   **Stage 1:** A gray rectangular block labeled "Gratings no delay."
*   **Stage 2:** A light gray/off-white rectangular block labeled "Gratings 0.5s delay."
*   **Stage 3:** A light brown/tan rectangular block labeled "Images A."

**B. Behavior + 2P Imaging Phase (Right Side):**
This phase consists of four sequential stages:
*   **Stage 4:** A reddish-brown rectangular block labeled "Images A." (This stage follows Stage 3).
*   **Stage 5:** A dark blue rectangular block labeled "Images B."
*   **Stage 6:** A medium-dark gray/blue rectangular block labeled "Images C."
*   **Stage 7:** A light blue/cyan rectangular block labeled "Images D."

**4. Data Trends & Details:**
As this is a schematic timeline, there are no quantitative data trends or axes present. The structure illustrates the sequence of experimental conditions applied over time.

**5. Contextual Caption Integration:**
The labels clearly delineate the experimental progression: the initial "training" involves presenting gratings under different temporal conditions (no delay vs. 0.5s delay), followed by the introduction of "Images A." The subsequent phase, "behavior + 2P imaging," continues with presentations of different image types (Images A, B, C, and D) across Stages 4 through 7.


---

## Page 4

Imaging excitatory and VIP inhibitory cell populations during task
performance
We imaged activity in transgenic mice expressing the calcium indicator GCaMP6f in excitatory pyra-
midal cells (Slc17a7-IRES2-Cre; CaMKII-tTA; Ai93-GCaMP6f) or VIP inhibitory cells (VIP-IRES-Cre;
Ai148-GCaMP6f) (see Table 1 for numbers of mice, sessions, and cells in the dataset). On average
we imaged 181 ± 77 (mean ± SD) Slc17a7+ cells or 15 ± 10 VIP+ cells per session. Measurements
were made in primary visual cortex (VISp) and one higher visual area (VISal) but we did not observe
major differences between these two areas, so the datasets were combined for the analyses
reported here. Because calcium signals have a slow decay time that could lead to an artificial
enhancement of the response to stimuli shown close together in time, we performed event detection
to identify the onset timing of ‘spike’ events underlying the GCaMP signal (de Vries et al., 2020;
Jewell and Witten, 2017; Jewell et al., 2019). This method produces a timeseries of detected
events which have a magnitude proportional to the change in calcium activity. Event magnitude
(arbitrary units) was used for all subsequent analysis.

Excitatory cells typically responded to only one or a few images in each set, showing fluorescence
increases after stimulus onset or sometimes after stimulus offset (Figure 2A,B). VIP cells were less
image selective and showed correlated fluctuations in activity (Figure 2C,D). Interestingly, VIP cells
had distinct activity dynamics relative to stimulus onset in novel versus familiar image sessions. Novel
images generated stimulus-locked activity in VIP cells (Figure 2D), but this was reduced or absent
with familiar images. Instead, during familiar image sessions many VIP neurons had ramping activity
that preceded stimulus presentation and decayed after stimulus onset (Figure 2C). These ramping
responses were even more pronounced when an image presentation was omitted (Figure 2C, right
panel). In contrast, VIP cells showed little activity during the omission of novel image presentations
(Figure 2D, right panel).

These differences in image responsiveness and temporal dynamics, already evident in single cell
activity, are further quantified across the population of recorded neurons in the subsequent sections.

Reduced image-evoked activity with familiar image sets
We used a heatmap to visualize activity of the full population of recorded neurons to the eight stim-
uli for each image set, as well as for omitted stimuli (Figure 3A). Most excitatory neurons responded
to one of the eight images from a given set and showed little activity when stimuli were omitted. VIP
neurons could also show robust image responses, particularly for the novel image sets. In contrast,
during sessions with familiar image sets, VIP neurons were most strongly active during the extended
gray screen period when stimuli were omitted (Figure 3A).

Quantifying each cell’s mean response to its preferred image in each set revealed that both excit-
atory and VIP inhibitory populations had reduced activity levels with familiar images (Figure 3B,
p<0.008 for all comparisons with image set A for both excitatory and VIP inhibitory populations,

Table 1. Number of mice, sessions, and cells in dataset.

cell class

image

set
mice
sessions

total

cells

Excitatory
A
11
13
2046

Excitatory
B
11
13
2594

Excitatory
C
11
13
2172

Excitatory
D
11
12
2232

VIP
Inhibitory

A
10
13
183

VIP
Inhibitory

B
10
13
209

VIP
Inhibitory

C
10
12
186

VIP
Inhibitory

D
10
12
175

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
4 of 25

Research article
Neuroscience


---

## Page 5

cell 0

Excitatory - familiar image set A

cell 1
cell 2
cell 3

0
20
40
60
80
time (seconds)
licks
rewards

cell 0

Excitatory - novel image set C

cell 1
cell 2
cell 3

0
20
40
60
80
time (seconds)
licks
rewards

cell 0

VIP inhibitory - familiar image set A

cell 1
cell 2
cell 3

0
20
40
60
80
time (seconds)
licks
rewards

cell 0

VIP inhibitory - novel image set C

cell 1
cell 2
cell 3

0
20
40
60
80
time (seconds)
licks
rewards

im061
im062
im063
im065
im066
im069
im077
im085
omitted

im000
im031
im035
im045
im054
im073
im075
im106
omitted

im061
im062
im063
im065
im066
im069
im077
im085
omitted

im000
im031
im035
im045
im054
im073
im075
im106
omitted

A

B

D

C

Figure 2. Activity in layer 2/3 excitatory and VIP inhibitory cells during change detection task. (A) Example cell responses to the familiar image set A,
from excitatory cells in layer 2/3 of an Slc17a7-IRES2-Cre;CaMkII-tTa;Ai93 mouse expressing GCaMP6f. Left panel: dF/F traces (gray) from four
excitatory cells over a 90 second epoch of a behavior session (scale bars on left indicate 75% dF/F). Deconvolved events are shown in blue below the
dF/F trace. Colored vertical bars indicate image presentation times; timing of licks and reward delivery are shown at bottom. Right panel: response
of the same 4 cells to each image, as well activity during stimulus omission (right column, gray shading indicates the time where a stimulus would have
been displayed). Scale bars indicate 0.05 event magnitude in arbitrary units. (B) Example excitatory cells from a session with novel image set C. Left
panel scale bars indicate 100% dF/F, right panel scale bars indicate event magnitude of 0.05. (C) Example VIP inhibitory cells from layer 2/3 of a VIP-
IRES-Cre;Ai148 mouse expressing GCaMP6f, from a session with familiar image set A. Left panel scale bars indicate 225% dF/F, right panel scale bars
indicate event magnitude of 0.05. (D) Example VIP inhibitory cells for a session with novel image set C. Left panel scale bars indicate 200% dF/F, right
panel scale bars indicate event magnitude of 0.05.

> Figure caption (from PDF text): Figure 2. Activity in layer 2/3 excitatory and VIP inhibitory cells during change detection task. (A) Example cell responses to the familiar image set A,
from excitatory cells in layer 2/3 of an Slc17a7-IRES2-Cre;CaMkII-tTa;Ai93 mouse expressing GCaMP6f. Left panel: dF/F traces (gray) from four
excitatory cells over a 90 second epoch of a behavior session (scale bars on left indicate 75% dF/F). Deconvolved events are shown in blue below the
dF/F trace. Colored vertical bars indicate image presentation times; timing of licks and reward delivery are shown at bottom. Right panel: response
of the same 4 cells to each image, as well activity during stimulus omission (right column, gray shading indicates the time where a stimulus would have
been displayed). Scale bars indicate 0.05 event magnitude in arbitrary units. (B) Example excitatory cells from a session with novel image set C. Left
panel scale bars indicate 100% dF/F, right panel scale bars indicate event magnitude of 0.05. (C) Example VIP inhibitory cells from layer 2/3 of a VIP-
IRES-Cre;Ai148 mouse expressing GCaMP6f, from a session with familiar image set A. Left panel scale bars indicate 225% dF/F, right panel scale bars
indicate event magnitude of 0.05. (D) Example VIP inhibitory cells for a session with novel image set C. Left panel scale bars indicate 200% dF/F, right
panel scale bars indicate event magnitude of 0.05.


### Overall Layout & Structure
The figure is dominated by a large, multi-row plot area. The title above the plots reads: "VIP inhibitory - novel image set C". The visualization consists of four distinct horizontal traces, each representing the activity of a single cell (labeled "cell 0" through "cell 3"). Each trace is composed of two main components: a continuous time-series plot (the top portion) and a corresponding event representation below it.

### Visual Components & Symbols
**Time-Series Plots (Top Section):**
*   Each cell trace features a continuous, fluctuating line graph representing neural activity (likely $\text{dF/F}$ traces).
*   The background of the plot area is segmented by colored vertical bars, indicating different experimental conditions or stimulus presentations.
    *   Light yellow/beige shading appears at the beginning of the traces.
    *   A light green shaded area is present in the middle section.
    *   A pink/reddish-brown shaded area appears towards the right side of the traces.
*   Within each trace, there are distinct visual markers:
    *   **Gray Shading/Line:** Represents the baseline or continuous activity trace.
    *   **Blue Vertical Spikes/Bars:** Represent deconvolved events (periods of high activity).

**Event Representation (Bottom Section):**
*   Below the main trace for each cell, there is a corresponding row showing discrete events. These are represented by small green vertical bars or dots aligned temporally with the activity above.

**Scale Bars and Annotations:**
*   The left side of the plot area has vertical scale bars associated with the activity traces, indicating normalization or magnitude.
*   The bottom of the entire visualization includes a row showing timing markers, which are colored blocks (green and white/light gray) corresponding to stimulus presentation times.

### Labels, Keys & Legends
*   **Title:** "VIP inhibitory - novel image set C"
*   **Cell Labels (Y-axis equivalent):** "cell 0", "cell 1", "cell 2", and "cell 3" are listed vertically next to the traces.
*   **Scale Bar Annotations (Implied from Caption):** The caption specifies that for this panel (D), the left panel scale bars indicate $200\%$ $\text{dF/F}$, and the right panel scale bars indicate an event magnitude of $0.05$.

### Data Trends & Details
The traces show dynamic changes in activity across the four cells:
1.  **Cell 0:** Shows relatively low baseline activity, with intermittent blue spikes occurring across the colored background segments.
2.  **Cell 1:** Exhibits moderate activity, with noticeable clusters of blue spikes corresponding to the transitions between colored background segments.
3.  **Cell 2:** Displays a pattern of activity that appears somewhat correlated with the transitions, showing distinct bursts of blue spikes.
4.  **Cell 3:** Shows a pattern similar to Cell 2, with activity modulated across the different stimulus presentation periods.

The colored background segments (yellow/beige $\rightarrow$ green $\rightarrow$ pink) delineate the experimental phases, and the blue spikes indicate periods of detected neural firing corresponding to these phases. The green bars at the very bottom likely mark specific time points related to stimulus presentation or behavioral events (like licks/reward, as per the caption context).

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
5 of 25

Research article
Neuroscience



**1. Overall Layout & Structure:**
The figure is structured as a series of stacked, horizontal tracks or plots. There are at least five distinct cell tracks visible, labeled on the far left: "cell 1," "cell 2," "cell 3," and two others implied by the continuation of the tracks. The visualization spans a horizontal axis representing time (implied, as it shows temporal activity) and a vertical dimension representing the intensity or level of activity within each cell track.

**2. Visual Components & Symbols:**
*   **Cell Tracks:** Each horizontal row represents a single cell's activity profile.
*   **Activity Traces (Spikes/Bursts):** Within each cell track, there are numerous vertical spikes or bursts of activity. These traces vary in height and density across the horizontal axis, indicating temporal patterns of activation.
*   **Color Coding:** The background and activity traces are segmented by color, suggesting different states or conditions across the time axis.
    *   The tracks are segmented into distinct vertical blocks of color (e.g., light yellow/beige, pale green, light blue, pinkish-red).
    *   The activity traces themselves appear to be colored according to the background segment they fall within, though some individual spikes might have a consistent color or be grayscale.
*   **Bottom Bar:** At the very bottom, there is a thin horizontal bar that appears to be a color key or summary indicator, showing small blocks of red and green.

**3. Labels, Keys & Legends:**
*   **Cell Identifiers (Left Margin):** The tracks are explicitly labeled: "cell 1," "cell 2," and "cell 3."
*   **Color Key (Bottom Right):** A small, partially visible legend or color bar is present in the bottom right corner, showing blocks of red and green.

**4. Data Trends & Details:**
*   **Temporal Patterns:** The activity across the cells is highly heterogeneous. For instance, in "cell 1," there are distinct periods of high-frequency spiking (e.g., within the light green segment) interspersed with quieter periods.
*   **Cell-Specific Dynamics:** The patterns differ significantly between cells:
    *   "cell 1" shows dense, rhythmic spiking in certain colored regions.
    *   "cell 2" exhibits bursts of activity that appear more clustered or less uniformly dense than in cell 1.
    *   "cell 3" shows a pattern that is less consistently high-frequency than cell 1, with more sporadic bursts.
*   **Segmentation:** The color blocks delineate distinct temporal regimes across the entire dataset, suggesting that the observed activity patterns are being compared or analyzed under different experimental conditions represented by these colors.

**5. Contextual Caption Integration:**
(No specific caption text was provided, so this section relies solely on interpreting the visual structure as a representation of cellular dynamics.) The visualization strongly suggests a comparison of temporal firing patterns (spiking activity) across multiple individual neurons ("cell 1," "cell 2," etc.) under different experimental conditions (indicated by the colored background segments).



**1. Overall Layout & Structure:**
The figure is structured as a vertical stack of time-series plots, organized by cell identity. There are at least three distinct traces visible for "cell 3," and the structure suggests multiple cells are being tracked, although only one cell label is clearly visible in the provided crop. The visualization style is a raster plot or multi-channel spike train/activity trace, where the vertical axis represents different cells and the horizontal axis represents time.

**2. Visual Components & Symbols:**
*   **Activity Traces (Top Section):** There are multiple horizontal lines representing the activity of different cells. These traces show fluctuating, noisy signals (likely voltage or firing rate) over time.
    *   The traces are color-coded, with distinct segments showing different colors (e.g., gray/black, light blue, green).
    *   The activity appears to be represented by continuous waveforms or high-frequency fluctuations.
*   **Time Markers/Annotations (Bottom Section):** Below the activity traces, there are horizontal bands or markers that appear to delineate specific time windows or states. These bands are color-coded:
    *   Light orange/tan bands.
    *   Blue bands.
    *   Green bands.
    *   Red/Pinkish bands (visible on the far right).

**3. Labels, Keys & Legends:**
*   **Cell Labeling:** The label "cell 3" is clearly visible on the left side, indicating that the traces immediately adjacent to it correspond to this specific cell.
*   **Color Coding:** The colors (gray, light blue, green, orange/tan) are used both in the activity traces and in the time-window markers below.

**4. Data Trends & Details:**
*   **Activity Traces (Cell 3):** The activity trace for "cell 3" shows periods of high and low fluctuation. There are distinct temporal segments where the activity trace color changes, corresponding to the colored bands below. For instance, there are periods of high-amplitude activity coinciding with specific color blocks in the lower section.
*   **Time Windows:** The colored bands below represent discrete temporal segments. These segments appear to be synchronized with changes in the neural activity above them, suggesting that these colors denote experimental conditions or states (e.g., stimulus presentation, network state).

**5. Contextual Caption Integration:**
While no explicit caption is provided for interpretation, the structure strongly suggests a visualization of neural dynamics (activity traces) mapped onto specific temporal contexts or conditions (the colored bands). The presence of "cell 3" confirms the focus on single-unit or multi-unit recordings. The color coding likely links specific network states (represented by the bands) to corresponding changes in neural firing patterns.



**1. Overall Layout & Structure:**
The figure consists of a multi-panel plot structure, organized vertically. There are four distinct horizontal traces or rows representing different neural units (cells), stacked one above the other. Each trace is a time-series plot, suggesting activity over a continuous period.

**2. Visual Components & Symbols:**
*   **Traces/Plots:** There are four primary horizontal plots, labeled on the left margin as "cell 0," "cell 1," "cell 2," and a fourth unlabeled trace (implied by the structure, though only three are explicitly labeled on the left).
*   **Activity Representation:** Within each trace, activity is represented by fluctuating lines or shaded areas. The traces appear to show the firing rate or some measure of neural activity over time.
*   **Time Axis (X-axis):** Although no explicit numerical scale is provided, the horizontal axis represents time.
*   **Activity Magnitude (Y-axis):** The vertical axis represents the magnitude of activity, though no explicit scale is provided.
*   **Color Coding/Vertical Bands:** The time axis is segmented by vertical colored bands, indicating different experimental conditions or stimulus presentations. These bands are color-coded:
    *   Light Blue/Periwinkle (far left)
    *   Yellowish-Orange (second band)
    *   Reddish/Pink (third band)
    *   Light Blue/Cyan (fourth band)
    *   Pinkish-Red (fifth band)
    *   Light Green/Mint (sixth band)
    *   Yellowish-Orange (seventh band, towards the right)
    *   Light Green/Mint (far right)

**3. Labels, Keys & Legends:**
*   **Title:** "VIP inhibitory - familiar image set A" is centered above the plots.
*   **Cell Labels (Left Margin):** The traces are labeled on the left: "cell 0," "cell 1," and "cell 2."
*   **Right Margin Label:** A partial label, starting with "in," is visible on the far right margin, likely indicating a specific context or layer.

**4. Data Trends & Details:**
The plots show distinct patterns of activity correlated with the colored time segments:

*   **Cell 0:** Shows relatively low baseline activity, followed by distinct peaks of increased activity corresponding to the yellow-orange and reddish/pink bands.
*   **Cell 1:** Exhibits clear, sharp bursts of activity that align strongly with the yellow-orange and reddish/pink bands.
*   **Cell 2:** Displays a more sustained, moderate level of activity across several segments, with noticeable increases during the yellow-orange and reddish/pink bands.
*   **General Trend:** The activity across all cells appears to be modulated by the presentation of different stimuli represented by the colored vertical bands.

**5. Contextual Caption Integration:**
The title "VIP inhibitory - familiar image set A" indicates that the data pertains to neural activity modulated by a stimulus set ("familiar image set A") and is specifically related to the function of VIP (Vasoactive Intestinal Peptide) inhibitory neurons. The structure suggests these plots are tracking the response of individual cells (cell 0, cell 1, cell 2) to these specific visual inputs.


---

## Page 6

except comparison between A-C for excitatory neurons where p=0.05, Welch’s t-test with Bonferroni
correction, see Materials and methods for detailed description of statistics used throughout). Both
VIP and excitatory cells showed increased stimulus omission activity in familiar image sessions
(Figure 3C, p<0.008 for all comparisons with image set A). The fraction of cells that were signifi-
cantly more responsive during image presentations compared to stimulus omission was higher for
novel image sets for both cell classes (Figure 3D, p<0.008 for all comparisons with image set A).
While excitatory cells had a small but significant increase in the fraction of omission responsive cells
(2.3% for image set A versus <1% for image sets B-D), a large fraction of VIP cells were omission
responsive with the familiar image set compared to novel image sets (55% for image set A, 6–20%
for image sets B-D) (Figure 3E, for VIP: p<0.008 for A-B and A-C, p=0.03 for A-D; for excitatory:

0.000

0.002

0.004

0.006

0.008

0.010

mean response

im061

im062

im063

im065

im066

im069

im077

im085

omitted

0

1821

cells

image set A

im012

im013

im036

im044

im047

im057

im078

im115

omitted

0

2472

image set B

im000

im031

im035

im045

im054

im073

im075

im106

omitted

0

2089

image set C

im005

im024

im034

im072

im087

im091

im104

im114

omitted

0

2147

image set D
Excitatory

0.000

0.004

0.008

0.012

0.016

0.020

mean response

im061

im062

im063

im065

im066

im069

im077

im085

omitted

0

148

image set A

im012

im013

im036

im044

im047

im057

im078

im115

omitted

0

173

image set B

im000

im031

im035

im045

im054

im073

im075

im106

omitted

0

154

image set C

im005

im024

im034

im072

im087

im091

im104

im114

omitted

0

151

image set D
VIP Inhibitory

0.00
0.01
image response

0.0

0.5

1.0

fraction of cells

Excitatory

0.00
0.05
image response

VIP Inhibitory

A
B
C
D

A
B
C
D

0.000
0.002
omission response

0.0

0.5

1.0

fraction of cells

Excitatory

0.00
0.02
omission response

VIP Inhibitory

A
B
C
D

A
B
C
D

Excitatory VIP Inhibitory

0.0

0.2

0.4

0.6

0.8

1.0

fraction responsive cells

image responsiveness

Excitatory VIP Inhibitory

0.0

0.2

0.4

0.6

0.8

1.0

fraction responsive cells

omission responsiveness

A

B
D
E
C

Figure 3. Reduced image-evoked activity for familiar stimuli. (A) Heatmap showing the mean response of excitatory (left panels) and VIP inhibitory (right
panels) cells to images and stimulus omission for familiar and novel image sets. Response is computed using detected events in a 500 ms window after
stimulus onset and averaged over all presentations of a given image or image omission. (B) Cumulative distribution of response magnitude for each
cell’s preferred image (excluding omissions) demonstrating reduced image-evoked activity for familiar compared to novel image sets. Insets show
comparisons with p<0.008 (Welch’s t-test with Bonferroni correction was used for all statistical comparisons, see Materials and methods for additional
details). (C) Cumulative distribution of omission response magnitude across cells, demonstrating increased activity during stimulus omission for the
familiar image set A. Insets are as described in panel B. (D) Fraction of image responsive cells is higher for novel image sets compared to the familiar
image set. Image responsiveness is defined for each cell as having >25% of preferred image stimulus presentations with a significant response
compared to a shuffled distribution of values taken from omission periods with extended gray screen. The fraction of image responsive cells is the
number of cells within each session that meet the criterion for image responsiveness. Individual sessions are shown in gray, with mean across sessions
± 95% confidence intervals in color. p<0.008 for all comparisons with image set A. (E) Fraction of omission responsive cells is higher for the familiar
image set in VIP inhibitory cells. Omission responsiveness is defined for each cell as having >10% of stimulus omissions with a significant response
compared to a shuffled distribution of values taken from image presentations. The fraction of omission responsive cells is the number of cells within
each session that meet the criterion for omission responsiveness. Individual sessions are shown in gray, with mean across sessions ± 95% confidence
intervals in color. p<0.008 for A-B and A-C in VIP cells.
The online version of this article includes the following figure supplement(s) for figure 3:

> Figure caption (from PDF text): Figure 3. Reduced image-evoked activity for familiar stimuli. (A) Heatmap showing the mean response of excitatory (left panels) and VIP inhibitory (right
panels) cells to images and stimulus omission for familiar and novel image sets. Response is computed using detected events in a 500 ms window after
stimulus onset and averaged over all presentations of a given image or image omission. (B) Cumulative distribution of response magnitude for each
cell’s preferred image (excluding omissions) demonstrating reduced image-evoked activity for familiar compared to novel image sets. Insets show
comparisons with p<0.008 (Welch’s t-test with Bonferroni correction was used for all statistical comparisons, see Materials and methods for additional
details). (C) Cumulative distribution of omission response magnitude across cells, demonstrating increased activity during stimulus omission for the
familiar image set A. Insets are as described in panel B. (D) Fraction of image responsive cells is higher for novel image sets compared to the familiar
image set. Image responsiveness is defined for each cell as having >25% of preferred image stimulus presentations with a significant response
compared to a shuffled distribution of values taken from omission periods with extended gray screen. The fraction of image responsive cells is the
number of cells within each session that meet the criterion for image responsiveness. Individual sessions are shown in gray, with mean across sessions
± 95% confidence intervals in color. p<0.008 for all comparisons with image set A. (E) Fraction of omission responsive cells is higher for the familiar
image set in VIP inhibitory cells. Omission responsiveness is defined for each cell as having >10% of stimulus omissions with a significant response
compared to a shuffled distribution of values taken from image presentations. The fraction of omission responsive cells is the number of cells within
each session that meet the criterion for omission responsiveness. Individual sessions are shown in gray, with mean across sessions ± 95% confidence
intervals in color. p<0.008 for A-B and A-C in VIP cells.
The online version of this article includes the following figure supplement(s) for figure 3:


### Overall Layout & Structure
The figure consists of two main plots side-by-side, each containing multiple subplots or integrated data visualizations.

**Left Panel: Excitatory Cells**
This panel contains a cumulative distribution plot (Panel B, as per the caption) showing response magnitude.

**Right Panel: VIP Inhibitory Cells**
This panel also contains a cumulative distribution plot (Panel B) showing response magnitude, followed by other related data visualizations implied by the caption structure (though only Panel B is clearly visible in this cropped view).

### Visual Components & Symbols
**Cumulative Distribution Plots (Both Panels):**
*   The plots display cumulative distribution functions. The y-axis represents the "fraction of cells" (ranging from 0.0 to 1.0).
*   The x-axis represents "image response" (ranging from 0.00 to approximately 0.05).
*   Multiple colored lines represent different conditions or stimulus sets (A, B, C, D).
*   Dashed vertical blue lines are present on both plots, likely indicating a threshold or specific point of interest.
*   Asterisks (\*) are used as statistical markers below the plots, indicating significant differences between conditions.

**Color Coding and Labels:**
*   The legend/labels A, B, C, and D are used to distinguish the different conditions being compared.
*   In the context of the caption, these likely correspond to different image sets (e.g., familiar vs. novel).
*   The caption specifies that the lines represent comparisons between "familiar and novel image sets."

### Labels, Keys & Legends
**Titles:**
*   The left panel is titled: "Excitatory".
*   The right panel is titled: "VIP Inhibitory".

**Axes Labels:**
*   Y-axis (Left Panel): "fraction of cells" (ranging from 0.0 to 1.0).
*   X-axis (Left Panel): "image response" (ranging from 0.00 to $\approx 0.05$).
*   Y-axis (Right Panel): "fraction of cells" (ranging from 0.0 to 1.0).
*   X-axis (Right Panel): "image response" (ranging from 0.00 to $\approx 0.05$).

**Annotations:**
*   The letters A, B, C, and D are used to label the different curves on the plots.
*   Asterisks (\*) appear below the plots, indicating statistical significance (e.g., $p<0.008$).

### Data Trends & Details
**Excitatory Cells (Left Plot):**
*   The curves show the cumulative distribution of image response. The general trend suggests that for certain conditions (likely A and B, based on the visual separation), the distribution shifts towards higher response values compared to others (C and D).
*   The dashed blue line appears around an image response value of approximately 0.01.
*   Statistical markers (\*) are present below the plot, indicating significant differences between conditions A/B and C/D.

**VIP Inhibitory Cells (Right Plot):**
*   This plot also shows cumulative distribution curves. The overall shape of the distributions appears similar to the excitatory cells, but the relative positions of the curves differ.
*   The dashed blue line is positioned slightly to the right of the corresponding line in the excitatory panel, around an image response value of approximately 0.015 to 0.02.
*   Statistical markers (\*) are present below the plot, indicating significant differences between conditions A/B and C/D.

*(Note: While the caption describes panels B, C, D, and E, the visible image primarily displays the cumulative distribution plots corresponding to Panel B for both cell types.)*

> Figure caption (from PDF text): Figure 3. Reduced image-evoked activity for familiar stimuli. (A) Heatmap showing the mean response of excitatory (left panels) and VIP inhibitory (right
panels) cells to images and stimulus omission for familiar and novel image sets. Response is computed using detected events in a 500 ms window after
stimulus onset and averaged over all presentations of a given image or image omission. (B) Cumulative distribution of response magnitude for each
cell’s preferred image (excluding omissions) demonstrating reduced image-evoked activity for familiar compared to novel image sets. Insets show
comparisons with p<0.008 (Welch’s t-test with Bonferroni correction was used for all statistical comparisons, see Materials and methods for additional
details). (C) Cumulative distribution of omission response magnitude across cells, demonstrating increased activity during stimulus omission for the
familiar image set A. Insets are as described in panel B. (D) Fraction of image responsive cells is higher for novel image sets compared to the familiar
image set. Image responsiveness is defined for each cell as having >25% of preferred image stimulus presentations with a significant response
compared to a shuffled distribution of values taken from omission periods with extended gray screen. The fraction of image responsive cells is the
number of cells within each session that meet the criterion for image responsiveness. Individual sessions are shown in gray, with mean across sessions
± 95% confidence intervals in color. p<0.008 for all comparisons with image set A. (E) Fraction of omission responsive cells is higher for the familiar
image set in VIP inhibitory cells. Omission responsiveness is defined for each cell as having >10% of stimulus omissions with a significant response
compared to a shuffled distribution of values taken from image presentations. The fraction of omission responsive cells is the number of cells within
each session that meet the criterion for omission responsiveness. Individual sessions are shown in gray, with mean across sessions ± 95% confidence
intervals in color. p<0.008 for A-B and A-C in VIP cells.
The online version of this article includes the following figure supplement(s) for figure 3:


### Overall Layout & Structure
The figure is divided into two main vertical sections, one for "Excitatory" cells and one for "VIP Inhibitory" cells. Each section contains a main plot showing cumulative distribution curves, and an inset box below the main plot containing statistical comparisons.

### Visual Components & Symbols
**Main Plots (Cumulative Distribution):**
*   The plots are standard cumulative distribution curves, where the y-axis represents a probability or fraction (ranging from 0.0 to 1.0).
*   The x-axis represents "omission response" or "emission response," ranging from 0.000 to approximately 0.025.
*   Multiple colored lines represent different conditions or stimulus sets (A, B, C, D).
*   Dashed vertical lines are present in both plots, indicating specific thresholds or comparison points.

**Inset Boxes:**
*   Below the main plot in each section, there is a small inset box containing letters (A, B, C, D) corresponding to the conditions represented by the curves.
*   Asterisks ($\text{*}$) are used next to these letters, indicating statistical significance based on the caption.

### Labels, Keys & Legends
**Titles:**
*   Left Panel Title: "Excitatory"
*   Right Panel Title: "VIP Inhibitory"

**Axis Labels:**
*   Y-axis (Both Panels): Unlabeled, but contextually represents the cumulative distribution of response magnitude.
*   X-axis (Left Panel): "emission response"
*   X-axis (Right Panel): "omission response"

**Data Representation:**
*   The curves are colored, and the caption indicates that colors correspond to different image sets (A, B, C, D).
*   The caption specifies that the curves demonstrate "reduced image-evoked activity for familiar compared to novel image sets."

### Data Trends & Details (Specific Plot Analysis)

**Left Panel: Excitatory Cells**
1.  **Curves:** Four distinct curves (A, B, C, D) are plotted.
2.  **Trend:** The curves generally rise steeply, indicating a distribution of responses.
3.  **Dashed Line:** A dashed vertical line is present around $x \approx 0.0015$.
4.  **Inset Comparison:** The inset shows letters A, B, C, and D with asterisks. The caption notes that the insets show comparisons with $p<0.008$.

**Right Panel: VIP Inhibitory Cells**
1.  **Curves:** Four distinct curves (A, B, C, D) are plotted.
2.  **Trend:** Similar to the left panel, these curves show a cumulative distribution of response magnitude.
3.  **Dashed Line:** A dashed vertical line is present around $x \approx 0.01$.
4.  **Inset Comparison:** The inset shows letters A, B, C, and D with asterisks. The caption notes that the insets show comparisons with $p<0.008$.

### Contextual Caption Integration
The caption clarifies the meaning of these plots:
*   **Main Plots (B):** These cumulative distributions demonstrate "reduced image-evoked activity for familiar compared to novel image sets."
*   **Cell Types:** The left panel represents "excitatory" cells, and the right panel represents "VIP inhibitory" cells.
*   **Statistical Significance:** The asterisks in the insets correspond to statistical comparisons ($p<0.008$) between different image sets (A, B, C, D).
*   **Color/Labeling:** The letters A, B, C, and D refer to specific image sets being compared.

Figure supplement 1. Response sparseness for familiar and novel images.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
6 of 25

Research article
Neuroscience


---

## Page 7

p=0.01 for A-B and A-C, p=0.05 for A-D). This indicates a trade-off between image responsiveness
and omission activity in VIP cells.

We also observed that the responses of individual excitatory neurons to natural images were
more selective for familiar compared to novel stimuli. To evaluate single cell image selectivity, we
quantified lifetime sparseness (Vinje and Gallant, 2000) for image responsive cells. Excitatory popu-
lations had higher lifetime sparseness values for the familiar image set compared to the novel image
sets (p<0.008 for all comparisons with image set A and for B-C for excitatory cells), and excitatory
cells were typically sparser than VIP cells (Figure 3—figure supplement 1A). Plotting the population
tuning curve for each image set revealed sharper tuning in image responsive excitatory cells for
familiar images due to a selective increase in the preferred image response (Figure 3—figure sup-
plement 1B), consistent with previous literature (Woloszyn and Sheinberg, 2012).Together, these
results demonstrate that while overall population activity levels were reduced for familiar images,
single cell selectivity was sharpened.

Inter-stimulus activity dynamics of VIP cells are altered by training
history
Next we investigated the temporal dynamics of activity during stimulus presentation and the preced-
ing inter-stimulus interval by examining the average population activity of VIP and excitatory cells for
each each image set (Figure 4A). The excitatory population showed a sharp increase in activity fol-
lowing stimulus onset, and while familiar images evoked a smaller population response magnitude,
the timing of activity was similar across novel and familiar image sets (Figure 4A, left panel). In con-
trast, VIP population dynamics were very different between familiar and novel images sets. With
novel images, the VIP population response increased following stimulus onset, but with familiar
images, VIP activity ramped up during the inter-stimulus interval and peaked at the time of stimulus
onset (Figure 4A). This pre-stimulus ramping activity was readily apparent in individual VIP cells but
was rare in excitatory cells (Figure 4B). Consistent with this effect, the distribution of peak response
times across VIP cells was shifted earlier in time for familiar versus novel images sets (Figure 4C,
p<0.008 for all image set comparisons except B-C for VIP cells). Excitatory cells also showed a small
but significant difference in the peak time distribution across image sets (Figure 4C, p<0.008 for all
comparisons with image set A, as well as B-C for excitatory cells).

To characterize these dynamics across the population, we made use of a ramping index to quan-
tify activity increases or decreases within the pre-stimulus and stimulus epochs. This index compares
activity between early and late portions of a defined temporal window and is positive for activity
increases and negative for activity decreases (Makino and Komiyama, 2015). The distribution of the
stimulus ramp index was shifted towards positive values for novel images, consistent with increased
image responsiveness (see marginal distributions in Figure 4D, p<0.008 for all comparisons with
image set A, as well as for B-D and C-D for excitatory cells). The distribution of the pre-stimulus
ramp index values was also shifted towards positive values for VIP cells with the familiar image set,
indicating an increase in pre-stimulus ramping (see marginals distributions in Figure 4D, p<0.008 for
all comparisons with image set A, as well as for B-C and C-D for excitatory cells and B-D for VIP
cells). The values of the ramp index for the pre-stimulus and stimulus periods were inversely corre-
lated (Figure 4D; VIP: r =  0.69, p<0.005; excitatory: r =  0.36, p<0.005; linear least-squares
regression fit across all cells). This indicates a tradeoff between stimulus-driven activity and inter-
stimulus ramping, particularly in VIP cells.

To further quantify how these response profiles relate to experience, we determined the fraction
of cells that were stimulus responsive (positive stimulus ramp index) or stimulus suppressed (negative
stimulus ramp index) across image sets (Figure 4E). The majority of excitatory neurons were stimulus
responsive (<85%), although there was a slight increase in the fraction of stimulus suppressed cells
for the familiar image set (1.4% for image set A versus ~0.4% for image sets B-D) (Figure 4E,F, left
panels; p<0.008 for all comparisons with image set A). VIP inhibitory cells showed a larger difference
across image sets: during novel image sessions, most cells were stimulus-driven (<80%), whereas
during familiar image sessions, the majority of VIP cells (60%) were stimulus-suppressed and showed
pre-stimulus ramping (Figure 4E,F right panels; p<0.008 for all comparisons with image set A).

As VIP cell activity has been associated with locomotion and arousal (Dipoppa et al., 2018;
Fu et al., 2014; Pakan et al., 2016), we performed several control analyses to determine whether
these factors could account for VIP cell pre-stimulus ramping activity. First, we sorted the data

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
7 of 25

Research article
Neuroscience


---

## Page 8

according to whether the mouse was running or stationary (see Materials and methods for descrip-
tion of running classification). We found that VIP cells exhibited clear pre-stimulus ramping even
when the mouse stationary (Figure 4—figure supplement 1A–D). Moreover, we examined stimulus-
triggered changes in running speed and found that the pattern of running behavior was similar for
novel and familiar sessions, despite a clear difference in VIP cell dynamics (Figure 4—figure supple-
ment 1C,D). We also analyzed differences in pupil size across image sets to evaluate whether
changes in pupil size around the time of stimulus onset could explain VIP activity dynamics. We
found that in novel sessions pupil area was slightly larger on average, but the stimulus-triggered
dynamics of pupil area changes were relatively flat and did not match the VIP cell dynamics (Fig-
ure 4—figure supplement 1E,F). Together these analyses demonstrate that VIP ramping activity
does not trivially reflect locomotor or pupil dynamics.

-0.5
0.0
0.5
time after stimulus onset (sec)

0.000

0.001

0.002

0.003

0.004

response

Excitatory

image set

A
B
C
D

-0.5
0.0
0.5
time after stimulus onset (sec)

0.0000

0.0025

0.0050

0.0075

0.0100

0.0125
VIP Inhibitory
population average image response

example cells

0.0
0.2
0.4
time to peak (s)

0.0

0.1

0.2

0.3

fraction of cells

0.0
0.2
0.4
time to peak (s)

0.0

0.1

0.2

0.3

A B C D

A
B
C
D

A B C D

A
B
C
D

−5
0
5
stimulus ramp index

−4

−2

0

2

4

r: -0.69, p<0.005

A
B
C
D

VIP Inhibitory

−10
0
10
stimulus ramp index

−10

−5

0

5

10

pre-stimulus ramp index

r: -0.36, p<0.005

A
B
C
D

Excitatory

stimulus

driven

stimulus
suppressed

0.0

0.5

1.0

fraction of cells

Excitatory

stimulus

driven

stimulus
suppressed

VIP Inhibitory

-0.5
0.0
0.5
time (sec)

0

1

normalized

response

-0.5
0.0
0.5
time (sec)

-0.5
0.0
0.5
time (sec)

0

1

-0.5
0.0
0.5
time (sec)

A

B

D

E

C

F

Figure 4. Experience-dependent shift in the dynamics of VIP inhibitory cells. (A) Population activity averaged over all image presentations for excitatory
(left panel) and VIP inhibitory cells (right panel). Traces show mean ± SEM across cells. Note distinct dynamics in VIP population for novel versus familiar
images sets. (B) Example single cell traces showing average image-evoked response for excitatory (left panel) and VIP inhibitory cells (right panel).
Background shading denotes stimulus presentation, with color indicating the image set shown during the session for that cell. Each trace represents a
unique cell recorded in a single session. Scale bar on left of each trace indicates a response magnitude of 0.005. (C) Histogram of time to peak
response after stimulus onset for excitatory (left panel) and VIP inhibitory cells (right panel). Inset shows comparisons across image sets where p<0.008
(Welch’s t-test with Bonferroni correction was used for all statistical comparisons, see Materials and methods for additional details). (D) Stimulus
ramping and pre-stimulus ramping are negatively correlated. Each point is one neuron. The stimulus ramp index was computed over a 125 ms window
after stimulus onset. The pre-stimulus ramp index was computed over a 400 ms window prior to stimulus onset. Data points across all image sets for
each panel were fit with linear least-squares regression. Correlation and significance values for the fit are shown in lower left of each panel. (E) Novel
image sets have an increased fraction of cells with stimulus-driven activity, whereas a larger fraction of cells was stimulus-suppressed for familiar images.
Cells with a positive stimulus ramp index are considered stimulus-driven and those with a negative ramp index are stimulus-suppressed. p<0.008 for all
comparisons with image set A. (F) Population average image evoked response for cells that met the criteria for stimulus driven or stimulus-suppressed,
as described in panel E.
The online version of this article includes the following figure supplement(s) for figure 4:

Figure supplement 1. Changes in image-evoked VIP dynamics are not explained by running behavior or pupil diameter.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
8 of 25

Research article
Neuroscience



**1. Overall Layout & Structure:**
The figure consists of a single plot area featuring multiple overlaid line graphs. The data is presented against two implied y-axes, though only the left axis scale is fully visible and labeled. The x-axis spans a range from approximately 0 to 1, with specific tick marks visible. A shaded vertical band is present in the central region of the plot area, spanning roughly from $x=0.2$ to $x=0.4$.

**2. Visual Components & Symbols:**
*   **Lines/Curves:** Four distinct lines represent the data for Image Sets A, B, C, and D.
    *   **Set A (Red):** Represented by a solid red line.
    *   **Set B (Dark Blue/Navy):** Represented by a solid dark blue line.
    *   **Set C (Medium Blue):** Represented by a solid medium blue line.
    *   **Set D (Light Blue):** Represented by a solid light blue line.
*   **Shaded Region:** A vertical, gray-shaded band is positioned centrally on the x-axis.

**3. Labels, Keys & Legends:**
*   **Legend:** A legend in the upper left corner identifies the color coding:
    *   Red square $\rightarrow$ A
    *   Dark Blue square $\rightarrow$ B
    *   Medium Blue square $\rightarrow$ C
    *   Light Blue square $\rightarrow$ D
*   **Y-Axis (Left):** The left vertical axis is labeled with numerical values ranging from 0.00 to 0.04, marked in increments of 0.01 (e.g., 0.00, 0.01, 0.02, 0.03, 0.04).
*   **X-Axis:** The horizontal axis is not explicitly labeled with a title, but tick marks are present at intervals (e.g., 0.5, 1.0).
*   **Y-Axis (Right):** A secondary y-axis scale is partially visible on the right side, showing values around 0.1 and 0.2 (e.g., 0.1, 0.2).

**4. Data Trends & Details:**
The lines generally follow a similar pattern: an initial decrease, followed by a sharp increase peaking within the shaded region, and then a subsequent decline.

*   **Initial Phase (Left side, $x < 0.2$):** All four lines start at a relatively high value (around 0.015 to 0.02) and decrease slightly, reaching a local minimum around $x \approx 0.1$ to $x \approx 0.2$.
*   **Peak Phase (Within shaded region, $0.2 < x < 0.4$):** All lines rise sharply.
    *   Set D (Light Blue) reaches the highest peak, slightly above 0.035 on the left axis scale.
    *   Set C (Medium Blue) peaks slightly below Set D, around 0.030.
    *   Set B (Dark Blue) peaks slightly lower than Set C, around 0.029.
    *   Set A (Red) peaks at the lowest level among the four, around 0.017 to 0.018.
*   **Decline Phase (Right side, $x > 0.4$):** Following the peak, all lines decrease steadily.
    *   The decline is relatively steep initially and then flattens out as $x$ approaches 1.0, where all lines converge near a value slightly above 0.005 on the left axis scale.

**5. Contextual Caption Integration:**
No specific contextual information regarding cell types, layers, or feedback loops is provided in the visible figure area itself; the legend only identifies the data source as "image set A, B, C, D."



**1. Overall Layout & Structure:**
The figure consists of a single plot area with two distinct lines plotted against shared axes. The background features a vertical shaded gray band, indicating a specific temporal region of interest.

**2. Visual Components & Symbols:**
*   **Axes:** The vertical (Y) axis is labeled with numerical values ranging from 0 to 100, marked in increments of 25 (0, 25, 50, 75, 100). The horizontal (X) axis is not explicitly labeled with units or ticks in the visible portion, but it represents time.
*   **Data Lines:** There are two primary data series represented by lines:
    *   A **blue line**: This line shows a distinct pattern of activity. It starts relatively low, rises sharply to a peak near 100 within the shaded region, and then declines.
    *   A **red line**: This line also shows activity but at a lower magnitude compared to the blue line. It exhibits a broader, more sustained peak that overlaps with the rise of the blue line but remains below 75.
*   **Shaded Region:** A prominent vertical gray band is positioned centrally in the plot, spanning a specific duration on the X-axis.

**3. Labels, Keys & Legends:**
*   **Y-Axis Labeling:** The Y-axis displays numerical values: 0, 25, 50, 75, 100.
*   **X-Axis Labeling:** No explicit label is visible for the X-axis.
*   **Legend/Key:** There is no explicit legend provided within the visible frame to distinguish what the blue and red lines represent, although contextually they likely represent different variables or conditions.

**4. Data Trends & Details:**
*   **Blue Line Trend:** The blue line starts around a value of approximately 70. It decreases slightly before rising steeply to reach its maximum peak, which is at or very near 100, coinciding with the center of the gray shaded region. Following this peak, it shows a rapid decline back towards baseline levels (around 25-30).
*   **Red Line Trend:** The red line starts around a value of approximately 35. It rises gradually, reaching its peak slightly before or within the shaded region, with a maximum value around 65-70. It then gradually declines but remains elevated compared to the blue line's trough immediately following its peak.
*   **Shaded Region Effect:** The gray shaded region appears to correspond precisely with the period where both lines exhibit their highest levels of activity.

**5. Contextual Caption Integration:**
No caption text was provided, so no specific contextual elements (like cell types or feedback loops) can be identified based on external information. The description is limited strictly to the visual data presented in the plot area.



### 1. Overall Layout & Structure
The figure is structured around a large scatter plot occupying the majority of the space. Above this scatter plot, there are overlaid density distributions (histograms/KDE plots). To the right of the scatter plot, there is a vertical density distribution.

### 2. Visual Components & Symbols
**Central Scatter Plot:**
*   The plot displays individual data points scattered across a 2D plane.
*   A prominent **gray diagonal line** runs from the upper-left quadrant (approximately $x=-5, y=4$) down to the lower-right quadrant (approximately $x=5, y=-4$). This line appears to represent a linear relationship or regression boundary.
*   The data points are colored according to four different categories, indicated by the legend: Red (A), Blue (B), Light Blue/Cyan (C), and Pale Blue/Lightest shade (D).

**Upper Density Plot:**
*   Located above the scatter plot, this panel shows overlapping density curves. These curves correspond to the four categories (A, B, C, D) and appear to represent the distribution of one variable across all categories.

**Right Density Plot:**
*   Located to the right edge of the figure, this panel shows a vertical density distribution. This likely represents the marginal distribution of the other variable across all categories.

### 3. Labels, Keys & Legends
**Legend (Top Right):**
A legend identifies the four data categories using colored circles:
*   $\text{A}$: Red circle
*   $\text{B}$: Dark Blue circle
*   $\text{C}$: Medium/Light Blue circle
*   $\text{D}$: Pale Blue circle

**Annotations (Bottom Left of Scatter Plot):**
Statistical metrics are provided below the scatter plot:
*   $r$: $-0.69$ (Correlation coefficient)
*   $p < 0.005$ (P-value)

**Axis Labels:**
*   The horizontal axis (x-axis) ranges from approximately $-5$ to $5$.
*   The vertical axis (y-axis) ranges from approximately $-4$ to $5$.

### 4. Data Trends & Details
**Scatter Plot Trend:**
*   The data points exhibit a clear negative correlation, as indicated by the calculated Pearson correlation coefficient ($r = -0.69$).
*   The data points generally cluster around the descending gray line, confirming a strong negative linear trend between the variables represented on the x and y axes.
*   The density plots above and to the right show the distribution of the variables, with overlapping distributions suggesting that while the overall trend is negative, there are overlaps between the groups A, B, C, and D.

**Density Plot Details:**
*   The upper plot shows multiple overlapping curves (one for each category A, B, C, D), indicating the distribution of one variable.
*   The right plot shows a single vertical density curve, representing the marginal distribution of the other variable.



**1. Overall Layout & Structure:**
The figure is dominated by a single, large scatter plot occupying the majority of the frame. Above this main plot, there are two overlaid density plots (histograms or kernel density estimates) positioned along the top edge of the graph area.

**2. Visual Components & Symbols:**
*   **Scatter Plot:** The main body of the figure contains numerous individual data points scattered across a 2D plane. These points are colored and differentiated according to the legend provided in the upper right corner.
*   **Trend Line:** A single, solid gray line is drawn across the scatter plot, representing a linear regression fit to the data.
*   **Density Plots (Top):** Two smooth, continuous curves are visible along the top edge. These appear to represent the distribution of one variable (likely the x-variable) for different groups, although they are positioned above the main plot area.
*   **Legend:** A legend box is located in the upper right quadrant of the main plot area, identifying four distinct groups (A, B, C, D) associated with different colors/symbols.

**3. Labels, Keys & Legends:**
*   **Axes Labels (Inferred):** The horizontal axis is labeled with numerical values ranging from -10 to 10. The vertical axis is labeled with numerical values ranging from -10 to 10.
*   **Legend Entries:** The legend identifies four groups:
    *   A (represented by a pink/red dot)
    *   B (represented by a blue dot)
    *   C (represented by a light blue/cyan dot)
    *   D (represented by a very light blue/white dot)
*   **Statistical Annotation:** In the lower left corner of the scatter plot, there is a statistical annotation: "r: -0.36, p<0.005".

**4. Data Trends & Details:**
*   **Scatter Plot Trend:** The data points generally exhibit a negative correlation. As the values on the x-axis increase, the corresponding y-values tend to decrease. The gray trend line clearly slopes downwards from the upper left toward the lower right, confirming this negative relationship.
*   **Data Distribution:** The data points are clustered around the origin (0, 0), with a noticeable spread.
*   **Density Plot Detail:** The two density curves at the top show distinct peaks, suggesting differences in the distribution of the variable represented on the x-axis across the groups.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so the description relies solely on the visual elements present in the figure itself. The statistical notation ($r = -0.36, p < 0.005$) indicates a statistically significant negative correlation between the variables plotted on the x and y axes.


---

## Page 9

VIP cells have strong ramping activity during omission of an expected
stimulus
Would cells with pre-stimulus ramping activity continue to ramp if an image was omitted? To assess
this, we analyzed activity during periods in which stimulus presentations were randomly omitted
from the regular sequence. Such trials made up 5% of all non-change stimuli during 2-photon imag-
ing sessions (stimuli were never omitted during behavioral training).

Strikingly, VIP population activity continued to ramp up during stimulus omission, until the subse-
quent stimulus presentation (Figure 5A). Activity following stimulus omission was much stronger dur-
ing familiar compared to novel image sessions (Figure 5B; p<0.008 for all comparisons except A-C
for VIP). Omission ramping was not prominent in the excitatory population (Figure 5A) but there
was a small yet significant increase in the strength of omission activity for the familiar image set
(Figure 5B, p<0.008 for all comparisons with image set A for excitatory). Visualizing mean omission
related activity for all cells as a heatmap for each image set confirmed that very few excitatory cells
showed increases in activity following stimulus omission and were primarily active during the stimulus
presentations before and after omission (Figure 5C). In contrast, most VIP cells showed a dramatic
increase in activity following stimulus omission for familiar stimuli (Figure 5C). In novel image ses-
sions, VIP cell activity was primarily concentrated outside the omission period, with visible stimulus-
locked activity in the surrounding timepoints (Figure 5C).

We again assessed whether the dynamics of neural activity were simply correlated with changes
in locomotor behavior or pupil area. We found that omission ramping activity was present even
when the mice were not running (Figure 5—figure supplement 1A–D). Moreover, omission-trig-
gered pupil dynamics were similar during novel and familiar sessions (Figure 5—figure supplement
1E–F).
To examine the relationship between omission ramping and pre-stimulus ramping in single cells,
we computed the ramp index during the omission window and compared it to the pre-stimulus
ramp index. We found a positive correlation between the strength of pre-stimulus and omission
ramping for VIP cells (Figure 5D; r = 0.49, p<0.005, linear least-squares regression across all VIP
cells). While strong omission ramping typically occurred in neurons that had pre-stimulus ramping, it
was also possible for cells without pre-stimulus ramping to show increases in activity following stimu-
lus omission (Figure 5E). In contrast, pre-stimulus and omission dynamics were not correlated in
excitatory cells.

Discussion
We imaged activity in L2/3 excitatory and VIP inhibitory neurons in response to highly familiar and
novel images during a visual task with a predictable temporal structure. This revealed several
changes associated with training history. Extended experience with a set of images resulted in
reduced overall activity levels in both excitatory and VIP cells. Strikingly, VIP cells exhibited distinct
activity dynamics when tested with familiar versus novel images. Novel images drove stimulus-locked
activity in VIP cells, whereas with familiar images VIP cells had ramping activity during the inter-stim-
ulus interval and were suppressed by stimulus onset. Moreover, these ramping responses continued
increasing when stimuli were omitted from the expected stimulus sequence. The magnitude of VIP
omission-related activity was several times larger than stimulus-driven activity, indicating these are
meaningful signals that could strongly influence network activity. This represents a major experi-
ence-dependent cell type-specific change in response dynamics in sensory cortex.

Predictive processing and changes in activity with experience
Predictive processing has emerged as a powerful paradigm for understanding brain function and
may help reconcile the traditional view of sensory processing with increasing evidence for experience
and context-dependent modulation in early sensory areas. This family of theories posits that the
brain constructs an internal model of the environment based on experience, and that incoming sen-
sory information is compared with learned expectations to continually update the model (de Lange
et al., 2018; Keller and Mrsic-Flogel, 2018; Lochmann and Deneve, 2011; Rao and Ballard,
1999). This dynamic updating with experience is proposed to shift the balance of bottom-up sensory
and top-down predictive pathways. As stimuli become familiar with learning, predictive signals may

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
9 of 25

Research article
Neuroscience


---

## Page 10

2
-2
-1
0
1
2
time after omission (sec)

0.000

0.001

0.002

0.003

0.004

0.005

mean response

Excitatory

-2
-1
0
1
time after omission (sec)

0.000

0.005

0.010

0.015

0.020

VIP Inhibitory

image set

A
B
C
D

population average omission response

A
B
C
D
image set

0.0000

0.0005

0.0010

mean response

Excitatory

A
B
C
D
image set

0.000

0.005

0.010

0.015

0.020

VIP Inhibitory

í
í
0
5
10
omission ramp index

í

í

0

5

10

pre-stimulus ramp index

r: -0.04, p = 0.175106

A
B
C
D

Excitatory

í
0
5
omission ramp index

í

í

0.0

2.5

5.0

r: 0.48, p<0.005

VIP Inhibitory

-2
0
2
-2
0
2
time after omission (sec)

-2
0
2

Excitatory cell examples

-2
0
2
-2
0
2
time after omission (sec)

-2
0
2

VIP Inhibitory cell examples

A
B

D
E

C

0.0000

0.0015

0.0030

0.0045

0.0060

0.0075

mean response

-2

-1

0

1

2

time after omission (s)

0

1984

cells

image set A

-2

-1

0

1

2

time after omission (s)

0

2472

image set B

-2

-1

0

1

2

time after omission (s)

0

2089

image set C

-2

-1

0

1

2

time after omission (s)

0

2147

image set D
Excitatory

0.000

0.005

0.010

0.015

0.020

0.025

0.030

mean response

-2

-1

0

1

2

time after omission (s)

0

148

image set A

-2

-1

0

1

2

time after omission (s)

0

173

image set B

-2

-1

0

1

2

time after omission (s)

0

154

image set C

-2

-1

0

1

2

time after omission (s)

0

151

image set D
VIP Inhibitory

Figure 5. VIP cells show strong ramping activity during stimulus omission. (A) Average population activity around the time of stimulus omission. On
average, excitatory neurons have little change in activity following stimulus omission (left panel). In contrast, activity of the VIP population for the
familiar image set A continues to ramp up until the time of the next stimulus presentation. In sessions with novel images (image sets B, C, D), the VIP
population also shows some change in activity following stimulus omission, but to a lesser degree than with familiar images. (B) Mean activity following
stimulus omission is higher during sessions with the familiar image set A. The mean response in a 750 ms window following the time of stimulus
omission was first computed for each cell in a given session, then averaged across cells in that session. Connected gray points indicate sessions
recorded in a given mouse. Colored points represent the average across sessions for each image set ± 95% confidence intervals. p<0.008 for all
comparisons with image set A, except A-C in VIP inhibitory cells (Welch’s t-test used for all statistical comparisons, see Materials and methods for
additional details). (C) Heatmap of activity around the time of stimulus omission across all excitatory (left panels) and VIP inhibitory cells (right panels),
sorted by magnitude of activity in the omission window. Start of omission period is shown by white vertical line at time = 0 and extends to 750 ms
thereafter when the next stimulus is presented. (D) The strength of the omission ramp index (y-axis) and pre-stimulus ramp index (x-axis) are positively
correlated across VIP cells, but not excitatory cells, indicating that VIP cells with pre-stimulus activity typically also show ramping during stimulus
omission. Data points across all image sets for each panel were fit with linear least-squares regression. Correlation and significance values for the fit are
shown in lower left of each panel. (E) Example cells showing different response dynamics during stimulus (colored bars) and omission (time of expected
stimulus indicated as gray dashed line) for excitatory and VIP inhibitory cells. Color of shaded bars indicates image set (familiar images in red, novel
images in blue). Cells typically show either stimulus-evoked activity and no omission response, or pre-stimulus ramping and strong omission responses.
Some cells (examples in right column of right panel) show a combination of stimulus-evoked and omission activity. Scale bar indicates a response of
0.01.
The online version of this article includes the following figure supplement(s) for figure 5:

> Figure caption (from PDF text): Figure 5. VIP cells show strong ramping activity during stimulus omission. (A) Average population activity around the time of stimulus omission. On
average, excitatory neurons have little change in activity following stimulus omission (left panel). In contrast, activity of the VIP population for the
familiar image set A continues to ramp up until the time of the next stimulus presentation. In sessions with novel images (image sets B, C, D), the VIP
population also shows some change in activity following stimulus omission, but to a lesser degree than with familiar images. (B) Mean activity following
stimulus omission is higher during sessions with the familiar image set A. The mean response in a 750 ms window following the time of stimulus
omission was first computed for each cell in a given session, then averaged across cells in that session. Connected gray points indicate sessions
recorded in a given mouse. Colored points represent the average across sessions for each image set ± 95% confidence intervals. p<0.008 for all
comparisons with image set A, except A-C in VIP inhibitory cells (Welch’s t-test used for all statistical comparisons, see Materials and methods for
additional details). (C) Heatmap of activity around the time of stimulus omission across all excitatory (left panels) and VIP inhibitory cells (right panels),
sorted by magnitude of activity in the omission window. Start of omission period is shown by white vertical line at time = 0 and extends to 750 ms
thereafter when the next stimulus is presented. (D) The strength of the omission ramp index (y-axis) and pre-stimulus ramp index (x-axis) are positively
correlated across VIP cells, but not excitatory cells, indicating that VIP cells with pre-stimulus activity typically also show ramping during stimulus
omission. Data points across all image sets for each panel were fit with linear least-squares regression. Correlation and significance values for the fit are
shown in lower left of each panel. (E) Example cells showing different response dynamics during stimulus (colored bars) and omission (time of expected
stimulus indicated as gray dashed line) for excitatory and VIP inhibitory cells. Color of shaded bars indicates image set (familiar images in red, novel
images in blue). Cells typically show either stimulus-evoked activity and no omission response, or pre-stimulus ramping and strong omission responses.
Some cells (examples in right column of right panel) show a combination of stimulus-evoked and omission activity. Scale bar indicates a response of
0.01.
The online version of this article includes the following figure supplement(s) for figure 5:


### Overall Layout & Structure
The figure is structured as a composite visualization with five labeled sub-panels (A through E), each presenting different types of data—time series plots, mean activity comparisons, heatmaps, correlation plots, and example traces.

### Panel Descriptions

**Panel (A): Average population activity around the time of stimulus omission.**
*   This panel displays two plots side-by-side, comparing activity in different cell types.
*   **Left Panel:** Shows the average population activity for excitatory neurons. The plot shows a relatively flat line, indicating "little change in activity following stimulus omission."
*   **Right Panel:** Shows the average population activity for VIP cells. This plot demonstrates a clear upward trend, indicating that "activity of the VIP population... continues to ramp up until the time of the next stimulus presentation."

**Panel (B): Mean activity following stimulus omission.**
*   This panel is a scatter plot comparing mean activity across different experimental conditions.
*   **Data Points:** Individual data points represent sessions recorded in a specific mouse, connected by gray lines to indicate continuity within that mouse.
*   **Color Coding:** Colored points represent the average across sessions for each image set (A, B, C, D).
*   **Trend:** The caption notes that the mean response is higher during sessions with the familiar image set A.
*   **Annotations:** Statistical significance markers are present, noting $p<0.008$ for all comparisons with image set A, except A-C in VIP inhibitory cells.

**Panel (C): Heatmap of activity around the time of stimulus omission.**
*   This panel is a heatmap divided into two sections: excitatory cells (left panels) and VIP inhibitory cells (right panels).
*   **Structure:** The heatmap visualizes activity magnitude over time.
*   **Time Axis:** A white vertical line marks the "Start of omission period at time = 0," extending to $750 \text{ ms}$ thereafter when the next stimulus is presented.
*   **Sorting:** Cells are sorted by the magnitude of activity within the omission window.

**Panel (D): Correlation plot.**
*   This panel plots two indices against each other: the omission ramp index (y-axis) versus the pre-stimulus ramp index (x-axis).
*   **Data Points:** Data points represent individual VIP cells and excitatory cells.
*   **Trend:** The caption indicates a positive correlation between the omission ramp index and pre-stimulus ramp index across VIP cells, but not excitatory cells.
*   **Annotations:** Linear least-squares regression lines are fitted to the data points, and correlation/significance values are noted in the lower left of each panel.

**Panel (E): Example cells showing different response dynamics.**
*   This panel displays example traces for both excitatory and VIP inhibitory cells.
*   **Structure:** It shows multiple individual cell traces arranged in columns/rows, illustrating different response patterns.
*   **Color Coding:** Shaded bars indicate the image set: red for familiar images, blue for novel images.
*   **Time Markers:** A gray dashed line indicates the "time of expected stimulus."
*   **Response Types Illustrated:** The caption describes typical patterns: (1) Stimulus-evoked activity and no omission response, or (2) Pre-stimulus ramping and strong omission responses. Some cells show a combination of both.
*   **Scale Bar:** A scale bar is provided, indicating a response magnitude of $0.01$.

Figure supplement 1. VIP omission ramping is not explained by running behavior or pupil diameter.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
10 of 25

Research article
Neuroscience



**Overall Layout & Structure:**
The figure consists of four distinct panels, labeled sequentially as "image set A," "image set B," "image set C," and "image set D." Each panel is a time-series visualization, structured as a heatmap where the y-axis represents individual cells and the x-axis represents time following an omission event.

**Visual Components & Symbols:**
Each panel is a dense, rectangular heatmap characterized by varying shades of color against a dark background. The colors transition from deep black/purple to brighter pinks and yellows, indicating varying levels of activity or firing rate.

*   **Y-axis (Cells):** The vertical axis is labeled "cells" and spans a large number of discrete units, suggesting individual neuronal recordings.
*   **X-axis (Time):** The horizontal axis is labeled "time after omission (s)" and shows discrete time points.
*   **Color Gradient:** A color bar is present to the right of the panels, indicating the intensity scale. The colors range from dark purple/black (low activity) to bright yellow/orange (high activity).

**Labels, Keys & Legends:**
*   **Title:** The overarching title above the panels is "Excitatory."
*   **Panel Labels:** Each panel is explicitly labeled: "image set A," "image set B," "image set C," and "image set D."
*   **X-axis Tick Marks:** The x-axes for all four panels share the same structure:
    *   The label is "time after omission (s)."
    *   Tick marks are present at $0$, $1$, and $2$ seconds.
    *   Specific numerical markers are provided below the axis for each panel: $1984$ (under A), $2472$ (under B), $2089$ (under C), and $2147$ (under D). These numbers likely correspond to specific experimental conditions or trial identifiers.
*   **Color Bar:** A vertical color bar is positioned to the right of the panels, indicating the intensity scale. It ranges from $0.000$ (darkest) up to $0.007$ (brightest).

**Data Trends & Details:**
The heatmaps display patterns of activity across the cell population over time. In all four panels (A, B, C, and D), there are visible bursts or streaks of brighter color appearing primarily around the $t=0$ mark and persisting into the subsequent seconds, indicating transient or sustained activity following the omission event. The specific temporal dynamics and spatial distribution of these active cells differ subtly between the four image sets, suggesting variations in the network response across different experimental conditions.



This figure presents four distinct heatmaps, arranged horizontally in a single row, illustrating neural activity related to "VIP Inhibitory" function across four different image sets (A, B, C, and D).

**1. Overall Layout & Structure:**
The figure is composed of four adjacent panels, labeled sequentially as "image set A," "image set B," "image set C," and "image set D." Each panel displays a time-series visualization, structured as a heatmap.

**2. Visual Components & Symbols:**
Each panel is a rectangular plot where the intensity of color represents neural activity. The color scale, indicated by a vertical bar on the right side of the figure, ranges from deep purple/black (low activity) to bright yellow/white (high activity).

**3. Labels, Keys & Legends:**
*   **Title:** The overall figure is titled "VIP Inhibitory."
*   **Y-Axis Label (Shared):** The vertical axis across all panels is labeled "mean response." This axis ranges from $0.0000$ to approximately $0.0075$.
*   **X-Axis Label (Shared):** The horizontal axis across all panels is labeled "time after omission (s)." This axis displays discrete time points: $2$, $1$, $0$, $1$, and $2$ seconds.
*   **Color Bar/Scale:** A vertical color bar is present on the right side, indicating the magnitude of the mean response. The scale ranges from $0.0000$ (darkest color) up to $0.030$ (brightest yellow/white).

**4. Data Trends & Details:**
The heatmaps display dynamic patterns of activity across the time points for each image set:

*   **Image Set A:** Shows a generally high level of activity, with bright streaks visible across the time points, particularly around $t=0$ seconds.
*   **Image Set B:** Exhibits a more structured pattern compared to A, with distinct bands of activity visible across the time points.
*   **Image Set C:** Displays a pattern similar to A, characterized by prominent bursts of activity across the time points.
*   **Image Set D:** Shows a pattern that appears slightly more diffuse or less intensely bright than A and C, though activity is still present across the time points.

**5. Contextual Caption Integration:**
The labels "image set A," "image set B," "image set C," and "image set D" identify the specific experimental conditions or stimuli being analyzed. The axes define that the visualization tracks the *mean response* (Y-axis) as a function of *time after omission* (X-axis), specifically quantifying the inhibitory activity associated with VIP neurons.



**1. Overall Layout & Structure:**
The figure consists of a single plot area with two y-axes: one on the left and one on the right. The x-axis spans from -2 to 2, representing a continuous variable (likely time or a normalized coordinate). The data is presented as four distinct colored lines, corresponding to different image sets identified in the legend.

**2. Visual Components & Symbols:**
*   **Lines/Curves:** Four continuous lines are plotted, each representing a different image set.
*   **Shaded Regions:** There are several vertical shaded gray bands overlaid on the plot, indicating specific regions of interest or experimental conditions.
*   **Dashed Vertical Line:** A dashed vertical line is present near $x=0$.

**3. Labels, Keys & Legends:**
*   **Legend:** A legend in the upper left corner identifies the four data series:
    *   Red line: Image set A
    *   Dark Blue line: Image set B
    *   Medium Blue line: Image set C
    *   Light Blue line: Image set D
*   **Y-Axis Labels:**
    *   Left Y-axis: Labeled with values ranging from 0.000 to 0.005, incrementing in steps of 0.001 (e.g., 0.005, 0.004, ..., 0.000).
    *   Right Y-axis: Labeled with values ranging from 0.0 to 0.4, incrementing in steps of 0.1 (e.g., 0.4, 0.3, ..., 0.0).
*   **X-Axis Label:** The x-axis ranges from -2 to 2.

**4. Data Trends & Details:**
The plot shows cyclical or oscillatory behavior for all four image sets, particularly in the regions around $x=-1$ to $x=1$.

*   **General Trend:** All lines exhibit peaks and troughs. The amplitude of the oscillations varies across the image sets, with Image set D (light blue) generally showing the highest peaks.
*   **Specific Observations:**
    *   Around $x \approx -1$: All lines show a local minimum followed by an increase.
    *   Around $x \approx 0$: The lines are relatively low, with the dashed line marking a transition point.
    *   Around $x \approx 0.5$ to $1$: A major peak occurs, with Image set D reaching the highest value (approaching 0.4 on the right axis).
    *   Around $x \approx 1.5$ to $2$: Another significant peak is visible, though slightly lower than the first major peak.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no interpretation based on external context can be offered. The figure visually compares the temporal dynamics (or spatial profiles) of four distinct datasets (A, B, C, D).



**1. Overall Layout & Structure:**
The figure consists of a single plot spanning the horizontal and vertical axes, without distinct panels (A, B, etc.). The visualization style is a time-series line graph.

**2. Visual Components & Symbols:**
*   **Axes:** There is a horizontal x-axis and a vertical y-axis.
*   **Data Curves:** Two distinct lines are plotted: one colored in **blue** and another colored in **red**. Both curves fluctuate over the displayed time range.
*   **Vertical Marker:** A dashed vertical line is present near $x=0$, serving as a temporal reference point.
*   **Background Shading:** The background of the plot area is segmented by vertical gray shaded bars, suggesting discrete time bins or experimental conditions.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0 to 020, marked in increments of 05 (i.e., 000, 005, 010, 015, 020).
*   **X-Axis Label:** The horizontal axis is labeled with numerical values ranging from -2 to 2, marked in increments of 1 (i.e., -2, -1, 0, 1, 2).
*   **Annotations:** There are no explicit legends identifying the blue and red lines, nor is there a main title provided within the visible frame.

**4. Data Trends & Details:**
*   **X-Axis (Time/Index):** Ranges from -2 to 2.
*   **Y-Axis (Magnitude/Activity):** Ranges from 0 to 20.
*   **Blue Line Trend:** The blue line shows several peaks and troughs. It exhibits a noticeable peak around $x \approx -1$ (reaching $\approx 010$), another smaller peak near $x \approx 0.5$, and a general trend of lower activity in the range $x < -1$ and $x > 1$.
*   **Red Line Trend:** The red line also shows significant fluctuation. It has a prominent peak around $x \approx 0.7$ (reaching $\approx 018$), another peak around $x \approx -0.7$ (reaching $\approx 006$), and generally tracks the blue line but with higher amplitude in certain regions.
*   **Dashed Line ($x=0$):** At the dashed line, both curves show a relative dip or transition point.

**5. Contextual Caption Integration:**
No caption text was provided to integrate specific contextual information (e.g., cell types or experimental conditions). The description is limited strictly to the visual elements present in the plot.


---

## Page 11

suppress bottom-up input, resulting in a sparser code. On the other hand, novel or surprising stimuli
are expected to robustly drive neural activity, signaling deviations from learned predictions.

We observed reduced activity in both VIP and excitatory cells due to long-term experience with a
set of images. The fraction of image responsive cells and mean response magnitude was lower with
familiar versus novel images. Previous studies have shown reductions in activity with experience
(Anderson
et al., 2008; Makino
and Komiyama,
2015;
Mruczek and Sheinberg,
2007;
Woloszyn and Sheinberg, 2012), and also novelty enhancement (Hamm and Yuste, 2016;
Homann et al., 2017; Ranganath and Rainer, 2003). Reduced activity for highly familiar stimuli can
efficiently code predictable stimuli, utilizing a smaller population of cells to represent learned infor-
mation (LeMessurier and Feldman, 2018). On the other hand, enhanced activity for novel stimuli
could aid detection of salient and behaviorally meaningful events by augmenting output to down-
stream targets and facilitating associative plasticity (Ranganath and Rainer, 2003).

Our results demonstrating reduced activity with long-term experience and enhancement with
novelty are consistent with the predictive coding framework. Increased VIP activity in response to
novel images may serve to disinhibit excitatory cell responses to novel stimuli (via the VIP-SST disin-
hibitory circuit). When stimuli are familiar, VIP cells are suppressed by image presentation, which
may permit increased inhibition of excitatory neurons by SST or PV cells, thus increasing the sparse-
ness of stimulus representations. Our observation that VIP cells show ramping activity between famil-
iar images, reminiscent of anticipatory signals, further implicates them in predictive processing.

Ramping activity in VIP cells
What does pre-stimulus and stimulus-omission ramping activity in VIP cells represent? One possibility
is that this activity reflects the temporal structure of the behavioral task such that these signals
encode predictions about stimulus timing or reward expectation, or serve as a temporal attention
signal (Nobre and van Ede, 2018). Previous studies have described stimulus and reward expectation
signals in the visual cortex of rodents. An early example showed that pairing visual stimulation with a
temporally predictable reward produces reward timing signals in visual cortex (Shuler and Bear,
2006). A more recent study using a visual orientation discrimination task in mice found pre-stimulus
ramping activity specifically in the subpopulation of excitatory cells that encoded the rewarded stim-
ulus, suggestive of reward anticipation (Poort et al., 2015). In our task, each stimulus presentation is
a potential opportunity to earn a reward if there is a stimulus change. VIP ramping during the inter-
stimulus interval may be important for enhancing the responses of excitatory cells to an anticipated
change stimulus and consequent reward.

Visual cortex has also been shown to learn experience-dependent stimulus predictions for
repeated sequences of visual stimuli in the absence of association with reward. One study demon-
strated
anticipatory
recall
of
an
omitted
stimulus
in
a
learned
spatiotemporal
sequence
(Gavornik and Bear, 2014). In a virtual navigation paradigm in which mice locomote along a linear
track, V1 neurons have been found to predict upcoming stimuli at specific locations, and to signal a
deviation from expectation when stimuli are omitted (Fiser et al., 2016). In these studies, the predic-
tive signal peaked at the expected time of the predicted event, whereas our results show a contin-
ued ramping past the expected time of stimulus onset on omission trials. This suggests that the
ramping signals we observe may represent something other than a pure prediction of stimulus tim-
ing. It is also important to note that most prior studies documenting predictive or ramping activity
reflect measurements from excitatory neurons, and thus may not be directly comparable to our
results in VIP cells. Nonetheless, VIP cells may serve to gate the predictive or anticipatory signals
documented in excitatory cells.

VIP cells in visual cortex have been shown to be modulated by locomotion and arousal in a con-
text-dependent manner (Dipoppa et al., 2018; Fu et al., 2014; Pakan et al., 2016). The ramping
activity in VIP cells that we observe, however, is not simply a reflection of locomotion or arousal (as
indexed by pupil diameter), since the differences in the dynamics of VIP cells cannot be explained by
differences in the pattern of animal running behavior or changes in pupil diameter relative to stimu-
lus and omission onset.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
11 of 25

Research article
Neuroscience


---

## Page 12

Role of VIP cells in learning and salience detection
Theoretical work suggests that VIP cells could mediate associative learning and experience-depen-
dent signal routing via disinhibition of local excitatory populations (Wang and Yang, 2018;
Wilmes and Clopath, 2018; Yang et al., 2016). Several lines of experimental evidence support this
hypothesis. For example, VIP cells in auditory cortex respond to salient reinforcement signals includ-
ing reward and punishment, and activation of VIP cells enhances the gain of auditory responses
(Letzkus et al., 2011; Pi et al., 2013). Inactivation of VIP cells in visual cortex impairs plasticity fol-
lowing monocular deprivation, while activating VIP cells enhances plasticity (Fu et al., 2017). In the
amygdala, VIP cells are necessary for associative memory formation through disinhibition of local
pyramidal cells during fear learning (Krabbe et al., 2019). Further, VIP cells are modulated by
expectation (Krabbe et al., 2019).

Our finding that VIP cells switch from a stimulus responsive to stimulus suppressed mode
depending on past experience with an image set may be consistent with a role for VIP cells in
enhancing the representation of salient events to facilitate learning and adaptive behavior. During
sessions with novel images, VIP activity is strongly driven by stimulus presentation, potentially serv-
ing to increase the gain of stimulus evoked excitatory responses to salient, novel stimuli. When stim-
uli are familiar, other aspects of the task may become more relevant, such as the unexpected
omission of stimuli from a predictable temporal sequence, and VIP cells switch from signaling the
presence of a stimulus to signaling the absence of a stimulus.

VIP cells in the visual cortex of passively viewing mice are suppressed by high contrast stimuli and
show direction selective responses at low contrast, leading to the proposal that VIP cells are involved
in enhancing the gain of weak but salient stimuli (de Vries et al., 2020; Millman et al., 2019). The
inter-stimulus and omission ramping activity we observed, with a decay in the VIP response following
onset of familiar images, is consistent with the phenomenon of contrast suppression. However our
finding that VIP cells show robust stimulus-evoked responses to novel stimuli demonstrates that VIP
responses are flexible and depend on experience. These seemingly divergent findings can be unified
under the view that VIP cells represent salient stimuli in a context-dependent manner. Novelty may
put cortical circuits in a regime requiring high sensitivity, involving VIP signaling to enhance the gain
of salient stimuli. When stimuli are familiar and the environment is more predictable, VIP cells may
be more sensitive to unexpected events, such as stimulus omission or violations of temporal expec-
tation. It remains an open question whether VIP activity switches from stimulus driven to stimulus
suppressed following passive exposure to a novel set of images in the absence of reward, or
whether active task performance and reinforcement are necessary to observe this context-depen-
dent switch in temporal dynamics.

Future directions
Further modifications of our visual change detection task to include omitted rewards or variation in
the predictability of the inter-stimulus interval could help to distinguish between coding of stimulus
timing versus reward anticipation. Studies examining the evolution of activity in identified VIP cells
across multiple behavior sessions as novel images become familiar are needed to determine the
time course of the observed experience dependent effects. Concurrent recordings of VIP, excitatory,
and other inhibitory cell classes including SST cells will be important to establish a direct link
between VIP activity and disinhibition of local excitatory neurons during task learning. Finally, experi-
ments examining the activity and impact of the diverse inputs to VIP cells, including neuromodula-
tory inputs (Lee et al., 2013; Letzkus et al., 2011), thalamic inputs (Williams and Holtmaat, 2019),
and feedback projections from other cortical regions (Wall et al., 2016; Zhang et al., 2016;
Zhang et al., 2014), will be critical to establish the function of and mechanism behind the shift in VIP
dynamics with experience.

Materials and methods

Key resources table

Reagent (species)
or resource
Designation
Source or reference
Identifiers

Additional
information
Continued on next page

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
12 of 25

Research article
Neuroscience


---

## Page 13

Continued

Reagent (species)
or resource
Designation
Source or reference
Identifiers

Additional
information

Genetic reagent
(M. musculus)

Slc17a7-IRES2-Cre;
Slc17a7+; Excitatory

Jackson Laboratory
Stock #:023527;
RRID:Addgene_61574

PMID: 25741722

Genetic reagent
(M. musculus)

VIP-IRES-Cre; VIP+;
VIP Inhibitory

Jackson Laboratory
Stock #: 010908;
RRID:MGI:4436915

Dr. Z Josh Huang
(Cold Spring
Harbor
Laboratory)

Genetic reagent
(M. musculus)

CaMKII-tTA x
Ai93-GCaMP6f

Jackson Laboratory
Stock #: 024108;
RRID:IMSR_JAX:024108

PMID: 22855807;
PMID: 25741722

Genetic reagent
(M. musculus)

Ai148-GCaMP6f
Jackson Laboratory
Stock #: 030328;
RRID:IMSR_JAX:030328

PMID: 30007418

Software,
algorithm

numpy
NumPy
RRID:SCR_008633

Software,
algorithm

scipy
SciPy
RRID:SCR_008058

Software,
algorithm

matplotlib
MatPlotLib
RRID:SCR_008624

Software,
algorithm

pandas
pandas
DOI:
10.5281/zenodo.3509134

Software,
algorithm

seaborn
seaborn
DOI:
10.5281/zenodo.1313201

Mice
All experiments and procedures were performed in accordance with protocols approved by the
Allen Institute Animal Care and Use Committee. We used male and female transgenic mice express-
ing GCaMP6f in VIP inhibitory interneurons (double transgenic: VIP-IRES-Cre x Ai148 mice; https://
www.jax.org/strain/010908; https://www.jax.org/strain/030328) (Daigle et al., 2018) or in excitatory
glutamatergic neurons (triple transgenic: Slc17a7-IRES2-Cre x CaMKII-tTA x Ai93; https://www.jax.
org/strain/023527, https://www.jax.org/strain/024108) (Madisen et al., 2015; Mayford et al.,
1996). Mice were single housed and maintained on a reverse 12 hr light cycle (off at 9am, on at
9pm) and all experiments were performed during the dark cycle.

Surgery
Surgical procedures were performed as described in de Vries et al. (2020) (see Supplementary Fig-
ure 14). Headpost and cranial window surgery was performed on healthy mice that ranged in age
from 5 to 12 weeks. Pre-operative injections of dexamethasone (3.2 mg/kg, S.C.) were administered
at 12 hr and 3 hr before surgery. Mice were initially anesthetized with 5% isoflurane (1–3 min) and
placed in a stereotaxic frame (Model# 1900, Kopf, Tujunga, CA), and isoflurane levels were main-
tained at 1.5–2.5% for surgery. An incision was made to remove skin, and the exposed skull was lev-
elled with respect to pitch (bregma-lambda level), roll and yaw. The stereotax was zeroed at lambda
using a custom headframe holder equipped with stylus affixed to a clamp-plate. The stylus was then
replaced with the headframe to center the headframe well at 2.8 mm lateral and 1.3 mm anterior to
lambda. The headframe was affixed to the skull with white Metabond and once dried, the mouse
was placed in a custom clamp to position the skull at a rotated angle of 23˚ such that visual cortex
was horizontal to facilitate the craniotomy. A circular piece of skull 5 mm in diameter was removed,
and a durotomy was performed. A coverslip stack (two 5 mm and one 7 mm glass coverslip adhered
together) was cemented in place with Vetbond (Goldey et al., 2014). Metabond cement was
applied around the cranial window inside the well to secure the glass window. Post-surgical brain
health was documented using a custom photo-documentation system and at one, two, and seven
days following surgery, animals were assessed for overall health (bright, alert, and responsive), cra-
nial window clarity, and brain health. After a 1–2 week recovery from surgery, animals underwent
intrinsic signal imaging for retinotopic mapping, then entered into behavioral training.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
13 of 25

Research article
Neuroscience


---

## Page 14

Intrinsic signal imaging
Intrinsic signal imaging (ISI) was performed as described in de Vries et al. (2020) (see Supplemen-
tary Figure 15) to produce a retinotopic map to define visual area boundaries and target in vivo two-
photon calcium imaging experiments to the center of visual space in each imaged area. Mice were
lightly anesthetized with 1–1.4% isoflurane administered with a somnosuite (model #715; Kent Scien-
tific, CON). Vital signs were monitored with a Physiosuite (model # PS-MSTAT-RT; Kent Scientific).
Eye drops (Lacri-Lube Lubricant Eye Ointment; Refresh) were applied to maintain hydration and clar-
ity of eye during anesthesia. Mice were headfixed for imaging.

The brain surface was illuminated with two independent LED lights: green (peak l = 527 nm;
FWHM = 50 nm; Cree Inc, C503B-GCN-CY0C0791) and red (peak l = 635 nm and FWHM of 20 nm;
Avago Technologies, HLMP-EG08-Y2000) mounted on the optical lens. A pair of Nikon lenses lens
(Nikon Nikkor 105 mm f/2.8, Nikon Nikkor 35 mm f/1.4), provided 3.0x magnification (M = 105/35)
onto an Andor Zyla 5.5 10tap sCMOS camera. A bandpass filter (Semrock; FF01-630/92 nm) was
used to record reflected red light from the brain.

A 24’ monitor was positioned 10 cm from the right eye. The monitor was rotated 30˚ relative to
the animal’s dorsoventral axis and tilted 70˚ off the horizon to ensure that the stimulus was perpen-
dicular to the optic axis of the eye (Oommen and Stahl, 2008). The visual stimulus for mapping reti-
notopy was a 20˚ x 155˚ drifting bar containing a checkerboard pattern, with individual square sizes
measuring 25˚, that alternated black and white as it moved across a mean-luminance gray back-
ground. The bar moved in each of the four cardinal directions 10 times. The stimulus was warped
spatially so that a spherical representation could be displayed on a flat monitor (Marshel et al.,
2011).
After defocusing from the surface vasculature (between 500 mm and 1500 mm along the optical
axis), up to 10 independent ISI timeseries were acquired and used to measure the hemodynamic
response to the visual stimulus. Averaged sign maps were produced from a minimum of 3 timeseries
images for a combined minimum of 30 stimulus sweeps in each direction (Garrett et al., 2014).

The resulting ISI maps were automatically segmented by comparing the sign, location, size, and
spatial relationships of the segmented areas against those compiled in an ISI-derived atlas of visual
areas (de Vries et al., 2020). A cost function, defined by the discrepancy between the properties of
the matched areas, was minimized to identify the best match between visual areas in the experimen-
tal sign map and those in the atlas, resulting in an auto-segmented and annotated map for each
experiment. Manual correction and editing of the results included merging and splitting of seg-
mented and annotated areas to correct errors. Finally, target maps were created to guide in vivo
two-photon imaging location using the retinotopic map. The center of retinotopic space was com-
puted from azimuth and altitude maps and adjusted for variability in eye position relative to the
monitor by zeroing to the anatomical center V1. The corresponding retinotopic location was identi-
fied for each visual area, and two-photon imaging was targeted to a region within 20˚ of the center
of gaze.

Behavior training
Water restriction and habituation
Throughout behavior training mice were water-restricted in order to maintain consistent motivation
to learn and perform the behavioral task (Guo et al., 2014). Prior to water restriction mice were
weighed once daily for three days to obtain a stable, initial baseline weight. During the first week of
water restriction mice were handled daily and habituated to increasing duration of head fixation in
the behavior enclosure over a five-day period. Thus, the first day of behavior training occurred after
10 days of water restriction. Mice were trained 5 days per week and could earn as much water as
possible during the daily one-hour sessions; supplemental water was provided if earned volume fell
below 1.0 mL and/or body weight fell under 80–85% of their initial baseline weight. On non-training
days mice were weighed and received enough water provision to reach their target weight of 80–
85% (never less than 1.0 mL per day).

Apparatus
Mice were trained in custom-designed, sound-attenuating behavior enclosures. Visual stimuli were
displayed on a 24’ LCD monitor (ASUS, Model # PA248Q) placed at a ~ 15 cm distance from the

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
14 of 25

Research article
Neuroscience


---

## Page 15

mouse’s right eye. The monitor was rotated 30˚ relative to the animal’s dorsoventral axis and tilted
70˚ off the horizon to ensure that the stimulus was perpendicular to the optic axis of the eye
(Oommen and Stahl, 2008). A behavior stage was placed in a consistent location using a kinematic
mount and consisted of a standardized headframe clamp to enable repeatable positioning of the
mouse relative to the monitor, and a 6.5’ running wheel tilted upwards by 10–15 degrees (see Sup-
plementary Figure 13 of de Vries et al., 2020). Running behavior was measured by a rotational
encoder. Water rewards were delivered using a solenoid (NResearch, Model #161K011) that allowed
for a calibrated volume of fluid to pass through a blunted, 17 g hypodermic needle (Hamilton) posi-
tioned approximately 2–3 mm from the animal’s mouth. Licks were detected by a capacitive sensor
coupled to the reward delivery spout. Running speed, lick times, and reward delivery times were
recorded on a NI PCI-6612 digital IO board and sampled at the frequency of the visual display (60
Hz).

Behavioral training procedure
Mice were trained for 1 hour/day, 5 days/week using an automated training algorithm. Briefly, mice
were trained to lick when the identity of a flashed visual stimulus changed. If mice responded cor-
rectly within a short, post-change response window (750 ms) a water reward (5–10 uL) was delivered.
On Day 1 of the automated training procedure mice received a short, 15 min ‘open loop’ condition-
ing session during which non-contingent water rewards were delivered coincident with 90 degree
changes in orientation of a full-field, static square-wave grating. This session was intended to 1)
introduce the mouse to the fluid delivery system, 2) provide the technician an opportunity to identify
the optimal lick spout position for each mouse and 3) condition the association between stimulus
changes and reward delivery. Each session thereafter was run in ‘closed loop’ mode, and progressed
through 3 stages of the operant task (schematized in Figure 1E): 1) static, full-field square wave gra-
tings (changes between 0 and 90 degrees, spatial frequency 0.04 cycles per degree), 2) full-field
square-wave gratings (changes between 0 and 90 degrees, spatial frequency 0.04 cycles per degree)
presented for 250 ms with an 500 ms inter stimulus gray period, and 3) full-field natural scenes (eight
natural images from the Allen Brain Observatory) presented for 250 ms with a 500 ms inter stimulus
gray period between stimuli. Progression through each stage required mice to achieve a session
maximum d-prime of 1 on two of the last three sessions. The shortest amount of time to reach the
final stage of training was five sessions. Once in stage 3, mice were considered ‘ready for imaging’
when 2 out of 3 sequential sessions had a d-prime >1 and mice performed at least 100 trials. How-
ever, many mice remained in stage 3 of behavior training until the 2-photon microscope became
available. This resulted in a variable training duration in stage three across mice (Figure 1—figure
supplement 1A).

Session and trial structure
Each behavior session lasted 60 min and consisted of a continuous series of image presentations
with GO and CATCH trials interspersed, schematized in Figure 1A,B. Briefly, prior to the start of
each trial a change-type and change-time were selected. Change-type was chosen based on prede-
termined frequencies such that GO and CATCH trials occurred with equal probabilities for sessions
with two oriented gratings. For the natural image phase in which there were 64 change-pair possibil-
ities, CATCH frequency was set to 12.5% (1/8 of the number of image transitions). To ensure even
sampling of all stimulus transitions, a transition path is selected at random from a matrix of 1000
pre-generated paths. Each path takes a pre-determined route through each of the 64 possible tran-
sitions, including same-to-same, or catch, transitions. Once a transition path is completed, another
path is chosen at random.

Change times were selected from an exponential distribution ranging from 2.25 to 8.25 s (mean
of 4.25 s) following the start of a trial. Catch trial times were drawn from the same distribution such
that false alarm rates were measured with the same temporal statistics as change trials, to account
for any learning of the temporal distribution of change times. On trials when a mouse licked prior to
the change or catch time, the trial was restarted with the same scheduled change or catch time. To
prevent mice from getting stuck on a single trial, the number of times a trial could be repeated was
limited to five. GO and CATCH trials, when combined with mouse’s licking response, yield HIT,
MISS, FALSE ALARM, and CORRECT REJECTION trials. In addition to the four trial types described

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
15 of 25

Research article
Neuroscience


---

## Page 16

above, behavior sessions contained a subset of ‘free reward’ trials (GO trials followed immediately
by delivery of a non-contingent reward). Behavior sessions across all phases began with five free-
reward trials to help prime engagement with the task. Additionally, to promote continued task
engagement, one of these free rewards was delivered after 10 consecutive MISS trials.

Each image was shown an average of 487 times during a given one-hour session. On average,
there were 4699 stimulus presentations in each session.

Two-photon imaging during behavior
Visual stimulation
Visual stimuli were generated using custom Python scripts written in PsychoPy (https://www.psy-
chopy.org/; Peirce, 2009; Peirce, 2007) and were displayed using an ASUS PA248Q LCD monitor,
with 1920  1200 pixels. Stimuli were presented monocularly, and the monitor was positioned 15
cm from the mouse’s eye and spanned 120˚ X 95˚ of visual space. The monitor was rotated 30˚ rela-
tive to the animal’s midline and tilted 70˚ off the horizon to ensure that the stimulus was perpendicu-
lar to the optic axis of the eye (Oommen and Stahl, 2008).

The monitor was gamma corrected and had a mean luminance of 50 cd/m2. To account for the
close viewing angle of the mouse, a spherical warping was applied to all stimuli to ensure that the
apparent size, speed, and spatial frequency were constant across the monitor as seen from the
mouse’s perspective (Marshel et al., 2011). Visual stimuli were presented at 60 Hz frame rate.

Visual stimuli consisted of a subset of the natural scene images used in the publicly available Allen
Brain Observatory dataset (https://observatory.brain-map.org/visualcoding/; de Vries et al., 2020).
The 32 natural images that we used originated from three different databases of natural scene
images: the Berkeley Segmentation Dataset (images 000, 005, 012, 013, 024, 031, 034, 035, 036,
044, 047, 045, 054, 057) (Strasburger et al., 2011), the van Hateren Natural Image Dataset (images
061, 062, 063, 065, 066, 069, 072, 073, 075, 077, 078, 085, 087, 091) (van Hateren and van der
Schaaf, 1998), and the McGill Calibrated Colour Image Database (images 104, 106, 114, 115)
(Olmos and Kingdom, 2004). The images were presented in grayscale, contrast normalized,
matched to have equal mean luminance, and resized to 1174  918 pixels.

Behavior apparatus
Running speed measurement, lick detection, and reward delivery were performed as described
above for behavioral training. The monitor was placed in a fixed location relative to the behavior
stage to ensure a consistent relationship between the mouse’s eye and the screen. Running speed,
lick times, and reward delivery times were recorded on a NI PCI-6612 digital IO board and sampled
at the frequency of the visual display (60 Hz).

Two-photon calcium imaging during behavior
Calcium imaging was performed using a Scientifica Vivoscope (https://www.scientifica.uk.com/prod-
ucts/scientifica-vivoscope). Laser excitation was provided by a Ti:Sapphire laser (Chameleon Vision –
Coherent) at 910 nm. Pre-compensation was set at  10,000 fs2. Movies were recorded at 30 Hz
using resonant scanners over a 400 mm field of view (512  512 pixels). Temporal synchronization of
calcium imaging, visual stimulation, reward delivery and behavioral output (lick times and running
speed) was achieved by recording all experimental clocks on a single NI PCI-6612 digital IO board at
100 kHz.
Behavior sessions under the two-photon microscope were 1 hr in duration, with task parameters
identical to stage 3 of the behavior training procedure as described above. In addition, during most
two-photon imaging sessions, 5% of stimulus presentations were randomly omitted, excluding the
change presentation and the presentation immediately prior to the change. These omitted presenta-
tions were added to the experimental protocol partway into the experiment, resulting in 86/101
(85%) imaging sessions including omitted presentations. The 15 sessions without omitted presenta-
tions included data from one Slc17a7-IRES2;CaMKII-tTA;Ai93 mouse (four sessions in VISp), and two
Vip-IRES-Cre;Ai148 mice (three sessions from VISal, and eight sessions from VISp). Sessions without
omitted presentations were excluded from any analysis depending on stimulus omission.

Movies of fluorescence were acquired near the center of retinotopic space in VISp and VISal,
using ISI target maps and vasculature images as a guide. Once a cortical region was selected, the

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
16 of 25

Research article
Neuroscience


---

## Page 17

objective was shielded from stray light coming from the stimulus monitor using opaque black tape.
All recordings were made at a depth of ~175 um from the brain surface. Once a field of view was
selected, a combination of PMT gain and laser power was selected to maximize laser power (based
on a look-up table against depth) and dynamic range while avoiding pixel saturation (max number of
saturated pixels < 1000). Immersion water was occasionally supplemented while imaging using a
micropipette taped to the objective (Microfil MF28G67-5 WPI) and connected to a 5 ml syringe via
an extension tubing. At the end of each experimental session, a z-stack of images (± 30 mm around
imaging site, 0.1 mm step) was collected to evaluate cortical anatomy and evaluate z-drift during
experiment. Experiments with z-drift above 10 mm over the course of the entire session were
excluded.

For each field of view, imaging and behavior sessions were conducted using each of the four
image sets shown in Figure 1F, including the familiar image set A used during behavior training,
and three novel image sets first experienced by the mouse during the imaging phase of the experi-
ment. On subsequent imaging days for a given field of view, we returned to the same location by
matching (1) the pattern of vessels in epi-fluorescence with (2) the pattern of vessels in two photon
imaging and (3) the pattern of cellular labelling in two photon imaging at the previously recorded
location. Typically, only one field of view was imaged per mouse, however in 3 out of the 21 mice,
fields of view were recorded in both VISp and VISal. In cases where an imaging session failed our
QC criteria (for example for z-drift >10 um), the session was retaken. As a result, some sessions with
‘novel’ image sets B, C or D were the second or third exposure (67% were first exposure, 27% were
the second exposure, 6% were the third or fourth exposure). In contrast, mice were exposed to
familiar image set A for an average of 17 ± 14 sessions during training.

Pupillometry
Pupil tracking was performed under 850 nm infrared illumination (OSRAM SYLVANIA Inc, LZ1-
10R602-0000 mounted to a Thorlabs LB1092-B-ML bi-convex lens) using a 30 Hz infrared sensitive
camera (Allied Vision Technologies Mako G-032B) mated to a 0.73x, 130 mm WD lens (Infinity Infin-
iStix, part #213073) and a 845–855 nm bandpass filter (Semrock FF01-850/10-25). The camera and
IR LED were mounted to the left of the animal and focused on a short-pass dichroic mirror (Semrock
FF750-SDi02 25  66, cutoff frequency = 750 nm) positioned between the animal and the monitor,
thus allowing tracking of the right (monitor facing) eye and pupil. Pupil diameter was extracted from
raw video frames using a processing pipeline based on the DeepLabCut tracking algorithm
(Mathis et al., 2018). Briefly, a model was fit using hand-annotated sample frames (12 points each
from the perimeter of the pupil and eyelid) from multiple imaging rigs, subjects, and lighting condi-
tions. The model was then applied to each frame of the 101 eye tracking videos acquired during
imaging sessions, excluding 38 sessions for which frame timing information was incomplete. Points
with a minimum confidence value of 0.8 (output by the DeepLabCut model) were used to fit sepa-
rate ellipses to the eyelid and pupil (Halir and Flusser, 1998). Any frames with fewer than six high-
confidence eye or pupil tracking points, which generally occurred during blinking/squinting, were
not fit (replaced with NaN). Pupil area was then calculated as the area of a circle with a radius equal
to the major axis of the ellipse fit. Frames with calculated areas greater than three standard devia-
tions from the mean were excluded, as were the two frames immediately before and after any miss-
ing fits. Pupil area was interpolated across periods with missing fits.

Quality control
All data streams were required to pass strict quality control criteria (de Vries et al., 2020; see Sup-
plementary Figure 16). For example, Z-drift of the 2-photon imaging plane over the 1 hr imaging
session was quantified by performing phase correlation between the frames of a 100 um z-stack
taken after the imaging session and a 500 frame average from the beginning of the 2-photon movie
and a 500 frame average at the end of the movie. If the distance between the z-stack frames found
to be most correlated with the beginning and end of the movie is greater than 10 um, the session
failed QC and was retaken. Only imaging sessions passing all QC criteria were included in this study.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
17 of 25

Research article
Neuroscience


---

## Page 18

Data processing
Post-processing of 2-photon imaging data was performed as described in de Vries et al.
(2020) (see Supplementary Figures 19, 20, 22, 23). For each two-photon imaging session, the image
processing pipeline included the following steps: (1) motion correction, (2) image normalization to
minimize confounding random variations between sessions, (3) segmentation of ROIs, and (4) ROI fil-
tering. Motion correction was performed using phase correlation and rigid translation. Segmentation
was performed by morphological filtering on normalized periodic average images constructed from
400 frame blocks, followed by unification of masks across all blocks. ROI filtering was performed to
remove segmented regions that were unlikely to correspond to cell somas, based on attributes
including size and shape (for example, small ROIs likely corresponding to apical dendrites were
removed).

Following identification of cell ROIs, the following steps were performed to obtain dF=F traces
and deconvolved event traces: (1) neuropil subtraction, (2) trace demixing, (3) dF=F computation, (4)
L0-regularized event detection. For each ROI, a neuropil mask was created, consisting of a 13 pixel
ring around the cell soma, excluding any other ROIs. The raw fluorescence trace was generated by
averaging all pixels within each cell ROI and the neuropil mask. A neuropil contamination ratio was
computed for each ROI and the calcium trace was modeled as FM ¼ FC þ rFN, where FM is the mea-
sured fluorescence trace, FC is the unknown true ROI fluorescence trace, FN is the fluorescence of
the surrounding neuropil, and r is the contamination ratio. After determination of r, we computed
the true trace as FC ¼ FM   rFN, which is used in all subsequent analysis. To avoid artificially correlat-
ing neurons’ activity by averaging fluorescence over two spatially overlapping ROIs, we demixed the
activity of all recorded ROIs, as described in de Vries et al. (2020). A global dF/F trace for each cell
was computed, with the baseline F0 determined by a rolling mode of 180 seconds across the raw
fluorescence trace. An L0-penalized event detection algorithm was applied to the dF/F trace to
obtain a timeseries of calcium events with a magnitude proportional to the increase in calcium activ-
ity (https://github.com/jewellsean/FastLZeroSpikeInference; Jewell and Witten, 2018; Jewell and
Witten, 2017). Parameters used for event detection can be found at: https://github.com/matchings/
visual_coding_2p_analysis/blob/master/visual_coding_2p_analysis/l0_analysis.py
(Garrett,
2020;
copy
archived
at
https://github.com/elifesciences-publications/visual_coding_2p_analysis).
Event
timeseries were smoothed with a casual half-Gaussian filter with a standard deviation of 0.065 sec.
Temporal alignment was performed to link two-photon acquisition frames (30Hz frame rate) with
visual stimulation frames (60Hz frame rate) and associated behavioral signals (licking, running speed,
reward delivery, sampled at 60Hz frame rate of visual stimulus). The visual stimulus time nearest to
each 2-photon frame time was computed, with the condition that the visual stimulus time must be
before the 2-photon acquisition time, to ensure that dF/F responses were not attributed to stimulus
or behavior events occurring after the change in the calcium signal.

Data analysis
All data analysis was performed using custom scripts in Python and relied heavily on pandas (https://
pandas.pydata.org/), numpy (https://numpy.org/), and scipy (https://www.scipy.org/). Data visualiza-
tion was performed using matplotlib (https://matplotlib.org/) and seaborn (https://seaborn.pydata.
org/).

Behavior
Response rates for GO and CATCH trials were calculated by evaluating the fraction of trials of each
type where a lick was registered within the 750 ms response window following the change or sham
change time (Figure 1I, Figure 1—figure supplement 1E). The fraction of GO trials with a response
is the hit rate and the fraction of CATCH trials with a lick response is the false alarm rate. Response
rate was similarly computed for all non-change stimulus presentations, as well as following stimulus
omission and for the stimulus presentation directly following stimulus omission (Figure 1—figure
supplement 1E). The d-prime value for each session (Figure 1—figure supplement 1D) was com-
puted as:

d

0 ¼ Z hitrate
½
   Z falsealarmrate
½


Where Z is the inverse of the cumulative distribution function (using scipy.stats.norm.ppf).

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
18 of 25

Research article
Neuroscience


---

## Page 19

Reaction time was calculated as the time to first lick after the start of the change time on GO tri-
als (Figure 1J) and displayed using seaborn pointplot. Mean run speed was calculated by taking the
average of the running speed trace in a ± 2 s window around the image change time for each GO
trial, then averaging across all GO trials in each session (Figure 1—figure supplement 1B).The aver-
age running speed trace across sessions (Figure 1—figure supplement 1C) was computed by aver-
aging the running speed trace across all GO trials in a [ 2,6] second window around the change
time for GO trials. A histogram of lick times relative to stimulus omission was generated across all 2-
photon sessions for all mice. The kernel density estimate of lick times was produced for each image
set individually (Figure 1—figure supplement 1F) using seaborn kdeplot.

Calculation of all behavior metrics was limited to the portion of the session where the mouse was
actively engaged in the behavioral task, where engagement was defined those periods during which
the mouse earned at least two rewards per minute. Mice performed 248 engaged GO trials per ses-
sion on average (range = 83–335).

Physiology
All analysis was performed on detected events, with arbitrary units designated as ‘response’
throughout the text and figures.

Neural responses were analyzed with respect to stimulus onset and the time of stimulus omis-
sions. Average stimulus evoked traces were generated by averaging all stimulus presentations for
each image (Figure 2, right panels) or across all stimulus presentations of all images (Figure 4A,B,
Figure 4—figure supplement 1). Average traces around the time of stimulus omission were gener-
ated relative to the time when a stimulus would have been presented (Figure 2, right columns of
right panels, Figure 5A,C,D, Figure 5—figure supplement 1). For each individual image presenta-
tion (or stimulus omission), the mean response in a 500 ms window after stimulus (or omission) onset
was computed (including the 250 ms stimulus duration and 250 ms after to include cells with delayed
responses or off responses after stimulus offset). Then the average across all stimulus presentations
for each image (or omission) was determined (Figure 3A). The cumulative distribution of mean
image response magnitude across cells was generated using seaborn distplot, for the preferred
image for each cell (Figure 3B). The preferred image was identified as the image evoking the largest
mean response for each cell. The cumulative distribution of mean omission response magnitude
across cells was similarly generated using seaborn distplot (Figure 3C).

Image responsiveness (Figure 3D) was calculated by first comparing the mean response to each
individual stimulus presentation for a cell’s preferred image to a shuffled distribution of omission
responses from that same cell. Specifically, we resampled the responses to omitted stimuli by draw-
ing randomly with replacement 10,000 times, and then assigned a p-value to each individual stimulus
presentation equal to the proportion of resampled omitted-stimulus responses that were larger than
the mean response to that stimulus presentation. Neurons were classified as ‘image responsive’ if at
least 25% of presentations of the preferred stimulus had a p-value (with respect to omission
responses) less than 0.05. Similarly, omission responsiveness (Figure 3F) was calculated by compar-
ing each omission response to a shuffled distribution of image responses from the same cell to get a
p-value, then classifying cells as ‘omission responsive’ if at least 10% of omitted-stimulus responses
had a p-value less than 0.05.

To quantify selectivity for individual cells, we used a lifetime sparseness metric, computed using
the definition in Vinje and Gallant (2000):

Sparseness ¼

1   1
N

i

X

ri


2

i

X

r2

i

1   1
N

where N is the number of images and ri is the response of the neuron to image i averaged across tri-
als. Lifetime sparseness was only computed for cells that met the image responsiveness criteria
described above. The cumulative distribution of lifetime sparseness values for image responsive cells
was generated using seaborn distplot (Figure 3—figure supplement 1A). Since there were an insuf-
ficient number of image responsive cells for image set A (<10), the distribution of lifetime sparseness

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
19 of 25

Research article
Neuroscience


---

## Page 20

values for this condition was not shown. We created population tuning curves across image respon-
sive cells by rank sorting the mean response to the 8 images shown in each session for each cell,
then averaging across cells (Figure 3—figure supplement 1B). An insufficient number of VIP cells
(<10) were image responsive for image set A, thus a tuning curve was not included for this condition
in Figure 3—figure supplement 1B.

The population average response was computed by first taking the average stimulus triggered
response across all images for each cell (examples in Figure 4B), then averaging across cells
(Figure 4A). The time to peak response was identified for each cell as the time where the average
stimulus triggered response in a 500 ms window after stimulus onset reached its maximum value
(Figure 4C).

The dynamics of cell responses were evaluated by computing a ramp index over different time
windows of interest, similar to Makino and Komiyama (2015):

Rampindex ¼ log2 Rlate   Rearly

 


Where RlateÞ is the mean response in the first half of a defined window of time, and RearlyÞ is the sec-
ond half of the window. This index provides a measure of the magnitude and direction of a change
in a signal within the window. For Figure 4D and E, the ramp index was computed for two windows:
the pre-stimulus window (400 ms prior to stimulus onset, comparing the first 120 ms with the last
120 ms) and the stimulus window (125 ms after stimulus offset, comparing the first 65 ms with the
last 65 ms in the window) for the mean events trace for each cell across all stimulus presentations of
all images. If the cell trace is increasing during the window, the ramp index is positive. If the cell
trace decreasing during the window, the ramp index is negative.

The pre-stimulus and stimulus ramp indices were plotted against each other on a cell by cell basis
(Figure 4D) and found to be correlated by least squares linear regression between the two measures
(using scipy.stats.linregress). Cells with positive values of the stimulus ramp index were considered
to be ‘stimulus driven’ and cells with negative values of the stimulus ramp index were considered to
be ‘stimulus suppressed’ (Figure 4E,F). The fraction of cells that fell in each of these categories was
calculated for each session, then averaged across sessions for each image set (Figure 4E). The popu-
lation average image response was created by averaging across all cells in each category, regardless
of image set (Figure 4F).

The population average image response was also computed separately for image presentations
where mice were running versus stationary (Figure 4—figure supplement 1A,B). Image presenta-
tions were classified as running if the mean running speed during the [ 0.5, 0.75] second window
around stimulus onset was >5 cm/s and as stationary if the mean running speed was <5 cm/s. To
confirm this classification, and to evaluate any differences in locomotion and arousal across image
sets, we also generated plots of average image triggered running speed and pupil area for stimulus
presentations classified as running and stationary (Figure 4—figure supplement 1C–F). For both
running speed and pupil area, traces aligned to the onset of stimulus presentations were first aver-
aged within each session, then averaged across all sessions for each image set.

For Figure 4D and E, the ramp index was computed for two windows: the pre-stimulus window
(400 ms prior to stimulus onset, comparing the first 120 ms with the last 120 ms) and the stimulus
window (125 ms after stimulus offset, comparing the first 65 ms with the last 65 ms in the window)
for the mean events trace for each cell across all stimulus presentations of all images. If the cell trace
is increasing during the window, the ramp index is positive. If the cell trace decreasing during the
window, the ramp index is negative.

The population average omission response was also computed separately for omissions where
mice were running versus stationary (Figure 5—figure supplement 1A,B). Image presentations were
classified as running if the mean running speed in a ± 2 s window around the time of omission >5
cm/s, and as stationary if the mean running speed in the same window was <5 cm/s. To confirm this
classification, and to evaluate any differences in locomotion and arousal across image sets, we also
generated plots of average omission triggered running speed and pupil area for omissions classified
as running and stationary (Figure 5—figure supplement 1C–F). For both running speed and pupil
area, traces aligned to the time where a stimulus would have been presented, first averaged within
each session, then averaged across all sessions for each image set.

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
20 of 25

Research article
Neuroscience


---

## Page 21

Statistics
For all statistical comparisons, ANOVA (scipy.stats.f_oneway) was used to test for an overall effect of
image set within the excitatory or VIP inhibitory groups, followed by Welch’s two-sample t-test
(scipy.stats.ttest_ind) for each image set pair, using Bonferroni correction for multiple comparisons
to set significance level. p-values are reported throughout the text and figure legends, and signifi-
cance of comparisons where p<0.0083 (an alpha value of 0.05 divided by the number of pairwise
comparisons) are indicated by asterisks in figure insets.

Acknowledgements
We thank Jerome Lecoq and Kevin Takasaki for technical help with the 2-photon microscope, Derric
Williams for help with behavior and stimulus control software, Douglas Kim, Janelia Research Cam-
pus, Howard Hughes Medical Institute, for providing GCaMP6f, and Saskia de Vries, Brian Hu, and
Christof Koch for comments on the manuscript. The authors thank the Allen Institute founder, Paul G
Allen, for his vision, encouragement, and support

Additional information

Funding

Funder
Author

Allen Institute for Brain Science
Marina Garrett
Sahar Manavi
Kate Roll
Douglas R Ollerenshaw
Peter A Groblewski
Justin T Kiggins
Linzy Casal
Kyla Mace
Ali Williford
Arielle Leon
Xiaoxuan Jia
Stefan Mihalas
Nicholas D Ponvert
Peter Ledochowitsch
Michael A Buice
Wayne Wakeman
Shawn R Olsen

The funders had no role in study design, data collection and
interpretation, or the decision to submit the work for publication.

Author contributions
Marina Garrett, Conceptualization, Data curation, Software, Formal analysis, Supervision, Validation,
Investigation, Visualization, Methodology, Writing - original draft, Project administration; Sahar Man-
avi, Data curation, Software, Formal analysis, Investigation, Visualization, Methodology; Kate Roll,
Data curation, Validation, Investigation, Methodology; Douglas R Ollerenshaw, Conceptualization,
Software, Methodology, Writing - review and editing; Peter A Groblewski, Conceptualization, Super-
vision, Methodology, Project administration, Writing - review and editing; Nicholas D Ponvert, Soft-
ware, Formal analysis, Writing - review and editing; Justin T Kiggins, Conceptualization, Software,
Methodology; Linzy Casal, Ali Williford, Project administration; Kyla Mace, Investigation; Arielle
Leon, Methodology; Xiaoxuan Jia, Software; Peter Ledochowitsch, Michael A Buice, Software, Vali-
dation; Wayne Wakeman, Software, Project administration; Stefan Mihalas, Conceptualization, Meth-
odology; Shawn R Olsen, Conceptualization, Supervision, Methodology, Writing - original draft,
Project administration

Author ORCIDs
Marina Garrett
https://orcid.org/0000-0002-5271-2291
Peter A Groblewski
http://orcid.org/0000-0002-8415-1118

Garrett et al. eLife 2020;9:e50340. DOI: https://doi.org/10.7554/eLife.50340
21 of 25

Research article
Neuroscience


---

## Page 22

Stefan Mihalas
http://orcid.org/0000-0002-2629-7100
Shawn R Olsen
https://orcid.org/0000-0002-9568-7057

Ethics
Animal experimentation: All experiments and procedures were performed in accordance with proto-
cols (#1801) approved by the Allen Institute Animal Care and Use Committee (IACUC).

Decision letter and Author response
Decision letter https://doi.org/10.7554/eLife.50340.sa1
Author response https://doi.org/10.7554/eLife.50340.sa2

Additional files

Supplementary files

. Transparent reporting form

Data availability
Figshare DOI: https://doi.org/10.6084/m9.figshare.c.4858779.v1.

The following dataset was generated:

Author(s)
Year Dataset title
Dataset URL

Database and
Identifier

Garrett M, Manavi
S, Roll KR, Oller-
enshaw D, Groble-
wski P, Ponvert ND,
Kiggins JT, Casal L,
Mace K, Williford A,
Leon A, Jia X,
Ledochowitsch P,
Buice MA, Wake-
man W, Mihalas S,
Olsen SR

2020
Experience shapes activity
dynamics and stimulus coding of
VIP inhibitory cells

https://doi.org/10.6084/
m9.figshare.c.4858779.v1

figshare, 10.6084/m9.
figshare.c.4858779.v1