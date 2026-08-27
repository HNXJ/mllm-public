Article
Cooperative thalamocortical circuit 
mechanism for sensory prediction errors

Shohei Furutachi1 ✉, Alexis D. Franklin1, Andreea M. Aldea1, Thomas D. Mrsic-Flogel1 ✉ & 
Sonja B. Hofer1 ✉

The brain functions as a prediction machine, utilizing an internal model of the world 
to anticipate sensations and the outcomes of our actions. Discrepancies between 
expected and actual events, referred to as prediction errors, are leveraged to update 
the internal model and guide our attention towards unexpected events1-10. Despite the 
importance of prediction-error signals for various neural computations across the 
brain, surprisingly little is known about the neural circuit mechanisms responsible for 
their implementation. Here we describe a thalamocortical disinhibitory circuit that is 
required for generating sensory prediction-error signals in mouse primary visual cortex 
(V1). We show that violating animals' predictions by an unexpected visual stimulus 
preferentially boosts responses of the layer 2/3 V1 neurons that are most selective for 
that stimulus. Prediction errors specifically amplify the unexpected visual input, rather 
than representing non-specific surprise or difference signals about how the visual input 
deviates from the animal's predictions. This selective amplification is implemented 
by a cooperative mechanism requiring thalamic input from the pulvinar and cortical 
vasoactive-intestinal-peptide-expressing (VIP) inhibitory interneurons. In response 
to prediction errors, VIP neurons inhibit a specific subpopulation of somatostatin- 
expressing inhibitory interneurons that gate excitatory pulvinar input to V1, resulting 
in specific pulvinar-driven response amplification of the most stimulus-selective 
neurons in V1. Therefore, the brain prioritizes unpredicted sensory information by 
selectively increasing the salience of unpredicted sensory features through the 
synergistic interaction of thalamic input and neocortical disinhibitory circuits.

Although our senses are continuously bombarded with inputs from 
the environment, only a subset of the sensory information is perceived 
or affects behaviour. Our brains thus prioritize important sensory 
features among irrelevant ones11. Psychological and physiological 
studies indicate that the brain generates internal predictions about 
incoming sensory information and compares them with actual sensory 
inputs5-10, resulting in prediction errors when sensory inputs do not 
match internal predictions. Error signals could mediate prioritization 
of unexpected-and therefore possibly relevant-sensory inputs, and 
be used to update internal predictions5-10. Indeed, sensory prediction- 
error signals have been observed in multiple cortical areas upon the 
violation of subjects' predictions9,10,12-16. Despite their prevalence 
across the brain and importance for perception and learning, it is 
still unclear what information is encoded by sensory prediction error 
signals, how they affect cortical networks, and through which circuit 
mechanisms they arise.

To study the neural implementation of predictive processing in 
cortical sensory networks, we used a paradigm in which head-fixed, 
food-deprived mice running on a cylinder navigated a virtual corridor 
in which they developed spatial predictions about stimulus identity at 
particular locations along the corridor. The corridor walls displayed 
alternating grating stimulus patterns (grating A-grating B-grating

A-grating B) separated by distinct landmarks (Fig. 1a). The visual stimuli 
appeared abruptly when mice reached the corresponding position in 
the corridor and were presented at constant visual flow independent of 
the running speed of the mice, to enable precise control over stimulus 
features and timing (Methods). Upon reaching the reward zone at the 
end of the corridor, mice received a liquid food reward and their posi-
tion was reset to the beginning of the corridor, starting a new trial. Mice 
traversed the corridor many times for five days of training (90 ± 48 
trials (traversals) per day, 59 ± 21 s per trial; mean ± s.d.) during which 
the sequence of the gratings was identical on every trial. On day six (C 
session), the identity of the stimulus at the fourth position changed 
in a subset of trials: a novel grating stimulus C was first shown instead 
of the second grating stimulus B in 10% of trials (block 1, 160 trials in 
total; Fig. 1a). Subsequently, stimulus C was shown at the fourth loca-
tion in all trials (block 2, 40 trials). Previous studies using similar para-
digms showed that mice form predictions of which stimuli to expect at 
specific locations in the corridor14,17. Accordingly, we found that mice 
interrupted their running behaviour when their expectations were 
violated by encountering stimulus C (Extended Data Fig. 1a,b), although 
running speed was not always a reliable behavioural indicator of the 
increasing familiarity of the novel stimulus with repeated exposure 
(Extended Data Fig. 1a,b).

https://doi.org/10.1038/s41586-024-07851-w

Received: 9 June 2023

Accepted: 18 July 2024

Published online: 28 August 2024

Open access

Check for updates

1Sainsbury Wellcome Centre, University College London, London, UK. ✉e-mail: s.furutachi@ucl.ac.uk; t.mrsic-flogel@ucl.ac.uk; s.hofer@ucl.ac.uk

---

Nature  |  Vol 633  |  12 September 2024  |  399

We recorded neural activity of layer 2/3 neurons in V1 using 
two-photon calcium imaging18 (Fig. 1b and Methods), and observed 
a stronger response to a visual stimulus that was novel and therefore 
unexpected (stimulus C in block 1) compared with the same stimu-
lus when it was expected (stimulus C in second half of block 2, P < 1 
× 10−4, hierarchical bootstrapping test; Fig. 1c and Extended Data 
Fig. 2a,b), consistent with previous studies in humans, non-human 
primates and rodents9,10,12-14,16,19-23. This difference in neural responses 
could not be explained by a drift in general behavioural state, such as 
arousal or task engagement across the imaging session, as responses to 
expected grating stimuli A and B were constant throughout the session

(Fig. 1c,d, all P  >  0.05; see also Extended Data Fig. 2a, b). The increased 
response to unexpected visual stimuli could also not be accounted for 
by changes in the animal's motor behaviour (Extended Data Fig. 1). Spe-
cifically, the response increase was not correlated with running speed, 
stimulus-induced deceleration or pupil size (Extended Data Fig. 1). V1 
responses to an unexpected stimulus were slightly larger when this 
stimulus was encountered closer to the reward location (Extended Data 
Fig. 3a-c), consistent with potentially higher behavioural relevance 
of visual stimuli at such a location17. However, the increased neural 
responses to unexpected stimuli were independent of reward-related 
signals in V1 (Extended Data Fig. 3c-e).

L2/3

V1

930 nm

1
Day
2 3 4 5 6

Training 
C session

90%
B4 (expected)

Block
1 
2

C4 (unexpected)

10%
C4
100%
C4 (expected)

100%

160
20
20
Trial

C
session

hSyn-GCaMP6f

Expected

input

Unexpected

actual input

Response to

unecpected C

(A expected)

Response to unexpected C (B expected)

Content of deviation of

actual from expected

Unspecific surprise signal or
 amplified sensory response

Unexpected C - expected C

Unspecific surprise

signal

Amplified sensory

response

Experiment 1
Experiment 2

a
b

c

e

g

j

k
f

Early
Late

2 s

1 z-scored ΔF/F

n = 158
P = 0.48

n = 125
P = 0.27

n = 644
P < 10-4

A1

Traversals with expected C4
Traversals with unexpected C4

B2
A3
C4

0
5
10

0

10

Unexpected C4

(z-scored ΔF/F)

Unexpected D4

(z-scored ΔF/F)

Response

5

m

0
5
10

0

10

Unexpected C4 - expected C4

(z-scored ΔF/F)

Unexpected D4 - expected D4

(z-scored ΔF/F)

n

5

-5
0
5
10
-5

0

5

10

Unexpected C2 - expected C2

(z-scored ΔF/F)

Δ response
Δ response

Unexpected C3 - expected C3

(z-scored ΔF/F)

i

0
5
10

0

5

10

Unexpected C2

(z-scored ΔF/F)

n = 533
r  = 0.91
P = 1.6 × 10-199

n = 533
r  = 0.80
P = 1.8 × 10-122

n = 957
r  = -0.16
P = 4.2 × 10-7

n = 957
r  = -0.034
P = 0.29

Response

Unexpected C3

(z-scored ΔF/F)

h

2 s

C4

D4

l

n = 729
P < 10-4

n = 355
P < 10-4
n = 533
P < 10-4

n = 533
P < 10-4

Unexpected  
Expected

n = 146
P = 0.23

d

Trial 
1-2 
15-16 
37-38
55-56
0

2.5

Visual stimulus response

(z-scored ΔF/F)

C4 (n = 644)
A3 (n = 146)

Block 1
Block 2

Late
Block 2

Early

1
2
3
4

A
B
A
B

B2 95% 
A3 95%

1 
2

C2
5%
C2
100%
C2
100%

1
2
3
4

A
B
A
B

Early
Late

1 
2
Early
Late

B4 90%

1 
2

C4
10%
C4
100%
C4
100%

1
2
3
4

A
B
A
B

Early
Late

C session

D session

B
C

A
C

Expected

input

B
C

D
B

Excitatory
Inhibitory

Neuron:

> Figure description (generated): This figure presents a time-course plot illustrating changes in neural activity across different experimental blocks.

**1. Overall Layout & Structure:**
The figure consists of a single, continuous line graph plotted against trial number on the x-axis and a normalized activity measure ($\Delta F/F$) on the y-axis. The x-axis is segmented into distinct experimental blocks, which are highlighted with background shading.

**2. Visual Components & Symbols:**
*   **Axes:** The y-axis is labeled "(z-scored $\Delta F/F$)" and ranges from 0 to 2.5, with major tick marks every 0.5 units. The x-axis is labeled "Trial" and spans from the beginning of Block 1 through to Trial 56.
*   **Data Series:** Two distinct data series are plotted:
    *   **C4 (Black Circles):** Represented by solid black circles connected by a line.
    *   **A3 (White Circles):** Represented by open white circles connected by a line.
*   **Shading/Blocks:** The x-axis is divided into three visually distinct blocks, indicated by background shading:
    *   **Block 1 (Pink Shading):** Covers trials approximately from 1 to 16.
    *   **Block 2 Early (White/Unshaded):** Covers trials approximately from 16 to 37.
    *   **Block 2 Late (Light Blue Shading):** Covers trials approximately from 37 to 56.

**3. Labels, Keys & Legends:**
*   **Legend:** A legend in the upper right quadrant identifies the data series:
    *   $\bullet$ C4 ($n = 644$)
    *   $\circ$ A3 ($n = 146$)
*   **Block Labels:** Text labels above the corresponding shaded regions identify the experimental phases: "Block 1," "Block 2 Early," and "Block 2 Late."

**4. Data Trends & Details:**
*   **C4 Trend (Black Circles):** In Block 1, the activity starts high (around $z$-score $\approx 1.5$) and shows a steep, monotonic decline across the trials in Block 1, reaching near baseline levels ($\approx 0.2$) by the transition into Block 2 Early. In Block 2 Early and Block 2 Late, the activity remains low and relatively stable, fluctuating slightly around a baseline of $z$-score $\approx 0.2$ to $0.3$.
*   **A3 Trend (White Circles):** In Block 1, the activity starts low (around $z$-score $\approx 0.2$) and remains relatively flat, showing minimal change across Block 1. In Block 2 Early and Block 2 Late, the activity remains consistently low, fluctuating slightly around a baseline of $z$-score $\approx 0.2$.

**5. Contextual Caption Integration:**
The figure visually compares the normalized calcium activity ($\Delta F/F$) of two populations, C4 ($n=644$) and A3 ($n=146$), across three distinct experimental phases: Block 1, Block 2 Early, and Block 2 Late. The data clearly shows a significant initial high activity phase for C4 in Block 1, which rapidly decays to match the baseline levels observed for both populations in subsequent blocks.

> Figure description (generated): This figure presents a schematic diagram illustrating experimental blocks and trial structures, likely related to decision-making or learning paradigms.

**1. Overall Layout & Structure:**
The figure is structured horizontally, divided into several conceptual sections indicated by large letters (A and B) at the top. Below this, a detailed block structure is presented in three main columns representing different phases or conditions: "Block 1," "Early" (under Block A), and "Late" (under Block B).

