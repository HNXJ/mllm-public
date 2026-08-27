## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

nature neuroscience

Perspective
A sensory-motor theory of the neocortex

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
compositional representations, for example, part-whole hierarchies, (4) 
how complex actions can be planned using simpler actions, and (5) how we 
form episodic memories of sensory-motor experiences and learn abstract 
concepts such as a family tree. I postulate a mapping of the APC model to the 
laminar architecture of the cortex and suggest possible roles for cortico-
cortical and cortico-subcortical pathways.

The predictive coding theory of cortical function, proposed in this jour-
nal in 1999 by the author and Ballard1, has been the subject of increasing 
attention in recent years2-4. However, as originally proposed, the theory 
ignored a fundamental aspect of perception, namely, that perception is 
action based: we move our eyes about three times a second to recognize 
objects in a scene, orient our heads to localize sounds, use our fingers to 
identify objects by touch and navigate ourselves in our environment to 
solve tasks that satisfy our needs. Away from experimentally imposed 
constraints in the laboratory, perception, in its natural state, can best 
be viewed as an action-based hypothesis-testing process (also called 
active sensing, active perception and active inference)5-8.

Recent studies have highlighted the important influence of 
impending actions across almost all cortical areas (Fig. 1). For exam-
ple, in mice solving a visual discrimination task using forepaws to 
rotate a wheel, Zatka-Haas et al.9 observed, using widefield calcium 
imaging, extensive bilateral activity across cortical areas preceding 
movements on choice trials (left or right action selected) but not on 
'NoGo' trials (no action is selected) (Fig. 1a, left). They further showed 
that impending movement could be decoded from cortical activity 
in most imaged regions by 25 ms before movement (Fig. 1a, right). In 
the same task, Steinmetz et al.10 used Neuropixels probes to record 
spiking activity from thousands of neurons and showed that, not

only does activity in the visual cortex get updated after movement 
(Fig. 1b, left), but almost all recorded cortical areas had neurons 
with activities that were predictive of upcoming movements (Fig. 1b, 
right). Similarly, Stringer et al.11 found that about a third of the popu-
lation activity of ~10,000 neurons in the visual cortex of awake mice 
could be predicted from motor actions derived from a video of the 
mouse's facial movements (Fig. 1c), suggesting that sensory-motor 
integration occurs even in the primary sensory cortex (the lack of a 
similar result in monkeys12 could be due to the increased functional 
specialization of primate visual cortical areas compared to that of 
the rodent cortex).

Actions may be integrated differently across the different layers 
of a cortical area. For example, Jordan and Keller13 showed that both 
layer 2/3 and layer 5/6 neurons in the mouse primary visual cortex 
(V1) undergo depolarization before locomotion onset (Fig. 1d, left and 
middle). While layer 2/3 neurons appear to be computing a difference 
between motor-related input and bottom-up visual flow input, layer 
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

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

consisting of a state-prediction network and an action-prediction net-
work, both implemented within each cortical area. 'State' here denotes 
hidden (or 'latent') aspects of the world inferred from sensory inputs, 
for example, parts of an object to be recognized or one's location in a 
building. 'Action' refers to not just motor commands but also abstract 
actions, for example, 'go to the maternal grandmother node' in a family 
tree or 'perform multiplication' on two given numbers. APC postulates 
that feedback from higher cortical areas modulates the dynamics of 
both state and action networks in lower areas, changing the functions 
they compute on the fly to suit the needs of the current task. This leads 
to representations that operate at multiple levels of sensory and motor 
abstraction, as observed in cortical hierarchies implicated in percep-
tion and action27-30. In the following sections, I present computational 
and neurobiological aspects of APC, comparing emerging studies and 
experimental results with the model's predictions. I present simula-
tions chosen to showcase the explanatory breadth of APC. While we 
have previously investigated APC in the context of machine learning 
(ML) and artificial intelligence (AI)31-33, here I explore APC as a model 
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
of 'efference copies' of upcoming actions ('corollary discharges' 
(ref. 17)) as well as the results of executed actions. Such a view harmo-
nizes well with the anatomical observation that all areas of the neocor-
tex (henceforth, the 'cortex'), including areas traditionally labeled as 
sensory cortices, send outputs to subcortical motor regions (refs. 18,19 
and references therein) and receive input from these regions. Indeed, 
Vernon Mountcastle, in his prescient article in 1978 (ref. 20), put forth 
the hypothesis that a single unifying computational principle might 
be operating across the entire cortex, proposing the 'cortical col-
umn' as a modular information-processing unit of the cortex (see also 
refs. 21-23 for related ideas). This hypothesis is supported by the 
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

