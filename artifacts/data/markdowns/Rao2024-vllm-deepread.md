## Page 1

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1221

nature neuroscience

https://doi.org/10.1038/s41593-024-01673-9
Perspective
A sensory–motor theory of the neocortex

Rajesh P. N. Rao 
  1,2

Recent neurophysiological and neuroanatomical studies suggest a close 
interaction between sensory and motor processes across the neocortex. 
Here, I propose that the neocortex implements active predictive coding 
(APC): each cortical area estimates both latent sensory states and actions 
(including potentially abstract actions internal to the cortex), and the cortex 
as a whole predicts the consequences of actions at multiple hierarchical 
levels. Feedback from higher areas modulates the dynamics of state and 
action networks in lower areas. I show how the same APC architecture can 
explain (1) how we recognize an object and its parts using eye movements, 
(2) why perception seems stable despite eye movements, (3) how we learn 
compositional representations, for example, part–whole hierarchies, (4) 
how complex actions can be planned using simpler actions, and (5) how we 
form episodic memories of sensory–motor experiences and learn abstract 
concepts such as a family tree. I postulate a mapping of the APC model to the 
laminar architecture of the cortex and suggest possible roles for cortico–
cortical and cortico–subcortical pathways.

The predictive coding theory of cortical function, proposed in this jour-
nal in 1999 by the author and Ballard1, has been the subject of increasing 
attention in recent years2–4. However, as originally proposed, the theory 
ignored a fundamental aspect of perception, namely, that perception is 
action based: we move our eyes about three times a second to recognize 
objects in a scene, orient our heads to localize sounds, use our fingers to 
identify objects by touch and navigate ourselves in our environment to 
solve tasks that satisfy our needs. Away from experimentally imposed 
constraints in the laboratory, perception, in its natural state, can best 
be viewed as an action-based hypothesis-testing process (also called 
active sensing, active perception and active inference)5–8.

Recent studies have highlighted the important influence of 
impending actions across almost all cortical areas (Fig. 1). For exam-
ple, in mice solving a visual discrimination task using forepaws to 
rotate a wheel, Zatka-Haas et al.9 observed, using widefield calcium 
imaging, extensive bilateral activity across cortical areas preceding 
movements on choice trials (left or right action selected) but not on 
‘NoGo’ trials (no action is selected) (Fig. 1a, left). They further showed 
that impending movement could be decoded from cortical activity 
in most imaged regions by 25 ms before movement (Fig. 1a, right). In 
the same task, Steinmetz et al.10 used Neuropixels probes to record 
spiking activity from thousands of neurons and showed that, not

only does activity in the visual cortex get updated after movement 
(Fig. 1b, left), but almost all recorded cortical areas had neurons 
with activities that were predictive of upcoming movements (Fig. 1b, 
right). Similarly, Stringer et al.11 found that about a third of the popu-
lation activity of ~10,000 neurons in the visual cortex of awake mice 
could be predicted from motor actions derived from a video of the 
mouse’s facial movements (Fig. 1c), suggesting that sensory–motor 
integration occurs even in the primary sensory cortex (the lack of a 
similar result in monkeys12 could be due to the increased functional 
specialization of primate visual cortical areas compared to that of 
the rodent cortex).

Actions may be integrated differently across the different layers 
of a cortical area. For example, Jordan and Keller13 showed that both 
layer 2/3 and layer 5/6 neurons in the mouse primary visual cortex 
(V1) undergo depolarization before locomotion onset (Fig. 1d, left and 
middle). While layer 2/3 neurons appear to be computing a difference 
between motor-related input and bottom–up visual flow input, layer 
5/6 responses were consistent with positive integration of visuomotor 
inputs (Fig. 1d, right). These results complement well-known earlier 
results on predictive activity in a range of cortical areas such as the 
visual cortex14, the parietal cortex15 and frontal eye fields16 that antici-
pate the visual consequences of impending eye movements.

Received: 21 June 2023

Accepted: 26 April 2024

Published online: 27 June 2024

Check for updates

1Center for Neurotechnology, University of Washington, Seattle, WA, USA. 2Paul G. Allen School of Computer Science and Engineering, University of 
Washington, Seattle,  WA, USA. 
 e-mail: rao@cs.washington.edu


---

## Page 2

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1222

Perspective
https://doi.org/10.1038/s41593-024-01673-9

consisting of a state-prediction network and an action-prediction net-
work, both implemented within each cortical area. ‘State’ here denotes 
hidden (or ‘latent’) aspects of the world inferred from sensory inputs, 
for example, parts of an object to be recognized or one’s location in a 
building. ‘Action’ refers to not just motor commands but also abstract 
actions, for example, ‘go to the maternal grandmother node’ in a family 
tree or ‘perform multiplication’ on two given numbers. APC postulates 
that feedback from higher cortical areas modulates the dynamics of 
both state and action networks in lower areas, changing the functions 
they compute on the fly to suit the needs of the current task. This leads 
to representations that operate at multiple levels of sensory and motor 
abstraction, as observed in cortical hierarchies implicated in percep-
tion and action27–30. In the following sections, I present computational 
and neurobiological aspects of APC, comparing emerging studies and 
experimental results with the model’s predictions. I present simula-
tions chosen to showcase the explanatory breadth of APC. While we 
have previously investigated APC in the context of machine learning 
(ML) and artificial intelligence (AI)31–33, here I explore APC as a model 
of cortical function.

APC
Neuroanatomical and physiological motivation
The axonal outputs of layer 5 neurons in almost all cortical areas target 
subcortical motor centers19. Even in V1, outputs from layer 5 neurons 
target the superior colliculus34, which is involved in eye movements 
(aside from other motor behaviors). Similarly, layer 5 neurons in the 
primary auditory cortex (A1) send outputs to the inferior colliculus35, 
which is involved in orienting and defensive motor behaviors36, while

The emerging view, as suggested by the studies above, is that 
almost all cortical areas update their representations on the basis 
of ‘efference copies’ of upcoming actions (‘corollary discharges’ 
(ref. 17)) as well as the results of executed actions. Such a view harmo-
nizes well with the anatomical observation that all areas of the neocor-
tex (henceforth, the ‘cortex’), including areas traditionally labeled as 
sensory cortices, send outputs to subcortical motor regions (refs. 18,19 
and references therein) and receive input from these regions. Indeed, 
Vernon Mountcastle, in his prescient article in 1978 (ref. 20), put forth 
the hypothesis that a single unifying computational principle might 
be operating across the entire cortex, proposing the ‘cortical col-
umn’ as a modular information-processing unit of the cortex (see also 
refs. 21–23 for related ideas). This hypothesis is supported by the 
remarkable anatomical similarities in laminar connectivity patterns 
across cortical areas24,25, even though the density of cells within laminae 
may vary across areas. Additional evidence for this hypothesis comes 
from experiments in which inputs from the optic nerve were diverted 
via the auditory thalamus to the auditory cortex, causing the auditory 
cortex to develop visual receptive field properties26.

If there is indeed a common computational principle operating 
across the cortex, it must be versatile enough to explain capabilities 
as diverse as (1) learning to recognize an object from multiple visual 
glimpses through eye and head movements or from multiple tactile 
sensations through finger movements, (2) solving a complex spatial 
navigation task using simpler movement sequences and (3) under-
standing abstract concepts (such as a family tree).

In this Perspective, I suggest APC as a unifying sensory–motor 
theory of the cortex. APC hypothesizes a canonical cortical module as

Action decoder accuracy 
(25 ms before L/R action)

c

PC1

PC2

PC3
t

t + 1

Spontaneous mouse behavior
'eigenfaces'

d

a

Left/right

choice

0
100 ms

VISp
VISal
–0.3

dF/F (%)

Decoder acc. (%)

0.3

0.2

0

–0.2

1,000 neurons

10 s

1,000 neurons

10 s

2 s

L2/3
L5/6

L2/3
L5/6

**
4
2
0
–2
–4
–6

Mismatch response

(mV)

4 mV

Neural activity prediction (test set) from face motion

Neural activity (test set) sorted by 1D embedding

80

5
2
0

50
20

125
150 MOs
MOp

SSp

200
Stim onset

NoGo

b

Contra

VISpm neuron
Action encoding

Neurons (%)

> Figure description (generated): This figure presents a series of brain activation maps illustrating neural activity across different time points following stimulus onset, separated by behavioral context.

**Overall Layout & Structure:**
The figure is structured as a $2 \times 5$ grid of coronal brain slices, organized into two main rows corresponding to different behavioral conditions: "Stim onset" (top row) and "NoGo" (bottom row). Each row contains five distinct columns, representing specific time points relative to stimulus onset.

**Visual Components & Symbols:**
*   **Brain Slices:** Each panel displays a coronal cross-section of the brain, depicted as an anatomical outline.
*   **Activation Maps:** Superimposed on these outlines are heatmaps indicating neural activity (dF/F). The activation is visualized using a color gradient.
*   **Time Points (Columns):** The columns are labeled with specific time points: "0", "100 ms", "125", "150", and "200".
*   **Behavioral Context (Rows):** The top row is labeled "Stim onset" and the bottom row is labeled "NoGo".
*   **Annotations:** Specific brain regions are pointed out with labels in the later time points (150 ms and 200 ms).

**Labels, Keys & Legends:**
*   **Time Labels (Top Row):** "Stim onset" is positioned above the top row.
*   **Time Labels (Bottom Row):** "NoGo" is positioned above the bottom row.
*   **Color Bar/Legend:** A color bar located to the right of the grid indicates the scale for $\text{dF/F (\%)}$:
    *   The range spans from $-0.3$ (dark blue) to $0.3$ (dark red).
    *   The color scale transitions through white/light colors in between.
*   **Region Labels (Annotations):** Several specific brain regions are labeled near the right side of the slices, primarily in the later time points:
    *   **MOs:** Labeled near 150 ms and 200 ms.
    *   **SSp:** Labeled near 200 ms.
    *   **VISp:** Labeled below the bottom row at 100 ms.
    *   **VISal:** Labeled below the top row at 125 ms.

**Data Trends & Details (Activation Patterns):**
*   **Time 0:** At time point 0, the activation maps in both conditions show minimal or diffuse activity across the visualized slices.
*   **Time 100 ms:** In both conditions, some localized activation begins to appear. The "NoGo" condition shows a distinct area labeled VISp starting to show activity.
*   **Time 125 ms:** The "Stim onset" condition shows activation localized in a region labeled VISal.
*   **Time 150 ms & 200 ms:** These later time points show the most pronounced and widespread activation, particularly in the "Stim onset" condition. In both conditions at 200 ms, activity is visible in the regions labeled MOs and SSp. The intensity of red (positive activation) appears generally stronger in the "Stim onset" condition compared to the "NoGo" condition at comparable time points, although both show significant activity.

In summary, the figure compares neural responses (measured as $\text{dF/F}$) in two behavioral contexts ("Stim onset" vs. "NoGo") across a temporal sequence (0 to 200 ms), highlighting the dynamic recruitment of specific cortical areas like MOs, SSp, VISp, and VISal.

> Figure description (generated): This figure presents a visualization titled "VISpm neuron," structured as two distinct, horizontally aligned panels. The overall style is a scatter plot or density map representation, likely illustrating the activity or feature space of a specific neuron type.

**1. Overall Layout & Structure:**
The figure is divided into two main horizontal sections, stacked vertically. Each section appears to represent a different feature or state associated with the "VISpm neuron." The structure is minimalist, relying on scattered points within defined horizontal bands.

**2. Visual Components & Symbols:**
*   **Panels:** There are two primary panels, stacked one above the other.
    *   The upper panel is associated with a label starting with "ntra" (likely representing an input or feature).
    *   The lower panel is associated with a label starting with "lpsi" (likely representing another input or feature).
*   **Data Points:** Within each panel, there are clusters of small, scattered points. These points are color-coded:
    *   **Orange/Reddish Points:** Present primarily in the upper panel.
    *   **Black Points:** Present prominently in both panels, often overlapping or adjacent to the orange points.
    *   **Blue Points:** Present primarily in the lower panel.
*   **Vertical Dashed Line:** A prominent vertical dashed line is positioned near the center of the visualization, acting as a potential boundary or reference point separating different regimes within the feature space.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "VISpm neuron" at the top center.
*   **Panel Labels (Y-axis proxies):**
    *   The upper panel is labeled with text beginning "ntra" (the full word is truncated).
    *   The lower panel is labeled with text beginning "lpsi" (the full word is truncated).
*   **Axes:** No explicit numerical axis labels are visible, suggesting the visualization represents a qualitative feature space rather than quantitative measurements on standard axes.

**4. Data Trends & Details:**
*   **Upper Panel ("ntra"):** This panel shows a concentration of activity points. The orange and black points form a dense cluster that appears to shift or spread slightly towards the right side of the visualization, particularly in the region immediately following the vertical dashed line.
*   **Lower Panel ("lpsi"):** This panel shows a distinct pattern dominated by blue and black points. The activity appears more spread out horizontally compared to the upper panel, with a noticeable concentration of black and blue points clustered towards the right side, again near or past the vertical dashed line.

**5. Contextual Caption Integration:**
The labels "ntra" and "lpsi" likely refer to specific features or dimensions being plotted against an implicit feature space (represented by the horizontal spread). The visualization contrasts the distribution of activity patterns associated with these two features for the VISpm neuron, highlighting differences in how orange/black vs. blue/black points are distributed relative to the central dashed line.

> Figure description (generated): This figure, titled "Action encoding," presents a comparative schematic illustrating neural activity patterns across two different views or states.

**1. Overall Layout & Structure:**
The figure is divided into two distinct, side-by-side schematic representations of a neural structure. There are no explicit panel labels (like A or B), but the two diagrams function as comparative views. The overall style is a simplified, anatomical/circuit diagram using shaded areas to represent neural populations or activity levels.

