## Page 1

398  |  Nature  |  Vol 633  |  12 September 2024

Article
Cooperative thalamocortical circuit 
mechanism for sensory prediction errors

Shohei Furutachi1 ✉, Alexis D. Franklin1, Andreea M. Aldea1, Thomas D. Mrsic-Flogel1 ✉ & 
Sonja B. Hofer1 ✉

The brain functions as a prediction machine, utilizing an internal model of the world 
to anticipate sensations and the outcomes of our actions. Discrepancies between 
expected and actual events, referred to as prediction errors, are leveraged to update 
the internal model and guide our attention towards unexpected events1–10. Despite the 
importance of prediction-error signals for various neural computations across the 
brain, surprisingly little is known about the neural circuit mechanisms responsible for 
their implementation. Here we describe a thalamocortical disinhibitory circuit that is 
required for generating sensory prediction-error signals in mouse primary visual cortex 
(V1). We show that violating animals’ predictions by an unexpected visual stimulus 
preferentially boosts responses of the layer 2/3 V1 neurons that are most selective for 
that stimulus. Prediction errors specifically amplify the unexpected visual input, rather 
than representing non-specific surprise or difference signals about how the visual input 
deviates from the animal’s predictions. This selective amplification is implemented 
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
inputs5–10, resulting in prediction errors when sensory inputs do not 
match internal predictions. Error signals could mediate prioritization 
of unexpected—and therefore possibly relevant—sensory inputs, and 
be used to update internal predictions5–10. Indeed, sensory prediction- 
error signals have been observed in multiple cortical areas upon the 
violation of subjects’ predictions9,10,12–16. Despite their prevalence 
across the brain and importance for perception and learning, it is 
still unclear what information is encoded by sensory prediction error 
signals, how they affect cortical networks, and through which circuit 
mechanisms they arise.

To study the neural implementation of predictive processing in 
cortical sensory networks, we used a paradigm in which head-fixed, 
food-deprived mice running on a cylinder navigated a virtual corridor 
in which they developed spatial predictions about stimulus identity at 
particular locations along the corridor. The corridor walls displayed 
alternating grating stimulus patterns (grating A–grating B–grating

A–grating B) separated by distinct landmarks (Fig. 1a). The visual stimuli 
appeared abruptly when mice reached the corresponding position in 
the corridor and were presented at constant visual flow independent of 
the running speed of the mice, to enable precise control over stimulus 
features and timing (Methods). Upon reaching the reward zone at the 
end of the corridor, mice received a liquid food reward and their posi-
tion was reset to the beginning of the corridor, starting a new trial. Mice 
traversed the corridor many times for five days of training (90 ± 48 
trials (traversals) per day, 59 ± 21 s per trial; mean ± s.d.) during which 
the sequence of the gratings was identical on every trial. On day six (C 
session), the identity of the stimulus at the fourth position changed 
in a subset of trials: a novel grating stimulus C was first shown instead 
of the second grating stimulus B in 10% of trials (block 1, 160 trials in 
total; Fig. 1a). Subsequently, stimulus C was shown at the fourth loca-
tion in all trials (block 2, 40 trials). Previous studies using similar para-
digms showed that mice form predictions of which stimuli to expect at 
specific locations in the corridor14,17. Accordingly, we found that mice 
interrupted their running behaviour when their expectations were 
violated by encountering stimulus C (Extended Data Fig. 1a,b), although 
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

## Page 2

Nature  |  Vol 633  |  12 September 2024  |  399

We recorded neural activity of layer 2/3 neurons in V1 using 
two-photon calcium imaging18 (Fig. 1b and Methods), and observed 
a stronger response to a visual stimulus that was novel and therefore 
unexpected (stimulus C in block 1) compared with the same stimu-
lus when it was expected (stimulus C in second half of block 2, P < 1 
× 10−4, hierarchical bootstrapping test; Fig. 1c and Extended Data 
Fig. 2a,b), consistent with previous studies in humans, non-human 
primates and rodents9,10,12–14,16,19–23. This difference in neural responses 
could not be explained by a drift in general behavioural state, such as 
arousal or task engagement across the imaging session, as responses to 
expected grating stimuli A and B were constant throughout the session

(Fig. 1c,d, all P  >  0.05; see also Extended Data Fig. 2a, b). The increased 
response to unexpected visual stimuli could also not be accounted for 
by changes in the animal’s motor behaviour (Extended Data Fig. 1). Spe-
cifically, the response increase was not correlated with running speed, 
stimulus-induced deceleration or pupil size (Extended Data Fig. 1). V1 
responses to an unexpected stimulus were slightly larger when this 
stimulus was encountered closer to the reward location (Extended Data 
Fig. 3a–c), consistent with potentially higher behavioural relevance 
of visual stimuli at such a location17. However, the increased neural 
responses to unexpected stimuli were independent of reward-related 
signals in V1 (Extended Data Fig. 3c–e).

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

Unspeciﬁc surprise signal or
 ampliﬁed sensory response

Unexpected C – expected C

Unspeciﬁc surprise

signal

Ampliﬁed sensory

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
P < 10–4

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

Unexpected C4 – expected C4

(z-scored ΔF/F)

Unexpected D4 – expected D4

(z-scored ΔF/F)

n

5

–5
0
5
10
–5

0

5

10

Unexpected C2 – expected C2

(z-scored ΔF/F)

Δ response
Δ response

Unexpected C3 – expected C3

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
P = 1.6 × 10–199

n = 533
r  = 0.80
P = 1.8 × 10–122

n = 957
r  = –0.16
P = 4.2 × 10–7

n = 957
r  = –0.034
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
P < 10–4

n = 355
P < 10–4
n = 533
P < 10–4

n = 533
P < 10–4

Unexpected  
Expected

n = 146
P = 0.23

d

Trial 
1–2 
15–16 
37–38
55–56
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

Unexp. D – exp. D

Unexpected

actual input



### Panel A: Content of deviation of actual from expected
*   **Structure:** This panel features a single conceptual diagram, resembling a 2D plot or relationship map.
*   **Visual Components:** There are two main conceptual axes implied by the labels below and to the left. A diagonal dashed line runs through the center of the space defined by these axes, suggesting a baseline or expected relationship.
*   **Labels:**
    *   The vertical axis label on the left is: "Content of deviation of actual from expected".
    *   The horizontal axis label below the diagram is: "Response to unexpected C (B expected)".
    *   The text above the axes reads: "Unexpected C (A expected)".

### Panel B: Unspecific surprise signal or amplified sensory response
*   **Structure:** Similar to Panel A, this panel presents a conceptual diagram.
*   **Visual Components:** It also features a diagonal dashed line, suggesting a baseline or expected relationship.
*   **Labels:** The panel is titled: "Unspecific surprise signal or amplified sensory response".

### Panel C: Expected vs. Actual Input
*   **Structure:** This panel uses a schematic representation involving input stimuli, depicted as patterns of black and white squares.
*   **Visual Components:** There are two distinct input scenarios shown side-by-side, connected by double-headed arrows indicating a comparison or transformation.
    *   **Left Side (Expected Input):** A block of vertical black and white stripes is shown.
    *   **Right Side (Actual Input):** A block of diagonally patterned squares is shown.
    *   The connection between the left and right sides shows: $\text{B} \rightleftharpoons \text{C}$ (with the striped pattern on the left and the checkered/patterned one on the right).
    *   A second comparison is shown below this first pair: A block of vertical black and white stripes on the left, connected to a block of randomly patterned squares on the right.
    *   The labels above these comparisons are: "Expected input" and "Actual input".

### Panel D: Unspecific surprise signal vs. Amplified sensory response
*   **Structure:** This panel is divided into two sub-diagrams, presented side-by-side, resembling conceptual plots.
*   **Visual Components:** Both sub-diagrams feature a diagonal dashed line, similar to Panels A and B.
    *   **Left Sub-diagram:** Shows a shaded area or distribution that slopes downwards from the upper left to the lower right, relative to the dashed line.
    *   **Right Sub-diagram:** Shows a shaded area or distribution that slopes upwards from the lower left to the upper right, relative to the dashed line.
*   **Labels:**
    *   The overall title above these two sub-diagrams is: "Unspecific surprise signal Amplified sensory response".
    *   The x-axis label below the left sub-diagram is: "Unexpected C - expected C".
    *   The y-axis label to the left of the left sub-diagram is: "Unexp. D - exp. D".

1 z-scored ΔF/F

1 z-scored ΔF/F

D4
10%
D4
100%
D4
100%

B4 90%

C3
100%
C3
100%
C3
5%

Fig. 1 | Prediction errors amplify unexpected visual information. a, Structure 
of the virtual corridor and experimental design. b, Two-photon calcium imaging 
approach. c, Average calcium responses to different stimuli in corridor traversals 
with unexpected C (red, in block 1) and with expected C (blue, in late block 2).  
V1 neurons responsive to the presented stimulus in unexpected C trials, expected 
C trials or both were included. Dotted vertical lines indicate grating onsets. 
Data from 9 mice; P values from hierarchical bootstrapping test. See also 
Extended Data Fig. 2b for combined responses of all grating-responsive 
neurons. d, Average calcium responses to stimuli C4 (dark grey) and A3  
(light grey) during C trials across trials and blocks. e, Thought experiment to 
disambiguate information represented by prediction errors. f, Experimental 
design. Stimulus C was presented at position 2 (C2) or at position 3 (C3) in 5% of 
trials each in block 1. g, Average calcium responses to unexpected (red) and

> Figure caption (from PDF text): Fig. 1 | Prediction errors amplify unexpected visual information. a, Structure 
of the virtual corridor and experimental design. b, Two-photon calcium imaging 
approach. c, Average calcium responses to different stimuli in corridor traversals 
with unexpected C (red, in block 1) and with expected C (blue, in late block 2).  
V1 neurons responsive to the presented stimulus in unexpected C trials, expected 
C trials or both were included. Dotted vertical lines indicate grating onsets. 
Data from 9 mice; P values from hierarchical bootstrapping test. See also 
Extended Data Fig. 2b for combined responses of all grating-responsive 
neurons. d, Average calcium responses to stimuli C4 (dark grey) and A3  
(light grey) during C trials across trials and blocks. e, Thought experiment to 
disambiguate information represented by prediction errors. f, Experimental 
design. Stimulus C was presented at position 2 (C2) or at position 3 (C3) in 5% of 
trials each in block 1. g, Average calcium responses to unexpected (red) and


**1. Overall Layout & Structure:**
The image is a two-dimensional scatter plot titled "Response." It plots data points against two continuous variables.

**2. Visual Components & Symbols:**
*   **Data Points:** Numerous small, dark grey circular data points are scattered across the plot area.
*   **Trend Line/Reference Line:** A dashed, light grey line runs diagonally through the upper right quadrant of the plot, sloping upwards from the bottom left to the top right.

**3. Labels, Keys & Legends:**
*   **Title:** "Response" is centered above the plot area.
*   **Y-axis Label:** "(z-scored $\Delta F/F$)" is located vertically on the left side. The scale ranges from 0 to 10, marked with major ticks at intervals of 5.
*   **X-axis Label:** "Unexpected C4" is located horizontally below the plot area. The scale ranges from 0 to 10, marked with major ticks at intervals of 5.
*   **Annotations (Statistics):** Several statistical metrics are provided in the upper right quadrant of the plot:
    *   $n = 957$
    *   $r = -0.16$
    *   $P = 4.2 \times 10^{-7}$

**4. Data Trends & Details:**
*   The scatter plot shows a general negative correlation between the two variables, as indicated by the reported Pearson correlation coefficient ($r = -0.16$).
*   The data points are clustered densely near the origin (low values for both axes), but there are several outliers extending towards higher values on the x-axis (Unexpected C4) and moderate positive values on the y-axis ($\text{z-scored } \Delta F/F$).
*   The dashed line suggests a positive trend, which contrasts with the reported negative correlation ($r = -0.16$).

**5. Contextual Caption Integration:**
The caption identifies this plot as related to "Average calcium responses to stimuli C4 (dark grey) and A3 (light grey) during C trials across trials and blocks," suggesting the plotted points represent neural activity ($\Delta F/F$) in response to specific visual stimuli (C4). The variables "Unexpected C4" and the $\text{z-scored } \Delta F/F$ likely quantify the neural response magnitude associated with unexpected visual input.

> Figure caption (from PDF text): Fig. 1 | Prediction errors amplify unexpected visual information. a, Structure 
of the virtual corridor and experimental design. b, Two-photon calcium imaging 
approach. c, Average calcium responses to different stimuli in corridor traversals 
with unexpected C (red, in block 1) and with expected C (blue, in late block 2).  
V1 neurons responsive to the presented stimulus in unexpected C trials, expected 
C trials or both were included. Dotted vertical lines indicate grating onsets. 
Data from 9 mice; P values from hierarchical bootstrapping test. See also 
Extended Data Fig. 2b for combined responses of all grating-responsive 
neurons. d, Average calcium responses to stimuli C4 (dark grey) and A3  
(light grey) during C trials across trials and blocks. e, Thought experiment to 
disambiguate information represented by prediction errors. f, Experimental 
design. Stimulus C was presented at position 2 (C2) or at position 3 (C3) in 5% of 
trials each in block 1. g, Average calcium responses to unexpected (red) and


**1. Overall Layout & Structure:**
The figure consists of a single, large scatter plot occupying the main visual area.

**2. Visual Components & Symbols:**
*   **Data Points:** Numerous small, circular data points are scattered across the plot area. These represent individual neural responses.
*   **Axes:** The plot has a horizontal (x-axis) and vertical (y-axis).
*   **Reference Lines:** A dashed diagonal line runs from the bottom-left quadrant towards the top-right quadrant, serving as a visual reference.

**3. Labels, Keys & Legends:**
*   **Title:** $\Delta$ response
*   **Y-axis Label:** (z-scored $\Delta F/F$)
*   **X-axis Label:** Unexpected C4 – expected C4
*   **Annotations within the plot area:**
    *   $n = 957$ (Indicating the total number of data points)
    *   $r = -0.034$ (Indicating the correlation coefficient)
    *   $P = 0.29$ (Indicating the p-value)

**4. Data Trends & Details:**
*   **X-axis Range:** The x-axis ranges from approximately -2 to 10.
*   **Y-axis Range:** The y-axis ranges from -2 to 10.
*   **Data Distribution:** The data points are clustered relatively tightly around the origin (0, 0), forming a dense cloud. The distribution appears somewhat centered near zero on both axes.
*   **Trend:** The correlation coefficient ($r = -0.034$) and the high p-value ($P = 0.29$) suggest a very weak, non-significant linear relationship between the prediction error (X-axis) and the change in neural response ($\Delta F/F$, Y-axis).

**5. Contextual Caption Integration:**
The provided caption indicates that this figure relates to calcium imaging data from mice. Specifically, the axes relate to stimuli C4 and A3 during corridor traversals:
*   The X-axis, "Unexpected C4 – expected C4," quantifies the prediction error related to stimulus C4.
*   The Y-axis, "(z-scored $\Delta F/F$)," represents the change in calcium response ($\Delta F/F$) of V1 neurons.
The caption mentions that the data includes responses from "V1 neurons responsive to the presented stimulus in unexpected C trials, expected C trials or both."

> Figure caption (from PDF text): Fig. 1 | Prediction errors amplify unexpected visual information. a, Structure 
of the virtual corridor and experimental design. b, Two-photon calcium imaging 
approach. c, Average calcium responses to different stimuli in corridor traversals 
with unexpected C (red, in block 1) and with expected C (blue, in late block 2).  
V1 neurons responsive to the presented stimulus in unexpected C trials, expected 
C trials or both were included. Dotted vertical lines indicate grating onsets. 
Data from 9 mice; P values from hierarchical bootstrapping test. See also 
Extended Data Fig. 2b for combined responses of all grating-responsive 
neurons. d, Average calcium responses to stimuli C4 (dark grey) and A3  
(light grey) during C trials across trials and blocks. e, Thought experiment to 
disambiguate information represented by prediction errors. f, Experimental 
design. Stimulus C was presented at position 2 (C2) or at position 3 (C3) in 5% of 
trials each in block 1. g, Average calcium responses to unexpected (red) and


**1. Overall Layout & Structure:**
The figure consists of a single, large scatter plot titled "$\Delta$ response."

**2. Visual Components & Symbols:**
*   **Data Points:** Individual data points are represented by open circles ($\circ$). These points are scattered across the plot area.
*   **Trend Line:** A dashed line, sloping upwards from the lower-left to the upper-right corner, indicates a positive correlation trend.

**3. Labels, Keys & Legends:**
*   **Title:** $\Delta$ response
*   **Y-axis Label:** (z-scored $\Delta F/F$)
*   **X-axis Label:** Unexpected C2 – expected C2
*   **Annotations within the plot area:**
    *   $n = 533$: Indicates the total number of data points analyzed.
    *   $r = 0.80$: Indicates the correlation coefficient between the axes variables.
    *   $P = 1.8 \times 10^{-122}$: Indicates the statistical significance of the correlation.

**4. Data Trends & Details:**
*   The plot shows a strong positive linear relationship between the two variables. As the value on the x-axis (Unexpected C2 – expected C2) increases, the corresponding z-scored $\Delta F/F$ on the y-axis tends to increase.
*   The data points cluster around the dashed trend line, confirming a strong correlation ($r=0.80$).

**5. Contextual Caption Integration:**
The caption identifies this plot as relating to "Prediction errors amplify unexpected visual information." The axes relate to calcium imaging data:
*   The y-axis, (z-scored $\Delta F/F$), represents the average calcium responses of V1 neurons.
*   The x-axis, (Unexpected C2 – expected C2), quantifies the prediction error related to stimulus presentation at position 2 (C2).

The caption further clarifies that the neurons included in this analysis were "V1 neurons responsive to the presented stimulus in unexpected C trials, expected C trials or both."

> Figure caption (from PDF text): Fig. 1 | Prediction errors amplify unexpected visual information. a, Structure 
of the virtual corridor and experimental design. b, Two-photon calcium imaging 
approach. c, Average calcium responses to different stimuli in corridor traversals 
with unexpected C (red, in block 1) and with expected C (blue, in late block 2).  
V1 neurons responsive to the presented stimulus in unexpected C trials, expected 
C trials or both were included. Dotted vertical lines indicate grating onsets. 
Data from 9 mice; P values from hierarchical bootstrapping test. See also 
Extended Data Fig. 2b for combined responses of all grating-responsive 
neurons. d, Average calcium responses to stimuli C4 (dark grey) and A3  
(light grey) during C trials across trials and blocks. e, Thought experiment to 
disambiguate information represented by prediction errors. f, Experimental 
design. Stimulus C was presented at position 2 (C2) or at position 3 (C3) in 5% of 
trials each in block 1. g, Average calcium responses to unexpected (red) and


### Overall Layout & Structure
The image consists of a single two-dimensional scatter plot. The axes are clearly labeled, and the data points are plotted against each other.

### Visual Components & Symbols
*   **Data Points:** The plot contains numerous small, circular data points. These points are clustered in the lower-left quadrant and spread out towards the upper-right, forming a general positive correlation trend.
*   **Trend Line:** A dashed line is overlaid on the scatter plot, indicating a positive linear trend across the data points.

### Labels, Keys & Legends
*   **Title:** The plot is titled "Response."
*   **Y-Axis Label:** The vertical axis is labeled "(z-scored $\Delta F/F$)."
*   **X-Axis Label:** The horizontal axis is labeled "Unexpected C2."
*   **Statistical Annotations (within the plot area):** Several statistical metrics are provided near the center-right of the plot:
    *   $n = 533$
    *   $r = 0.91$
    *   $P = 1.6 \times 10^{-19}$

### Data Trends & Details
*   **Correlation:** The plot demonstrates a strong positive correlation between the two variables. As "Unexpected C2" (x-axis) increases, the "(z-scored $\Delta F/F$)" (y-axis) generally increases.
*   **Range:** The x-axis ranges from approximately 0 to 10, and the y-axis ranges from -1 (implied by the axis start) up to 10.
*   **Trend Line:** The dashed line slopes upward, visually confirming the strong positive correlation indicated by $r=0.91$.

### Contextual Caption Integration
While the caption describes multiple panels (a, b, c, d, e, f, g), this specific plot corresponds to the data presented in one of those panels (likely related to calcium responses, as indicated by $\Delta F/F$). The caption mentions:
*   "V1 neurons responsive to the presented stimulus in unexpected C trials, expected C trials or both were included."
*   The variables likely relate to the calcium responses ($\Delta F/F$) measured in V1 neurons when stimulus C is presented at position 2 (C2) under unexpected conditions.

expected (blue) stimuli C2 (top) and C3 (bottom). Data from 9 mice, P values 
from hierarchical bootstrapping test. h, Responses to unexpected stimulus C2 
plotted against responses to unexpected C3 for individual V1 layer 2/3 neurons; 
Pearson correlation. i, Difference in response strength between unexpected 
and expected C2 plotted against response strength difference between 
unexpected and expected C3 responses for individual V1 layer 2/3; Pearson 
correlation. j, Similar to e, but for a second thought experiment. Exp., expected; 
unexp., unexpected. k, Experimental design. Stimuli C or D were presented at 
position 4 (C4 and D4) in 10% of trials in different sessions. l, Same as g, but for 
stimuli C4 (top) and D4 (bottom). Data from 5 mice. m, Same as h, but for 
stimuli C4 and D4. n, Same as i, but for stimuli C4 and D4. c,d,g,l, Data are 
mean ± bootstrap 95% confidence intervals. See also Extended Data Figs. 1–3.


---

## Page 3

400  |  Nature  |  Vol 633  |  12 September 2024

Article

Neural responses to grating stimulus C strongly decreased over time 
as mice encountered the visual stimulus more often, and responses 
were asymptotic within several trials in block 2 when stimulus C was 
encountered in every trial (Fig. 1d and Extended Data Fig. 2g). This grad-
ual decrease in response cannot simply be explained by visual adapta-
tion to repetitive stimuli, as C was only presented every 448 ± 364 s 
(mean ± s.d.) in block 1, owing to the considerable length of the virtual 
corridor. Of note, responses also significantly increased when the famil-
iar stimulus A was presented at an unexpected location in the corridor 
(Extended Data Fig. 4a–d, P < 1 × 10−4), and some neurons responded 
to the omission of an expected stimulus14 (Extended Data Fig. 2e,f, 
P < 1 × 10−4 for visual stimulus omission). The elevated neural response 
to an unexpected stimulus does thus not only constitute a response to 
stimulus novelty, but also is most consistent with a prediction-error 
signal. Moreover, the gradual decrease and eventual cessation of the 
prediction-error signal after repeated exposure to the novel stimulus 
at the same location indicates that mice learned to update their spatial 
expectations about stimulus identity over time.

Nature of prediction-error signals

What information sensory prediction error signals represent is cur-
rently unclear. According to theories of predictive coding, prediction

error signals have been proposed to encode the difference between pre-
dicted and actual visual input5–8 (encoding the content of how the actual 
visual input is different from predictions). However, error responses 
could also represent a more unspecific surprise signal, encoding only 
the magnitude of the deviation without its content (also called unsigned 
prediction error9), or could enhance the representation of unpredicted 
sensory input (encoding the content of the actual input). We designed 
further experiments to disambiguate between these options. First, in 
a small subset of trials, we presented stimulus C at one of two differ-
ent locations in the corridor, at which either stimulus B (position 2) 
or stimulus A (position 3) were expected (experiment 1; Fig. 1e,f). Grat-
ing stimulus C elicited a stronger response in V1 in either location when 
it was unexpected (Fig. 1g). In these two instances the actual visual 
stimulus is the same, but the predictions are likely to be different. If 
the prediction-error signal contains information about the predicted 
stimulus and/or how the actual stimulus deviates from this prediction, 
V1 responses should differ to stimulus C at the two different locations. 
However, V1 prediction-error responses to the unexpected stimulus C 
in the two locations were notably similar (Fig. 1h,i; r = 0.91, P = 1.6 × 10−199 
and r = 0.80, P = 1.8 × 10−122 (Pearson correlation for Fig. 1h,i, respec-
tively); Extended Data Fig. 3g), indicating that—at least at the level of 
individual neurons in V1—the sensory prediction-error signal contains 
little information about how the actual input differs from predictions.

c
a

d

2 s

–5

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

–4
0
4
8
12
–4

0

4

8

12

Expected C4
(z-scored ΔF/F)

Unexpected C4 – expected C4

(z-scored ΔF/F)

n = 320
r = 0.30 
P = 3.4 × 10–8

–4

0

4

8

12

–1
0
1
–1
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

Unexpected C4 – expected C4

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
1–2 15–16
37–38
55–56

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
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
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
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
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
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
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
neurons (n = 329 cells, 9 mice) to all grating stimuli in traversals with 
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
(middle; responsive to C with selectivity < 0.6) and highly selective neurons 
(right; responsive to C with selectivity towards C, compared to B > 0.8) in late 
block 2. Data are mean responses for individual mice (n = 9), black horizontal 
bars indicate mean across mice. Two-sided signed-rank test. f, Mean calcium 
responses to stimulus C4 across all trials of highly selective (dark grey, n = 77 
cells from 9 mice) and non-selective (light grey, n = 53) grating C4-responsive 
cells in late block 2. Error bars indicate bootstrap 95% confidence intervals. See 
also Extended Data Figs. 4–6.


---

## Page 4

Nature  |  Vol 633  |  12 September 2024  |  401

Next, we tested whether the prediction-error signal represents the 
actual visual input or instead a non-specific surprise or motor-related 
signal (experiment 2; Fig. 1j,k). To this end we introduced an addi-
tional unexpected visual stimulus D that was presented at corridor 
position 4 in a subset of trials in a separate imaging session of the 
same neuronal populations (Fig. 1j,k). Both stimuli C and D evoked 
strong prediction-error responses when they were unexpected (Fig. 1l 
and Extended Data Fig. 2c,d). Neural responses to C and D should be 
similar if they simply represented a non-specific surprise signal, or 
activity related to surprise-triggered movement, such as decelera-
tion in response to an unexpected stimulus. However, most neurons 
responded strongly to only one of the two unexpected stimuli, and V1 
population responses to these stimuli were thus different and specific 
to stimulus features (Fig. 1m,n and Extended Data Fig. 5a–e). This was 
also the case when comparing prediction-error responses to two more 
similar visual stimuli (two gratings of different orientation; Extended 
Data Fig. 5l–p).

Indeed, V1 neurons that responded to an unexpected stimulus (that 
is, grating C) often also responded to the same stimulus when it was 
expected, but not to gratings A or B (Fig. 2a–c). Importantly, only 
visually driven neurons that responded highly selectively to a stimu-
lus showed amplified responses when this stimulus was unexpected 
(Fig. 2d–f; P = 0.0078 for highly selective cells), whereas more broadly 
tuned neurons that also responded to other visual stimuli did not show 
prediction-error signals (Fig. 2e,f: P = 0.82 for non-selective cells). This 
selective amplification was equally evident in the V1 responses to a dif-
ferent unexpected stimulus (stimulus D; Extended Data Fig. 6a–h), and 
could not be explained by differences in response strength between 
selective and non-selective neurons (Extended Data Fig. 6i,j). Nota-
bly, increased V1 activity in response to a familiar stimulus (A) at an 
unexpected location was also restricted to those visually responsive 
neurons selective for the presented stimulus (Extended Data Fig. 4e,f), 
indicating that selective amplification of visual information that is 
unexpected may be a general feature of sensory prediction-error 
signals in V1.