**2. Visual Components & Symbols:**
*   **Top Row Markers (A, B):** The top section features markers labeled 'A' and 'B', suggesting different experimental phases or conditions.
*   **Block Structure:** The central area is organized into three distinct vertical columns: "Block 1," "Early," and "Late."
*   **Trial Representation:** Within each block/phase, the structure is further broken down into "Trial" rows.
*   **Stimulus/Condition Representation:** The core of the diagram uses patterned boxes to represent experimental trials.
    *   **Patterned Boxes:** These boxes contain alternating diagonal black and white stripes, representing a specific stimulus or condition.
    *   **Text Annotations:** Text labels are placed within or immediately adjacent to these patterned boxes to denote the specific condition (e.g., "C4 (unexpected)", "B4 (expected)").
*   **Bottom Row Data:** Below the main schematic, there are rows indicating sample sizes ($n$) for different conditions (B2, A3, C4).

**3. Labels, Keys & Legends:**
*   **Top Level Labels:** 'A' and 'B' are present at the top.
*   **Block/Phase Labels:** "Block 1," "Early," and "Late" are clearly labeled above the trial structures.
*   **Trial Labels:** The rows are explicitly labeled "Trial."
*   **Condition Labels (within boxes):**
    *   In Block 1: "C4 (unexpected)" and "B4 (expected)".
    *   In Early Phase: "C4 100%".
    *   In Late Phase: "C4 (expected) 100%".
*   **Bottom Row Labels:** The conditions are labeled B2, A3, and C4.
*   **Sample Size Notation:** Below the condition labels, sample sizes are provided: $n = 125$ (under B2), $n = 146$ (under A3), and $n = 644$ (under C4).
*   **Other Annotations:** There are small, partially visible labels like "58" and a symbol $\Delta F/F$ near the bottom right, suggesting measures of neural activity.

**4. Data Trends & Details:**
The diagram does not contain traditional plotted graphs (like line or bar charts) showing trends over time, but rather a structural representation of experimental conditions. The structure implies a progression:
*   Block 1 involves a mix of unexpected (C4) and expected (B4) trials.
*   The "Early" phase appears to be dominated by C4 (100%).
*   The "Late" phase is characterized by C4 trials being explicitly labeled as (expected) and occurring at 100%.

**5. Contextual Caption Integration:**
The labels C4 and B4 refer to specific trial types or stimuli. The structure suggests a comparison between conditions where the outcome is "unexpected" versus "expected," and how this changes across different experimental blocks (Block 1, Early, Late). The notation $n = X$ indicates the sample size for each condition group.

C2

C3

2 s

Unexp. D - exp. D

Unexpected

actual input

> Figure description (generated): This figure is composed of four distinct panels, labeled A, B, C, and D, arranged horizontally. The overall style is conceptual, using diagrams and schematic representations rather than detailed plots or circuit schematics.

Article

Neural responses to grating stimulus C strongly decreased over time 
as mice encountered the visual stimulus more often, and responses 
were asymptotic within several trials in block 2 when stimulus C was 
encountered in every trial (Fig. 1d and Extended Data Fig. 2g). This grad-
ual decrease in response cannot simply be explained by visual adapta-
tion to repetitive stimuli, as C was only presented every 448 ± 364 s 
(mean ± s.d.) in block 1, owing to the considerable length of the virtual 
corridor. Of note, responses also significantly increased when the famil-
iar stimulus A was presented at an unexpected location in the corridor 
(Extended Data Fig. 4a-d, P < 1 × 10−4), and some neurons responded 
to the omission of an expected stimulus14 (Extended Data Fig. 2e,f, 
P < 1 × 10−4 for visual stimulus omission). The elevated neural response 
to an unexpected stimulus does thus not only constitute a response to 
stimulus novelty, but also is most consistent with a prediction-error 
signal. Moreover, the gradual decrease and eventual cessation of the 
prediction-error signal after repeated exposure to the novel stimulus 
at the same location indicates that mice learned to update their spatial 
expectations about stimulus identity over time.

Nature of prediction-error signals

What information sensory prediction error signals represent is cur-
rently unclear. According to theories of predictive coding, prediction

error signals have been proposed to encode the difference between pre-
dicted and actual visual input5-8 (encoding the content of how the actual 
visual input is different from predictions). However, error responses 
could also represent a more unspecific surprise signal, encoding only 
the magnitude of the deviation without its content (also called unsigned 
prediction error9), or could enhance the representation of unpredicted 
sensory input (encoding the content of the actual input). We designed 
further experiments to disambiguate between these options. First, in 
a small subset of trials, we presented stimulus C at one of two differ-
ent locations in the corridor, at which either stimulus B (position 2) 
or stimulus A (position 3) were expected (experiment 1; Fig. 1e,f). Grat-
ing stimulus C elicited a stronger response in V1 in either location when 
it was unexpected (Fig. 1g). In these two instances the actual visual 
stimulus is the same, but the predictions are likely to be different. If 
the prediction-error signal contains information about the predicted 
stimulus and/or how the actual stimulus deviates from this prediction, 
V1 responses should differ to stimulus C at the two different locations. 
However, V1 prediction-error responses to the unexpected stimulus C 
in the two locations were notably similar (Fig. 1h,i; r = 0.91, P = 1.6 × 10−199 
and r = 0.80, P = 1.8 × 10−122 (Pearson correlation for Fig. 1h,i, respec-
tively); Extended Data Fig. 3g), indicating that-at least at the level of 
individual neurons in V1-the sensory prediction-error signal contains 
little information about how the actual input differs from predictions.

c
a

d

2 s

-5

0

5
b

1

329

Unexpected C4

trials 
Expected C4

trials

Cells

1

329

Cells

A1
B2
A3
C4

2 s

1 z-scored ΔF/F

0

5

10

15

A1
B2
A3
C4

Unexpected C4 
Expected C4

Visual stimulus response

(z-scored ΔF/F)

n = 329

-4
0
4
8
12
-4

0

4

8

12

Expected C4
(z-scored ΔF/F)

Unexpected C4 - expected C4

(z-scored ΔF/F)

n = 320
r = 0.30 
P = 3.4 × 10-8

-4

0

4

8

12

-1
0
1
-1
0
1

n = 320

B
C
Selective to

Selectivity
(late block 2)
Selectivity
(late block 2)

Unexpected C4 - expected C4

(z-scored ΔF/F)

A
C
Selective to

n = 320

(z-scored
ΔF/F)

f

Highly selective
Non-selective

0

5

Trial 
1-2 15-16
37-38
55-56

Visual stimulus response

(z-scored ΔF/F)

Block 1

Late
Block 2
Early
Block 2

e

0

3

6

Visual stimulus response

(z-scored ΔF/F)

P = 0.25

Non-
selective

Highly
selective
Responsive

to A or B

not C

P = 0.82

P = 0.0078

Responsive to C

(late block 2)

Unexpected C4
Expected C4

Fig. 2 | Prediction error specifically boosts the most stimulus-selective 
neurons. a, Trial-averaged responses of all prediction-error-responsive 
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
unexpected C4 (top; block 1) and expected C4 (bottom; late block 2), sorted by 
response to unexpected C4. b, Same as a, but average response strength of 
individual neurons (top) and mean calcium responses of all neurons (bottom). 
Shading indicates bootstrap 95% confidence intervals. c, Difference in 
response strength to unexpected (block 1) and expected C4 (late block 2) for all 
grating-responsive cells in late block 2, plotted against response to expected 
C4 in late block 2 for individual neurons. Pearson correlation; 9 mice. d, Left, 
difference in response strength between unexpected and expected C4 
responses of individual neurons, plotted against their response selectivity to 
stimulus C versus stimulus B in late block 2 (Methods) for all neurons

> Figure caption (from PDF text): Fig. 2 | Prediction error specifically boosts the most stimulus-selective 
neurons. a, Trial-averaged responses of all prediction-error-responsive 
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
unexpected C4 (top; block 1) and expected C4 (bottom; late block 2), sorted by 
response to unexpected C4. b, Same as a, but average response strength of 
individual neurons (top) and mean calcium responses of all neurons (bottom). 
Shading indicates bootstrap 95% confidence intervals. c, Difference in 
response strength to unexpected (block 1) and expected C4 (late block 2) for all 
grating-responsive cells in late block 2, plotted against response to expected 
C4 in late block 2 for individual neurons. Pearson correlation; 9 mice. d, Left, 
difference in response strength between unexpected and expected C4 
responses of individual neurons, plotted against their response selectivity to 
stimulus C versus stimulus B in late block 2 (Methods) for all neurons
> Figure description (generated): This image displays a single plot, likely Panel D based on the provided caption context, which illustrates a relationship between neuronal response differences and stimulus selectivity.

**1. Overall Layout & Structure:**
The figure is a scatter plot, characterized by individual data points plotted across two axes. A shaded vertical region is present on the right side of the plot, indicating a confidence interval or specific range.

**2. Visual Components & Symbols:**
*   **Data Points:** Numerous small, filled circles represent individual neurons. These points are scattered across the plot area.
*   **Axes:** There is a horizontal (x-axis) and a vertical (y-axis).
*   **Shaded Region:** A light gray, vertically shaded band is located on the far right side of the plot.

**3. Labels, Keys & Legends:**
*   **Title/Annotation above the plot:** The text "Selective to" is positioned above the main plotting area, with a double-headed arrow spanning across the central region of the plot.
*   **X-axis Labeling:** The x-axis is labeled with numerical values, including $-1$, $0$, and $1$.
*   **Y-axis Labeling:** The y-axis is labeled with numerical values ranging from $-4$ to $12$, marked in increments of 4 (i.e., $-4, 0, 4, 8, 12$).
*   **Annotation:** The text "$n = 320$" is present in the lower-left quadrant of the plot area.

**4. Data Trends & Details:**
*   **Y-axis Interpretation (Inferred from Caption D):** The y-axis represents the "difference in response strength between unexpected and expected C4 responses of individual neurons."
*   **X-axis Interpretation (Inferred from Caption D):** The x-axis represents the "response selectivity to stimulus C versus stimulus B in late block 2 for individual neurons."
*   **Data Distribution:** The majority of the data points are clustered near $y=0$ for x-values between approximately $-1$ and $1$.
*   **Trend near the Shaded Region:** As the x-values approach and enter the shaded region (around $x=1$), there is a noticeable upward trend in the y-values. The data points within or immediately adjacent to the shaded region show higher positive values on the y-axis, reaching up towards $y=12$.

**5. Contextual Caption Integration:**
The caption identifies this plot (Panel d) as showing the "difference in response strength between unexpected and expected C4 responses of individual neurons, plotted against their response selectivity to stimulus C versus stimulus B in late block 2 (Methods) for all neurons." The visual elements directly map to this description: the y-axis is the difference in response strength, and the x-axis represents stimulus selectivity (C vs B).

> Figure caption (from PDF text): Fig. 2 | Prediction error specifically boosts the most stimulus-selective 
neurons. a, Trial-averaged responses of all prediction-error-responsive 
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
unexpected C4 (top; block 1) and expected C4 (bottom; late block 2), sorted by 
response to unexpected C4. b, Same as a, but average response strength of 
individual neurons (top) and mean calcium responses of all neurons (bottom). 
Shading indicates bootstrap 95% confidence intervals. c, Difference in 
response strength to unexpected (block 1) and expected C4 (late block 2) for all 
grating-responsive cells in late block 2, plotted against response to expected 
C4 in late block 2 for individual neurons. Pearson correlation; 9 mice. d, Left, 
difference in response strength between unexpected and expected C4 
responses of individual neurons, plotted against their response selectivity to 
stimulus C versus stimulus B in late block 2 (Methods) for all neurons
> Figure description (generated): This image displays a single graph, likely representing data from multiple panels (a, b, c, d) as suggested by the caption, although only one plot is fully visible.

**1. Overall Layout & Structure:**
The image presents a single, complex line graph with error bars, suggesting it is one of the sub-panels (likely Panel 2a or 2b based on the caption). The plot is structured with a vertical y-axis and a horizontal x-axis.