**2. Visual Components & Symbols:**
*   **Neural Structure Representation:** Both diagrams depict a complex, somewhat lobed or segmented structure, likely representing a brain region. The structures are outlined in black lines and filled with varying shades of green/gray.
*   **Color Coding (Activity Level):** A color bar legend is positioned above the diagrams, indicating a scale for "Neurons (%)".
    *   The color transitions from white/light gray (representing 0% activity) through various shades of green to a dark, saturated green (representing 5% or higher activity).
*   **Left Diagram:** This view appears to be a dorsal or superior cross-section. It shows a more organized, segmented structure with distinct boundaries between regions. The shading indicates varying levels of neural activity across these segments.
*   **Right Diagram:** This view appears to be a lateral or sagittal cross-section, showing a more complex, three-dimensional arrangement of the neural tissue. The shading here is highly variegated, showing clusters and patches of high activity (dark green) interspersed with lower activity areas.
*   **Outlines:** Thin, light gray lines are visible surrounding the main neural mass in both diagrams, suggesting boundaries or surrounding tissue.

**3. Labels, Keys & Legends:**
*   **Title:** The main title above the diagrams is "Action encoding".
*   **Legend/Scale Bar:** A horizontal bar graph labeled "Neurons (%)" is present above the diagrams. This scale ranges from 0 to 5, with corresponding color gradients shown beneath the numerical labels (0, 2, 5).

**4. Data Trends & Details:**
The diagrams do not contain quantitative plots (like axes with numerical scales for time or frequency). Instead, the data is represented spatially through color intensity:
*   In both diagrams, areas shaded in dark green indicate a higher percentage of active neurons (approaching 5% according to the legend).
*   Areas shaded in light green or gray indicate lower percentages of active neurons (closer to 0%).

**5. Contextual Caption Integration:**
The figure is explicitly titled "Action encoding," suggesting that the spatial distribution of neural activity shown in these two views represents how motor or behavioral actions are represented within this specific neural structure. The color scale quantifies the density of active neurons ($\%$).

Ipsi

Locomotion onset
Locomotion onset

14
–2
0
2
4
6
–20

–10

0

10

20

Time (s)

Vm response (mV)

10

Sorted neuron #

6

2

Fig. 1 | Widespread influence of actions across the cortex. a, Left, widefield 
calcium imaging reveals bilateral activity (cortical fluorescence dF/F) from 0 to 
200 ms after stimulus (stim) onset across cortical areas preceding movements 
on left or right (L/R) action-selection trials. ‘NoGo’ trials do not show such 
activity. Right, average action execution decoder accuracy (acc.) 25 ms before 
movement onset, showing that an impending movement can be decoded from 
cortical activity in most imaged regions (adapted from ref. 9, CC BY 4.0). MOs, 
secondary motor cortical area; MOp, primary motor cortex; SSp, primary 
somatosensory cortex; VISp, primary visual cortex; VISal, secondary visual 
cortical area. b, Left, increased spiking after a correct choice movement in a 
visual cortex neuron (posteromedial visual area, VISpm) for both contralateral 
(contra) and ipsilateral (ipsi) stimulus presentations (orange and blue dots, 
spikes; black dots, movement onset). Right, fraction of neurons in each brain 
region with pre-movement activity that could be accurately predicted from 
the animal’s movement (in either the left or right direction) (adapted from 
ref. 10, Springer Nature Limited). c, Motor action information extracted using

> Figure caption (from PDF text): Fig. 1 | Widespread influence of actions across the cortex. a, Left, widefield 
calcium imaging reveals bilateral activity (cortical fluorescence dF/F) from 0 to 
200 ms after stimulus (stim) onset across cortical areas preceding movements 
on left or right (L/R) action-selection trials. ‘NoGo’ trials do not show such 
activity. Right, average action execution decoder accuracy (acc.) 25 ms before 
movement onset, showing that an impending movement can be decoded from 
cortical activity in most imaged regions (adapted from ref. 9, CC BY 4.0). MOs, 
secondary motor cortical area; MOp, primary motor cortex; SSp, primary 
somatosensory cortex; VISp, primary visual cortex; VISal, secondary visual 
cortical area. b, Left, increased spiking after a correct choice movement in a 
visual cortex neuron (posteromedial visual area, VISpm) for both contralateral 
(contra) and ipsilateral (ipsi) stimulus presentations (orange and blue dots, 
spikes; black dots, movement onset). Right, fraction of neurons in each brain 
region with pre-movement activity that could be accurately predicted from 
the animal’s movement (in either the left or right direction) (adapted from 
ref. 10, Springer Nature Limited). c, Motor action information extracted using
> Figure description (generated): This figure presents two panels, labeled implicitly by their content structure, displaying neural activity data visualized as raster plots.

**Overall Layout & Structure:**
The figure is composed of two distinct, stacked panels, each presenting a raster plot. The top panel shows "Neural activity (test set) sorted by 1D embedding," and the bottom panel shows "Neural activity prediction (test set) from face motion." Both panels share a similar structure: a time-series visualization across many neurons.

**Visual Components & Symbols:**
Both panels utilize raster plots where the vertical axis represents individual neurons and the horizontal axis represents time.

*   **Y-axis (Neurons):** Labeled "1,000 neurons" in both panels, indicating that the data spans activity across a large population of 1,000 recorded neurons.
*   **X-axis (Time):** Labeled "10 s" in both panels, indicating a 10-second time window.
*   **Activity Representation:** The neural activity is represented by dense, black marks (spikes or fluorescence events) scattered across the grid defined by neurons and time.

**Panel 1: Neural activity (test set) sorted by 1D embedding**
*   This panel displays the raw or processed neural activity. The black marks show when individual neurons fired during the test set trials, sorted according to a 1D embedding. The activity appears highly complex and distributed across the population over time.

**Panel 2: Neural activity prediction (test set) from face motion**
*   This panel displays the predicted neural activity. The black marks here represent the model's prediction of neuronal firing based on face motion input. Visually, this panel appears to show a pattern that is structured or more predictable compared to the raw activity in Panel 1, although it still contains significant stochasticity.

**Labels, Keys & Legends:**
*   The primary labels are the titles above each plot: "Neural activity (test set) sorted by 1D embedding" and "Neural activity prediction (test set) from face motion."
*   The axes are labeled as described above: "1,000 neurons" (Y-axis) and "10 s" (X-axis).

**Contextual Caption Integration:**
The provided caption text refers to related figures (Fig. 1, parts a, b, c) and mentions specific cortical areas: MOs (secondary motor cortical area), MOp (primary motor cortex), SSp (primary somatosensory cortex), VISp (primary visual cortex), and VISal (secondary visual cortical area). While these specific anatomical labels are not present *within* the two raster plots shown, the caption contextually frames these visualizations as relating to cortical activity preceding movements.

**Data Trends & Details:**
*   In both plots, the data is dense, indicating high levels of neural firing across the population over the 10-second window.
*   The sorting in Panel 1 suggests that neurons exhibiting similar temporal firing patterns (as captured by the 1D embedding) are grouped together vertically.
*   Panel 2 shows how well the model can reproduce the temporal firing patterns observed in Panel 1, serving as a comparison between actual activity and model prediction.

> Figure caption (from PDF text): Fig. 1 | Widespread influence of actions across the cortex. a, Left, widefield 
calcium imaging reveals bilateral activity (cortical fluorescence dF/F) from 0 to 
200 ms after stimulus (stim) onset across cortical areas preceding movements 
on left or right (L/R) action-selection trials. ‘NoGo’ trials do not show such 
activity. Right, average action execution decoder accuracy (acc.) 25 ms before 
movement onset, showing that an impending movement can be decoded from 
cortical activity in most imaged regions (adapted from ref. 9, CC BY 4.0). MOs, 
secondary motor cortical area; MOp, primary motor cortex; SSp, primary 
somatosensory cortex; VISp, primary visual cortex; VISal, secondary visual 
cortical area. b, Left, increased spiking after a correct choice movement in a 
visual cortex neuron (posteromedial visual area, VISpm) for both contralateral 
(contra) and ipsilateral (ipsi) stimulus presentations (orange and blue dots, 
spikes; black dots, movement onset). Right, fraction of neurons in each brain 
region with pre-movement activity that could be accurately predicted from 
the animal’s movement (in either the left or right direction) (adapted from 
ref. 10, Springer Nature Limited). c, Motor action information extracted using
> Figure description (generated): This figure presents a heatmap visualization titled "Locomotion onset," which appears to be part of a larger multi-panel figure (implied by the caption referencing 'a', 'b', and 'c').

**1. Overall Layout & Structure:**
The visualization is a single, large heatmap plot. It displays activity across different cortical areas (represented on the y-axis) over time relative to a specific event, "Locomotion onset" (indicated by a vertical dashed line).

**2. Visual Components & Symbols:**
*   **Heatmap Grid:** The core of the figure is a grid where color intensity represents activity level.
*   **Y-axis (Cortical Areas):** The y-axis lists specific cortical regions, labeled numerically from 2 to 14. These labels likely correspond to different brain areas mentioned in the caption (MOs, MOp, SSp, VISp, VISal).
*   **X-axis (Time):** The x-axis represents time, labeled in seconds ($\text{s}$), ranging from approximately $-2$ to $7$.
*   **Color Bar/Legend:** A vertical color bar is positioned on the right side of the plot, indicating the scale for the activity represented by the heatmap colors.
*   **Event Marker:** A vertical dashed line is placed at $t=0$, explicitly marked with a downward-pointing black triangle and the text "Locomotion onset," indicating the reference point for the time axis.

**3. Labels, Keys & Legends:**
*   **Title:** "Locomotion onset"
*   **X-axis Label:** $\text{Time (s)}$
*   **Y-axis Labels:** Numerical labels: 2, 6, 10, 14.
*   **Color Bar Scale:** The color bar ranges from $-20$ to $20$.
    *   The scale indicates that colors shift from deep blue (negative values, e.g., $-20$) through white/light colors (near 0) to deep red/magenta (positive values, e.g., $20$).

**4. Data Trends & Details:**
*   **Activity Pattern:** The heatmap shows widespread, fluctuating activity across the displayed cortical areas (y-axis) leading up to and immediately following locomotion onset ($t=0$).
*   **Pre-Onset Activity:** There is noticeable activity (indicated by warmer colors, red/magenta) present in many rows across the time window preceding $t=0$ (e.g., between $-2\text{s}$ and $0\text{s}$).
*   **Post-Onset Activity:** Activity continues after $t=0$, with sustained patterns visible across the time range up to $7\text{s}$.
*   **Specific Regions:** The rows corresponding to areas 6, 10, and 14 show distinct patterns of activity that appear more intense or sustained compared to the regions at 2.

**5. Contextual Caption Integration:**
The caption identifies several abbreviations relevant to the cortical areas: MOs (secondary motor cortical area), MOp (primary motor cortex), SSp (primary somatosensory cortex), VISp (primary visual cortex), and VISal (secondary visual cortical area). The heatmap likely represents the "cortical fluorescence dF/F" mentioned in the caption, showing bilateral activity preceding movements.

principal-component (PC) analysis of a video of a mouse’s facial movements 
(left, example frames t, t + 1; middle, top three principal components) accurately 
predicted (using reduced-rank regression) about a third of the population 
activity of ~10,000 neurons (raster representations on the right) measured 
using two-photon calcium imaging of the visual cortex of awake mice (adapted 
with permission from ref. 11, AAAS). 1D, one dimensional. d, Intracellular 
recordings in V1 of mice on a spherical treadmill with locomotion coupled 
to visual flow feedback. Visual flow was halted at random times to generate 
visuomotor mismatch events. Left, heatmap of average responses before 
and after locomotion onset across all layer 5/6 neurons. Baseline activity was 
subtracted from responses by using the average membrane potential in the 2.5 s 
before locomotion onset before averaging. Middle, average response before and 
after locomotion onset across all layer 5/6 (L5/6) neurons (black, 14 neurons) 
compared with all layer 2/3 (L2/3) neurons (gray, 32 neurons). Right, average 
mismatch responses of layer 2/3 and layer 5/6 neurons (adapted with permission 
from ref. 13, Elsevier).


---

## Page 3

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1223

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): ## Figure Description: Canonical APC Module

This figure, labeled as **BOX 1**, illustrates the structure of a "Canonical APC module" across three distinct panels: (a), (b), and (c). The overall style is a schematic diagram representing neural circuit architecture.

---

### Panel (a): Lower-order Thalamus Schematic
Panel (a) depicts a schematic representing the lower-order thalamus.

*   **Structure:** It is a layered diagram showing interconnected nodes/layers.
*   **Nodes/Layers:** There are four distinct horizontal layers indicated by labeled boxes: "Lower-order thalamus," "Motor centers," "Higher-order thalamus," and a final layer labeled "Input."
*   **Connections:** Arrows indicate flow between these layers. Specifically:
    *   An input arrow points into the "Lower-order thalamus."
    *   Connections flow from the "Lower-order thalamus" to the "Motor centers."
    *   Connections flow from the "Lower-order thalamus" to the "Higher-order thalamus."
    *   Connections flow from the "Motor centers" to the "Higher-order thalamus."
    *   The "Input" layer appears to feed into the system, though its specific connection point is not explicitly detailed as a single input node.

### Panel (b): Action/Goal Coordinates Schematic
Panel (b) illustrates a schematic related to action/goal coordinates, structured similarly to Panel (a).

*   **Structure:** It shows a layered arrangement with four main labeled sections: "Lower-order thalamus," "Motor centers," "Higher-order thalamus," and "Input."
*   **Nodes/Layers:** The layers are labeled identically to Panel (a).
*   **Connections:** Arrows indicate information flow:
    *   An input arrow points into the "Lower-order thalamus."
    *   Connections flow from the "Lower-order thalamus" to the "Motor centers."
    *   Connections flow from the "Lower-order thalamus" to the "Higher-order thalamus."
    *   Connections flow from the "Motor centers" to the "Higher-order thalamus."
    *   The "Input" layer feeds into the system.

### Panel (c): Full APC Module Schematic
Panel (c) presents a more complex, integrated schematic representing the full Canonical APC module. This panel incorporates feedback loops and specific functional blocks.

