## Page 1

Layer and rhythm specificity for predictive routing

André M. Bastosa,b,1,2, Mikael Lundqvista,b,c, Ayan S. Waitea,b, Nancy Kopelld,1,3, and Earl K. Millera,b,3

aThe Picower Institute for Learning and Memory, Massachusetts Institute of Technology, Cambridge, MA 02139; bDepartment of Brain and Cognitive
Sciences, Massachusetts Institute of Technology, Cambridge, MA 02139; cDivision of Biological Psychology, Department of Psychology, Stockholm University,
SE-10691, Stockholm, Sweden; and dDepartment of Mathematics and Statistics, Boston University, Boston, MA 02215

Contributed by Nancy J. Kopell, October 13, 2020 (sent for review July 17, 2020; reviewed by Ole Jensen and Lucia Melloni)

In predictive coding, experience generates predictions that atten-
uate the feeding forward of predicted stimuli while passing
forward unpredicted “errors.” Different models have suggested
distinct cortical layers, and rhythms implement predictive coding.
We recorded spikes and local field potentials from laminar elec-
trodes in five cortical areas (visual area 4 [V4], lateral intraparietal
[LIP], posterior parietal area 7A, frontal eye field [FEF], and pre-
frontal cortex [PFC]) while monkeys performed a task that modu-
lated visual stimulus predictability. During predictable blocks,
there was enhanced alpha (8 to 14 Hz) or beta (15 to 30 Hz) power
in all areas during stimulus processing and prestimulus beta (15 to
30 Hz) functional connectivity in deep layers of PFC to the other
areas. Unpredictable stimuli were associated with increases in
spiking and in gamma-band (40 to 90 Hz) power/connectivity that
fed forward up the cortical hierarchy via superficial-layer cortex.
Power and spiking modulation by predictability was stimulus spe-
cific. Alpha/beta power in LIP, FEF, and PFC inhibited spiking in deep
layers of V4. Area 7A uniquely showed increases in high-beta (∼22
to 28 Hz) power/connectivity to unpredictable stimuli. These results
motivate a conceptual model, predictive routing. It suggests that
predictive coding may be implemented via lower-frequency alpha/
beta rhythms that “prepare” pathways processing-predicted inputs
by inhibiting feedforward gamma rhythms and associated spiking.

predictive coding | cortical layers | gamma oscillations | beta oscillations |
neural synchronization
T

he brain exploits predictability. It makes cortical processing
more
efficient.
Visuomotor
integration,
visual/auditory
speech perception, and visual perception all benefit when sen-
sory inputs are predictable (1–3). The brain has an arsenal of
mechanisms to tamp down and improve processing of familiar,
repeated, or predictable inputs. One example is stimulus-specific
adaptation. All over cortex, there is less spiking and smaller
blood-oxygen-level-dependent (BOLD) responses when a stim-
ulus is repeated (4–9). Responsiveness is recovered if the stim-
ulus is changed or a pattern is violated (i.e., to “oddballs”) (10,
11). This can lead to fewer activated neurons but finer-tuned,
more robust representations (8).

But the brain does more than adapt to repeated inputs. A wide
variety of evidence indicates that it makes mental models of the
world that actively generate predictions, a process known as pre-
dictive coding (12–14). Moment-to-moment predictions are used
to inhibit processing of expected inputs which, because they were
expected, are not informative. Unexpected sensory inputs that
deviate from a prediction, are “prediction errors” (PEs). They are
informative and thus not inhibited, fed forward, processed, affect
behavior, and are used to update the prediction models.

Much of the work on the neural mechanisms of prediction and
its violation has focused on spiking activity (2, 15–17). But there
is mounting evidence that oscillatory dynamics play a role in
regulating cortical processing and thus can also play a role, es-
pecially the gamma (40 to 90 Hz) and alpha/beta (10 to 30 Hz)
bands (1, 18–25). A key observation is that, all across cortex,
gamma power (>35 Hz)/spiking is higher during bottom-up
sensory inputs. They are anticorrelated with alpha/beta (8 to
30 Hz) power (26–29), which is higher under conditions of top-
down control (e.g., attention and response inhibition) (30–34).

This suggests that top-down alpha/beta help regulate the pro-
cessing of bottom-up inputs served by gamma and spiking. The
idea is that alpha/beta carries the top-down predictions that in-
hibit the gamma/spiking that process expected inputs. This is
consistent with gamma power being higher in the superficial,
feedforward, cortical layers, and alpha/beta power being higher
in the deep, feedback, cortical layers (26, 35–40). Indeed, su-
perficial cortical layers have been hypothesized to be specialized
for computing PEs and feeding PEs forward at gamma frequency
(1, 19). In addition, computational modeling studies have shown
the plausibility of superficial gamma circuits to engage in pre-
diction error computations (38, 41, 42). Direct evidence for al-
pha/beta and gamma in predictive coding per se comes from
observations of increased gamma power to stimuli that are pre-
diction errors (22, 24, 25).

How these rhythms (and their relation to spiking) differ with
stimulus repetition/predictability as well as their stimulus speci-
ficity is not well known. Most neurophysiological studies of the
effects of stimulus predictability have focused on spiking activity,
often in a single area. And none of them to date have examined
and compared activity in different cortical layers. We recorded
local field potentials (LFPs) and spiking using multiarea, multi-
laminar recordings from a visual area (V4) and higher-order
cortical areas (posterior parietal cortex and prefrontal cortex

Significance

An established theoretical model, predictive coding, states that
the brain is constantly building models (signifying changing
predictions) of the environment. The brain does this by form-
ing predictions and signaling sensory inputs which deviate
from predictions (“prediction errors”). Various hypotheses exist
about how predictive coding could be implemented in the
brain. We recorded neural spiking and oscillations with laminar
resolution in a network of cortical areas as monkeys performed
a working memory task with changing stimulus predictability.
Predictability modulated the patterns of feedforward/feedback
flow, cortical layers, and oscillations used to process a visual
stimulus. These data support the theory of predictive coding
but suggest an alternate model for its neural implementation:
predictive routing.

Author contributions: A.M.B. and E.K.M. designed research; A.M.B. and M.L. performed
research; A.M.B. and A.S.W. analyzed data; A.M.B., N.K., and E.K.M. wrote the paper; and
N.K. co-mentored analysis of data formulating the predictive routing framework.

Reviewers: O.J., University of Birmingham; and L.M., New York University Langone
Medical Center.

The authors declare no competing interest.

This open access article is distributed under Creative Commons Attribution-NonCommercial-
NoDerivatives License 4.0 (CC BY-NC-ND).

1To whom correspondence may be addressed. Email: andre.bastos@vanderbilt.edu or nk@
bu.edu.

2Present address: Department of Psychology and Vanderbilt Brain Institute, Vanderbilt
University, Nashville, TN 37240.

3N.K. and E.K.M. contributed equally to this work.

This article contains supporting information online at https://www.pnas.org/lookup/suppl/
doi:10.1073/pnas.2014868117/-/DCSupplemental.

First published November 23, 2020.

www.pnas.org/cgi/doi/10.1073/pnas.2014868117
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31459–31469

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.



**Please provide the academic PDF figure you would like me to describe.**

Once you provide the image, I will structure my response according to your strict requirements:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details (if applicable)**
5. **Contextual Caption Integration**

I await the figure to proceed with the exhaustive analysis as a senior neuroscientist and technical editor.


---

## Page 2

[PFC]) simultaneously. Area V4 was selected as previous studies
have shown this area to be a target of top-down signals such as
attention (43, 44). Frontoparietal cortex was targeted because of
its well-established role in top-down attention and working
memory, cognitive processes that are engaged in the task
employed here (30, 31). We manipulated the predictability of
objects used in a working memory task. This revealed layer and
frequency-specific associations with stimulus repetition/predict-
ability as well as evidence for the direction of flow of these sig-
nals. The findings suggest an update of neural models of
prediction and predictive coding.

Results

Task, Behavior, and Neurophysiological Recordings. Monkeys per-
formed a delayed match to sample (DMS) task (Fig. 1A). The
task was performed in one of two modes: 1) unpredictable
blocks, where one of three objects was chosen randomly as a
sample on each trial for a block of 50 trials; and 2) predictable
blocks, where the same object was used as a sample for 50
consecutive trials. The purpose of the DMS task was to ensure
that animals were always engaged and attending to the stimuli.

Choosing the match was more accurate and faster when the
sample, seen 0.5 to 1.2 s before, had been predictable. Fig. 1 B,
Upper shows the distribution of average performance across
sessions and monkeys for predictable vs. unpredictable blocks.
Average performance during predictable blocks was 80.6% vs.
74.2% for unpredictable blocks (sign test across sessions, P < 1E-

8). Fig. 1 B, Lower shows the corresponding distribution for re-
action time (RT). Although the RT effect size was small, the
match was found significantly more quickly during predictable vs.
unpredictable blocks (mean RT predictable: 236 ms; mean RT
unpredictable: 239 ms; sign test across sessions, P = 0.017).

We recorded spiking and LFPs using multilaminar electrodes
(Fig. 1D) in five cortical areas spanning sensory (V4), posterior
parietal (lateral intraparietal area [LIP] and posterior parietal
area 7A), and PFC and frontal eye fields [FEFs] (Fig. 1C) in two
monkeys over 71 sessions. For areas on cortical gyri (V4, 7A, and
PFC), we introduced the electrodes perpendicular to cortex
(Fig. 1D) to resolve recordings into superficial layers (2/3) vs.
deep layers (5/6). Data were aligned to the top of cortex as this
was the most robust metric with minimal assumptions (SI Ap-
pendix, Experimental Procedures). Areas FEF and LIP are located
in sulci. Recordings there were not layer resolved.

Neurophysiological analysis focused on the 1 s of fixation
before the sample (presample interval) and the 1 s of sample
presentation (sample interval). During the presample interval,
monkeys could have an expectation of the forthcoming sample
during predictable blocks. Once the sample appeared (sample
interval), predictions about the sample could be confirmed
or violated.

Neuronal Spiking Was Greater to Unpredictable than Predictable
Samples. During the sample interval, spike rates were higher if the
sample was unpredictable compared to when it was predictable. The

200 um

3000 um

N= 71 sessions from 2 monkeys

Predictable block (N=50)
Unpredictable block (N=50)

A-A-A-A-...A-
B-C-A-B-B-...C-

FEF

PFC
V4

LIP
7A
P

Sample identity:

sts
as
ps
ls
ips

Example recording location (PFC)

perpendicular to cortex

Fixation Window

Saccade

60
65
70
75
80
85
90
95
100
Accuracy (%)

0

10

20

30

Num sessions

180
200
220
240
260
280
300
320
Reaction Time (ms)

0

5

10

15

20

Num sessions

Predictable
Unpredictable

Predictable
Unpredictable

A

B

C

D

Fixation (1s)
Sample (1s) 
Delay (0.5-1.2s)
Response

Unpredictable blocks

Predictable blocks
Multi-contact
“laminar” U/V probes

Fig. 1.
Task design, recordings, and behavior. (A) Task design: after a 1-s fixation interval, a sample stimulus (one of three pictures) was shown for 1 s. After a
variable delay, the sample reappeared at one of four locations (always randomized). Monkeys saccaded to the sampled stimulus. The sample identity was
either randomized (unpredictable blocks) or held constant (predictable blocks). (B) Behavioral performance across 71 sessions. (Upper) Accuracy on the task
during predictable vs. unpredictable blocks. (Lower) Same, but for reaction time. Solid red/blue bars denote the mean performance and dashed bars denote
the mean ± SEM across sessions. (C) Recorded brain areas. PFC: prefrontal cortex, FEF: frontal eye fields, LIP: lateral intraparietal area, 7A: posterior parietal
area 7A, V4: visual area 4. (D) Multielectrode 16 channel Plexon U/V probes with 200 μm site-to-site spacing. MRIs were used to select grid locations for laminar
(perpendicular) access in areas located on cortical gyri: V4, 7A, and PFC. An example penetration in PFC is shown.

> Figure caption (from PDF text): Fig. 1.
Task design, recordings, and behavior. (A) Task design: after a 1-s fixation interval, a sample stimulus (one of three pictures) was shown for 1 s. After a
variable delay, the sample reappeared at one of four locations (always randomized). Monkeys saccaded to the sampled stimulus. The sample identity was
either randomized (unpredictable blocks) or held constant (predictable blocks). (B) Behavioral performance across 71 sessions. (Upper) Accuracy on the task
during predictable vs. unpredictable blocks. (Lower) Same, but for reaction time. Solid red/blue bars denote the mean performance and dashed bars denote
the mean ± SEM across sessions. (C) Recorded brain areas. PFC: prefrontal cortex, FEF: frontal eye fields, LIP: lateral intraparietal area, 7A: posterior parietal
area 7A, V4: visual area 4. (D) Multielectrode 16 channel Plexon U/V probes with 200 μm site-to-site spacing. MRIs were used to select grid locations for laminar
(perpendicular) access in areas located on cortical gyri: V4, 7A, and PFC. An example penetration in PFC is shown.


Here is a detailed description:

**1. Overall Layout & Structure:**
The image displays a single, high-resolution cross-sectional micrograph or MRI slice, likely representing an anatomical penetration site within the brain tissue. It is a grayscale image with high contrast, characteristic of neuroimaging or histology.

**2. Visual Components & Symbols:**
*   **Background Image:** The majority of the image is a grayscale anatomical slice showing brain tissue structures.
*   **Penetration/Probe Representation:** A prominent, thick red line is superimposed onto the grayscale image. This line represents a penetration or probe trajectory.
*   **Orientation:** The red line is angled, running diagonally from the upper right quadrant down toward the lower center/right.
*   **Contextual Annotation (Implied):** The caption identifies this as "An example penetration in PFC," indicating the red line illustrates a specific access point into the Prefrontal Cortex (PFC).

**3. Labels, Keys & Legends:**
No explicit labels or legends are visible *within* the cropped image itself. The context provided by the caption is crucial for interpretation:
*   The caption states this image illustrates "An example penetration in PFC."

**4. Data Trends & Details:**
As this is an anatomical illustration of a penetration site, there are no data trends or plots to describe. The visual detail focuses on the physical intersection of the probe with the tissue structure.

**5. Contextual Caption Integration:**
The caption identifies this image as illustrating the method used for laminar access:
*   **Purpose:** The technique involves using MRIs to select grid locations for **laminar (perpendicular) access** in specific cortical areas: V4, 7A, and PFC.
*   **Probe Details:** The probes used are described as "Multielectrode 16 channel Plexon U/V probes with $200 \mu\text{m}$ site-to-site spacing."
*   **Interpretation:** The red line visually represents the trajectory of one such probe penetrating perpendicularly into the cortical layers of the PFC.

> Figure caption (from PDF text): Fig. 1.
Task design, recordings, and behavior. (A) Task design: after a 1-s fixation interval, a sample stimulus (one of three pictures) was shown for 1 s. After a
variable delay, the sample reappeared at one of four locations (always randomized). Monkeys saccaded to the sampled stimulus. The sample identity was
either randomized (unpredictable blocks) or held constant (predictable blocks). (B) Behavioral performance across 71 sessions. (Upper) Accuracy on the task
during predictable vs. unpredictable blocks. (Lower) Same, but for reaction time. Solid red/blue bars denote the mean performance and dashed bars denote
the mean ± SEM across sessions. (C) Recorded brain areas. PFC: prefrontal cortex, FEF: frontal eye fields, LIP: lateral intraparietal area, 7A: posterior parietal
area 7A, V4: visual area 4. (D) Multielectrode 16 channel Plexon U/V probes with 200 μm site-to-site spacing. MRIs were used to select grid locations for laminar
(perpendicular) access in areas located on cortical gyri: V4, 7A, and PFC. An example penetration in PFC is shown.


### Overall Layout & Structure
The figure is structured vertically, containing two distinct bar charts: the upper panel (labeled implicitly as part of Panel B in the caption context, but visually distinct) showing accuracy, and the lower panel (also part of Panel B) showing reaction time.

### Visual Components & Symbols
**Upper Plot (Accuracy):**
*   This is a histogram-style bar chart.
*   The x-axis represents "Accuracy (%)" ranging from 60% to 100%.
*   The y-axis represents "Num Sessions," ranging from 0 to 30.
*   Data is presented using vertical bars, color-coded and differentiated by block type:
    *   **Red Bars:** Represent "Unpredictable blocks."
    *   **Blue Bars:** Represent "Predictable blocks."
*   Dashed vertical lines are present above the bars, indicating specific thresholds or means.

**Lower Plot (Reaction Time):**
*   This is also a histogram-style bar chart.
*   The x-axis represents "Reaction Time (ms)" ranging from 180 ms to 320 ms.
*   The y-axis represents "Num Sessions," ranging from 0 to 20.
*   Data is presented using vertical bars, color-coded similarly:
    *   **Red Bars:** Represent "Unpredictable blocks."
    *   **Blue Bars:** Represent "Predictable blocks."

### Labels, Keys & Legends
**Annotations within the Upper Plot:**
*   A legend/annotation box in the upper right corner identifies the block types:
    *   "Unpredictable blocks" is associated with red.
    *   "Predictable blocks" is associated with blue.

**Axis Labels:**
*   Upper Plot X-axis: "Accuracy (%)"
*   Upper Plot Y-axis: "Num Sessions"
*   Lower Plot X-axis: "Reaction Time (ms)"
*   Lower Plot Y-axis: "Num Sessions"