In addition to visually driven neurons, a subset of non-visually 
responsive neurons was also recruited by prediction errors (Fig. 2a and 
Extended Data Fig. 4i). Responses of these neurons were nevertheless 
highly stimulus-selective, and restricted to specific unexpected stimuli 
(Extended Data Fig. 5f–k). Neurons responding to the unexpected omis-
sion of a stimulus constituted an additional V1 population, which was 
not activated when the omitted stimulus was instead replaced by a dif-
ferent, unexpected stimulus (Extended Data Fig. 5q–z). This indicates 
that negative prediction errors (responses to the unexpected absence 
of a stimulus or event10,14) are not significantly contributing to the V1 
prediction-error signal in response to a novel, unexpected stimulus.

Together, these experiments indicate that the prediction-error 
signal evoked in layer 2/3 of V1 by unexpected visual stimuli is not a 
non-specific surprise or a difference signal about how the visual input 
deviates from the animal’s predictions. Instead, prediction error sig-
nals are specific to the features of the unexpected visual input and 
amplify the activity of neurons that respond highly selectively to the 
unexpected visual features, thereby selectively increasing the salience 
of unpredicted—and therefore potentially most relevant—sensory 
information.

Circuits mediating V1 prediction-error signals

We next examined the circuit mechanisms by which sensory predic-
tion error signals are implemented in V1 networks. VIP inhibitory 
interneurons in V1 receive cortical top-down and neuromodulatory 
inputs, and can disinhibit local principal cells through prominent 
inhibitory connections onto somatostatin-expressing (SOM) inhibi-
tory interneurons24–28, providing a circuit for top-down gain modulation 
of sensory responses29,30. VIP cells have also been shown to respond

strongly to novel, but not familiar, visual stimuli20,23. To assess whether 
VIP interneuron activity is important for prediction-error signals in V1, 
we first examined how VIP interneurons respond to unexpected and 
expected visual information by using the experimental paradigms 
described in Fig. 1k (Fig. 3a). VIP interneurons were suppressed by 
expected visual stimuli, but strongly responded to unexpected visual 
stimuli (Fig. 3b–d and Extended Data Fig. 7a,b), consistent with previous 
studies15,20,23. VIP neurons also responded to familiar stimuli encoun-
tered at an unexpected location (Extended Data Fig. 8a–d), showing that 
they are not only activated by novel stimuli, but also by sensory predic-
tion errors more generally. Prediction-error responses of VIP neurons 
were much less selective than those of putative excitatory neurons in 
V1: many VIP neurons responded to both unexpected stimuli C and D 
(Extended Data Fig. 7c–e). Responses of VIP interneurons decreased 
over time as mice encountered the same stimulus more often, in par-
allel with the gradual cessation of the prediction-error signal in the 
layer 2/3 network (Fig. 3d; see also Fig. 1d), suggesting that the recruit-
ment of VIP interneurons may be causally related to the generation of 
prediction-error signals in V1.

To test whether the recruitment of VIP interneurons is required for 
the prediction-error signal in the general V1 population, we optoge-
netically silenced VIP interneurons as mice encountered expected 
or unexpected visual stimuli while recording calcium responses of 
V1 layer 2/3 neurons (Fig. 3e–g and Methods). This manipulation was 
highly effective as VIP neurons were fully inactivated during light 
stimulation (Extended Data Fig. 9a–c). Inactivating VIP neurons sig-
nificantly reduced the responses of V1 layer 2/3 cells to unexpected 
visual stimuli (Fig. 3f, middle, P < 1 × 10−4; Extended Data Fig. 10a–h), 
whereas it had no effect on responses to expected visual stimuli A 
and B (Fig. 3f, left; P = 0.24), consistent with the specific recruitment 
of VIP interneurons by unexpected sensory stimuli (Fig. 3a–d). Fur-
thermore, the effect of VIP inactivation on individual V1 layer 2/3 cells 
could not be explained by light artefacts (Extended Data Fig. 9g,h), 
and it was not uniform, but highly correlated with how strongly V1 
neurons were facilitated by prediction errors, much more so than 
with their visual response strength: neurons with the strongest 
prediction-error signal were the ones that were most suppressed by 
VIP interneuron inactivation (Fig. 3g and Extended Data Fig. 10c,e,f). 
V1 prediction-error signals in response to familiar stimulus A at an 
unexpected location were also abolished when VIP neurons were inac-
tivated (Extended Data Fig. 8e,f), demonstrating that the recruitment 
of VIP neurons is required more generally for prediction-error sig-
nals in layer 2/3 of V1, rather than specifically for V1 signals related to 
stimulus novelty.

We next explored the identity of the long-range inputs to V1 that 
could mediate the activation of VIP neurons by prediction errors. The 
pulvinar is a higher-order visual area in thalamus, also called lateral 
posterior nucleus in mice, that integrates information from many corti-
cal and subcortical areas and sends prominent feedback projections 
to V131–36. Notably, pulvinar projections to V1 carry information about 
visual input that is not predicted by the animal’s own actions, indicat-
ing that the pulvinar conveys sensory–motor prediction errors to V131. 
To test whether pulvinar projections to V1 also signal prediction 
errors arising from spatial predictions of visual input in our task, we 
used two-photon imaging to record calcium signals from pulvinar 
axons in V131. Calcium activity of pulvinar axons was strongly and 
non-selectively boosted when a visual stimulus was unexpected 
(Fig. 3h–k and Extended Data Fig. 7h–n), and this prediction-error 
response decreased with repeated exposure to the same stimulus, with 
a time course similar to responses in V1 neurons (Fig. 3k). Pulvinar axons 
were also activated by a familiar stimulus at an unexpected location 
(Extended Data Fig. 8g–i).

To determine whether pulvinar input to V1 is required for 
prediction-error signals in V1 neurons, we optogenetically inacti-
vated pulvinar axons in V1 while recording calcium responses of V1


---

## Page 5

402  |  Nature  |  Vol 633  |  12 September 2024

Article

layer 2/3 neurons (Fig. 3l–n). This manipulation—light stimulation of 
eNpHR3.0-expressing pulvinar axons in V1—reduced activity of pulvinar 
axons, but had only a partial effect (Extended Data Fig. 9d–f). Neverthe-
less, suppressing pulvinar input to V1 specifically reduced the responses 
of V1 layer 2/3 neurons to unexpected visual stimuli (Fig. 3m, middle,

P < 1 × 10−4, and Extended Data Fig. 10i–p), but not to expected stimuli 
(Fig. 3m, P = 0.074 and P = 0.088 for visual stimuli A and B, and expected 
C and D, respectively). Similar to the effect of VIP neuron silencing, V1 
neurons with strong prediction-error responses were more likely to be 
strongly suppressed by pulvinar inactivation (Fig. 3n and Extended Data

i

Pulvinar bouton no.

900

1

1,078

1

C session
D session

–1

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

1–2 9–10
29–30
47–48

0
5
10
15
–6

–4

–2

0

2

n = 528

r = –0.50
P = 1.2 × 10–34

Unexpected C4 or D4 – expected C4 or D4

(LED off, z-scored ΔF/F)

LED on – LED off

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
–6

–4

–2

0

2

Unexpected C4 or D4 – expected C4 or D4

(LED off, z-scored ΔF/F)

LED on – LED off

(unexpected C4 or D4,

z-scored ΔF/F)

r  = –0.78
P = 9.3 × 10–120

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

–2

0

2
1

403

1

C session
D session

–0.2

0

1

1–2 15–16
37–38
55–56
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

–0.2

0

0.6

Visual stimulus response

(z-scored ΔF/F)

Visual stimulus response

(z-scored ΔF/F)

P < 10–4 P < 10–4

P < 10–4 P < 10–4

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
Cohen’s d = 0.13

n = 528
P < 10–4

Cohen’s d = 0.36

n = 158
P = 0.074
Cohen’s d = –0.15

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
P < 10–4

n = 223
P = 2 × 10–4

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



**1. Overall Layout & Structure:**
The figure consists of a single plot area with two primary data series plotted against a shared x-axis representing time intervals and a y-axis representing a measured value (likely a rate or magnitude). The plot is segmented by two distinct, vertically shaded background regions.

**2. Visual Components & Symbols:**
*   **Data Series 1 (C4 or D4):** Represented by dark gray circular markers connected by a solid line. This series shows fluctuations over the measured intervals.
*   **Data Series 2 (Same-trial average):** Represented by open white circular markers connected by a solid line. This series remains consistently low across all intervals shown.
*   **Shaded Regions:** There are two vertical shaded bands:
    *   A light reddish-pink band covering the intervals 1–2 and extending slightly into 15–16.
    *   A light blue-gray band covering the intervals 37–38 and extending through 55–56.

**3. Labels, Keys & Legends:**
*   **Legend:** The legend in the upper right corner identifies the two data series:
    *   "C4 or D4" corresponds to the dark gray line/markers.
    *   "Same-trial average (A1 B2 A3)" corresponds to the open white line/markers.
*   **X-Axis Labels:** The x-axis displays discrete time intervals: "1–2", "15–16", "37–38", and "55–56".
*   **Y-Axis Labels:** The y-axis is labeled with numerical values, ranging from 0.0 to 0.2 (with tick marks at intervals of 0.1).

**4. Data Trends & Details:**
*   **Y-Axis Range:** The vertical axis ranges from 0.0 to 0.2, with major ticks at 0.0, 0.1, and 0.2.
*   **C4 or D4 Trend:** This series starts high in the 1–2 interval (near 0.2), shows a rapid decline through the 15–16 interval, reaching values near or below 0.1. It then exhibits a low baseline during the 37–38 interval, followed by slight fluctuations around zero in the 55–56 interval.
*   **Same-trial average Trend:** This series remains consistently low, hovering just above the 0.0 line across all intervals shown.
*   **Shaded Region Effects:** The C4 or D4 data shows a significant initial high activity within the reddish-pink shaded region (1–2). The blue-gray shaded region (37–56) corresponds to a period where the C4 or D4 activity is generally low, near baseline.

**5. Contextual Caption Integration:**
The legend explicitly defines the data series: "C4 or D4" represents one measured variable, while "Same-trial average (A1 B2 A3)" represents the average across specific trial components (A1, B2, and A3). The shaded regions delineate distinct experimental phases relevant to the interpretation of these measured variables.

–0.05

0

0.2

Visual stimulus response

(z-scored ΔF/F)

Visual stimulus response

(z-scored ΔF/F)

P < 10–4 P < 10–4

C session
D session

P = 2 × 10–4
P = 6 × 10–4

(z-scored
ΔF/F)



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
cells in V1 layer 2/3 was recorded during the experiment depicted in Fig. 1k.  
b, Single-cell responses for all VIP cells (individual rows) in the session with 
unexpected stimulus C (top; C session, n = 350 cells from 7 mice) and with 
unexpected stimulus D (bottom; D session, n = 403 cells from 7 mice) to 
expected B4 (left), unexpected C4 or D4 (middle; block 1) and expected C4 or 
D4 (right; late block 2), sorted by response strength to unexpected C4 or D4.  
c, Cell- and trial-averaged stimulus responses of all VIP cells in b. P values from 
hierarchical bootstrapping test with Bonferroni correction. d, Average calcium 
responses of all VIP cells to grating stimulus C4 or D4 (dark grey) and other 
gratings in the same trial (average of A1, B2 and A3, light grey) over time.  
e, Experimental design. Calcium activity of V1 layer 2/3 cells was recorded while 
VIP cells were optogenetically silenced during visual stimulus presentation.

> Figure caption (from PDF text): Fig. 3 | Activity of VIP interneurons and pulvinar input is required for V1 
prediction-error signals. a, Experimental design. Calcium activity of VIP  
cells in V1 layer 2/3 was recorded during the experiment depicted in Fig. 1k.  
b, Single-cell responses for all VIP cells (individual rows) in the session with 
unexpected stimulus C (top; C session, n = 350 cells from 7 mice) and with 
unexpected stimulus D (bottom; D session, n = 403 cells from 7 mice) to 
expected B4 (left), unexpected C4 or D4 (middle; block 1) and expected C4 or 
D4 (right; late block 2), sorted by response strength to unexpected C4 or D4.  
c, Cell- and trial-averaged stimulus responses of all VIP cells in b. P values from 
hierarchical bootstrapping test with Bonferroni correction. d, Average calcium 
responses of all VIP cells to grating stimulus C4 or D4 (dark grey) and other 
gratings in the same trial (average of A1, B2 and A3, light grey) over time.  
e, Experimental design. Calcium activity of V1 layer 2/3 cells was recorded while 
VIP cells were optogenetically silenced during visual stimulus presentation.


### Panel 1 (Left Plot)

This panel features two main graphical elements: a time-course plot at the top and a scatter plot below it.

**Top Plot (Time Course):**
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)", ranging from approximately 0 to 15.
*   **X-axis:** Not explicitly labeled with units, but represents time progression.
*   **Curves:** Two overlaid curves are present:
    *   A dark line (representing one condition, likely LED off).
    *   An orange/yellow line (representing the other condition, likely LED on).
*   **Trend:** Both curves show a transient increase in $\Delta F/F$ peaking around the middle of the plotted time window, followed by a return toward baseline.
*   **Annotation:** A bracket spans across the peak activity region, with an associated statistical annotation: "$n = 158$", "$P = 0.074$", and "Cohen's $d = -0.15$".

**Bottom Plot (Scatter Plot):**
*   This plot compares the response magnitude from the top time-course data.
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)".
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)".
*   **Data Points:** Numerous black circles are scattered across the plot. The data points generally cluster around the diagonal line, indicating a correlation between the responses under different conditions (though the specific comparison is implied by the context).

### Panel 2 (Middle Plot)

This panel also features a time-course plot at the top and a scatter plot below it.

**Top Plot (Time Course):**
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)", ranging from approximately 0 to 15.
*   **X-axis:** Represents time progression.
*   **Curves:** Two overlaid curves are present:
    *   A dark line (representing one condition).
    *   An orange/yellow line (representing the other condition).
*   **Trend:** Both curves show a clear, transient increase in $\Delta F/F$ peaking around the middle of the plotted time window.
*   **Annotation:** A bracket spans across the peak activity region, with an associated statistical annotation: "$n = 528$", "$P < 10^{-4}$", and "Cohen's $d = 0.36$".

**Bottom Plot (Scatter Plot):**
*   This plot compares the response magnitude.
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)".
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)".
*   **Data Points:** Numerous black circles are scattered across the plot. The data points show a clear positive correlation, trending upwards from the bottom-left to the top-right.

### Panel 3 (Right Plot)

This panel mirrors the structure of the first two, featuring a time-course plot at the top and a scatter plot below it.

**Top Plot (Time Course):**
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)", ranging from approximately 0 to 15.
*   **X-axis:** Represents time progression.
*   **Curves:** Two overlaid curves are present:
    *   A dark line (representing one condition).
    *   An orange/yellow line (representing the other condition).
*   **Trend:** Both curves show a transient increase in $\Delta F/F$ peaking around the middle of the plotted time window.
*   **Annotation:** A bracket spans across the peak activity region, with an associated statistical annotation: "$n = 186$", "$P = 0.088$", and "Cohen's $d = 0.13$".

**Bottom Plot (Scatter Plot):**
*   This plot compares the response magnitude.
*   **Y-axis:** Labeled "(z-scored $\Delta F/F$)".
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)".
*   **Data Points:** Numerous black circles are scattered across the plot, showing a general positive trend.

### General Observations (Legend/Key)
The legend provided in the top right corner of the figure indicates:
*   **Black line:** LED off
*   **Orange/Yellow line:** LED on

The caption contextually identifies the data as relating to "Calcium activity of VIP cells in V1 layer 2/3" and the comparison involves responses to "unexpected stimulus C4 or D4."

f, Top, cell- and trial-averaged responses of V1 neurons significantly responsive 
to the presented visual stimuli with (amber) or without (black) VIP silencing. 
Bottom, responses of individual neurons to the visual stimulus indicated above 
during VIP cell silencing (LED on), plotted against responses to the same 
stimulus in control trials (LED off). P values from hierarchical bootstrapping 
test, from 9 mice. g, Effect of VIP neuron silencing (LED on − LED off during 
unexpected stimulus C4 or D4) plotted against the strength of prediction-error 
signals (response to unexpected C4 or D4 − response to expected C4 or D4); 
Pearson correlation. h–k, Same as a–d, but for calcium responses of pulvinar 
axonal boutons in V1 layer 1. l–n, Same as e–g, but the activity of V1 layer 2/3 
cells was recorded while pulvinar axons in V1 were optogenetically silenced. 
c,d,f,j,k,m, Data are mean ± bootstrap 95% confidence intervals (shading or 
error bars). See also Extended Data Figs. 7–10.


---

## Page 6

Nature  |  Vol 633  |  12 September 2024  |  403

Fig. 10k,m), independent of their visual response strength (Extended 
Data Fig. 10n). Moreover, pulvinar input was also required for V1 
prediction-error responses to a familiar stimulus at an unexpected 
location (Extended Data Fig. 8j,k). Together, these cell-type-specific

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

–1
0
1

A
B
Selective to

–4

0

4

8

LED on – LED off

(z-scored ΔF/F)

–4

0

4

8

LED on – LED off

(z-scored ΔF/F)

–4

0

4

8

LED on – LED off

(z-scored ΔF/F)

–4

0

4

8

LED on – LED off

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
P < 10–4

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

–1
0
1
Selectivity (LED off)

–1
0
1
Selectivity (LED off)

–1
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
P = 2.0 × 10–4