*   **Structure:** It is a multi-component diagram showing information flow between different functional units.
*   **Components & Flow:**
    1.  **State Feedback Loop (Top Left):** A block labeled "State feedback" is shown, with an arrow pointing towards the main processing stream.
    2.  **Core Processing Stream (Center):** The central flow involves nodes representing different stages:
        *   An initial node receives input.
        *   This flows into a block labeled $\vec{a}_t$ (likely representing action/state).
        *   This flows into a block labeled $\vec{f}_t$ (likely representing function/goal).
        *   The output of $\vec{f}_t$ flows into a block labeled $d_t$.
    3.  **Thalamic/Motor Integration (Bottom):** The lower part of the diagram shows a structure analogous to Panels (a) and (b), featuring:
        *   "Lower-order thalamus"
        *   "Motor centers"
        *   "Higher-order thalamus"
    4.  **Feedback Loops:**
        *   A loop connects the output of $\vec{a}_t$ back towards the "Lower-order thalamus."
        *   A loop connects the output of $\vec{f}_t$ back towards the "Higher-order thalamus."
        *   The entire structure is framed by connections suggesting a closed-loop system.

### Annotations and Labels (Across Panels)
*   **Numerical Markers:** In Panel (a), there are numerical markers $1, 2/3, 4, 5, 6$ positioned near the layers. In Panel (b), similar markers $1, 2/3, 4, 5, 6$ are present. In Panel (c), the same numerical markers $1, 2/3, 4, 5, 6$ are present near the corresponding layers in the lower schematic.
*   **Variables:** The variables $\vec{a}_t$ and $\vec{f}_t$ are prominently displayed in Panel (c).
*   **Caption Context:** The caption clarifies that the diagram represents a "six-layered laminar structure of a cortical column," and that Panel (c) shows the "possible implementation of inference in a canonical APC module."

layer 5 neurons in the primary somatosensory cortex send outputs 
to the spinal cord37, which controls body movements. On the other 
hand, layer 5 neurons in the primary motor cortex (or M1) (such as Betz 
cells) have long been implicated in motor function via their axonal 
projections to the spinal cord38, but the middle and upper layers of 
traditional ‘motor’ cortical areas such as M1 are involved in sensory 
processing of feedback from subcortical and cortical sources39,40: for 
example, layer 2/3 neurons in mouse M1 respond to unexpected sen-
sory perturbations in a visually guided motor task41, while neurons in 
mouse M2 encode auditory sensation and expectation42. Thus, despite

well-known differences in the laminar densities of neurons in different 
cortical areas (for example, V1 versus M1), the sensory–motor nature 
of the cortex is retained. This motivates the idea of a ‘sensory–motor 
cortical module’ as a canonical feature of the cortex (described further 
in the section APC module and neuroanatomical implementation).

The figure in Box 1 (panel a) depicts the laminar structure of a typi-
cal cortical column and its connectivity (based on refs. 18,24,43). Inputs 
from a sensory region or a lower cortical area target layer 4 neurons, 
the outputs of which are then conveyed to the superficial layer 2/3 
neurons. These neurons in turn send their axons to the deeper layers,

Box 1

Canonical APC module

The canonical APC module is motivated by the laminar structure 
of the cortex (figure in Box 1, panel a) and consists of the following 
components:

State-transition function. The state-transition function fs models 
the physics of the environment and the agent, and predicts the 
next state st, given the previous state st−1 and action at−1 (figure in 
Box 1, panel b). In general, states and actions are vectors. By 
learning an approximation ̂ fs of fs from interactions with the 
world, the agent can learn an ‘internal model’ of the world81,87,88,94 
(also called a ‘world model’, forward model or generative model) 
and use it to run simulations of the world, imagine new scenarios, 
explore what happens when particular actions are executed and 
plan actions that lead to desirable states. Biologically, the function ̂

fs can be implemented by a recurrently connected network of 
neurons, with the network activity at time t denoting an estimate ̂st 
of the state st (figure in Box 1, panel c). Neural population activity 
in visual, auditory and somatosensory cortices, for instance, after 
processing a sensory stimulus (or more generally, after sequential 
sampling of the stimulus), can be regarded as the estimated ̂st for 
that stimulus computed by the cortical region.

Policy function. An internal model (such as ̂ fs above) can be used to 
plan actions by unrolling the model into the future to explore the

consequences of various action choices, but this mode of selecting 
actions requires considerable effort and deliberation (‘system 2’ 
thinking68). A more efficient way to select actions (‘system 1’ 
thinking68) is to have a state-to-action ‘policy’ (ref. 44) ̂ fa, which maps 
the current estimated state ̂st directly to an action ̂at to achieve the 
current goal (figure in Box 1, panel c). Biologically, the policy ̂ fa can 
be implemented by a recurrent network of neurons with activity at 
time t denoting ̂at.

Coupling perception and action. Given a policy ̂ fa for a particular 
task or goal, the agent can execute an action ̂at  
from the policy while simultaneously sending ̂at as an ‘efference 
copy’ (or ‘corollary discharge’ (ref. 17)) to the learned model ̂ fs to 
predict the sensory consequences of each action. The agent  
can then correct its prediction of the new state of the world  
based on the new sensory observation that resulted from  
taking the action, using prediction errors as prescribed by 
predictive coding theory1. The corrected state estimate ̂st can in 
turn be fed as input to the policy ̂ fa to generate the next  
action for the task, continuing until the goal is achieved or  
the task times out. A biological implementation of this idea  
involves coupling the state and policy recurrent networks within 
the laminar structure of a cortical area, as depicted in the figure in 
Box 1 (panel c).

b

Action/goal/coordinates
Input

a
1

2/3
at–1

at

st–1
st

st
at–1

fs

fa

4

5

6
D

Lower-order 
thalamus

Higher-order 
thalamus
Motor 
centers

ât–1

ât

ŝt–1

ât–1
ŝt

fs

fa

D

c

Lower-order thalamus
Higher-order thalamus

1

2/3

4

5

6

State

feedback

Action
feed-
back

Motor centers

Canonical APC module. a, Depiction of the six-layered laminar structure of a cortical column, showing some of the major connections 
between layers and with the thalamus (not all connections are shown) (based on refs. 18,24,43). b, Canonical APC generative model. The 
dashed arrow denotes a delay of one time step. D denotes a decoder converting state to input. c, One possible implementation of inference in 
a canonical APC module for the generative model in b.


---

## Page 4

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1224

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): This figure, labeled **BOX 2**, is a multi-panel illustration detailing aspects of state and action networks in the cortex, combining schematic diagrams, time-course plots, and functional representations.

### Overall Layout & Structure
The figure is divided into several distinct panels: **(a)**, **(b)**, **(c)**, and **(d)**. Panels (a) and (b) appear to be related time-course plots or representations of neural activity, while panels (c) and (d) are schematic diagrams illustrating network dynamics.

### Panel-by-Panel Description

#### Panel (a): Time Course Plot
*   **Type:** A line graph showing activity over time.
*   **Y-axis Label:** "Auditory cortex" (implied activity level).
*   **X-axis Label:** "Time (s)". The axis ranges from 0 to approximately 120 ms.
*   **Content:** Two distinct traces are shown:
    *   A trace labeled "Omission" shows a rapid, transient increase in activity starting near $t=0$ s.
    *   A trace labeled "Movement Passive" shows a similar, but perhaps slightly different, transient activity pattern.
*   **Annotations:** The plot includes a vertical line indicating the onset of an event, and labels "Omission" and "Movement Passive" are positioned above their respective traces.

#### Panel (b): Time Course Plot
*   **Type:** A line graph showing activity over time, likely related to the auditory cortex.
*   **Y-axis Label:** "Frequency" (implied activity level).
*   **X-axis Label:** "Time (s)". The axis ranges from 0 to approximately 120 ms.
*   **Content:** Two traces are shown:
    *   A trace labeled "Omission" shows a pattern of activity.
    *   A trace labeled "Movement Passive" shows another pattern of activity, which appears slightly different from the Omission trace.
*   **Annotations:** The plot includes a vertical line indicating an event onset, and labels "Omission" and "Movement Passive" are positioned above the traces.

#### Panel (c): Schematic Diagram - Cortical Networks
*   **Type:** A schematic diagram illustrating cortical connectivity and processing stages.
*   **Structure:** It features three main columns, each representing a different context or state: "Monkey B," "Monkey J-array," and "Monkey N-array."
*   **Components:** Within each column, there are representations of neural processing stages:
    *   A box labeled "Projection onto PC" (Projecting to Primary Cortex).
    *   A box labeled "Projection into PC" (Projecting into Primary Cortex).
    *   An arrow flows from the "Projection onto PC" box to a central element, and another arrow flows into the "Projection into PC" box.
*   **Labels:** The diagram uses arrows to denote flow between these projection stages across the three monkey contexts.

#### Panel (d): Schematic Diagram - Network Dynamics
*   **Type:** A schematic diagram illustrating the dynamics of neural populations, likely related to prediction or error signaling.
*   **Structure:** This panel is divided into two main sections, separated by a vertical line.
*   **Left Side (Prediction):**
    *   A box labeled "Neural population trajectory, thalamus" is shown.
    *   An arrow points from this box to a central element labeled "Lift."
    *   A time-course plot below shows activity over time, with labels indicating "Lift +350 ms" and "Lift -100 ms."
*   **Right Side (Error/Correction):**
    *   A box labeled "Neural population trajectory, cortex" is shown.
    *   An arrow points from this box to a central element labeled "Lift."
    *   A time-course plot below shows activity over time, with labels indicating "Lift +350 ms" and "Lift -100 ms."
*   **Bottom Row:** Below the main schematic, there are three small plots labeled PC1, PC2, and PC3. These appear to be time-course representations of different principal components or neural features across the network dynamics shown above.

### Contextual Caption Integration Notes
The caption indicates that these panels relate to "State and action networks in the cortex." Specifically:
*   The description mentions that Panel (a) and (b) relate to the time course of activity for "Omission" versus "Movement Passive."
*   Panel (c) illustrates the projection dynamics across different monkey arrays.
*   Panel (d) depicts the "Lift" event and associated neural trajectories, linking to concepts of prediction and error correction.

Box 2

State and action networks in the cortex

State network ̂ f̂f̂fs and sensory–motor prediction in the cortex. The 
APC model predicts that cortical networks implementing the 
state-prediction function ̂ fs should learn to anticipate the sensory 
consequences of actions (by predicting latent sensory states) and 
exhibit anticipatory activity before movement. A study by Audette 
et al.93 found such anticipatory activity in the primary auditory 
cortex (figure in Box 2, panel a): mice were trained to push a lever 
with their forelimb, which produced a pure tone at a fixed position 
early in each movement; after training, omission of this learned 
movement-associated sound (figure in Box 2, panel a, top left) 
revealed a large population of auditory cortex neurons firing roughly 
200 ms before movement onset, with this activity peaking around 
the time of the expected tone (figure in Box 2, panel a, top middle 
and right). The study also found prediction error-like suppression of 
neural activity for anticipated sounds, consistent with the use of 
errors in predictive coding for state inference (figure in Box 2, panel 
a, bottom). Predictive activity anticipating the visual consequences

of an upcoming eye movement has been observed across the cortex 
including the visual cortex14, the parietal cortex15 and the frontal 
cortex16 (figure in Box 2, panel b, left, middle and right, respectively). 
Other types of movement, such as locomotion, can also predictively 
activate cortical neurons, for example, in V1 (ref. 13 and Fig. 1d). 
These results are consistent with the APC model’s use of a state 
network ̂ fs to learn the sensory consequences of actions.

Action network ̂ f̂f̂fa and cortical motor dynamics. The APC model 
assumes that the network within a cortical area implementing the 
action-prediction function ̂ fa is a recurrent network (figure in  
Box 1, panel c) for which the outputs, in the case of the motor cortex, 
encode the dynamics of movement. There is now considerable 
neurophysiological evidence that, when an animal is performing a 
movement (for example, reaching toward a goal), the activities of 
neurons in the motor cortex are well described by a dynamical 
system of the form ̇a = f(a, u) where u is an external input95.

b

c

a

d

Omission

10

Movement

0

Passive

n = 377
Visual cortex 
(V3A)

Eye movement

onset

Frontal cortex
(FEF)

Eye movement

onset

200 ms

FP1

FP2
Stim

Parietal
cortex

V eye
H eye

Stim

H
V

FP2

FP2
FP1

Stim

FP1

Eye movement

onset
Stimulus

onset

Auditory 
cortex

Frequency

(Hz)

Time (s)

Motor
cortex
Monkey B

Projection

onto jPC2 (AU)

Projection
onto jPC1 (AU)

Projection
onto jPC1 (AU)

Projection
onto jPC1 (AU)

Lift –100 ms

Lift –100 ms

Lift +350 ms
Lift

Lift
Lift +350 ms

Neural population
trajectory, thalamus

Neural population

trajectory, cortex

PC1
PC2
PC3

PC1
PC2
PC3

Lift

Population

trajectory, cortex
Population

trajectory, thalamus

Single-trial population trajectories,

cortex and thalamus

PC1

PC1

PC2

PC2

PC3

PC3

Monkey J-array
Monkey N-array

6

5 Hz

100 ms

100 ms
50 ms

100

2
–0.4
0
0.4

0.4 0

30

0
0.4