In this Perspective, I suggest APC as a unifying sensory-motor 
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

100 ms

VISp
VISal
-0.3

dF/F (%)

Decoder acc. (%)

0.3

0.2

-0.2

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

-2
-4
-6

Mismatch response

(mV)

4 mV

Neural activity prediction (test set) from face motion

Neural activity (test set) sorted by 1D embedding

150 MOs
MOp

SSp

Stim onset

NoGo

b

Contra

VISpm neuron
Action encoding

Neurons (%)

In summary, the figure compares neural responses (measured as $\text{dF/F}$) in two behavioral contexts ("Stim onset" vs. "NoGo") across a temporal sequence (0 to 200 ms), highlighting the dynamic recruitment of specific cortical areas like MOs, SSp, VISp, and VISal.

Ipsi

Locomotion onset
Locomotion onset

-2

-20

-10

Time (s)

Vm response (mV)

Sorted neuron #

Fig. 1 | Widespread influence of actions across the cortex. a, Left, widefield 
calcium imaging reveals bilateral activity (cortical fluorescence dF/F) from 0 to 
200 ms after stimulus (stim) onset across cortical areas preceding movements 
on left or right (L/R) action-selection trials. 'NoGo' trials do not show such 
activity. Right, average action execution decoder accuracy (acc.) 25 ms before 
movement onset, showing that an impending movement can be decoded from 
cortical activity in most imaged regions (adapted from ref. 9, CC BY 4.0). MOs, 
secondary motor cortical area; MOp, primary motor cortex; SSp, primary 
somatosensory cortex; VISp, primary visual cortex; VISal, secondary visual 
cortical area. b, Left, increased spiking after a correct choice movement in a 
visual cortex neuron (posteromedial visual area, VISpm) for both contralateral 
(contra) and ipsilateral (ipsi) stimulus presentations (orange and blue dots, 
spikes; black dots, movement onset). Right, fraction of neurons in each brain 
region with pre-movement activity that could be accurately predicted from 
the animal's movement (in either the left or right direction) (adapted from 
ref. 10, Springer Nature Limited). c, Motor action information extracted using

> Figure caption (from PDF text): Fig. 1 | Widespread influence of actions across the cortex. a, Left, widefield 
calcium imaging reveals bilateral activity (cortical fluorescence dF/F) from 0 to 
200 ms after stimulus (stim) onset across cortical areas preceding movements 
on left or right (L/R) action-selection trials. 'NoGo' trials do not show such 
activity. Right, average action execution decoder accuracy (acc.) 25 ms before 
movement onset, showing that an impending movement can be decoded from 
cortical activity in most imaged regions (adapted from ref. 9, CC BY 4.0). MOs, 
secondary motor cortical area; MOp, primary motor cortex; SSp, primary 
somatosensory cortex; VISp, primary visual cortex; VISal, secondary visual 
cortical area. b, Left, increased spiking after a correct choice movement in a 
visual cortex neuron (posteromedial visual area, VISpm) for both contralateral 
(contra) and ipsilateral (ipsi) stimulus presentations (orange and blue dots, 
spikes; black dots, movement onset). Right, fraction of neurons in each brain 
region with pre-movement activity that could be accurately predicted from 
the animal's movement (in either the left or right direction) (adapted from 
ref. 10, Springer Nature Limited). c, Motor action information extracted using

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

This figure, labeled as **BOX 1**, illustrates the structure of a "Canonical APC module" across three distinct panels: (a), (b), and (c). The overall style is a schematic diagram representing neural circuit architecture.

---

### Annotations and Labels (Across Panels)
*   **Numerical Markers:** In Panel (a), there are numerical markers $1, 2/3, 4, 5, 6$ positioned near the layers. In Panel (b), similar markers $1, 2/3, 4, 5, 6$ are present. In Panel (c), the same numerical markers $1, 2/3, 4, 5, 6$ are present near the corresponding layers in the lower schematic.
*   **Variables:** The variables $\vec{a}_t$ and $\vec{f}_t$ are prominently displayed in Panel (c).
*   **Caption Context:** The caption clarifies that the diagram represents a "six-layered laminar structure of a cortical column," and that Panel (c) shows the "possible implementation of inference in a canonical APC module."

layer 5 neurons in the primary somatosensory cortex send outputs 
to the spinal cord37, which controls body movements. On the other 
hand, layer 5 neurons in the primary motor cortex (or M1) (such as Betz 
cells) have long been implicated in motor function via their axonal 
projections to the spinal cord38, but the middle and upper layers of 
traditional 'motor' cortical areas such as M1 are involved in sensory 
processing of feedback from subcortical and cortical sources39,40: for 
example, layer 2/3 neurons in mouse M1 respond to unexpected sen-
sory perturbations in a visually guided motor task41, while neurons in 
mouse M2 encode auditory sensation and expectation42. Thus, despite