**2. Visual Components & Symbols:**
*   **Data Points/Lines:** There are two distinct sets of data points plotted:
    *   **Black Circles ($\bullet$):** Represent "Highly selective" neurons. These points are connected by a line, showing a trend over the x-axis.
    *   **White Circles ($\circ$):** Represent "Non-selective" neurons. These points are also connected by a line, showing a trend over the x-axis.
*   **Error Bars:** Vertical lines (error bars) extend above and below each data point for both highly selective and non-selective neurons, indicating variability (likely standard deviation or SEM).
*   **Shading:** The background is segmented by two shaded regions:
    *   A **light pink/reddish-brown shaded area** on the left side of the plot.
    *   A **light blue/cyan shaded area** on the right side of the plot.

**3. Labels, Keys & Legends:**
*   **Legend:** A legend is present in the upper right quadrant of the plot area:
    *   $\bullet$ Highly selective
    *   $\circ$ Non-selective
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0 to 5, though the full label text is truncated or absent in this crop.
*   **X-Axis Label:** The horizontal axis has no explicit label visible in the provided crop, but it represents a progression across stimuli or conditions.

**4. Data Trends & Details:**
*   **Y-Axis Range:** The visible range is 0 to 5.
*   **Highly Selective Neurons (Black Circles):** These neurons show a high initial response, peaking around the left side of the plot (within the pink shaded area), reaching values near 3.5 to 4.0. The response then generally decreases as the x-axis progresses, dropping below 2.0 in the middle section and remaining low but fluctuating towards the right side (within the blue shaded area).
*   **Non-selective Neurons (White Circles):** These neurons maintain a consistently low response across the entire x-axis, hovering near or slightly above 0.5 throughout both shaded regions.
*   **Shaded Regions Context (Inferred from Caption):** The caption mentions "unexpected C4 (top; block 1)" and "expected C4 (bottom; late block 2)." The pink shading likely corresponds to the unexpected condition, and the blue shading likely corresponds to the expected condition.

**5. Contextual Caption Integration:**
The caption identifies this figure as relating to "Prediction error specifically boosts the most stimulus-selective neurons." The legend confirms that the black circles represent these "Highly selective" neurons, which are expected to show a greater response difference related to prediction error compared to the "Non-selective" neurons (white circles). The shading likely demarcates experimental blocks or conditions related to the prediction error manipulation.

> Figure caption (from PDF text): Fig. 2 | Prediction error specifically boosts the most stimulus-selective 
neurons. a, Trial-averaged responses of all prediction-error-responsive 
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
unexpected C4 (top; block 1) and expected C4 (bottom; late block 2), sorted by 
response to unexpected C4. b, Same as a, but average response strength of 
individual neurons (top) and mean calcium responses of all neurons (bottom). 
Shading indicates bootstrap 95% confidence intervals. c, Difference in 
response strength to unexpected (block 1) and expected C4 (late block 2) for all 
grating-responsive cells in late block 2, plotted against response to expected 
C4 in late block 2 for individual neurons. Pearson correlation; 9 mice. d, Left, 
difference in response strength between unexpected and expected C4 
responses of individual neurons, plotted against their response selectivity to 
stimulus C versus stimulus B in late block 2 (Methods) for all neurons
> Figure description (generated): This figure presents a set of comparative plots illustrating neural responses across different stimulus conditions, categorized by the degree of stimulus selectivity.

**Overall Layout & Structure:**
The figure is structured as a single graph containing multiple data points and statistical annotations, organized along an x-axis representing stimulus selectivity levels. The y-axis represents response strength (likely firing rate or calcium activity).

**Visual Components & Symbols:**
The plot uses distinct markers to differentiate between two conditions:
*   **Red Circles ($\circ$):** Represent "Unexpected C4" responses.
*   **Blue Circles ($\bullet$):** Represent "Expected C4" responses.

The x-axis is divided into three categorical bins: "Responsive," "Non-", and "Highly."

**Labels, Keys & Legends:**
*   **Y-axis Label:** No explicit label is provided for the y-axis, but it ranges from 0 to 6.
*   **X-axis Labels:** "Responsive," "Non-", and "Highly."
*   **Legend/Key:** The legend identifies the markers:
    *   Red Circle ($\circ$): Unexpected C4
    *   Blue Circle ($\bullet$): Expected C4
*   **Statistical Annotations:** Several $P$-values are displayed above the data clusters:
    *   $P = 0.25$ (above the "Responsive" group)
    *   $P = 0.82$ (above the "Non-" group)
    *   $P = 0.0078$ (above the "Highly" group)

**Data Trends & Details:**
The data points are clustered within each of the three x-axis categories:

1.  **Responsive:** The red and blue circles are clustered very close to the baseline (near $y=0$).
2.  **Non-:** The red and blue circles are clustered slightly above the baseline, around $y \approx 0.2$ to $0.4$.
3.  **Highly:** This group shows the highest response magnitudes. The red circles (Unexpected C4) are generally higher than the blue circles (Expected C4), with several red points reaching up to $y \approx 5.5$. The blue circles are clustered lower, generally between $y \approx 1$ and $y \approx 3$.

**Contextual Caption Integration:**
The caption indicates that this figure relates to "Prediction error specifically boosts the most stimulus-selective neurons."
*   The comparison between red ($\text{Unexpected C4}$) and blue ($\text{Expected C4}$) points directly visualizes the effect of prediction error.
*   The x-axis categories ("Responsive," "Non-", "Highly") correspond to the selectivity of the neurons, as described in the caption (e.g., "most stimulus-selective neurons" corresponds to the "Highly" category).
*   The statistical significance ($P=0.0078$) shown above the "Highly" group suggests a significant difference in response strength between unexpected and expected C4 for highly selective neurons.

responsive to at least one of the grating stimuli in late block 2. −1 indicates only 
responsive to B, +1 indicates only responsive to C, and 0 indicates similar 
responses to both. Right, same as on the left but for response selectivity to 
stimulus C versus stimulus A. e, Mean responses to expected (blue) and 
unexpected (red) C4, of V1 neurons responsive to A or B (left), of non-selective 
(middle; responsive to C with selectivity < 0.6) and highly selective neurons 
(right; responsive to C with selectivity towards C, compared to B > 0.8) in late 
block 2. Data are mean responses for individual mice (n = 9), black horizontal 
bars indicate mean across mice. Two-sided signed-rank test. f, Mean calcium 
responses to stimulus C4 across all trials of highly selective (dark grey, n = 77 
cells from 9 mice) and non-selective (light grey, n = 53) grating C4-responsive 
cells in late block 2. Error bars indicate bootstrap 95% confidence intervals. See 
also Extended Data Figs. 4-6.

---

Nature  |  Vol 633  |  12 September 2024  |  401

Next, we tested whether the prediction-error signal represents the 
actual visual input or instead a non-specific surprise or motor-related 
signal (experiment 2; Fig. 1j,k). To this end we introduced an addi-
tional unexpected visual stimulus D that was presented at corridor 
position 4 in a subset of trials in a separate imaging session of the 
same neuronal populations (Fig. 1j,k). Both stimuli C and D evoked 
strong prediction-error responses when they were unexpected (Fig. 1l 
and Extended Data Fig. 2c,d). Neural responses to C and D should be 
similar if they simply represented a non-specific surprise signal, or 
activity related to surprise-triggered movement, such as decelera-
tion in response to an unexpected stimulus. However, most neurons 
responded strongly to only one of the two unexpected stimuli, and V1 
population responses to these stimuli were thus different and specific 
to stimulus features (Fig. 1m,n and Extended Data Fig. 5a-e). This was 
also the case when comparing prediction-error responses to two more 
similar visual stimuli (two gratings of different orientation; Extended 
Data Fig. 5l-p).

Indeed, V1 neurons that responded to an unexpected stimulus (that 
is, grating C) often also responded to the same stimulus when it was 
expected, but not to gratings A or B (Fig. 2a-c). Importantly, only 
visually driven neurons that responded highly selectively to a stimu-
lus showed amplified responses when this stimulus was unexpected 
(Fig. 2d-f; P = 0.0078 for highly selective cells), whereas more broadly 
tuned neurons that also responded to other visual stimuli did not show 
prediction-error signals (Fig. 2e,f: P = 0.82 for non-selective cells). This 
selective amplification was equally evident in the V1 responses to a dif-
ferent unexpected stimulus (stimulus D; Extended Data Fig. 6a-h), and 
could not be explained by differences in response strength between 
selective and non-selective neurons (Extended Data Fig. 6i,j). Nota-
bly, increased V1 activity in response to a familiar stimulus (A) at an 
unexpected location was also restricted to those visually responsive 
neurons selective for the presented stimulus (Extended Data Fig. 4e,f), 
indicating that selective amplification of visual information that is 
unexpected may be a general feature of sensory prediction-error 
signals in V1.

In addition to visually driven neurons, a subset of non-visually 
responsive neurons was also recruited by prediction errors (Fig. 2a and 
Extended Data Fig. 4i). Responses of these neurons were nevertheless 
highly stimulus-selective, and restricted to specific unexpected stimuli 
(Extended Data Fig. 5f-k). Neurons responding to the unexpected omis-
sion of a stimulus constituted an additional V1 population, which was 
not activated when the omitted stimulus was instead replaced by a dif-
ferent, unexpected stimulus (Extended Data Fig. 5q-z). This indicates 
that negative prediction errors (responses to the unexpected absence 
of a stimulus or event10,14) are not significantly contributing to the V1 
prediction-error signal in response to a novel, unexpected stimulus.

Together, these experiments indicate that the prediction-error 
signal evoked in layer 2/3 of V1 by unexpected visual stimuli is not a 
non-specific surprise or a difference signal about how the visual input 
deviates from the animal's predictions. Instead, prediction error sig-
nals are specific to the features of the unexpected visual input and 
amplify the activity of neurons that respond highly selectively to the 
unexpected visual features, thereby selectively increasing the salience 
of unpredicted-and therefore potentially most relevant-sensory 
information.

Circuits mediating V1 prediction-error signals

We next examined the circuit mechanisms by which sensory predic-
tion error signals are implemented in V1 networks. VIP inhibitory 
interneurons in V1 receive cortical top-down and neuromodulatory 
inputs, and can disinhibit local principal cells through prominent 
inhibitory connections onto somatostatin-expressing (SOM) inhibi-
tory interneurons24-28, providing a circuit for top-down gain modulation 
of sensory responses29,30. VIP cells have also been shown to respond

strongly to novel, but not familiar, visual stimuli20,23. To assess whether 
VIP interneuron activity is important for prediction-error signals in V1, 
we first examined how VIP interneurons respond to unexpected and 
expected visual information by using the experimental paradigms 
described in Fig. 1k (Fig. 3a). VIP interneurons were suppressed by 
expected visual stimuli, but strongly responded to unexpected visual 
stimuli (Fig. 3b-d and Extended Data Fig. 7a,b), consistent with previous 
studies15,20,23. VIP neurons also responded to familiar stimuli encoun-
tered at an unexpected location (Extended Data Fig. 8a-d), showing that 
they are not only activated by novel stimuli, but also by sensory predic-
tion errors more generally. Prediction-error responses of VIP neurons 
were much less selective than those of putative excitatory neurons in 
V1: many VIP neurons responded to both unexpected stimuli C and D 
(Extended Data Fig. 7c-e). Responses of VIP interneurons decreased 
over time as mice encountered the same stimulus more often, in par-
allel with the gradual cessation of the prediction-error signal in the 
layer 2/3 network (Fig. 3d; see also Fig. 1d), suggesting that the recruit-
ment of VIP interneurons may be causally related to the generation of 
prediction-error signals in V1.