State and action networks in the cortex. a, Top left, schematic of the omission of an expected sound during a lever-press movement (black 
curve) in a self-generated sound task in mice93. a, Top middle and right, neural activity in the auditory cortex aligned to six positions (colored 
dots) along the lever-press movement: peak firing always corresponded to the time of the expected sound (occurring on average 36 ms 
after movement onset), with the activity starting roughly 200 ms before movement onset (as reported in ref. 93). a, Bottom, heatmaps (left) 
of responses for all recorded neurons and the average response (right) for 377 of those neurons responding above a threshold to the sound 
when it was self-generated by a lever press (‘movement’) and when it was not self-generated (‘passive’). Note the greater suppression (green) 
for self-generated sounds (adapted from ref. 93, Elsevier). b, Predictive activity anticipating the visual consequences of an upcoming eye 
movement in the visual cortex (left) (adapted with permission from ref. 14, National Academy of Sciences, USA), the parietal cortex (middle) 
(adapted with permission from ref. 15, AAAS) and the frontal cortex (right) (adapted with permission from ref. 16, American Physiological 
Society). FP, fixation point; H, horizontal eye movement; V, vertical eye movement; FEF, frontal eye fields. c, Two-dimensional projection (using 
jPCA95) of population activity of motor cortex neurons in three monkeys performing straight and curved reaching movements, showing rotation 
of the neural state. Traces are colored from green to red based on the preparatory neural state (circles) for each reach condition (adapted 
from ref. 95, Springer Nature Limited). jPC1 and jPC2, first and second dimensions, respectively, of jPCA space; AU, arbitrary units. d, Results 
from simultaneous population recordings of the motor thalamus and the motor cortex in mice performing reach-to-grasp movements97. Left, 
neural population trajectories for the thalamus (left, green) and the cortex (right, magenta) obtained using trial-averaged PCA. Right, single-trial 
population activity in the thalamus (top) and the cortex (bottom) (adapted from ref. 97, Springer Nature Limited).


---

## Page 5

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1225

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): Since no actual image of "Figure 2" was provided, I must generate a template response based on the context given in the caption. This description assumes Figure 2 is a schematic illustrating the interaction between cortical motor dynamics, thalamic inputs, and action network outputs, as described in the text.

***

**[NOTE: As no image was provided, this description is a detailed structural template based on the textual context. Please provide the actual figure for an accurate analysis.]**

### Exhaustive Figure Description (Hypothetical based on Caption Context)

This figure, designated as **Figure 2**, appears to be a complex schematic diagram illustrating the functional architecture of sensorimotor control, specifically detailing the interaction between cortical motor dynamics and thalamic inputs within a recurrent neural network framework. The structure is likely divided into multiple panels (Panel A, Panel B, and Panel C) to delineate different aspects of the system.

#### 1. Overall Layout & Structure
The figure is structured as a multi-panel schematic, likely employing block diagrams and directional arrows to represent information flow. The layout suggests a feedforward/feedback loop structure, characteristic of neural circuit diagrams.

#### 2. Visual Components & Symbols
*   **Nodes/Boxes:** Rectangular or irregularly shaped boxes likely represent major functional modules (e.g., "Cortical Motor Network," "Thalamus," "Action Network").
*   **Connections/Arrows:** Directed arrows indicate the flow of information or influence. These arrows are crucial for depicting causality and feedback loops (e.g., from the cortex back to the thalamus, or within the cortical network).
*   **Internal Elements:** Within the main modules, smaller nodes might represent specific neural populations or sub-regions.
*   **Color Coding (If present):** Different colors would likely be used to distinguish between cortical areas, thalamic nuclei, or different types of neural activity (e.g., sensory vs. motor).

#### 3. Labels, Keys & Legends
The figure is expected to contain several key labels corresponding to the concepts mentioned in the caption:
*   **$\mathbf{f}_a$:** This variable, representing the action network output, is likely labeled prominently.
*   **Cortical Motor Dynamics:** A major module representing the primary motor control area.
*   **Thalamic Inputs:** A distinct module showing inputs originating from the thalamus, which feeds into the cortical system.
*   **Action Network:** A specific component within the network structure, receiving inputs and generating outputs.
*   **Feedback Loops:** Arrows explicitly showing recurrent connections (e.g., from the cortex back to itself or upstream structures).

#### 4. Data Trends & Details (If Plots are Present)
If any panel contains plots, they would likely illustrate time-varying dynamics:
*   **Axes:** The X-axis would typically represent **Time**. The Y-axis would likely represent a measure of neural activity (e.g., firing rate, population vector magnitude) or kinematic variables (e.g., joint angle).
*   **Curves:** Different lines would represent the activity of different components (e.g., one line for thalamic drive, another for cortical output $\mathbf{f}_a$).

#### 5. Contextual Caption Integration
The caption directs attention to specific elements:
*   **Panel (c):** This panel specifically illustrates the **sensorimotor loop in cortical pattern generation**. It should visually depict how sensory feedback modulates motor output.
*   **Panel (b):** This panel likely details the **thalamic inputs** and their role in driving cortical pattern generation.
*   **Panel (a):** This panel likely shows the core **action network dynamics**, perhaps illustrating how $\mathbf{f}_a$ is generated or utilized.

**In summary, Figure 2 functions as a comprehensive circuit diagram mapping the flow of information—from thalamic sensory input, through recurrent cortical processing involving the action network ($\mathbf{f}_a$), to the generation of motor patterns.**

predominantly targeting layer 5 neurons. One class of layer 5 neurons 
(with thick tufted apical dendrites and firing in bursts) send their axons 
to subcortical motor centers such as the superior colliculus and other 
parts of the brainstem19,34,43. Other layer 5 neurons, which do not fire in 
bursts and have slender apical dendrites, project to the striatum and 
other cortical regions34,43. There is also a substantial axonal projection 
from layer 5 back to layer 2/3, signifying recurrent feedback within a 
cortical column. There are additional projections from layer 5 to layer 
6, and layer 6 in turn sends outputs to the parts of the thalamus that 
send inputs to layer 4.

Computational motivation
Computational considerations point to maintaining a close link 
between actions and their sensory consequences. In model-based 
reinforcement learning44 and, more generally, in the framework of 
partially observable Markov decision processes45,46, an intelligent 
‘agent’ interacts with the world by executing an action at−1 at time t − 1, 
and this causes the agent’s ‘state’ to change from st−1 to st; this change 
is governed by the state-transition function fs(st−1, at−1), which gener-
ates a new state st according to a probability distribution P(st|st−1, at−1). 
When the agent executes an action based on a policy fa, for example, 
moving its body by walking or making an eye movement, the hidden 
state changes to the next state st (a new location in a building being 
navigated or a new part of a scene being recognized) according to

fs(st−1, at−1). Inferring these hidden states as the agent makes move-
ments is the essence of perception47,48.

APC module and neuroanatomical implementation
The above computational considerations motivate the canonical APC 
generative model shown in the figure in Box 1 (panel b). The correspond-
ing model for inference and learning, referred to as the canonical APC 
module, is described in Box 1 and shown in the figure in Box 1 (panel 
c). This figure also suggests one possible functional mapping of APC’s 
computational elements onto the cortical laminar structure in the 
figure in Box 1 (panel a), which builds on previous proposals mapping 
predictive coding to cortical laminae49,50.

As shown in the figure in Box 1 (panel c), the superficial layer cortical 
neurons, which receive the filtered sensory inputs from layer 4 and are 
recurrently connected to each other, are well suited to implementing 
the state-transition function ̂ fs. The motor output layer 5 neurons, which 
are also recurrently connected to each other, fit the role of neurons 
computing the action–policy function ̂ fa. The other class of layer 5 
neurons, which convey information to other cortical areas and the stria-
tum, could maintain the current state estimate ̂st by integrating the state 
prediction from layer 2/3 and correcting it with prediction errors from 
the feedforward thalamic inputs to layers 4 and 5/6 (ref. 1). Layer 6 neu-
rons receiving inputs from these state-estimating layer 5 neurons are 
well placed to compute the prediction for a lower-level area: at the lowest 
level, layer 6 neurons predict sensory input Īt for the input It (layer 6 
neurons at a higher level would predict the cortical state at a lower level;

for more details, see the section Hierarchical APC and cortical 
feedback).

Layer 5 motor output neurons, for example, those sending outputs 
to the superior colliculus, send axon collaterals to higher-order tha-
lamic nuclei18,19 and receive motor information from subcortical motor 
centers such as the superior colliculus regarding actions executed. 
These thalamic nuclei are therefore in an ideal position to compare the 
actual executed action at (from the superior colliculus or other motor 
center) and the cortical prediction ̂at. The resulting action feedback 
(for example, in the form of action-prediction errors), in addition to 
sensory feedback (in the form of sensory-prediction errors), can be 
conveyed by the thalamus back to the cortex to enable the 
state-transition network ̂ fs to correct its state prediction and the action 
network ̂ fa to correct its action prediction. Indeed, it is known that 
higher-order nuclei such as the pulvinar receive cortical layer 5 inputs 
and information from the superior colliculus and send axons to super-
ficial layers of area V1, explaining the response of V1 neurons to saccadic 
eye movements51.

The implementation suggested above is consistent with growing 
experimental data on predictive coding in the cortex2,4, with predic-
tion error-like activity reported in superficial layers13,52 and predictive 
activity observed in deeper layers53 and in cortico–cortical interac-
tions54,55. The implementation above also shares similarities with pre-
vious canonical circuits for predictive coding49 in specifying laminar 
roles for state estimates and prediction errors but differs in the use 
of both actions and states to generate predictions, rather than being 
limited to hidden causes49. Evidence for state and action networks in 
the cortex is summarized in Box 2.

Hierarchical APC and cortical feedback
A characteristic feature of the cortex is the reciprocal nature of con-
nections between cortical areas27: ‘feedforward’ connections from a 
cortical area A (originating in the superficial layers) to a cortical area 
B (terminating in layer 4) are invariably reciprocated by anatomically 
defined ‘feedback’ (or descending) connections from area B to area A 
(originating in the deeper (and sometimes superficial) layers of B to 
superficial and deep layers of A). Why are cortical areas reciprocally 
connected and organized in an approximate hierarchy27,56?

Computational motivation
Consider the problem of going to the grocery store from one’s house. 
As shown in Fig. 2a, the complexity of the problem can be substantially 
reduced by dividing the task into subtasks (or ‘subgoals’), dividing each 
subtask into ‘sub-subtasks’, and so on. Reducing a complex problem 
to a sequence of easier-to-solve components and reusing these com-
ponents to solve new problems gets to the heart of compositionality, 
which is thought to form the basis for cognitive flexibility and fast 
generalization in humans57,58.

A complex problem can be characterized by its (typically 
high-dimensional) state-transition function, which governs how the

The figure in Box 2 (panel c) illustrates these motor cortical 
dynamics in monkeys performing reach movements. Such 
dynamics can be learned and implemented by a recurrent neural 
network96, which in the APC model is the action network  ̂

fa. The APC action network receives as input not only local 
recurrent activity but also the current state estimate ̂s (figure in 
Box 1, panel c), which is updated using sensory feedback from 
other brain regions such as the thalamus. The APC model 
therefore predicts a close interaction between thalamic inputs 
and motor cortical outputs of the action network ̂ fa. A recent 
study by Sauerbrei et al.97 confirmed the importance of this tight

sensory–motor loop in cortical pattern generation in mice 
performing dextrous movements. They showed that time-varying 
thalamic inputs are required for cortical pattern generation.  
The neural population activity in both the thalamus and the 
cortex exhibited strong co-modulation in trial-averaged  
(figure in Box 2, panel d, left) and single-trial (figure in Box 2, 
panel d, right) activity. Inactivating the thalamus perturbed 
cortical activity and disrupted limb kinematics97, implying that 
both local dynamics and sensory-derived state contribute to 
generating cortical motor patterns (see inputs to ̂ fa in the figure 
in Box 1, panel c).

(continued from previous page)


---

## Page 6

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1226

Perspective
https://doi.org/10.1038/s41593-024-01673-9

state of the environment changes when one applies an action. Fortu-
nately, in the natural world, the consequences of most actions are local, 
and these local dynamics tend to be shared across many environments 
and objects, allowing complex problems to be modeled in terms of 
simpler lower-dimensional state-transition functions. This is illustrated 
in the example in Fig. 2b, a simplification of the ‘go to the grocery store’ 
problem: here, a maze-like environment is modeled using simpler 
components (yellow- and red-outlined rooms), each composed of even 
simpler components (corridors).

Interestingly, the same concept can also be applied to visual per-
ception. As illustrated in Fig. 2c, a visual object can be compositionally 
defined in terms of parts and their locations within the object’s reference 
frame59; the parts can in turn be decomposed into simpler parts within 
their respective reference frames. Nested compositional representations 
of objects and environments offer substantial combinatorial flexibility 
for solving complex problems in terms of simpler, reusable components. 
The fact that the world we live in and the problems we seek to solve are 
amenable to compositional solutions makes such an approach attractive, 
from both a computational and an evolutionary perspective.

The hierarchical APC model
Box 3 describes the APC model’s hierarchical architecture and its neural 
implementation. The figure in Box 3 (panel e) shows two levels of the 
model, implemented using top–down ‘contextual inputs’ to connect 
the higher level to the lower level (see Box 3 for an alternate implemen-
tation based on gain modulation).

State inference using predictive coding and compositional learn-
ing. As shown in the figure in Box 3 (panel e, left), the higher-level 
state neurons maintain an estimate for the state s(i+1)

t
 at time t and 
modulate the lower-level state network via top–down feedback given 
by H(i)

s (s(i+1)

t
). The lower-level state neurons maintain an estimate for 
si

t,τ, where τ denotes a time step at the lower level within the 
higher-level time interval given by t. The lowest-level state makes a 
prediction of the input via a ‘decoder’ network D (figure in Box 1, panel 
b). If D is a linear matrix U, this lowest level of APC is equivalent to the 
generative model in sparse coding (I = Us, where s is sparse60). At each 
time step, the network predicts the next input as a function of previ-
ous state and action. Feedforward pathways convey prediction errors 
to update state estimates1, while descending pathways convey top–
down modulation as described above (see ref. 61 for an example). 
Prediction errors are also used to learn the weights of the state net-
works at all levels using predictive coding-based self-supervised 
learning1,32,61. Such learning approximates error backpropagation, 
the workhorse of contemporary deep learning, in a biologically plau-
sible manner62.

Action inference through planning and reinforcement learning. As 
shown in the figure in Box 3 (panel e, right), the higher-level action 
neurons represent an abstract action (such as ‘open the door’) via an 
action vector a(i+1)

t
 at time t. Given the abstract action a(i+1)

t
, top–down 
feedback given by the embedding input H(i)

a (a(i+1)

t
) modulates the 
lower-level action network and instantiates the goal-specific policy

f (i)