well-known differences in the laminar densities of neurons in different 
cortical areas (for example, V1 versus M1), the sensory-motor nature 
of the cortex is retained. This motivates the idea of a 'sensory-motor 
cortical module' as a canonical feature of the cortex (described further 
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
world, the agent can learn an 'internal model' of the world81,87,88,94 
(also called a 'world model', forward model or generative model) 
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
actions requires considerable effort and deliberation ('system 2' 
thinking68). A more efficient way to select actions ('system 1' 
thinking68) is to have a state-to-action 'policy' (ref. 44) ̂ fa, which maps 
the current estimated state ̂st directly to an action ̂at to achieve the 
current goal (figure in Box 1, panel c). Biologically, the policy ̂ fa can 
be implemented by a recurrent network of neurons with activity at 
time t denoting ̂at.

Coupling perception and action. Given a policy ̂ fa for a particular 
task or goal, the agent can execute an action ̂at  
from the policy while simultaneously sending ̂at as an 'efference 
copy' (or 'corollary discharge' (ref. 17)) to the learned model ̂ fs to 
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

2/3
at-1

at

st-1
st

st
at-1

fs

fa

D

Lower-order 
thalamus

Higher-order 
thalamus
Motor 
centers

ât-1

ât

ŝt-1

ât-1
ŝt

fs

fa

D

c

Lower-order thalamus
Higher-order thalamus

2/3

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

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

### Exhaustive Figure Description (Hypothetical based on Caption Context)

This figure, designated as **Figure 2**, appears to be a complex schematic diagram illustrating the functional architecture of sensorimotor control, specifically detailing the interaction between cortical motor dynamics and thalamic inputs within a recurrent neural network framework. The structure is likely divided into multiple panels (Panel A, Panel B, and Panel C) to delineate different aspects of the system.

#
#
#
#
#
## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

state of the environment changes when one applies an action. Fortu-
nately, in the natural world, the consequences of most actions are local, 
and these local dynamics tend to be shared across many environments 
and objects, allowing complex problems to be modeled in terms of 
simpler lower-dimensional state-transition functions. This is illustrated 
in the example in Fig. 2b, a simplification of the 'go to the grocery store' 
problem: here, a maze-like environment is modeled using simpler 
components (yellow- and red-outlined rooms), each composed of even 
simpler components (corridors).

Interestingly, the same concept can also be applied to visual per-
ception. As illustrated in Fig. 2c, a visual object can be compositionally 
defined in terms of parts and their locations within the object's reference 
frame59; the parts can in turn be decomposed into simpler parts within 
their respective reference frames. Nested compositional representations 
of objects and environments offer substantial combinatorial flexibility 
for solving complex problems in terms of simpler, reusable components. 
The fact that the world we live in and the problems we seek to solve are 
amenable to compositional solutions makes such an approach attractive, 
from both a computational and an evolutionary perspective.

The hierarchical APC model
Box 3 describes the APC model's hierarchical architecture and its neural 
implementation. The figure in Box 3 (panel e) shows two levels of the 
model, implemented using top-down 'contextual inputs' to connect 
the higher level to the lower level (see Box 3 for an alternate implemen-
tation based on gain modulation).

State inference using predictive coding and compositional learn-
ing. As shown in the figure in Box 3 (panel e, left), the higher-level 
state neurons maintain an estimate for the state s(i+1)

t
 at time t and 
modulate the lower-level state network via top-down feedback given 
by H(i)

s (s(i+1)

t
). The lower-level state neurons maintain an estimate for 
si

t,τ, where τ denotes a time step at the lower level within the 
higher-level time interval given by t. The lowest-level state makes a 
prediction of the input via a 'decoder' network D (figure in Box 1, panel 
b). If D is a linear matrix U, this lowest level of APC is equivalent to the 
generative model in sparse coding (I = Us, where s is sparse60). At each 
time step, the network predicts the next input as a function of previ-
ous state and action. Feedforward pathways convey prediction errors 
to update state estimates1, while descending pathways convey top-
down modulation as described above (see ref. 61 for an example). 
Prediction errors are also used to learn the weights of the state net-
works at all levels using predictive coding-based self-supervised 
learning1,32,61. Such learning approximates error backpropagation, 
the workhorse of contemporary deep learning, in a biologically plau-
sible manner62.