**Data Representation Detail (from Caption):**
*   Solid red/blue bars denote the mean performance.
*   Dashed bars (though not explicitly visible as separate dashed lines in the provided image crop, this is noted from the caption) denote the mean $\pm$ SEM across sessions.

### Data Trends & Details (Observed from Plots)
**Upper Plot (Accuracy):**
*   The distribution of accuracy is centered around 75% to 85%.
*   In the region around 75-80%, there is a high frequency of sessions (tall bars) for both red and blue blocks.
*   The highest peak appears to be in the red (Unpredictable) bars around 75-80%.
*   The blue (Predictable) bars show a significant presence around 80-90%.

**Lower Plot (Reaction Time):**
*   The distribution of reaction times is centered around 210 ms to 250 ms.
*   The highest frequency of sessions (tallest bars) appears in the blue (Predictable) blocks, clustered around 230-240 ms.
*   The red (Unpredictable) blocks show a distribution that is slightly broader or perhaps shifted towards higher reaction times compared to the blue blocks in some regions.

*(Note: The caption references panels C and D, which detail brain areas (PFC, FEF, LIP, 7A, V4) and electrode setups, but these elements are not visible in the provided image crop containing only the behavioral plots (A and B).)*

31460
|
www.pnas.org/cgi/doi/10.1073/pnas.2014868117
Bastos et al.

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.



**1. Overall Layout & Structure:**
The figure is a single, continuous schematic map showing several distinct, irregularly shaped regions overlaid on a generalized cortical surface outline. The representation uses color-coded and labeled areas to denote specific functional or anatomical regions.

**2. Visual Components & Symbols:**
The diagram features several distinct, colored/shaded regions:

*   **PFC (Prefrontal Cortex):** Represented by a large, dark gray/black shaded area located in the lower-left quadrant of the schematic.
*   **FEF (Frontal Eye Field):** A medium-sized, brown/tan shaded area located superior and slightly anterior to the PFC.
*   **LIP (Lateral Intraparietal area):** A small, reddish-brown shaded region situated superiorly and centrally.
*   **7A:** A small, orange-colored area located in the upper right quadrant.
*   **ips (Intraparietal Sulcus/Area):** A label pointing to a region adjacent to LIP.
*   **sts (Superior Temporal Sulcus/Area):** A label pointing to a region inferior to LIP and ips.
*   **V4:** A distinct, teal/green shaded area located in the right-middle section of the schematic.
*   **Is (Inferior Sulcus/Area):** A label pointing to a region adjacent to V4.
*   **as (Anterior Sulcus/Area):** A label pointing to a region adjacent to the PFC.

The overall shape suggests a lateral view of the cortex, with labels indicating specific anatomical landmarks or functional areas.

**3. Labels, Keys & Legends:**
The following labels are present within the schematic:
*   PFC
*   FEF
*   LIP
*   7A
*   ips
*   sts
*   V4
*   Is
*   as

**4. Data Trends & Details:**
As this is a schematic map and not a plot, there are no axes or data trends to describe. The elements represent static anatomical/functional locations.

**5. Contextual Caption Integration:**
The figure visually maps out several key cortical areas (PFC, FEF, LIP, V4) alongside associated anatomical markers (ips, sts, Is, as). The color coding distinguishes these regions: dark gray for PFC, brown/tan for FEF, reddish-brown for LIP, orange for 7A, teal/green for V4. The spatial arrangement suggests a functional connectivity map or topographical representation of visual and executive control areas.



**1. Overall Layout & Structure:**
The figure is structured as a block diagram or schematic representation, showing a single experimental stage. Panel A occupies the left portion of the visible area, adjacent to an unlabelled panel on the right.

**2. Visual Components & Symbols:**
*   **Outer Box (Fixation Window):** A large, rectangular boundary defines the "Fixation Window." This box encloses all elements of this stage.
*   **Central Stimulus:** Inside the Fixation Window, there is a central black solid circle, representing a fixation point.
*   **Dashed Circle:** Surrounding the central black dot is a dashed circle, indicating a region of interest or a target area.
*   **Arrow:** A thick black arrow originates outside the central stimulus area (to the lower-left) and points directly toward the dashed circle/central dot, indicating a directed action or gaze movement.

**3. Labels, Keys & Legends:**
The following text labels are present within or immediately below the schematic:
*   Inside the main box: "Fixation Window" (located in the lower right quadrant of the window).
*   Below the schematic: "Fixation (1s)" (indicating the duration of this stage).

**4. Data Trends & Details:**
As this is a schematic diagram, there are no data trends or axes to describe.

**5. Contextual Caption Integration:**
The visual elements depict a standardized fixation period used in an experiment, where the participant is instructed to maintain focus on a central point for one second.



**1. Overall Layout & Structure:**
The figure is composed of at least three distinct vertical panels arranged side-by-side. The first panel on the left is partially visible, followed by a central panel, and then a third panel on the right. The overall style appears to be schematic or illustrative of visual stimuli presentation rather than a complex circuit diagram or data plot.

**2. Visual Components & Symbols:**
*   **Panel 1 (Left):** This panel is mostly cropped, showing a white background within a black border.
*   **Panel 2 (Center):** This panel features a large white square area bordered in black. Within this central area, there is a small, solid black dot positioned near the center. Surrounding this central dot is a dashed circle (or ring) of medium gray, indicating a spatial or temporal boundary.
*   **Panel 3 (Right):** This panel is also bordered in black and shows two smaller, cropped images stacked vertically. The top image appears to show a portion of a light blue or cyan vehicle (possibly an automobile). The bottom image shows a bright green, rounded object.

**3. Labels, Keys & Legends:**
*   Below the central panel (Panel 2), there is a prominent label: **"Delay (0.5-1.2s)"**. This text is centered beneath the panel and specifies a time interval associated with the stimulus shown in that panel.
*   The text fragment **" )"** is visible to the left of the central panel, suggesting it belongs to a label from Panel 1.

**4. Data Trends & Details:**
Since the panels primarily depict static stimuli rather than dynamic plots, there are no discernible data trends or axes to describe. The central panel illustrates a specific visual configuration (a dot within a dashed circle) presented during a defined delay period.

**5. Contextual Caption Integration:**
The label "Delay (0.5-1.2s)" explicitly defines the temporal context for the stimulus presented in the middle panel, indicating that the visual configuration shown (dot within a dashed circle) is maintained or presented during this specific time window.



**1. Overall Layout & Structure:**
The figure is structured as a tripartite arrangement, consisting of three distinct vertical panels. The middle panel is the most detailed and contains the primary visual element, while the flanking panels appear to be placeholders or subsequent steps in a sequence.

**2. Visual Components & Symbols:**
*   **Panel 1 (Left):** This panel is mostly blank in the visible area, but contains a partial label at the bottom.
*   **Panel 2 (Center):** This panel contains a large white background area with a central visual element. The element is an image of a light blue car, which is enclosed within a dashed black circle/oval. This entire element is framed by a thick black rectangular border, indicating it represents a specific stage or sample.
*   **Panel 3 (Right):** This panel is also mostly blank in the visible area, similar to Panel 1.

**3. Labels, Keys & Legends:**
Several labels are present beneath the panels:
*   Beneath Panel 1, the text "ow" is partially visible.
*   Beneath Panel 2, the label reads: "**Sample (1s)**". This explicitly labels the central panel as representing a sample duration of 1 second.
*   Beneath Panel 3, the text "D" is partially visible, followed by an incomplete label.

**4. Data Trends & Details:**
Since the central element is a static image (a car within a dashed circle) and not a plot, there are no discernible data trends or axes to describe.

**5. Contextual Caption Integration:**
The label "Sample (1s)" in the center panel indicates that this visual representation captures a specific moment or duration of 1 second, likely corresponding to the stimulus presentation time mentioned in the surrounding context (though the full caption is not provided). The visual content itself—a car image—is the stimulus being presented during this 1-second window.



**1. Overall Layout & Structure:**
The figure is structured as a single, large rectangular panel containing several distinct visual elements arranged spatially. The layout suggests a sequence or decision-making process, indicated by the presence of an arrow labeled "Saccade."

**2. Visual Components & Symbols:**
*   **Main Frame:** The central content is enclosed within a large black-bordered rectangle.
*   **Stimuli/Targets:** There are three distinct visual stimuli presented within this frame:
    *   **Top Left Stimulus:** A small image of a light blue sports car is positioned in the upper left quadrant.
    *   **Bottom Left Stimulus:** A solid, bright green, rectangular/block-like shape is positioned in the lower left quadrant.
    *   **Bottom Right Stimulus:** A small image of an orange sphere (resembling a piece of fruit) is positioned in the lower right quadrant.