a , which produces lower-level actions ai

t,τ. The hierarchical action 
networks in the APC model can be trained in multiple ways: (1) planning: 
the state-transition networks can be used to search for sequences of 
actions, starting from the highest abstraction level, that are likely to 
result in states with the highest cumulative reward or closest to the 
goal (see also active inference8, planning by inference63–65 and model 
predictive control66; see the section Illustrative examples of diverse 
computational capabilities). Successful actions can be used as ‘labels’

in supervised learning to train the policy networks ̂ f

(i)

a ; (2) reinforce-

ment learning: hierarchical reinforcement learning67 can be used to 
train action networks at each level to maximize the total expected 
reward according to a reward function that may be specific to that level 
(details in the section Illustrative examples of diverse computational 
capabilities); (3) policies providing priors for planning: action networks ̂

f

(i)

a at each level predict a distribution over actions, which can serve as 
a prior, in a Bayesian sense, for guiding the search for actions in plan-
ning. Thus, predicted actions for new tasks will have high uncertainty, 
requiring effort and deliberation in planning (‘system 2 thinking’ 
(ref. 68)), while, for frequently encountered tasks, action networks are 
well trained and will predict actions with high confidence (‘system 1 
thinking’ (ref. 68)).

An advantage of continuous-valued state s(i+1) and action a(i+1) 
vectors is that interpolating or sampling in the neighborhood of 
learned s(i+1) and a(i+1) generates, on the fly, new state-transition func-

tions ̃ f

(i)

s and new policy functions ̃ f

(i)

a , opening the door to fast gen-
eralization and transfer of knowledge to new tasks. The alternative to 
continuous states is to use discrete states, as in previous models of 
predictive coding based on belief propagation or variational message 
passing (for example, Fig. 10 in ref. 69). Aside from the possibility of 
fast generalization and transfer, APC’s use of continuous states also 
allows explicit representation of prediction errors, which in turn allow 
local optimization of dynamics and learning (under Gaussian 
assumptions)1.

Proposed neuroanatomical implementation
I propose that neural populations in a higher cortical area A represent-

ing current state and action vectors ̂s

(i+1) and ̂a

(i+1) modulate the state

and action networks ̂ f

(i)

s and ̂ f

(i)

a in a lower cortical area B via descend-

Go to grocery store

Walk to door
Walk to garage
Get into car +
drive to store

…

…
…

b
a
c

Open car

door

Sit inside
  Close car

door

Put on seatbelt  …

Fig. 2 | Using hierarchies and compositionality to simplify complex tasks. 
a, Decomposition of the ‘go to the grocery store’ problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building’s state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics

> Figure caption (from PDF text): Fig. 2 | Using hierarchies and compositionality to simplify complex tasks. 
a, Decomposition of the ‘go to the grocery store’ problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building’s state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics
> Figure description (generated): ## Figure Description: Panel C

This figure, labeled with the letter 'C', presents a hierarchical structure diagram, resembling a decision tree or a compositional breakdown, illustrating a process of decomposition.

**1. Overall Layout & Structure:**
The structure is organized vertically, starting with a single top node and branching downwards through multiple levels of decomposition. It functions as a flow chart demonstrating hierarchical organization.

**2. Visual Components & Symbols:**
*   **Nodes/Boxes:** The structure consists of square nodes at each level. These nodes contain stylized representations of the digit '8' or abstract visual patterns, suggesting different levels of abstraction or complexity.
*   **Connections:** Solid black lines connect the nodes, indicating a hierarchical relationship (parent-child dependency). The flow is strictly top-down.
*   **Color Coding/Markers:** There are small colored squares positioned to the left of the main structure:
    *   A solid black square ($\blacksquare$) is positioned near the top left.
    *   A small red square ($\blacksquare$) is positioned further down the left side.

**3. Labels, Keys & Legends:**
*   The panel is explicitly labeled with the capital letter **'C'** in the top left corner.
*   No explicit axis labels or mathematical notations are present within the diagram itself, only the visual content of the nodes.

**4. Data Trends & Details:**
The diagram shows a clear progression from a single, high-level concept (the top node) down to multiple low-level components.

*   **Level 1 (Top):** A single square node containing a stylized '8'.
*   **Level 2:** The top node branches into three distinct, equally sized square nodes. These nodes contain abstract visual patterns that appear more complex or detailed than the top node, though still stylized.
*   **Level 3 (Bottom):** Each of the three Level 2 nodes further branches down into a set of smaller, uniform square nodes.
    *   The leftmost Level 2 node branches into two small squares.
    *   The middle Level 2 node branches into three small squares.
    *   The rightmost Level 2 node branches into four small squares.

**5. Contextual Caption Integration:**
The provided caption mentions: "Fig. 2 | Using hierarchies and compositionality to simplify complex tasks." This context suggests that Panel C illustrates the decomposition of a complex task into simpler, constituent subtasks across multiple levels of abstraction. The visual progression from the single top node to the numerous small bottom nodes exemplifies this hierarchical decomposition process.

> Figure caption (from PDF text): Fig. 2 | Using hierarchies and compositionality to simplify complex tasks. 
a, Decomposition of the ‘go to the grocery store’ problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building’s state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics
> Figure description (generated): ## Figure Description: Panel b

This figure panel, labeled 'b', illustrates a navigation problem within a maze-like environment. The visual representation is a grid map, simulating a building layout.

**1. Overall Layout & Structure:**
The panel consists primarily of a large, two-dimensional grid structure representing the environment. To the right of this main grid, there is a schematic representation showing how the structure can be decomposed or simplified.

**2. Visual Components & Symbols:**
*   **Grid Environment:** The main body is a large grid composed of square cells. These cells are colored to represent different parts of the environment:
    *   **Black Cells:** Represent corridors or pathways.
    *   **Gray Cells:** Represent walls.
*   **Key Markers within the Grid:**
    *   A **Blue Dot** is located in a cell on the upper-left side of the grid. According to the caption, this represents the **current location**.
    *   A **Green Square** is located in a cell slightly to the right and above the blue dot. According to the caption, this represents the **desired goal location**.
*   **Bounding Boxes/Highlighting:** Several colored rectangular boxes are overlaid on the grid, indicating regions of interest or hierarchical decomposition:
    *   **Yellow Boxes:** Two distinct yellow boxes are visible. One surrounds the blue dot and adjacent cells, and another is located further down and to the right of the first.
    *   **Red Boxes:** Two prominent red boxes are visible, one in the upper-middle section and another further to the right.
    *   **Light Green Square:** A small, light green square is visible within the upper-middle section of the grid, overlapping with a red box.
*   **Decomposition Schematic (Right Side):** To the right of the main grid, there is a schematic flow diagram:
    *   The structure of the environment (the maze) leads into an arrow pointing towards a simplified representation.
    *   This schematic shows two distinct, smaller rectangular blocks: one primarily **Yellow** and another primarily **Red**.
    *   An arrow originates from the main grid structure, pointing towards these two simplified blocks.

**3. Labels, Keys & Legends:**
*   The panel is labeled with the letter **'b'**.
*   The caption provides context: "Blue dot, current location; green square, desired goal location."

**4. Data Trends & Details:**
As this is a schematic map and not a plot, there are no axes or quantitative data trends to report. The structure illustrates spatial relationships and hierarchical decomposition rather than dynamic changes over time, although the caption mentions temporal hierarchy in relation to Panel 'a'.

**5. Contextual Caption Integration:**
The caption clarifies that the grid represents "A navigation problem in a maze-like building environment with corridors (black) and walls (gray)." Furthermore, it explains that "The structure of the environment (pathways and walls) can be understood in terms of the building’s state-transition dynamics, which in turn can be divided into the simpler transition dynamics," referencing the decomposition shown on the right side of Panel b.

of its compositional elements, namely, the two rooms outlined in yellow and 
red that appear at several different locations within the reference frame of 
the environment. These simpler elements can be further decomposed into 
horizontal and vertical corridors shown on the right that appear at different 
locations within the local reference frame of each room. c, An object (such as a 
handwritten digit ‘8’) can be divided into parts (loops and curves at the middle 
level), each of which can be divided into subparts (strokes, lines, smaller curves at 
the lower level). Each part and subpart is associated with its coordinates (location 
and transformation) within a local reference frame.


---

## Page 7

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1227

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): ## Figure Description: Hierarchical APC Model and its Neural Implementation

This figure is divided into three main panels: **(a)**, **(b)**, and **(c)**.

### Panel (a): Hierarchical APC Model Diagram
Panel (a) presents a schematic diagram illustrating the hierarchical structure of the Adaptive Predictive Coding (APC) model. It is organized into three distinct levels, labeled $L^0$, $L^1$, and $L^2$.

*   **Structure:** The diagram shows interconnected layers representing different levels of abstraction.
    *   The bottom layer is labeled $L^0$. It contains nodes representing sensory input and local processing.
    *   The middle layer is labeled $L^1$. It receives input from $L^0$ and projects upwards.
    *   The top layer is labeled $L^2$. It receives input from $L^1$ and represents the highest level of abstraction.
*   **Connections:** Arrows indicate information flow:
    *   Downward arrows show the transmission of predictions/top-down influence (e.g., from $L^2$ to $L^1$, and from $L^1$ to $L^0$).
    *   Upward arrows show the transmission of prediction errors (e.g., from $L^0$ to $L^1$, and from $L^1$ to $L^2$).
*   **Nodes:** Within each layer, there are nodes labeled with mathematical notation:
    *   In $L^0$, nodes include $\sigma_{i}^{0}$, $\sigma_{j}^{0}$, and $a_{k}^{0}$.
    *   In $L^1$, nodes include $\sigma_{i}^{1}$, $\sigma_{j}^{1}$, and $a_{k}^{1}$.
    *   In $L^2$, nodes include $\sigma_{i}^{2}$, $\sigma_{j}^{2}$, and $a_{k}^{2}$.
*   **Annotations:** The diagram is annotated with the following text: "Fixation input" pointing towards $L^0$, and "Stimulus mod 1" and "Stimulus mod 2" pointing towards $L^0$.

### Panel (b): Recurrent Units Schematic
Panel (b) illustrates a schematic representation of recurrent units, likely corresponding to the processing within one level of the hierarchy.

*   **Structure:** It shows a set of interconnected nodes arranged in a circular or recurrent fashion.
*   **Nodes:** There are several labeled nodes: $\sigma_{i}^{1}$, $\sigma_{j}^{1}$, $a_{k}^{1}$, and a central node labeled "Recurrent units."
*   **Connections:** Arrows indicate recurrent connections between these nodes, suggesting internal feedback loops within the processing unit.
*   **Annotations:** The panel is labeled "Recurrent units."

### Panel (c): Neural Circuit Schematic
Panel (c) depicts a simplified neural circuit model, likely representing the implementation of the APC mechanism.

*   **Structure:** This panel is divided into two main sections: a schematic circuit diagram on the left and a time-series plot on the right.
*   **Circuit Diagram (Left):** This section shows a simplified neural network structure:
    *   It features input nodes labeled $\sigma_{i}^{0}$ and $\sigma_{j}^{0}$.
    *   These inputs feed into a processing block labeled "APC."
    *   The APC block connects to output nodes, including $\sigma_{i}^{1}$ and $\sigma_{j}^{1}$.
    *   There are feedback loops indicated by arrows connecting the output nodes back towards the input/processing area.
    *   The overall structure is framed by labels indicating "Cortical network" and "Excitatory/Inhibitory."
*   **Time-Series Plot (Right):** This is a graph showing activity over time.
    *   **Y-axis:** Labeled "Firing rate (Hz)," ranging from 0 to 80.
    *   **X-axis:** Labeled "Time (ms)," ranging from 0 to 100 ms.
    *   **Curves:** Two distinct curves are plotted:
        *   One curve, labeled "Input (AU)," shows a transient rise and decay.
        *   A second curve, labeled "Gen," shows a pattern that appears related to the input but potentially modulated.
    *   **Annotations:** The plot includes a label "Gen" near the right side, suggesting generated activity.

Box 3

Hierarchical APC model and its neural implementation

In the hierarchical APC model (figure in Box 3, panel a), a state s(i+1) 
and an action a(i+1) at abstraction level i + 1 generate, respectively, a 
state-transition function f (i)

s and a policy function f (i)

a (‘option’ (ref. 
44)) at the lower level i. These functions interact with each other to 
generate lower-level states and actions (figure in Box 3, panel a). Each 
such state and action in turn generates transition and policy functions 
at an even lower level of abstraction. A lower-level sequence 
executes for a period of time until a condition is met (for example, a 
subgoal is reached, a task is completed or times out or there is an 
irreconcilable error at that level). Control then returns to the higher 
level, which transitions to a new higher-level state (via f (i+1)

s
) and 
action (via f (i+1)

a
). Such a model captures both the dynamics of states 
(the ‘physics’ of the world) and actions (‘policies’) at different time 
scales, allowing hierarchical problem solving (Fig. 2). Biologically, the 
recurrent networks implementing fs and fa are governed by specific 
decay time constants, but differences in recurrent excitation can 
allow a hierarchy of time scales, as observed across the cortex98. 
Hierarchical dynamics in predictive coding was previously explored 
in ref. 3 for perception and production of birdsong, with lower-level

dynamics contextualized by slowly varying control parameters 
supplied by a higher level.

Can the hierarchical model in the figure in Box 3 (panel a) be 
implemented in networks of neurons? More specifically, how can a 
population of neurons, representing, for example, the higher-level 
state vector s(i+1) (or action vector a(i+1)), generate a whole function

f (i)

s (or f (i)

a ) at the lower level?