Action inference through planning and reinforcement learning. As 
shown in the figure in Box 3 (panel e, right), the higher-level action 
neurons represent an abstract action (such as 'open the door') via an 
action vector a(i+1)

t
 at time t. Given the abstract action a(i+1)

t
, top-down 
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
goal (see also active inference8, planning by inference63-65 and model 
predictive control66; see the section Illustrative examples of diverse 
computational capabilities). Successful actions can be used as 'labels'

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
requiring effort and deliberation in planning ('system 2 thinking' 
(ref. 68)), while, for frequently encountered tasks, action networks are 
well trained and will predict actions with high confidence ('system 1 
thinking' (ref. 68)).

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
fast generalization and transfer, APC's use of continuous states also 
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

...

...
...

b
a
c

Open car

door

Sit inside
  Close car

door

Put on seatbelt  ...

Fig. 2 | Using hierarchies and compositionality to simplify complex tasks. 
a, Decomposition of the 'go to the grocery store' problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building's state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics

> Figure caption (from PDF text): Fig. 2 | Using hierarchies and compositionality to simplify complex tasks. 
a, Decomposition of the 'go to the grocery store' problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building's state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics

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
a, Decomposition of the 'go to the grocery store' problem into subgoals or 
subtasks, each of which can be further divided into sub-subgoals or sub-subtasks. 
Note that the rate of change is faster at the lower levels than at the higher levels, 
leading naturally to a temporal hierarchy. b, A navigation problem in a maze-like 
building environment with corridors (black) and walls (gray). Blue dot, current 
location; green square, desired goal location. The structure of the environment 
(pathways and walls) can be understood in terms of the building's state-transition 
dynamics, which in turn can be divided into the simpler transition dynamics

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
The caption clarifies that the grid represents "A navigation problem in a maze-like building environment with corridors (black) and walls (gray)." Furthermore, it explains that "The structure of the environment (pathways and walls) can be understood in terms of the building's state-transition dynamics, which in turn can be divided into the simpler transition dynamics," referencing the decomposition shown on the right side of Panel b.

of its compositional elements, namely, the two rooms outlined in yellow and 
red that appear at several different locations within the reference frame of 
the environment. These simpler elements can be further decomposed into 
horizontal and vertical corridors shown on the right that appear at different 
locations within the local reference frame of each room. c, An object (such as a 
handwritten digit '8') can be divided into parts (loops and curves at the middle 
level), each of which can be divided into subparts (strokes, lines, smaller curves at 
the lower level). Each part and subpart is associated with its coordinates (location 
and transformation) within a local reference frame.

---

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

This figure is divided into three main panels: **(a)**, **(b)**, and **(c)**.

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

Once you provide the image, I will follow your instructions precisely:
1.  Provide a highly detailed, comprehensive, and exhaustive description of the visual and structural contents.
2.  Focus strictly on the visual evidence, adhering to all specified structural points (Layout, Components, Labels, Data Trends, Caption Integration).
3.  Return the output in clean markdown format.

ing connections that target the superficial and deep layers of area B27. 
Feedforward connections that target layer 4 of area A arise from the 
lower area B and from the higher-order thalamic region receiving 'driver 
input' from area B18,27. I propose that these feedforward connections 
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
(through top-down modulation), rather than only conveying 
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
from sensory inputs. This vector produces (via that level's action net-
work ̂ fa) the topmost action vector specifying a 'goal' or option for the 
task; I hypothesize that this vector is maintained in the prefrontal cortex. 
Some of the pre-movement anticipatory activity in Fig. 1a may well 
reflect such a 'cognitive' decision. This abstract action vector is decom-
posed hierarchically all the way down to elemental actions (for example, 
muscle control signals in M1). When a sequence of elemental actions is 
executed and a subgoal is reached, control is returned back to the level 
above to generate a new subgoal (see the sections Active visual percep-

tion and part-whole learning and Planning and navigation using 
hierarchical world models for examples) and similarly for all levels. 
I postulate that such coordination between hierarchical levels for action 
selection occurs via cortex-basal ganglia-thalamus-cortex loops; 
I leave the important problem of working out the implementation 
details in these loops to future research.

Illustrative examples of diverse computational 
capabilities
The architecture of the APC model was inspired by the hypothesis that 
evolution may have replicated a common computational principle 
across the cortex20-23. If that is the case, one would expect the same 
architecture to be able to solve a diverse set of problems. Inspired by 
this observation, I provide here examples illustrating the APC model's 
diverse capabilities.

Active visual perception and part-whole learning
Human vision can be viewed as an active sensory-motor process 
that employs eye movements to move the high-resolution fovea to 
appropriate locations in a scene, gathering evidence for or against 
competing visual hypotheses7,48. The APC architecture is well suited 
to modeling such a sensory-motor process, given its integrated state 
and action networks. To illustrate this capability, we simulated31,32 a 
two-level APC model (figure in Box 3, panel e) in which the lower-level 
actions emulated eye movements by moving a fovea ('glimpse sensor' 
(ref. 74)) to extract high-resolution information about a small part 
of the input image within a larger reference frame selected by the 
higher-level action.

The lower-level action also predicts a new state vector st,τ+1, which 
generates, via a trained decoder, a prediction for the glimpse image 
expected after the 'eye movement'. The resulting prediction error was 
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
'primary network'). In the APC model, I propose that the higher-level 
state vector s(i+1) is fed as input to a top-down feedback network

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
cortical networks using top-down contextual inputs. For example, 
Yang et al.72 showed that, by feeding a top-down contextual input 
('rule input') as a nonchanging input to a recurrent network (in addition 
to its usual recurrent and external inputs), one can change the 
input-output function that the network computes, allowing the same 
network to solve different tasks (figure in Box 3, panel d; see also the

model of Eliasmith and colleagues105). This is known in ML as the 
'embedding approach' and can be shown to be equivalent in 
computational function to hypernetworks106. In the case of APC, the 
higher-level state vector s(i+1) (and action vector a(i+1)) can be fed as 
input to a top-down feedback network H (i)

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

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