LED



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
a, Experimental design. After training in the virtual corridor (stimuli A–B–A–B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response

> Figure caption (from PDF text): Fig. 4 | Neocortical disinhibition and pulvinar input act synergistically.  
a, Experimental design. After training in the virtual corridor (stimuli A–B–A–B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response


### 1. Overall Layout & Structure
The figure consists primarily of a single, large scatter plot with overlaid mean lines and confidence intervals. The x-axis categorizes neurons based on their response selectivity, while the y-axis quantifies a measure of neural activity change ($\Delta$). The plot is divided into three distinct groups along the x-axis: "Responsive to A not B," "Non-selective," and "Highly selective."

### 2. Visual Components & Symbols
*   **Data Points:** Individual data points (dots) represent the measured response for individual V1 neurons.
*   **Mean/Intervals:** Horizontal lines with shaded regions above the data points represent the mean response and the 95% bootstrap confidence intervals for each group.
*   **Statistical Annotations:** $P$-values are displayed above the groups to indicate statistical significance between comparisons.
*   **Lines:** Thin lines connect individual data points across the groups, suggesting a comparison of the same neurons or related metrics across selectivity levels.

### 3. Labels, Keys & Legends
**Axes Labels:**
*   **Y-axis:** Labeled as "$\Delta$ (score $\Delta$)".
*   **X-axis Categories:** Labeled as "Responsive to A not B," "Non-selective," and "Highly selective."

**Annotations:**
*   $P = 0.22$: Placed above the "Responsive to A not B" group, indicating a statistical comparison.
*   $P = 0.63$: Placed above the "Non-selective" group, indicating a statistical comparison.
*   $P = 0.031$: Placed above the "Highly selective" group, indicating a statistical comparison.

**Inset:**
There is an inset plot visible in the upper right corner, which shows a "calcium response." This inset contains individual traces (lines) and shaded regions, suggesting it displays the raw calcium activity data mentioned in the caption.

### 4. Data Trends & Details
The plot compares three distinct groups of V1 neurons:

*   **Responsive to A not B:** The data points are clustered very close to the zero line on the y-axis. The mean response appears near 0, and the associated $P$-value is $0.22$.
*   **Non-selective:** The data points show a slight upward trend compared to the first group. The mean response is slightly positive, and the associated $P$-value is $0.63$.
*   **Highly selective:** This group shows the highest level of activity change ($\Delta$). The data points are significantly higher than in the other two groups. The mean response is substantially positive, and the associated $P$-value is $0.031$, indicating a statistically significant difference compared to the other groups (implied by the placement of the $P$-value).

The lines connecting points suggest that as selectivity increases (moving from left to right), the mean $\Delta$ score generally increases, with a marked jump in the "Highly selective" category.

### 5. Contextual Caption Integration
The caption identifies this figure as relating to "Neocortical disinhibition and pulvinar input act synergistically."
*   The data likely represents the "effect of optogenetic stimulation (difference of response to grating B2 with and without LED stimulation)" plotted against "response selectivity" of individual V1 neurons.
*   The comparison between the three groups ("Responsive to A not B," "Non-selective," and "Highly selective") corresponds directly to the neuronal response selectivity mentioned in the caption.
*   The inset showing "calcium response" relates to the underlying physiological measurement of V1 neuron activity.

> Figure caption (from PDF text): Fig. 4 | Neocortical disinhibition and pulvinar input act synergistically.  
a, Experimental design. After training in the virtual corridor (stimuli A–B–A–B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response


**Overall Layout & Structure:**
The figure consists primarily of a single, large scatter plot occupying the main visual area. The caption indicates that this panel (likely corresponding to part of a larger figure structure, though only one plot is visible here) plots the "effect of optogenetic stimulation" against "response selectivity."

**Visual Components & Symbols:**
*   **Data Points:** Numerous small, circular data points are scattered across the plot area. These represent individual V1 neurons.
*   **Axes:** The plot has a horizontal (x-axis) and vertical (y-axis).
*   **Shaded Region:** A light gray shaded rectangular region is present on the right side of the plot, indicating a specific range or threshold.

**Labels, Keys & Legends:**
*   **X-axis Label:** "Selectivity (LED off)"
*   **Y-axis Label:** The y-axis label is partially visible but appears to relate to the magnitude of a response or effect.
*   **Data Count Annotation:** Below the plot, there is an annotation: "$n = 423$".

**Data Trends & Details:**
*   **X-axis Range:** The x-axis ranges approximately from -1 to 1.
*   **Y-axis Range:** The y-axis ranges from -4 to 8.
*   **Data Distribution:** Most data points are clustered near the origin (around $x=0, y \approx 0$).
*   **Trend:** There is a clear positive correlation visible in the data points as they move towards the right side of the plot (higher selectivity). As the x-value increases toward 1, the y-values tend to increase significantly.
*   **Shaded Region:** The gray shaded region is located where the x-values are close to 1 (specifically, around $x \approx 0.8$ to $x=1$) and the y-values are high (above $\approx 2$).

**Contextual Caption Integration:**
The caption identifies this plot as showing the "effect of optogenetic stimulation (difference of response to grating B2 with and without LED stimulation) plotted against response selectivity (Methods) of individual V1 neurons."
*   The **X-axis ("Selectivity (LED off)")** represents the response selectivity of individual V1 neurons.
*   The **Y-axis (implied)** represents the magnitude of the effect of optogenetic stimulation.
*   The annotation $n=423$ indicates that 423 individual neurons were analyzed for this plot.

> Figure caption (from PDF text): Fig. 4 | Neocortical disinhibition and pulvinar input act synergistically.  
a, Experimental design. After training in the virtual corridor (stimuli A–B–A–B), 
optogenetic manipulation was paired with grating B2 in 50% of trials. b, Left, 
the activity of V1 layer 2/3 cells was recorded while pulvinar axons were 
optogenetically stimulated. Stimulation started 0.1 s after grating onset and 
lasted for 1 s. Second column, responses of individual V1 neurons with and 
without pulvinar axonal stimulation (LED on versus LED off). n = 118 grating  
A or B responsive cells from 6 mice, Hierarchical bootstrapping test. Inset, 
cell-averaged calcium responses with (amber) or without (black) optogenetic 
stimulation. Lines and shaded regions are mean and bootstrap 95% confidence 
intervals. Third column, effect of optogenetic stimulation (difference of 
response to grating B2 with and without LED stimulation) plotted against 
response selectivity (Methods) of individual V1 neurons. Right, calcium response


### Overall Layout & Structure
The figure is structured into several distinct visual components, though the provided image snippet focuses heavily on a scatter plot and an inset line graph. The caption suggests the figure contains multiple parts (a, b, third column, right), but the visible portion is dominated by a scatter plot on the left and an inset graph in the upper right.

### Visual Components & Symbols
**Main Plot (Scatter Plot):**
*   The main plot is a two-dimensional scatter graph.
*   The x-axis represents "LED off (z-scored $\Delta F/F$)" and ranges from approximately -1 to 8.
*   The y-axis represents "1 z-scored $\Delta F/F$" and ranges from 0 to 8.
*   Numerous small, black circular data points are scattered across the plot area. A dense cluster of these points is visible near the origin (low values on both axes).
*   A dashed gray line originates from the lower-left corner and slopes upward toward the upper right, indicating a correlation or threshold relationship.

**Inset Graph (Upper Right):**
*   This is a line graph embedded in the upper right corner.
*   The x-axis scale bar indicates "2 s".
*   The y-axis is not explicitly labeled in the visible area but represents calcium response magnitude.
*   Two distinct lines are plotted: one colored **amber** and another colored **black**.
*   The amber line shows a rapid rise, peaking around the center of the visible time frame, followed by a decay.
*   The black line follows a similar trajectory but appears slightly lower or delayed compared to the amber line.
*   A shaded region surrounds both lines, representing a 95% confidence interval (as per the caption).

### Labels, Keys & Legends
**Axes and Annotations:**
*   X-axis label: "LED off (z-scored $\Delta F/F$)"
*   Y-axis label: "1 z-scored $\Delta F/F$" (The full label is truncated but implied by the context).
*   Annotation near the scatter plot: "$n = 423$" and "$P < 10^{-4}$".
*   A vertical dashed line is present in the upper right quadrant of the main plot, near $x \approx 4$.

**Inset Graph Labels:**
*   The caption clarifies that the inset shows "cell-averaged calcium responses with (amber) or without (black) optogenetic stimulation."
*   The caption also mentions "Lines and shaded regions are mean and bootstrap 95% confidence intervals."

### Data Trends & Details
**Scatter Plot Trend:**
*   The scatter plot shows a distribution of individual neuron responses. The presence of the dashed line suggests that neurons exhibiting higher activity when LED is off (positive x-values) might correlate with a specific level of response magnitude on the y-axis.
*   The statistical notation ($n=423, P < 10^{-4}$) indicates a statistically significant relationship or finding derived from the data set.

**Inset Graph Trend:**
*   The inset graph demonstrates a transient calcium response over time (2 seconds). The comparison between the amber line (with stimulation) and the black line (without stimulation) allows for a visual assessment of the effect of optogenetic manipulation on the calcium trace. The amber line shows a higher peak response compared to the black line, consistent with the caption's description of stimulation effects.

### Contextual Caption Integration
The caption identifies the context: "Neocortical disinhibition and pulvinar input act synergistically."
*   The scatter plot likely plots the effect of stimulation (related to pulvinar input) against a baseline response measure.
*   The inset graph directly illustrates the calcium responses of V1 layer 2/3 cells, comparing responses *with* (amber) and *without* (black) pulvinar axonal stimulation.
*   The caption specifies that the data comes from "grating A or B responsive cells from 6 mice."

strength to stimulus B2 of neurons selective to A (left), and non-selective 
(selectivity B versus A < 0.6, middle) and highly selective (selectivity B versus 
A > 0.8, right) grating B2 responsive cells in V1 layer 2/3 with (amber) or without 
(grey) optogenetic stimulation. P values from two-sided signed-rank test. Data 
points depict mean responses for individual imaging sessions; n = 6 mice; black 
horizontal bars indicate mean across animals. c, Same as b, but the activity of 
V1 layer 2/3 cells was recorded while VIP cells were optogenetically stimulated. 
n = 6 mice. d, Same as b, but the activity of V1 layer 2/3 cells was recorded while 
pulvinar axons and VIP cells were optogenetically stimulated simultaneously. 
n = 9 mice. e, Same as b, but the activity of V1 layer 2/3 cells was recorded while 
pulvinar axons and SOM cells were optogenetically co-manipulated for 3 s 
starting at grating stimulus onset. n = 6 sessions from 4 mice. See also 
Extended Data Fig. 11.


---

## Page 7

404  |  Nature  |  Vol 633  |  12 September 2024

Article

Cooperative thalamocortical circuit

Pulvinar axons make synaptic connections onto VIP neurons in the 
neocortex30. A plausible scenario for how the pulvinar and neocortical 
VIP neurons interact to mediate prediction-error signals may therefore 
involve pulvinar input activating VIP neurons in V1, which in turn boost 
pyramidal neuron responses to unexpected visual stimuli through the 
VIP–SOM disinhibitory circuit24–26,28. To directly test this hypothesis, 
we optogenetically stimulated either pulvinar axons or VIP interneu-
rons in V1 while monitoring neural responses of V1 layer 2/3 neurons 
to the expected grating stimuli in the virtual corridor (Fig. 4a–c; see 
also Extended Data Fig. 11). Consistent with a previous report37, stimu-
lating pulvinar axons broadly suppressed responses to visual stimuli 
in V1 (Fig. 4b, P = 2.0 × 10−4). Moreover, stimulating pulvinar axons 
excited only a small subset of VIP neurons, and decreased VIP neuron 
prediction-error responses (Extended Data Fig. 12a–f). Optogenetically 
stimulating VIP interneurons had a minor effect on V1 activity, with 
a non-significant trend towards facilitating visual responses, unlike 
the strong amplification of stimulus-selective V1 neurons by predic-
tion errors (Fig. 4c; P = 0.18). Remarkably, simultaneous co-activation 
of both pulvinar axons and VIP neurons strongly facilitated visual 
responses of a subset of V1 neurons (Fig. 4d, P = 0.020), indicating that 
pulvinar input and VIP neurons act synergistically, not additively. More-
over, response facilitation was specific to those visually driven neurons 
that responded highly selectively to the visual stimulus that was paired 
with optogenetic stimulation, mimicking the prediction-error signal in 
V1 (Fig. 4d, P = 0.039; Extended Data Fig. 11f–i; compared to Fig. 2d,e). 
Our experimental evidence therefore does not support a direct path-
way from pulvinar inputs onto VIP neurons to facilitate V1 responses, 
but pulvinar and VIP neurons are likely to be recruited independently, 
and act synergistically to provide stimulus-selective amplification of 
responses to unexpected stimuli in V1.

Our results indicate that when VIP neurons are activated, they can 
counteract the inhibitory influence pulvinar activation has on the V1 
network. The main synaptic targets of VIP neurons are SOM interneu-
rons that inhibit the apical dendrites of pyramidal cells24–26,28. VIP neu-
rons can therefore disinhibit pyramidal cells via the inhibition of SOM 
neurons. We hypothesized that pulvinar activation may recruit SOM 
neurons whose inhibitory influence on the V1 network may be allevi-
ated when VIP neurons are simultaneously active. If this were the case, 
silencing SOM neurons while activating pulvinar should have effects 
similar to VIP neuron and pulvinar co-activation. Indeed, simultaneous 
optogenetic stimulation of pulvinar axons and inactivation of SOM 
neurons in V1 completely abolished the pulvinar-driven suppression of 
V1 activity (Fig. 4e; compared to Fig. 4b). Remarkably, this manipulation 
also strongly and specifically facilitated visual responses of V1 neurons 
responding highly selectively to the visual stimulus paired with the 
optogenetic manipulation, again mimicking the V1 prediction-error 
signal (Fig. 4e, P = 0.031), and suggesting that the pulvinar’s excita-
tory drive onto V1 pyramidal neurons is accompanied by a strong 
feed-forward inhibitory drive via SOM neurons.

Although higher-order sensory thalamocortical pathways do not 
prominently target cortical SOM neurons37–39, at least a subset of SOM 
neurons in V1 has been shown to receive input from the pulvinar30,40,41. 
We imaged responses of V1 layer 2/3 SOM neurons while optogeneti-
cally stimulating pulvinar axons in V1, and found that although most 
SOM neurons were either not affected or even suppressed, a subset of 
SOM neurons (16 ± 9%; mean ± s.d.) was strongly activated by pulvinar 
stimulation (Fig. 5a–c and Extended Data Fig. 12g,h). Notably, SOM 
neurons that were recruited by pulvinar stimulation were suppressed 
by unexpected visual input, suggesting that this subset of SOM neurons 
is inhibited by VIP neurons28 (Fig. 5d,e). By contrast, layer 2/3 SOM 
neurons that are not recruited by pulvinar stimulation were activated 
by unexpected visual stimuli, similar to VIP neurons, suggesting that

they do not receive strong inhibition from VIP neurons and/or are more 
strongly driven by the local excitatory layer 2/3 network (Fig. 5d,e), 
consistent with previous studies28,42,43. Together, these results show 
that excitatory drive from the pulvinar onto V1 pyramidal neurons is 
paralleled by a powerful inhibitory pathway via a specific subpopula-
tion of SOM neurons. When VIP neurons are active simultaneously with 
pulvinar input they inhibit SOM neurons, thus reducing feed-forward 
inhibition from pulvinar to V1, and enabling pulvinar drive to strongly 
activate a subset of layer 2/3 pyramidal cells (Fig. 5f). These results 
therefore reveal a circuit driving V1 prediction-error signals through 
synergistic interactions of pulvinar inputs and VIP neurons.

Discussion

Here we describe a mechanism for boosting sensory responses by 
prediction errors in V1 when animals’ expectations of visual stimuli 
at specific locations of a virtual environment are violated. Prediction 
errors selectively amplify the representation of unexpected visual 
input, via synergistic interactions of higher-order thalamic input and 
local VIP–SOM disinhibitory circuits in V1.

Prediction-error responses are dependent on VIP neuron activity 
as well as input from the pulvinar, a higher-order visual nucleus in the 
thalamus that has previously been implicated in predictive process-
ing, and conveys prediction-error signals to V131,32,44. Co-activation 
of pulvinar axons and VIP neurons in V1 can reproduce the selective 
amplification of V1 neurons even in the absence of prediction errors. 
Notably, we found that pulvinar input to V1 is gated by VIP–SOM inhibi-
tory interactions. The pulvinar suppresses the activity of V1 cells via a 
subpopulation of SOM neurons. To allow pulvinar input to amplify V1 
responses, this inhibition has to be alleviated by activity in VIP neu-
rons that inhibit SOM neuron responses (Fig. 5f). This mechanism 
may explain seemingly contradictory findings about how the pulvi-
nar affects cortical activity37,45 and establishes VIP neurons as a gate 
for higher-order thalamic input to V1. VIP neurons receive prominent 
neuromodulatory and top-down cortical input, and have been shown 
to be activated by salient events such as reward, punishment and novel 
stimuli20,23,24,26,27,29,30,46–48. They can therefore regulate the influence of 
pulvinar input on visual processing in V1, depending on the relevance 
of visual stimuli or the animal’s behavioural state. As VIP–SOM disin-
hibitory circuits and higher-order thalamic feedback input are present 
throughout the cortical hierarchy24–26,28,30,34,47, this cooperative circuit 
mechanism may serve as a common computational motif in neocorti-
cal networks.

Although VIP neurons and pulvinar inputs to V1 are broadly recruited 
by unexpected stimuli (Extended Data Fig. 7), prediction-error sig-
nals in V1 are observed only in subpopulations of neurons that are 
highly selective for the visual stimulus encountered. Our results 
point to a potential circuit mechanism for this selective response 
amplification in V1. We reproduced the selective amplification of 
only stimulus-selective V1 neurons by co-activating VIP neurons 
with pulvinar input to V1, but also when bypassing VIP activation by 
silencing SOM neurons while stimulating pulvinar input (Fig. 4d,e). 
Thus, selectivity of response amplification in V1 neurons does not 
depend on VIP neuron recruitment or the activity of SOM neurons, 
but rather on pulvinar input more effectively driving V1 neurons with 
sharp tuning. This suggests a selective influence of pulvinar on sub-
populations of stimulus-selective V1 neurons, balanced by inhibition 
from pulvinar-driven SOM neurons (Extended Data Fig. 11j–m). This 
pulvinar-dependent response enhancement may be further amplified 
via recurrent excitation within subnetworks of selective V1 neurons 
tuned to the same stimulus49 and lateral suppression of the rest of the 
network via parvalbumin-expressing neurons50–52, collectively leading 
to selective amplification of unexpected input.

Which inputs drive pulvinar and VIP neurons, and what informa-
tion do they convey? Visual prediction errors are derived through


---

## Page 8

Nature  |  Vol 633  |  12 September 2024  |  405

a comparison of the actual visual input with internal predictions of 
expected visual input. Several top-down pathways have been proposed 
to convey different types of stimulus predictions to V1, including higher 
visual areas and anterior cingulate cortex6,14,53. In our paradigm, pre-
diction errors may arise from violations of spatial predictions of the 
expected visual scene at a given location. Such spatio-visual predictions 
necessitate neural representations of space and spatial memory, and 
are thus likely to originate from hippocampus or related areas such as 
the retrosplenial cortex54,55. Previous studies have proposed that visual 
prediction errors may be computed in V16,14,53. We observed sensory 
prediction-error signals not only in V1, but also in the pulvinar, and V1 
prediction errors were dependent on pulvinar input. Prediction-error 
signals may therefore be computed outside of these visual areas—for 
instance, within the hippocampal formation—and conveyed to V1 by 
top-down projections via pulvinar and local VIP interneurons. Alter-
natively, errors could be computed in the pulvinar or in V1 from the 
comparison of visual input with spatio-visual predictions5–10,14, and 
could then be amplified through pulvinar–V1 recurrent connections. 
The generation of other types of visual prediction errors observed in V1, 
such as those signalling deviations from visuo-motor predictions given 
the animal’s own actions15,31, probably involves different, motor-related 
pathways, including superior colliculus, anterior cingulate cortex or 
secondary motor cortex10,53,56,57. In general, prediction-error signals in 
V1 may be further enhanced by neuromodulators such as acetylcholine 
or noradrenaline that may signal stimulus saliency and novelty, or 
surprise more generally27,48,58,59, and these signals are likely to influence 
the activity of VIP neurons27,48,60.

Our results indicate that individual V1 neurons do not signal how the 
actual visual input deviates from the animal’s predictions, as postu-
lated within the predictive coding framework5–8. Instead, we propose 
an alternative view of predictive processing in sensory circuits: predic-
tion errors amplify the representation of feed-forward sensory input 
in neocortex, while the extent of amplification may depend on how 
much the visual stimulus deviates from expectations and therefore 
the magnitude of animals’ surprise. This would explain the particu-
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
Ampliﬁed response
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

LED on – LED off (z-scored ΔF/F )

–3

0

3

–3

0

3

–3

0

3

–3
0
3
–3
0
3
–3
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

–3

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

–0.25

0

0.25

–0.25

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
axons were optogenetically stimulated for 3 s starting at visual stimulus onset. 
b, Single-cell responses to expected and unexpected visual stimuli of all SOM 
cells (individual rows, n = 6 sessions from 4 mice) with (right) or without (left) 
optogenetic stimulation. c, Cell-averaged calcium responses with (amber) or 
without (black) optogenetic stimulation of SOM cells significantly activated  
by pulvinar stimulation (recruited cells, n = 29) and other cells (n = 159). Lines 
represent the mean and shaded regions indicate 95% confidence intervals.  
d, Visual stimulus responses of individual SOM neurons to expected B4 stimulus 
(left), unexpected C4 or D4 stimulus (middle; in block 1) and expected C4 or D4 
stimulus (right; in late block 2) plotted against the effect of pulvinar stimulation

> Figure caption (from PDF text): Fig. 5 | Pulvinar activates a specific subpopulation of SOM cells.  
a, Experimental design. The activity of SOM cells was recorded while pulvinar 
axons were optogenetically stimulated for 3 s starting at visual stimulus onset. 
b, Single-cell responses to expected and unexpected visual stimuli of all SOM 
cells (individual rows, n = 6 sessions from 4 mice) with (right) or without (left) 
optogenetic stimulation. c, Cell-averaged calcium responses with (amber) or 
without (black) optogenetic stimulation of SOM cells significantly activated  
by pulvinar stimulation (recruited cells, n = 29) and other cells (n = 159). Lines 
represent the mean and shaded regions indicate 95% confidence intervals.  
d, Visual stimulus responses of individual SOM neurons to expected B4 stimulus 
(left), unexpected C4 or D4 stimulus (middle; in block 1) and expected C4 or D4 
stimulus (right; in late block 2) plotted against the effect of pulvinar stimulation


### Overall Layout & Structure
The figure consists of two side-by-side scatter plots, presented horizontally.

### Visual Components & Symbols
Each plot is a 2D Cartesian coordinate system (a scatter plot).

*   **Data Points:** Individual data points are plotted, representing the responses of individual SOM neurons.
*   **Axes:** Both plots share identical axis scaling and labels, although the specific stimulus context differs between the two panels.
*   **Gridlines:** Faint dashed gridlines are present, intersecting at the origin (0, 0), aiding in reading coordinates.

### Labels, Keys & Legends
**Axes Labels (Shared):**
*   **Y-axis:** Labeled with numerical values ranging from -3 to 3, representing a response metric (implied by the caption context).
*   **X-axis:** Labeled as "ED on - LED off (z scored $\Delta F/F$)", indicating a z-scored change in fluorescence ($\Delta F/F$) comparing an "on" state to an "off" state.

**Panel Specific Labels (Inferred from Caption Context):**
*   The left plot is associated with the "expected B4 stimulus" (as per caption d).
*   The right plot is associated with the "expected C4 or D4 stimulus" (as per caption d).

### Data Trends & Details
**Left Plot:**
*   The data points are clustered around the origin (0, 0).
*   There is a visible spread of points, with some extending slightly into the positive and negative quadrants.
*   The distribution appears relatively centered around zero, suggesting a baseline or moderate response profile for the expected B4 stimulus.

**Right Plot:**
*   Similar to the left plot, the data points are clustered around the origin (0, 0).
*   The overall distribution appears slightly more tightly grouped or perhaps shifted compared to the left plot, though both plots show a general concentration near zero.

### Contextual Caption Integration
The caption identifies this visualization as showing the "Visual stimulus responses of individual SOM neurons to expected B4 stimulus (left), unexpected C4 or D4 stimulus (middle; in block 1) and expected C4 or D4 stimulus (right; in late block 2) plotted against the effect of pulvinar stimulation."

Based on this context:
*   The **Left Plot** represents the response to an **expected B4 stimulus**.
*   The **Right Plot** represents the response to an **expected C4 or D4 stimulus**.

*(Note: The caption mentions a "middle" plot for unexpected C4 or D4 stimulus, which is not explicitly shown in the provided image pair.)*

(difference in strength of visual stimulus responses with and without 
optogenetic pulvinar axon stimulation) for recruited (brown) and other  
(black) SOM cells. e, Cell-averaged strength of calcium response to expected 
B4 (black), unexpected C4 or D4 (red) and expected C4 or D4 (blue) stimuli of 
recruited and other SOM cells. P values from hierarchical bootstrapping test 
with Bonferroni correction. Data are mean ± 95% bootstrap confidence 
intervals. f, Proposed circuit mechanism for sensory prediction errors.  
VIP neurons inhibit a specific subpopulation of SOM cells that otherwise  
gate pulvinar input to V1, resulting in specific pulvinar-driven response 
amplification of the most stimulus-selective neurons in V1. See also Extended 
Data Fig. 12.


---

## Page 9

406  |  Nature  |  Vol 633  |  12 September 2024

Article

1.	
Schultz, W. & Dickinson, A. Neuronal coding of prediction errors. Annu. Rev. Neurosci. 23, 
473–500 (2000).
2.	
Starkweather, C. K., Babayan, B. M., Uchida, N. & Gershman, S. J. Dopamine reward 
prediction errors reflect hidden-state inference across time. Nat. Neurosci. 20, 581–589 
(2017).
3.	
Lowet, A. S., Zheng, Q., Matias, S., Drugowitsch, J. & Uchida, N. Distributional 
reinforcement learning in the brain. Trends Neurosci. 43, 980–997 (2020).
4.	
Wolpert, D. M., Miall, R. C. & Kawato, M. Internal models in the cerebellum. Trends Cogn. 
Sci. 2, 338–347 (1998).
5.	
Mumford, D. On the computational architecture of the neocortex. II. The role of cortico- 
cortical loops. Biol. Cybern. 66, 241–251 (1992).
6.	
Rao, R. P. & Ballard, D. H. Predictive coding in the visual cortex: a functional interpretation 
of some extra-classical receptive-field effects. Nat. Neurosci. 2, 79–87 (1999).
7.	
Friston, K. A theory of cortical responses. Philos. Trans. R. Soc. B 360, 815–836 (2005).
8.	
Clark, A. Whatever next? Predictive brains, situated agents, and the future of cognitive 
science. Behav. Brain Sci. 36, 181–204 (2013).
9.	
den Ouden, H. E. M., Kok, P. & de Lange, F. P. How prediction errors shape perception, 
attention, and motivation. Front. Psychol. 3, 548 (2012).
10.	
Keller, G. B. & Mrsic-Flogel, T. D. Predictive processing: a canonical cortical computation. 
Neuron 100, 424–435 (2018).
11.	
Rust, N. C. & Cohen, M. R. Priority coding in the visual system. Nat. Rev. Neurosci. 23, 
376–388 (2022).
12.	
Alink, A., Schwiedrzik, C. M., Kohler, A., Singer, W. & Muckli, L. Stimulus predictability 
reduces responses in primary visual cortex. J. Neurosci. 30, 2960–2966 (2010).
13.	
Meyer, T. & Olson, C. R. Statistical learning of visual transitions in monkey inferotemporal 
cortex. Proc. Natl Acad. Sci. USA 108, 19401–19406 (2011).
14.	
Fiser, A. et al. Experience-dependent spatial expectations in mouse visual cortex. Nat. 
Neurosci. 19, 1658–1664 (2016).
15.	
Attinger, A., Wang, B. & Keller, G. B. Visuomotor coupling shapes the functional 
development of mouse visual cortex. Cell 169, 1291–1302.e14 (2017).
16.	
Audette, N. J., Zhou, W., La Chioma, A. & Schneider, D. M. Precise movement-based 
predictions in the mouse auditory cortex. Curr. Biol. 32, 4925–4940.e6 (2022).
17.	
Kim, H. R. et al. A unified framework for dopamine signals across timescales. Cell 183, 
1600–1616.e25 (2020).
18.	
Chen, T.-W. et al. Ultrasensitive fluorescent proteins for imaging neuronal activity. Nature 
499, 295–300 (2013).
19.	
Ranganath, C. & Rainer, G. Neural mechanisms for detecting and remembering novel 
events. Nat. Rev. Neurosci. 4, 193–202 (2003).
20.	 Garrett, M. et al. Stimulus novelty uncovers coding diversity in visual cortical circuits. 
Preprint at bioRxiv https://doi.org/10.1101/2023.02.14.528085 (2023).
21.	
Homann, J., Koay, S. A., Chen, K. S., Tank, D. W. & Berry, M. J. Novel stimuli evoke excess 
activity in the mouse primary visual cortex. Proc. Natl Acad. Sci. USA 119, e2108882119 
(2022).
22.	 Tang, M. F. et al. Expectation violations enhance neuronal encoding of sensory 
information in mouse primary visual cortex. Nat. Commun. 14, 1196 (2023).
23.	 Garrett, M. et al. Experience shapes activity dynamics and stimulus coding of VIP 
inhibitory cells. eLife 9, e50340 (2020).
24.	 Pi, H.-J. et al. Cortical interneurons that specialize in disinhibitory control. Nature 503, 
521–524 (2013).
25.	 Pfeffer, C. K., Xue, M., He, M., Huang, Z. J. & Scanziani, M. Inhibition of inhibition in visual 
cortex: the logic of connections between molecularly distinct interneurons. Nat. 
Neurosci. 16, 1068–1076 (2013).
26.	 Lee, S., Kruglikov, I., Huang, Z. J., Fishell, G. & Rudy, B. A disinhibitory circuit mediates 
motor integration in the somatosensory cortex. Nat. Neurosci. 16, 1662–1670 (2013).
27.	
Fu, Y. et al. A cortical circuit for gain control by behavioral state. Cell 156, 1139–1152 (2014).
28.	 Schneider-Mizell, C. M. et al. Cell-type-specific inhibitory circuitry from a connectomic 
census of mouse visual cortex. Preprint at bioRxiv https://doi.org/10.1101/2023.01.23.525290 
(2023).
29.	 Zhang, S. et al. Long-range and local circuits for top-down modulation of visual cortex 
processing. Science 345, 660–665 (2014).
30.	 Ma, G. et al. Hierarchy in sensory processing reflected by innervation balance on cortical 
interneurons. Sci. Adv. 7, eabf5676 (2021).
31.	
Roth, M. M. et al. Thalamic nuclei convey diverse contextual information to layer 1 of 
visual cortex. Nat. Neurosci. 19, 299–307 (2016).
32.	 Blot, A. et al. Visual intracortical and transthalamic pathways carry distinct information to 
cortical areas. Neuron 109, 1996–2008.e6 (2021).
33.	 Bennett, C. et al. Higher-Order thalamic circuits channel parallel streams of visual 
information in mice. Neuron 102, 477–492.e5 (2019).
34.	 Harris, J. A. et al. Hierarchical organization of cortical and thalamic connectivity. Nature 
575, 195–202 (2019).

35.	 Sherman, S. M. & Guillery, R. W. The role of the thalamus in the flow of information to the 
cortex. Phil. Trans. R. Soc. Lond. B 357, 1695–1708 (2002).
36.	 Grieve, K. L., Acuña, C. & Cudeiro, J. The primate pulvinar nuclei: vision and action. Trends 
Neurosci. 23, 35–39 (2000).
37.	
Fang, Q. et al. A differential circuit via retino-colliculo-pulvinar pathway enhances feature 
selectivity in visual cortex through surround suppression. Neuron 105, 355–369.e6 (2020).
38.	 Audette, N. J., Urban-Ciecko, J., Matsushita, M. & Barth, A. L. POm thalamocortical input 
drives layer-specific microcircuits in somatosensory cortex. Cereb. Cortex 28, 1312–1328 
(2018).
39.	 Sermet, B. S. et al. Pathway-, layer- and cell-type-specific thalamic input to mouse barrel 
cortex. eLife 8, e52665 (2019).
40.	 Pouchelon, G. et al. The organization and development of cortical interneuron 
presynaptic circuits are area specific. Cell Rep. 37, 109993 (2021).
41.	
Yao, S. et al. A whole-brain monosynaptic input connectome to neuron classes in mouse 
visual cortex. Nat. Neurosci. 26, 350–364 (2023).
42.	 Adesnik, H., Bruns, W., Taniguchi, H., Huang, Z. J. & Scanziani, M. A neural circuit for 
spatial summation in visual cortex. Nature 490, 226–231 (2012).
43.	 Pala, A. & Petersen, C. C. H. In vivo measurement of cell-type-specific synaptic connectivity 
and synaptic transmission in layer 2/3 mouse barrel cortex. Neuron 85, 68–75 (2015).
44.	 Kanai, R., Komura, Y., Shipp, S. & Friston, K. Cerebral hierarchies: predictive processing, 
precision and the pulvinar. Philos. Trans. R. Soc. B 370, 20140169 (2015).
45.	 Hu, F. et al. Prefrontal corticotectal neurons enhance visual processing through the 
superior colliculus and pulvinar thalamus. Neuron 104, 1141–1152.e4 (2019).
46.	 Melzer, S. et al. Bombesin-like peptide recruits disinhibitory cortical circuits and enhances 
fear memories. Cell 184, 5622–5634.e25 (2021).
47.	
Szadai, Z. et al. Cortex-wide response mode of VIP-expressing inhibitory neurons by 
reward and punishment. eLife 11, e78815 (2022).
48.	 Ren, C. et al. Global and subtype-specific modulation of cortical inhibitory neurons 
regulated by acetylcholine during motor learning. Neuron 110, 2334–2350.e8 (2022).
49.	 Cossell, L. et al. Functional organization of excitatory synaptic strength in primary visual 
cortex. Nature 518, 399–403 (2015).
50.	 Znamenskiy, P. et al. Functional specificity of recurrent inhibition in visual cortex. Neuron 
112, 991–1000.e8 (2024).
51.	
Bock, D. D. et al. Network anatomy and in vivo physiology of visual cortical neurons. Nature 
471, 177–182 (2011).
52.	 Packer, A. M. & Yuste, R. Dense, unspecific connectivity of neocortical parvalbumin-positive 
interneurons: a canonical microcircuit for inhibition? J. Neurosci. 31, 13260–13271 (2011).
53.	 Leinweber, M., Ward, D. R., Sobczak, J. M., Attinger, A. & Keller, G. B. A sensorimotor circuit 
in mouse cortex for visual flow predictions. Neuron 96, 1204 (2017).
54.	 Hartley, T., Lever, C., Burgess, N. & O’Keefe, J. Space in the brain: how the hippocampal 
formation supports spatial cognition. Philos. Trans. R. Soc. B 369, 20120510 (2014).
55.	 Vann, S. D., Aggleton, J. P. & Maguire, E. A. What does the retrosplenial cortex do? Nat. 
Rev. Neurosci. 10, 792–802 (2009).
56.	 Schneider, D. M., Nelson, A. & Mooney, R. A synaptic and circuit basis for corollary 
discharge in the auditory cortex. Nature 513, 189–194 (2014).
57.	
Brenner, J. M., Beltramo, R., Gerfen, C. R., Ruediger, S. & Scanziani, M. A genetically 
defined tecto-thalamic pathway drives a system of superior-colliculus-dependent visual 
cortices. Neuron 111, 2247–2257.e7 (2023).
58.	 Hangya, B., Ranade, S. P., Lorenc, M. & Kepecs, A. Central cholinergic neurons are rapidly 
recruited by reinforcement feedback. Cell 162, 1155–1168 (2015).
59.	 Jordan, R. & Keller, G. B. The locus coeruleus broadcasts prediction errors across the 
cortex to promote sensorimotor plasticity. eLife 12, RP85111 (2023).
60.	 Kuchibhotla, K. V. et al. Parallel processing by cortical inhibition enables 
context-dependent behavior. Nat. Neurosci. 20, 62–71 (2017).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 
4.0 International License, which permits use, sharing, adaptation, distribution 
and reproduction in any medium or format, as long as you give appropriate 
credit to the original author(s) and the source, provide a link to the Creative Commons licence, 
and indicate if changes were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your 
intended use is not permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a copy of this licence, 
visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024


---

## Page 10

Methods

Mice
All experiments were performed under the UK Animals (Scientific 
Procedures) Act of 1986 (PPL PD867676F) following UK Home Office 
approval and local ethical approval by the Sainsbury Wellcome Centre 
Animal Welfare Ethical Review Body. A total of 105 mice, including 27 
C57BL/6J mice, 24 VIP-Cre mice (JAX 010908, Jackson Laboratory; Cre 
expressed in VIP interneurons), 43 VIP-Cre × Ai14 mice (JAX 010908 
and JAX 007914, Jackson Laboratory; tdTomato expressed in VIP 
interneurons), 7 SOM-Cre mice (JAX 013044, Jackson Laboratory; 
Cre expressed in SOM interneurons) and 4 SOM-Cre × Ai14 mice (JAX 
013044 and JAX 007914, Jackson Laboratory; tdTomato expressed in 
SOM interneurons) were used in this study. Both female and male mice, 
at least 7 weeks old at the start of the experiments, were used. Mice were 
co-housed with littermates in IVC cages, in reversed day–night cycle 
lighting conditions, with the ambient temperature and humidity set to 
23 °C and 56% relative humidity, respectively. Standard environment 
enrichment was provided in the form of a running wheel, a clear tube 
and wooden toys.

Surgical procedures
Prior to surgery, Dexadreson (2–3 mg kg−1) and Carprofen (5 mg kg−1) 
were administered. General anaesthesia was induced with 2.5–3% iso-
flurane, which was then reduced to maintain a breathing rate of around 
1 Hz. A 3- or 4-mm craniotomy was made over the right V1, centred 
on 2.45 mm lateral and 3.6 mm posterior of bregma. For two-photon 
calcium imaging and optogenetic manipulations of V1 cells, we 
injected adeno-associated virus (AAV) vectors into right monocu-
lar V1 (centred on 2.45 mm lateral and 3.7 mm posterior of bregma, 
1–3 injections per mouse, 100–150 nl per injection). For two-photon 
calcium imaging and optogenetic manipulations of pulvinar axons, 
we injected AAV vector into the right pulvinar (calcium imaging 
and optogenetic activation: 1.6 mm lateral and 2.1 mm posterior of 
bregma, 2.35 below the cortical surface, 1 injection per mouse, 60 nl 
per injection; optogenetic inactivation: 1.55 mm lateral and 2.0 mm 
posterior of bregma, 2.3 mm below the cortical surface, 1.60 mm 
lateral and 2.2 mm posterior of bregma, 2.4 mm below the cortical 
surface, 2 injections per mouse, 60 nl per injection). All injections 
were performed using glass pipettes and Nanoject III microinjector 
(Drummond Scientific) or a pressure injection system (Picospritzer 
III, Parker). A 3- or 4-mm circular cover glass was glued in place using 
cyanoacrylate glue (Pattex). A custom-designed stainless steel head 
plate was attached to the skull using dental cement (Super-Bond C&B, 
Sun Medical). Animals were given analgesics (Carprofen; 5 mg kg−1) at 24 
and 48 h after surgery. Imaging started approximately 3 weeks after the 
virus injection.

Viral constructs
We used AAV1-hSyn-GCaMP6f (2 × 1013 vg ml−1 Penn Vector Core/
Addgene; diluted 1:8 to 1:15 in saline) for experiments involving 
two-photon calcium imaging of V1 layer 2/3 cells; AAV1-hSyn-GCaMP7b 
(2 × 1013 vg ml−1 Penn Vector Core/Addgene; diluted 1:2 in saline) 
or AAV1-hSyn-axon-GcaMP6s (9 × 1012 vg ml−1 Penn Vector Core/
Addgene; diluted 1:2 in saline) for imaging of pulvinar axons; 
AAV2-EF1a-DIO-eNpHR3.0-mCherry (4.0 × 1012 vg ml−1, 1:2 to 1:10 
dilution, UNC vector core) for optogenetic silencing of VIP cells or 
SOM cells; AAV2-hSyn-eNpHR3.0-mCherry (3.3 × 1012 vg ml−1, 1:2 to 
1:4 dilution, UNC vector core) for optogenetic silencing of pulvinar 
axons; AAV1-hSyn-Flex-ChrimsonR-tdTomato (3.9 × 1012 vg ml−1, 1:2 
to 1:5 dilution, UNC vector core) for optogenetic activation of VIP 
cells; AAV1-Syn-ChrimsonR-tdTomato (4.1 × 1012 vg ml−1, 1:2 to 1:5 dilu-
tion, UNC vector core) for optogenetic activation of pulvinar inputs; 
AAV1-hEF1a-mCherry (5.7 × 1012 vg ml−1, 1:2 to 1:5 dilution, Zurich vector 
core) for control experiment for LED light stimulation.

Behavioural setup
Behavioural setups consisted of a styrofoam running wheel, two visual 
stimulation display monitors (see below), a reward delivery spout, and 
a camera for recording the pupil. Mice were head-fixed and placed 
on a styrofoam wheel (20 cm diameter, 12 cm width). Their running 
speed was monitored using a rotary encoder (Kubler Encoder 1000 
ppr) coupled to the wheel axle. Reward (a drop of strawberry milk, 
50% Ensure nutrition shake, Abbott Laboratories) was delivered by a 
lick spout in front of the mouse and was regulated via a solenoid pinch 
valve (161P011, NResearch). Licks were detected with a piezoelectric 
diaphragm sensor (7BB-12-9, Murata) placed under the spout. Images 
of the left eye were recorded with a CMOS camera (22BUC03, Imag-
ing Source) at 30 Hz in order to track eye movements and pupil size. 
The recording of the encoder, presentation of visual stimuli, open-
ing of the reward valves, and camera recordings were controlled by 
custom-written software in LabView. Behavioural data were acquired 
using a PCIe 6321 acquisition card (National Instruments).

Food restriction and pre-training
Before mice underwent training in the virtual environment, they were 
food-restricted and pre-trained to encourage continuous running on 
the styrofoam wheel. Four to seven days after surgery, food restriction 
and pre-training started. Mice were weighed daily and given typically 
2–3 g of food pellet in addition to strawberry milk given in training ses-
sions to ensure they maintained around 90%, but at least 85%, of their 
starting body weight. For the first few days, animals were handled in 
a soft cloth and iteratively fed strawberry milk (Abbott Laboratories) 
through a syringe until they got used to short manual restraint of the 
head plate. Mice were then head-fixed and put on the freely rotat-
ing styrofoam wheel for 15–60 min. Mice were encouraged to run on 
the wheel by delivering strawberry milk rewards after they moved a 
short distance (initially set to ~10 cm). This distance was adjusted (up 
to 500 cm) depending on the running speed of the mouse, such that 
mice received roughly one reward every 30 s. Additional rewards were 
occasionally delivered by the experimenter. This pre-training took 
4–10 days.

Virtual corridor
Once mice were running continuously, they were moved to a virtual 
environment consisting of a linear corridor with varying wall patterns 
as described previously14. The cylinder’s rotation (the instantaneous 
running speed of the animal) was used to control the speed at which 
the animal moved through the virtual environment. The virtual envi-
ronment was displayed on two monitors (U2715H, Dell; 60 Hz refresh 
rate), placed 21 cm away from both eyes of mice and oriented at 35° 
relative to the midline. Each monitor covered a visual field of approxi-
mately 110° horizontally and 60° vertically. All elements of the corridor 
including the gratings were calibrated to be isoluminant (10.1 cd m−2). 
The luminance of the monitor was set at 0.1 cd m−2, 10.1 cd m−2 and 
20.1 cd m−2, at black, grey and white values, respectively. The lumi-
nance of visual stimuli was measured using a luminance meter (Konica 
Minolta, LS-100). The grey walls of the virtual corridor were lined with 
four different landmarks. The last landmark represented the reward 
zone located at the end of the corridor. Reaching the reward zone trig-
gered an automatic reward delivered by a spout located in front of the 
mouse. After the reward delivery, the virtual environment was reset to 
the beginning of the corridor to start the next trial.

Grating stimuli were suddenly presented on full screen once the 
mouse entered a certain position in the corridor. This was done to 
ensure precise control of when the mouse would first see the grating. 
Grating stimuli were presented at four different positions between 
landmarks. The optic flow of the grating stimuli was ‘uncoupled’ from 
the running speed for 2.4 s, such that the animal’s locomotion did not 
affect its temporal frequency. Gratings were square-wave gratings, with


---

## Page 11

Article

the spatial frequency of approximately 0.04 cycles per degree (cpd) at 
the centre of the monitor and the temporal frequency approximately 
2 cycles per second (Hz). Duration of the grating presentation was 
approximately 2 s at the centre of the monitors. The precise timing 
of visual stimulus onsets was recorded with a photodiode (Thorlabs) 
attached to the monitor.

During 5 training sessions, the virtual corridor and the sequence of 
the four grating stimuli was identical (A–B–A–B) on every trial. In the 
subsequent imaging session, the identity of one of the four grating stim-
uli was changed. In block 1 of this session (160 trials), the identity of the 
4th grating stimulus B changed either to a novel grating stimulus C (C 
session), a novel stimulus D (D session), familiar stimulus A (A session) 
or no stimulus was shown (omission session) on randomly chosen 10% 
of trials. In block 2, the novel stimulus or no stimulus was shown at 
the fourth position in 100% of trials. Occasionally one mouse under-
went several sessions with unexpected stimuli. In that case, mice went 
through another training session (with gratings A–B–A–B) in between. 
For imaging of pulvinar axons, block 1 was shortened to 60 trials, and 
either a novel grating stimulus C (C session) or a novel stimulus D (D 
session) was shown at the fourth position on randomly chosen 15% 
of trials. In block 2, the novel stimulus was shown in 100% of trials, as 
for imaging of V1 layer 2/3 cells. For experiments in Extended Data 
Figs. 3a–e and 5l–p, a horizontal grating stimulus E was shown at posi-
tion 1 and 3 instead of grating stimulus A (E–B–E–B). A novel stimulus 
C (C session) or a novel stimulus A (A session) was shown on randomly 
chosen 10% of trials. For experiments in Extended Data Figs. 8 and 9a–c, 
we used a short version of the virtual corridor with two grating stimuli 
(A–B) and the identity of the 2nd grating stimulus B changed to familiar 
stimulus A on randomly chosen 10% of trials.

Visual stimulation
For experiments in Extended Data Fig. 9d–f, visual stimuli were gener-
ated using the open-source Psychophysics Toolbox61 based on MATLAB 
(MathWorks) and were presented full-field on one monitor at approxi-
mately 21 cm from the left eye of the mouse, covering 110° of visual 
space. Square-wave gratings (spatial frequency: 0.04 cpd, temporal 
frequency: 2 Hz, duration: 2 s, interval: 4 s, directions: 0 to 360° in 
45° increments) were randomized in order and presented 10 times 
per direction.

Two-photon calcium imaging
Two-photon calcium imaging was performed using a commercial reso-
nance scanning two-photon microscope (B-Scope; Thorlabs) with a 16× 
water-immersion objective (NA 0.8, Nikon), with a Ti::Sapphire laser at 
930 nm excitation wavelength (Mai Tai, SpectraPhysics). Emission light 
was band-pass filtered using a 525/50 filter for GCaMP and a 607/70 
filter for tdTomato/mCherry (Semrock). Images of 512 × 512 pixels 
from four imaging planes with fields of view ranging from 380 × 380 
μm to 440 × 440 μm were acquired at 7.5 Hz frame rate for imaging of 
V1 neurons and of a single plane of 160 × 160 μm at 15 Hz frame rate for 
imaging of pulvinar axonal boutons using ScanImage62. For imaging 
of V1 neurons, we used a piezo-actuator (Physik Instrumente) to move 
the objective in steps of 15 μm between frames to acquire images at 
four different depths, thus reducing the effective frame rate to 7.5 Hz. 
Imaging of V1 neurons was performed in layer 2/3 (typically 150–200 
μm below the cortical surface). The laser power under the objective 
never exceeded 35 mW. Axonal bouton calcium measurements were 
performed in cortical layer 1 (35–55 μm below the cortical surface), 
with laser powers below 20 mW.

To avoid cross-talk between imaging and visual stimulation, the moni-
tor backlight was controlled using a custom-built circuit to present vis-
ual stimuli only at the resonant scanner turnaround points in between 
two subsequent imaging lines (when data were not acquired)63. The 
frame trigger signal during two-photon calcium imaging was recorded 
by Labview and used for synchronization between the calcium imaging

frames and task related data (for example, behaviour data and visual 
stimuli onsets).

For imaging of pulvinar axons, we used VIP-Cre × Ai14 mice. We simul-
taneously imaged pulvinar axons expressing GCaMP and neurites of 
VIP neurons expressing tdTomato in layer 1. We then used the red signal 
(tdTomato) as a structural marker to perform Z-drift correction during 
imaging and frame registration during data pre-processing.

Optogenetic manipulation
Simultaneous two-photon imaging and optogenetic stimulations were 
performed as previously described15. Briefly, 595 nm light was delivered 
through the objective lens using a fast LED (UHP-T-595, Prizmatix). 
The LED light power was set to 8 mW in front of the objective. To com-
bine two-photon imaging and optogenetic manipulation, the LED for 
optogenetic manipulation was synchronized to the resonant scanner 
turnaround points (when data were not acquired). The propagation of 
reflected light to the eyes of the mouse was blocked by a metal light 
shield cone placed on the head plate and a black cement wall around 
the implant. Optogenetic manipulation occurred in randomly chosen 
10–50% of each trial type. For most of optogenetic manipulations, LED 
stimulation was applied continuously for 3 s, starting at visual stimulus 
onset. For optogenetic silencing during passive visual stimulation 
(Extended Data Fig. 9d–f), LED stimulation was applied throughout 
visual stimulus presentation (2 s). For optogenetic activation (Fig. 4b–d 
and Extended Data Fig. 11a–c,f–i), LED stimulation was applied at a 
frequency of 20 Hz, with 40% duty cycle (20 ms pulses) for 1 s starting 
0.1 s after visual stimulus onset.

Histology
At the end of each experiment, targeting of virus injections was con-
firmed by histology. Brains were extracted and fixed overnight in 4% 
paraformaldehyde, and stored in a 50 mM phosphate buffer. Brains 
were embedded in 5% agarose and imaged using serial section64 
two-photon65 microscopy. Our microscope was controlled by Scan-
Image Basic (MBF Bioscience) using BakingTray, a custom software 
wrapper for setting up the imaging parameters66. Images were assem-
bled using StitchIt67. Coronal slices were cut at a thickness of 40 μm 
using a vibratome (Leica VT1000), and imaged every 20 µm with a 16× 
water-immersion objective (NA 0.8, Nikon). Whole brain coronal image 
stacks were acquired at a resolution of 4.4 × 4.4 × 20 µm in xyz, with a 
two-photon laser wavelength of 780 nm, and approximately 130 mW at 
the sample. Selected brain images were registered to the adult mouse 
Allen common coordinate framework68 using The Slice Histology Align-
ment, Registration, and Probe-Track analysis (SHARP-Track), a MAT-
LAB based registration pipeline with optimized parameters for mouse 
brain registration at various cutting angles69. A subset of brains was 
embedded in 4% agarose (A9539, Sigma), cut in 200 μm coronal slices 
on a vibratome (HM650V; Microm), mounted in a mounting medium 
containing DAPI (Vectashield; Vector Laboratories) and imaged on a 
slide scanner (Zeiss AxioScan) or on a confocal microscope (Leica SP8).

Quantification and statistical analysis
Two-photon imaging. Two-photon imaging frames were motion cor-
rected and segmented using custom-written scripts in MATLAB as previ-
ously described31. In brief, to correct for x–y motion, two-photon imag-
ing frames were registered to a 1,200-frame average (40 frames × 30 
batches) using a phase-correlation algorithm. When the same V1 neu-
rons were imaged over multiple sessions, images from those sessions 
were registered together, and identical cells were matched across ses-
sions by using custom-written software. Frames with large motion 
were detected by inspecting the registration displacement results and 
were discarded from further analysis. Regions of interest (ROIs) were 
detected semi-automatically using intensity thresholding combined 
with principal component analysis–independent component analysis 
refinement and validated and refined manually. All time series were


---

## Page 12

extracted and analysed with custom-written functions using the Time-
SeriesAnalysis package70. All pixels within each ROI were averaged to 
give a single time course. Contaminating signals from neuropil were 
subtracted using an asymmetric Student’s t model (ast_model; https://
github.com/BaselLaserMouse/ast_model). Calcium ΔF/F0 signals were 
obtained by using the baseline fluorescence F0, which is estimated by a 
Gaussian mixture model with two components fitted on the raw fluo-
rescence data. The mean parameter of the lowest Gaussian component 
is used as F0. To be able to compare calcium activity across sessions and 
mice, z-scored ΔF/F was computed by subtracting the mean value of ΔF/F 
of a session and dividing the resulting trace by the standard deviation.

Analysis of visual responses. The response to each grating was calcu-
lated using the mean z-scored ΔF/F calcium signal averaged over a win-
dow from 0.4 s to 2 s after grating onset, baseline-subtracted using the 
mean z-scored ΔF/F signal during 0.5 s before stimulus onset for each 
grating presentation. Neurons were classified as stimulus-responsive 
if their mean response was bigger than 0.5 z-scored ΔF/F. In Fig. 1, 
cell-averaged calcium traces are from neurons responsive to the pre-
sented grating in trials with unexpected C or D (block 1), trials with 
expected C or D trials (late block 2) or both. For comparison, Extended 
Data Fig. 2 shows cell-averaged calcium responses of all neurons respon-
sive to any grating. In Fig. 2a,b and Extended Data Figs. 5u–z and 6a,b, 
cells were defined as prediction-error-responsive if the responses were 
significantly different between unexpected stimuli C4, D4 or stimulus 
omission (block 1) and expected stimuli C4, D4 or stimulus omission 
(second half of block 2, two-sided t-test; α = 0.05; unexpected C4, D4 
or omission versus expected C4, D4 or omission) and the difference in 
response was larger than 0.5 z-scored ΔF/F. Similarly, in Extended Data 
Figs. 5e,p and 7e, cells were defined as prediction-error-responsive if 
the responses were significantly different between unexpected C4 or 
D4 (block 1) and expected C4 or D4 (second half of block 2, two-sided 
t-test; α = 0.05; unexpected C4 or D4 versus expected C4 or D4) and the 
difference in response was larger than 0.3 z-scored ΔF/F. In Fig. 3f,g,m,n, 
average response in LED on and off trials was used for classification 
of stimulus-responsive cells to avoid selection bias towards LED off 
trials. In Fig. 4, response in LED off trials was used for classification of 
stimulus-selective cells to avoid inclusion of opsin-expressing, there-
fore directly activated VIP cells. In Fig. 5 and Extended Data Fig. 12, 
SOM cells or VIP cells were defined as ‘recruited’ if their responses were 
significantly different between with and without optogenetic pulvinar 
axon stimulation (two-sided t-test; α = 0.016; with versus without LED 
light stimulation) and the difference in response was larger than 0.3 
z-scored ΔF/F, during at least one of the visual stimulus presentations 
(expected B4, unexpected C4 or D4, expected C4 or D4). In Extended 
Data Fig. 5f–k, cells were defined as prediction-error (C or D) respon-
sive but not responsive to expected C or D if the responses were sig-
nificantly different between unexpected C4 or D4 and expected C4 
or D4 (two-sided t-test; α = 0.05) and the difference in response was 
larger than 0.5 z-scored ΔF/F, but the response to expected C4 or D4 
was smaller than 0.5 z-scored ΔF/F. In Extended Data Fig. 6g,h, in which 
raw ΔF/F rather than z-scored ΔF/F was used, neurons were defined as 
stimulus-responsive if their stimulus response strength was larger than 
0.2 ΔF/F in the second half of block 2. In Extended Data Fig. 7j,k, boutons 
were defined as stimulus-responsive if the response to any expected 
stimulus in late block 2 was larger than 0.1 z-scored ΔF/F.

Selectivity and selectivity index. To quantify the selectivity of neural 
responses we computed a response selectivity measure for individual 
V1 layer 2/3 cells and pulvinar boutons:

R
R
R
R
Selectivity = (
−
)/(
+
)
C4 or D4
A3 or B2
C4 or D4
A3 or B2

Where RC4 or D4 is the mean response to the gratings C4 or D4 in late block 
2, and RA3 or B2 is the mean response to the gratings A3 or B2 in late block

2. Selectivity values of >1 or <−1 were shown as 1 or −1, respectively. If 
selectivity of neurons responsive to a specific visual stimulus was less 
than 0.6 or more than 0.8, they were classified as either non-selective 
or highly selective to that stimulus, respectively. We also used an addi-
tional selectivity index (SI) to quantify response selectivity of individual 
pulvinar boutons (Extended Data Fig. 7l–n), since this index provided 
a more reliable measure for the noisy bouton calcium traces. SI was 
calculated as previously described71. In brief, it was computed from 
the difference between the mean response to the expected stimulus C4 
or D4 and expected stimulus B2 in late block 2, divided by the pooled 
standard deviation of the responses.

Fast and slow running trials. For the analysis in Extended Data Fig. 1k,l, 
trials in block 1 and 2 were divided into fast and slow running trials 
based on mean running speed during presentation of grating C4. A time 
window starting 0.4 s and ending 2 s after the grating onset, similar to 
the response window used for calcium responses, was used to calculate 
the mean running speed. A trial was defined as ‘fast’ or ‘slow’ if the mean 
running speed during the time window was in the top 50th or bottom 
50th percentile of all visual stimulus C4 presentations in block 1 or 2.

Correlation of running speed and neuronal activity. To determine the 
effect of running speed on neuronal activity (Extended Data Fig. 1m,n), 
we computed for each cell the correlation between mean ΔF/F and mean 
running speed in a time window (starting 0.4 s and ending 2 s after 
grating stimulus onset) of each trial in block 1 or 2. For the analysis in 
Extended Data Fig. 1o, we used the square of the correlation coefficient 
(R2, coefficient of determination) of running speed and ΔF/F across 
the recording, to quantify the strength of the modulation of neural 
responses by running speed across the entire session (block 1 and 2).

Pupil size. Pupil size was computed offline. The pupil was detected us-
ing a binary threshold and centre of mass of the detected regions. We 
then applied a one-dimensional filter to the traces using the filloutlier 
function in MATLAB.

Statistics. We used two-sided Wilcoxon signed-rank tests for com-
parisons across animals and hierarchical bootstrapping test for com-
parisons across cells unless otherwise stated. Hierarchical bootstrap 
procedure was performed as previously described72,73. In short, we first 
randomly resampled animals with replacement and then resampled 
cells with replacement from each of the resampled animals. We then 
randomly shuffled the paired data and calculated the statistic of inter-
est. This process was repeated 10,000 times. The statistic values were 
compared against the value of the original data to calculate P values. 
Where relevant P values were adjusted for multiple comparisons using 
Bonferroni correction, as indicated in the figure legends. For the ran-
domization test, we computed the statistic of interest with randomly 
shuffled data (10,000 times). The statistic values were compared against 
the value of the original data to calculate P values. All tests were per-
formed using MATLAB. Mean and bootstrap 95% confidence intervals 
were used for display purposes, as stated in the figure legends. Confi-
dence intervals were estimated using bootci function in MATLAB, with 
10,000 bootstrap samples with replacement. Cohen’s d was computed 
from the difference between the two mean responses, divided by the 
pooled standard deviation of the responses. No statistical methods were 
used to predetermine sample sizes, but our sample sizes are similar to 
those generally used in the field. Experimenters were not blinded to 
experimental groups. Animals were allocated to experimental groups 
pseudo-randomly, and trial types (expected or unexpected stimuli, 
with or without optogenetic manipulation) were randomly interleaved.

Reporting summary
Further information on research design is available in the Nature Port-
folio Reporting Summary linked to this article.


---

## Page 13

Article

Data availability

The data that support the main findings of this study are publicly avail-
able at https://doi.org/10.5281/zenodo.11403111 (ref. 74). Other data 
that are generated in this study are available from the corresponding 
author upon reasonable request. Source data are provided with this 
paper.

Code availability

The analysis code is publicly available at https://doi.org/10.5281/
zenodo.11403111 (ref. 74).

61.	
Kleiner, M. et al. What’s new in Psychtoolbox-3? Perception 36, 1–16 (2007).
62.	 Pologruto, T. A., Sabatini, B. L. & Svoboda, K. ScanImage: flexible software for operating 
laser scanning microscopes. Biomed. Eng. Online 2, 13 (2003).
63.	 Leinweber, M. et al. Two-photon calcium imaging in mice navigating a virtual reality 
environment. J. Vis. Exp. 84, e50885 (2014).
64.	 Mayerich, D., Abbott, L. & McCormick, B. Knife-edge scanning microscopy for imaging 
and reconstruction of three-dimensional anatomical structures of the mouse brain.  
J. Microsc. 231, 134–143 (2008).
65.	 Ragan, T. et al. Serial two-photon tomography for automated ex vivo mouse brain 
imaging. Nat. Methods 9, 255–258 (2012).
66.	 Campbell, R. SainsburyWellcomeCentre/BakingTray: Jan 2020 (Version Jan2020). 
Zenodo https://doi.org/10.5281/zenodo.3631610 (2020).
67.	
Campbell, R., Blot, A. & Iguerard. SainsburyWellcomeCentre/StitchIt: Last release of 
stitching model 1 (Version stitchingModel1). Zenodo https://doi.org/10.5281/
zenodo.3941901 (2020).
68.	 Wang, Q. et al. The Allen Mouse Brain Common Coordinate Framework: A 3D Reference 
Atlas. Cell 181, 936–953.e20 (2020).
69.	 Shamash, P., Carandini, M., Harris, K. & Steinmetz, N. A tool for analyzing electrode tracks 
from slice histology. Preprint at bioRxiv https://doi.org/10.1101/447995 (2018).
70.	 Muir, D. R., Roth, M. & Blot, A. TimeSeries analysis toolbox for Matlab. Zenodo https://doi.
org/10.5281/zenodo.3859433 (2020).

71.	
Poort, J. et al. Learning enhances sensory and multiple non-sensory representations in 
primary visual cortex. Neuron 86, 1478–1490 (2015).
72.	 Saravanan, V., Berman, G. J. & Sober, S. J. Application of the hierarchical bootstrap to 
multi-level data in neuroscience. Neurons Behav. Data Anal. Theory 3, 13927 (2020).
73.	 Kanamori, T. & Mrsic-Flogel, T. D. Independent response modulation of visual cortical 
neurons by attentional and behavioral states. Neuron 110, 3907–3918.e6 (2022).
74.	 Furutachi, S. Data for ‘Cooperative thalamocortical circuit mechanism for sensory 
prediction errors’. Zenodo https://doi.org/10.5281/zenodo.11403111 (2024).

Acknowledgements The authors thank M. Li for help with animal husbandry and 
pre-training; M. Rio for help with the calcium imaging data pre-processing pipeline and 
virtual reality; R. A. A. Campbell and SWC Advanced Microscopy Facility for help with 
microscopy; N. Vissers for help with histology; A. Fiser and G. Keller for the initial design  
of the virtual corridor; T. Kanamori, I. Voitov and M. Javadzadeh for feedback on the 
manuscript; and T.D.M.-F. laboratory members and S.B.H. laboratory members for 
discussions. This work was supported by Osamu Hayaishi Memorial Scholarship (to S.F.);  
a Sainsbury Wellcome Centre Core Grant from the Gatsby Charitable Foundation and 
Wellcome (219627/Z/19/Z and 090843/F/09/Z); a Wellcome Investigator Award 
(219561/Z/19/Z to S.B.H.); the Gatsby Charitable Foundation (GAT3212 and GAT3361 to 
T.D.M.-F.); the Wellcome Trust (090843/E/09/Z and 217211/Z/19/Z to T.D.M.-F.); European 
Research Council (HigherVision 337797 to S.B.H.; NeuroV1sion 616509 to T.D.M.-F.); the 
SNSF (31003 A 169525 to S.B.H.); and Biozentrum core funds (University of Basel).

Author contributions S.F., S.B.H. and T.D.M.-F. conceived the study. S.F. performed the 
experiments and analysed the data. A.D.F. assisted with surgical procedures, animal 
pre-training and preliminary optogenetic experiments. A.M.A. assisted with animal 
pre-training and histology. S.F., S.B.H. and T.D.M.-F. wrote the manuscript.

Competing interests The authors declare no competing interests.

Additional information
Supplementary information The online version contains supplementary material available at 
https://doi.org/10.1038/s41586-024-07851-w.
Correspondence and requests for materials should be addressed to Shohei Furutachi, 
Thomas D. Mrsic-Flogel or Sonja B. Hofer.
Peer review information Nature thanks Pieter Goltstein and the other, anonymous, reviewer(s) 
for their contribution to the peer review of this work. Peer reviewer reports are available.
Reprints and permissions information is available at http://www.nature.com/reprints.


---

## Page 14



### Panel Layout and Structure
The figure is organized into several rows of plots:
*   **Top Row (a, b):** Plots comparing running speed and relative pupil size for Position 3 vs. Position 4, with sub-panels distinguishing between C3 and B4 stimuli/conditions.
*   **Second Row (c, d):** Plots comparing relative pupil size for Position 3 vs. Position 4, again distinguishing between C3 and B4 conditions.
*   **Third Row (e, f):** Plots showing lick rate for Position 3 vs. Position 4, distinguishing between C3 and B4 conditions.
*   **Fourth Row (g, h):** Plots showing running speed for Position 3 vs. Position 4, distinguishing between C3 and B4 conditions (similar to Panel a).
*   **Fifth Row (i, j):** Plots showing relative pupil size for Position 3 vs. Position 4, distinguishing between C3 and B4 conditions (similar to Panel c).
*   **Bottom Row (k, l, m, n, o):** Plots showing running speed and lick rate across different blocks (Block 1 vs. Block 2) or correlations between variables, often involving regression-like plots.

### Detailed Panel Descriptions

**Panels (a) and (g): Running Speed Plots**
*   These panels display time-series plots of "Running speed (m/s)" on the y-axis versus "Time from onset (s)" on the x-axis, spanning approximately -2 to 4 seconds.
*   **Panel (a):** Compares Position 3 (stimulus A3) vs. Position 4 (stimulus B4 or C4).
    *   The plot shows multiple lines representing different conditions (e.g., Expected B4 trial, Unexpected C4 trial).
    *   **Panel (b):** Provides statistical comparisons for the conditions shown in Panel (a). It shows box plots comparing running speed between Position 3 and Position 4, with statistical markers ($P=0.53$, $P<0.1$) above the plots.
*   **Panel (g):** Similar to Panel (a), comparing Position 3 (stimulus A3) vs. Position 4 (stimulus B4 or D4).
    *   **Panel (h):** Provides statistical comparisons for the conditions shown in Panel (g), showing box plots with $P=0.63$ and $P<0.31$.

**Panels (c) and (i): Relative Pupil Size Plots**
*   These panels display time-series plots of "Relative pupil size" on the y-axis versus "Time from onset (s)" on the x-axis.
*   **Panel (c):** Compares Position 3 (stimulus A3) vs. Position 4 (stimulus B4 or C4).
    *   **Panel (d):** Shows statistical comparisons using box plots, indicating $P=0.078$ and $P<0.055$.
*   **Panel (i):** Compares Position 3 (stimulus A3) vs. Position 4 (stimulus B4 or D4).
    *   **Panel (j):** Shows statistical comparisons using box plots, indicating $P=0.063$ and $P<0.1$.

**Panels (e) and (f): Lick Rate Plots**
*   These panels display time-series plots of "Lick (Hz)" on the y-axis versus "Time from onset (s)" on the x-axis.
*   **Panel (e):** Compares Position 3 (stimulus A3) vs. Position 4 (stimulus B4 or C4).
    *   **Panel (f):** Shows statistical comparisons using box plots, indicating $P<0.063$ and $P=0.60$.

**Panels (k) through (o): Block/Correlation Plots**
*   **Panel (k):** Shows "Running speed (m/s)" vs. time, comparing "Fast trials" and "Slow trials."
*   **Panel (l):** Shows "Running speed (m/s)" vs. time, comparing "Fast trials" and "Slow trials," similar to Panel (k).
*   **Panel (m):** A scatter plot titled "Modulation by prediction error." The y-axis is labeled "Modulation by running speed (m/s)" and the x-axis is "Modulation by prediction error." It shows data points for Block 1 ($n=644$) and Block 2 ($n=644$).
*   **Panel (n):** A scatter plot titled "Modulation by prediction error." The y-axis is labeled "Modulation by lick rate (Hz)" and the x-axis is "Modulation by prediction error." It shows data points for Block 1 ($n=644$) and Block 2 ($n=644$).
*   **Panel (o):** A scatter plot showing the correlation between two variables. The y-axis is "Correlation and running speed (coefficient of determination, $R^2$)" and the x-axis is "Modulation by prediction error." It shows data points for Block 1 & 2, with a noted correlation $r=-0.021; P=0.60$.

### Summary of Key Visual Elements
*   **Time Series Plots (a, c, e, g, i):** Use continuous lines to track variables over time relative to an event onset.
*   **Box Plots (b, d, f, h, j):** Used to summarize distributions and compare means across discrete conditions.
*   **Scatter Plots (m, n, o):** Used to visualize relationships between modulation effects across different blocks.
*   **Color Coding:** While specific colors are not detailed without the original image, different conditions (e.g., Expected vs. Unexpected trials) are differentiated by distinct lines or markers in the time-series plots.
*   **Statistical Annotations:** $P$-values are explicitly placed above the box plots to denote statistical significance between conditions.

Extended Data Fig. 1 | See next page for caption.


---

## Page 15

Article

Extended Data Fig. 1 | Running and licking behaviour and pupil size during 
presentation of expected and unexpected gratings. Related to Figs. 1 and 2. 
a, Running speed at virtual corridor position 3 (left, grating A3 shown) or at 
position 4 (right, grating B4 or C4 shown) in trials in which grating B was 
presented at position 4 (black, expected B4 trials, 90% of trials in block 1), trials 
in which grating C was presented at position 4 (red, 10% of trials in block 1, 
unexpected C4 trials) and trials in the second half of block 2 (blue, expected C4 
trials, late block 2). Light grey shading indicates length of visual stimulus at the 
centre of monitors. Lines and shading are mean and bootstrap 95% CI (n = 20 
mice). b, Same as a, but data from individual animals are shown separately. 
Black bars represent mean across animals. Position 3, running speed during 
grating A3 presentation in B4 vs unexpected C4 trials: P = 0.53; running speed 
during grating A3 presentation in unexpected vs expected C4 trials: P = 1. 
Position 4, running speed during B4 vs unexpected C4 presentation: P = 4.4 × 
10−4; running speed during unexpected vs expected C4 presentation: P = 0.33. 
n = 20 mice, two-sided signed-rank test with Bonferroni correction. c and d, 
Same as a and b, but for relative pupil size (normalized by each session’s  
median value). d, Position 3, pupil size during grating A3 presentation in B4 vs 
unexpected C4 trails: P = 1; pupil size during grating A3 presentation in 
unexpected vs expected C4 trials: P = 0.078. Position 4, pupil size during B4 vs 
unexpected C4 presentation: P = 1; pupil size during unexpected vs expected 
C4 presentation: P = 0.055; n = 9 mice, two-sided signed-rank test with 
Bonferroni correction. e and f, Same as a and b, but for lick rate. e, Inset shows 
lick rate around the reward delivery. f, Position 3, lick rate during A3 
presentation in B4 vs unexpected C4 trials: P = 0.063; lick rate during A3 
presentation in unexpected vs expected C4 trials: P = 1. Position 4, lick rate 
during B4 vs unexpected C4 presentation: P = 0.60; lick rate during unexpected 
vs expected C4 presentation: P = 1. n = 9 mice, two-sided signed-rank test with

Bonferroni correction. g-j, Same as a-d, but for a different unexpected visual 
stimulus D. h, Position 3, running speed during grating A3 presentation in B4 vs 
unexpected D4 trials: P = 0.63; running speed during grating A3 presentation in 
unexpected vs expected D4 trials: P = 1. Position 4, running speed during B4 vs 
unexpected D4 presentation: P = 0.31; running speed during unexpected vs 
expected C4 presentation: P = 0.63. n = 6 mice, two-sided signed-rank test with 
Bonferroni correction. j, Position 3, pupil size during grating A3 presentation in 
B4 vs unexpected D4 trials: P = 1; pupil size during grating A3 presentation in 
unexpected vs expected D4 trials: P = 0.063. Position 4, pupil size during B4 vs 
unexpected D4 presentation: P = 1; pupil size during unexpected vs expected 
D4 presentation: P = 0.063; n = 6 mice, two-sided signed-rank test with 
Bonferroni correction. k, Running speed (left) and responses to grating C4 
(right) on trials with fast (black, top 50%) and slow (red, bottom 50%) running 
speed during grating C presentation at position 4 in block 1 (see Methods).  
l, Same as k, but for block 2. m, Scatterplot showing the relationship between 
response modulation by running speed (difference in calcium response 
between fast and slow trials) and strength of prediction error responses 
(Pearson correlation: r = 0.27, P = 1.3 × 10−12; n = 644 cells from 9 mice) in block 1. 
The positive correlation shows that the response to unexpected grating C was 
larger in trials with higher running speed, as expected from previous studies. 
This shows that running speed changes (deceleration in response to the 
unexpected stimulus) cannot explain the increased neural responses to 
unexpected stimuli. n, Same as m, but for block 2 (Pearson correlation: 
r = −0.064, P = 0.11; n = 644 cells from 9 mice). o, Scatterplot showing the 
relationship between correlation of z-scored ΔF/F and running speed 
(coefficient of determination R2, over the entire recording session) and 
strength of prediction error responses (Pearson correlation: r = −0.021, 
P = 0.60; n = 644 cells from 9 mice).


---

## Page 16



### Panel Layout and Structure
The figure is organized into several distinct panels: **a**, **b**, **c**, **d**, **e**, **f**, and **g**. Panels **a** through **f** primarily consist of schematic diagrams illustrating experimental conditions (C session and D session) followed by corresponding traces of neural activity. Panel **g** is a time-series plot showing visual responses across trials.

### Detailed Component Description

#### Panel **a** (C session Schematic)
This panel shows a schematic representation of the C session. It features four vertical columns labeled **A**, **B**, **C**, and **D** at the top, corresponding to four distinct experimental blocks or conditions. Below these labels are smaller schematic representations showing a sequence of stimuli presentation, indicated by numbered boxes (1, 2, 3, 4) arranged horizontally.
*   **Stimulus Presentation:** The sequence shows a progression from block 1 to block 4.
*   **Legend/Key:** A small inset box indicates the stimulus presentation pattern: "Early" and "Late," with a percentage bar graph showing $100\%$ for both.
*   **Contextual Note:** The panel is titled "C session."

#### Panel **b** (Neural Activity Plots - C Session)
This panel displays neural activity traces corresponding to the C session. It is divided into four sub-sections, likely corresponding to conditions A1, B2, A3, and C4.
*   **Top Section (General):** Above the traces, there is a legend indicating two types of responses: "Unexpected C4/D4/omission trial" (represented by a red line) and "Expected C4/D4/omission trial" (represented by a blue line).
*   **Traces:** Below the legend, there are four sets of traces:
    *   **A1:** Shows a trace with $n=158$.
    *   **B2:** Shows a trace with $n=125$.
    *   **A3:** Shows a trace with $n=146$.
    *   **C4:** Shows a trace with $n=644$.
*   **Time Axis:** All traces share a common time axis labeled "2 s" at the bottom right, with an associated y-axis label: "$z$-scored $\Delta F/F$".

#### Panel **c** (D session Schematic)
This panel mirrors the structure of Panel **a**, representing the D session. It also features four vertical columns labeled **A**, **B**, **C**, and **D**.
*   **Stimulus Presentation:** Similar to Panel **a**, it shows a sequence of numbered boxes (1, 2, 3, 4) indicating stimulus presentation.
*   **Legend/Key:** An inset box shows the "Early" and "Late" stimulus presentation pattern, again with $100\%$ indicated.
*   **Contextual Note:** The panel is titled "D session."

#### Panel **d** (Neural Activity Plots - D Session)
This panel displays neural activity traces corresponding to the D session, structured similarly to Panel **b**.
*   **Top Section (General):** The legend indicating "Unexpected C4/D4/omission trial" and "Expected C4/D4/omission trial" is present.
*   **Traces:** Four sets of traces are shown:
    *   **A1:** Shows a trace with $n=125$.
    *   **B2:** Shows a trace with $n=129$.
    *   **A3:** Shows a trace with $n=129$.
    *   **D4:** Shows a trace with $n=840$.
*   **Time Axis:** The traces share the common time axis labeled "2 s" and y-axis label: "$z$-scored $\Delta F/F$".

#### Panel **e** (Omission Session Schematic)
This panel illustrates the Omission session setup, structurally similar to Panels **a** and **c**. It shows four columns labeled **A**, **B**, **C**, and **D** with a sequence of numbered stimulus presentation boxes (1, 2, 3, 4).
*   **Legend/Key:** An inset box indicates the stimulus pattern ("Early" and "Late") with $100\%$ shown.
*   **Contextual Note:** The panel is titled "Omission session."

#### Panel **f** (Neural Activity Plots - Omission Session)
This panel displays neural activity traces for the Omission session, structured like Panels **b** and **d**.
*   **Top Section (General):** The legend for "Unexpected C4/D4/omission trial" and "Expected C4/D4/omission trial" is present.
*   **Traces:** Four sets of traces are shown:
    *   **A1:** Shows a trace with $n=92$.
    *   **B2:** Shows a trace with $n=92$.
    *   **A3:** Shows a trace with $n=92$.
    *   **Omission:** A final trace labeled "Omission" is shown.
*   **Time Axis:** The traces share the common time axis labeled "2 s" and y-axis label: "$z$-scored $\Delta F/F$".

#### Panel **g** (Trial-by-Trial Response Plot)
This panel is a time-series plot showing the average calcium response across trials.
*   **X-Axis:** Labeled "Trial," ranging from 1 to 56, grouped into blocks (Block 1 and Block 2).
*   **Y-Axis:** Labeled "Visual stimulus response ($z$-scored $\Delta F/F$)."
*   **Data Lines:** Two distinct lines are plotted:
    *   A solid black line representing the response for "C4."
    *   A dashed gray line representing the response for "Same traversal average (A1 B2 A3)."
*   **Annotations:** The plot is segmented into "Block 1" and "Block 2." A specific annotation points to the C4 response line, referencing "B4 (first trial after C4)."

Extended Data Fig. 2 | Average calcium responses in V1 to expected and 
unexpected stimuli and unexpected stimulus omissions. a, Schematic of 
visual stimuli shown in a C session (unexpected C stimulus presented in 10% of 
trials instead of B at position 4 in block 1 and in 100% of trials in block 2). b, Top: 
Average calcium responses of all cells significantly responsive to any of 
the presented gratings in unexpected C4 (block 1) or expected C4 (late block 2) 
trials (n = 887). Dotted line indicates grating stimulus onset. Bottom: Average 
calcium responses as on top, but only of neurons significantly responsive to 
each presented grating stimulus (n = 158, 125, 146, 644; Gratings A1, B2, A3, C4 
responsive cells). Same as Fig. 1c. Data from 9 mice. c, Schematic of visual 
stimuli shown in a D session (unexpected D stimulus presented in 10% of trials

instead of B at position 4 in block 1 and in 100% of trials in block 2). d, Same as b 
but responses to stimulus D4 on the right. Top: n = 1,069. Bottom: n = 125, 129, 
129, 840; A1, B2, A3, D4 responsive cells. Data from 7 mice. e, Schematic of 
visual stimuli shown in an omission session (stimulus B4 omitted in 10% of trials 
in block 1 and in 100% of trials in block 2). f, Average calcium responses to 
gratings A1, B2, A3 and omission of B4 of all omission responsive cells (n = 92 
from 5 mice). Lines and shading are mean and bootstrap 95% CI. g, Average 
calcium responses to C4 (dark grey), average responses to A1, B2, A3 (light grey) 
and to B4 (black) of all cells significantly responsive to any of the presented 
gratings in block 1 or late block 2 trials (n = 887). Symbols and error bars depict 
mean and bootstrap 95% CI.


---

## Page 17

Article



### Panel a: Schematic Diagram (Top Left)
Panel **a** contains two small schematic diagrams, labeled with time points and cell types.

*   **Top Diagram:** Shows a sequence: **1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4**. Above the sequence, there are labels: **E** (Early) and **B** (Late). Below the sequence, there are labels: **C2** and **B**.
*   **Bottom Diagram:** Shows a similar sequence: **1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4**. Above the sequence, there are labels: **E** (Early) and **B** (Late). Below the sequence, there are labels: **C2** and **B**.
*   Both diagrams include percentage annotations below the sequence, such as "C2 5%", "100%", and "B 95%".

### Panel b: Time-Series Plots (Top Right)
Panel **b** displays two time-series plots comparing "Unexpected" and "Expected" neural responses.

*   **Top Plot (C2):** Shows a trace labeled **C2**. The x-axis is time, scaled in seconds ($\text{s}$), ranging from 0 to 2 $\text{s}$. The y-axis is labeled "1 z-scored $\Delta F/F$". Two lines are plotted: one for **Unexpected** (red) and one for **Expected** (blue). A statistical notation, "$n=496$", is present, along with a p-value: "$P < 10^{-4}$".
*   **Bottom Plot (C4):** Shows a trace labeled **C4**. The x-axis is time, scaled in seconds ($\text{s}$), ranging from 0 to 2 $\text{s}$. The y-axis is labeled "1 z-scored $\Delta F/F$". Two lines are plotted: one for **Unexpected** (red) and one for **Expected** (blue). A statistical notation, "$n=496$", is present, along with a p-value: "$P < 10^{-4}$".

### Panel c: Scatter Plot (Middle Left)
Panel **c** is a scatter plot comparing neural activity across different conditions.

*   **Title:** "All C responsive cells".
*   **Axes:** The x-axis is labeled "Unexpected C2 (z-scored $\Delta F/F$)" and the y-axis is labeled "Unexpected C4 (z-scored $\Delta F/F$)".
*   **Data Points:** The plot contains numerous black data points.
*   **Annotations:** A statistical notation "$n=496$" is present in the upper left corner.

### Panel d: Scatter Plot (Middle Center)
Panel **d** is a scatter plot comparing neural activity related to reward.

*   **Title:** "Reward responsive cells".
*   **Axes:** The x-axis is labeled "Unexpected C2 (z-scored $\Delta F/F$)" and the y-axis is labeled "Unexpected C4 (z-scored $\Delta F/F$)".
*   **Data Points:** The plot contains numerous black data points.
*   **Annotations:** A statistical notation "$n=28$" is present in the upper left corner, along with a p-value: "$P = 0.0094$".

### Panel e: Scatter Plot (Middle Right)
Panel **e** is a scatter plot comparing neural activity for other responsive cells.

*   **Title:** "Other C responsive cells".
*   **Axes:** The x-axis is labeled "Unexpected C2 (z-scored $\Delta F/F$)" and the y-axis is labeled "Unexpected C4 (z-scored $\Delta F/F$)".
*   **Data Points:** The plot contains numerous black data points.
*   **Annotations:** A statistical notation "$n=468$" is present in the upper left corner, along with a p-value: "$P < 10^{-4}$".

### Panel f: Schematic Diagram (Bottom Left)
Panel **f** contains two small schematic diagrams, similar in structure to Panel **a**.

*   **Top Diagram:** Shows a sequence: **1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4**. Above the sequence, there are labels: **E** (Early) and **B** (Late). Below the sequence, there are labels: **C2** and **B**.
*   **Bottom Diagram:** Shows a sequence: **1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4**. Above the sequence, there are labels: **E** (Early) and **B** (Late). Below the sequence, there are labels: **C3** and **B**.
*   Both diagrams include percentage annotations below the sequence, such as "C2 5%", "100%", and "B 95%".

### Panel g: Scatter Plot (Bottom Right)
Panel **g** is a scatter plot comparing normalized responses.

*   **Title:** "Response".
*   **Axes:** The x-axis is labeled "Unexpected C2 (norm. z-scored $\Delta F/F$)" and the y-axis is labeled "Unexpected C3 (norm. z-scored $\Delta F/F$)".
*   **Data Points:** The plot contains numerous black data points.
*   **Annotations:** A statistical notation "$n=549$" is present in the upper left corner. The plot includes a regression line and associated statistics: "$r = 0.88$" and "$P = 7.9 \times 10^{-18}$".

### General Annotations
A footnote below the panels reads: "$\dagger$ Prediction error responses to the same unexpected aligned to reward onset of all neurons and reward response."

Extended Data Fig. 3 | Prediction error responses to the same unexpected 
visual stimulus encountered at different locations. a, Experimental design. 
Grating stimulus C was presented at position 2 (C2) or at position 4 (C4) in 5% 
of trials each in block 1. b, Average calcium responses to unexpected (red)  
and expected (blue) C2 (left, n = 496 from 5 mice, P < 1 × 10−4, hierarchical 
bootstrapping test) and C4 (right, n = 496 from 5 mice, P < 1 × 10−4). Cells 
responsive to unexpected or expected C2 or C4 were pooled. Lines and shading 
indicate mean and bootstrap 95% CI. c, Top: average calcium responses to 
unexpected C2 (dotted red) and unexpected C4 (red, n = 496 from 5 mice, P < 1 × 
10−4, hierarchical bootstrapping test) and responses of individual V1 neurons to 
C2 plotted against their responses to C4. Bottom: average calcium response

aligned to reward onset of all neurons and reward response (from 0.5 s before 
to 0.5 s after reward onset) plotted against difference in response to unexpected 
C2 and unexpected C4 (n = 496 from 5 mice). d, Same as c, but only for reward 
responsive cells (n = 28 from 5 mice, P = 0.0094, hierarchical bootstrapping 
test). e, Same as c, but for the remaining, reward non-responsive cells (n = 468 
from 5 mice, P < 1 × 10−4, hierarchical bootstrapping test). f, Experimental 
design. Grating C was presented at position 2 (C2) or at position 3 (C3) in 5%  
of trials each in block 1. Same as Fig. 1f. g, Same as Fig. 1h, but responses are 
normalized across animals by mean response of all responsive neurons (C2 or 
C3) of individual animals (n = 549 from 9 mice, Pearson correlation: r = 0.88, 
P = 7.9 × 10−181).


---

## Page 18



### Panel Layout and Structure
The figure is organized into multiple distinct panels: **a**, **b**, **c**, **d**, **e**, **f**, **g**, **h**, **i**, **j**, and **k**. Panels **a** through **d** appear to be schematic representations or small plots related to experimental conditions. Panels **b**, **c**, and **d** contain scatter plots with overlaid traces. Panels **e** through **k** present various types of graphs and schematics.

### Detailed Component Descriptions

#### Panel a: Schematic Diagram
Panel **a** is a schematic diagram illustrating experimental conditions. It shows three sequential stages labeled "A session," "B4 (unexpected)," and "B4 (expected)."
*   **Structure:** A horizontal timeline or sequence is depicted.
*   **Labels:** Above the diagram, there are labels indicating trial numbers: "1," "2," "3," and "4."
*   **Annotations:** Below the sequence, there are labels indicating probabilities or conditions: "A (unexpected)" and "B4 (expected)," with associated percentages ($10\%$ and $90\%$, respectively).

#### Panel b: Scatter Plot (A1 or A3 responsive cells)
Panel **b** is a scatter plot titled "A1 or A3 responsive cells."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "Expected A1 ($z$-scored $\Delta F/F$)".
*   **Data Points:** Several individual data points are plotted.
*   **Overlayed Traces:** Two distinct traces are shown, labeled "Expected A1" and "Unexpected A3."
*   **Statistics:** The plot includes a statistical annotation: "$n = 95$" and "$P = 0.53$".

#### Panel c: Scatter Plot (B2 or B4 responsive cells)
Panel **c** is a scatter plot titled "B2 or B4 responsive cells."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "Expected B2 ($z$-scored $\Delta F/F$)".
*   **Data Points:** Several individual data points are plotted.
*   **Overlayed Traces:** Two distinct traces are shown, labeled "Expected B4" and "Unexpected B2."
*   **Statistics:** The plot includes a statistical annotation: "$n = 73$" and "$P = 0.0032$".

#### Panel d: Scatter Plot (A4 or A4 responsive cells)
Panel **d** is a scatter plot titled "A4 or A4 responsive cells." (Note: The title seems redundant, possibly indicating a specific cell type).
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "Expected A3 ($z$-scored $\Delta F/F$)".
*   **Data Points:** Several individual data points are plotted.
*   **Overlayed Traces:** Two distinct traces are shown, labeled "Expected A4" and "Unexpected A3."
*   **Statistics:** The plot includes a statistical annotation: "$n = 171$" and "$P < 10^{-4}$".

#### Panel e: Scatter Plot (Selectivity)
Panel **e** is a scatter plot titled "Selectivity."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "Selectivity."
*   **Data Points:** Numerous individual data points are scattered across the plot.
*   **Annotations:** The panel includes a label "Unexpected A4 - expected A3" near the top left.

#### Panel f: Scatter Plot (Visual Stimulus Response)
Panel **f** is a scatter plot titled "Visual stimulus response."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "Response to B not A selective."
*   **Data Points & Grouping:** Data points are grouped and colored/labeled: "Unexpected A4" (blue circles), "Expected A3" (red circles).
*   **Statistics:** The plot includes statistical annotations: "$P = 0.055$" and "$P = 0.0078$".

#### Panel g: Schematic Diagram (C session)
Panel **g** is a schematic diagram illustrating the "C session."
*   **Structure:** A horizontal timeline or sequence is shown with three labeled points: "1," "2," and "3."
*   **Annotations:** Below the timeline, there are labels indicating conditions: "$10\%$," "$90\%$," and "100%."

#### Panel h: Scatter Plot (Expected vs. Unexpected C4)
Panel **h** is a scatter plot titled "Expected or unexpected C4 responsive cells."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **Data Points & Grouping:** Data points are colored and labeled: "Unexpected C4" (red) and "Expected C4" (black).
*   **Statistics:** The plot includes a statistical annotation: "$n = 644$" and "$P < 10^{-4}$".

#### Panel i: Scatter Plot (Unexpected C4)
Panel **i** is a scatter plot titled "Unexpected C4 responsive cells."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **Data Points:** Data points are plotted, likely representing a subset of the cells from Panel h.
*   **Statistics:** The plot includes a statistical annotation: "$n = 482$".

#### Panel j: Scatter Plot (Expected C4)
Panel **j** is a scatter plot titled "Expected C4 responsive cells."
*   **Y-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **X-axis:** Labeled "$z$-scored $\Delta F/F$".
*   **Data Points:** Data points are plotted, likely representing a subset of the cells from Panel h.
*   **Statistics:** The plot includes a statistical annotation: "$n = 162$".

#### Panel k: Line Graph (Trial Activity)
Panel **k** is a line graph showing activity across trials.
*   **Y-axis:** Labeled "Visual stimulus response ($z$-scored $\Delta F/F$)".
*   **X-axis:** Labeled with trial numbers: "1-2," "15-16," "37-38," and "55-56."
*   **Data Lines:** Two lines are plotted: one labeled "Unexpected (but not expected)" and another labeled "C4 responsive cells."
*   **Annotations:** The plot includes a caption-like note below the axes: "Extended Data Fig. 4 | Prediction error signal in response to familiar and two-sided signed rank test), and non-selective (selectivity A3 vs B2 < 0.6; left."

Extended Data Fig. 4 | Prediction error signal in response to a familiar 
visual stimulus encountered at an unexpected location (grating A 
presented at location 4 instead of grating B). a, Schematic of experimental 
design (A session). b, Calcium responses of individual V1 neurons to expected 
grating A1 plotted against responses to expected grating A3. Neurons 
responsive to either A1 or A3 were included in the analysis (n = 95 cells from 8 
mice, P = 0.53, hierarchical bootstrapping test). c, Calcium responses of 
individual V1 neurons to expected grating B2 plotted against responses to 
expected grating B4. Neurons responsive to either B2 or B4 were included in 
the analysis (n = 77 cells from 8 mice, P = 0.0032, hierarchical bootstrapping 
test). d, Calcium responses of individual V1 neurons to expected grating A3 
plotted against responses to unexpected grating A4. Neurons responsive to 
either A3 or A4 were included in the analysis (n = 171 cells from 8 mice, P < 1 × 
10−4, hierarchical bootstrapping test). e, Strength of prediction error signal 
(difference in response to unexpected grating A4 and expected grating A3) 
plotted against grating response selectivity (difference in response to grating 
A3 and grating B2 divided by the sum of responses) for all cells responsive to 
expected gratings. f, Cell-averaged response strength to expected grating A3 
(blue) and unexpected grating A4 (red) of B-selective (left, n = 8 mice, P = 0.055,

two-sided signed-rank test), and non-selective (selectivity A3 vs B2 < 0.6, left, 
n = 8 mice, P = 0.84, two-sided signed-rank test) and highly selective (selectivity 
A3 vs B2 > 0.8, right, n = 8 mice, P = 0.0078) grating A3 responsive cells. Data 
points depict mean responses for individual animals, n = 8 mice, black 
horizontal bars indicate mean across animals. g, Schematic of experimental 
design (C session). h, Same as d, but for C session. Calcium responses of 
individual V1 neurons to expected grating C4 plotted against responses to 
unexpected grating C4. Neurons responsive to either expected for unexpected 
C4 were included in the analysis (n = 644 cells from 9 mice, P < 1 × 10−4, 
hierarchical bootstrapping test). i, Calcium responses of individual V1 neurons 
to expected grating C4 plotted against responses to unexpected grating C4. 
Neurons responsive to unexpected C4 but not expected C4 were included in 
the analysis (n = 482 cells from 9 mice). Cell- and trial-averaged calcium 
responses of the same cells to unexpected C4 (red) and expected C4 (blue) 
were plotted on top. j, Same as i, but for neurons responsive to expected C4 
(n = 162 from 9 mice). k, Average calcium responses to C4 of neurons 
responding to unexpected but not expected C4 (dark grey, n = 482) and of 
neurons responding to expected C4 (light grey, n = 162) across trials and 
blocks. Symbols and error bars depict mean and bootstrap 95% CI.


---

## Page 19

Article



### Overall Layout & Structure
The figure is organized into 26 distinct panels, labeled sequentially from **a** through **z**. The layout is a grid-like arrangement, with panels grouped horizontally and vertically. Panels **a** through **e** form the first row of plots, followed by panels **f** through **k**, then **l** through **p**, and finally **q** through **z**.

### Panel Descriptions (Detailed Breakdown)

#### Panels a-e: Schematic Diagrams and Initial Plots
*   **Panel a:** A schematic diagram illustrating two conditions, "C session" and "D session." Both show a simplified neural circuit structure with labeled nodes (A, B, C, D) and connections.
*   **Panel b:** A scatter plot titled "Unexpected C4 or D4." The x-axis is labeled "z-scored $\Delta f/F$" and the y-axis is not explicitly labeled but represents a comparison or grouping. It shows data points clustered around zero, with annotations indicating "Unexpected C4" and "Expected C4."
*   **Panel c:** A scatter plot titled "Response." The x-axis is labeled "z-scored $\Delta f/F$" and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected C4" and "Expected C4."
*   **Panel d:** A scatter plot titled "$\Delta$response." The x-axis is labeled "z-scored $\Delta f/F$" and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected C4" and "Expected C4."
*   **Panel e:** A pie chart titled "Prediction-error responsive cells." It shows two segments: one labeled "D" (representing 64%) and another labeled "C&D" (representing 36%).

#### Panels f-k: Time-Series Plots
These panels display time-series data, typically showing fluorescence traces ($\Delta f/F$) over time.

*   **Panel f:** Labeled "C session." Shows a trace plot with an x-axis labeled "2 s" and a y-axis representing $\Delta f/F$. It includes annotations for $n=133$ and a comparison between "Unexpected C4" and "Expected C4."
*   **Panel g:** Labeled "Response." Similar to Panel f, showing a trace plot with $n=133$ and comparisons for "Unexpected C4" vs. "Expected C4."
*   **Panel h:** Labeled "$\Delta$response." Shows a trace plot with $n=133$, comparing "Unexpected C4" and "Expected C4."
*   **Panel i:** Labeled "C session." Shows a trace plot with $n=138$, comparing "Unexpected C4" and "Expected C4."
*   **Panel j:** Labeled "Response." Shows a trace plot with $n=138$, comparing "Unexpected C4" and "Expected C4."
*   **Panel k:** Labeled "$\Delta$response." Shows a trace plot with $n=138$, comparing "Unexpected C4" and "Expected C4."

#### Panels l-p: Schematic Diagrams and Plots
*   **Panel l:** A schematic diagram similar to Panel a, showing "C session" and "A session," with nodes labeled A, B, C, D.
*   **Panel m:** A scatter plot titled "Unexpected C4 or A4." The x-axis is labeled "z-scored $\Delta f/F$," and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected C4" and "Expected C4."
*   **Panel n:** A scatter plot titled "Response." The x-axis is labeled "z-scored $\Delta f/F$," and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected C4" and "Expected C4."
*   **Panel o:** A scatter plot titled "$\Delta$response." The x-axis is labeled "z-scored $\Delta f/F$," and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected C4" and "Expected C4."
*   **Panel p:** A pie chart titled "Prediction-error responsive cells," showing segments for "C" (46%) and "A&D" (54%).

#### Panels q-z: Final Plots
These panels continue the pattern of time-series plots and scatter plots.

*   **Panel q:** A schematic diagram showing "Omission session" and "D session," with nodes labeled A, B, C, D.
*   **Panel r:** A scatter plot titled "Omission session." The x-axis is labeled "z-scored $\Delta f/F$," and the y-axis is not explicitly labeled. It shows data points, with annotations for "Unexpected Omission" and "Expected Omission."
*   **Panel s:** A time-series plot labeled "Response" for the Omission session, showing $n=39$.
*   **Panel t:** A time-series plot labeled "$\Delta$response" for the Omission session, showing $n=39$.
*   **Panel u:** A time-series plot labeled "Omission session" for the D session, showing $n=39$.
*   **Panel v:** A time-series plot labeled "Response" for the D session, showing $n=39$.
*   **Panel w:** A time-series plot labeled "$\Delta$response" for the D session, showing $n=39$.
*   **Panel x:** A time-series plot labeled "Omission session" for the D session, showing $n=234$.
*   **Panel y:** A time-series plot labeled "Response" for the D session, showing $n=234$.
*   **Panel z:** A time-series plot labeled "$\Delta$response" for the D session, showing $n=234$.

*(Note: The caption mentions "Extended Data Fig. S1," indicating these panels are part of supplementary material, which is consistent with the detailed nature of the plots.)*

Extended Data Fig. 5 | See next page for caption.


---

## Page 20

Extended Data Fig. 5 | Prediction error responses of layer 2/3 cells in V1 to 
different visual stimuli. a-d, Same as Fig. 1k–n, but excluding VIP neurons 
which were labelled with tdTomato in these experiments. b, Top: cell- and trial-
averaged calcium responses of C4-responsive neurons to expected B4 (black, 
block 1), unexpected C4 (red, block 1) and expected C4 (blue, late block 2). 
n = 304 cells from 5 mice, P < 1 × 10−4, Hierarchical bootstrapping test. Bottom: 
cell- and trial-averaged calcium responses to expected B4 (black), unexpected 
D4 (red) and expected D4 (blue). n = 607 cells from 5 mice, P < 1 × 10−4, 
Hierarchical bootstrapping test. Lines and shading are mean and bootstrap 
95% CI. c, Calcium responses of individual V1 neurons to unexpected D4 
plotted against unexpected C4 responses. Pearson correlation: r = −0.17, 
P = 2.0 × 10−6, n = 814 cells from 5 mice. d, Left: the difference of responses 
between unexpected and expected D4 plotted against the difference of 
responses between unexpected and expected C4. Pearson correlation: 
r = −0.041, P = 0.25, n = 814 cells from 5 mice. Right: same as on the left but 
excluding neurons not responsive to C and D. Inset: distribution of prediction 
error absolute selectivity |(C − D)/(C + D)| of V1 neurons in the right scatter plot 
compared to a shuffled data set. V1 responses to the two stimuli are more 
selective than expected by chance. n = 467 cells from 5 mice, P < 1 × 10−4, 
randomization test. e, Pie chart with proportion of prediction-error responsive 
non-VIP neurons in V1 for stimulus C, stimulus D, or both (see Methods). n = 960 
cells from 5 mice. f-h, Same as b-d, but for cells responsive to prediction error 
(C), but not responsive to expected C4 (n = 133). i-k, Same as f-h, but for cells 
responsive to prediction error (D), but not responsive to expected D4 (n = 138). 
l, Experimental design. Gratings C or A were presented at position 4 (C4 and A4) 
in 5% or 10% of trials in different sessions (C and A sessions, respectively).  
Note that a horizontal grating E was presented at position 1 and 3 in these 
experiments and during training. m-p, Same as b-e, but for comparison of 
unexpected C4 and unexpected A4 responses. m, Top: cell- and trial-averaged

calcium responses of C4-responsive neurons to unexpected C4 (red, block 1) 
and expected C4 (blue, late block 2). n = 233 cells from 3 mice, P < 1 × 10−4, 
Hierarchical bootstrapping test. Bottom: cell- and trial-averaged calcium 
responses to unexpected A4 (red) and expected A4 (blue). n = 204 cells from  
3 mice, P < 1 × 10−4, Hierarchical bootstrapping test. Lines and shading are  
mean and bootstrap 95% CI. n, Calcium responses of individual V1 neurons  
to unexpected A4 plotted against unexpected C4. Pearson correlation: 
r = −0.098, P = 0.052, n = 394 cells from 3 mice. o, The difference of responses 
between unexpected and expected A4 plotted against the difference of 
responses between unexpected and expected C4. Pearson correlation: 
r = −0.030, P = 0.56, n = 394 cells from 3 mice. p, Pie chart with proportion of 
prediction-error responsive non-VIP neurons for stimulus C, stimulus A, or 
both (see Methods). n = 464 cells from 3 mice. q, Schematic of visual stimuli 
shown in an omission session (stimulus B4 omitted in 10% of trials in block 1 and 
in 100% of trials in block 2) and a D session (stimulus D was presented at 
position 4 in 10% of trials in block 1 and in 100% of trials in block 2). r, Average V1 
calcium responses to unexpected (red) and expected (blue) omission (top, 
n = 78 from 4 mice, P < 1 × 10−4) and D4 (bottom, n = 479 from 4 mice, P < 1 × 10−4). 
Hierarchical bootstrapping test. Lines and shading indicate mean and 
bootstrap 95% CI. s, Responses to unexpected omission plotted against 
responses to unexpected D4 for individual V1 layer 2/3 neurons (n = 538 cells 
from 4 mice). t, Difference between responses to unexpected omission and 
expected omission of B4 plotted against response difference between 
unexpected D4 and expected D4 stimulus responses for individual V1 layer 2/3 
neurons. u-w, Same as r-t, but for cells with a significant difference in response 
between expected and unexpected stimulus omission (n = 39). x-z, Same as r-t, 
but for cells with a significant difference in response between expected and 
unexpected stimulus D4 (n = 234).


---

## Page 21

Article



**Panel a: Raster Plot/Spike Train Visualization**
This panel displays two sets of raster plots, labeled "Unexpected D4" and "Expected D4," stacked vertically.
*   **Y-axis:** Labeled "Cells," with specific cell indices visible (e.g., 1, 383).
*   **X-axis:** Labeled with time markers (e.g., "0 s," "2 s").
*   **Visual Content:** The plots show vertical lines (spikes) indicating neural firing across different cells over time.
*   **Inset Plot:** To the right of the raster plots, there is a small line graph showing a trace labeled "(z-scored $\Delta F/F$)" over time, suggesting calcium imaging data.

**Panel b: Bar Graph and Trace Plot**
This panel contains two distinct visualizations side-by-side.

*   **Left Plot (Bar Graph):**
    *   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
    *   **X-axis:** Labeled with conditions: "A1," "B2," "A3," and "D4."
    *   **Data Representation:** Two sets of bars are shown for each condition: one colored red (labeled "Unexpected D4") and one colored blue (labeled "Expected D4").
    *   **Annotations:** A total sample size, "$n = 383$," is noted above the graph.

*   **Right Plot (Trace):**
    *   This is a time-series trace showing calcium activity.
    *   **Y-axis:** Labeled "$\Delta F/F$."
    *   **X-axis:** Labeled with time markers (e.g., "0 s," "2 s").
    *   **Visual Content:** A trace line is displayed, likely representing the average response over time.

**Panel c: Scatter Plot**
This panel displays a scatter plot comparing two variables.
*   **Y-axis:** Labeled "Unexpected D4 (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Expected D4 (z-scored $\Delta F/F$)."
*   **Data Points:** Individual data points are plotted.
*   **Annotations:** A correlation coefficient ($r = 0.32$) and a p-value ($P = 3.6 \times 10^{-12}$) are provided in the upper right corner, indicating a weak but significant correlation. The total sample size is noted as "$n = 437$."

**Panel d: Scatter Plot (Selectivity)**
This panel shows two separate scatter plots, likely comparing selectivity metrics.

*   **Left Plot:**
    *   **Y-axis:** Labeled "Unexpected D4 - Expected D4 (z-scored $\Delta F/F$)."
    *   **X-axis:** Labeled "Selectivity (late block 2)."
    *   **Data Points:** Individual data points are plotted. The sample size is "$n = 437$."

*   **Right Plot:**
    *   **Y-axis:** Labeled "Unexpected D4 - Expected D4 (z-scored $\Delta F/F$)."
    *   **X-axis:** Labeled "Selectivity (late block 2)."
    *   **Data Points:** Individual data points are plotted. The sample size is "$n = 437$."

**Panel e: Bar Graph and Trace Plot (Response Types)**
This panel compares responses across different categories.

*   **Left Plot (Bar Graph):**
    *   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
    *   **X-axis:** Categorized into "Responsive to A or B," "Non-responsive to D," and "Highly selective response to D (late block 2)."
    *   **Data Representation:** Bar heights represent the mean response for each category. Statistical significance markers ($P = 0.69$ and $P = 0.016$) are present above the bars, along with a general significance marker ($P = 0.94$).

*   **Right Plot (Trace):**
    *   This is a time-series trace, likely showing the average response profile.

**Panel f: Time Course Plot (Selectivity)**
This panel displays a time-course plot across different trial blocks.
*   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
*   **X-axis:** Labeled with trial ranges: "1-2," "15-16," "37-38," and "55-56."
*   **Data Representation:** Two lines are plotted: one solid black line and one dashed gray line.
*   **Legend:** A legend indicates the lines: "Highly selective" and "Non-selective."

**Panel g: Bar Graph (Response Types)**
This panel presents a bar graph comparing responses across different categories, similar to Panel e.

*   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
*   **X-axis:** Categorized into "Responsive not C," "Highly selective response to C (late block 2)," and "Responsive to C (late block 2)."
*   **Data Representation:** Bar heights represent the mean response. Statistical significance markers ($P = 0.50$, $P = 0.031$) are shown, and a general significance marker ($P = 0.0078$) is present.

**Panel h: Bar Graph (Response Types)**
This panel presents another bar graph comparing responses.

*   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
*   **X-axis:** Categorized into "Responsive not D," "Highly selective response to D (late block 2)," and "Responsive to D (late block 2)."
*   **Data Representation:** Bar heights represent the mean response. Statistical significance markers ($P = 0.44$, $P = 0.30$) are shown, and a general significance marker ($P = 0.016$) is present.

**Panel i: Bar Graph (Response Types)**
This panel presents a bar graph comparing responses related to C.

*   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
*   **X-axis:** Categorized into "Non-selective," "Highly selective," and "Responsive to C (late block 2)."
*   **Data Representation:** Bar heights represent the mean response. Statistical significance markers ($P = 0.16$ and $P = 0.037$) are shown.

**Panel j: Bar Graph (Response Types)**
This panel presents a bar graph comparing responses related to D.

*   **Y-axis:** Labeled "Visual stimulus response ($\Delta F/F$)."
*   **X-axis:** Categorized into "Non-selective" and "Highly selective response to D (late block 2)."
*   **Data Representation:** Bar heights represent the mean response. Statistical significance markers ($P = 0.97$ and $P = 0.016$) are shown.

Extended Data Fig. 6 | Prediction error specifically boosts neurons most 
selective to the presented visual stimulus (stimulus D). a-f, Same as Fig. 2, 
but for a second unexpected visual stimulus D. a, Single-cell responses for all 
prediction-error responsive cells (individual rows) (n = 383 cells, 7 mice) to 
visual stimuli A1, B2, A3 and D4 in unexpected D4 (top) and expected D4 
(bottom) trials, sorted by response to unexpected D4. b, Top: calcium 
responses for all prediction-error responsive cells (individual dots) (n = 383 
cells, 7 mice) to visual stimuli A1, B2, A3 and D4 in unexpected D4 (red) and 
expected D4 (blue) trials. Bottom: Cell-averaged calcium responses. Lines and 
shading are mean and bootstrap 95% CI. c, Difference in response strength 
between unexpected (block 1) and expected D4 (late block 2) for all visual 
stimulus-responsive cells in late block 2, plotted against response to expected 
D4 (late block 2) for individual neurons. r = 0.32, P = 3.6 × 10−12, Pearson 
correlation; n = 437, 7 mice. d, Left: difference in response strength between 
unexpected and expected D4 responses of individual neurons, plotted against 
their response selectivity to stimulus D vs. stimulus B in late block 2 (difference 
in response strength between expected D4 and B2 divided by the sum of 
responses to both stimuli) for all neurons responsive to at least one of the visual 
stimuli in late block 2. −1 indicates only responsive to B, +1 only responsive to D, 
and 0 equal responses to both. Right: same as on the left but for response 
selectivity to stimulus D vs. stimulus A in late block 2. e, Mean responses to

expected (blue) and unexpected (red) stimulus D4 of A or B selective cells (left, 
n = 7 mice, P = 0.94; two-sided signed-rank test), and non-selective (selectivity 
towards D, compared to B < 0.6, middle, n = 7 mice; P = 0.69; two-sided 
signed-rank test) and highly selective (selectivity towards D, compared to 
B > 0.8, right, n = 7 mice; P = 0.016) stimulus D4 responsive cells in late block 2. 
Data points depict mean responses for individual animals, n = 7 mice, black 
horizontal bars indicate mean across animals. f, Mean calcium responses to 
stimulus D4 over all trials in the imaging session of highly selective (dark grey, 
n = 185) and non-selective (light grey, n = 75) stimulus D4 responsive cells in 
block 2. Responses were averaged over two trials. Error bars are bootstrap 95% 
CI. g, Same as Fig. 2e, but showing responses as raw ΔF/F0 without z-scoring.  
h, Same as g, but for sessions with unexpected stimulus D, equivalent to panel e. 
i, Same as Fig. 2e, but highly selective cells were sub-selected to match their 
average response strength to the expected stimulus C4 with the average 
response to expected stimulus C4 of non-selective cells. To achieve this, highly 
selective cells that responded strongly to expected gratings (top 35%) were 
removed from the analysis. Hierarchical bootstrapping test. Bars and error bars 
are mean and 95% bootstrap CI. j, Same as i, but for sessions with unexpected 
stimulus D, equivalent to panel e, but with matched average response strength 
to expected stimulus D4 of highly selective and non-selective V1 cells.


---

## Page 22



### Panel (a)
Panel (a) is a schematic diagram illustrating the experimental setup involving different recording sessions. It shows four distinct blocks labeled "A," "B," "C," and "D." Each block contains a small schematic representation of a neural structure, likely representing different recording conditions or locations. Above the blocks are labels: "C session" and "D session." Within each block (A, B, C, D), there are small icons representing different states or conditions.

### Panel (b)
Panel (b) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** There are two sets of data points, distinguished by color/symbol (though specific colors aren't detailed, the legend implies two groups).
*   **Annotations:** The plot includes text annotations: "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Statistics:** A p-value is noted: $P < 10^{-4}$.

### Panel (c)
Panel (c) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** Similar to Panel (b), there are data points plotted.
*   **Annotations:** The plot includes text annotations: "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Statistics:** A p-value is noted: $P < 10^{-4}$.

### Panel (d)
Panel (d) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** Data points are plotted, likely representing a subset of the data from (b) or (c).
*   **Annotations:** The plot includes text annotations: "Unexpected C4 - expected D4" and "Expected C4."
*   **Statistics:** A p-value is noted: $P = 0.13$.

### Panel (e)
Panel (e) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** Data points are plotted, with a visual representation of density or distribution.
*   **Annotations:** The plot includes text annotations: "Unexpected C4 - expected D4" and "Expected C4."
*   **Statistics:** A percentage is noted: $46\%$.

### Panel (f)
Panel (f) is a bar chart showing the "Fraction of cells" on the y-axis versus different categories on the x-axis.
*   **X-axis Categories:** The categories are "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Data:** The bar for "Unexpected C4 or D4" shows a fraction of approximately 0.1, while the bar for "Expected C4 or D4" shows a fraction of approximately 0.92 (or $92\%$).
*   **Annotations:** The plot includes a label indicating the total number of cells ($n=747$) and the percentage for the second category ($92\%$).

### Panel (g)
Panel (g) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** Data points are plotted, likely representing a specific subset of cells.
*   **Annotations:** The plot includes text annotations: "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Statistics:** A p-value is noted: $P < 10^{-4}$.

### Panel (h)
Panel (h) is a schematic diagram illustrating the neural circuit structure. It shows two main sections: "C session" and "D session."
*   **Circuit Elements:** Within each session, there are schematic representations of neural layers or regions (labeled 1 through 4).
*   **Connections:** Arrows indicate flow between these layers. The diagram includes labels like "V1," "GCaMP7b," and "tdTomato."
*   **Schematic Detail:** The structure suggests a layered cortical organization.

### Panel (i)
Panel (i) is a scatter plot comparing two metrics: "Unexpected C4 or D4" on the y-axis and "Expected C4 or D4" on the x-axis.
*   **Data Points:** A large number of data points ($n=1978$) are plotted.
*   **Annotations:** The plot includes text annotations: "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Context:** The plot is titled with a description related to selectivity.

### Panel (j)
Panel (j) presents two scatter plots side-by-side, both comparing "Unexpected C4 or D4" (y-axis) vs. "Expected C4 or D4" (x-axis).
*   **Left Plot:** Titled "Selective to B $\rightarrow$ C or D." It shows data points ($n=953$) and a general trend.
*   **Right Plot:** Titled "Selective to A $\rightarrow$ C or D." It shows data points ($n=953$) and a general trend.
*   **Context:** Both plots are associated with "Selectivity (late block 2)."

### Panel (k)
Panel (k) is a bar chart comparing "Visual stimulus response" across different selectivity categories.
*   **X-axis Categories:** The bars are grouped by "Responsive to A or B," "Non-selective," and "Responsive to C or D."
*   **Y-axis:** Labeled "Visual stimulus response."
*   **Data:** The bars show quantitative differences in response magnitude across the categories.
*   **Statistics:** A p-value is noted: $P < 10^{-2}$.

### Panel (l)
Panel (l) is a histogram showing the "Fraction of boutons" on the y-axis versus "Selectivity index (SI)" on the x-axis.
*   **X-axis Range:** The SI ranges from -2 to 2, with bins centered around specific values.
*   **Data:** The histogram shows the distribution of SI values, with a peak around 0.
*   **Annotations:** The plot is divided into two sections: "Selective to B $\rightarrow$ C or D" (left) and "Other" (right).

### Panel (m)
Panel (m) is a histogram showing the "Fraction of boutons" on the y-axis versus "Visual stimulus response (z-scored $\Delta F/F$)" on the x-axis.
*   **X-axis Range:** The response ranges from -2 to 2.
*   **Data:** This histogram shows the distribution of responses, separated into two conditions: "Unexpected C4 or D4" and "Expected C4 or D4."
*   **Annotations:** The plot is divided into two sections: "Selective to B $\rightarrow$ C or D" (left) and "Other" (right).

### Panel (n)
Panel (n) is a bar chart comparing metrics across different selectivity categories.
*   **X-axis Categories:** The categories are "Other" and "Highly selective."
*   **Y-axis:** Labeled "Visual stimulus response (z-scored $\Delta F/F$)."
*   **Data:** The bars show the mean response for each category.
*   **Statistics:** A p-value is noted: $P = 0.0049$.

Extended Data Fig. 7 | See next page for caption.


---

## Page 23

Article

Extended Data Fig. 7 | Prediction error responses of VIP cells to different 
visual stimuli, effect of optogenetic VIP neuron silencing on strongly 
responding layer 2/3 cells, and broad facilitation of pulvinar inputs by 
prediction errors. a, Schematic of the experimental design. Stimulus C or D 
was presented at position 4 (C4 and D4) in 10% of trials in different sessions (C 
and D sessions, respectively). Calcium activity of VIP cells in V1 layer 2/3 was 
recorded. b, Top: cell- and trial-averaged VIP calcium responses to expected B4 
(black), unexpected C4 (red, block 1) and expected C4 (blue, late block 2). 
n = 291 VIP cells from 5 mice, P < 1 × 10−4, Hierarchical bootstrapping test. 
Bottom: cell- and trial-averaged VIP calcium responses to expected B4 (black), 
unexpected D4 (red) and expected D4 (blue). n = 298 VIP cells from 5 mice,  
P < 1 × 10−4, Hierarchical bootstrapping test. Lines and shading are mean and 
bootstrap 95% CI. c, Calcium responses of individual VIP neurons to unexpected 
D4 plotted against responses to unexpected C4. Pearson correlation: r = 0.29, 
P = 1.8 × 10−5, n = 290 from 5 mice. d, Difference of responses to unexpected and 
expected stimulus D4 plotted against the difference of unexpected and 
expected C4 responses (Pearson correlation: r = 0.13, P = 0.031, n = 290 from 5 
mice. e, Pie chart with proportion of prediction-error responsive VIP cells for 
stimulus C, stimulus D, or both (see Methods). n = 199 from 5 mice. f, Distribution 
of stimulus response strength for VIP cells to unexpected C4 or D4 (n = 753, 14 
sessions from 7 mice). g, Same as Fig. 3f, but only cells exhibiting a visual 
stimulus response of more than 3 z-scored ΔF/F were included in order to avoid 
inclusion of opsin-expressing and therefore directly silenced VIP cells, which 
cannot be visually identified in these experiments (n = 45 from 7 sessions; P < 1 
× 10−4; Hierarchical bootstrapping test). Neurons indicated in black have 
responses > 3 z-scored ΔF/F. Inset: Responses to unexpected stimulus C4 or D4 
of V1 layer 2/3 cells with (amber) or without (black) VIP silencing. Lines and 
shading are mean and bootstrap 95% CI. h, Experimental design. The calcium

activity of axonal boutons of pulvinar projections in V1 L1 was recorded.  
i, Stimulus responses of individual pulvinar boutons to unexpected C4 or D4 
plotted against responses to expected C4 or D4. n = 1,978 pulvinar boutons 
from 10 sessions, 7 mice. j, Left: difference in response strength between 
unexpected and expected C4 or D4 responses of individual neurons, plotted 
against their response selectivity to stimulus C or D vs. stimulus B in late block  
2 (difference in response strength between expected C4 or D4 and B2 divided 
by the sum of responses to both stimuli) for all boutons responsive to at least 
one of the visual stimuli in late block 2. −1 indicates only responsive to B, +1 only 
responsive to C or D, and 0 equal responses to both. Right: same as on the left 
but for response selectivity to stimulus C or D vs. stimulus A in late block 2.  
k, Mean responses to expected (blue) and unexpected (red) stimuli C4 or D4,  
of boutons selective to A or B (left, n = 512 boutons; P < 1 × 10−4; Hierarchical 
bootstrapping test), and non-selective (selectivity towards C, compared to 
B < 0.6, middle, n = 200 boutons; P = 0.0049) and highly selective (selectivity 
towards C, compared to B > 0.8, right, n = 191 boutons; P = 0.0032) grating C4 
responsive neurons in late block 2. Bars and error bars are mean and 95% 
bootstrap CI. l, Distribution of selectivity index (difference in response 
strength between expected C4 or D4 and B2 divided by the pooled standard 
deviation, see methods) for all pulvinar boutons. m, Distribution of stimulus 
response strength of non-selective (selectivity index C4/D4, compared to 
B2 < 0.6, left) and highly selective (selectivity index > 0.8, right) pulvinar 
boutons to unexpected C4 or D4 (red) and expected C4 or D4 (blue). n, Cell- and 
trial-averaged stimulus responses to expected C4 or D4 (blue) and unexpected 
C4 or D4 (red), of non-selective (left) and highly selective (right) pulvinar 
boutons. n = 1,790 and n = 99; P < 1 × 10−4, P = 0.0049; non-selective and highly 
selective boutons, hierarchical bootstrapping test. Bars and error bars are 
mean and 95% bootstrap CI.


---

## Page 24



### Panel a: Experimental Setup Schematic
Panel **a** presents a schematic diagram illustrating the experimental setup for VIP interneuron activity.
*   It shows a simplified representation of a neural circuit or recording setup.
*   A block labeled "A session (short corridor)" is shown on the left, connected to a sequence of events.
*   A timeline or progression shows: "160 trials" followed by a branching structure.
*   The branches indicate two conditions: "A2 (unexpected) 10%" and "B2 (expected) 90%".
*   The overall structure suggests a behavioral or stimulus-driven paradigm.

### Panel b: Imaging Setup Schematic
Panel **b** shows a schematic of the imaging setup.
*   It depicts a microscope or recording apparatus focused on neural tissue.
*   Labels indicate different cell types/markers: "GCaMP6f" and "VIP-Cre; tdTomato".
*   The setup includes a light source indicated by an arrow pointing towards the tissue, labeled "930 nm".
*   The panel is titled "VIP interneurons" and shows the cell types being monitored.

### Panel c: VIP Interneuron Activity Plot
Panel **c** displays a raster plot or time-series visualization of neural activity.
*   The y-axis is labeled "VIP cells".
*   The x-axis represents time, marked in seconds ("2 s").
*   There are two conditions indicated by the legend: "Expected B2" and "Unexpected A2".
*   The plot shows traces of activity (likely fluorescence or spiking) over time for the two conditions.

### Panel d: VIP Interneuron Response Plot
Panel **d** presents a plot showing the change in neural activity.
*   The y-axis is labeled "VIP stimulus response ($\Delta F/F$)" and ranges from -0.2 to 0.6.
*   The x-axis is time, marked in seconds ("2 s").
*   Two curves are plotted: "Expected B2" and "Unexpected A2".
*   The plot includes a statistical annotation: "$P < 10^{-4}$" near the top right, suggesting a significant difference.

### Panel e: Silencing Setup Schematic
Panel **e** illustrates an experimental setup involving silencing.
*   It shows a schematic similar to Panel **b**, but with an added element indicating silencing.
*   The setup includes "GCaMP6f" and "VIP-Cre".
*   A label indicates the stimulus: "930 nm 594 nm".
*   The panel is titled "Silencing" and shows the cell types involved.

### Panel f: Silenced VIP Activity Plot
Panel **f** displays the results of the silencing experiment.
*   The y-axis is labeled "($z$-scored $\Delta F/F$)".
*   The x-axis is time, marked in seconds ("2 s").
*   Two conditions are shown: "LED on" and "LED off".
*   The plot shows data points clustered around zero for both conditions, with statistical annotations: "$n = 69$" and "$P = 0.98$" for the "LED on" condition, and "$n = 179$" and "$P < 10^{-4}$" for the "LED off" condition.

### Panel g: Pulvinar Input Schematic
Panel **g** shows a schematic related to pulvinar inputs.
*   It depicts a neural circuit diagram focusing on the pulvinar region.
*   Labels include "V1" and "Pulvinar".
*   The cell type being monitored is indicated by a marker: "GCaMP7b".
*   The panel is titled "Pulvinar inputs".

### Panel h: Pulvinar Activity Plot
Panel **h** presents a time-series plot of pulvinar activity.
*   The y-axis is labeled "($z$-scored $\Delta F/F$)".
*   The x-axis is time, marked in seconds ("2 s").
*   This plot shows activity across multiple trials (indicated by the vertical lines/traces).

### Panel i: Pulvinar Response Plot
Panel **i** displays the average response of pulvinar neurons.
*   The y-axis is labeled "VIP stimulus response ($\Delta F/F$)".
*   The x-axis is time, marked in seconds ("2 s").
*   Two conditions are plotted: "Expected B2" and "Unexpected A1".
*   A statistical annotation "$P < 10^{-4}$" is present.

### Panel j: Silencing Pulvinar Inputs Schematic
Panel **j** illustrates a silencing setup targeting pulvinar inputs.
*   Similar to Panel **e**, this is a schematic showing the experimental setup.
*   It involves "GCaMP6f" and targets "Pulvinar".
*   The stimulus is indicated: "LED on/off".

### Panel k: Silenced Pulvinar Activity Plot
Panel **k** shows the results of silencing pulvinar inputs.
*   The y-axis is labeled "($z$-scored $\Delta F/F$)".
*   The x-axis is time, marked in seconds ("2 s").
*   Two conditions are shown: "LED on" and "LED off".
*   The plot includes statistical annotations: "$n = 36$" and "$P = 0.39$" for the "LED on" condition, and "$n = 66$" and "$P = 0.033$" for the "LED off" condition.

Extended Data Fig. 8 | See next page for caption.


---

## Page 25

Article

Extended Data Fig. 8 | Activity of VIP interneurons and pulvinar input is 
required for prediction error signals to familiar visual stimulus presented 
at unexpected location. a, Schematic of the experimental design. For the 
experiments in this figure a shorter virtual corridor was employed as depicted. 
b, Calcium activity of VIP cells in V1 layer 2/3 was recorded during the 
experiment. c, Single-cell responses for all VIP cells (individual rows) in the A 
session (n = 289 cells from 5 mice) to expected B2 (left), unexpected A2 (middle) 
and expected A1 (right), sorted by response strength to unexpected A2. d, Cell- 
and trial-averaged calcium responses of all VIP cells (n = 289) to expected B2 
(black), unexpected A2 (red) and expected A1 (blue). Lines and bars are mean, 
shading and error bars indicate bootstrap 95% CI. P < 1 × 10−4 for all comparisons 
between expected and unexpected stimuli; Hierarchical bootstrapping test 
with Bonferroni correction. e, Schematic of the experiment. Calcium activity of 
V1 layer 2/3 cells was recorded while VIP cells were optogenetically silenced. VIP 
cell silencing started at the onset of visual stimuli and lasted for 3 s. f, Top: cell- 
and trial-averaged responses of V1 neurons significantly responsive to the 
presented grating stimuli to expected grating B2 (left, P = 0.98, Hierarchical 
bootstrapping test, n = 69 cells, 5 mice), unexpected grating A2 (middle, P < 1 × 
10−4, n = 179) and expected grating A1 (right, P = 0.11, n = 118) with (amber) or 
without (black) VIP silencing. Lines and shading are mean and bootstrap 95% CI. 
Bottom: responses of individual neurons to the grating stimulus indicated 
above during VIP silencing (LED on), plotted against responses to the same

stimulus in control trials (LED off). g-i, Same as b-d, but for calcium responses 
of pulvinar axonal boutons in V1 (see Methods). g, Calcium activity of axonal 
boutons of pulvinar projections was recorded in V1 layer 1. h, Single-bouton 
responses for all pulvinar axonal boutons (individual rows) in the A session 
(n = 1,453 boutons, 6 mice) to expected B2 (left), unexpected A2 (middle) and 
expected A1 (right), sorted by response strength to unexpected A2. i, Bouton- 
and trial-averaged calcium responses of all pulvinar boutons (n = 1,453 
boutons) to expected grating B2 (black), unexpected grating A2 (red) and 
expected grating A1 (blue). Lines and bars are mean, shading and error bars 
indicate bootstrap 95% CI. P < 1 × 10−4 for all comparisons between expected 
and unexpected stimuli; Hierarchical bootstrapping test with Bonferroni 
correction. j and k, Same as e and f, but with optogenetic silencing of pulvinar 
axons. j, The activity of V1 layer 2/3 cells was recorded while pulvinar axons in V1 
were optogenetically silenced (see Methods). k, Top: cell- and trial-averaged 
responses of neurons significantly responsive to the presented grating stimuli 
to expected grating B2 (left, P = 0.39, Hierarchical bootstrapping test, n = 36 
cells, 5 mice), unexpected grating A2 (middle, P = 0.033, n = 66) and expected 
grating A1 (right, P = 0.44, n = 57) with (amber) or without (black) silencing of 
pulvinar axons. Lines and shading are mean and bootstrap 95% CI. Bottom: 
responses of individual neurons to the grating stimulus indicated above during 
silencing of pulvinar axons (LED on), plotted against responses to the same 
stimulus in control trials (LED off).


---

## Page 26



### Overall Layout & Structure
The figure is organized into eight distinct panels (a, b, c, d, e, f, g, h), each presenting a different experimental setup or data visualization. Panels (a) and (d) are schematic diagrams illustrating the experimental preparation, while panels (b), (c), (e), (f), and (h) display time-series plots or statistical comparisons of neural activity. Panel (g) is another schematic diagram.

### Detailed Panel Descriptions

**Panel a: Silencing Setup Schematic**
This panel is a schematic diagram illustrating the experimental setup for silencing VIP cells.
*   **Visual Components:** It shows a simplified representation of visual processing, featuring two main components: "Silencing VIP cells" and "Imaging VIP cells."
*   **Labels:** The schematic includes labels for the cell types: "VIP cells" and "VIP$^+$ cells."
*   **Optogenetic Elements:** Arrows indicate the application of light: "930 nm" and "594 nm."
*   **Genetic Markers:** The diagram indicates the expression of fluorescent proteins: "GCaMP6f" and "eNpHR3.0-mCherry."
*   **Contextual Annotation:** A label below the schematic reads: "VIP-Cre; Ai14," indicating the genetic driver used.

**Panel b: Time Course Plot (Unexpected A2)**
This panel displays a time-series plot comparing neural activity under different light conditions.
*   **Plot Type:** Line graph showing $\Delta F/F$ over time (x-axis).
*   **X-Axis:** Time, ranging from 0 to 2 seconds (s).
*   **Y-Axis:** $\Delta F/F$ (Z-scored), ranging from approximately -0.1 to 0.3.
*   **Curves:** Two lines are plotted: "LED off" (black line) and "LED on" (orange/yellow line).
*   **Annotations:** The panel is titled "Unexpected A2." Above the plot, $n=289$ is noted.

**Panel c: Statistical Comparison Plot (Unexpected A2 vs Unexpected C2)**
This panel compares the average $\Delta F/F$ response between two conditions.
*   **Plot Type:** Bar chart comparing mean $\Delta F/F$ values.
*   **X-Axis Categories:** "Unexpected A2" and "Unexpected C2."
*   **Y-Axis:** Visual stimulus response ($\Delta F/F$, Z-scored), ranging from -0.1 to 0.6.
*   **Data Representation:** Two bars represent the mean response for each category. Error bars are present on both bars.
*   **Statistics:** A significance notation, $P < 10^{-4}$, is displayed above the bars. The sample size $n=213$ is noted in the top right corner.

**Panel d: Silencing Setup Schematic (Pulvinar Inputs)**
This panel is a schematic diagram similar to Panel a, but focused on pulvinar inputs.
*   **Visual Components:** It shows "Silencing pulvinar inputs" and "Imaging pulvinar inputs."
*   **Optogenetic Elements:** Light wavelengths are indicated: "930 nm" and "594 nm."
*   **Genetic Markers:** It shows the expression of "GCaMP6f" and "eNpHR3.0-mCherry."
*   **Contextual Annotation:** The schematic includes a representation of the pulvinar structure.

**Panel e: Time Course Plot (All Boutons)**
This panel shows the average neural response across all boutons.
*   **Plot Type:** Line graph showing $\Delta F/F$ over time (x-axis).
*   **X-Axis:** Time, ranging from 0 to 2 seconds (s).
*   **Y-Axis:** $\Delta F/F$ (Z-scored), ranging from approximately -0.3 to 0.4.
*   **Curves:** Two lines are plotted: "LED off" (black line) and "LED on" (orange/yellow line).
*   **Annotations:** The panel is titled "All boutons (mean of all directions)." Above the plot, $n=1135$ is noted.

**Panel f: Statistical Comparison Plot (Grating Responsive Boutons)**
This panel compares the response of grating-responsive boutons.
*   **Plot Type:** Bar chart comparing mean $\Delta F/F$ values.
*   **X-Axis Category:** "Grating responsive boutons."
*   **Y-Axis:** Grating response ($\Delta F/F$, Z-scored), ranging from 0 to 2.
*   **Data Representation:** A single bar represents the mean response, with error bars.
*   **Statistics:** The significance notation $P = 0.014$ is displayed, and the sample size $n=198$ is noted.

**Panel g: Imaging Setup Schematic (V1 L2/3 Cells)**
This panel is a schematic diagram illustrating imaging in V1 layer 2/3 cells.
*   **Visual Components:** It shows a representation of the visual pathway, focusing on V1.
*   **Labels:** It specifies "Imaging V1 L2/3 cells" and shows the location of the pulvinar input.
*   **Optogenetic Elements:** Light wavelengths are indicated: "930 nm" and "594 nm."
*   **Genetic Markers:** It shows the expression of "GCaMP6f" and "mCherry."

**Panel h: Time Course Plot (Expected vs Unexpected)**
This panel compares neural activity under expected and unexpected conditions.
*   **Plot Type:** Line graph showing $\Delta F/F$ over time (x-axis).
*   **X-Axis:** Time, ranging from 0 to 2 seconds (s).
*   **Y-Axis:** $\Delta F/F$ (Z-scored), ranging from -0.2 to 0.4.
*   **Curves:** Two lines are plotted: "LED off" (black line) and "LED on" (orange/yellow line).
*   **Annotations:** The panel is divided into three sections: "Expected A3 or B4," "Unexpected C4 or D4," and "Expected C4 or D4."
    *   The first section shows $n=49$ with $P = 0.14$.
    *   The middle section shows $n=195$ with $P = 0.51$.
    *   The third section shows $n=82$ with $P = 0.15$.

### Contextual Caption Integration
The caption states: "Data Fig. 9 | Confirmation of optogenetic silencing and control sessions." This confirms that the panels demonstrate validation experiments for the optogenetic manipulation techniques used in the study.

Extended Data Fig. 9 | Confirmation of optogenetic silencing and control 
experiment for LED light stimulation. a, Schematic of the experimental 
design. Calcium activity of VIP cells in V1 was recorded while they were 
optogenetically silenced. b, Cell- and trial-averaged responses of VIP cells to 
unexpected stimulus A2 (familiar stimulus at unexpected position; left, n = 289 
from 5 mice) and unexpected stimulus C2 (right, n = 213 from 5 mice) with 
(amber) or without (black) VIP silencing. Lines and shading are mean and 
bootstrap 95% CI. c, Responses to unexpected A2 (left, n = 289, P < 1 × 10−4) and 
unexpected C2 (right, n = 213, P < 1 × 10−4) stimuli with (amber) and without 
(grey) VIP silencing. Hierarchical bootstrapping test. Bars and error bars are 
mean and 95% bootstrap CI. d, Schematic of the experimental design. Calcium 
activity of pulvinar boutons was recorded while they were optogenetically 
silenced during presentation of differently oriented, drifting grating stimuli 
(see Methods). e, Cell- and trial-averaged responses of all pulvinar boutons to 
all grating directions (left, n = 1,135 from 5 sessions, 3 mice) and of visually 
responsive boutons to the preferred grating direction (right, n = 198 from 5

sessions, 3 mice) with (amber) or without (black) pulvinar axonal silencing. 
Lines and shading are mean and bootstrap 95% CI. f, Responses of grating 
responsive boutons to preferred direction with (amber) and without (grey) 
pulvinar axonal silencing (n = 198, P = 0.014). Hierarchical bootstrapping test. 
Bars and error bars are mean and 95% bootstrap CI. g, Schematic of the 
experimental design. Calcium activity of V1 layer 2/3 cells was recorded during 
light stimulation without expression of opsins. mCherry was expressed in 
pulvinar neurons. h, Top: cell- and trial-averaged responses to expected stimulus 
A3 or B4 (left), unexpected stimulus C4 or D4 (middle) and expected C4 or D4 
(right) with or without light stimulation (amber and black, respectively). Lines 
and shading are mean and bootstrap 95% CI (n = 49, 195, 82, 3 mice; P = 0.14, 
P = 0.51, P = 0.15; for expected A3 or B4 responsive cells, unexpected C4 or D4 
responsive cells, and expected C4 or D4 responsive cells; Hierarchical 
bootstrapping test). Bottom: Responses of individual V1 neurons to stimuli 
indicated above with and without LED light stimulation (LED on vs LED off).


---

## Page 27

Article



### Overall Layout and Structure
The figure is structured into several rows of panels, with each row containing multiple sub-panels (e.g., Panel a has one schematic and three plots). The panels are grouped thematically, with the top section focusing on "VIP interneurons" and subsequent sections detailing different cell types or conditions (e.g., Pulvinar, Pulvinar/GCAmP).

### Detailed Panel Descriptions

#### Top Section: VIP Interneurons (Panels a, b, c)
**Panel a:** This is a schematic diagram illustrating the cellular context. It shows a simplified representation of neurons, including labels like "VIP cells," "GCAmP," and "V1 L2/3 cells." Arrows indicate connections or processes.
**Panel b:** This panel contains three scatter plots comparing activity under different conditions: "Expected A3 or B4," "Unexpected C4," and "Unexpected D4."
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)" for all three plots.
*   **Y-axis:** Labeled "LED on (z-scored $\Delta F/F$)" for all three plots.
*   **Data Points:** Each plot shows individual data points scattered across the plane, with a regression line fitted through them.
*   **Annotations:** Each plot includes statistical annotations: $n$ (number of samples) and a correlation coefficient ($r$). For example, in the first plot ("Expected A3 or B4"), $n=10$ and $r=0.83$.
**Panel c:** This panel also contains three scatter plots, mirroring the structure of Panel b.
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)" for all three plots.
*   **Y-axis:** Labeled "LED on (z-scored $\Delta F/F$)" for all three plots.
*   **Data Points:** Scatter plots with regression lines.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for each plot. For instance, the first plot shows $n=123$ and $r=-0.85 \pm 10^{-3}$.

#### Middle Section: Pulvinar (Panels d, e)
**Panel d:** This panel contains three scatter plots, similar in structure to Panel b.
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)" for all three plots.
*   **Y-axis:** Labeled "LED on (z-scored $\Delta F/F$)" for all three plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are provided for each plot.

**Panel e:** This panel contains three scatter plots, similar in structure to Panel c.
*   **X-axis:** Labeled "LED off (z-scored $\Delta F/F$)" for all three plots.
*   **Y-axis:** Labeled "LED on (z-scored $\Delta F/F$)" for all three plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are provided for each plot.

#### Lower Middle Section: Pulvinar/GCAmP (Panels f, g)
**Panel f:** This panel contains two scatter plots.
*   **X-axis:** Labeled "Expected C4 or D4 (LED off, z-scored $\Delta F/F$)" for the left plot and "Expected C4 or D4 (LED off, z-scored $\Delta F/F$)" for the right plot.
*   **Y-axis:** Labeled "Unexpected C4 or D4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

**Panel g:** This panel contains two scatter plots, structurally similar to Panel f.
*   **X-axis:** Labeled "Expected C4 or D4 (LED off, z-scored $\Delta F/F$)" for both plots.
*   **Y-axis:** Labeled "Unexpected C4 or D4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

#### Lower Section: Pulvinar (Panels h, i)
**Panel h:** This panel contains two scatter plots.
*   **X-axis:** Labeled "Expected C4 or D4 (LED off, z-scored $\Delta F/F$)" for both plots.
*   **Y-axis:** Labeled "Unexpected C4 or D4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

**Panel i:** This panel contains two scatter plots, structurally similar to Panel h.
*   **X-axis:** Labeled "Expected A3 or B4 (LED off, z-scored $\Delta F/F$)" for both plots.
*   **Y-axis:** Labeled "Unexpected C4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

#### Bottom Section: Pulvinar/GCAmP (Panels j, k)
**Panel j:** This panel contains two scatter plots.
*   **X-axis:** Labeled "Expected A3 or B4 (LED off, z-scored $\Delta F/F$)" for both plots.
*   **Y-axis:** Labeled "Unexpected C4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

**Panel k:** This panel contains two scatter plots, structurally similar to Panel j.
*   **X-axis:** Labeled "Expected C4 or D4 (LED off, z-scored $\Delta F/F$)" for both plots.
*   **Y-axis:** Labeled "Unexpected C4 (LED on, z-scored $\Delta F/F$)" for both plots.
*   **Annotations:** Statistical annotations ($n$ and $r$) are present for both plots.

#### Final Rows (Panels l through p)
These panels continue the pattern of scatter plots, comparing expected vs. unexpected activity across different conditions:

**Panel l:** Two scatter plots with annotations ($n$ and $r$).
**Panel m:** Two scatter plots with annotations ($n$ and $r$).
**Panel n:** Two scatter plots comparing "Expected C4 or D4" vs. "Unexpected C4 or D4," with annotations ($n$ and $r$).
**Panel o:** Two scatter plots, structurally similar to Panel n.
**Panel p:** Two scatter plots comparing "Expected C4 or D4" vs. "Unexpected C4 or D4," with annotations ($n$ and $r$).

In summary, the figure is a dense compilation of comparative scatter plots used to quantify correlations between baseline activity (LED off) and induced activity (LED on) across various neuronal populations (VIP interneurons, Pulvinar) under different experimental expectations.

Extended Data Fig. 10 | See next page for caption.


---

## Page 28

Extended Data Fig. 10 | Effect of optogenetic silencing of VIP interneurons 
or pulvinar input to V1 in C and D sessions. Related to Fig. 3. a-e, Same as 
Fig. 3e–g, but C session (b and c) and D session (d and e) are plotted separately. 
a, Schematic of the experiment. Calcium activity of V1 layer 2/3 cells was 
recorded while VIP cells were optogenetically silenced in 50% of trials. VIP cell 
silencing started at the onset of visual stimuli and lasted for 3 s. b, Top: cell- and 
trial-averaged responses of neurons significantly responsive to the presented 
stimuli to expected grating A3 or B4 (left, P = 0.83, Hierarchical bootstrapping 
test, n = 32 cells, 4 mice), unexpected grating C4 (middle, P < 1 × 10−4, n = 123) 
and expected grating C4 (right, P = 0.0024, n = 42) with (amber) or without 
(black) VIP silencing. Lines and shading are mean and bootstrap 95% CI. 
Bottom: responses of individual V1 neurons to the grating stimulus indicated 
above during VIP silencing (LED on), plotted against responses to the same 
stimulus in control trials (LED off). c, Effect of VIP neuron silencing (LED on - 
LED off during unexpected grating C4) plotted against the strength of 
prediction error signals (response to unexpected C4 - response to expected 
C4). Pearson correlation: r = −0.85, P = 8.5 × 10−35. d, Top: cell- and trial-averaged 
responses of neurons significantly responsive to the presented stimuli to 
expected A3 or B4 (left, P = 0.11, Hierarchical bootstrapping test, n = 55 cells, 3 
mice), unexpected D4 (middle, P < 1 × 10−4, n = 446) and expected D4 (right, P < 1 
× 10−4, n = 181) with (amber) or without (black) VIP silencing. Lines and shading 
are mean and bootstrap 95% CI. Bottom: responses of individual neurons to the 
visual stimulus indicated above during VIP silencing (LED on), plotted against 
responses to the same stimulus in control trials (LED off). e Effect of VIP neuron

silencing (LED on - LED off during unexpected stimulus D4) plotted against the 
strength of prediction error signals (response to unexpected D4 - response to 
expected D4). Pearson correlation: r = −0.66, P = 1.3 × 10−57. f, Effect of VIP 
neuron silencing (LED on - LED off during unexpected C4 or D4) plotted against 
response to expected C4 or D4 for individual V1 neurons; n = 569. Pearson 
correlation: r = −0.27, P = 4.8 × 10−11. g, Response to unexpected C4 or D4 with 
VIP silencing plotted against response to expected C4 or D4 without VIP 
silencing; n = 569. Pearson correlation: r = 0.81, P = 2.1 × 10−133. h, Strength of 
prediction error signal (response to unexpected C4 or D4 - response to 
expected C4 or D4) with VIP silencing plotted against strength of prediction 
error signal without VIP silencing; n = 569. Pearson correlation: r = 0.76,  
P = 8.5 × 10−109. i-p, Same as a-h but for optogenetic silencing of pulvinar inputs. 
i, Calcium activity of V1 layer 2/3 cells was recorded while pulvinar inputs were 
optogenetically silenced in 50% of trials. j, Expected grating A3 or B4 (left, 
P = 0.21, Hierarchical bootstrapping test, n = 120 cells, 7 mice), unexpected 
grating C4 (middle, P < 1 × 10−4, n = 301) and expected grating C4 (right, P = 0.77, 
n = 92) responses with (amber) or without (black) pulvinar axon silencing.  
k, n = 301 cells. Pearson correlation: r = −0.47, P = 1.1 × 10−17. l, Expected 
stimuli A3 or B4 (left, P = 0.17, Hierarchical bootstrapping test, n = 38 cells, 2 
mice), unexpected D4 (middle, P < 1 × 10−4, n = 227) and expected D4 (right, 
P = 0.027, n = 94) responses with (amber) or without (black) VIP silencing. m, 
n = 227. Pearson correlation: r = −0.56, P = 6.3 × 10−20. n, n = 528. Pearson 
correlation: r = −0.0052, P = 0.23. o, n = 528. Pearson correlation: r = 0.55, P = 7.7 
× 10−43. p, n = 528. Pearson correlation: r = 0.91, P = 2.0 × 10−198.


---

## Page 29

Article



### Panels a–e: Running Speed Plots (Time-Series Data)

Panels **a** through **e** are time-series plots showing "Running speed ($\text{cm/s}$)" on the y-axis versus "Time from onset (s)" on the x-axis. Each panel compares two conditions: "Activation" and "Silencing."

*   **Panel a (Pulvinar inputs):** Shows running speed over time. The plot displays two lines: one for "Activation" and one for "Silencing." Below the main graph, there are box plots comparing running speed between conditions. The text indicates $n=6$ and $P=1$.
*   **Panel b (VIP cells):** Similar time-series plot comparing "Activation" and "Silencing" for VIP cells. Box plots below show the comparison, with $n=6$ and $P=1$.
*   **Panel c (Pulvinar inputs):** Another time-series plot for Pulvinar inputs. Box plots below show the comparison, with $n=9$ and $P=0.20$.
*   **Panel d (VIP cells):** Another time-series plot for VIP cells. Box plots below show the comparison, with $n=6$ and $P=0.31$.
*   **Panel e (SOM cells):** A time-series plot for SOM cells. Box plots below show the comparison, with $n=5$ and $P=0.31$.

In all panels (a-e), the legend indicates that the solid line represents "LED on" and the dashed line represents "LED off."

### Panels f–i: Schematic Diagrams and Activity Plots (Cellular/Circuit Level)

Panels **f** through **i** transition to schematic representations and corresponding activity plots.

*   **Panel f (Schematic):** This is a schematic diagram illustrating neural layers and cell types. It shows a vertical structure with labels: "Pulvinar," "VIP-Cre," and "ChrimsonR." Below this, there is a representation of cortical layers: $\text{V1}$, $\text{L2/3 cells}$, and a schematic of the cell types involved.
*   **Panel g (Activity Plot):** This plot shows "z-scored $\Delta F/F$" on the y-axis versus time (implied, as it shows a transient response). It is labeled "LED off" and includes data points for $n=217$.
*   **Panel h (Activity Plot):** This plot shows "z-scored $\Delta F/F$" on the y-axis versus time. It is labeled "LED on" and includes data points for $n=217$.
*   **Panel i (Selectivity Plot):** This plot compares "Visual stimulus response" on the y-axis against a categorical x-axis: "Responsive to A," "Non-selective," and "Highly selective responsive to B." The plot shows data points for both "LED on" and "LED off," with $P=0.031$ noted above the plot, indicating a significant difference between conditions.

### Panels j–m: Schematic Diagrams and Activity Plots (SOM/Cortical Level)

Panels **j** through **m** continue the theme with SOM cells and cortical layers.

*   **Panel j (Schematic):** A schematic diagram similar to Panel f, but focused on SOM cells. It shows "SOM-Cre" and "ChrimsonR." The cortical layers are labeled: $\text{V1}$, $\text{L2/3 cells}$, and a representation of the SOM cell type.
*   **Panel k (Activity Plot):** This plot shows "z-scored $\Delta F/F$" on the y-axis versus time. It is labeled "LED off" and includes data points for $n=179$.
*   **Panel l (Activity Plot):** This plot shows "z-scored $\Delta F/F$" on the y-axis versus time. It is labeled "LED on" and includes data points for $n=179$.
*   **Panel m (Selectivity Plot):** This plot compares "Visual stimulus response" on the y-axis against a categorical x-axis: "Responsive to A," "Non-selective," and "Highly selective responsive to B." It shows data points for both "LED on" and "LED off," with $P=0.25$ noted above the plot, indicating a non-significant difference between conditions.

Extended Data Fig. 11 | See next page for caption.


---

## Page 30

Extended Data Fig. 11 | Effect of optogenetic manipulation of pulvinar 
inputs, VIP cells and SOM cells on running speed and visual responses of V1 
layer 2/3 cells (related to Fig. 4). a-e, Running speed with (amber) or without 
(black) optogenetic manipulation for activation of pulvinar axons (a), activation 
of VIP neurons (b), co-activation of pulvinar axons and VIP neurons (c), activation 
of pulvinar axons and simultaneous silencing of SOM cells (d), and silencing  
of SOM cells (e). Top: Lines and shading are mean and bootstrap 95% CI. Orange 
shading indicates time of optogenetic stimulation. Bottom: Data from the 
individual animals are shown separately. Data from the same animals are 
connected by lines. Black horizontal bars represent mean across animals.  
P-values from two-sided signed-rank test. f-i, Same as Fig. 4d, but optogenetic 
stimulation was paired with the grating stimulus A3 instead of B2. f, Schematic 
of the experimental design. The activity of V1 layer 2/3 cells was recorded  
while pulvinar axons and VIP cells were optogenetically co-stimulated. 
Stimulation started 0.1 s after visual stimulus onset and lasted for 1 s 
(see methods). g, Response strength to grating stimulus A3 with and without 
co-stimulation of pulvinar inputs and VIP cells. n = 217 grating A or B responsive 
cells, 6 sessions from 6 mice. Inset: Cell-averaged calcium responses with 
(amber) or without (black) optogenetic stimulation. h, Effect of optogenetic 
stimulation (difference of response to grating A3 with and without laser 
stimulation) plotted against response selectivity (difference in response 
strength between stimulus A and B divided by the sum of responses) of

individual V1 neurons. i, Calcium response strength to grating stimulus A3 of B 
selective cells (left, n = 6 mice, P = 0.84), and non-selective (selectivity A vs 
B < 0.6, middle, n = 6 mice, P = 0.44, two-sided signed-rank test) and highly 
selective (selectivity A vs B > 0.8, right, n = 6 mice, P = 0.031, two-sided signed-
rank test) grating A3 responsive cells in V1 layer 2/3 with (amber) or without 
(grey) optogenetic stimulation. j-m, Same as f-i, but for optogenetic silencing 
of SOM cells during presentation of grating stimulus B2. j, Schematic of the 
experimental design. The activity of V1 layer 2/3 cells was recorded while SOM 
cells were optogenetically silenced for 3 s, starting at grating stimulus onset.  
k, Grating B2 responses with and without the silencing of SOM cells. n = 179 
grating A or B responsive cells, 5 sessions from 3 mice, P < 1 × 10−4, Hierarchical 
bootstrapping test. l, Effect of optogenetic stimulation (difference of response 
to grating B2 with and without laser stimulation) plotted against response 
selectivity (difference in response strength between stimulus B and A divided 
by the sum of responses) of individual V1 neurons. m, Calcium response 
strength to grating stimulus B2 of A-selective neurons (left, n = 5 sessions  
from 3 mice, P = 0.19), and non-selective (selectivity B vs A < 0.6, middle, n = 5 
sessions from 3 mice, P = 0.81, two-sided signed-rank test) and highly selective 
(selectivity B vs A > 0.8, right, n = 5 sessions from 3 mice, P = 0.25, two-sided 
signed-rank test) grating B2 responsive cells in V1 layer 2/3 with (amber) or 
without (grey) optogenetic stimulation.


---

## Page 31

Article



### Panel a: Schematic Diagram
Panel **a** is a schematic diagram illustrating the inputs to VIP cells. It shows:
*   A box labeled "VIP neurons" on the left, which has an arrow pointing towards a central node.
*   A box labeled "Pulvinar inputs" on the left, also pointing towards the central node.
*   A box labeled "VIP cells" on the right, which receives input from the central node.
*   The diagram includes labels indicating specific cell types or regions: "V1," "VIP-Cre; Ai14," and a general label "VIP cells."

### Panel b: Line Graph (LED on vs. LED off)
Panel **b** contains a line graph comparing neural activity under two conditions: "LED on" and "LED off."
*   **Y-axis:** Labeled "Neural activity (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Time (s)".
*   The graph shows two distinct traces: one for "LED on" and one for "LED off." Both traces show fluctuations over time, with the y-axis ranging approximately from -0.5 to 1.0.

### Panel c: Line Graph (Expected vs. Unexpected)
Panel **c** is a line graph comparing neural activity based on prediction error: "Expected" versus "Unexpected."
*   **Y-axis:** Labeled "Neural activity (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Time (s)".
*   The graph displays two traces: one for "Expected" and one for "Unexpected."

### Panel d: Line Graph (Expected B4 vs. Unexpected C4 or D4)
Panel **d** is a line graph comparing activity in different brain regions under expected and unexpected conditions.
*   **Y-axis:** Labeled "Neural activity (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Time (s)".
*   The graph shows two traces: one for "Expected B4" and one for "Unexpected C4 or D4."

### Panel e: Line Graph (Recruited vs. Other cells)
Panel **e** is a line graph comparing activity in recruited versus other cells.
*   **Y-axis:** Labeled "Neural activity (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Time (s)".
*   The graph displays two traces: one for "Recruited cells" and one for "Other cells."

### Panel f: Line Graph (Expected vs. Unexpected)
Panel **f** is a line graph comparing activity under expected and unexpected conditions, similar in structure to Panel c.
*   **Y-axis:** Labeled "Neural activity (z-scored $\Delta F/F$)."
*   **X-axis:** Labeled "Time (s)".
*   The graph shows two traces: one for "Expected" and one for "Unexpected."

### Panel g: Representative Images (Mouse 1-4)
Panel **g** consists of four rows, one for each mouse (Mouse 1 through Mouse 4). Each row contains two representative images:
*   The left image is labeled "LD" (likely representing a baseline or low-demand state).
*   The right image is labeled "LP" (likely representing a high-demand or perturbed state).
*   These images appear to be fluorescence microscopy snapshots showing neuronal activity, characterized by bright, filamentous structures (likely dendritic or axonal arborizations) visualized against a darker background.

### Panel h: Line Graphs (Session Data for Mouse 1-4)
Panel **h** consists of four rows, corresponding to the four mice shown in Panel g. Each row contains two line graphs:
*   **Left Graph (Session 1):** Plots "Visual stimulus response (z-scored $\Delta F/F$)" on the y-axis against "Time (s)" on the x-axis.
*   **Right Graph (Session 2):** Plots "Visual stimulus response (z-scored $\Delta F/F$)" on the y-axis against "Time (s)" on the x-axis.
*   In both graphs, data points are plotted, and a fitted line (likely representing the average response) is visible. The x-axis ranges from approximately -3 to 3 seconds, and the y-axis ranges from -3 to 3.

Extended Data Fig. 12 | See next page for caption.


---

## Page 32

Extended Data Fig. 12 | Effect of optogenetic stimulation of pulvinar inputs 
on visual responses of VIP cells in V1 layer 2/3, and expression of ChrimsonR- 
tdTomato and LED effect of individual animals used in Fig. 5. a, Schematic  
of the experimental design. The activity of VIP cells was recorded while 
pulvinar axons were optogenetically stimulated for 3 s, starting at the onset of 
the visual stimulus. b, Single-cell responses of pulvinar-recruited VIP cells 
(individual rows, n = 69 cells, 7 sessions from 5 mice) and other non-recruited 
VIP cells (individual rows, n = 310 cells, 7 sessions from 5 mice) to expected B4, 
unexpected C4 or D4 and expected C4 or D4 stimuli with (right) and without 
(left) optogenetic stimulation (see Methods). c, Cell-averaged calcium 
responses with (amber) or without (black) optogenetic stimulation of pulvinar-
recruited and other non-recruited VIP cells. Lines and shaded regions are mean 
and bootstrap 95% CI. d, Visual stimulus responses of individual VIP neurons 
without optogenetic stimulation plotted against the effect of pulvinar stimulation 
(difference of visual responses with and without optogenetic stimulation).  
e, Strength of calcium response to expected B4 (black), unexpected C4 or D4 
(red) and expected C4 or D4 (blue) stimuli of pulvinar-recruited VIP cells (left, 
n = 69, B4 vs unexpected C4/D4: P < 10−4; unexpected vs expected C4/D4: 
P < 10−4, Hierarchical bootstrapping test with Bonferroni correction) and other

VIP cells (right, n = 310, B4 vs unexpected C4/D4: P < 10−4; unexpected vs 
expected C4/D4: P < 10−4, Hierarchical bootstrapping test with Bonferroni 
correction). 7 sessions from 5 mice. Bars and error bars indicate mean and 95% 
bootstrap CI. f, Responses to expected B4 (left), unexpected C4 or D4 (middle) 
and expected C4 or D4 (right) stimuli with (amber) and without (black) pulvinar 
stimulation. n = 379 cells from 7 sessions, 5 mice, LED on vs off during expected 
B4 stimulus: P < 1 × 10−4; LED on vs off during unexpected C4 or D4 stimulus, 
P = 4.0 × 10−4; LED on vs off during expected C4 or D4 stimulus, P = 0.48; 
Hierarchical bootstrapping test. Bars and error bars are mean and 95% 
bootstrap CI. g, Coronal slice through the pulvinar injection site (LP, right) and 
through the laterodorsal nucleus of thalamus (LD, left), showing specific 
expression of ChrimsonR-tdTomato (red) in LP, not in LD. Scale bars: 100 μm.  
h, Same as Fig. 5d, but plotted for individual mice. Visual stimulus responses of 
individual SOM neurons to expected B4 stimulus (left), unexpected C4 or D4 
stimulus (middle, in block 1) and expected C4 or D4 stimulus (right, in late block 
2) plotted against the effect of pulvinar stimulation (difference in strength of 
visual stimulus responses with and without optogenetic pulvinar axon 
stimulation) for recruited (brown) and other (black) SOM cells.


---

## Page 33



**Figure Description:**

1. **Overall Layout & Structure**: The image consists solely of text presented as a logo, centered horizontally. It is not structured into panels (A, B, C) or composed of scientific diagrams like plots, flow charts, or circuit schematics.
2. **Visual Components & Symbols**: The visual components are typographic characters forming the words "nature portfolio." There are no shapes, nodes, arrows, or color-coding indicative of a scientific diagram.
3. **Labels, Keys & Legends**: The legible text within the image is: "nature portfolio".
4. **Data Trends & Details**: As this is a logo, there are no data trends or axes to describe.
5. **Contextual Caption Integration**: No caption was provided, but based on the visual content, this image serves as branding for "Nature Portfolio."



Here is a detailed description of its visual and structural contents:

**1. Overall Layout & Structure:**
The figure is dominated by a single, tall, solid red rectangular shape that spans the entire visible height of the image. The structure is linear and monolithic, lacking distinct panels (A, B, C) or complex internal divisions.

**2. Visual Components & Symbols:**
*   **Background/Main Element:** A uniform, bright red vertical bar.
*   **Text Elements:** Several lines of white text are overlaid on the red background, positioned along the left side of the bar.
*   **Bottom Element:** Near the bottom edge, there is a small white symbol ($\#$) centered within the red bar.

**3. Labels, Keys & Legends:**
The legible text elements are:
*   "nature portfolio | reporting summary" (This appears to be a multi-line title or section header).
*   "April 2023" (This is located near the bottom of the bar).

**4. Data Trends & Details:**
As this is a graphic element and not a plot, there are no axes, curves, or data trends to report.

**5. Contextual Caption Integration:**
The text elements ("nature portfolio | reporting summary" and "April 2023") suggest this graphic functions as a header or branding element for a specific report or section within the document, likely related to "nature portfolio" reporting for April 2023. The symbol ($\#$) at the bottom is an isolated marker within this graphic context.

Corresponding author(s):

Last updated by author(s):

Reporting Summary

Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency 
in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist.

Please do not complete any field with "not applicable" or n/a.  Refer to the help text for what text to use if an item is not relevant to your study. 
For final submission: please carefully check your responses for accuracy; you will not be able to make changes later.

Statistics

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.

n/a Confirmed

The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement

A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly

The statistical test(s) used AND whether they are one- or two-sided 
Only common tests should be described solely by name; describe more complex techniques in the Methods section.

A description of all covariates tested

A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons

A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) 
AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)

For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted 
Give P values as exact values whenever suitable.

For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings

For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes

Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated

Our web collection on statistics for biologists contains articles on many of the points above.

Software and code

Policy information about availability of computer code

Data collection

Data analysis

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and 
reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information.

Data

Policy information about availability of data

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:

- Accession codes, unique identifiers, or web links for publicly available datasets 
- A description of any restrictions on data availability 
- For clinical datasets or third party data, please ensure that the statement adheres to our policy



Sonja Hofer

09. 06. 2024

ScanImage, Labview

Matlab 2018b, 2021a

The data that support the main findings of this study are publicly available at https://doi.org/10.5281/zenodo.11403111. 
Other data that are generated in this study are available from the corresponding author upon reasonable request. 
Source data are provided with this paper.


---

## Page 34



Here is the exhaustive description based on the visual evidence:

**1. Overall Layout & Structure:**
The image is dominated by a tall, solid red vertical bar that spans the entire visible area. Text elements are positioned along this bar.

**2. Visual Components & Symbols:**
*   **Background:** A uniform, bright red vertical field.
*   **Text Elements:** White text is overlaid on the red background, suggesting a title or section heading.
*   **Bottom Element:** Near the bottom of the visible area, there is a small white hash symbol ($\#$).

**3. Labels, Keys & Legends:**
The following text is legible:
*   Near the top/middle section, vertically oriented text reads: "nature portfolio | reporting summary".
*   Near the bottom of the visible area, there is a date: "April 2023".
*   At the very bottom, there is a hash symbol: "\#".

**4. Data Trends & Details:**
As this is not a plot or graph, there are no data trends to report.

**5. Contextual Caption Integration:**
No contextual caption was provided, so no specific elements can be identified based on external context. The visual evidence suggests this is a stylized header or divider page for a "nature portfolio | reporting summary" dated April 2023.

Research involving human participants, their data, or biological material

Policy information about studies with human participants or human data. See also policy information about sex, gender (identity/presentation), 
and sexual orientation and race, ethnicity and racism.

Reporting on sex and gender

Reporting on race, ethnicity, or 
other socially relevant 
groupings

Population characteristics

Recruitment

Ethics oversight

Note that full information on the approval of the study protocol must also be provided in the manuscript.

Field-specific reporting

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.

Life sciences
Behavioural & social sciences
 Ecological, evolutionary & environmental sciences

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf

Life sciences study design

All studies must disclose on these points even when the disclosure is negative.

Sample size

Data exclusions

Replication

Randomization

Blinding

Behavioural & social sciences study design

All studies must disclose on these points even when the disclosure is negative.

Study description

Research sample

Sampling strategy

Data collection

Timing

Data exclusions

Non-participation

Randomization

Not applicable

Not applicable

Not applicable

Not applicable

Not applicable

Matches standards in the field (Voitov et al, Nature, 2022, Kanamori and Mrsic-Flogel, Neuron, 2022)

Data excluded if imaging quality insufficient or expression of constructs failed or in wrong location

Main results contain multiple data sets in which findings could be replicated (see numbers of animals for biological replicates)

In our study, stimulus presentation and optogenetic manipulation were randomized by software.

In our study, stimulus presentation and optogenetic manipulation were randomized by software.


---

## Page 35



Here is the exhaustive description based strictly on the visual evidence:

**1. Overall Layout & Structure:**
The primary element is a tall, solid red vertical bar that dominates the frame. Text elements are positioned adjacent to or overlaid on this red background, suggesting a title or section marker rather than a data visualization.

**2. Visual Components & Symbols:**
*   **Red Bar:** A continuous, uniform red vertical rectangle spans most of the height of the image.
*   **Text Elements:** White text is visible against the red background, indicating section titles or document metadata.

**3. Labels, Keys & Legends:**
The following legible text elements are present:
*   Near the top of the red bar, vertically oriented text reads: "nature portfolio | reporting summary".
*   Near the bottom of the red bar, there is a date label: "April 2023".
*   At the very bottom, there is a symbol: "#".

**4. Data Trends & Details:**
As this is not a plot or graph, there are no axes, data trends, or quantitative details to report.

**5. Contextual Caption Integration:**
No contextual caption was provided, so no specific elements can be identified based on external context. The visual evidence suggests this is a stylized header or divider page element for a "nature portfolio | reporting summary" dated April 2023.

Ecological, evolutionary & environmental sciences study design

All studies must disclose on these points even when the disclosure is negative.

Study description

Research sample

Sampling strategy

Data collection

Timing and spatial scale

Data exclusions

Reproducibility

Randomization

Blinding

Did the study involve field work?
Yes
No

Field work, collection and transport

Field conditions

Location

Access & import/export

Disturbance

Reporting for specific materials, systems and methods

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material,
system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.

Materials & experimental systems

n/a Involved in the study

Antibodies

Eukaryotic cell lines

Palaeontology and archaeology

Animals and other organisms

Clinical data

Dual use research of concern

Plants

Methods

n/a
Involved in the study

ChIP-seq

Flow cytometry

MRI-based neuroimaging

Antibodies

Antibodies used

Validation


---

## Page 36



Here is a detailed description based on the visual evidence:

**1. Overall Layout & Structure:**
The primary structure is a tall, uninterrupted vertical red rectangle that spans the height of the visible area. Text elements are positioned along this red bar, suggesting a title or section header format.

**2. Visual Components & Symbols:**
*   **Background:** A solid, vibrant red color dominates the entire frame.
*   **Text Placement:** Text is positioned vertically along the left side of the red bar, and a date/identifier is placed near the bottom.

**3. Labels, Keys & Legends:**
The following text elements are visible:

*   **Vertical Text (Top/Upper Section):** The text is oriented vertically, reading from top to bottom:
    *   `nature portfolio | reporting summary` (This text is stacked vertically).

*   **Bottom Text/Identifier:** Near the bottom of the red bar, there are two distinct pieces of text:
    *   `April 2023` (This appears horizontally aligned near the bottom).
    *   A hash symbol (`#`) is present below the date, also near the bottom.

**4. Data Trends & Details:**
As this is a graphic element and not a data plot, there are no axes, curves, or quantifiable trends to describe.

**5. Contextual Caption Integration:**
The visible text elements (`nature portfolio | reporting summary`, `April 2023`) strongly suggest this visual functions as a header or branding element indicating the source and date of the document section.

Eukaryotic cell lines

Policy information about cell lines and Sex and Gender in Research

Cell line source(s)

Authentication

Mycoplasma contamination

Commonly misidentified lines
(See ICLAC register)

Palaeontology and Archaeology

Specimen provenance

Specimen deposition

Dating methods

Tick this box to confirm that the raw and calibrated dates are available in the paper or in Supplementary Information.

Ethics oversight

Note that full information on the approval of the study protocol must also be provided in the manuscript.

Animals and other research organisms

Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research, and Sex and Gender in 
Research

Laboratory animals

Wild animals

Reporting on sex

Field-collected samples

Ethics oversight

Note that full information on the approval of the study protocol must also be provided in the manuscript.

Clinical data

Policy information about clinical studies
All manuscripts should comply with the ICMJE guidelines for publication of clinical research and a completed CONSORT checklist must be included with all submissions.

Clinical trial registration

Study protocol

Data collection

Outcomes

Dual use research of concern

Policy information about dual use research of concern

Hazards

Could the accidental, deliberate or reckless misuse of agents or technologies generated in the work, or the application of information presented 
in the manuscript, pose a threat to:

No wild animals were used in the study

Both male and female were used in the study

Mice. See manuscript methods for mouse lines used

No field collected samples were used in the study

This study was approved by institutional ethics and UK Home Office


---

## Page 37



Here is the exhaustive description based on the visual evidence:

**1. Overall Layout & Structure:**
The primary structure is a tall, uninterrupted vertical red rectangle that spans the majority of the image height. The content is organized linearly along this vertical axis, with text elements placed against the red background.

**2. Visual Components & Symbols:**
*   **Background:** A solid, vibrant red color dominates the entire frame.
*   **Text Elements:** Several lines of text are overlaid on this red background, suggesting they function as titles or section markers.
*   **Bottom Element:** Near the bottom edge, there is a small, white or light-colored symbol resembling a hash tag ($\#$).

**3. Labels, Keys & Legends:**
The following text is legible:
*   Near the top section (vertically oriented): "nature portfolio | reporting summary"
*   Mid-section: "April 2023"
*   Bottom section (adjacent to the hash symbol): "\#"

**4. Data Trends & Details:**
As this is not a plot or graph, there are no axes, data trends, or quantitative details to report.

**5. Contextual Caption Integration:**
The text elements ("nature portfolio | reporting summary," "April 2023") strongly suggest this visual element serves as a branding or section header/footer indicating the document's context (a Nature portfolio report) and date. The hash symbol ($\#$) is a common stylistic element used in digital documents or presentations.

No
Yes

Public health

National security

Crops and/or livestock

Ecosystems

Any other significant area

Experiments of concern

Does the work involve any of these experiments of concern:

No
Yes

Demonstrate how to render a vaccine ineffective

Confer resistance to therapeutically useful antibiotics or antiviral agents

Enhance the virulence of a pathogen or render a nonpathogen virulent

Increase transmissibility of a pathogen

Alter the host range of a pathogen

Enable evasion of diagnostic/detection modalities

Enable the weaponization of a biological agent or toxin

Any other potentially harmful combination of experiments and agents

Novel plant genotypes

Seed stocks

Authentication

Plants

ChIP-seq

Data deposition

Confirm that both raw and final processed data have been deposited in a public database such as GEO.

Confirm that you have deposited or provided access to graph files (e.g. BED files) for the called peaks.

Data access links 
May remain private before publication.

Files in database submission

Genome browser session 
(e.g. UCSC)

Methodology

Replicates

Sequencing depth

Antibodies

Peak calling parameters

Data quality


---

## Page 38



Here is the exhaustive description based on the visible components:

**1. Overall Layout & Structure:**
The primary structure is a tall, solid red vertical bar that dominates the frame. Text elements are positioned along or adjacent to this bar.

**2. Visual Components & Symbols:**
*   **Red Bar:** A continuous, solid red vertical rectangle forms the main background element.
*   **Text Placement:** Text is positioned along the left edge of this red bar, suggesting it might be a running header or section title.

**3. Labels, Keys & Legends:**
The following text fragments are visible:
*   Along the top left edge of the red bar, there is text that reads: "nature portfolio | reporting summary".
*   Near the bottom of the visible red bar, there is a date label: "April 2023".
*   At the very bottom, there is a small symbol: "#".

**4. Data Trends & Details:**
Since the image consists only of a colored bar and text labels, there are no discernible data trends, axes, or plotted variables.

**5. Contextual Caption Integration:**
No specific contextual caption was provided to interpret the meaning of "nature portfolio | reporting summary" or "April 2023," so these are described purely as textual labels within the visual structure.

Software

Flow Cytometry

Plots

Confirm that:

The axis labels state the marker and fluorochrome used (e.g. CD4-FITC).

The axis scales are clearly visible. Include numbers along axes only for bottom left plot of group (a 'group' is an analysis of identical markers).

All plots are contour plots with outliers or pseudocolor plots.

A numerical value for number of cells or percentage (with statistics) is provided.

Methodology

Sample preparation

Instrument

Software

Cell population abundance

Gating strategy

Tick this box to confirm that a figure exemplifying the gating strategy is provided in the Supplementary Information.

Magnetic resonance imaging

Experimental design

Design type

Design specifications

Behavioral performance measures

Imaging type(s)

Field strength

Sequence & imaging parameters

Area of acquisition

Diffusion MRI
Used
Not used

Preprocessing

Preprocessing software

Normalization

Normalization template

Noise and artifact removal

Volume censoring

Statistical modeling & inference

Model type and settings

Effect(s) tested


---

## Page 39



Here is the exhaustive description based on the visible components:

**1. Overall Layout & Structure:**
The primary structure is a tall, uninterrupted vertical red rectangle that spans the majority of the image height. There are no discernible panels (A, B, C) or complex internal divisions within the red field.

**2. Visual Components & Symbols:**
*   **Background/Container:** A solid, vibrant red vertical bar.
*   **Text Elements:** Several lines of white text are overlaid on the red background, positioned near the top and bottom.
*   **Symbols:** A hash symbol ($\#$) is visible near the bottom right corner, rendered in white.

**3. Labels, Keys & Legends:**
The following text is legible:
*   Near the top center/left, stacked vertically: "nature portfolio | reporting summary"
*   Near the bottom right corner, in a smaller font: "April 2023"
*   At the very bottom, aligned to the right: "\#"

**4. Data Trends & Details:**
As this is not a plot or graph, there are no axes, data trends, or quantitative details to report.

**5. Contextual Caption Integration:**
No contextual caption was provided, so no specific scientific elements (cell types, layers, etc.) can be identified. The visible text suggests this element is related to a "nature portfolio" or "reporting summary" dated "April 2023."

Specify type of analysis:
Whole brain
ROI-based
Both

Statistic type for inference

(See Eklund et al. 2016)

Correction

Models & analysis

n/a Involved in the study

Functional and/or effective connectivity

Graph analysis

Multivariate modeling or predictive analysis

Functional and/or effective connectivity

Graph analysis

Multivariate modeling and predictive analysis

This checklist template is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give 
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in 
the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by 
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/