Gain modulation in the cortex. There is considerable evidence for 
‘gain modulation’ in cortical networks99–102, implemented 
computationally by multiplying the synaptic weights or outputs of 
neurons by a gain factor. Evidence for gain modulation ranges from 
multiplicative modulation of tuning curves of visual cortical neurons 
during attention103 to changes in the input–output function of 
neurons in deep layers of the cortex due to ‘top–down’ modulatory 
inputs to their apical dendrites in layers 1 and 2/3 (figure in Box 3, 
panel b)100. We can view gain modulation as a biologically plausible 
way of implementing a ‘hypernetwork’ (ref. 104), which in ML and AI is 
a neural network that produces the synaptic weights (or more

b
a

e

c

Initial

Cortical network
Excitatory
Inhibitory

Network

output

(EMG)

5 Hz

100 ms
Input (AU)

Gain
–20

Relative

firing rate (f) (Hz)

0

20

40

60

80

4
0

1
2
3

condition

Gain
modulation

d

fs

(i + 1)
fa

(i + 1)

fa

(i)

fa

(i)

fa

(i)

fs

(i)

fs

(i)

st

(i + 1)

st

(i + 1)

at

(i + 1)

Ha

(i)

st

(i + 1)
Hs

(i)

Hs

(i)

at

(i + 1)

Ha

(i)

(

(

Hs

(i)

st,τ–1

(i)

at,τ–1

(i)

st,τ–1

(i)

at,τ–1

(i)

st,τ

(i)

st,τ

(i)

at,τ

(i)

at,τ

(i)

at,τ–1

(i)

st,τ

(i)

at,τ–1

(i)

at,τ–1

(i)

256Recurrent units

Fixation output

Response

1

360°

0°

20

1

360°

0°

0
1,000
Time (ms)

Rule inputs

Stimulus mod 2

Stimulus mod 1

Fixation input

Hierarchical APC model. a, Two levels (levels i + 1 and i) of a hierarchical APC generative model. Each level has a state-transition function fs 
capturing the dynamics of the world at a particular level of abstraction and a policy function fa specifying that level’s actions, goals and 
coordinates (conditioned on the current highest-level goal or task). Higher-level state and action vectors at time t generate, via top–down 
networks Hs and Ha, lower-level state-transition and policy functions, allowing the higher level to compose a sequence of states and actions at 
the lower level to accomplish a goal. b, As depicted here for a single pyramidal neuron, I hypothesize that top–down inputs H (i)

s (s(i+1)

t
) from a 
higher cortical area to the apical dendrites of lower-area neurons modulate the dynamics of a network of such neurons (for example, via gain 
modulation100,101), allowing the higher area to change the functions fs and fa at the lower level. c, Top, multiplicative gain modulation (for 
example, due to top–down inputs) in the input–output function of neurons in a recurrent network allows the network to generate a rich set of 
motor cortical dynamics matching experimental data102. EMG, electromyogram of muscle activity. Bottom, changing the gain from 1 (black) to 2 
(blue) (bottom left plot) dramatically alters neuronal firing rates (three example neurons are shown on the right), mimicking quasi-oscillatory 
motor cortical activity (see figure in Box 2, panels c,d) (adapted from ref. 102, Springer Nature Limited). d, The function computed by a recurrent 
network (center) can be modulated using a nonchanging top–down contextual input or ‘rule input’ (one-hot vector, bottom left) in addition to 
recurrent and stimulus inputs (top left), allowing the same network to solve different tasks (output for a specific task is shown on the right) 
(adapted from ref. 72, Springer Nature Limited). Mod, modality. e, Implementation of the APC model in a using contextual inputs: higher-level 
state and action neurons maintaining estimates of s(i+1)

t
 and a(i+1)

t
 modulate lower-level state and action networks via top–down contextual 
inputs H (i)

s (s(i+1)

t
) and H (i)

a (a(i+1)

t
), respectively.


---

## Page 8

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1228

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): Since no figure image was provided, I cannot generate the detailed description.

**Please provide the academic PDF figure you would like me to describe.**

Once you provide the image, I will follow your instructions precisely:
1.  Provide a highly detailed, comprehensive, and exhaustive description of the visual and structural contents.
2.  Focus strictly on the visual evidence, adhering to all specified structural points (Layout, Components, Labels, Data Trends, Caption Integration).
3.  Return the output in clean markdown format.

ing connections that target the superficial and deep layers of area B27. 
Feedforward connections that target layer 4 of area A arise from the 
lower area B and from the higher-order thalamic region receiving ‘driver 
input’ from area B18,27. I propose that these feedforward connections 
carry the state and action feedback (for example, prediction errors) 
that enable the higher area A to correct its abstract state and action 
estimates. Such a neural implementation is consistent with studies 
reporting prediction error-like responses in superficial layers and 
state-estimation-like responses in deeper layers of the cortex2,13.

A key difference from previous formulations of hierarchical predic-
tive coding1,2,49,50 is that APC places subcortical (thalamic) populations 
center stage in the evaluation of state- and action-prediction errors 
and their broadcasting to superficial pyramidal cells in the cortex70. 
Additionally, in APC, descending connections from higher to lower 
cortical areas change the function being computed in the lower area 
(through top–down modulation), rather than only conveying 
lower-level state predictions as in traditional predictive coding1. 
Higher-area neurons representing action a(i+1)

t
 modulate the action

network ̂ f

(i)

a in a lower area, changing the policy function that this 
lower-level network is computing. Neurophysiological evidence for 
such compositional representations has recently emerged in the pre-
motor cortex71. Computational models have demonstrated composi-
tionality for task transfer using the embedding space of a(i+1)

t
 (ref. 72).

Hierarchical representations found in the visual27,29 and motor sys-
tems30 are also consistent with the hierarchical compositional approach 
espoused by the APC model. Finally, the compositional representations 
in the cortex postulated by the APC model align well with recent hypoth-
eses regarding compositional hippocampal replay73.

After the state and action networks have been learned for a set of 
tasks (as described in the section The hierarchical APC model), given a 
particular task, the topmost state vector in the hierarchy is first inferred 
from sensory inputs. This vector produces (via that level’s action net-
work ̂ fa) the topmost action vector specifying a ‘goal’ or option for the 
task; I hypothesize that this vector is maintained in the prefrontal cortex. 
Some of the pre-movement anticipatory activity in Fig. 1a may well 
reflect such a ‘cognitive’ decision. This abstract action vector is decom-
posed hierarchically all the way down to elemental actions (for example, 
muscle control signals in M1). When a sequence of elemental actions is 
executed and a subgoal is reached, control is returned back to the level 
above to generate a new subgoal (see the sections Active visual percep-

tion and part–whole learning and Planning and navigation using 
hierarchical world models for examples) and similarly for all levels. 
I postulate that such coordination between hierarchical levels for action 
selection occurs via cortex–basal ganglia–thalamus–cortex loops; 
I leave the important problem of working out the implementation 
details in these loops to future research.

Illustrative examples of diverse computational 
capabilities
The architecture of the APC model was inspired by the hypothesis that 
evolution may have replicated a common computational principle 
across the cortex20–23. If that is the case, one would expect the same 
architecture to be able to solve a diverse set of problems. Inspired by 
this observation, I provide here examples illustrating the APC model’s 
diverse capabilities.

Active visual perception and part–whole learning
Human vision can be viewed as an active sensory–motor process 
that employs eye movements to move the high-resolution fovea to 
appropriate locations in a scene, gathering evidence for or against 
competing visual hypotheses7,48. The APC architecture is well suited 
to modeling such a sensory–motor process, given its integrated state 
and action networks. To illustrate this capability, we simulated31,32 a 
two-level APC model (figure in Box 3, panel e) in which the lower-level 
actions emulated eye movements by moving a fovea (‘glimpse sensor’ 
(ref. 74)) to extract high-resolution information about a small part 
of the input image within a larger reference frame selected by the 
higher-level action.

The lower-level action also predicts a new state vector st,τ+1, which 
generates, via a trained decoder, a prediction for the glimpse image 
expected after the ‘eye movement’. The resulting prediction error was 
used for state inference and learning. The state networks at both levels 
were trained to minimize image-prediction errors, while the action 
networks were trained using reinforcement learning for the task of 
image reconstruction (for image classification as the task, see ref. 31).

Fig. 3a shows an example of a learned parsing strategy by the 
two-level APC model. The higher level learned to select actions that 
cover the input image sufficiently, avoiding blank regions, while the 
lower level learned to parse subparts inside the reference frame com-
puted by the higher level. Fig. 3a also suggests a potential explanation 
for why human perception can appear stable despite dramatic changes

plausibly, the gain parameters) for another neural network (called the 
‘primary network’). In the APC model, I propose that the higher-level 
state vector s(i+1) is fed as input to a top–down feedback network

H (i)

s , which produces the gain values to modulate the lower-level 
state network f (i)

s (and similarly for the action network). The ability of 
such a neural mechanism to modulate the function being computed 
by a cortical network was demonstrated by Stroud et al. (figure in 
Box 3, panel c), who showed that multiplicative gain modulation of a 
recurrent network can generate a rich set of motor cortical dynamics 
matching experimental data102.

Contextual inputs in the cortex. Aside from gain modulation, higher 
cortical areas can also change the function being computed by lower 
cortical networks using top–down contextual inputs. For example, 
Yang et al.72 showed that, by feeding a top–down contextual input 
(‘rule input’) as a nonchanging input to a recurrent network (in addition 
to its usual recurrent and external inputs), one can change the 
input–output function that the network computes, allowing the same 
network to solve different tasks (figure in Box 3, panel d; see also the

model of Eliasmith and colleagues105). This is known in ML as the 
‘embedding approach’ and can be shown to be equivalent in 
computational function to hypernetworks106. In the case of APC, the 
higher-level state vector s(i+1) (and action vector a(i+1)) can be fed as 
input to a top–down feedback network H (i)

s (H (i)

a ) that produces an 
embedding vector, which acts as a contextual input to a lower-level 
cortical network that computes f (i)

s ( f (i)

a ) (figure in Box 3, panel e). The 
higher level can therefore control the function being computed at the 
lower level by changing the embedding vector (contextual input).

The APC model acknowledges the existence of both gain 
modulation and contextual inputs in the cortex and postulates that 
either or both of these mechanisms are used for changing the 
functions f (i)

s and f (i)

a at the lower level according to the current 
higher-level state vector s(i+1) and the action vector a(i+1). The 
examples described in the section Illustrative examples of diverse 
computational capabilities were implemented using the method of 
contextual inputs. The reader is referred to ref. 61 for examples  
based on gain modulation and to refs. 32,33 for hypernetwork- 
based examples.

(continued from previous page)


---

## Page 9

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1229

Perspective
https://doi.org/10.1038/s41593-024-01673-9

in our retinal images due to eye movements: the model maintains a 
stable visual hypothesis that is gradually refined without exhibiting 
the rapid changes seen in the sampled image regions (Fig. 3a, actual 
glimpses). This ‘perceptual’ stability is enabled by the model’s ability 
to predict the expected glimpses for each planned ‘eye movement’ 
(Fig. 3a, predicted glimpses), similar to predictive activity observed in 
the visual cortex before eye movements (figure in Box 2, panel b)14–16.

Fig. 3b shows a learned part–whole hierarchy for a digit in terms 
of strokes and mini-strokes along with their locations within nested 
reference frames. The model learns different parsing strategies for 
different classes of objects (Fig. 3c). Setting the image-prediction

error input to the network to zero forces the model to predict the next 
sequence of parts and ‘complete’ an object32. Finally, compositional 
learning in the APC model facilitates transfer of learned knowledge to 
new objects (Fig. 3d).

Planning and navigation using hierarchical world models
Interestingly, the same APC framework used above for active vision 
can also be used for planning hierarchical actions for tasks such as 
navigation. Consider the problem of navigating from any starting 
location to any goal location in a large ‘multi-room’ building envi-
ronment such as the one in Fig. 4a (gray, walls; blue circle, current

a

b

c
d

New
input

Object
perception/
decoder
output

Part hierarchy

T-shirt
Trouser
Pullover
Dress

Shirt
Sneaker
Bag Boot
Sandal

Coat

Location hierarchy

Actual glimpses

Initial
glimpse

Predicted glimpses

Micro-steps

Macro-steps

Macro-step

1
Macro-step

2
Macro-step

3

Recons-
truction

Predicted

parts

Fig. 3 | Active vision, part–whole learning and transfer of knowledge. a, First 
row, initial glimpse (purple box) and higher-level reference frames selected (red, 
green and blue boxes) at higher-level time steps (‘macro-steps’); second row, 
regions fixated at lower-level time steps (‘micro-steps’) within each higher-level 
reference frame; third and fourth rows, predicted versus actual glimpses; fifth 
row, the model’s ‘perception’ over time (object reconstructed by a decoder 
network from the current network state). Note the model’s ‘perceptual’ stability 
despite jumps in actual glimpses, enabled by predictions of the glimpses similar 
to visual cortical predictions before eye movements (figure in Box 2, panel b).  
b, The digit ‘8’ is parsed by a trained APC model as a parse tree of parts and subparts 
(left) and their corresponding coordinates (locations) within their respective 
reference frames (right). The representation is compositional: the same set of

> Figure caption (from PDF text): Fig. 3 | Active vision, part–whole learning and transfer of knowledge. a, First 
row, initial glimpse (purple box) and higher-level reference frames selected (red, 
green and blue boxes) at higher-level time steps (‘macro-steps’); second row, 
regions fixated at lower-level time steps (‘micro-steps’) within each higher-level 
reference frame; third and fourth rows, predicted versus actual glimpses; fifth 
row, the model’s ‘perception’ over time (object reconstructed by a decoder 
network from the current network state). Note the model’s ‘perceptual’ stability 
despite jumps in actual glimpses, enabled by predictions of the glimpses similar 
to visual cortical predictions before eye movements (figure in Box 2, panel b).  
b, The digit ‘8’ is parsed by a trained APC model as a parse tree of parts and subparts 
(left) and their corresponding coordinates (locations) within their respective 
reference frames (right). The representation is compositional: the same set of
> Figure description (generated): ## Detailed Figure Description

This figure, labeled as **Fig. 3**, illustrates concepts related to active vision, part-whole learning, and knowledge transfer, structured across multiple panels (a, b, c, d).

### Panel a: Active Vision and Glimpse Prediction Flow
Panel **a** presents a multi-row, time-series visualization demonstrating the process of visual perception across different temporal scales. The structure is a sequence of columns representing time steps, organized into several rows detailing different aspects of the visual processing.

**Structure and Flow:**
The visualization flows horizontally across time steps, labeled sequentially as "Macro-steps 1," "Macro-steps 2," and "Macro-steps 3."

*   **Top Row (Macro-steps):** This row shows the overall visual input or reference frame at higher temporal resolutions.
    *   The first cell is labeled "initial glimpse (purple box)" and shows a visual representation of the digit '8' with a purple bounding box.
    *   Subsequent cells show the same object ('8') but with different colored bounding boxes (red, green, blue) indicating higher-level reference frames selected at macro-steps 1, 2, and 3.
*   **Second Row (Micro-steps):** This row details fixation points at lower temporal resolutions within the macro-step frames. It shows smaller, localized regions of interest (ROIs) corresponding to the higher-level reference frames above.
*   **Third Row (Predicted Glimpses):** This row displays the model's *predicted* visual input at each time step. These are small, localized patches of visual data.
*   **Fourth Row (Actual Glimpses):** This row displays the *actual* visual input captured at each time step, corresponding to the micro-steps.
*   **Fifth Row (Object Perception/Decoder Output):** This row shows the output of a decoder network, representing the model's reconstructed perception of the object over time. This is a full-scale rendering of the digit '8' that evolves across the macro-steps.

**Key Annotations (from Caption):**
The caption clarifies that the first row shows "initial glimpse (purple box) and higher-level reference frames selected (red, green and blue boxes) at higher-level time steps (‘macro-steps’)"; the second row shows "regions fixated at lower-level time steps (‘micro-steps’) within each higher-level reference frame"; the third and fourth rows show "predicted versus actual glimpses"; and the fifth row shows the model’s 'perception' over time.

### Panel b: Compositional Parsing of the Digit '8'
Panel **b** illustrates how a trained model parses an object into compositional parts and their spatial locations. It is divided into two main sections: "Part hierarchy" (left) and "Location hierarchy" (right).

**Left Side: Part Hierarchy:**
*   A large image of the digit '8' is shown at the top.
*   Below this, a hierarchical tree structure (a parse tree) is displayed. The root node represents the whole object ('8'), and branches descend to represent its constituent parts and subparts. The structure suggests a decomposition of the '8' into distinct components.

**Right Side: Location Hierarchy:**
*   This section shows the spatial mapping corresponding to the parts. It features a series of small, colored bounding boxes (red, green, blue) arranged in rows and columns.
*   These boxes represent the coordinates or locations of the parts identified on the left side, relative to their respective reference frames. The structure implies a mapping between abstract parts and concrete spatial locations within the visual field.

**Key Annotation (from Caption):**
The caption states that "The digit ‘8’ is parsed by a trained APC model as a parse tree of parts and subparts (left) and their corresponding coordinates (locations) within their respective reference frames (right). The representation is compositional."

### Panel c: Part-Whole Learning Examples
Panel **c** presents a grid demonstrating the application of part-whole learning across various objects.

*   The panel is organized as a grid where each cell contains an image of a different object (e.g., T-shirt, Trouser, Pullover, Dress, Coat).
*   Below the object images, there are smaller inset images showing various parts or subparts associated with that object (e.g., for "T-shirt," there are images of parts).
*   The objects listed across the top row include: "T-shirt," "Trouser," "Pullover," "Dress," and "Coat."
*   The objects listed across the bottom row include: "Sandal," "Shirt," and "Sneaker," followed by "Bag" and "Boot."

### Panel d: Knowledge Transfer
Panel **d** illustrates the concept of knowledge transfer, showing how learned parts can be reused across different contexts.

*   The panel is divided into three conceptual columns: "New input," "Reconstruction," and "Predicted parts."
*   **"New input":** Shows several abstract or partial visual inputs (e.g., fragmented shapes).
*   **"Reconstruction":** Shows the model's attempt to reconstruct a whole object based on the new input.
*   **"Predicted parts":** Shows localized patches or bounding boxes indicating which learned parts are recognized within the new input, demonstrating reuse.

**Key Annotation (from Caption):**
The caption notes that "parts and subparts can potentially be reused at other locations."

parts and subparts can potentially be reused at other locations and with other 
transformations to compose new digits. c, Higher-level part locations selected by 
a trained APC model for a particular class of clothing items in the Fashion-MNIST 
dataset (red, green and blue dots show the average sampled locations fixated in 
the following order: first, red; second, green; third, blue). Note the differences 
in the model’s fixation strategies between vertically symmetric items (shirts, 
trousers, bags) and footwear (sandals, sneakers, boots). d, An APC model trained 
on the Omniglot handwritten characters dataset (from 50 different alphabets) 
can transfer its learned knowledge to predict parts of previously unseen 
character classes. First column, input image from a new character class. Middle 
column, APC model’s reconstruction of the input. Last column, parts predicted 
by the model (d, adapted with permission from ref. 32, MIT Press).


---

## Page 10

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1230

Perspective
https://doi.org/10.1038/s41593-024-01673-9

location; green square, current goal location). Here, the lower-level 
states of the APC model are locations in the grid, and lower-level 
actions are going north, east, south or west, with a large reward at 
the goal location and smaller negative rewards for each action to 
encourage shorter paths.

Just as an object consists of parts at different locations, the build-
ing environment in Fig. 4a is composed of smaller elements (two 3 × 3 
‘room types’, S1 (red) and S2 (yellow)) at different locations in the global 
reference frame of the building. The higher-level states of the APC 
model are defined by state-embedding vectors S1 and S2, trained to 
generate, via the top–down network Hs (figure in Box 3, panel a), the 
lower-level transition functions ̂ fs for rooms S1 and S2, respectively.

Similar to how the APC vision model reconstructed an image in 
the section Active visual perception and part–whole learning by com-
posing parts from subparts, the APC model for planning computes 
higher-level action embedding vectors Ai (option vectors) that gener-
ate, via the top–down network Ha (figure in Box 3, panel a), lower-level 
policies ̂ fa that produce primitive actions (north, east, south or west) 
from any location in the local reference frame (S1 or S2) to reach a local 
goal i within that frame. Fig. 4a (right) illustrates two of the eight Ai,

each trained using reinforcement learning to reach one of the four 
corners of S1 or S2 (see ref. 32 for details). Defining these policies to 
operate within the local reference frame of the higher-level state S1 or 
S2 (regardless of global location in the building) allows the same policy 
to be reused at multiple locations.

The higher-level state network was trained to predict the next 
higher-level state. This trained higher-level network was used for plan-
ning (using model predictive control66): random state–action trajecto-
ries of length 4 were generated using the higher-level state network by 
starting from the current higher-level state and picking at random one 
of the four higher-level actions Ai for each next higher-level state. The 
action sequence with the highest total reward was selected, and its first 
action was executed. This process was repeated. Fig. 4b,c illustrates this 
high-level planning process using the trained APC model.

Fig. 4d illustrates the efficacy of the APC model’s high-level plan-
ning compared to lower-level planning using primitive actions (see ref. 
32 for details): the APC model takes significantly fewer planning steps 
and can reuse its learned higher-level actions in new combinations to 
quickly solve new tasks (for example, when the goal is changed; Fig. 4e), 
similar to a recent study in mice75 (Fig. 4f).

a
A1

A3

A4

A3

A3

A2

A1
A1
A7

Reward!

A3
x

x

x

x

x
x
x

x
x

1

3

e

c

b

d

Number of planning

steps

Episodic rewards

Correct (%)

100
10

5

0

–5

–10

0
Scratch

Pretraining

20

40

60

80

100

Low-level planning
APC planning

RL agent
APC agent
Goal changed
80

60

40

20

0

0
5
10
15
20
0
500
1,000
2,000

1
2
3

Session

Composite task

4
5

1,500

Distance from goal
Episodes

f

***

Fig. 4 | Hierarchical planning. a, The problem of navigating in a large 
environment (left) can be reduced to planning using high-level states (red- and 
yellow-outlined ‘rooms’) and high-level abstract actions (panels on the right 
show two abstract actions, A1 and A3). Blue, current location; gray, walls; green, 
current goal location. b, To navigate to the goal, the APC model uses its learned 
high-level state network to sample K high-level state–action sequences (K = 2 
here, shown bifurcating from the initial state). In each sequence, the high-level 
state is depicted by a predicted room image (red- or yellow-outlined image) and 
its location (marked by an ‘X’ in the rectangular global frame below the image). 
High-level actions are depicted as square local frames (next to arrows) with 
goal locations (purple). c, Given the sampled sequences, the model picks the 
sequence with the highest total reward, executes this sequence’s first (high-level) 
action to reach the blue location (top) and repeats to reach the goal location with

> Figure caption (from PDF text): Fig. 4 | Hierarchical planning. a, The problem of navigating in a large 
environment (left) can be reduced to planning using high-level states (red- and 
yellow-outlined ‘rooms’) and high-level abstract actions (panels on the right 
show two abstract actions, A1 and A3). Blue, current location; gray, walls; green, 
current goal location. b, To navigate to the goal, the APC model uses its learned 
high-level state network to sample K high-level state–action sequences (K = 2 
here, shown bifurcating from the initial state). In each sequence, the high-level 
state is depicted by a predicted room image (red- or yellow-outlined image) and 
its location (marked by an ‘X’ in the rectangular global frame below the image). 
High-level actions are depicted as square local frames (next to arrows) with 
goal locations (purple). c, Given the sampled sequences, the model picks the 
sequence with the highest total reward, executes this sequence’s first (high-level) 
action to reach the blue location (top) and repeats to reach the goal location with
> Figure description (generated): ## Figure 4 Description: Hierarchical Planning

This figure, labeled "Fig. 4," illustrates a hierarchical planning process across several panels (a through f), combining visual representations of an environment, abstract state/action sequences, and performance plots.

### Panel (a): Environment and High-Level States
Panel (a) displays a grid-based environment map.
*   **Environment:** The background is a dark gray grid representing the navigable space, interspersed with black blocks representing walls.
*   **Locations:** A blue circle indicates the current location. A green square marks the current goal location.
*   **High-Level States:** Two distinct areas are outlined: a red rectangle and a yellow rectangle, representing high-level states or "rooms."
*   **Abstract Actions:** To the right of the environment map, there are two panels illustrating abstract actions:
    *   **$A_1$:** Shows an upward arrow ($\uparrow$) and a rightward arrow ($\rightarrow$), suggesting movement or transition. A purple square is associated with this action, likely indicating a goal location within that abstract context.
    *   **$A_3$:** Shows a downward arrow ($\downarrow$) and an upward arrow ($\uparrow$), also associated with a purple square goal location.

### Panel (b): State-Action Sequence Sampling
Panel (b) illustrates the process of sampling high-level state–action sequences.
*   **Flow:** The panel shows a bifurcation originating from the initial state (implied, though not explicitly drawn as a starting node).
*   **Sequences:** Two sequences are shown branching out:
    1.  A sequence associated with a red-outlined image (representing a predicted room image) and an 'X' marker in the global frame below it.
    2.  A sequence associated with a yellow-outlined image and an 'X' marker in the global frame below it.
*   **High-Level Actions:** Next to these sequences, there are square local frames depicting high-level actions. These frames contain arrows and a purple circle indicating goal locations, corresponding to the abstract actions shown in Panel (a).
*   **Reward:** At the bottom right, a green box labeled "Reward!" indicates the outcome of the sequence evaluation.

### Panel (c): Sequence Execution
Panel (c) shows a continuation of the planning process, likely after sequence selection.
*   **Environment:** A grid environment similar to (a) is shown.
*   **States/Goals:** The red and yellow outlined areas are present, along with the blue current location and a green goal location.
*   **Execution:** The caption implies that the model selects the sequence with the highest reward and executes its first high-level action to reach a blue location (top), repeating the process until the green goal is reached.

### Panel (d): Sequence Representation Detail
Panel (d) provides a detailed view of the sampled sequences, showing transitions between abstract states.
*   **Structure:** It displays a sequence of state/action representations: $A_3 \rightarrow A_1$, followed by transitions involving states represented by red and yellow outlined images, each marked with an 'X' in a small global frame.
*   **Transitions:** Arrows connect these elements, indicating the flow through the sequence. The final element shows a transition leading to $A_7$ (a new abstract action/state).

### Panel (e): Episodic Rewards Plot
Panel (e) is a line graph tracking performance over time.
*   **Y-axis:** Labeled "Episodic rewards," ranging from approximately -10 to 10.
*   **X-axis:** Labeled with numerical values (e.g., 0, 500, 1000, 1500, 2000), representing steps or episodes.
*   **Curves:** Two lines are plotted:
    *   A light blue line, labeled "Low-level planning," showing a generally increasing trend.
    *   A red line, labeled "APC agent," showing a fluctuating but generally lower trend compared to the low-level planning.
*   **Annotations:** Green dots are placed along the x-axis, labeled "Goal changed," indicating points where the goal state was modified during training.

### Panel (f): Composite Task Performance Plot
Panel (f) is a scatter plot showing task success rate over training sessions.
*   **Y-axis:** Labeled "Correct (%)", ranging from 0 to 100.
*   **X-axis:** Labeled "Session," ranging from 1 to 5.
*   **Data Points/Trend:** A red line connects data points, showing a clear upward trend in the percentage of correct completions as the session number increases.
*   **Annotation:** A triple asterisk ($***$) is placed near the top right, indicating statistical significance.

only three high-level actions (bottom). Small red dot, intermediate location; 
small blue dot, intermediate goal. d, High-level planning by the APC model versus 
low-level heuristic planning using primitive actions (see text for details). e, The 
APC model can reuse learned high-level actions in new combinations to quickly 
solve new tasks (green circles, times at which the navigation goal changed); a 
reinforcement learning (RL) agent needs to relearn a new policy from scratch. 
Blue- or red-shaded regions in d,e are 1 s.d. from the mean. f, Mice pretrained on 
two subtasks quickly learned to combine them to solve a new composite task75 
(compare with the APC model in e after a goal change). Blue, performance of mice 
learning the task from scratch (compare with the reinforcement learning agent in 
e after a goal change) (a–e, adapted with permission from ref. 32, MIT Press;  
f, adapted from ref. 75, CC BY 4.0).


---

## Page 11

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1231

Perspective
https://doi.org/10.1038/s41593-024-01673-9

> Figure description (generated): Since no figure was provided, I cannot generate the detailed description. Please provide the academic PDF or the specific figure you would like me to describe, and I will proceed with a highly detailed, comprehensive, and exhaustive analysis following all your specified guidelines.

Episodic memories and cortical–hippocampal binding
Each level of the APC hierarchy learns generic ‘basis functions’ for rep-
resenting states and actions based on interactions with the environ-
ment. For example, the basis functions learned by the lowest-level state

network when the inputs are natural videos comprise oriented spati-
otemporal Gabor filters coding for edges and bars moving at different 
orientations61. The neural activity vector is a specific activation pattern 
coding for the current video segment in terms of the learned

Box 4

Model flexibility and predictions

The APC model appears to be flexible enough to perform a diverse 
set of functions such as: (1) parsing images and learning part–whole 
hierarchies: the model uses eye movements to parse images and 
learn hierarchical representations of parts and subparts of objects 
(details in the section Active visual perception and part–whole 
learning); (2) invariant perception: learned representations of 
objects and sequences are transformed by the APC generative 
model to match current inputs and remain invariant to different 
types of transformations (translations were considered in the 
section Active visual perception and part–whole learning, other 
transformations such as rotations and scaling are included in ref. 33); 
(3) perceptual stability: inference in the APC model naturally 
leads to integration of information across actions such as eye 
movements, leading to perceptual stability (examples in the section 
Active visual perception and part–whole learning; see also refs. 
23,59,74); (4) compositionality and fast transfer of knowledge: by 
learning compositional representations, the model can compose 
and generate new objects and action sequences, leading to fast 
generalization to new inputs and goals (examples in the sections 
Active visual perception and part–whole learning and Planning and 
navigation using hierarchical world models); (5) efficient planning: 
hierarchical state networks in the APC model can be used to solve 
tasks efficiently (for example, navigating in a large environment) by 
planning using hierarchical actions (details in the section Planning 
and navigation using hierarchical world models; see also ref. 107); 
(6) habit formation: successful plans can be used to learn new 
policies (‘habits’; see the section Planning and navigation using 
hierarchical world models); alternately, the APC model also allows 
policies to be learned using hierarchical reinforcement learning (see 
the section Active visual perception and part–whole learning); (7) 
reference frames and temporal hierarchies: the APC model provides 
a neural implementation of nested reference frames23 and offers an 
explanation for object-centered parts-based representations in the 
cortex108 as well as cortical temporal hierarchies28,29; (8) prediction 
and postdiction: because the model maintains a temporally stable 
higher-level state (a ‘timeline’ (ref. 76)) encoding an entire sequence 
(past, present and future), the update of this representation 
during prediction error minimization explains both predictive and 
postdictive phenomena in perception (for example, flash lag and 
color phi effects; see ref. 61 for details); (9) generating ‘schemas’ 
or ‘programs’ for solving new tasks: the APC model suggests a 
neural mechanism (via top–down inputs and/or gain modulation) 
for generating new sensory–motor ‘programs’ or ‘schemas’ on the 
fly to solve new tasks (Box 3 and ref. 109); (10) binding and episodic 
memories of perception–action sequences: when coupled with a 
hippocampus-like associative memory, the model binds multimodal 
cortical activations at the highest level into an episodic memory, 
allowing activity recall, prediction based on episodic context 
and cortical consolidation for fast generalization and learning, 
as discussed in the section Episodic memories and cortical–
hippocampal binding; (11) language and symbolic representations: 
making state and action representations categorical (for example, 
ref. 78) and using cortical–hippocampal binding may allow the APC

model to bind sensory and symbolic representations for language 
processing and cognitive tasks such as arithmetic (see the section 
Learning abstract concepts and ref. 58); (12) learning abstract 
concepts: the same sensory–motor architecture used for perception 
and planning can also be used to model abstract concepts such as 
family trees (details in the section Learning abstract concepts  
and ref. 77).

The APC model makes the following predictions:
•
• The laminar implementation proposed in the figure in Box 1 (panel 
c) predicts that, in each cortical area, neurons representing the 
sensory-derived latent state will exhibit predictive activity, 
representing the output of the state-transition function ̂ fs, as a 
function of both sensory inputs and deeper-layer ‘action’ inputs; 
experimental manipulation of deeper-layer activity should allow 
control of this predictive activity and change this activity similar to 
how the predicted glimpses change in Fig. 3a as a function of 
action inputs to ̂ fs.
•
• In each cortical area (including traditional ‘sensory’ areas), the 
model predicts a population of neurons in layer 5 representing 
‘actions’, either motor outputs (for example, in M1 or the primary 
somatosensory cortex) or abstract actions or goals (for example, 
in the parietal or prefrontal cortex); this action-related population 
activity in layer 5 should change in a coordinated manner across 
cortical areas whenever the goal or task is changed, similar to 
how the lower- and higher-level actions change in the APC model 
whenever the goal location is changed in Fig. 4a.
•
• As depicted in the figure in Box 3 (panels a,e), feedback from a 
higher cortical area should originate from two separate 
populations (higher-level state- and action-representing neurons) 
and specifically target two separate populations in the lower area 
(lower-level state- and action-representing neurons, respectively); 
this feedback should be modulatory and capable of changing the 
functional connectivity of their target populations, emulating the 
effects of the ‘hypernetworks’ H (i)

s and H (i)

a in the figure in Box 3

(panels a,e). Experimental manipulation of this feedback should

selectively change the lower-level functions ̂ f

(i)

s and ̂ f

(i)

a being

computed, with the effects becoming apparent in the state 
predictions being generated by ̂ fs (see predicted glimpses in 
Fig. 3a) and the actions being output by ̂ fa (see primitive actions in 
Fig. 4c (bottom)), respectively.
•
• APC’s hierarchical arrangement predicts the existence of 
both state and action representations in higher-order cortical 
areas that encode information over longer time scales than 
lower areas28,29,61,80,98,110; furthermore, the model predicts that a 
substantial population-level activity change in the superficial 
layers of a higher area, denoting a higher-level state change 
triggered by a subgoal being achieved by the lower area, would 
cause a large population-level activity change in layer 5, signifying 
a new high-level action or subgoal being generated (for example, 
the high-level action leading to macro-step 2 or macro-step 3  
in Fig. 3a or a subgoal that reaches the lower yellow square in  
Fig. 4c (top)).


---

## Page 12

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1232

Perspective
https://doi.org/10.1038/s41593-024-01673-9

spatiotemporal filters. At the highest level N of the APC model, the 
specific activation patterns ̂s

(N) and ̂a

(N) together represent (figure in 
Box 3, panel e, with i + 1 = N) an entire sequence (or timeline76) corre-
sponding to the current episode of interaction with the environment, 
for example, the sequence of glimpses of an object as in Fig. 3a or the 
sequence of locations visited during navigation as in Fig. 4c (bottom). 
By ‘binding’ these highest-level neural activation patterns ̂s

(N) and ̂a

(N) 
(assumed to correspond to entorhinal cortex activity in the APC model) 
in a hippocampus-like associative memory, one can store the current 
sequence of experienced sensations (vision, touch, sound, smell, 
rewards, etc.), locations (or coordinates within a reference frame) and 
actions as an episodic memory vector m (ref. 61).

The projection from the hippocampus back to the entorhinal 
cortex implies that the fused multimodal information in the current 
episodic memory vector m is fed back to enable better prediction (m 
plays a role similar to context windows in transformers in AI) and to 
influence state and action estimation in cortical areas down the hierar-
chy to the lowest levels. Particularly salient episodic memory vectors 
may be stored and later compositionally recombined73 or recalled for 
replay in the cortex when given an internal or external cue, for example, 
a location where the episode occurred, a sound or smell associated 
with the episode or a partial visual input marking the beginning of the 
episode (see ref. 61 for an example).

In summary, the APC model suggests that the cortex encodes 
generic semantic knowledge about the world within state and action 
networks that implement nested reference frames. Any particular 
instantiation of this knowledge invoked by, for example, an interac-
tion with a person or an object, is stored temporarily as an episodic 
memory vector m in the hippocampus. This instantiation could be 
used for reasoning about the current situation or for planning and, if 
deemed important, could be consolidated within the cortex by updat-
ing cortical networks via replay during inactivity or sleep. The idea 
of fast binding of specific instances (‘fillers’) with generic semantic 
‘roles’ is gaining currency in both AI58 and hippocampal modeling (for 
example, the Tolman–Eichenbaum machine77; see also ref. 73). The 
benefits of such a representation, including fast transfer of knowl-
edge and zero-shot learning, can be expected to also accrue to the 
memory-augmented APC model.

Learning abstract concepts
I briefly sketch here how the same sensory–motor architecture used 
for perception and planning above could also be potentially used to 
model abstract concepts. Take, for example, modeling the concept of 
a family tree. The state–action representations in the APC model can 
be made categorical (for example, as in ref. 78), allowing states and 
actions to represent symbols. The states can then represent abstract 
categories such as father, mother, daughter, uncle, etc., while abstract 
actions (up, down, etc.) can be used to traverse and define a family tree 
sequentially. The notion of ‘fast binding’ of cortical representations in 
hippocampal memory discussed above could be used to bind specific 
persons to their roles (father, mother, etc.).

Results along these lines were obtained using the Tolman–Eichen-
baum machine model77, in which a recurrent neural network (similar 
to the state-transition network in the APC model but for a single level) 
was used in conjunction with an associative memory to learn the struc-
ture of family trees from examples. Extending these ideas to abstract 
state–action networks for symbolic reasoning in a hierarchical APC 
model may offer new insights into understanding how cortical–hip-
pocampal networks represent language and solve abstract cognitive 
tasks such as arithmetic.

Discussion
Inspired by recent results highlighting the influence of actions across 
most areas of the cortex, I suggested APC as a sensory–motor theory of 
cortical function. APC proposes that (1) each cortical area implements

both a state-transition network for state prediction and an action net-
work for action (or goal) prediction, and (2) higher-area neurons rep-
resenting more abstract states and actions modulate lower-area state 
and action networks via top–down modulatory control to change the 
functions they are computing, leading to nested reference frames and 
hierarchical representations of objects, states and actions. A possible 
neuroanatomical mapping of the APC model to cortical laminar struc-
ture was suggested in the section APC module and neuroanatomical 
implementation.

The APC model lends support to the hypothesis20–23 that there may 
be a unifying computational principle operating across the cortex by 
showing how the same basic APC architecture can perform a diverse 
range of computations (see Box 4 for a summary). The APC model 
shares broad similarities with a number of other models advocating 
prediction and hierarchy as core aspects of brain function1,3,22,23,79–83, 
going back to the seminal early work of MacKay84 and Albus85. The 
goal of putting action on an equal footing with perception in terms 
of Bayesian inference and prediction error minimization is in keeping 
with the theories of free energy minimization proposed by Friston and 
others3,8,69. In its current formulation, APC addresses action selection 
via reinforcement learning (see the section Active visual perception 
and part–whole learning) and planning via model predictive control 
(as described in the section Planning and navigation using hierar-
chical world models). The latter is related to planning as inference 
methods63–65 and active inference schemes that optimize expected 
information gain plus expected value8,69.

Compositionality and the representation of sensory–motor infor-
mation in cortical columns are also central tenets of the ‘thousand 
brains’ theory23,59. The close interaction between state-estimation 
networks and action-computing networks in the APC model is con-
sistent with theories of optimal motor control86, especially theories 
highlighting the importance of internal models in solving the inverse 
problem of computing optimal motor commands to solve a task81,87,88. 
However, based on recent evidence pointing to outputs from layer 5 in 
essentially all cortical areas to subcortical motor centers19,34,35,37, the APC 
model proposes that all cortical areas include both state-estimation 
and policy components. M1 is often cited as a uniquely ‘motor’ cortical 
area missing the sensory input layer 4, with damage to M1 in primates 
causing permanent loss of distal (although not proximal) movements89. 
However, even M1 receives sensory information from other cortical and 
subcortical areas90, especially in its superficial layers39,40, and could 
therefore, as suggested by the APC model, predict and estimate state 
(for example, proprioceptive state) and compute actions based on 
these state estimates91.

The APC generative model in the figure in Box 3 (panel a) focuses on 
hierarchical structure and does not account for cross-modal (sensory 
to sensory) or hierarchically ‘horizontal’ connections in the neocortex 
(for example, ref. 92). However, it is possible to extend APC’s generative 
model to allow cross-modal influences and horizontal interactions to 
enable more accurate state prediction and estimation. For example, 
consider a generative model evolved for use by an animal foraging in 
the forest: the hidden state denoting, for example, a tiger, can generate 
both a visual cue (stripes) and an auditory cue (rustling sound). In the 
extended APC model employing such a generative model, the state 
network in a sensory area (for example, V1) would leverage information 
from other sensory modalities (for example, from the auditory cortex) 
via horizontal cortical connections to derive an accurate estimate of 
the current state of the world. Extending the APC model to account 
for such cross-modal and horizontal cortico–cortical connections is 
an important direction for future work.

A large number of unknowns remain such as the exact physiologi-
cal mechanisms underlying the modulatory interactions between 
higher-order and lower-order cortical areas across multiple time 
scales, the role of alpha, beta, theta and gamma oscillations in such 
interactions and the representation of uncertainty in the cortex.


---

## Page 13

Nature Neuroscience | Volume 27 | July 2024 | 1221–1235
1233

Perspective
https://doi.org/10.1038/s41593-024-01673-9

While there is emerging neurophysiological and neuroanatomical 
evidence2,9–11,13–16,18,41,42,51,55,93 that lends some support to the APC model’s 
predictions (Box 4), there is much that remains to be tested. I hope 
that the theoretical framework offered by the APC model is helpful in 
the design of new experiments aimed at uncovering the cortical and 
subcortical basis of sensory–motor processing and cognition.