in our retinal images due to eye movements: the model maintains a 
stable visual hypothesis that is gradually refined without exhibiting 
the rapid changes seen in the sampled image regions (Fig. 3a, actual 
glimpses). This 'perceptual' stability is enabled by the model's ability 
to predict the expected glimpses for each planned 'eye movement' 
(Fig. 3a, predicted glimpses), similar to predictive activity observed in 
the visual cortex before eye movements (figure in Box 2, panel b)14-16.

Fig. 3b shows a learned part-whole hierarchy for a digit in terms 
of strokes and mini-strokes along with their locations within nested 
reference frames. The model learns different parsing strategies for 
different classes of objects (Fig. 3c). Setting the image-prediction

error input to the network to zero forces the model to predict the next 
sequence of parts and 'complete' an object32. Finally, compositional 
learning in the APC model facilitates transfer of learned knowledge to 
new objects (Fig. 3d).

Planning and navigation using hierarchical world models
Interestingly, the same APC framework used above for active vision 
can also be used for planning hierarchical actions for tasks such as 
navigation. Consider the problem of navigating from any starting 
location to any goal location in a large 'multi-room' building envi-
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

Macro-step

Macro-step

Recons-
truction

Predicted

parts

Fig. 3 | Active vision, part-whole learning and transfer of knowledge. a, First 
row, initial glimpse (purple box) and higher-level reference frames selected (red, 
green and blue boxes) at higher-level time steps ('macro-steps'); second row, 
regions fixated at lower-level time steps ('micro-steps') within each higher-level 
reference frame; third and fourth rows, predicted versus actual glimpses; fifth 
row, the model's 'perception' over time (object reconstructed by a decoder 
network from the current network state). Note the model's 'perceptual' stability 
despite jumps in actual glimpses, enabled by predictions of the glimpses similar 
to visual cortical predictions before eye movements (figure in Box 2, panel b).  
b, The digit '8' is parsed by a trained APC model as a parse tree of parts and subparts 
(left) and their corresponding coordinates (locations) within their respective 
reference frames (right). The representation is compositional: the same set of

> Figure caption (from PDF text): Fig. 3 | Active vision, part-whole learning and transfer of knowledge. a, First 
row, initial glimpse (purple box) and higher-level reference frames selected (red, 
green and blue boxes) at higher-level time steps ('macro-steps'); second row, 
regions fixated at lower-level time steps ('micro-steps') within each higher-level 
reference frame; third and fourth rows, predicted versus actual glimpses; fifth 
row, the model's 'perception' over time (object reconstructed by a decoder 
network from the current network state). Note the model's 'perceptual' stability 
despite jumps in actual glimpses, enabled by predictions of the glimpses similar 
to visual cortical predictions before eye movements (figure in Box 2, panel b).  
b, The digit '8' is parsed by a trained APC model as a parse tree of parts and subparts 
(left) and their corresponding coordinates (locations) within their respective 
reference frames (right). The representation is compositional: the same set of

This figure, labeled as **Fig. 3**, illustrates concepts related to active vision, part-whole learning, and knowledge transfer, structured across multiple panels (a, b, c, d).

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