To test whether the recruitment of VIP interneurons is required for 
the prediction-error signal in the general V1 population, we optoge-
netically silenced VIP interneurons as mice encountered expected 
or unexpected visual stimuli while recording calcium responses of 
V1 layer 2/3 neurons (Fig. 3e-g and Methods). This manipulation was 
highly effective as VIP neurons were fully inactivated during light 
stimulation (Extended Data Fig. 9a-c). Inactivating VIP neurons sig-
nificantly reduced the responses of V1 layer 2/3 cells to unexpected 
visual stimuli (Fig. 3f, middle, P < 1 × 10−4; Extended Data Fig. 10a-h), 
whereas it had no effect on responses to expected visual stimuli A 
and B (Fig. 3f, left; P = 0.24), consistent with the specific recruitment 
of VIP interneurons by unexpected sensory stimuli (Fig. 3a-d). Fur-
thermore, the effect of VIP inactivation on individual V1 layer 2/3 cells 
could not be explained by light artefacts (Extended Data Fig. 9g,h), 
and it was not uniform, but highly correlated with how strongly V1 
neurons were facilitated by prediction errors, much more so than 
with their visual response strength: neurons with the strongest 
prediction-error signal were the ones that were most suppressed by 
VIP interneuron inactivation (Fig. 3g and Extended Data Fig. 10c,e,f). 
V1 prediction-error signals in response to familiar stimulus A at an 
unexpected location were also abolished when VIP neurons were inac-
tivated (Extended Data Fig. 8e,f), demonstrating that the recruitment 
of VIP neurons is required more generally for prediction-error sig-
nals in layer 2/3 of V1, rather than specifically for V1 signals related to 
stimulus novelty.

We next explored the identity of the long-range inputs to V1 that 
could mediate the activation of VIP neurons by prediction errors. The 
pulvinar is a higher-order visual area in thalamus, also called lateral 
posterior nucleus in mice, that integrates information from many corti-
cal and subcortical areas and sends prominent feedback projections 
to V131-36. Notably, pulvinar projections to V1 carry information about 
visual input that is not predicted by the animal's own actions, indicat-
ing that the pulvinar conveys sensory-motor prediction errors to V131. 
To test whether pulvinar projections to V1 also signal prediction 
errors arising from spatial predictions of visual input in our task, we 
used two-photon imaging to record calcium signals from pulvinar 
axons in V131. Calcium activity of pulvinar axons was strongly and 
non-selectively boosted when a visual stimulus was unexpected 
(Fig. 3h-k and Extended Data Fig. 7h-n), and this prediction-error 
response decreased with repeated exposure to the same stimulus, with 
a time course similar to responses in V1 neurons (Fig. 3k). Pulvinar axons 
were also activated by a familiar stimulus at an unexpected location 
(Extended Data Fig. 8g-i).

To determine whether pulvinar input to V1 is required for 
prediction-error signals in V1 neurons, we optogenetically inacti-
vated pulvinar axons in V1 while recording calcium responses of V1

---

Article