*   **Saccade Indicator:** A black, filled circle (representing a point of focus or the eye's target) is positioned centrally between the top-left and bottom-right stimuli. An arrow originates near this central point, points towards the car image (top left), and is explicitly labeled "Saccade."
*   **External Elements:** To the far left, there is a partial vertical white box structure. Below this main panel, there are labels indicating temporal or procedural stages: "2s)" and "Response."

**3. Labels, Keys & Legends:**
The following text labels are visible within or immediately adjacent to the main visual area:
*   "Saccade": Located near the central arrow, indicating a rapid eye movement.
*   "Response": A label positioned below the main panel, suggesting an output stage.

**4. Data Trends & Details:**
As this is a schematic diagram and not a plot, there are no axes or data trends to describe. The elements represent discrete states or events in a cognitive process.

**5. Contextual Caption Integration:**
The structure strongly suggests a paradigm where the subject is presented with multiple visual targets (car, green block, orange sphere). The arrow labeled "Saccade" indicates a directed movement of attention or gaze from an initial state (implied, perhaps the center) toward one specific target (the car). The label "Response" below implies that a behavioral output is elicited following this visual processing sequence.


---

## Page 3

black lines in Fig. 2 A–E show the average multiunit activity (MUA)
for unpredictable minus predictable blocks (see SI Appendix, Ex-
perimental Procedures for data preprocessing steps; for MUA re-
sponse to unpredictable vs. predictable without subtraction, see SI
Appendix, Fig. S1). Positive numbers mean more spiking during
unpredictable than predictable blocks. MUA in all areas showed
greater spiking (Fig. 2 A–E, red bars, cluster-based randomization
testing, P < 0.05) to unpredictable than predictable samples. Fur-
ther, analysis of single neurons (SI Appendix, Experimental Proce-
dures) confirmed that, during sample presentation, spikes also
carried more information when the sample was unpredictable (P <
0.05 cluster-based randomization test, Fig. 2F). V4 spiking carried
more sample information than other areas (SI Appendix, Fig. S3A,
Wilcoxon rank sum test, V4 vs. all individual areas, all comparisons
P < 0.01). Further, the increase in spiking to unpredictable samples
was stronger in superficial than deep layers (Fig. 2G) in area V4 but
not in 7A or PFC (Wilcoxon rank sum test for MUA difference,
unpredicted minus predicted, in superficial vs. deep at 0.1 to 0.5 s
postsample onset, P < 0.05).

As expected, given randomly drawn samples during unpre-
dictable blocks, spiking during the presample interval carried no
information about the identity of the forthcoming sample. It did
during predictable blocks in all areas (P < 0.05 cluster-based
randomization test, Fig. 2F). PFC carried more information
about the identity of the forthcoming sample than area V4 (SI
Appendix, Fig. S3B, Wilcoxon rank sum test, V4 vs. PFC, P < 1E-
4). In addition, we analyzed whether the difference in neural
information between unpredictable and predictable blocks was
stronger in superficial vs. deep layers. In the sample interval this
positive difference (more neural information in unpredictable
blocks) was stronger in superficial layers compared to deep
layers (SI Appendix, Fig. S3C, Right subpanel, Wilcoxon rank sum
test, P < 0.01). In the presample interval this negative difference

(more neural information in predictable blocks) was stronger in
deep layers compared to superficial layers (SI Appendix, Fig.
S3C, Left subpanel, Wilcoxon rank sum test, P < 1E-8).

Predictability Changed the LFP Power Balance. Sample predictability
had different effects on different oscillatory bands/layers/areas.
For each frequency, we calculated percent change in LFP power
for unpredictable vs. predictable blocks (Fig. 3 A–E). During the
sample interval, gamma-band power (∼40 to 90 Hz) was higher
to unpredictable samples in all areas. In all areas except FEF,
theta-band power (∼2 to 6 Hz) was higher to unpredictable than
predictable samples (red lines in Fig. 3 A–E indicate significantly
more power during unpredictable samples, P < 0.05, cluster-
based randomization test). The alpha (8 to 14 Hz) and beta
(15 to 30 Hz) bands generally showed the opposite effect (blue
lines in Fig. 3 indicate significantly more power during predict-
able samples, P < 0.05, cluster-based randomization test). It was
generally higher to predictable than unpredictable samples. The
one exception was posterior parietal area 7A where there was
higher power in a high-beta band (∼20 to 27 Hz) during un-
predictable samples (Fig. 3C, but note that in 7A, power in a
lower frequency band, 6 to 14 Hz, was higher for predictable
samples). The differences in power between predictable vs. un-
predictable blocks remained to a large extent significant even
after equating for the time between repetitions of the same
sample in the two block types (SI Appendix, Supplemental Results
and Fig. S5).

The strength of these power differences varied as a function of
layer. Areas V4 and PFC showed a greater increase in
superficial-layer than deep-layer gamma power during unpre-
dictable samples (Fig. 3F, Wilcoxon rank sum test comparing
power modulation in superficial vs. deep layers, P < 0.05) as did
theta in area V4 (Fig. 3I). The PFC showed a greater increase in

A
F

G

B

C

D

E

Fig. 2.
Spiking to unpredictable vs. predictable samples. (A–E) MUA of unpredictable minus predictable blocks. Mean across all available MUAs per area (N =
1,664, 736, 704, 880, and 1,472 for V4, LIP, 7A, FEF, and PFC, respectively), ±1 SEM across MUAs. Horizontal bars denote significance at P < 0.05 for un-
predictable vs. predictable, corrected for multiple comparisons (SI Appendix, Experimental Procedures). (F) Mean information ± SEM, quantified with percent
explained variance (PEV) (see Experimental Procedures) in thresholded single units across all areas about the sample during predictable (blue line) vs. un-
predictable (red line) blocks. Horizontal blue bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable < predictable information.
Horizontal red bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable > predictable information. (G) Unpredictable minus
predictable MUA for deep layers (5/6) vs. superficial layers (2/3), averaged between 0.1 and 0.5 s postsample onset. Mean ± SEM across MUAs in superficial
(N = 575, 215, 397 for areas V4, 7A, and PFC) vs. deep layers (N = 615, 248, and 468 for areas V4, 7A, and PFC). Red asterisk denotes significant differences.

> Figure caption (from PDF text): Fig. 2.
Spiking to unpredictable vs. predictable samples. (A–E) MUA of unpredictable minus predictable blocks. Mean across all available MUAs per area (N =
1,664, 736, 704, 880, and 1,472 for V4, LIP, 7A, FEF, and PFC, respectively), ±1 SEM across MUAs. Horizontal bars denote significance at P < 0.05 for un-
predictable vs. predictable, corrected for multiple comparisons (SI Appendix, Experimental Procedures). (F) Mean information ± SEM, quantified with percent
explained variance (PEV) (see Experimental Procedures) in thresholded single units across all areas about the sample during predictable (blue line) vs. un-
predictable (red line) blocks. Horizontal blue bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable < predictable information.
Horizontal red bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable > predictable information. (G) Unpredictable minus
predictable MUA for deep layers (5/6) vs. superficial layers (2/3), averaged between 0.1 and 0.5 s postsample onset. Mean ± SEM across MUAs in superficial
(N = 575, 215, 397 for areas V4, 7A, and PFC) vs. deep layers (N = 615, 248, and 468 for areas V4, 7A, and PFC). Red asterisk denotes significant differences.


### Overall Layout & Structure
The figure is composed of multiple panels (A through E, and implicitly F and G based on the caption) arranged vertically. Panels A through E are time-series plots showing MUA differences, while the caption references subsequent panels (F and G) which are not fully visible in the provided image crop but are described.

### Visual Components & Symbols
Each panel (A-E) contains a time-series plot.
*   **X-axis:** Represents time, ranging from 0 to 1 (likely normalized time post-sample onset).
*   **Y-axis:** Represents the MUA difference (Unpredictable minus Predictable blocks), ranging from approximately -0.02 to 0.06 in the visible panels.
*   **Data Lines:** Each panel displays a mean trace (a solid line) representing the average MUA difference across multiple units.
*   **Error Bars:** Shaded regions or lines around the mean trace represent $\pm 1$ SEM (Standard Error of the Mean).
*   **Significance Bars:** Horizontal red bars are overlaid on the plots. These bars indicate statistically significant differences between unpredictable and predictable conditions, as detailed in the caption.

### Labels, Keys & Legends
**Panel Labels (Areas):**
*   **A:** V4
*   **B:** LIP
*   **C:** 7A
*   **D:** FEF
*   **E:** PFC

**Axis Labels (Inferred from context):**
*   Y-axis: MUA difference (Unpredictable minus Predictable blocks).
*   X-axis: Time (0 to 1).

**Annotations/Legend Elements:**
*   The caption specifies that the red horizontal bars denote significance at $P < 0.05$ for unpredictable vs. predictable, corrected for multiple comparisons.
*   The caption also specifies the number of MUAs used for each area: V4 ($N=1,664$), LIP ($N=736$), 7A ($N=704$), FEF ($N=880$), and PFC ($N=1,472$).

### Data Trends & Details (Panels A-E)
**Panel A (V4):** Shows a clear, transient peak in the MUA difference around $t=0.1$ to $t=0.2$. A significant red bar spans a portion of the time course, indicating a period where unpredictable activity is significantly higher than predictable activity.
**Panel B (LIP):** Shows a sustained, elevated difference in MUA starting around $t=0.1$ and lasting through the plotted range, with multiple significant red bars indicating sustained differences.
**Panel C (7A):** Shows a relatively flat MUA difference, with some minor fluctuations. A significant red bar is present around $t=0.3$ to $t=0.5$.
**Panel D (FEF):** Displays a sustained, elevated MUA difference across most of the time course shown, indicated by a long red bar spanning from approximately $t=0.1$ to $t=0.9$.
**Panel E (PFC):** Shows a low, relatively flat MUA difference across the time course. A significant red bar is present around $t=0.4$ to $t=0.5$.

### Contextual Caption Integration (Referencing F and G)
The caption describes subsequent panels:
*   **Panel F:** Compares mean information ($\pm$ SEM) quantified with Percent Explained Variance (PEV). It uses blue and red lines:
    *   Blue line: Predictable blocks.
    *   Red line: Unpredictable blocks.
    *   Blue bars indicate significant unpredictable $<$ predictable information.
    *   Red bars indicate significant unpredictable $>$ predictable information.
*   **Panel G:** Compares MUA difference for deep layers (5/6) versus superficial layers (2/3) in V4, 7A, and PFC, averaged between $0.1$ and $0.5$ s post-sample onset. Red asterisks denote significant differences between layer types.

> Figure caption (from PDF text): Fig. 2.
Spiking to unpredictable vs. predictable samples. (A–E) MUA of unpredictable minus predictable blocks. Mean across all available MUAs per area (N =
1,664, 736, 704, 880, and 1,472 for V4, LIP, 7A, FEF, and PFC, respectively), ±1 SEM across MUAs. Horizontal bars denote significance at P < 0.05 for un-
predictable vs. predictable, corrected for multiple comparisons (SI Appendix, Experimental Procedures). (F) Mean information ± SEM, quantified with percent
explained variance (PEV) (see Experimental Procedures) in thresholded single units across all areas about the sample during predictable (blue line) vs. un-
predictable (red line) blocks. Horizontal blue bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable < predictable information.
Horizontal red bars indicate significant (P < 0.05, corrected for multiple comparisons) unpredictable > predictable information. (G) Unpredictable minus
predictable MUA for deep layers (5/6) vs. superficial layers (2/3), averaged between 0.1 and 0.5 s postsample onset. Mean ± SEM across MUAs in superficial
(N = 575, 215, 397 for areas V4, 7A, and PFC) vs. deep layers (N = 615, 248, and 468 for areas V4, 7A, and PFC). Red asterisk denotes significant differences.


### Panel 1 (Top Plot)

This panel is a time-series plot showing Mean Unit Activity (MUA).
*   **Y-axis:** Labeled with numerical values ranging from 0 to 0.05, representing the activity level (likely MUA).
*   **X-axis:** Labeled "Time relative to sample onset (s)," ranging from approximately -1.0 s to 1.0 s.
*   **Data Representation:** Two distinct lines are plotted:
    *   A **blue line**, labeled "Predictable," shows relatively low activity across the time course, with a slight increase around sample onset.
    *   A **red line**, labeled "Unpredictable," shows low activity before sample onset, a sharp and significant peak immediately following sample onset (around $t=0$ s), followed by a gradual decay.
*   **Annotations:** The lines are color-coded and labeled directly above the plot area: "Unpredictable" (red) and "Predictable" (blue).
*   **Contextual Note:** The caption indicates this plot shows "MUA of unpredictable minus predictable blocks."

### Panel 2 (Bottom Left Bar Chart)

This panel is a bar chart comparing activity across different brain areas.
*   **Y-axis:** Labeled with numerical values ranging from 0 to approximately 0.025, representing a measured value (likely related to activity or information).
*   **X-axis:** Displays three distinct brain areas: "V4," "7A," and "PFC."
*   **Data Representation:** For each area, there are two bars: a blue bar and an orange/red bar.
    *   **V4:** Shows a blue bar (approx. 0.015) and an orange/red bar (approx. 0.022).
    *   **7A:** Shows a blue bar (approx. 0.010) and an orange/red bar (approx. 0.009).
    *   **PFC:** Shows a blue bar (approx. 0.010) and an orange/red bar (approx. 0.016).
*   **Annotations:** A red asterisk ($\text{*}$) is placed above the V4 bars, indicating a significant difference.
*   **Contextual Note:** The caption identifies this as comparing "Deep vs Superficial" layers, and the bars likely represent differences in activity or information between these layer types across V4, 7A, and PFC.

### Panel 3 (Bottom Right Bar Chart)

This panel is another bar chart, likely related to the information content mentioned in the caption.
*   **Y-axis:** Labeled with numerical values ranging from 0 to approximately 0.025, representing a measured value (likely related to information).
*   **X-axis:** Displays the same three brain areas: "V4," "7A," and "PFC."
*   **Data Representation:** Similar to Panel 2, there are two bars for each area (blue and orange/red).
    *   **V4:** Shows a blue bar (approx. 0.015) and an orange/red bar (approx. 0.023).
    *   **7A:** Shows a blue bar (approx. 0.010) and an orange/red bar (approx. 0.009).
    *   **PFC:** Shows a blue bar (approx. 0.010) and an orange/red bar (approx. 0.016).
*   **Contextual Note:** The caption specifies that this panel relates to "Mean information $\pm$ SEM, quantified with percent explained variance (PEV)" and describes the significance of red/blue bars based on whether unpredictable $>$ predictable or vice versa.

Bastos et al.
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31461

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 4

superficial layer than deep alpha (8–14 Hz) and beta (15 to 30
Hz) during predictable samples (Fig. 3 G and H, Wilcoxon rank
sum test, P < 1E-3 for both alpha and beta). Area 7A showed a
greater increase in superficial layer than deep beta (15–30 Hz)
during unpredictable samples (Fig. 3G, Wilcoxon rank sum test,
P < 1E-4). In area V4 in the alpha band (8–14 Hz), superficial
and deep layers had different signs of modulation with respect to
sample predictability. V4 deep-layer alpha increased with pre-
dictable samples but superficial-layer alpha increased to unpre-
dictable samples (Fig. 3H, Wilcoxon rank sum test comparing
power modulation in superficial vs. deep layers, P < 1E-8).

In, general, the sites with strong MUA modulation (unpre-
dictable vs. predictable) were also sites with strong LFP gamma
power modulation (unpredictable vs. predictable, SI Appendix,
Supplemental Results and Fig. S2). The positive relationship be-
tween MUA and LFP gamma-power modulation was consis-
tently strongest in superficial as compared to deep layers (SI
Appendix, Fig. S2B, Wilcoxon rank sum test comparing correla-
tion between MUA and gamma-power modulation in superficial
vs. deep layers, P < 1E-4 for all areas). By contrast, in area V4
the negative relationship between MUA and LFP alpha- and
beta-power modulation were consistently strongest in deep as
compared to superficial layers (SI Appendix, Fig. S2 C and D,
Wilcoxon rank sum test comparing correlation between MUA
and alpha- and beta-power modulation in superficial vs. deep
layers, P < 0.05 for both alpha and beta).

The increase in gamma and theta power was greater in V4
compared to higher areas (SI Appendix, Fig. S3 D and G). V4
showed the greatest increase in gamma and theta power during

unpredictable samples while PFC/7A showed the smallest. In
contrast, in the alpha band (8 to 14 Hz), LIP, PFC, and 7A had the
strongest power modulation to predictable samples. The strength
of alpha-band power modulation in all higher-order areas was
stronger than in V4 (SI Appendix, Fig. S3F, V4 alpha-band power
modulation vs. all other areas, Wilcoxon rank sum test, P < 1E-2).
In the beta band (15 to 30 Hz) PFC had the strongest power
modulation to predictable samples of any area (SI Appendix, Fig.
S3E, PFC beta-band power modulation vs. all other areas, Wil-
coxon rank sum test, P < 1E-16 for all comparisons).

Sample predictability also modulated LFP power during the
presample interval but the effects were weaker and sparser.
There was greater gamma/high-beta power during unpredictable
than predictable blocks in V4, LIP, and 7A and reduced alpha/
beta power in V4, 7A, and FEF (P < 0.05, SI Appendix, Fig.
S4 A–E). During the presample interval, power modulation did
not differ between superficial vs. deep layers (all comparisons,
P > 0.05).

Violation of Predictions and Time Course of Prediction. During pre-
dictable blocks, a strong expectation of a specific sample object
could build. Then, when there was a switch to an unpredictable
block, that expectation was violated for at least the first few
trials. We examined the LFP power as a function of the number
of trials since a switch from a predictable to an unpredictable
block. This revealed strong gamma increases in all areas that
were maximal within the first few trials of such a “violation” of
expectation (SI Appendix, Supplemental Results and Fig. S6A).

Power change (%)

Theta (2-6 Hz)

Power change (%)
Power change (%)

Power change Unpredictable vs. Predictable (%)

Gamma (40-90 Hz)

V4
7A
PFC

Deep
Superﬁcial

Frequency (Hz)

A
F

G

H

B

C

D

E

*

*

*

*

*

*

-2

0

2

4

-6

-4

-2

0

-5

0

5

0
1

2

3

4

Power change (%)

I

Alpha (8-14 Hz)

Beta (15-30 Hz)
Deep
Superﬁcial

Deep
Superﬁcial

Deep
Superﬁcial

V4
7A
PFC

V4
7A
PFC

V4
7A
PFC

-5

0
5
10
15

0

5

10

-5

0

5

-5

0

5

0

10

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

V4

LIP

7A

FEF

PFC

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

*

unpredictable  > predictable

predictable > unpredictable

Fig. 3.
LFP power for unpredictable vs. predictable samples. (A–E) Unpredictable vs. predictable percent change in LFP power from 0 to 100 Hz during the 1-s
sample processing interval. Mean across all available bipolar derivations of LFPs per area (N = 1,483, 666, 650, 793, and 1,358 for V4, LIP, 7A, FEF, and PFC,
respectively), ±1 SEM across LFPs. Horizontal red bars denote significance at P < 0.05 for power in unpredictable > predictable blocks, blue bars for power in
predictable > unpredictable blocks (corrected for multiple comparisons). (F–I) Percent change in LFP power for unpredictable vs. predictable samples for deep
vs. superficial layers in different bands. (F) Gamma band (40 to 90 Hz), (G) beta band (15 to 30 Hz), (H) alpha band (8 to 14 Hz), (I) theta band (2 to 6 Hz).
Mean ± SEM across LFPs in superficial (N = 564, 227, and 410 for areas V4, 7A, and PFC) vs. deep layers (N = 586, 245, and 480 for areas V4, 7A, and PFC). Red
asterisk denotes significant (P < 0.05) differences.

> Figure caption (from PDF text): Fig. 3.
LFP power for unpredictable vs. predictable samples. (A–E) Unpredictable vs. predictable percent change in LFP power from 0 to 100 Hz during the 1-s
sample processing interval. Mean across all available bipolar derivations of LFPs per area (N = 1,483, 666, 650, 793, and 1,358 for V4, LIP, 7A, FEF, and PFC,
respectively), ±1 SEM across LFPs. Horizontal red bars denote significance at P < 0.05 for power in unpredictable > predictable blocks, blue bars for power in
predictable > unpredictable blocks (corrected for multiple comparisons). (F–I) Percent change in LFP power for unpredictable vs. predictable samples for deep
vs. superficial layers in different bands. (F) Gamma band (40 to 90 Hz), (G) beta band (15 to 30 Hz), (H) alpha band (8 to 14 Hz), (I) theta band (2 to 6 Hz).
Mean ± SEM across LFPs in superficial (N = 564, 227, and 410 for areas V4, 7A, and PFC) vs. deep layers (N = 586, 245, and 480 for areas V4, 7A, and PFC). Red
asterisk denotes significant (P < 0.05) differences.


### Overall Layout and Structure
The figure consists of a series of bar plots arranged vertically, organized by frequency band.

*   **Top Section (Panels A-E):** These panels compare LFP power changes between unpredictable and predictable samples across different brain areas (V4, 7A, PFC).
*   **Bottom Section (Panels F-I):** These panels specifically compare the percent change in LFP power between deep and superficial layers for four distinct frequency bands: Gamma, Beta, Alpha, and Theta.

### Visual Components & Color Coding
The plots utilize vertical bar graphs:

*   **Color Coding:** Blue bars represent power changes in the **predictable > unpredictable** blocks, while orange/red bars represent power changes in the **unpredictable > predictable** blocks.
*   **Significance Markers:** A red asterisk ($\text{*}$) placed above a bar indicates statistical significance ($P < 0.05$) for the indicated comparison (unpredictable > predictable blocks, as per the caption).

### Detailed Panel Descriptions

#### Top Section (LFP Power Comparison)
This section shows the percent change in LFP power from 0 to 100 Hz.

*   **Panel (A): Gamma (40-90 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Y-axis represents the magnitude of LFP power change (no explicit scale provided, but relative heights are visible).
    *   Data shows a significant increase (red bar with $\text{*}$) in V4 for the unpredictable > predictable comparison.
*   **Panel (B): Beta (15-30 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Data shows a significant increase (red bar with $\text{*}$) in 7A for the unpredictable > predictable comparison.
*   **Panel (C): Alpha (8-14 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Data shows a significant decrease (blue bar with $\text{*}$) in V4 for the predictable > unpredictable comparison.
*   **Panel (D): Theta (2-6 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Data shows a significant increase (red bar with $\text{*}$) in V4 for the unpredictable > predictable comparison.

*(Note: Panel E is not explicitly labeled with a frequency band in the visible portion, but it follows the pattern of A-D.)*

#### Bottom Section (Layer Comparison - Percent Change)
This section shows the percent change in LFP power for deep vs. superficial layers.

*   **Panel (F): Gamma band (40 to 90 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   The legend indicates that the blue bars represent **Deep** layers and the orange/red bars represent **Superficial** layers.
    *   Red asterisks denote significant differences between deep and superficial layers for the respective band/area.
*   **Panel (G): Beta band (15 to 30 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Blue bars = Deep; Orange/Red bars = Superficial.
*   **Panel (H): Alpha band (8 to 14 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Blue bars = Deep; Orange/Red bars = Superficial.
*   **Panel (I): Theta band (2 to 6 Hz)**
    *   X-axis labels: V4, 7A, PFC.
    *   Blue bars = Deep; Orange/Red bars = Superficial.

### Contextual Caption Integration
The caption clarifies the following:
*   **Data Source:** The data represents LFP power for unpredictable vs. predictable samples, measured as the percent change from 0 to 100 Hz during a 1-s sample processing interval.
*   **Averages:** Means are calculated across all available bipolar derivations of LFPs per area.
*   **Significance Key:** Red asterisks ($\text{*}$) denote significance ($P < 0.05$) for power in **unpredictable > predictable** blocks (in the top panels). Blue bars denote significance for power in **predictable > unpredictable** blocks.
*   **Layer Specifics (F-I):** Panels F through I specifically show the percent change in LFP power for **deep vs. superficial layers**.
*   **Sample Sizes:** The caption provides sample sizes ($N$) for the different comparisons (e.g., $N=564, 227,$ and $410$ for superficial layers in V4, 7A, and PFC, respectively).

> Figure caption (from PDF text): Fig. 3.
LFP power for unpredictable vs. predictable samples. (A–E) Unpredictable vs. predictable percent change in LFP power from 0 to 100 Hz during the 1-s
sample processing interval. Mean across all available bipolar derivations of LFPs per area (N = 1,483, 666, 650, 793, and 1,358 for V4, LIP, 7A, FEF, and PFC,
respectively), ±1 SEM across LFPs. Horizontal red bars denote significance at P < 0.05 for power in unpredictable > predictable blocks, blue bars for power in
predictable > unpredictable blocks (corrected for multiple comparisons). (F–I) Percent change in LFP power for unpredictable vs. predictable samples for deep
vs. superficial layers in different bands. (F) Gamma band (40 to 90 Hz), (G) beta band (15 to 30 Hz), (H) alpha band (8 to 14 Hz), (I) theta band (2 to 6 Hz).
Mean ± SEM across LFPs in superficial (N = 564, 227, and 410 for areas V4, 7A, and PFC) vs. deep layers (N = 586, 245, and 480 for areas V4, 7A, and PFC). Red
asterisk denotes significant (P < 0.05) differences.


### Overall Layout & Structure
The figure consists of five distinct line graphs stacked vertically, labeled A through E. Each panel plots a time-course measurement against the percentage change in LFP power, comparing unpredictable versus predictable conditions.

### Visual Components & Symbols
*   **Plots:** Each panel (A-E) contains a single continuous line graph.
*   **X-axis:** The horizontal axis in all panels represents time, ranging from 0 to 100 (presumably representing a percentage or normalized time scale).
*   **Y-axis:** The vertical axis in all panels represents the percent change in LFP power.
*   **Lines:** A single gray line traces the mean trend across the samples for each area.
*   **Significance Markers:**
    *   Horizontal **red bars** indicate periods where the power in unpredictable $>$ predictable blocks is significantly different ($P < 0.05$).
    *   Horizontal **blue bars** indicate periods where the power in predictable $>$ unpredictable blocks is significantly different ($P < 0.05$).

### Labels, Keys & Legends
**Panel Titles (Areas):**
*   A: V4
*   B: LIP
*   C: 7A
*   D: FEF
*   E: PFC

**Axis Labels (Inferred from Caption):**
*   The Y-axis represents the "Percent change in LFP power."
*   The X-axis represents time during the "1-s sample processing interval."

**Annotations (From Caption):**
*   The red bars denote significance for "unpredictable $>$ predictable blocks."
*   The blue bars denote significance for "predictable $>$ unpredictable blocks."

### Data Trends & Details (Panel by Panel)

**Panel A (V4):**
*   The gray line starts near 0% change and shows a slight initial dip before rising slightly.
*   A red bar spans approximately from $x=0$ to $x \approx 25$, indicating significant differences where unpredictable power is higher.
*   A blue bar spans approximately from $x=15$ to $x \approx 25$, indicating significant differences where predictable power is higher.

**Panel B (LIP):**
*   The gray line starts near 0% change and shows a slight initial decrease.
*   A red bar spans approximately from $x=35$ to $x \approx 70$, indicating significant differences where unpredictable power is higher.
*   A blue bar spans approximately from $x=10$ to $x \approx 25$, indicating significant differences where predictable power is higher.

**Panel C (7A):**
*   The gray line starts near 0% change, dips slightly below zero, and then rises.
*   A red bar spans approximately from $x=35$ to $x \approx 70$, indicating significant differences where unpredictable power is higher.
*   A blue bar spans approximately from $x=5$ to $x \approx 15$, indicating significant differences where predictable power is higher.

**Panel D (FEF):**
*   The gray line starts near 0% change, dips slightly below zero, and then remains relatively flat.
*   A red bar spans approximately from $x=0$ to $x \approx 15$, indicating significant differences where unpredictable power is higher.
*   A blue bar spans approximately from $x=5$ to $x \approx 15$, indicating significant differences where predictable power is higher.

**Panel E (PFC):**
*   The gray line starts near 0% change and shows a slight initial dip.
*   A red bar spans approximately from $x=45$ to $x \approx 70$, indicating significant differences where unpredictable power is higher.
*   A blue bar spans approximately from $x=10$ to $x \approx 25$, indicating significant differences where predictable power is higher.

### Contextual Caption Integration
The caption specifies that the data represents "LFP power for unpredictable vs. predictable samples" and is measured as the "percent change in LFP power from 0 to 100 Hz during the 1-s sample processing interval." The analysis is based on mean values across multiple bipolar derivations for each area (V4, LIP, 7A, FEF, PFC). The caption also notes that Panels F-I (not fully shown) detail layer-specific differences across different frequency bands ($\gamma$, $\beta$, $\alpha$, $\theta$).

31462
|
www.pnas.org/cgi/doi/10.1073/pnas.2014868117
Bastos et al.

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 5

We next analyzed the trial-by-trial power change in predict-
able blocks relative to the switch from an unpredictable block.
For this analysis, each trial’s power on predictable trials com-
pared to the average of all trials during an unpredictable block.
In the gamma band, responses to predictable samples gradually
reduced, reaching their minimum response at different trials in
different areas. This followed a hierarchical progression with V4
reaching its minimum earliest at trial 19 (reflecting 18 repeti-
tions), LIP at trial 35, 7A at trial 46, and both FEF and PFC at
trial 49 (SI Appendix, Fig. S7A). In the alpha and beta bands,
sample repetition caused power to increase. This plateaued after
a number of repetitions. There was no clear hierarchical pro-
gression, with different areas reaching their maximum alpha/beta
power in a wide variety of repetitions (range in areas LIP, 7A,
FEF, and PFC: trials 12 to 47, SI Appendix, Fig. S7B). These
increases in beta power and decreases in theta/gamma power
tracked the animals’ behavioral improvement within predictable
blocks (SI Appendix, Supplemental Results and Fig. S8).

Stimulus Specificity of Spiking and LFP Power Modulation. We next
investigated whether the effects of predictability were stimulus
specific. We tested whether the modulation of LFP power was
strongest at recording sites that preferred (showed higher spiking
to) the specific stimulus that is being predicted. We addressed
this in V4 because its spiking showed the strongest spiking se-
lectivity for the identity of the sample objects (SI Appendix, Fig.
S3A).

We first analyzed each V4 site’s MUA activity for sample object
specificity. For each V4 site, the sample that produced the highest
MUA activity was defined as the “preferred” sample. The sample
object that produced the least MUA activity was the “nonpreferred”
sample. We calculated differences in power during unpredictable vs.
predictable blocks for the preferred and nonpreferred samples
separately.

Power modulation was stimulus specific. It was higher for the
recording site’s preferred than nonpreferred sample object. Dur-
ing the sample interval, LFP gamma power and MUA modulation
(unpredictable > predictable) was greater to the preferred sample
in superficial cortical layers (P < 0.01, Wilcoxon rank sum test
comparing each site’s preferred vs. nonpreferred power modula-
tion) but not in deep layers (Fig. 4 A and B for LFP gamma and
Fig. 4 I and J for MUA). An ANOVA testing for interaction
between factors preference and layer on neural modulation by
predictability revealed a significant interaction for MUA (P < 0.05
for MUA, P = 0.056 for gamma). Alpha- and beta-power modu-
lation (predicted > unpredicted) was stronger to the preferred
object in deep cortical layers (Fig. 4 C and E, P < 0.05, Wilcoxon
rank sum test comparing each site’s preferred vs. nonpreferred
power modulation) but not superficial (Fig. 4 D and F, P > 0.05,
Wilcoxon rank sum test). Theta-power modulation (unpredict-
able > predictable) was significantly greater for preferred vs.
nonpreferred samples only in deep layers (P < 0.05, Wilcoxon
rank sum test comparing each site’s power modulation for pre-
ferred vs. nonpreferred sample objects, Fig. 4G). ANOVAs testing
for interactions between factors preference and layer on neural
modulation by predictability were not significant for theta, alpha,
or beta (P > 0.05). Similar selectivity effects on LFP power were
found in the presample interval (SI Appendix, Supplemental Results
and Fig. S4).

Network Interactions for Predictability. We first examined network
interactions using coherence analysis between LFPs recorded in
each pair of areas. During the sample interval, this confirmed
coherence networks involving theta and gamma for unpredict-
able samples and alpha and beta for predictable samples (SI
Appendix, Supplemental Results and Figs. S9 and S10, for pre-
sample coherence, see SI Appendix, Fig. S11). We next examined
the
direction
of
interactions
between
areas.
We
used

nonparametric Granger causality (GC), which separately mea-
sures the impact of area A to B vs. B to A at each frequency from
1 to 100 Hz (45). To assess feedforward vs. feedback flow, we
assumed the following cortical hierarchy (from lower to higher):
V4, LIP, 7A, FEF, and PFC (46). We first focused on the sample
interval. Fig. 5A shows the percentage of significantly modulated
connections (cluster-based randomization test, P < 0.05) for both
feedforward (solid lines) and feedback (dotted lines) directions
(modulation of Granger causality for all individual area pairs is
shown in SI Appendix, Fig. S12). The red line indicates unpre-
dictable > predictable GC while the blue line shows the opposite
(cluster-based randomization test, P < 0.05). Fig. 5 B and C show
the sums of modulated connections per area as a function of
whether connections into and out of the area were feedforward
or feedback, respectively.

Preferred
Non-Preferred

Unpred. vs. Pred. %Change

Deep layers, theta

Preferred
Non-Preferred
0

2

4

6

8

10

Unpred. vs. Pred. %Change

-3

-2

-1

0

Unpred. vs. Pred. %Change

Preferred
Non-Preferred
0

2

4

6

Unpred. vs. Pred. %Change

Deep layers, gamma

Preferred
Non-Preferred
0

2

4

6

Unpred. vs. Pred. %Change

0

Deep layers, MUA

0

0.01

0.02

MUA Diﬀerence

(Unpred. - Pred.)

0.01

0.02

A
B



**Overall Layout & Structure:**
The figure is structured vertically, consisting of four separate panels labeled B, D, F, and H. Each panel is a bar chart comparing two conditions: "Preferred" and "Non-Preferred."

**Visual Components & Symbols:**
Each panel contains two vertical blue bars representing the mean value for each condition. Error bars are present atop each bar, indicating variability (likely standard error or standard deviation).

**Labels, Keys & Legends:**
The panels are titled to specify the frequency band and cortical layer:
*   **Panel B:** "Superficial layers, gamma"
*   **Panel D:** "Superficial layers, beta"
*   **Panel F:** "Superficial layers, alpha"
*   **Panel H:** "Superficial layers, theta"

The x-axis labels for all panels are:
*   "Preferred"
*   "Non-Preferred"

The y-axis labels vary by panel, representing the measured activity level (though specific units are not provided on the axes).

**Data Trends & Details:**

*   **Panel B (Gamma):**
    *   The y-axis ranges from 0 to 6.
    *   The "Preferred" bar is significantly higher, reaching approximately 5.5. An asterisk (\*) is present above the "Non-Preferred" bar, suggesting a statistically significant difference between the two conditions.
    *   The "Non-Preferred" bar reaches approximately 3.8.

*   **Panel D (Beta):**
    *   The y-axis ranges from -3 to 0.
    *   Both bars are negative. The "Preferred" bar is slightly lower (more negative), around -2.3, with an error bar extending below -3.
    *   The "Non-Preferred" bar is slightly higher (less negative), around -1.5, with an error bar extending down to approximately -2.8.

*   **Panel F (Alpha):**
    *   The y-axis ranges from 0 to 4.
    *   Both bars are high and nearly equal in height, around 2.7 to 2.8. Both bars have visible error bars.

*   **Panel H (Theta):**
    *   The y-axis ranges from 0 to 10.
    *   The "Preferred" bar is the highest, reaching approximately 7.8. It has a visible error bar extending up to nearly 9.
    *   The "Non-Preferred" bar is lower, reaching approximately 4.5. It also has a visible error bar.



**Overall Layout & Structure:**
The figure is composed of four distinct panels, labeled A, C, E, and G (though the panel labels are not explicitly shown in sequence for all four plots provided, they correspond to different frequency bands). Each panel is a bar chart comparing two conditions: "Preferred" and "Non-Preferred."

**Visual Components & Symbols:**
Each panel contains two vertical blue bars representing the mean value for each condition. Error bars, represented by thin vertical lines extending above and below the top of the blue bars, indicate variability (likely standard error or standard deviation). Asterisks ($\text{*}$) are used as annotations above specific bars to denote statistical significance.

**Labels, Keys & Legends:**
The titles of the panels specify the frequency band being analyzed:
*   Top Panel Title: "Deep layers, gamma"
*   Second Panel Title: "Deep layers, beta"
*   Third Panel Title: "Deep layers, alpha"
*   Bottom Panel Title: "Deep layers, theta"

The x-axis labels for all plots are consistent: "Preferred" and "Non-Preferred."

The y-axis labels vary by panel, representing the measured value (likely a spectral power or similar metric):
*   Panel A (Gamma): Y-axis ranges from 0 to 6, with major ticks at intervals of 2.
*   Panel C (Beta): Y-axis ranges from -3 to 1, with major ticks at intervals of 1.
*   Panel E (Alpha): Y-axis ranges from -1 to 1, with major ticks at intervals of 0.5.
*   Panel G (Theta): Y-axis ranges from 0 to 10, with major ticks at intervals of 2.

**Data Trends & Details:**

*   **Panel A (Gamma):**
    *   The "Preferred" bar shows a mean value around 3.5, with an error bar extending roughly from 2 to 4.
    *   The "Non-Preferred" bar shows a mean value slightly lower, around 2.8, with an error bar extending roughly from 2 to 3.5.
    *   No asterisks are present in this panel.

*   **Panel C (Beta):**
    *   The "Preferred" bar shows a negative mean value, approximately -2.3, with an error bar extending roughly from -1 to -3.5. An asterisk ($\text{*}$) is placed above this bar, indicating significance.
    *   The "Non-Preferred" bar shows a small negative mean value, close to 0 (approximately -0.2), with an error bar extending roughly from -1 to 0.5. An asterisk ($\text{*}$) is placed above this bar, indicating significance.

*   **Panel E (Alpha):**
    *   The "Preferred" bar shows a negative mean value, approximately -0.6, with an error bar extending roughly from -1 to 0.
    *   The "Non-Preferred" bar shows a positive mean value, approximately 0.3, with an error bar extending roughly from -0.5 to 1. An asterisk ($\text{*}$) is placed above this bar, indicating significance.

*   **Panel G (Theta):**
    *   The "Preferred" bar shows a high positive mean value, approximately 6.5, with an error bar extending roughly from 4 to 8.
    *   The "Non-Preferred" bar shows a lower positive mean value, approximately 2.5, with an error bar extending roughly from 1 to 4. An asterisk ($\text{*}$) is placed above the "Non-Preferred" bar, indicating significance.

D

G
H

I
J

Deep layers, beta

Preferred
Non-Preferred
Preferred
Non-Preferred

C

0

1

2

3

4
Deep layers, alpha

-1

-0.5

0

0.5

1

Preferred
Non-Preferred
Preferred
Non-Preferred

E
F

Preferred
Non-Preferred
Preferred
Non-Preferred

MUA Diﬀerence

(Unpred. - Pred.)

-3

-2

-1

0

0

2

4

6

8

10

Unpred. vs. Pred. %Change

Unpred. vs. Pred. %Change

Unpred. vs. Pred. %Change

Fig. 4.
Pathway specificity of LFP power and MUA modulation. (A–H)
Unpredicted vs. predicted percent change in LFP power for the preferred
and nonpreferred stimulus. (A) Deep layers in the gamma band (40 to 90 Hz),
(B ) superficial layers in the gamma band, (C) deep layers in the beta band
(15 to 30 Hz), (D) superficial layers in the beta band, (E) deep layers in the
alpha band (8 to 14 Hz), (F) superficial layers in the alpha band, (G) deep
layers in the theta band (2 to 6 Hz), (H) superficial layers in the theta band. (I)
MUA modulation of deep cortical layers in area V4, unpredictable minus
predictable during the sample interval, (J) same as I, but for superficial lay-
ers. Mean ± SEM. Red asterisk denotes significant (P < 0.05) differences
between neural modulation of preferred vs. nonpreferred samples.

Bastos et al.
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31463

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 6

The strength and sign of modulation of GC by predictability
depended on frequency and directionality. In the feedforward
direction, unpredictable > predictable GC modulation peaked in
the gamma-frequency range (Fig. 5A, solid red lines). Although
the feedback direction was also positively modulated (Fig. 5A,
dotted red lines), the percentage of modulated connections was
lower than feedforward gamma (χ2 test for percentage of positive
modulation across the gamma band, 40 to 90 Hz, in the feed-
forward vs. feedback directions, 0.57 vs. 0.33, P < 1E-13). In the
theta band (2–6 Hz), an approximately equal percentage of both
feedforward and feedback connections had positive task modu-
lation (unpredicted > predicted GC).

Notably, virtually all directed functional connections with
greater GC during predictable than unpredictable samples were in
the alpha and beta bands (blue lines in Fig. 5A). And they were
mostly feedback connections. The percentage of feedback direc-
tion GC that was greater for predictable than unpredictable
samples was higher than those in feedforward direction for alpha
(χ2 test for percentage of negative modulation across the alpha
band, 8 to 14 Hz, in the feedforward vs. feedback directions, 0%
vs. 29%, P < 1E-5), beta (χ2 test for percentage of negative
modulation across the beta band, 15 to 30 Hz, in the feedforward
vs. feedback directions, 10% vs. 30%, P < 1E-5), and theta (χ2 test
for percentage of negative modulation across the theta band, 2 to
6 Hz, in the feedforward vs. feedback directions, 0% vs. 10%, P <
0.05). There was no predictable > unpredictable GC modulation
in the gamma band in either direction. In short, feedforward
functional connections were enhanced during unpredictable

samples, especially in the gamma range, whereas feedback func-
tional connections were enhanced during predictable samples with
a peak at alpha/beta frequencies.

To determine the layer specificity of these effects, we focused
on the two areas at the bottom and top of the hierarchy: V4 and
PFC. The rationale was that GC interactions from V4 to the
other areas are all feedforward, and interactions from PFC to the
other areas are all feedback. The modulation of these feedfor-
ward and feedback functional connections by layer is shown in
Fig. 5D (for V4) and Fig. 5E (for PFC) during the sample in-
terval, and for PFC during the presample interval in Fig. 5F.

During the sample interval, feedforward connections from V4
to the rest of the areas were greater during unpredictable sam-
ples. This modulation was greater in superficial layers than deep
layers in theta, alpha, beta, and gamma bands (Fig. 5D, Wilcoxon
rank sum test comparing modulations for all feedforward chan-
nel pairs in superficial vs. deep layers, P < 1E-3 for theta, P < 1E-
14 for alpha, P < 1E-8 for beta, and P < 1E-3 for gamma). By
contrast, in PFC feedback, GC was greater during predictable
samples, especially in the beta band (Fig. 5E). This effect was
stronger in superficial than deep layers (Fig. 5E, Wilcoxon rank
sum test comparing task modulations for all feedback channel
pairs in superficial vs. deep, P < 1E-16 for the beta band, not
significant for the alpha band). In the theta band, PFC feedback
GC in deep layers was significantly stronger during predictable
samples compared to superficial layers (Fig. 5E, Wilcoxon rank
sum test comparing task modulations for all feedback channel
pairs in superficial vs. deep, P < 1E-5 for the theta band).

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
Frequency (Hz)

0

10

20

30

40

50

60

70

80

Percentage of connections modulated

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
Frequency (Hz)

-15

-10

-5

0

5

10
PFC Feedback to rest (sample interval)

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
Frequency (Hz)

0

5

10

15

20

25

30

35

40
V4 Feedforward to rest (sample interval)

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
Frequency (Hz)

PFC Feedback to rest (pre-sample interval)

A
B
C

D
E
F

Unpred. > Pred.
Pred. > Unpred

Feedback
Feedforward
Unpred > Pred

Pred > Unpred

Deep
Deep

Feedback GC modulation

V4

LIP

7A

FEF

PFC

Feedforward GC modulation



This figure is a heatmap visualization titled "Feedforward GC modulation," displaying data across different cortical areas and frequency bands.

**1. Overall Layout & Structure:**
The figure is structured as a grid or matrix plot, where the vertical axis represents different cortical areas (layers/regions) and the horizontal axis represents frequency in Hertz ($\text{Hz}$). The visualization uses color intensity to represent a measured value, likely related to modulation strength or activity level.

**2. Visual Components & Symbols:**
*   **Grid Structure:** The plot is divided into rows corresponding to the cortical areas and columns corresponding to frequency bins.
*   **Color Coding:** The primary visual element is the color filling each cell of the grid. A legend on the right side maps these colors to a quantitative scale, labeled "Unpr" (likely representing Unprojected or Unmodulated activity).
*   **Color Scale:** The color scale ranges from dark blue/purple (low values, near 0) through greens and yellows to bright yellow/orange (high values, up to 4).

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Feedforward GC modulation."
*   **Y-Axis Labels (Cortical Areas):** The vertical axis lists several abbreviations, likely representing different cortical areas or layers:
    *   V4
    *   LIP
    *   7A
    *   EF
    *   PFC
*   **X-Axis Label:** The horizontal axis is labeled "Frequency ($\text{Hz}$)," ranging from 0 to 100.
*   **Legend:** A vertical color bar on the right side serves as the legend, labeled "Unpr," with numerical ticks indicating values: 0, 2, and 4.

**4. Data Trends & Details:**
The heatmap displays distinct patterns across the frequency spectrum for each cortical area:

*   **V4:** Shows high activity (bright yellow/orange) across most frequencies, particularly strong in the 30-80 $\text{Hz}$ range.
*   **LIP:** Exhibits a mix of colors, with significant yellow/orange patches around 40-60 $\text{Hz}$ and some blue areas at lower frequencies.
*   **7A:** Shows a broad distribution, with notable green and blue areas across the spectrum.
*   **EF:** Displays a prominent dark purple/blue patch centered around 30-40 $\text{Hz}$, indicating a low value in that specific frequency band, surrounded by orange/yellow activity.
*   **PFC:** Shows a generally greener profile compared to V4, with some localized yellow patches.

**5. Contextual Caption Integration:**
The labels (V4, LIP, 7A, EF, PFC) identify specific brain regions or functional areas being analyzed for their modulation characteristics across different frequency bands. The legend "Unpr" indicates that the color intensity quantifies a specific metric related to unprojected modulation within these regions.



This figure presents a visualization titled "Feedback GC modulation," structured as a 2D heatmap or matrix plot.

**1. Overall Layout & Structure:**
The figure is a single, large grid-like visualization where the horizontal axis represents frequency and the vertical axis represents different states or conditions. The plot uses color intensity to encode data across these two dimensions, functioning as a spectral representation or modulation map.

**2. Visual Components & Symbols:**
*   **Axes:** The horizontal axis (x-axis) is labeled "Frequency (Hz)" and ranges from 0 to 100, marked with increments every 10 units (e.g., 10, 20, ..., 100). The vertical axis (y-axis) is segmented into distinct regions labeled "Pred" and "Unpred," suggesting different predictive states.
*   **Color Coding:** A color bar/legend is present on the right side of the plot, indicating a continuous scale. This legend ranges from dark blue/purple (at the bottom) through various shades of green, yellow, and bright red/orange (at the top). The color scale appears to represent a quantitative measure of modulation strength or activity.
*   **Data Representation:** The main body of the plot is filled with colored rectangular blocks, representing the modulation across specific frequency bands for each state.

**3. Labels, Keys & Legends:**
*   **Title:** "Feedback GC modulation"
*   **X-Axis Label:** "Frequency (Hz)"
*   **Y-Axis Labels:** The vertical axis is divided into sections. At the top, there is a label "Pred," and at the bottom, there is another section labeled "Pred." In between these two main sections, there are labels indicating the structure being modulated: "connections."
*   **Color Legend:** A vertical color bar is present on the right side. While specific numerical values are not provided, it shows a gradient transitioning from dark blue/purple $\rightarrow$ green $\rightarrow$ yellow $\rightarrow$ orange.

**4. Data Trends & Details:**
The plot displays distinct patterns of color across the frequency spectrum for different states:

*   **Top "Pred" Region:** Shows patches of high modulation (yellow/orange) concentrated in the lower frequency range (around 10-30 Hz), interspersed with areas of moderate modulation.
*   **Middle "connections" Region:** This area shows a complex pattern. There are prominent vertical bands of color, particularly around 20-30 Hz and 60-70 Hz.
*   **Bottom "Pred" Region:** This region exhibits strong, broad bands of modulation, notably a deep blue/purple area spanning from approximately 20 Hz to 50 Hz.

**5. Contextual Caption Integration:**
The labels "Pred" and "Unpred" (though only "Pred" is clearly visible in the top section, implying a counterpart exists) suggest that the modulation patterns are being compared between predictive and non-predictive states. The label "connections" likely refers to the specific neural pathways or synaptic connections whose modulation is being analyzed in response to feedback.



**1. Overall Layout & Structure:**
The figure consists of a single plot area with labeled axes, presenting multiple overlaid line graphs.

**2. Visual Components & Symbols:**
*   **Axes:** The horizontal axis (x-axis) represents **Frequency (Hz)**, ranging from 0 to 100 Hz. The vertical axis (y-axis) represents an unspecified magnitude, ranging from 0 to 80.
*   **Lines/Curves:** There are four distinct data series represented by different line styles and colors:
    *   **Solid Red Line:** Represents the condition "Pred. > Unpred." (Prediction greater than Unpredicted).
    *   **Dashed Red Line:** Represents the condition "Unpred. > Pred." (Unpredicted greater than Prediction).
    *   **Solid Black Line:** Represents the "Feedforward" pathway.
    *   **Dotted Black Line:** Represents the "Feedback" pathway.

**3. Labels, Keys & Legends:**
*   **Legend/Key:** The top-left corner contains a legend defining the line styles:
    *   "Pred. > Unpred" (associated with red lines)
    *   "Unpred. > Pred." (associated with red lines)
    *   "Feedforward" (associated with solid black line)
    *   "Feedback" (associated with dotted black line)
*   **Axis Labels:** The x-axis is labeled "Frequency (Hz)". The y-axis has no explicit label provided in the visible portion of the image, but numerical ticks range from 0 to 80.

**4. Data Trends & Details:**
The plot shows distinct frequency-dependent responses for the four conditions:

*   **Pred. > Unpred (Solid Red Line):** This curve shows a strong peak around 60-70 Hz, reaching a maximum value near 75. It starts low, rises sharply around 40 Hz, peaks high, and then drops off but remains elevated compared to the other lines at higher frequencies.
*   **Unpred. > Pred. (Dashed Red Line):** This curve shows a broader, lower response compared to the solid red line. It has noticeable peaks around 20 Hz and again near 70-80 Hz, with values generally below 50.
*   **Feedforward (Solid Black Line):** This line is very low across most frequencies, showing a small peak around 15-20 Hz (reaching approximately 10) and remaining near zero otherwise.
*   **Feedback (Dotted Black Line):** This line shows a moderate response, peaking around 30 Hz at a value near 20. It also shows some activity in the mid-frequency range, though generally lower than the red lines.

**5. Contextual Caption Integration:**
No external caption text was provided, so no specific contextual interpretation beyond the labels is possible. The figure visually compares frequency-domain characteristics (likely power spectral density or transfer function magnitude) under different predictive coding conditions ("Pred. > Unpred" vs. "Unpred. > Pred.") and pathway types ("Feedforward" vs. "Feedback").

-2

0

2

4

Num of mod.

connections

10
20
30
40
50
60
70
80
90 100
Frequency (Hz)

10
20
30
40
50
60
70
80
90 100
Frequency (Hz)

Unpred > Pred

Pred > Unpred

-2

0

2

4

Num of mod.

connections

Deep

-15

-10

-5

0

5

10

Fig. 5.
Granger causal networks for unpredicted vs. predicted samples. (A) Percentage of interareal functional connections with significant (P < 0.05, cor-
rected for multiple comparisons) task modulation (red lines: unpredictable > predictable; blue lines: unpredictable < predictable), separately for feedforward
(solid lines) and feedback (dotted lines). (B) Number of feedforward functional connections into and out of each area that are modulated as a function of
frequency (yellow colors represent number of functional connections with more unpredictable > predictable Granger causality; blue lines represent number
of functional connections with more unpredictable < predictable Granger causality). (C) Same as B, but for feedback Granger causality. (D) Granger causal
z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial
(red lines) vs. deep (blue lines). Mean ± SEM. (E) Granger causal z-score difference, unpredictable minus predictable, from PFC to other areas (feedback
functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean ± SEM. (F) same as E, but for the presample interval.

> Figure caption (from PDF text): Fig. 5.
Granger causal networks for unpredicted vs. predicted samples. (A) Percentage of interareal functional connections with significant (P < 0.05, cor-
rected for multiple comparisons) task modulation (red lines: unpredictable > predictable; blue lines: unpredictable < predictable), separately for feedforward
(solid lines) and feedback (dotted lines). (B) Number of feedforward functional connections into and out of each area that are modulated as a function of
frequency (yellow colors represent number of functional connections with more unpredictable > predictable Granger causality; blue lines represent number
of functional connections with more unpredictable < predictable Granger causality). (C) Same as B, but for feedback Granger causality. (D) Granger causal
z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial
(red lines) vs. deep (blue lines). Mean ± SEM. (E) Granger causal z-score difference, unpredictable minus predictable, from PFC to other areas (feedback
functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean ± SEM. (F) same as E, but for the presample interval.


### Detailed Figure Description (Focusing on Panel D)

**1. Overall Layout & Structure:**
The visible portion of the figure displays a line graph, specifically Panel (D), which is part of a larger multi-panel figure (Figure 5). The graph plots data across a frequency range on the x-axis against a quantitative measure (likely a z-score difference) on the y-axis.

**2. Visual Components & Symbols:**
*   **Lines:** There are two primary sets of lines plotted: red and blue. These lines represent different conditions being compared across the frequency spectrum.
*   **Shading/Error Bars:** The lines are accompanied by shaded areas, indicating variability (likely Standard Error of the Mean, as suggested by the caption).
*   **Annotations:** A prominent arrow points towards the red line, labeled "Superficial," and another arrow points towards the blue line, labeled "Deep."

**3. Labels, Keys & Legends:**
*   **X-Axis Label:** The horizontal axis is labeled with frequency units, indicated as "f (Hz)" (though the full label is partially cut off, the context suggests frequency). The visible range spans from approximately 5 Hz up to 100 Hz.
*   **Y-Axis Label:** The vertical axis is not fully labeled in the visible snippet, but based on the caption context (Panel D), it represents "Granger causal z-score difference, unpredictable minus predictable."
*   **Annotations:**
    *   "Superficial" is pointed to by a red arrow.
    *   "Deep" is pointed to by a blue arrow.

**4. Data Trends & Details (Panel D):**
*   **Red Line (Superficial):** The red line shows a distinct peak in the lower frequency range, reaching a maximum value near 35 on the y-axis around 10–20 Hz. Following this peak, the values decrease but remain relatively high compared to the blue line in certain frequency bands.
*   **Blue Line (Deep):** The blue line generally exhibits lower values than the red line, particularly in the low-frequency range. It shows a less pronounced peak compared to the red line and generally tracks below it across much of the spectrum.
*   **Comparison:** The graph visually compares the magnitude of the Granger causal z-score difference (Unpredictable minus Predictable) between superficial and deep layers across different frequencies.

**5. Contextual Caption Integration:**
The caption identifies Panel (D) as: "Granger causal z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean $\pm$ SEM." This confirms that the red and blue lines represent superficial and deep layers, respectively, and the data reflects feedforward connections originating from V4.

> Figure caption (from PDF text): Fig. 5.
Granger causal networks for unpredicted vs. predicted samples. (A) Percentage of interareal functional connections with significant (P < 0.05, cor-
rected for multiple comparisons) task modulation (red lines: unpredictable > predictable; blue lines: unpredictable < predictable), separately for feedforward
(solid lines) and feedback (dotted lines). (B) Number of feedforward functional connections into and out of each area that are modulated as a function of
frequency (yellow colors represent number of functional connections with more unpredictable > predictable Granger causality; blue lines represent number
of functional connections with more unpredictable < predictable Granger causality). (C) Same as B, but for feedback Granger causality. (D) Granger causal
z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial
(red lines) vs. deep (blue lines). Mean ± SEM. (E) Granger causal z-score difference, unpredictable minus predictable, from PFC to other areas (feedback
functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean ± SEM. (F) same as E, but for the presample interval.


**1. Overall Layout & Structure:**
The figure is a line graph plotting a quantitative measure against frequency, presented as mean $\pm$ SEM (Standard Error of the Mean). The plot is divided into two distinct data series, differentiated by color and labeled with directional arrows.

**2. Visual Components & Symbols:**
*   **X-axis:** Represents frequency, labeled in Hertz (Hz). The visible range spans from approximately 5 Hz to 100 Hz.
*   **Y-axis:** Represents the "Granger causal z-score difference, unpredictable minus predictable." The scale ranges from approximately -15 to +6.
*   **Lines:** Two primary sets of lines are plotted:
    *   **Red Lines (Superficial):** These represent data related to "superficial" connections.
    *   **Blue Lines (Deep):** These represent data related to "deep" connections.
    *   Each color appears to have multiple lines, suggesting the presence of different conditions or iterations (though only one representative line is clearly labeled for each category).
*   **Annotations:** Two large, colored arrows point to specific regions of the plot:
    *   A red arrow points toward the upper region of the graph, labeled "Superficial."
    *   A blue arrow points toward the lower region of the graph, labeled "Deep."

**3. Labels, Keys & Legends:**
*   **Y-axis Label:** "Granger causal z-score difference, unpredictable minus predictable."
*   **X-axis Label:** "Frequency (Hz)."
*   **Annotations/Labels within the plot area:** "Superficial" (associated with red lines) and "Deep" (associated with blue lines).

**4. Data Trends & Details:**
*   **Superficial (Red Lines):** The red lines show a complex, fluctuating trend across the frequency spectrum. They exhibit peaks around 15-20 Hz and again around 35-45 Hz, with values generally fluctuating between -1 and +6.
*   **Deep (Blue Lines):** The blue lines show a generally lower trend compared to the superficial data. They start around -8 at low frequencies, dip significantly below -12 around 25-30 Hz, and then gradually rise toward the baseline (around -4 to -6) as frequency increases towards 100 Hz.
*   **Baseline Reference:** A dashed horizontal line is present at $y = -5$, which serves as a visual reference point.

**5. Contextual Caption Integration:**
Based on the caption, this plot (Panel D) specifically shows: "Granger causal z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean $\pm$ SEM." This confirms that the data represents feedforward connections originating from V4.

> Figure caption (from PDF text): Fig. 5.
Granger causal networks for unpredicted vs. predicted samples. (A) Percentage of interareal functional connections with significant (P < 0.05, cor-
rected for multiple comparisons) task modulation (red lines: unpredictable > predictable; blue lines: unpredictable < predictable), separately for feedforward
(solid lines) and feedback (dotted lines). (B) Number of feedforward functional connections into and out of each area that are modulated as a function of
frequency (yellow colors represent number of functional connections with more unpredictable > predictable Granger causality; blue lines represent number
of functional connections with more unpredictable < predictable Granger causality). (C) Same as B, but for feedback Granger causality. (D) Granger causal
z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial
(red lines) vs. deep (blue lines). Mean ± SEM. (E) Granger causal z-score difference, unpredictable minus predictable, from PFC to other areas (feedback
functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean ± SEM. (F) same as E, but for the presample interval.


**1. Overall Layout & Structure:**
The figure is a line graph plotting a quantitative measure against an unspecified variable on the x-axis. The plot features two distinct sets of lines, color-coded and labeled to represent different conditions: "Superficial" (red) and "Deep" (blue). The data is presented as mean values with associated standard error of the mean ($\pm$ SEM), indicated by shaded areas surrounding the lines.

**2. Visual Components & Symbols:**
*   **X-axis:** The horizontal axis ranges from approximately 0 to 100, though specific tick marks are not fully visible in the cropped view.
*   **Y-axis:** The vertical axis represents a quantitative measure, labeled with numerical values ranging from -15 to 5.
*   **Lines and Shading:**
    *   **Red Lines/Shading (Superficial):** Represents data for the "Superficial" condition. The line itself is visible, and it is surrounded by a red shaded area indicating variability (SEM).
    *   **Blue Lines/Shading (Deep):** Represents data for the "Deep" condition. This line is also surrounded by a blue shaded area indicating variability (SEM).
*   **Annotations:** There are two explicit text annotations pointing to the respective curves: "Superficial" points toward the upper red curve, and "Deep" points toward the lower blue curve.
*   **Reference Line:** A horizontal dashed line is present across the plot at $y=0$, serving as a baseline reference.

**3. Labels, Keys & Legends:**
*   **Y-axis Label (Partial):** The y-axis is labeled with numerical values, and the caption identifies this plot as showing "Granger causal z-score difference, unpredictable minus predictable."
*   **X-axis Label (Partial):** The x-axis represents a variable related to the "sample interval."
*   **Annotations:** "Superficial" and "Deep" are used as labels pointing to the data sets.

**4. Data Trends & Details:**
*   **Superficial (Red):** The red line starts near $y=5$ at the left edge of the plot. It rapidly decreases, reaching a minimum value around $y=-15$ near the x-axis position of 20. Following this trough, it rises sharply, crossing $y=0$ around the x-position of 45, and then fluctuates slightly above and below $y=0$ before settling around $y=0$ by the right edge of the plot.
*   **Deep (Blue):** The blue line starts near $y=-5$ at the left edge. It decreases more gradually than the superficial curve, reaching a minimum value around $y=-10$ near the x-position of 35. It then rises, crossing $y=0$ around the x-position of 60, and generally remains close to or slightly below $y=0$ for the remainder of the plot.
*   **Comparison:** The superficial condition exhibits a much larger magnitude swing (from $\approx 5$ down to $\approx -15$) compared to the deep condition, which remains more constrained between approximately $-10$ and $2$.

**5. Contextual Caption Integration:**
The caption identifies this specific plot as **Fig. 5 (D)**: "Granger causal z-score difference, unpredictable minus predictable, from V4 to other areas (feedforward functional connections) during the sample interval for superficial (red lines) vs. deep (blue lines). Mean $\pm$ SEM." This confirms that the plot displays the difference in Granger causality scores (Unpredictable minus Predictable) for feedforward connections originating from V4, comparing superficial versus deep processing states during the sample interval.

31464
|
www.pnas.org/cgi/doi/10.1073/pnas.2014868117
Bastos et al.

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 7

During the presample interval, PFC feedback was different
depending on whether it arose from superficial vs. deep layers.
Superficial-layer PFC feedback was greater during unpredictable
blocks but deep-layer PFC feedback was greater during pre-
dictable blocks (Fig. 5F). The differences between layers was
significant for theta, alpha, and beta (Fig. 5F, Wilcoxon rank sum
test comparing modulations for all feedback channel pairs in
superficial vs. deep layers, P < 0.01 for the theta band, P < 1E-7
for the alpha and beta bands).

Higher Order Cortex Modulates Spiking and Gamma in V4. Finally,
we analyzed whether oscillations in higher-order areas (LIP, 7A,
FEF, and PFC) couple to, and potentially inhibit, spiking and
gamma in area V4. We used a general linear modeling (GLM)
framework (see Experimental Procedures) to test whether MUA
and gamma in V4 could be explained by power in higher-order
cortex. We performed this GLM with laminar-resolved regres-
sors in PFC and 7A. We attempted to explain trial-by-trial var-
iance in superficial and deep layers of V4. Higher-order cortex
inhibition of V4 would be reflected in a regression coefficient
with a negative sign.

MUA in deep layers of V4 was negatively coupled to theta in
superficial and deep layers of 7A, alpha in LIP and deep layers of
PFC, and beta in LIP, FEF, and superficial layers of PFC (SI
Appendix, Fig. S13, sign test for average regression coefficient
across sessions, P < 0.05 for all comparisons). MUA in superficial
layers of V4 was not significantly coupled to trial-by-trial varia-
tions in higher-order cortex power. Gamma in deep layers of V4
was negatively coupled to beta in superficial and deep layers of
PFC and alpha in superficial layers of PFC. In addition to these
negative regression coefficients, we also found positive coeffi-
cients. Beta in superficial and deep layers of area 7A positively
coupled to gamma in superficial and deep layers of V4 (SI Ap-
pendix, Fig. S13C, sign test for average regression coefficient
across all available sessions, P < 0.05). Gamma in all areas except
LIP positively coupled to V4 gamma (SI Appendix, Fig. S13D, sign
test for average regression coefficient across all available sessions,
all comparisons, P < 0.05).

Discussion
Our results show differences in oscillatory dynamics between
cortical layers as animals switch between two different modes of
processing. In the “bottom-up” mode, a new sensory input had to
be processed on every trial. In the other, “top-down” mode the
same stimulus was used on every trial and thus there was no need
to fully process new bottom-up inputs. In bottom-up mode,
gamma power and feedforward Granger causality predominated.
By contrast, in top-down mode, alpha/beta power and feedback
Granger causality predominated.

This could be due to a variety of processes that differ between
the two modes. One is habituation/adaptation due to stimulus
repetition. To examine this, we measured effects as a function of
the time between repetitions of the same sample object. This
revealed that short-term adaptation alone did not explain the
results. Longer-term stimulus repetition could have contributed.
Passive adaptation effects tend to reach their maximum after just
a single repetition (47). In our study repetition effects took
dozens of trials to reach their maximum and correlated with the
behavioral time course of improvement. This suggests that the
animals were exploiting the increasing familiarity due to repeti-
tion. This is not surprising. Repetition is a foundation of pre-
dictability. Most, if not all, forms of prediction likely depend on
repetition whether the repetition was from past experience or
generated in the recent past (seconds to minutes).

In addition, the neurophysiological signatures of prediction
and passive stimulus repetition are divergent. In previous studies
where stimulus repetition was not behaviorally relevant, gamma-
band power and synchronization in visual cortex increased with

repetition, whereas we observed decreases (48, 49). In our study,
repetition was used by the animals to perform the task. Here, we
have used repetition as an initial tool to elicit predictions and
top-down processing. In future paradigms, we will test more
cognitive forms of prediction, such as learned associations.

In bottom-up mode, new inputs needed to be fully attended,
processed, and temporarily held in working memory. In top-
down mode, less attention could be paid to the repeating stim-
ulus; it could be stored in and recalled from long-term memory.
Such differences can be captured under the umbrella of pre-
dictive coding theory.

Relation to Predictive Coding Models. Many predictive coding
models share common elements. Prediction (PD) units antici-
pate forthcoming sensory inputs. They inhibit prediction error
(PE) units when inputs match predictions. A mismatch due to an
unpredictable input disinhibits the PE units. They feedforward
the unpredicted input which updates the internal models that
generate the predictions. Models differ on the details of the
implementation in the brain. Some models (50) propose that
prediction error signals act locally in each cortical area to update
models. Predictions flow between areas in both feedforward and
feedback directions. Other models (12, 14) instead suggest that
predictions come from higher cortical areas that act on lower
cortical (sensory) areas to gate the feeding forward of prediction
errors. Of special note, many current models of predictive coding
emphasize that prediction errors can be modulated by precision
weighting, for example, by increasing attention or sensory evi-
dence (12, 51, 52). Here, we have used a task that did not set out
to explicitly modulate the precision of sensory samples in the
unpredicted vs. predicted blocks. Sensory samples were always
presented at full contrast; and in both block types, monkeys were
required to attend to the samples in order to perform an at-
tentional search. Therefore, we did not explicitly consider the
issue of precision weighting of prediction errors.

A distinct class of models goes further in proposing a neuro-
physiological
implementation
involving
distinct
oscillations.
“Rhythm-based” models suggest that superficial cortical layers
(layers 2 and 3) feedforward prediction errors using gamma.
Deep-layer cortex (layers 5 and 6) feedback predictions using
alpha/beta (1, 19). Our results are more consistent with the
rhythm-based models. We showed differences between areas,
with higher areas contributing more to prediction, and rhythmic-
and laminar-based differences between areas. Below, we sum-
marize and discuss these effects.

The Contribution of Cortical Rhythms to Predictive Processing. Al-
pha/beta and gamma have properties that suggest a general role
in gating and control. They are common and anticorrelated
across cortex. Gamma power is high during sensory inputs; al-
pha/beta power is high when they are ignored. In visual cortex,
gamma power is high and alpha low during sensory stimulation.
When a stimulus needs to be filtered or ignored, gamma power is
low and alpha is high (43, 53–55). Further, alpha/beta oscillations
in deep cortical layers are anticorrelated with superficial-layer
gamma associated with spiking carrying sensory inputs (26, 27).
The balance between alpha/beta and gamma reflect the encod-
ing, maintenance, and read-out of working memory (56). The
general idea is that top-down signals are fed back through alpha/
beta in deep cortical layers. They inhibit and thus gate the ex-
pression of gamma in superficial layers that help feed forward
and maintain the spiking carrying sensory inputs.

Extrapolating from the rhythm-based models of predictive
coding (1, 19), this suggests a framework we call predictive routing
(PR) (Fig. 6). In PR, there are not specialized circuits that com-
pute prediction errors and send them feedforward. Rather, PR
uses the same cortical circuitry used for other functions (sensory
processing, attention, maintenance/control of working memory,

Bastos et al.
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31465

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 8

etc.). Predictions act by alpha/beta preparation that actively inhibit
the specific pathways in sensory cortex that would process the
predicted input. As a result, there is less gamma and spiking to
predicted inputs (and less feedforward output as a result). In other
words, prediction errors do not result from a comparison between
predictions and inputs via a specialized circuit. They result from
the feed-forward passing of unexpected inputs because their
pathways have not been prepared (functionally inhibited).

This does not mean that alpha/beta (or gamma) have the exact
same roles all over cortex. For example, in prefrontal cortex, beta
has been modeled as an inhibitory–excitatory network but with
slower time constants than what would produce a gamma (57).
By contrast, modeling suggests that in parietal cortex, there is a
distinction between beta-1 (14 to 20 Hz) and beta-2 (24 to 30 Hz)
(58) and that parietal beta-1 may act as a memory buffer acti-
vated by strong cortical inputs that feeds forward violations to
the PFC (59). Indeed, we found in this study, that in parietal
cortex (area 7A) beta was unique and beta was functionally ex-
citatory (positively correlated with violations and local spiking)
unlike the other areas. Below, we elaborate on how our results
support different models of predictive coding.

Theta-band coherence and Granger causal interactions were
stronger during unpredictable stimuli in the sample interval.
These interactions were strongest between superficial layers of
V4 and the other members of the network. Theta-band inter-
actions were not previously proposed as candidates for pro-
cessing unpredictable stimuli. However, theta is well known to be
a slow rhythm in which faster rhythms such as gamma, can nest
(60–62) and aid long-range communication (63). In addition, a
previous study identified theta as a carrier for feedforward in-
teractions in the visual system (30). In predictive routing, what-
ever mechanisms are already in place for feedforward processing
are enhanced during unpredictable processing. Therefore, it
makes sense that theta (and gamma) from V4 to higher-order
cortex is enhanced during unpredicted stimuli, because this re-
flects an up-regulation of the feedforward channel.

Unpredicted Stimuli Enhance Spiking in Superficial Layers. At each
level of the cortical hierarchy tested, neurons spiked more to,
and carried more information about, unpredictable compared to
predicted stimuli. Neurons in superficial cortical layers (L2/3) of
V4 showed stronger effects than deep layers. In addition, only
superficial layers had unpredicted spiking selective to the pre-
dicted stimulus. Superficial layers 2/3 contain the majority of
feedforward projecting cells. This laminar specificity suggests
that unpredicted inputs are preferentially processed in superfi-
cial layers and fed forward.

Spiking Reflects an Upcoming Predictable Stimulus. We found that
during trial blocks in which the monkeys could predict the up-
coming stimulus, all cortical areas we recorded carried infor-
mation about it before it appeared. PFC contained the most
prestimulus information. In addition, we found that deep layers
held more information about the upcoming sample than super-
ficial layers. This is consistent with hierarchical models that
propose that generating predictions is primarily a function of
higher than sensory cortex and deep layers.

Modulation of Rhythms by Prediction Are Layer Dependent. In all
areas studied, unpredictable stimuli evoked more gamma (40 to
90 Hz) power and less alpha/beta (8 to 30 Hz) power compared
to predictable stimuli (beta in area 7A was an exception). These
effects were strongest in the first few trials when transitioning
from a predictable block to an unpredictable block, potentially
reflecting a violation, or prediction error. This effect and the
positive correlation between gamma and spiking (SI Appendix,
Fig. S2) were stronger in superficial than deep cortical layers.
There was generally more alpha/beta power to predictable than
unpredictable stimuli but layer differences varied by area. This
generally supports rhythm-based models positing that gamma
transmits prediction errors and alpha/beta transmits predictions.

Modulation of Rhythms by Prediction Are Stimulus Specific. The in-
creases in gamma power (and spiking) with unpredicted stimuli
and the increased alpha/beta with predicted stimuli were stim-
ulus specific. Effects were larger at recoding sites where spiking
preferred (was greater to) the specific stimulus that was pre-
dicted. For spiking, this selectivity occurred only in superficial
layers. For gamma, this selectivity was only significant in super-
ficial layers, and for alpha and beta, this selectivity was only
significant in deep layers. Therefore, rhythmic modulation of
power by predictability is stimulus specific. This supports the
view that oscillations can be modulated in a representationally
specific way (64), rather than only in a nonspecific way across
wide areas of cortex. The specificity is a central feature of pre-
dictive routing, where alpha/beta inhibits the pathways that
process the specific predicted stimulus and the increased gamma/
spiking occurs because the pathways processing other stimuli
were not inhibited.

Fig. 6.
Predictive routing model. Arrows and connections represent func-
tional (not anatomical) connections between areas/layers. Thick lines rep-
resent effective connections with increased influence; thin lines represent
effective connections with decreased influence. The Upper boxes represent
superficial layers (1 to 4) and the Lower boxes represent deep layers (5/6).
(Left subpanel) Sensory cortex is dynamically prepared to process its pre-
ferred stimulus, stimulus A, by feedback which inhibits MUA and enhances
alpha/beta in deep layers. Enhanced deep-layer alpha/beta functionally in-
hibits superficial-layer processing of stimulus A by reducing spiking and
gamma, reducing feedforward outputs. (Right subpanel) When a strong
prediction for stimulus B is present and stimulus A is presented (as in the first
few trials of an unpredictable block after a predictable block where “B” was
the repeated/predicted sample), there is less feedback alpha/beta inhibition
to the A column. Deep-layer to superficial-layer inhibition is weak or absent.
The A column is more excitable and responds to stimulus A with more
gamma/spiking and enhanced feedforward output from superficial layers (a
prediction error). Although we hypothesize this mechanism occurs at the
level of cortical columns, it could apply to any pathway that processes the
specific predicted stimulus. We also hypothesize that this mechanism can be
graded to reflect varying strengths of prediction.

> Figure caption (from PDF text): Fig. 6.
Predictive routing model. Arrows and connections represent func-
tional (not anatomical) connections between areas/layers. Thick lines rep-
resent effective connections with increased influence; thin lines represent
effective connections with decreased influence. The Upper boxes represent
superficial layers (1 to 4) and the Lower boxes represent deep layers (5/6).
(Left subpanel) Sensory cortex is dynamically prepared to process its pre-
ferred stimulus, stimulus A, by feedback which inhibits MUA and enhances
alpha/beta in deep layers. Enhanced deep-layer alpha/beta functionally in-
hibits superficial-layer processing of stimulus A by reducing spiking and
gamma, reducing feedforward outputs. (Right subpanel) When a strong
prediction for stimulus B is present and stimulus A is presented (as in the first
few trials of an unpredictable block after a predictable block where “B” was
the repeated/predicted sample), there is less feedback alpha/beta inhibition
to the A column. Deep-layer to superficial-layer inhibition is weak or absent.
The A column is more excitable and responds to stimulus A with more
gamma/spiking and enhanced feedforward output from superficial layers (a
prediction error). Although we hypothesize this mechanism occurs at the
level of cortical columns, it could apply to any pathway that processes the
specific predicted stimulus. We also hypothesize that this mechanism can be
graded to reflect varying strengths of prediction.


### 1. Overall Layout & Structure
The figure is organized vertically into two main functional layers: a **Superficial** layer and a **Deep** layer. The structure is divided into two conceptual subpanels (Left and Right), although the provided image snippet primarily shows a generalized structure that is referenced by the caption as representing two scenarios. The diagram uses rectangular boxes to represent functional areas or layers and arrows/lines to denote functional connections between them.

### 2. Visual Components & Symbols
**Nodes (Boxes):**
*   **Superficial Layer Box:** Labeled "A Column" and containing the text "Gamma Spiking." This represents the superficial cortical processing area.
*   **Deep Layer Box:** Labeled "Alpha/beta" and representing the deep cortical processing area.

**Connections (Arrows and Lines):**
*   **Feedback Loops:** There are connections flowing from the superficial layer back to itself (indicated by feedback loops involving stimuli A and B).
*   **Inter-Layer Connections:** Arrows connect the Superficial layer box to the Deep layer box, and vice versa.
*   **Line Thickness/Style:** The caption specifies that **thick lines represent effective connections with increased influence**, while **thin lines represent effective connections with decreased influence**.

**Stimulus/Input Representation:**
*   At the top, there are representations of stimuli: "Fe" (likely referring to a feature or stimulus) associated with the superficial layer, and another representation involving stimuli A and B near the top boundary.
*   The connections related to stimulus A show a blue wavy line and a red jagged line, suggesting different types of input or modulation related to stimulus A.

**Directionality:**
*   Arrows indicate the direction of functional influence or flow between layers/components.

### 3. Labels, Keys & Legends
**Layer Designations:**
*   The top section is labeled **"Superficial."**
*   The bottom section is labeled **"Deep."**

**Internal Labels:**
*   Inside the Superficial box: "A Column," "Gamma Spiking."
*   Inside the Deep box: "Alpha/beta."

**External Annotations (Arrows):**
*   A downward-pointing arrow next to the Superficial box indicates a decrease or reduction in activity (associated with inhibition).
*   An upward-pointing arrow next to the Deep box indicates an increase or enhancement in activity.

### 4. Data Trends & Details
Since this is a schematic model and not a plot, there are no quantitative axes or data trends to describe. The arrows and associated symbols (up/down arrows) qualitatively represent changes in neural activity or influence strength.

### 5. Contextual Caption Integration
The caption provides crucial context for interpreting the schematic elements:

*   **Functional vs. Anatomical:** The connections shown are functional, not anatomical.
*   **Layer Mapping:** Superficial layers correspond to cortical layers 1-4, and Deep layers correspond to layers 5/6.
*   **Scenario Interpretation (Left Subpanel):** This scenario describes the system being dynamically prepared for stimulus A. Feedback from deep layers inhibits MUA and enhances alpha/beta in the deep layers. This enhanced deep-layer activity then functionally inhibits superficial-layer processing of stimulus A by reducing spiking and gamma, thereby reducing feedforward outputs.
*   **Scenario Interpretation (Right Subpanel):** This scenario occurs when a strong prediction for stimulus B is present while stimulus A is presented. In this case, the feedback alpha/beta inhibition to the A column is weak or absent. Consequently, the A column becomes more excitable, responding to stimulus A with increased gamma/spiking and enhanced feedforward output (interpreted as a prediction error).
*   **Grading:** The model hypothesizes that this mechanism can be graded based on the strength of prediction.

> Figure caption (from PDF text): Fig. 6.
Predictive routing model. Arrows and connections represent func-
tional (not anatomical) connections between areas/layers. Thick lines rep-
resent effective connections with increased influence; thin lines represent
effective connections with decreased influence. The Upper boxes represent
superficial layers (1 to 4) and the Lower boxes represent deep layers (5/6).
(Left subpanel) Sensory cortex is dynamically prepared to process its pre-
ferred stimulus, stimulus A, by feedback which inhibits MUA and enhances
alpha/beta in deep layers. Enhanced deep-layer alpha/beta functionally in-
hibits superficial-layer processing of stimulus A by reducing spiking and
gamma, reducing feedforward outputs. (Right subpanel) When a strong
prediction for stimulus B is present and stimulus A is presented (as in the first
few trials of an unpredictable block after a predictable block where “B” was
the repeated/predicted sample), there is less feedback alpha/beta inhibition
to the A column. Deep-layer to superficial-layer inhibition is weak or absent.
The A column is more excitable and responds to stimulus A with more
gamma/spiking and enhanced feedforward output from superficial layers (a
prediction error). Although we hypothesize this mechanism occurs at the
level of cortical columns, it could apply to any pathway that processes the
specific predicted stimulus. We also hypothesize that this mechanism can be
graded to reflect varying strengths of prediction.


### 1. Overall Layout & Structure
The figure is structured as a schematic flow chart, divided conceptually into two scenarios (Left and Right subpanels), although the provided image snippet only clearly shows elements related to a general mechanism. The structure involves two main functional blocks stacked vertically: an upper block representing superficial layers and a lower block representing deep layers.

### 2. Visual Components & Symbols
**Nodes/Boxes:**
*   **Upper Box (Superficial Layers):** Labeled "A Column Gamma Spiking." This represents the processing activity in superficial cortical layers (Layers 1-4, according to the caption).
*   **Lower Box (Deep Layers):** Labeled "Alpha/beta $\downarrow$." This represents the activity in deep cortical layers (Layers 5/6).

**Connections and Flow:**
*   **Feedback Loops (Top):** At the top of the diagram, there are two distinct feedback pathways indicated by lines connecting back to the upper box.
    *   On the left, a blue line segment is shown with an arrow pointing towards the upper box, labeled "Feed."
    *   On the right, a red, segmented line segment is shown with an arrow pointing towards the upper box, also labeled "Feed."
*   **Downward Flow (Top to Bottom):** A downward arrow connects the upper box ("A Column Gamma Spiking") to the lower box ("Alpha/beta $\downarrow$").
*   **Upward Flow (Bottom to Top):** An upward arrow connects the lower box ("Alpha/beta $\downarrow$") back up to the upper box ("A Column Gamma Spiking").
*   **External Connections:** Arrows extend outward from the boxes, indicating inputs or outputs to/from the system.

**Line Thickness and Influence:**
The caption specifies that "Thick lines represent effective connections with increased influence; thin lines represent effective connections with decreased influence." While the provided snippet does not clearly delineate thick vs. thin lines for all internal connections, this distinction is a key feature of the model's representation style.

### 3. Labels, Keys & Legends
**Internal Labels:**
*   Upper Box: "A Column Gamma Spiking"
*   Lower Box: "Alpha/beta $\downarrow$"

**External Labels:**
*   The top feedback lines are labeled "Feed."
*   Arrows indicate directional flow (e.g., $\uparrow$ next to the upper box, $\downarrow$ next to the lower box).

### 4. Contextual Caption Integration
The caption provides crucial context for interpreting the schematic:
*   **Layer Representation:** The upper boxes represent superficial layers (1 to 4), and the lower boxes represent deep layers (5/6).
*   **Functional Connections:** Arrows denote functional connections, not anatomical ones.
*   **Scenario Interpretation (Left Subpanel):** The left side illustrates a scenario where the sensory cortex is dynamically prepared for stimulus A. This preparation involves **feedback that inhibits MUA and enhances alpha/beta in deep layers**. Furthermore, the caption states that **enhanced deep-layer alpha/beta functionally inhibits superficial-layer processing of stimulus A by reducing spiking and gamma, thereby reducing feedforward outputs.**
*   **Scenario Interpretation (Right Subpanel):** The right side illustrates a scenario where a strong prediction for stimulus B is present while A is presented. In this case, there is **less feedback alpha/beta inhibition to the A column**, leading to a state where the A column is more excitable and responds with **more gamma/spiking and enhanced feedforward output (a prediction error)**.

In summary, the figure models a dynamic interaction where deep-layer oscillatory activity (Alpha/beta) modulates the excitability and spiking patterns ($\text{Gamma Spiking}$) in superficial cortical columns, serving as a mechanism for predictive coding.

31466
|
www.pnas.org/cgi/doi/10.1073/pnas.2014868117
Bastos et al.

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 9

Networks and Directionality. Both coherence and Granger cau-
sality analysis showed that rhythmic interactions were modulated
by stimulus predictability at several frequencies. Gamma-band
coherence within and between areas was higher with unpredict-
able than predictable stimuli. This effect was largest for coherence
between superficial layers of areas V4 and PFC. Granger causality
analysis further showed that the increase in gamma-band coher-
ence with unpredictable stimuli was stronger in the feedforward
than feedback direction. In V4, this was more prominent in su-
perficial layers. There was overall greater alpha/beta coherence
with predictable stimuli. The strongest effects involved PFC and
were stronger in the feedback compared to feedforward direction.
In the presample interval, the enhanced Granger causality during
predictable stimuli was strongest between deep layers of PFC to
the rest of the network. These results are in line with hierarchical
and rhythms models where (gamma-based) prediction errors pri-
marily feed forward flow up the cortical hierarchy and (alpha/beta-
based) predictions flow down the cortical hierarchy. They suggest
that modulation of interareal synchronization at distinct fre-
quencies is a central mechanism in communicating specific (pre-
dicted
vs.
unpredicted)
information
(65–68).
In
addition,
prefrontal control over behavior is thought to be mediated by
dynamic patterns of neuronal functional connectivity (69).

Higher-Order Cortex Inhibition of V4. Trial-by-trial beta power in all
higher-order areas except 7A negatively coupled to both spikes
and gamma power in V4. Interestingly, this corticocortical top-
down inhibition of V4 spiking was found only in deep layers,
despite the fact that anatomically, top-down feedback targets
both superficial and deep layers of V4 (46). In contrast, the ac-
tual effects of prediction on spiking and gamma were stronger in
superficial layers. This suggests distinct layers for transmitting
top-down prediction signals (in deep layers of V4) vs. bottom-up
routing of unpredicted information (in superficial layers of V4).
It also suggests a local circuit mechanism in visual cortex where
deep layers functionally inhibit activity of superficial layers (70).

Summary. Our results suggest a hierarchical layer and frequency-
specific framework for top-down vs. bottom-up processing re-
lated to stimulus predictability. We interpret the results in a
framework we call predictive routing (Fig. 6). Unpredictable
stimuli evoked stronger feedforward- superficial-layer gamma/
spiking (and theta), especially when they violated a previous
prediction: the hallmark of a prediction error signal. Superficial-
layer parietal area 7A high beta also signaled violations in both
feedforward and feedback directions, which could engage
working memory update mechanisms to process and hold
unpredicted information online. Coherence and feedback con-
nectivity were enhanced in the alpha/beta band when a stimulus
was predictable. In the presample interval this enhanced feed-
back connectivity during predictable stimuli originated in deep
layers of PFC. Alpha/beta power in higher-order cortical areas
LIP, FEF, and PFC negatively modulated spiking in deep layers
of V4. The modulatory effects of stimulus predictability on al-
pha/beta and on gamma/spiking modulation was strongest at the
sensory cortical sites that preferred the predicted stimulus.
Spiking/gamma in sensory cortex was only selective to the pre-
dictive stimulus in superficial layers. Alpha/beta was only selec-
tive to the predicted stimulus in deep layers. These results are
consistent with the predictive routing model, which states that
there need not be specialized circuits for extracting prediction
error. Rather, when stimuli are predictable, these rhythmic,
layer-specific mechanisms prepare and inhibit columns in sen-
sory cortex that process the predicted stimulus. In the absence of
these pathway-specific prediction signals, sensory samples re-
ceive stronger processing, causing enhanced spiking and feed-
forward gamma. Together, these results suggest that predictive
coding may stem from rhythmic interactions between lower

frequency rhythms in deep cortical layers that signal predictions
and inhibit the superficial-layer gamma and spiking in the sen-
sory pathways that match those predictions.

Experimental Procedures. We performed multilaminar recordings
using linear array U and V probes (Plexon). We recorded spiking
and LFP activity in visual area V4, parietal, and prefrontal cor-
tices of two macaque monkeys (Macaca mulatta) while the ani-
mals performed a delayed match to sample task. All surgical and
animal care procedures were approved by the Massachusetts
Institute of Technology (MIT)’s Committee on Animal Care and
were conducted in accordance with the guidelines of the Na-
tional Institute of Health and MIT’s Department of Comparative
Medicine. Additional details of the study’s methodology are
provided in SI Appendix, Experimental Procedures.

Behavioral Training and Task. Monkeys were trained to sit com-
fortably in a primate chair inside a sound attenuating behavioral
testing booth. They were seated 50 cm away from a LCD monitor
with a 144-Hz refresh rate (ASUS, Taiwan). Using positive re-
inforcement, we trained monkeys to perform a visual search task
(Fig. 1A). Monkeys fixated on a point at the center of the screen
(fixation window radius: 2 to 3 visual degrees) for a duration of 1
s, were presented with one of three cue objects for a duration of
1 s, and were required to maintain fixation over a delay (between
0.5 and 1.2 s). A search array then appeared that consisted of the
cued item together with either one or two distractors presented
at the same eccentricity (3° to 8°), but different visual quadrants
as the cued object. The position of the cued object and the
distractors were always randomly chosen. Monkeys were rewar-
ded with a few drops of diluted juice if they performed a saccade
toward the cued item. Behavioral performance was high for each
of the monkeys (monkey S: 77% over 41 sessions, monkey L:
75% over 30 sessions). Monkeys were trained on this task using a
library of 22 sample images. For recordings, we used a subset of
these images (12), choosing a total of 3 per session. Most ses-
sions (65 out of 71) used the 3 objects depicted in Fig. 1: an
orange, a green block, and a blue car.

To manipulate prediction, the task was performed either with
unpredictable or predictable cuing. During unpredictable cuing,
samples were randomly drawn on each trial. In block cuing/sam-
pling, the sample was held constant for the duration of the block.
The trial-by-trial and blocked modes each lasted for 50 trials be-
fore switching block modes. The starting order was randomized
over sessions. The task design is schematized in Fig. 1A.

Neurophysiological Recordings. All of the data were recorded
through Blackrock headstages (Blackrock Cereplex M), sampled
at 30 kHz, band passed between 0.3 Hz and 7.5 kHz (first order
Butterworth high pass and third order Butterworth low pass),
and digitized at a 16-bit, 250 nV/bit. All LFPs were recorded with
a low-pass 250-Hz Butterworth filter, sampled at 1 kHz, and
alternating current (AC) coupled.

We implanted the monkeys with a custom-machined carbon
PEEK chamber system with three recording wells placed over
visual/temporal, parietal, and frontal cortex. The process for
making the chambers was based on design principles outlined
previously (71). Briefly, we first took an anatomical MRI scan
(0.5 mm^3 voxel size) and/or computed tomography (CT) scan
to extract the bone and coregister the skull model with the brain
tissue. We designed the center of each chamber to overlie the
primary recording area of interest and to have an optimal angle
for perpendicular recordings relative to the cortical folding.
Postoperatively, after the recording chambers were implanted,
MRIs were taken with the recording grid in place, filled with
water, which created a marker to coregister each possible elec-
trode trajectory with the animal’s anatomy, and to confirm tra-
jectories that were as close to perpendicular as possible.

Bastos et al.
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31467

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 10

The areas where we could achieve perpendicular recordings
(for laminar sampling) on the overlying gyrus were V4 (foveal
and parafoveal representations), parietal cortex (area 7A), and
prefrontal cortex (area 8A, ventro and dorsal lateral prefrontal
cortex [VLPFC/DLPFC]). The areas where we recorded without
laminar alignment (due to their location in sulci) were areas FEF
and LIP.

We recorded a total of 71 sessions with laminar probes. In each
session, we inserted between 1 and 3 laminar probes (“U probes”
and “V probes” from Plexon) into each recording chamber with
either 100- or 200-μm intersite spacing and either 16 or 32 total
electrodes per probe. This gave a total linear sampling of 3.0 to
3.1 mm on each probe. Between three and seven probes in total
per session were used, with a total channel count ranging between
48 and 128 electrodes per session. The recording reference was
the reinforcement tube, which made metallic contact with the
entire length of the probe (total probe length from connector to
tip was 70 mm). Some U/V probes had noisy channels (average
power greater than 2 SDs above the mean of all channels, this
occurred on less than 5% of all channels), which were interpolated
based on nearest neighbors prior to analysis.

Multiunit Activity Extraction and Spike Sorting. For the analysis of
the analog MUA we band-pass filtered the raw, unfiltered, 30-kHz
sampled data into a wide band between 500 and 5,000 Hz, the
power range dominated by spikes. The signal was then low-pass
filtered at 250 Hz and resampled to 1,000 kHz. The advantage of
this signal is that it captures all nearby units, including those with
low signal-to-noise ratio that would not be captured with a strict
threshold. For the analysis of thresholded spikes, we manually
sorted spikes using a Plexon offline sorter. For additional details
please see SI Appendix, Experimental Procedures.

Local Field Potential Power, Coherence, and Granger Causality
Analysis. All analyses were performed with customized MAT-
LAB scripts and with Fieldtrip software (72). Bipolar derivation is a
recommended prestep prior to Granger causality and coherence
analysis, as the presence of a common reference can lead to spu-
rious results (73, 74). In addition, bipolar derivation enhances the
spatial localization of LFP signals and removes the common ref-
erence and any common noise or volume conduction in the signal
(75). Here, we computed the sample-by-sample bipolar differences
by subtracting contacts that were at a distance of 400 μm: next-
nearest neighbors for the laminar probe data spaced at 200 μm
between contacts, and next-next-nearest neighbors for the probe
data spaced at 100 μm between contacts.

We then estimated power, coherence, and Granger causality on
these bipolar derivations. We estimated power at all frequencies
from 0 to 250 Hz using multitaper spectral estimation (smoothing
window of 5 Hz), leading to nine tapers per spectral estimate,
using window sizes of 1 s (0 to 1 s relative to sample onset is the

period of visual stimulation, −1 to 0 s relative to sample onset is
the prestimulus fixation interval) per trial. These Fourier coeffi-
cients were then used to calculate the cross-spectral density ma-
trix, from which we derived coherence and nonparametric spectral
Granger causality (45).

Neural Information Analysis with Percent Explained Variance. We
quantified the amount of variance in the task (sample identity)
that could be explained by the spike rate of neurons using an
unbiased statistic called the omega squared (76). For each point
in time relative to sample onset, the amount of variance that
firing rate of a given neuron across trials explained about the
sample was measured. This was done separately for predictable
and unpredictable blocks. We used nonparametric cluster-based
statistics to assess differences in neural information during pre-
dictable vs. unpredictable blocks.

General Linear Model Analysis. We assessed whether trial-by-trial
fluctuations in LFP power during the sample interval in LIP, 7A,
FEF, and PFC could explain variance in gamma power and
MUA activity (averaged between 0.05 and 0.4 s postsample on-
set) in V4. We used a GLM with higher-order power (which had
laminar resolution in PFC and 7A) as the regressors (77). We ran
separate GLMs per session and then combined coefficients
across sessions. We then used a sign test to assess whether the
median sign of these regressors was significantly positive or
negative (reflecting functional inhibition of V4 neural activity by
higher-order cortex power).

Statistical Testing. We computed whether the MUA, power, co-
herence, and Granger causality was systematically different be-
tween conditions (predictable vs. unpredictable). To do this, we
calculated either the mean difference or percent change for each
channel or interareal channel pair of predictable vs. unpredict-
able sampling. We then quantified whether this raw difference or
percent change was significant by performing a cluster-based
nonparametric randomization test (78). For additional details
on statistical testing, please see SI Appendix, Experimental
Procedures.

Data Availability. Data are available on request by contacting Earl
Miller (ekmiller@mit.edu).

ACKNOWLEDGMENTS. We thank Scott Brincat for assistance with surgeries
and data preprocessing and Morteza Moazami and Jefferson Roy for
assistance with surgeries and animal training. We also thank the MIT
veterinary staff and animal caretakers for their excellent support. We also
thank Jaan Aru and Bruno Gomes for comments on the manuscript and
Miles Whittington for many useful conversations. This work was supported
by
National
Institutes
of
Mental
Health
Grant
R37MH087027
and
5K99MH116100-02, Office of Naval Research Multidisciplinary University
Research Initiatives Grant N00014-16-1-2832, and the MIT Picower Institute
Faculty Innovation Fund.

1. L. H. Arnal, A.-L. Giraud, Cortical oscillations and sensory predictions. Trends Cogn. Sci.
16, 390–398 (2012).
2. A. H. Bell, C. Summerfield, E. L. Morin, N. J. Malecek, L. G. Ungerleider, Encoding of stimulus
probability in macaque inferior temporal cortex. Curr. Biol. 26, 2280–2290 (2016).
3. K. P. Körding, D. M. Wolpert, Bayesian integration in sensorimotor learning. Nature
427, 244–247 (2004).
4. A. Alink, C. M. Schwiedrzik, A. Kohler, W. Singer, L. Muckli, Stimulus predictability
reduces responses in primary visual cortex. J. Neurosci. 30, 2960–2966 (2010).
5. P. Kok, J. F. M. Jehee, F. P. de Lange, Less is more: Expectation sharpens representa-
tions in the primary visual cortex. Neuron 75, 265–270 (2012).
6. L. Li, E. K. Miller, R. Desimone, The representation of stimulus familiarity in anterior
inferior temporal cortex. J. Neurophysiol. 69, 1918–1929 (1993).
7. E. K. Miller, L. Li, R. Desimone, A neural mechanism for working and recognition
memory in inferior temporal cortex. Science 254, 1377–1379 (1991).
8. G. Rainer, E. K. Miller, Effects of visual experience on the representation of objects in
the prefrontal cortex. Neuron 27, 179–189 (2000).
9. C. Summerfield, E. H. Trittschuh, J. M. Monti, M.-M. Mesulam, T. Egner, Neural rep-
etition suppression reflects fulfilled perceptual expectations. Nat. Neurosci. 11,
1004–1006 (2008).

10. M. I. Garrido, J. M. Kilner, K. E. Stephan, K. J. Friston, The mismatch negativity: A
review of underlying mechanisms. Clin. Neurophysiol. 120, 453–463 (2009).
11. C. Wacongne et al., Evidence for a hierarchy of predictions and prediction errors in
human cortex. Proc. Natl. Acad. Sci. U.S.A. 108, 20754–20759 (2011).
12. K. Friston, The free-energy principle: A unified brain theory? Nat. Rev. Neurosci. 11,
127–138 (2010).
13. D. Mumford, On the computational architecture of the neocortex. II. The role of
cortico-cortical loops. Biol. Cybern. 66, 241–251 (1992).
14. R. P. N. Rao, D. H. Ballard, Predictive coding in the visual cortex: A functional in-
terpretation of some extra-classical receptive-field effects. Nat. Neurosci. 2, 79–87
(1999).
15. E. B. Issa, C. F. Cadieu, J. J. DiCarlo, Neural dynamics at successive stages of the ventral
visual stream are consistent with hierarchical error signals. eLife 7, e42870 (2018).
16. C. M. Schwiedrzik, W. A. Freiwald, High-level prediction signals in a low-level area of
the macaque face-processing hierarchy. Neuron 96, 89–97.e4 (2017).
17. P. Zmarz, G. B. Keller, Mismatch receptive fields in mouse visual cortex. Neuron 92,
766–772 (2016).
18. R. Auksztulewicz, K. Friston, Repetition suppression and its contextual determinants
in predictive coding. Cortex 80, 125–140 (2016).

31468
|
www.pnas.org/cgi/doi/10.1073/pnas.2014868117
Bastos et al.

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.


---

## Page 11

19. A. M. Bastos et al., Canonical microcircuits for predictive coding. Neuron 76, 695–711
(2012).
20. M. Bauer, M.-P. Stenner, K. J. Friston, R. J. Dolan, Attentional modulation of alpha/
beta and gamma oscillations reflect functionally distinct processes. J. Neurosci. 34,
16117–16125 (2014).
21. A. Brodski, G.-F. Paasch, S. Helbling, M. Wibral, The faces of predictive coding.
J. Neurosci. 35, 8997–9006 (2015).
22. Z. C. Chao, K. Takaura, L. Wang, N. Fujii, S. Dehaene, Large-scale cortical networks for
hierarchical prediction and prediction error in the primate brain. Neuron 100,
1252–1266.e3 (2018).
23. A. Mayer, C. M. Schwiedrzik, M. Wibral, W. Singer, L. Melloni, Expecting to see a
letter: Alpha oscillations as carriers of top-down sensory predictions. Cereb. Cortex 26,
3146–3160 (2016).
24. S. van Pelt et al., Beta- and gamma-band activity reflect predictive coding in the
processing of causal events. Soc. Cogn. Affect. Neurosci. 11, 973–980 (2016).
25. A. Todorovic, F. van Ede, E. Maris, F. P. de Lange, Prior expectation mediates neural
adaptation to repeated sounds in the auditory cortex: An MEG study. J. Neurosci. 31,
9118–9123 (2011).
26. A. M. Bastos, R. Loonis, S. Kornblith, M. Lundqvist, E. K. Miller, Laminar recordings in
frontal cortex suggest distinct layers for maintenance and control of working mem-
ory. Proc. Natl. Acad. Sci. U.S.A. 115, 1117–1122 (2018).
27. M. Lundqvist et al., Gamma and beta bursts underlie working memory. Neuron 90,
152–164 (2016).
28. M. Lundqvist, A. M. Bastos, E. K. Miller, Preservation and changes in oscillatory dy-
namics across the cortical hierarchy. J. Cogn. Neurosci. 32, 2024–2035 (2020).
29. E. K. Miller, M. Lundqvist, A. M. Bastos, Working memory 2.0. Neuron 100, 463–475
(2018).
30. A. M. Bastos et al., Visual areas exert feedforward and feedback influences through
distinct frequency channels. Neuron 85, 390–401 (2015).
31. T. J. Buschman, E. K. Miller, Top-down versus bottom-up control of attention in the
prefrontal and posterior parietal cortices. Science 315, 1860–1862 (2007).
32. J. P. Donoghue, J. N. Sanes, N. G. Hatsopoulos, G. Gaál, Neural discharge and local
field potential oscillations in primate motor cortex during voluntary movements.
J. Neurophysiol. 79, 159–173 (1998).
33. S. Haegens, V. Nácher, R. Luna, R. Romo, O. Jensen, α-Oscillations in the monkey
sensorimotor network influence discrimination performance by rhythmical inhibition
of neuronal spiking. Proc. Natl. Acad. Sci. U.S.A. 108, 19377–19382 (2011).
34. N. Swann et al., Intracranial EEG reveals a time- and frequency-specific role for the
right inferior frontal gyrus and primary motor cortex in stopping initiated responses.
J. Neurosci. 29, 12675–12685 (2009).
35. A. Bollimunta, Y. Chen, C. E. Schroeder, M. Ding, Neuronal mechanisms of cortical
alpha oscillations in awake-behaving macaques. J. Neurosci. 28, 9976–9988 (2008).
36. T. van Kerkoerle et al., Alpha and gamma oscillations characterize feedback and
feedforward processing in monkey visual cortex. Proc. Natl. Acad. Sci. U.S.A. 111,
14332–14341 (2014).
37. A. Maier, G. K. Adams, C. Aura, D. A. Leopold, Distinct superficial and deep laminar
domains of activity in the visual cortex during rest and stimulation. Front. Syst.
Neurosci. 4, 31 (2010).
38. J. F. Mejias, J. D. Murray, H. Kennedy, X.-J. Wang, Feedforward and feedback
frequency-dependent interactions in a large-scale laminar network of the primate
cortex. Sci. Adv. 2, e1601335 (2016).
39. M. A. Smith, X. Jia, A. Zandvakili, A. Kohn, Laminar dependence of neuronal corre-
lations in visual cortex. J. Neurophysiol. 109, 940–947 (2013).
40. D. Xing, C.-I. Yeh, S. Burns, R. M. Shapley, Laminar analysis of visually evoked activity
in the primary visual cortex. Proc. Natl. Acad. Sci. U.S.A. 109, 13871–13876 (2012).
41. A. M. Bastos et al., A DCM study of spectral asymmetries in feedforward and feedback
connections between visual areas V1 and V4 in the monkey. Neuroimage 108,
460–475 (2015).
42. D. A. Pinotsis et al., Contrast gain control and horizontal interactions in V1: A DCM
study. Neuroimage 92, 143–155 (2014).
43. P. Fries, J. H. Reynolds, A. E. Rorie, R. Desimone, Modulation of oscillatory neuronal
synchronization by selective visual attention. Science 291, 1560–1563 (2001).
44. C. A. Bosman et al., Attentional stimulus selection through selective synchronization
between monkey visual areas. Neuron 75, 875–888 (2012).
45. M. Dhamala, G. Rangarajan, M. Ding, Estimating Granger causality from fourier and
wavelet transforms of time series data. Phys. Rev. Lett. 100, 018701 (2008).
46. D. J. Felleman, D. C. Van Essen, Distributed hierarchical processing in the primate
cerebral cortex. Cereb. Cortex 1, 1–47 (1991).
47. J. A. Westerberg, M. A. Cox, K. Dougherty, A. Maier, V1 microcircuit dynamics: Altered
signal propagation suggests intracortical origins for adaptation in response to visual
repetition. J. Neurophysiol. 121, 1938–1952 (2019).

48. N. M. Brunet et al., Stimulus repetition modulates gamma-band synchronization in
primate visual cortex. Proc. Natl. Acad. Sci. U.S.A. 111, 3626–3631 (2014).
49. B. J. Hansen, V. Dragoi, Adaptation-induced synchronization in laminar cortical cir-
cuits. Proc. Natl. Acad. Sci. U.S.A. 108, 10720–10725 (2011).
50. M. W. Spratling, Reconciling predictive coding and biased competition models of
cortical function. Front. Comput. Neurosci. 2, 4 (2008).
51. H. R. Brown, K. J. Friston, Dynamic causal modelling of precision and synaptic gain in
visual perception–An EEG study. Neuroimage 63, 223–231 (2012).
52. H. R. Brown, K. J. Friston, The functional anatomy of attention: A DCM study. Front.
Hum. Neurosci. 7, 784 (2013).
53. M. Bauer, R. Oostenveld, M. Peeters, P. Fries, Tactile spatial attention enhances
gamma-band activity in somatosensory cortex and reduces low-frequency activity in
parieto-occipital areas. J. Neurosci. 26, 490–501 (2006).
54. E. A. Buffalo, P. Fries, R. Landman, T. J. Buschman, R. Desimone, Laminar differences
in gamma and alpha coherence in the ventral stream. Proc. Natl. Acad. Sci. U.S.A. 108,
11262–11267 (2011).
55. D. Jokisch, O. Jensen, Modulation of gamma and alpha activity during a working
memory task engaging the dorsal or ventral stream. J. Neurosci. 27, 3244–3251 (2007).
56. M. Lundqvist, P. Herman, M. R. Warden, S. L. Brincat, E. K. Miller, Gamma and beta
bursts during working memory readout suggest roles in its volitional control. Nat.
Commun. 9, 394 (2018).
57. J. S. Sherfey, S. Ardid, J. Hass, M. E. Hasselmo, N. J. Kopell, Flexible resonance in
prefrontal networks with strong feedback inhibition. PLOS Comput. Biol. 14,
e1006357 (2018).
58. A. K. Roopun et al., Period concatenation underlies interactions between gamma and
beta rhythms in neocortex. Front. Cell. Neurosci. 2, 1 (2008).
59. A. Gelastopoulos, M. A. Whittington, N. J. Kopell, Parietal low beta rhythm provides a
dynamical substrate for a working memory buffer. Proc. Natl. Acad. Sci. U.S.A. 116,
16613–16620 (2019).
60. R. T. Canolty et al., High gamma power is phase-locked to theta oscillations in human
neocortex. Science 313, 1626–1628 (2006).
61. P. A. Herman, M. Lundqvist, A. Lansner, Nested theta to gamma oscillations and
precise spatiotemporal firing during memory retrieval in a simulated attractor net-
work. Brain Res. 1536, 68–87 (2013).
62. P. Lakatos, G. Karmos, A. D. Mehta, I. Ulbert, C. E. Schroeder, Entrainment of neuronal
oscillations as a mechanism of attentional selection. Science 320, 110–113 (2008).
63. A. B. L. Tort, H. G. Rotstein, T. Dugladze, T. Gloveli, N. J. Kopell, On the formation of
gamma-coherent cell assemblies by oriens lacunosum-moleculare interneurons in the
hippocampus. Proc. Natl. Acad. Sci. U.S.A. 104, 13490–13495 (2007).
64. S. Xie, D. Kaiser, R. M. Cichy, Visual imagery and perception share neural represen-
tations in the alpha frequency band. Curr. Biol. 30, 2621–2627.e5 (2020).
65. P. Fries, Rhythms for cognition: Communication through coherence. Neuron 88,
220–235 (2015).
66. T. Womelsdorf et al., Modulation of neuronal interactions through neuronal syn-
chronization. Science 316, 1609–1612 (2007).
67. T. Womelsdorf, S. Ardid, S. Everling, T. A. Valiante, Burst firing synchronizes pre-
frontal and anterior cingulate cortex during attentional control. Curr. Biol. 24,
2613–2621 (2014).
68. T. Womelsdorf, T. A. Valiante, N. T. Sahin, K. J. Miller, P. Tiesinga, Dynamic circuit
motifs underlying rhythmic gain control, gating and integration. Nat. Neurosci. 17,
1031–1039 (2014).
69. D. A. Crowe et al., Prefrontal neurons transmit signals to parietal neurons that reflect
executive control of cognition. Nat. Neurosci. 16, 1484–1491 (2013).
70. S. R. Olsen, D. S. Bortone, H. Adesnik, M. Scanziani, Gain control by layer six in cortical
circuits of vision. Nature 483, 47–52 (2012).
71. G. H. Mulliken et al., Custom-fit radiolucent cranial implants for neurophysiological
recording and stimulation. J. Neurosci. Methods 241, 146–154 (2015).
72. R. Oostenveld, P. Fries, E. Maris, J.-M. Schoffelen, FieldTrip: Open source software for
advanced analysis of MEG, EEG, and invasive electrophysiological data. Comput. In-
tell. Neurosci. 2011, 156869 (2011).
73. A. Trongnetrpunya et al., Assessing granger causality in electrophysiological data:
Removing the adverse effects of common signals via bipolar derivations. Front. Syst.
Neurosci. 9, 189 (2016).
74. M. Vinck et al., How to detect the Granger-causal flow direction in the presence of
additive noise? Neuroimage 108, 301–318 (2015).
75. A. M. Bastos, J.-M. Schoffelen, A tutorial review of functional connectivity analysis
methods and their interpretational pitfalls. Front. Syst. Neurosci. 9, 175 (2016).
76. S. Olejnik, J. Algina, Generalized eta and omega squared statistics: measures of effect
size for some common research designs. Psychol. Methods 8, 434–447 (2003).
77. N. R. Draper, H. Smith, Applied regression analysis (Wiley, 3rd Ed., 1998).
78. E. Maris, R. Oostenveld, Nonparametric statistical testing of EEG- and MEG-data.
J. Neurosci. Methods 164, 177–190 (2007).

Bastos et al.
PNAS
|
December 8, 2020
|
vol. 117
|
no. 49
|
31469

NEUROSCIENCE

Downloaded from https://www.pnas.org by VANDERBILT UNIVERSITY LIBRARY PERIODICALS RECEIVING on May 8, 2023 from IP address 129.59.122.114.