location; green square, current goal location). Here, the lower-level 
states of the APC model are locations in the grid, and lower-level 
actions are going north, east, south or west, with a large reward at 
the goal location and smaller negative rewards for each action to 
encourage shorter paths.

Just as an object consists of parts at different locations, the build-
ing environment in Fig. 4a is composed of smaller elements (two 3 × 3 
'room types', S1 (red) and S2 (yellow)) at different locations in the global 
reference frame of the building. The higher-level states of the APC 
model are defined by state-embedding vectors S1 and S2, trained to 
generate, via the top-down network Hs (figure in Box 3, panel a), the 
lower-level transition functions ̂ fs for rooms S1 and S2, respectively.

Similar to how the APC vision model reconstructed an image in 
the section Active visual perception and part-whole learning by com-
posing parts from subparts, the APC model for planning computes 
higher-level action embedding vectors Ai (option vectors) that gener-
ate, via the top-down network Ha (figure in Box 3, panel a), lower-level 
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
ning (using model predictive control66): random state-action trajecto-
ries of length 4 were generated using the higher-level state network by 
starting from the current higher-level state and picking at random one 
of the four higher-level actions Ai for each next higher-level state. The 
action sequence with the highest total reward was selected, and its first 
action was executed. This process was repeated. Fig. 4b,c illustrates this 
high-level planning process using the trained APC model.

Fig. 4d illustrates the efficacy of the APC model's high-level plan-
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

e

c

b

d

Number of planning

steps

Episodic rewards

Correct (%)

-5

-10

Scratch

Pretraining

Low-level planning
APC planning

RL agent
APC agent
Goal changed

1,000
2,000

Session

Composite task

1,500

Distance from goal
Episodes

f

***

Fig. 4 | Hierarchical planning. a, The problem of navigating in a large 
environment (left) can be reduced to planning using high-level states (red- and 
yellow-outlined 'rooms') and high-level abstract actions (panels on the right 
show two abstract actions, A1 and A3). Blue, current location; gray, walls; green, 
current goal location. b, To navigate to the goal, the APC model uses its learned 
high-level state network to sample K high-level state-action sequences (K = 2 
here, shown bifurcating from the initial state). In each sequence, the high-level 
state is depicted by a predicted room image (red- or yellow-outlined image) and 
its location (marked by an 'X' in the rectangular global frame below the image). 
High-level actions are depicted as square local frames (next to arrows) with 
goal locations (purple). c, Given the sampled sequences, the model picks the 
sequence with the highest total reward, executes this sequence's first (high-level) 
action to reach the blue location (top) and repeats to reach the goal location with

> Figure caption (from PDF text): Fig. 4 | Hierarchical planning. a, The problem of navigating in a large 
environment (left) can be reduced to planning using high-level states (red- and 
yellow-outlined 'rooms') and high-level abstract actions (panels on the right 
show two abstract actions, A1 and A3). Blue, current location; gray, walls; green, 
current goal location. b, To navigate to the goal, the APC model uses its learned 
high-level state network to sample K high-level state-action sequences (K = 2 
here, shown bifurcating from the initial state). In each sequence, the high-level 
state is depicted by a predicted room image (red- or yellow-outlined image) and 
its location (marked by an 'X' in the rectangular global frame below the image). 
High-level actions are depicted as square local frames (next to arrows) with 
goal locations (purple). c, Given the sampled sequences, the model picks the 
sequence with the highest total reward, executes this sequence's first (high-level) 
action to reach the blue location (top) and repeats to reach the goal location with

This figure, labeled "Fig. 4," illustrates a hierarchical planning process across several panels (a through f), combining visual representations of an environment, abstract state/action sequences, and performance plots.

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

Episodic memories and cortical-hippocampal binding
Each level of the APC hierarchy learns generic 'basis functions' for rep-
resenting states and actions based on interactions with the environ-
ment. For example, the basis functions learned by the lowest-level state

network when the inputs are natural videos comprise oriented spati-
otemporal Gabor filters coding for edges and bars moving at different 
orientations61. The neural activity vector is a specific activation pattern 
coding for the current video segment in terms of the learned

Box 4

Model flexibility and predictions