layer 2/3 neurons (Fig. 3l-n). This manipulation-light stimulation of 
eNpHR3.0-expressing pulvinar axons in V1-reduced activity of pulvinar 
axons, but had only a partial effect (Extended Data Fig. 9d-f). Neverthe-
less, suppressing pulvinar input to V1 specifically reduced the responses 
of V1 layer 2/3 neurons to unexpected visual stimuli (Fig. 3m, middle,

P < 1 × 10−4, and Extended Data Fig. 10i-p), but not to expected stimuli 
(Fig. 3m, P = 0.074 and P = 0.088 for visual stimuli A and B, and expected 
C and D, respectively). Similar to the effect of VIP neuron silencing, V1 
neurons with strong prediction-error responses were more likely to be 
strongly suppressed by pulvinar inactivation (Fig. 3n and Extended Data

i

Pulvinar bouton no.

900

1

1,078

1

C session
D session

-1

0

1

2 s

Unexpected C4 or D4 
Expected B4 
Expected C4 or D4
Expected

B4

Unexpected

C4 or D4

Expected

C4 or D4

j

2 s

0.1 z-scored ΔF/F

1 z-scored ΔF/F

C session

D session

c
d

g
f

m

k

n

Trial

0

0.2

C4 or D4 
Same-trial average
(A1 B2 A3)

1-2 9-10
29-30
47-48

0
5
10
15
-6

-4

-2

0

2

n = 528

r = -0.50
P = 1.2 × 10-34

Unexpected C4 or D4 - expected C4 or D4

(LED off, z-scored ΔF/F)

LED on - LED off

(unexpected C4 or D4,

z-scored ΔF/F)

e

a

h

l

V1

GCaMP7b

Pulvinar

pulvinar inputs
Imaging

V1

Pulvinar

Pulvinar inputs
V1 L2/3 cells

GCaMP6f

Imaging
Silencing

eNpHR3.0

0
10
-6

-4

-2

0

2

Unexpected C4 or D4 - expected C4 or D4

(LED off, z-scored ΔF/F)

LED on - LED off

(unexpected C4 or D4,

z-scored ΔF/F)

r  = -0.78
P = 9.3 × 10-120

n = 569

b

VIP cell no.

350

2 s

Expected

B4

Unexpected

C4 or D4

Expected

C4 or D4

-2

0

2
1

403

1

C session
D session

-0.2

0

1

1-2 15-16
37-38
55-56
Trial

Block 1

Late
Block 2
Early
Block 2

C4 or D4 
Same-trial average
(A1 B2 A3)

V1

930 nm

GCaMP6f
VIP+

tdTomato

VIP cells
Imaging

VIP-Cre; Ai14

V1

GCaMP6f

930 nm 594 nm

VIP+

eNpHR3.0-mCherry

VIP cells
V1 L2/3 cells
Imaging
Silencing

VIP-Cre

-0.2

0

0.6

Visual stimulus response

(z-scored ΔF/F)

Visual stimulus response

(z-scored ΔF/F)

P < 10-4 P < 10-4

P < 10-4 P < 10-4

C session
D session

2 s

1 z-scored ΔF/F

C session

D session

0
15
0
15
0
15

0

15

0

15

0

15

n = 186
P = 0.088
Cohen's d = 0.13

n = 528
P < 10-4

Cohen's d = 0.36

n = 158
P = 0.074
Cohen's d = -0.15

Expected A3 or B4 
Unexpected C4 or D4 
Expected C4 or D4

LED off (z-scored ΔF/F)

LED on

(z-scored ΔF/F)

LED on 
LED off

2 s

0
15
0
15
0
15

0

15

0

15

0

15

n = 87
P = 0.24

LED off (z-scored ΔF/F)

LED on

(z-scored ΔF/F)

n = 569
P < 10-4

n = 223
P = 2 × 10-4

2 s

1 z-scored ΔF/F

LED
Expected A3 or B4 
Unexpected C4 or D4 
Expected C4 or D4

LED on 
LED off

Unexpected C4 or D4 
Expected B4 
Expected C4 or D4

> Figure description (generated): This figure presents a line graph illustrating data trends across different time intervals, overlaid with shaded regions indicating specific experimental phases.

**1. Overall Layout & Structure:**
The figure consists of a single plot area with two primary data series plotted against a shared x-axis representing time intervals and a y-axis representing a measured value (likely a rate or magnitude). The plot is segmented by two distinct, vertically shaded background regions.

**2. Visual Components & Symbols:**
*   **Data Series 1 (C4 or D4):** Represented by dark gray circular markers connected by a solid line. This series shows fluctuations over the measured intervals.
*   **Data Series 2 (Same-trial average):** Represented by open white circular markers connected by a solid line. This series remains consistently low across all intervals shown.
*   **Shaded Regions:** There are two vertical shaded bands:
    *   A light reddish-pink band covering the intervals 1-2 and extending slightly into 15-16.
    *   A light blue-gray band covering the intervals 37-38 and extending through 55-56.

**3. Labels, Keys & Legends:**
*   **Legend:** The legend in the upper right corner identifies the two data series:
    *   "C4 or D4" corresponds to the dark gray line/markers.
    *   "Same-trial average (A1 B2 A3)" corresponds to the open white line/markers.
*   **X-Axis Labels:** The x-axis displays discrete time intervals: "1-2", "15-16", "37-38", and "55-56".
*   **Y-Axis Labels:** The y-axis is labeled with numerical values, ranging from 0.0 to 0.2 (with tick marks at intervals of 0.1).

**4. Data Trends & Details:**
*   **Y-Axis Range:** The vertical axis ranges from 0.0 to 0.2, with major ticks at 0.0, 0.1, and 0.2.
*   **C4 or D4 Trend:** This series starts high in the 1-2 interval (near 0.2), shows a rapid decline through the 15-16 interval, reaching values near or below 0.1. It then exhibits a low baseline during the 37-38 interval, followed by slight fluctuations around zero in the 55-56 interval.
*   **Same-trial average Trend:** This series remains consistently low, hovering just above the 0.0 line across all intervals shown.
*   **Shaded Region Effects:** The C4 or D4 data shows a significant initial high activity within the reddish-pink shaded region (1-2). The blue-gray shaded region (37-56) corresponds to a period where the C4 or D4 activity is generally low, near baseline.

**5. Contextual Caption Integration:**
The legend explicitly defines the data series: "C4 or D4" represents one measured variable, while "Same-trial average (A1 B2 A3)" represents the average across specific trial components (A1, B2, and A3). The shaded regions delineate distinct experimental phases relevant to the interpretation of these measured variables.

-0.05

0

0.2

Visual stimulus response

(z-scored ΔF/F)

Visual stimulus response

(z-scored ΔF/F)

P < 10-4 P < 10-4

C session
D session

P = 2 × 10-4
P = 6 × 10-4

(z-scored
ΔF/F)

> Figure description (generated): This figure presents a comparison of calcium imaging traces under two different lighting conditions, displayed across two main panels.

**Overall Layout & Structure:**
The figure is composed of two primary comparative plots, positioned side-by-side. Both panels share a similar structure: a set of overlaid line graphs at the top, followed by a scatter plot below them.

**Visual Components & Symbols:**
*   **Top Plots (Time Series):** Each panel features two distinct colored lines representing calcium activity over time.
    *   A black line represents the condition "LED off."
    *   An orange/yellow line represents the condition "LED on."
    *   A dashed gray line is present in both top plots, likely indicating a baseline or zero activity level.
    *   A horizontal bar labeled "2 s" is present in the upper right corner of both panels, indicating a time scale reference.
*   **Bottom Plots (Scatter Plots):** Each panel contains a scatter plot comparing data points.
    *   The x-axis represents "LED off (z-scored $\Delta F/F$)."
    *   The y-axis represents an unspecified variable, implied to be the corresponding measurement under "LED on."
    *   A dashed gray line runs diagonally through the scatter plots, representing a $y=x$ relationship.
    *   Individual data points (circles) are plotted in the scatter plots.

**Labels, Keys & Legends:**
*   **Top Left Annotation:** "LED" is labeled above the top-left plot.
*   **Legend (Top Plots):** A legend in the upper right corner of both plots indicates:
    *   Black line: "LED off"
    *   Orange/Yellow line: "LED on"
*   **Statistical Annotations (Top Plots):** Above the top plots, there are statistical notations:
    *   Left Plot: "$n = 87$" and "$P = 0.24$".
    *   Right Plot: "$n = 569$" and "$P < 10^{-4}$".
*   **Statistical Annotations (Bottom Plots):** Below the scatter plots, further statistical information is provided:
    *   Left Plot (Scatter): "$n = 569$" and "$P < 10^{-4}$". (Note: The $n$ value here seems to correspond to the right plot's top annotation, suggesting a potential labeling inconsistency or grouping across the figure).
    *   Right Plot (Scatter): "$n = 223$" and "$P = 2 \times 10^{-4}$".

**Data Trends & Details:**
*   **Top Plots (Time Series):** In both panels, the calcium traces show a transient increase in activity following an initial baseline period. The peak amplitude appears slightly higher for the "LED on" condition (orange line) compared to the "LED off" condition (black line), particularly in the right panel.
*   **Bottom Plots (Scatter):** The scatter plots show a general positive correlation between the values measured under "LED off" and the corresponding values in the other condition (implied by the diagonal dashed line). The data points are clustered around this diagonal, indicating a strong relationship between the two measurements.

**Contextual Caption Integration:**
The figure compares calcium activity ($\Delta F/F$) under two conditions: "LED off" and "LED on." The statistical metrics ($n$ and $P$-values) quantify the sample size and the significance of the observed differences or correlations between these conditions. The structure suggests a comparison of neural activity modulation by external light stimulation (LED).

(z-scored
ΔF/F)

Block 1

Late
Block 2
Early
Block 2

> Figure description (generated): This figure presents a line graph illustrating data trends, likely related to neural activity or behavioral metrics across different time points.

**1. Overall Layout & Structure:**
The figure consists of a single plot area with two distinct data series plotted against an x-axis representing sequential time points or trials, and a y-axis representing a normalized value (ranging from 0.0 to 0.2). The plot is overlaid with shaded vertical regions indicating specific experimental phases or conditions.

**2. Visual Components & Symbols:**
*   **Data Series 1 (Dark Gray Line with Circles):** Represented by solid dark gray circles connected by a line, labeled in the legend as "C4 or D4."
*   **Data Series 2 (Light Gray Line with Open Circles):** Represented by open light gray circles connected by a line, labeled in the legend as "Same-trial average (A1 B2 A3)."
*   **Shaded Regions:** There are two distinct vertical shaded regions:
    *   A **light red/pink** shaded region on the left side of the plot.
    *   A **light blue/gray** shaded region on the right side of the plot.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with numerical values, ranging from 0.0 to 0.2 (with major ticks at intervals of 0.1).
*   **X-Axis Label:** The horizontal axis is not fully legible but appears to denote sequential points or trials.
*   **Legend:** The legend clearly identifies the two plotted lines:
    *   $\bullet$ C4 or D4 (Dark gray line)
    *   $\circ$ Same-trial average (A1 B2 A3) (Light gray line)

**4. Data Trends & Details:**
*   **Y-Axis Range:** The plotted values range from approximately 0.0 to a peak near 0.15.
*   **Trend in Red Shaded Region (Left):** Both data series start at relatively high values. The "C4 or D4" line shows a steep initial decline within this region, dropping from above 0.1 to below 0.05. The "Same-trial average" line also decreases but remains slightly lower than the C4/D4 data initially.
*   **Trend in Middle Region (Unshaded):** Following the red region, both lines show fluctuating activity. The "C4 or D4" line exhibits several peaks and troughs, generally hovering between 0.0 and 0.1. The "Same-trial average" line remains generally lower, fluctuating around the baseline of 0.0 to 0.05.
*   **Trend in Blue/Gray Shaded Region (Right):** In this region, both data series show a general downward trend compared to the preceding points. The "C4 or D4" line shows some moderate activity before declining towards zero, while the "Same-trial average" line remains close to or below 0.0.

**5. Contextual Caption Integration:**
The legend explicitly defines the data being compared: "C4 or D4" versus the "Same-trial average (A1 B2 A3)." This suggests that the data compares activity from specific channels/conditions (C4 or D4) against an average derived across three distinct phases or conditions labeled A1, B2, and A3. The shaded regions likely demarcate specific experimental phases corresponding to these conditions or related behavioral states.

Fig. 3 | Activity of VIP interneurons and pulvinar input is required for V1 
prediction-error signals. a, Experimental design. Calcium activity of VIP  
cells in V1 layer 2/3 was recorded during the experiment depicted in Fig. 1k.  
b, Single-cell responses for all VIP cells (individual rows) in the session with 
unexpected stimulus C (top; C session, n = 350 cells from 7 mice) and with 
unexpected stimulus D (bottom; D session, n = 403 cells from 7 mice) to 
expected B4 (left), unexpected C4 or D4 (middle; block 1) and expected C4 or 
D4 (right; late block 2), sorted by response strength to unexpected C4 or D4.  
c, Cell- and trial-averaged stimulus responses of all VIP cells in b. P values from 
hierarchical bootstrapping test with Bonferroni correction. d, Average calcium 
responses of all VIP cells to grating stimulus C4 or D4 (dark grey) and other 
gratings in the same trial (average of A1, B2 and A3, light grey) over time.  
e, Experimental design. Calcium activity of V1 layer 2/3 cells was recorded while 
VIP cells were optogenetically silenced during visual stimulus presentation.

> Figure caption (from PDF text): Fig. 3 | Activity of VIP interneurons and pulvinar input is required for V1 
prediction-error signals. a, Experimental design. Calcium activity of VIP  
cells in V1 layer 2/3 was recorded during the experiment depicted in Fig. 1k.  
b, Single-cell responses for all VIP cells (individual rows) in the session with 
unexpected stimulus C (top; C session, n = 350 cells from 7 mice) and with 
unexpected stimulus D (bottom; D session, n = 403 cells from 7 mice) to 
expected B4 (left), unexpected C4 or D4 (middle; block 1) and expected C4 or 
D4 (right; late block 2), sorted by response strength to unexpected C4 or D4.  
c, Cell- and trial-averaged stimulus responses of all VIP cells in b. P values from 
hierarchical bootstrapping test with Bonferroni correction. d, Average calcium 
responses of all VIP cells to grating stimulus C4 or D4 (dark grey) and other 
gratings in the same trial (average of A1, B2 and A3, light grey) over time.  
e, Experimental design. Calcium activity of V1 layer 2/3 cells was recorded while 
VIP cells were optogenetically silenced during visual stimulus presentation.
> Figure description (generated): This image displays three comparative plots, likely representing calcium activity responses of VIP interneurons in V1. The overall structure consists of three side-by-side panels, each containing a combination of time-course plots and scatter plots.

### General Observations (Legend/Key)
The legend provided in the top right corner of the figure indicates:
*   **Black line:** LED off
*   **Orange/Yellow line:** LED on

The caption contextually identifies the data as relating to "Calcium activity of VIP cells in V1 layer 2/3" and the comparison involves responses to "unexpected stimulus C4 or D4."

f, Top, cell- and trial-averaged responses of V1 neurons significantly responsive 
to the presented visual stimuli with (amber) or without (black) VIP silencing. 
Bottom, responses of individual neurons to the visual stimulus indicated above 
during VIP cell silencing (LED on), plotted against responses to the same 
stimulus in control trials (LED off). P values from hierarchical bootstrapping 
test, from 9 mice. g, Effect of VIP neuron silencing (LED on − LED off during 
unexpected stimulus C4 or D4) plotted against the strength of prediction-error 
signals (response to unexpected C4 or D4 − response to expected C4 or D4); 
Pearson correlation. h-k, Same as a-d, but for calcium responses of pulvinar 
axonal boutons in V1 layer 1. l-n, Same as e-g, but the activity of V1 layer 2/3 
cells was recorded while pulvinar axons in V1 were optogenetically silenced. 
c,d,f,j,k,m, Data are mean ± bootstrap 95% confidence intervals (shading or 
error bars). See also Extended Data Figs. 7-10.

---

Nature  |  Vol 633  |  12 September 2024  |  403

Fig. 10k,m), independent of their visual response strength (Extended 
Data Fig. 10n). Moreover, pulvinar input was also required for V1 
prediction-error responses to a familiar stimulus at an unexpected 
location (Extended Data Fig. 8j,k). Together, these cell-type-specific

inactivation experiments indicate that both intracortical VIP interneu-
rons and pulvinar inputs contribute to prediction-error signals in V1. 
Next, we investigated how these two circuit elements interact to gener-
ate the amplified responses to unexpected stimuli.

a
LED (50% of trials)

A1
B2
A3
B4

e

V1 L2/3 cells
Imaging

Pulvinar inputs
Activation

SOM cells
Silencing

d

VIP cells
V1 L2/3 cells
Imaging

Pulvinar inputs
Activation
Activation

b

Pulvinar inputs
V1 L2/3 cells
Imaging
Activation

VIP cells
V1 L2/3 cells
Imaging
Activation

V1

Pulvinar
GCaMP6f

ChrimsonR

c

-1
0
1

A
B
Selective to

-4

0

4

8

LED on - LED off

(z-scored ΔF/F)

-4

0

4

8

LED on - LED off

(z-scored ΔF/F)

-4

0

4

8

LED on - LED off

(z-scored ΔF/F)

-4

0

4

8

LED on - LED off

(z-scored ΔF/F)

n = 118

n = 214

Pulvinar

ChrimsonR

ChrimsonR

VIP

VIP-Cre

Pulvinar
ChrimsonR

eNpHR3.0

SOM

SOM-Cre

ChrimsonR

VIP

VIP-Cre

0

3

6

P = 0.16

P = 0.031

P = 0.031

P = 1

P = 0.84

P = 0.44

Visual stimulus response

(z-scored ΔF/F)

0

3

6

Visual stimulus response

(z-scored ΔF/F)

0

3

6

Visual stimulus response

(z-scored ΔF/F)

0

3

6

Visual stimulus response

(z-scored ΔF/F)

P = 0.43

P = 0.20

P = 0.039

P = 0.22

P = 0.63

P = 0.031

LED on
LED off

n = 307

n = 423
n = 423
P < 10-4

n = 307
P = 0.020

n = 214
P = 0.18

LED off
LED on

0
4
8

0

4

8

Selectivity (LED off)

-1
0
1
Selectivity (LED off)

-1
0
1
Selectivity (LED off)

-1
0
1
Selectivity (LED off)

Responsive to

A not B

Non-
selective

Highly
selective
Responsive to B

Responsive to

A not B

Non-
selective

Highly
selective
Responsive to B

Responsive to

A not B

Non-
selective

Highly
selective
Responsive to B

LED off (z-scored ΔF/F)

0
4
8
LED off (z-scored ΔF/F)

0
4
8
LED off (z-scored ΔF/F)

0
4
8
LED off (z-scored ΔF/F)

n = 118
P = 2.0 × 10-4

LED

> Figure description (generated): This figure is a single plot displaying data across three experimental conditions, comparing two states of an external light source (LED).

**1. Overall Layout & Structure:**
The figure is a scatter plot with error bars, structured horizontally across three distinct groups on the x-axis. The y-axis represents a quantitative measure, and the legend distinguishes between two experimental conditions: "LED on" and "LED off."

**2. Visual Components & Symbols:**
*   **Axes:** The vertical (y) axis is labeled with numerical values ranging from 0 to 6, marked in increments of 1. The horizontal (x) axis is divided into three categorical groups: "Responsive to," "Non-selective," and "Highly selective."
*   **Data Points:** Data points are represented by circles. The color and fill of these circles correspond to the legend:
    *   **Orange/Yellow Circle (Filled):** Represents "LED on."
    *   **Gray Circle (Hollow/Outline):** Represents "LED off."
*   **Error Bars:** Vertical lines (error bars) are attached to each data point, indicating variability.
*   **Statistical Annotations:** Several $P$-values are annotated above the data clusters, indicating statistical comparisons between groups or conditions.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The label on the left vertical axis is partially visible, reading "$\text{Y} \text{ [Unit]}$" (the full unit is truncated).
*   **X-Axis Labels:** The three categories on the x-axis are: "Responsive to," "Non-selective," and "Highly selective."
*   **Legend:** A legend in the upper left corner defines the symbols:
    *   Orange circle: "LED on"
    *   Gray circle: "LED off"
*   **Statistical Annotations:**
    *   Above the first two groups: $P = 0.16$ (spanning across "Responsive to" and "Non-selective").
    *   Above the second and third groups: $P = 0.031$ (spanning across "Non-selective" and "Highly selective").
    *   Above the third group: $P = 0.031$ (This annotation appears specifically above the "Highly selective" group, likely comparing LED on vs. LED off within that group).

**4. Data Trends & Details:**
*   **Responsive to Group:** Both "LED on" and "LED off" data points are clustered very close to the baseline (Y $\approx 0$).
*   **Non-selective Group:** Data points for both conditions are slightly elevated compared to the "Responsive to" group, clustering around Y $\approx 1$ to $2$.
*   **Highly selective Group:** This group shows the highest values. The "LED off" points are clustered around Y $\approx 1$ to $2$, while the "LED on" points show a higher mean, with one point reaching nearly Y $\approx 3$.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so the description relies solely on the visual elements present in the plot itself. The structure clearly compares a measured variable across three functional categories ("Responsive to," "Non-selective," "Highly selective") under two distinct experimental manipulations (LED on vs. LED off).

2 s

1 z-scored ΔF/F

2 s

1 z-scored ΔF/F

2 s

1 z-scored ΔF/F

2 s

1 z-scored ΔF/F

Responsive to

A not B

Non-
selective

Highly
selective
Responsive to B

LED on

(z-scored ΔF/F)

0

4

8

> Figure description (generated): This figure presents a set of comparative scatter plots illustrating data across three distinct experimental conditions.

**1. Overall Layout & Structure:**
The figure consists of a single, multi-panel plot structure arranged horizontally. The data is presented using scatter plots with individual data points connected by lines, suggesting paired or repeated measures across the three conditions.

**2. Visual Components & Symbols:**
*   **Axes:** The vertical axis (Y-axis) is labeled, and the horizontal axis (X-axis) delineates three distinct groups.
*   **Data Points:** Individual data points are plotted for each condition. These points appear to be connected by thin lines, forming small clusters or trajectories across the conditions.
*   **Statistical Annotations:** Above each group, there are statistical annotations indicating $P$-values comparing the groups.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled: "$\text{Normalized } \Delta\text{R}$".
*   **X-Axis Labels (Conditions):** The three conditions along the horizontal axis are labeled:
    1.  "Responsive to $\text{A not B}$" (This label is partially truncated but clearly indicates the first condition).
    2.  "Non-selective" (This label is centered above the second cluster of data points).
    3.  "Highly selective" (This label is centered above the third cluster of data points).
*   **Statistical Annotations:**
    *   Above the first group: "$P = 1$"
    *   Between the first and second groups (or spanning across them): "$P = 0.84$"
    *   Above the third group: "$P = 0.44$"

**4. Data Trends & Details:**
*   **Y-Axis Scale:** The Y-axis ranges from 0 to 6, marked in increments of 1.
*   **Data Clustering:**
    *   **Responsive to A not B:** The data points are clustered very close to the baseline (Y $\approx 0$ to $1$).
    *   **Non-selective:** The data points show a slight upward trend compared to the first group, clustering roughly between Y $\approx 1$ and $2$.
    *   **Highly selective:** The data points show the highest mean values, clustering roughly between Y $\approx 1.5$ and $2.5$.

**5. Contextual Caption Integration:**
The labels on the X-axis ("Responsive to A not B," "Non-selective," and "Highly selective") define the three experimental conditions being compared, which are likely related to neural responsiveness or selectivity based on the context implied by the axis label ($\text{Normalized } \Delta\text{R}$). The $P$-values indicate the statistical significance of differences between these conditions.

LED on

(z-scored ΔF/F)

0

4

8

> Figure description (generated): This figure presents a set of comparative scatter plots illustrating data across three distinct experimental conditions.

**1. Overall Layout & Structure:**
The figure consists of a single, multi-panel plot structure, although it appears to be one continuous graph divided into three distinct groups along the x-axis. The visualization style is a scatter plot showing individual data points connected by lines, suggesting paired or repeated measures across the three conditions.

**2. Visual Components & Symbols:**
*   **Axes:** The vertical (y-axis) and horizontal (x-axis) axes are clearly defined.
*   **Data Points:** Individual data points are plotted for each condition group. These points appear to be connected by thin lines, suggesting a trajectory or comparison between the conditions for each subject.
*   **Annotations:** Statistical significance markers ($P$ values) are placed above the data clusters to indicate comparisons between groups.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled: "$\Delta$ score $\text{d} \text{r}$ ($\%$)".
*   **X-Axis Labels:** The horizontal axis is divided into three categorical groups:
    1.  "Responsive to A not B"
    2.  "Non-selective"
    3.  "Highly selective"
*   **Statistical Annotations:** Several $P$ values are displayed:
    *   Above the first two groups (comparing "Responsive to A not B" and "Non-selective"): $P = 0.43$.
    *   Above the second and third groups (comparing "Non-selective" and "Highly selective"): $P = 0.20$.
    *   Above the third group (comparing "Non-selective" and "Highly selective"): $P = 0.039$.

**4. Data Trends & Details:**
*   **Y-Axis Range:** The y-axis ranges from 0 to 6, marked in increments of 1.
*   **Data Distribution:**
    *   **Responsive to A not B:** The data points are clustered very close to the zero line, with values generally below 1.
    *   **Non-selective:** The data points are clustered slightly higher than the first group, generally between 0.5 and 1.5.
    *   **Highly selective:** This group shows the highest values, with points ranging from near 0 up to approximately 3.0.
*   **Trend Observation:** There appears to be a general increasing trend in the mean $\Delta$ score across the three conditions, with the "Highly selective" group exhibiting the highest scores.

**5. Contextual Caption Integration:**
The labels on the x-axis ("Responsive to A not B," "Non-selective," and "Highly selective") categorize the experimental conditions being compared, likely referring to different behavioral or neural response profiles. The y-axis measures the change in score ($\Delta$ score $\text{d} \text{r}$ ($\%$), indicating a relative change or difference in performance/activity.

> Figure description (generated): This figure is a scatter plot displaying data points across a range of values, with a shaded region highlighting a specific area.

**1. Overall Layout & Structure:**
The figure consists of a single, two-dimensional scatter plot. It features labeled axes and includes annotations indicating the total sample size ($n$).

**2. Visual Components & Symbols:**
*   **Data Points:** The primary data is represented by numerous small, open circles ($\circ$). These points are scattered across the plot area.
*   **Shaded Region:** A vertical, light gray shaded band is present on the right side of the plot. This region spans from approximately $x=0.8$ to $x=1.0$.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with a bracketed unit, though the full label text is truncated or partially obscured. The visible portion suggests units related to a measurement, with tick marks ranging from -4 to 8.
*   **X-Axis Label:** The horizontal axis is labeled "Selectivity (LFD off)". Tick marks are present at -1, 0, and 1.
*   **Annotation:** Below the plot area, there is a text annotation: "$n = 307$".

**4. Data Trends & Details:**
*   **X-Axis Range:** The data spans from approximately $x=-1.2$ to $x=1.0$.
*   **Y-Axis Range:** The vertical axis ranges from -4 to 8.
*   **Data Distribution:** For $x$ values less than approximately 0.7, the data points are generally clustered around a mean value close to zero on the y-axis.
*   **Trend in Shaded Region:** Within the shaded region ($x \approx 0.8$ to $1.0$), there is a noticeable upward trend in the data points, with many circles clustered at higher positive y-values (ranging from approximately 0 to 7).

**5. Contextual Caption Integration:**
No specific contextual caption text was provided, so no interpretation based on external context can be given. The figure visually presents the distribution of a measured variable (Y-axis) as a function of "Selectivity (LFD off)" (X-axis), highlighting the behavior of the data when selectivity approaches 1.0.

> Figure description (generated): This figure presents a combination of scatter plots and line graphs, likely illustrating neural activity changes over time.

**1. Overall Layout & Structure:**
The figure is dominated by a large scatter plot in the lower-left quadrant, overlaid with a time-series line graph positioned above and to the right of the scatter plot. The overall structure suggests a comparison between baseline/pre-event activity (scatter plot) and the temporal dynamics of the response following an event (line graph).

**2. Visual Components & Symbols:**
*   **Scatter Plot Area:** This area contains numerous small, black circular data points ($\circ$). These points are distributed across the lower-left portion of the plot.
*   **Line Graph Area:** This area features two smooth, continuous curves plotted against time. These curves are colored in shades of orange/brown and black/dark gray, indicating two different conditions or datasets being compared.
*   **Annotations:** There are several key annotations: a vertical dashed line, a shaded region above the curves, and statistical text placed in the lower right corner.

**3. Labels, Keys & Legends:**
*   **Y-Axis (Left):** Labeled "1z-scored $\Delta F/F$". The scale ranges from 0 to 8.
*   **X-Axis (Bottom):** Labeled "LED off (z scored $\Delta F/F$)". The scale ranges from approximately -2 to 8.
*   **Y-Axis (Right):** Labeled "1z-scored $\Delta F/F$". This axis corresponds to the line graph.
*   **Time Scale:** A scale bar is present in the upper right corner of the line graph area, labeled "2 s".
*   **Statistical Annotations (Lower Right):**
    *   $n = 307$
    *   $P = 0.020$

**4. Data Trends & Details:**
*   **Scatter Plot Trend:** The black data points are clustered primarily in the region where both axes values are low (near zero), with a tail extending towards positive values on both the X and Y axes.
*   **Line Graph Trend:** The two curves show a temporal profile:
    1.  They start at a relatively low baseline level (around 5 on the right Y-axis scale).
    2.  They exhibit a transient increase, peaking within the shaded region. The peak appears to be around 7 on the right Y-axis scale.
    3.  Following the peak, both curves decline back towards a lower baseline level.
*   **Vertical Dashed Line:** This line is positioned at an X-axis value of approximately 4, marking a specific temporal or experimental demarcation point relative to the line graph.
*   **Shaded Region:** A light, yellowish-tan shaded area is positioned above the peaks of the two curves, indicating a region of interest or significant activity.

**5. Contextual Caption Integration:**
The labels "1z-scored $\Delta F/F$" on both axes indicate that the data represents fluorescence change normalized by baseline, standardized to a z-score. The scatter plot uses this metric for the "LED off" condition, while the line graph displays the temporal evolution of this same metric. The statistical notation ($n=307, P=0.020$) suggests a significant finding derived from the comparison of these datasets.

LED on

(z-scored ΔF/F)

0

4

8

LED on

(z-scored ΔF/F)

Fig. 4 | Neocortical disinhibition and pulvinar input act synergistically.  
a, Experimental design. After training in the virtual corridor (stimuli A-B-A-B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response

> Figure caption (from PDF text): Fig. 4 | Neocortical disinhibition and pulvinar input act synergistically.  
a, Experimental design. After training in the virtual corridor (stimuli A-B-A-B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response
> Figure description (generated): This figure presents a set of comparative plots illustrating neural activity, likely related to visual processing and the influence of pulvinar input. The figure is structured as a comparative graph comparing neuronal responses across different levels of stimulus selectivity.

Article

Cooperative thalamocortical circuit

Pulvinar axons make synaptic connections onto VIP neurons in the 
neocortex30. A plausible scenario for how the pulvinar and neocortical 
VIP neurons interact to mediate prediction-error signals may therefore 
involve pulvinar input activating VIP neurons in V1, which in turn boost 
pyramidal neuron responses to unexpected visual stimuli through the 
VIP-SOM disinhibitory circuit24-26,28. To directly test this hypothesis, 
we optogenetically stimulated either pulvinar axons or VIP interneu-
rons in V1 while monitoring neural responses of V1 layer 2/3 neurons 
to the expected grating stimuli in the virtual corridor (Fig. 4a-c; see 
also Extended Data Fig. 11). Consistent with a previous report37, stimu-
lating pulvinar axons broadly suppressed responses to visual stimuli 
in V1 (Fig. 4b, P = 2.0 × 10−4). Moreover, stimulating pulvinar axons 
excited only a small subset of VIP neurons, and decreased VIP neuron 
prediction-error responses (Extended Data Fig. 12a-f). Optogenetically 
stimulating VIP interneurons had a minor effect on V1 activity, with 
a non-significant trend towards facilitating visual responses, unlike 
the strong amplification of stimulus-selective V1 neurons by predic-
tion errors (Fig. 4c; P = 0.18). Remarkably, simultaneous co-activation 
of both pulvinar axons and VIP neurons strongly facilitated visual 
responses of a subset of V1 neurons (Fig. 4d, P = 0.020), indicating that 
pulvinar input and VIP neurons act synergistically, not additively. More-
over, response facilitation was specific to those visually driven neurons 
that responded highly selectively to the visual stimulus that was paired 
with optogenetic stimulation, mimicking the prediction-error signal in 
V1 (Fig. 4d, P = 0.039; Extended Data Fig. 11f-i; compared to Fig. 2d,e). 
Our experimental evidence therefore does not support a direct path-
way from pulvinar inputs onto VIP neurons to facilitate V1 responses, 
but pulvinar and VIP neurons are likely to be recruited independently, 
and act synergistically to provide stimulus-selective amplification of 
responses to unexpected stimuli in V1.

Our results indicate that when VIP neurons are activated, they can 
counteract the inhibitory influence pulvinar activation has on the V1 
network. The main synaptic targets of VIP neurons are SOM interneu-
rons that inhibit the apical dendrites of pyramidal cells24-26,28. VIP neu-
rons can therefore disinhibit pyramidal cells via the inhibition of SOM 
neurons. We hypothesized that pulvinar activation may recruit SOM 
neurons whose inhibitory influence on the V1 network may be allevi-
ated when VIP neurons are simultaneously active. If this were the case, 
silencing SOM neurons while activating pulvinar should have effects 
similar to VIP neuron and pulvinar co-activation. Indeed, simultaneous 
optogenetic stimulation of pulvinar axons and inactivation of SOM 
neurons in V1 completely abolished the pulvinar-driven suppression of 
V1 activity (Fig. 4e; compared to Fig. 4b). Remarkably, this manipulation 
also strongly and specifically facilitated visual responses of V1 neurons 
responding highly selectively to the visual stimulus paired with the 
optogenetic manipulation, again mimicking the V1 prediction-error 
signal (Fig. 4e, P = 0.031), and suggesting that the pulvinar's excita-
tory drive onto V1 pyramidal neurons is accompanied by a strong 
feed-forward inhibitory drive via SOM neurons.

Although higher-order sensory thalamocortical pathways do not 
prominently target cortical SOM neurons37-39, at least a subset of SOM 
neurons in V1 has been shown to receive input from the pulvinar30,40,41. 
We imaged responses of V1 layer 2/3 SOM neurons while optogeneti-
cally stimulating pulvinar axons in V1, and found that although most 
SOM neurons were either not affected or even suppressed, a subset of 
SOM neurons (16 ± 9%; mean ± s.d.) was strongly activated by pulvinar 
stimulation (Fig. 5a-c and Extended Data Fig. 12g,h). Notably, SOM 
neurons that were recruited by pulvinar stimulation were suppressed 
by unexpected visual input, suggesting that this subset of SOM neurons 
is inhibited by VIP neurons28 (Fig. 5d,e). By contrast, layer 2/3 SOM 
neurons that are not recruited by pulvinar stimulation were activated 
by unexpected visual stimuli, similar to VIP neurons, suggesting that

they do not receive strong inhibition from VIP neurons and/or are more 
strongly driven by the local excitatory layer 2/3 network (Fig. 5d,e), 
consistent with previous studies28,42,43. Together, these results show 
that excitatory drive from the pulvinar onto V1 pyramidal neurons is 
paralleled by a powerful inhibitory pathway via a specific subpopula-
tion of SOM neurons. When VIP neurons are active simultaneously with 
pulvinar input they inhibit SOM neurons, thus reducing feed-forward 
inhibition from pulvinar to V1, and enabling pulvinar drive to strongly 
activate a subset of layer 2/3 pyramidal cells (Fig. 5f). These results 
therefore reveal a circuit driving V1 prediction-error signals through 
synergistic interactions of pulvinar inputs and VIP neurons.

Discussion

Here we describe a mechanism for boosting sensory responses by 
prediction errors in V1 when animals' expectations of visual stimuli 
at specific locations of a virtual environment are violated. Prediction 
errors selectively amplify the representation of unexpected visual 
input, via synergistic interactions of higher-order thalamic input and 
local VIP-SOM disinhibitory circuits in V1.

Prediction-error responses are dependent on VIP neuron activity 
as well as input from the pulvinar, a higher-order visual nucleus in the 
thalamus that has previously been implicated in predictive process-
ing, and conveys prediction-error signals to V131,32,44. Co-activation 
of pulvinar axons and VIP neurons in V1 can reproduce the selective 
amplification of V1 neurons even in the absence of prediction errors. 
Notably, we found that pulvinar input to V1 is gated by VIP-SOM inhibi-
tory interactions. The pulvinar suppresses the activity of V1 cells via a 
subpopulation of SOM neurons. To allow pulvinar input to amplify V1 
responses, this inhibition has to be alleviated by activity in VIP neu-
rons that inhibit SOM neuron responses (Fig. 5f). This mechanism 
may explain seemingly contradictory findings about how the pulvi-
nar affects cortical activity37,45 and establishes VIP neurons as a gate 
for higher-order thalamic input to V1. VIP neurons receive prominent 
neuromodulatory and top-down cortical input, and have been shown 
to be activated by salient events such as reward, punishment and novel 
stimuli20,23,24,26,27,29,30,46-48. They can therefore regulate the influence of 
pulvinar input on visual processing in V1, depending on the relevance 
of visual stimuli or the animal's behavioural state. As VIP-SOM disin-
hibitory circuits and higher-order thalamic feedback input are present 
throughout the cortical hierarchy24-26,28,30,34,47, this cooperative circuit 
mechanism may serve as a common computational motif in neocorti-
cal networks.

Although VIP neurons and pulvinar inputs to V1 are broadly recruited 
by unexpected stimuli (Extended Data Fig. 7), prediction-error sig-
nals in V1 are observed only in subpopulations of neurons that are 
highly selective for the visual stimulus encountered. Our results 
point to a potential circuit mechanism for this selective response 
amplification in V1. We reproduced the selective amplification of 
only stimulus-selective V1 neurons by co-activating VIP neurons 
with pulvinar input to V1, but also when bypassing VIP activation by 
silencing SOM neurons while stimulating pulvinar input (Fig. 4d,e). 
Thus, selectivity of response amplification in V1 neurons does not 
depend on VIP neuron recruitment or the activity of SOM neurons, 
but rather on pulvinar input more effectively driving V1 neurons with 
sharp tuning. This suggests a selective influence of pulvinar on sub-
populations of stimulus-selective V1 neurons, balanced by inhibition 
from pulvinar-driven SOM neurons (Extended Data Fig. 11j-m). This 
pulvinar-dependent response enhancement may be further amplified 
via recurrent excitation within subnetworks of selective V1 neurons 
tuned to the same stimulus49 and lateral suppression of the rest of the 
network via parvalbumin-expressing neurons50-52, collectively leading 
to selective amplification of unexpected input.

Which inputs drive pulvinar and VIP neurons, and what informa-
tion do they convey? Visual prediction errors are derived through

---

Nature  |  Vol 633  |  12 September 2024  |  405

a comparison of the actual visual input with internal predictions of 
expected visual input. Several top-down pathways have been proposed 
to convey different types of stimulus predictions to V1, including higher 
visual areas and anterior cingulate cortex6,14,53. In our paradigm, pre-
diction errors may arise from violations of spatial predictions of the 
expected visual scene at a given location. Such spatio-visual predictions 
necessitate neural representations of space and spatial memory, and 
are thus likely to originate from hippocampus or related areas such as 
the retrosplenial cortex54,55. Previous studies have proposed that visual 
prediction errors may be computed in V16,14,53. We observed sensory 
prediction-error signals not only in V1, but also in the pulvinar, and V1 
prediction errors were dependent on pulvinar input. Prediction-error 
signals may therefore be computed outside of these visual areas-for 
instance, within the hippocampal formation-and conveyed to V1 by 
top-down projections via pulvinar and local VIP interneurons. Alter-
natively, errors could be computed in the pulvinar or in V1 from the 
comparison of visual input with spatio-visual predictions5-10,14, and 
could then be amplified through pulvinar-V1 recurrent connections. 
The generation of other types of visual prediction errors observed in V1, 
such as those signalling deviations from visuo-motor predictions given 
the animal's own actions15,31, probably involves different, motor-related 
pathways, including superior colliculus, anterior cingulate cortex or 
secondary motor cortex10,53,56,57. In general, prediction-error signals in 
V1 may be further enhanced by neuromodulators such as acetylcholine 
or noradrenaline that may signal stimulus saliency and novelty, or 
surprise more generally27,48,58,59, and these signals are likely to influence 
the activity of VIP neurons27,48,60.

Our results indicate that individual V1 neurons do not signal how the 
actual visual input deviates from the animal's predictions, as postu-
lated within the predictive coding framework5-8. Instead, we propose 
an alternative view of predictive processing in sensory circuits: predic-
tion errors amplify the representation of feed-forward sensory input 
in neocortex, while the extent of amplification may depend on how 
much the visual stimulus deviates from expectations and therefore 
the magnitude of animals' surprise. This would explain the particu-
larly strong responses to novel stimuli that were not encountered 
before, as these are the least expected20,23. The amplified responses 
to unexpected stimuli may serve as a neural substrate for attentional 
shifts towards surprising events in the environment. However, the 
content of how actual input deviates from predictions may still be 
encoded in other brain areas or higher-dimensional population 
activity in V1.

In summary, sensory prediction errors in V1 increase the saliency of 
unexpected, and thus probably relevant, visual information. This ena-
bles downstream brain areas to prioritize these signals and potentially 
utilize them for updating internal predictions.

Online content

Any methods, additional references, Nature Portfolio reporting summa-
ries, source data, extended data, supplementary information, acknowl-
edgements, peer review information; details of author contributions 
and competing interests; and statements of data and code availability 
are available at https://doi.org/10.1038/s41586-024-07851-w.

Unexpected
sensory input

Prediction error:
Amplified response
to unexpected 
sensory input

V1

VIP

SOM

Pulvinar

Direct
excitation
Feed-forward

inhibition

Respond to unexpected input

PC

f

a

Imaging

Pulvinar inputs
Activation

SOM cells

V1

Pulvinar

GCaMP6f

ChrimsonR

tdTomato

SOM

SOM-Cre; Ai14

d

LED on - LED off (z-scored ΔF/F )

-3

0

3

-3

0

3

-3

0

3

-3
0
3
-3
0
3
-3
0
3

Recruited cells (n = 29)
Other cells (n = 159)

2 s

Expected

B4

Expected

B4
Unexpected

C4 or D4

Unexpected

C4 or D4
Expected

C4 or D4

Expected

C4 or D4

LED off
LED on

-3

0

3

SOM cell no.

1

159

1
29

Recruited cells
Other cells

b

LED off
LED on
2 s

Recruited cells (n = 29)

Other cells (n = 159)

Expected

B4

Unexpected

C4 or D4

Expected

C4 or D4
c

e

Expected B4

Unexpected
C4 or D4

Expected
C4 or D4

Recruited cells

(n = 29)

Other cells

(n = 159)

P = 0.034

P = 0.098

P = 0.0058

-0.25

0

0.25

-0.25

0

0.25
P = 0.030

LED

Expected

B4

Unexpected

C4 or D4

Expected

C4 or D4

(z-scored
ΔF/F)

1 z-scored ΔF/F

Visual stimulus response

(z-scored ΔF/F)

Visual stimulus response

(z-scored ΔF/F)

Fig. 5 | Pulvinar activates a specific subpopulation of SOM cells.  
a, Experimental design. The activity of SOM cells was recorded while pulvinar 
axons were optogenetically stimulated for 3 s starting at visual stimulus onset. 
b, Single-cell responses to expected and unexpected visual stimuli of all SOM 
cells (individual rows, n = 6 sessions from 4 mice) with (right) or without (left) 
optogenetic stimulation. c, Cell-averaged calcium responses with (amber) or 
without (black) optogenetic stimulation of SOM cells significantly activated  
by pulvinar stimulation (recruited cells, n = 29) and other cells (n = 159). Lines 
represent the mean and shaded regions indicate 95% confidence intervals.  
d, Visual stimulus responses of individual SOM neurons to expected B4 stimulus 
(left), unexpected C4 or D4 stimulus (middle; in block 1) and expected C4 or D4 
stimulus (right; in late block 2) plotted against the effect of pulvinar stimulation

> Figure caption (from PDF text): Fig. 5 | Pulvinar activates a specific subpopulation of SOM cells.  
a, Experimental design. The activity of SOM cells was recorded while pulvinar 
axons were optogenetically stimulated for 3 s starting at visual stimulus onset. 
b, Single-cell responses to expected and unexpected visual stimuli of all SOM 
cells (individual rows, n = 6 sessions from 4 mice) with (right) or without (left) 
optogenetic stimulation. c, Cell-averaged calcium responses with (amber) or 
without (black) optogenetic stimulation of SOM cells significantly activated  
by pulvinar stimulation (recruited cells, n = 29) and other cells (n = 159). Lines 
represent the mean and shaded regions indicate 95% confidence intervals.  
d, Visual stimulus responses of individual SOM neurons to expected B4 stimulus 
(left), unexpected C4 or D4 stimulus (middle; in block 1) and expected C4 or D4 
stimulus (right; in late block 2) plotted against the effect of pulvinar stimulation
> Figure description (generated): This image displays two scatter plots, labeled implicitly as parts of a larger figure (likely Panel d based on the caption). Both plots share the same axes structure and represent visual stimulus responses of individual SOM neurons.

Article

1.	
Schultz, W. & Dickinson, A. Neuronal coding of prediction errors. Annu. Rev. Neurosci. 23, 
473-500 (2000).
2.	
Starkweather, C. K., Babayan, B. M., Uchida, N. & Gershman, S. J. Dopamine reward 
prediction errors reflect hidden-state inference across time. Nat. Neurosci. 20, 581-589 
(2017).
3.	
Lowet, A. S., Zheng, Q., Matias, S., Drugowitsch, J. & Uchida, N. Distributional 
reinforcement learning in the brain. Trends Neurosci. 43, 980-997 (2020).
4.	
Wolpert, D. M., Miall, R. C. & Kawato, M. Internal models in the cerebellum. Trends Cogn. 
Sci. 2, 338-347 (1998).
5.	
Mumford, D. On the computational architecture of the neocortex. II. The role of cortico- 
cortical loops. Biol. Cybern. 66, 241-251 (1992).
6.	
Rao, R. P. & Ballard, D. H. Predictive coding in the visual cortex: a functional interpretation 
of some extra-classical receptive-field effects. Nat. Neurosci. 2, 79-87 (1999).
7.	
Friston, K. A theory of cortical responses. Philos. Trans. R. Soc. B 360, 815-836 (2005).
8.	
Clark, A. Whatever next? Predictive brains, situated agents, and the future of cognitive 
science. Behav. Brain Sci. 36, 181-204 (2013).
9.	
den Ouden, H. E. M., Kok, P. & de Lange, F. P. How prediction errors shape perception, 
attention, and motivation. Front. Psychol. 3, 548 (2012).
10.	
Keller, G. B. & Mrsic-Flogel, T. D. Predictive processing: a canonical cortical computation. 
Neuron 100, 424-435 (2018).
11.	
Rust, N. C. & Cohen, M. R. Priority coding in the visual system. Nat. Rev. Neurosci. 23, 
376-388 (2022).
12.	
Alink, A., Schwiedrzik, C. M., Kohler, A., Singer, W. & Muckli, L. Stimulus predictability 
reduces responses in primary visual cortex. J. Neurosci. 30, 2960-2966 (2010).
13.	
Meyer, T. & Olson, C. R. Statistical learning of visual transitions in monkey inferotemporal 
cortex. Proc. Natl Acad. Sci. USA 108, 19401-19406 (2011).
14.	
Fiser, A. et al. Experience-dependent spatial expectations in mouse visual cortex. Nat. 
Neurosci. 19, 1658-1664 (2016).
15.	
Attinger, A., Wang, B. & Keller, G. B. Visuomotor coupling shapes the functional 
development of mouse visual cortex. Cell 169, 1291-1302.e14 (2017).
16.	
Audette, N. J., Zhou, W., La Chioma, A. & Schneider, D. M. Precise movement-based 
predictions in the mouse auditory cortex. Curr. Biol. 32, 4925-4940.e6 (2022).
17.	
Kim, H. R. et al. A unified framework for dopamine signals across timescales. Cell 183, 
1600-1616.e25 (2020).
18.	
Chen, T.-W. et al. Ultrasensitive fluorescent proteins for imaging neuronal activity. Nature 
499, 295-300 (2013).
19.	
Ranganath, C. & Rainer, G. Neural mechanisms for detecting and remembering novel 
events. Nat. Rev. Neurosci. 4, 193-202 (2003).
20.	 Garrett, M. et al. Stimulus novelty uncovers coding diversity in visual cortical circuits. 
Preprint at bioRxiv https://doi.org/10.1101/2023.02.14.528085 (2023).
21.	
Homann, J., Koay, S. A., Chen, K. S., Tank, D. W. & Berry, M. J. Novel stimuli evoke excess 
activity in the mouse primary visual cortex. Proc. Natl Acad. Sci. USA 119, e2108882119 
(2022).
22.	 Tang, M. F. et al. Expectation violations enhance neuronal encoding of sensory 
information in mouse primary visual cortex. Nat. Commun. 14, 1196 (2023).
23.	 Garrett, M. et al. Experience shapes activity dynamics and stimulus coding of VIP 
inhibitory cells. eLife 9, e50340 (2020).
24.	 Pi, H.-J. et al. Cortical interneurons that specialize in disinhibitory control. Nature 503, 
521-524 (2013).
25.	 Pfeffer, C. K., Xue, M., He, M., Huang, Z. J. & Scanziani, M. Inhibition of inhibition in visual 
cortex: the logic of connections between molecularly distinct interneurons. Nat. 
Neurosci. 16, 1068-1076 (2013).
26.	 Lee, S., Kruglikov, I., Huang, Z. J., Fishell, G. & Rudy, B. A disinhibitory circuit mediates 
motor integration in the somatosensory cortex. Nat. Neurosci. 16, 1662-1670 (2013).
27.	
Fu, Y. et al. A cortical circuit for gain control by behavioral state. Cell 156, 1139-1152 (2014).
28.	 Schneider-Mizell, C. M. et al. Cell-type-specific inhibitory circuitry from a connectomic 
census of mouse visual cortex. Preprint at bioRxiv https://doi.org/10.1101/2023.01.23.525290 
(2023).
29.	 Zhang, S. et al. Long-range and local circuits for top-down modulation of visual cortex 
processing. Science 345, 660-665 (2014).
30.	 Ma, G. et al. Hierarchy in sensory processing reflected by innervation balance on cortical 
interneurons. Sci. Adv. 7, eabf5676 (2021).
31.	
Roth, M. M. et al. Thalamic nuclei convey diverse contextual information to layer 1 of 
visual cortex. Nat. Neurosci. 19, 299-307 (2016).
32.	 Blot, A. et al. Visual intracortical and transthalamic pathways carry distinct information to 
cortical areas. Neuron 109, 1996-2008.e6 (2021).
33.	 Bennett, C. et al. Higher-Order thalamic circuits channel parallel streams of visual 
information in mice. Neuron 102, 477-492.e5 (2019).
34.	 Harris, J. A. et al. Hierarchical organization of cortical and thalamic connectivity. Nature 
575, 195-202 (2019).

35.	 Sherman, S. M. & Guillery, R. W. The role of the thalamus in the flow of information to the 
cortex. Phil. Trans. R. Soc. Lond. B 357, 1695-1708 (2002).
36.	 Grieve, K. L., Acuña, C. & Cudeiro, J. The primate pulvinar nuclei: vision and action. Trends 
Neurosci. 23, 35-39 (2000).
37.	
Fang, Q. et al. A differential circuit via retino-colliculo-pulvinar pathway enhances feature 
selectivity in visual cortex through surround suppression. Neuron 105, 355-369.e6 (2020).
38.	 Audette, N. J., Urban-Ciecko, J., Matsushita, M. & Barth, A. L. POm thalamocortical input 
drives layer-specific microcircuits in somatosensory cortex. Cereb. Cortex 28, 1312-1328 
(2018).
39.	 Sermet, B. S. et al. Pathway-, layer- and cell-type-specific thalamic input to mouse barrel 
cortex. eLife 8, e52665 (2019).
40.	 Pouchelon, G. et al. The organization and development of cortical interneuron 
presynaptic circuits are area specific. Cell Rep. 37, 109993 (2021).
41.	
Yao, S. et al. A whole-brain monosynaptic input connectome to neuron classes in mouse 
visual cortex. Nat. Neurosci. 26, 350-364 (2023).
42.	 Adesnik, H., Bruns, W., Taniguchi, H., Huang, Z. J. & Scanziani, M. A neural circuit for 
spatial summation in visual cortex. Nature 490, 226-231 (2012).
43.	 Pala, A. & Petersen, C. C. H. In vivo measurement of cell-type-specific synaptic connectivity 
and synaptic transmission in layer 2/3 mouse barrel cortex. Neuron 85, 68-75 (2015).
44.	 Kanai, R., Komura, Y., Shipp, S. & Friston, K. Cerebral hierarchies: predictive processing, 
precision and the pulvinar. Philos. Trans. R. Soc. B 370, 20140169 (2015).
45.	 Hu, F. et al. Prefrontal corticotectal neurons enhance visual processing through the 
superior colliculus and pulvinar thalamus. Neuron 104, 1141-1152.e4 (2019).
46.	 Melzer, S. et al. Bombesin-like peptide recruits disinhibitory cortical circuits and enhances 
fear memories. Cell 184, 5622-5634.e25 (2021).
47.	
Szadai, Z. et al. Cortex-wide response mode of VIP-expressing inhibitory neurons by 
reward and punishment. eLife 11, e78815 (2022).
48.	 Ren, C. et al. Global and subtype-specific modulation of cortical inhibitory neurons 
regulated by acetylcholine during motor learning. Neuron 110, 2334-2350.e8 (2022).
49.	 Cossell, L. et al. Functional organization of excitatory synaptic strength in primary visual 
cortex. Nature 518, 399-403 (2015).
50.	 Znamenskiy, P. et al. Functional specificity of recurrent inhibition in visual cortex. Neuron 
112, 991-1000.e8 (2024).
51.	
Bock, D. D. et al. Network anatomy and in vivo physiology of visual cortical neurons. Nature 
471, 177-182 (2011).
52.	 Packer, A. M. & Yuste, R. Dense, unspecific connectivity of neocortical parvalbumin-positive 
interneurons: a canonical microcircuit for inhibition? J. Neurosci. 31, 13260-13271 (2011).
53.	 Leinweber, M., Ward, D. R., Sobczak, J. M., Attinger, A. & Keller, G. B. A sensorimotor circuit 
in mouse cortex for visual flow predictions. Neuron 96, 1204 (2017).
54.	 Hartley, T., Lever, C., Burgess, N. & O'Keefe, J. Space in the brain: how the hippocampal 
formation supports spatial cognition. Philos. Trans. R. Soc. B 369, 20120510 (2014).
55.	 Vann, S. D., Aggleton, J. P. & Maguire, E. A. What does the retrosplenial cortex do? Nat. 
Rev. Neurosci. 10, 792-802 (2009).
56.	 Schneider, D. M., Nelson, A. & Mooney, R. A synaptic and circuit basis for corollary 
discharge in the auditory cortex. Nature 513, 189-194 (2014).
57.	
Brenner, J. M., Beltramo, R., Gerfen, C. R., Ruediger, S. & Scanziani, M. A genetically 
defined tecto-thalamic pathway drives a system of superior-colliculus-dependent visual 
cortices. Neuron 111, 2247-2257.e7 (2023).
58.	 Hangya, B., Ranade, S. P., Lorenc, M. & Kepecs, A. Central cholinergic neurons are rapidly 
recruited by reinforcement feedback. Cell 162, 1155-1168 (2015).
59.	 Jordan, R. & Keller, G. B. The locus coeruleus broadcasts prediction errors across the 
cortex to promote sensorimotor plasticity. eLife 12, RP85111 (2023).
60.	 Kuchibhotla, K. V. et al. Parallel processing by cortical inhibition enables 
context-dependent behavior. Nat. Neurosci. 20, 62-71 (2017).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 
4.0 International License, which permits use, sharing, adaptation, distribution 
and reproduction in any medium or format, as long as you give appropriate 
credit to the original author(s) and the source, provide a link to the Creative Commons licence, 
and indicate if changes were made. The images or other third party material in this article are 
included in the article's Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article's Creative Commons licence and your 
intended use is not permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a copy of this licence, 
visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024

---