The APC model appears to be flexible enough to perform a diverse 
set of functions such as: (1) parsing images and learning part-whole 
hierarchies: the model uses eye movements to parse images and 
learn hierarchical representations of parts and subparts of objects 
(details in the section Active visual perception and part-whole 
learning); (2) invariant perception: learned representations of 
objects and sequences are transformed by the APC generative 
model to match current inputs and remain invariant to different 
types of transformations (translations were considered in the 
section Active visual perception and part-whole learning, other 
transformations such as rotations and scaling are included in ref. 33); 
(3) perceptual stability: inference in the APC model naturally 
leads to integration of information across actions such as eye 
movements, leading to perceptual stability (examples in the section 
Active visual perception and part-whole learning; see also refs. 
23,59,74); (4) compositionality and fast transfer of knowledge: by 
learning compositional representations, the model can compose 
and generate new objects and action sequences, leading to fast 
generalization to new inputs and goals (examples in the sections 
Active visual perception and part-whole learning and Planning and 
navigation using hierarchical world models); (5) efficient planning: 
hierarchical state networks in the APC model can be used to solve 
tasks efficiently (for example, navigating in a large environment) by 
planning using hierarchical actions (details in the section Planning 
and navigation using hierarchical world models; see also ref. 107); 
(6) habit formation: successful plans can be used to learn new 
policies ('habits'; see the section Planning and navigation using 
hierarchical world models); alternately, the APC model also allows 
policies to be learned using hierarchical reinforcement learning (see 
the section Active visual perception and part-whole learning); (7) 
reference frames and temporal hierarchies: the APC model provides 
a neural implementation of nested reference frames23 and offers an 
explanation for object-centered parts-based representations in the 
cortex108 as well as cortical temporal hierarchies28,29; (8) prediction 
and postdiction: because the model maintains a temporally stable 
higher-level state (a 'timeline' (ref. 76)) encoding an entire sequence 
(past, present and future), the update of this representation 
during prediction error minimization explains both predictive and 
postdictive phenomena in perception (for example, flash lag and 
color phi effects; see ref. 61 for details); (9) generating 'schemas' 
or 'programs' for solving new tasks: the APC model suggests a 
neural mechanism (via top-down inputs and/or gain modulation) 
for generating new sensory-motor 'programs' or 'schemas' on the 
fly to solve new tasks (Box 3 and ref. 109); (10) binding and episodic 
memories of perception-action sequences: when coupled with a 
hippocampus-like associative memory, the model binds multimodal 
cortical activations at the highest level into an episodic memory, 
allowing activity recall, prediction based on episodic context 
and cortical consolidation for fast generalization and learning, 
as discussed in the section Episodic memories and cortical-
hippocampal binding; (11) language and symbolic representations: 
making state and action representations categorical (for example, 
ref. 78) and using cortical-hippocampal binding may allow the APC

model to bind sensory and symbolic representations for language 
processing and cognitive tasks such as arithmetic (see the section 
Learning abstract concepts and ref. 58); (12) learning abstract 
concepts: the same sensory-motor architecture used for perception 
and planning can also be used to model abstract concepts such as 
family trees (details in the section Learning abstract concepts  
and ref. 77).

The APC model makes the following predictions:
•
• The laminar implementation proposed in the figure in Box 1 (panel 
c) predicts that, in each cortical area, neurons representing the 
sensory-derived latent state will exhibit predictive activity, 
representing the output of the state-transition function ̂ fs, as a 
function of both sensory inputs and deeper-layer 'action' inputs; 
experimental manipulation of deeper-layer activity should allow 
control of this predictive activity and change this activity similar to 
how the predicted glimpses change in Fig. 3a as a function of 
action inputs to ̂ fs.
•
• In each cortical area (including traditional 'sensory' areas), the 
model predicts a population of neurons in layer 5 representing 
'actions', either motor outputs (for example, in M1 or the primary 
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
effects of the 'hypernetworks' H (i)

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
• APC's hierarchical arrangement predicts the existence of 
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

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

spatiotemporal filters. At the highest level N of the APC model, the 
specific activation patterns ̂s

(N) and ̂a

(N) together represent (figure in 
Box 3, panel e, with i + 1 = N) an entire sequence (or timeline76) corre-
sponding to the current episode of interaction with the environment, 
for example, the sequence of glimpses of an object as in Fig. 3a or the 
sequence of locations visited during navigation as in Fig. 4c (bottom). 
By 'binding' these highest-level neural activation patterns ̂s

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
of fast binding of specific instances ('fillers') with generic semantic 
'roles' is gaining currency in both AI58 and hippocampal modeling (for 
example, the Tolman-Eichenbaum machine77; see also ref. 73). The 
benefits of such a representation, including fast transfer of knowl-
edge and zero-shot learning, can be expected to also accrue to the 
memory-augmented APC model.

Learning abstract concepts
I briefly sketch here how the same sensory-motor architecture used 
for perception and planning above could also be potentially used to 
model abstract concepts. Take, for example, modeling the concept of 
a family tree. The state-action representations in the APC model can 
be made categorical (for example, as in ref. 78), allowing states and 
actions to represent symbols. The states can then represent abstract 
categories such as father, mother, daughter, uncle, etc., while abstract 
actions (up, down, etc.) can be used to traverse and define a family tree 
sequentially. The notion of 'fast binding' of cortical representations in 
hippocampal memory discussed above could be used to bind specific 
persons to their roles (father, mother, etc.).

Results along these lines were obtained using the Tolman-Eichen-
baum machine model77, in which a recurrent neural network (similar 
to the state-transition network in the APC model but for a single level) 
was used in conjunction with an associative memory to learn the struc-
ture of family trees from examples. Extending these ideas to abstract 
state-action networks for symbolic reasoning in a hierarchical APC 
model may offer new insights into understanding how cortical-hip-
pocampal networks represent language and solve abstract cognitive 
tasks such as arithmetic.

Discussion
Inspired by recent results highlighting the influence of actions across 
most areas of the cortex, I suggested APC as a sensory-motor theory of 
cortical function. APC proposes that (1) each cortical area implements

both a state-transition network for state prediction and an action net-
work for action (or goal) prediction, and (2) higher-area neurons rep-
resenting more abstract states and actions modulate lower-area state 
and action networks via top-down modulatory control to change the 
functions they are computing, leading to nested reference frames and 
hierarchical representations of objects, states and actions. A possible 
neuroanatomical mapping of the APC model to cortical laminar struc-
ture was suggested in the section APC module and neuroanatomical 
implementation.

The APC model lends support to the hypothesis20-23 that there may 
be a unifying computational principle operating across the cortex by 
showing how the same basic APC architecture can perform a diverse 
range of computations (see Box 4 for a summary). The APC model 
shares broad similarities with a number of other models advocating 
prediction and hierarchy as core aspects of brain function1,3,22,23,79-83, 
going back to the seminal early work of MacKay84 and Albus85. The 
goal of putting action on an equal footing with perception in terms 
of Bayesian inference and prediction error minimization is in keeping 
with the theories of free energy minimization proposed by Friston and 
others3,8,69. In its current formulation, APC addresses action selection 
via reinforcement learning (see the section Active visual perception 
and part-whole learning) and planning via model predictive control 
(as described in the section Planning and navigation using hierar-
chical world models). The latter is related to planning as inference 
methods63-65 and active inference schemes that optimize expected 
information gain plus expected value8,69.

Compositionality and the representation of sensory-motor infor-
mation in cortical columns are also central tenets of the 'thousand 
brains' theory23,59. The close interaction between state-estimation 
networks and action-computing networks in the APC model is con-
sistent with theories of optimal motor control86, especially theories 
highlighting the importance of internal models in solving the inverse 
problem of computing optimal motor commands to solve a task81,87,88. 
However, based on recent evidence pointing to outputs from layer 5 in 
essentially all cortical areas to subcortical motor centers19,34,35,37, the APC 
model proposes that all cortical areas include both state-estimation 
and policy components. M1 is often cited as a uniquely 'motor' cortical 
area missing the sensory input layer 4, with damage to M1 in primates 
causing permanent loss of distal (although not proximal) movements89. 
However, even M1 receives sensory information from other cortical and 
subcortical areas90, especially in its superficial layers39,40, and could 
therefore, as suggested by the APC model, predict and estimate state 
(for example, proprioceptive state) and compute actions based on 
these state estimates91.

The APC generative model in the figure in Box 3 (panel a) focuses on 
hierarchical structure and does not account for cross-modal (sensory 
to sensory) or hierarchically 'horizontal' connections in the neocortex 
(for example, ref. 92). However, it is possible to extend APC's generative 
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
for such cross-modal and horizontal cortico-cortical connections is 
an important direction for future work.

A large number of unknowns remain such as the exact physiologi-
cal mechanisms underlying the modulatory interactions between 
higher-order and lower-order cortical areas across multiple time 
scales, the role of alpha, beta, theta and gamma oscillations in such 
interactions and the representation of uncertainty in the cortex.

---

## 

Nature Neuroscience | Volume 27 | July 2024 | 1221-1235

Perspective

While there is emerging neurophysiological and neuroanatomical 
evidence2,9-11,13-16,18,41,42,51,55,93 that lends some support to the APC model's 
predictions (Box 4), there is much that remains to be tested. I hope 
that the theoretical framework offered by the APC model is helpful in 
the design of new experiments aimed at uncovering the cortical and 
subcortical basis of sensory-motor processing and cognition.