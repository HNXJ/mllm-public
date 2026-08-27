## Page 1

Despite the wealth of empirical data in neuroscience, 
there are relatively few global theories about how the 
brain works. A recently proposed free-energy principle 
for adaptive systems tries to provide a unified account 
of action, perception and learning. Although this prin-
ciple has been portrayed as a unified brain theory1, its 
capacity to unify different perspectives on brain function 
has yet to be established. This Review attempts to place 
some key theories within the free-energy framework, in 
the hope of identifying common themes. I first review 
the free-energy principle and then deconstruct several 
global brain theories to show how they all speak to the 
same underlying idea.

The free-energy principle
The free-energy principle (BOX 1) says that any self- 
organizing system that is at equilibrium with its environ-
ment must minimize its free energy2. The principle is 
essentially a mathematical formulation of how adaptive 
systems (that is, biological agents, like animals or brains) 
resist a natural tendency to disorder3–6. What follows is 
a non-mathematical treatment of the motivation and 
implications of the principle. We will see that although the 
motivation is quite straightforward, the implications are 
complicated and diverse. This diversity allows the prin-
ciple to account for many aspects of brain structure and 
function and lends it the potential to unify different per-
spectives on how the brain works. In subsequent sections, 
I discuss how the principle can be applied to neuronal 
systems as viewed from these perspectives. This Review 
starts in a rather abstract and technical way but then tries 
to unpack the basic idea in more familiar terms.

Motivation: resisting a tendency to disorder. The 
defining characteristic of biological systems is that 
they maintain their states and form in the face of a 
constantly changing environment3–6. From the point 
of view of the brain, the environment includes both 
the external and the internal milieu. This maintenance 
of order is seen at many levels and distinguishes bio-
logical from other self-organizing systems; indeed, the 
physiology of biological systems can be reduced almost 
entirely to their homeostasis7. More precisely, the rep-
ertoire of physiological and sensory states in which an 
organism can be is limited, and these states define the 
organism’s phenotype. Mathematically, this means that 
the probability of these (interoceptive and exterocep-
tive) sensory states must have low entropy; in other 
words, there is a high probability that a system will 
be in any of a small number of states, and a low prob-
ability that it will be in the remaining states. Entropy 
is also the average self information or ‘surprise’8 
(more formally, it is the negative log-probability of an 
outcome). Here, ‘a fish out of water’ would be in a sur-
prising state (both emotionally and mathematically). 
A fish that frequently forsook water would have high 
entropy. Note that both surprise and entropy depend 
on the agent: what is surprising for one agent (for 
example, being out of water) may not be surprising 
for another. Biological agents must therefore mini-
mize the long-term average of surprise to ensure that 
their sensory entropy remains low. In other words, 
biological systems somehow manage to violate the 
fluctuation theorem, which generalizes the second law 
of thermodynamics9.

The Wellcome Trust Centre  
for Neuroimaging,  
University College London, 
Queen Square, London, 
WC1N 3BG, UK.
e‑mail:  
k.friston@fil.ion.ucl.ac.uk
doi:10.1038/nrn2787
Published online  
13 January 2010

Free energy
An information theory measure 
that bounds or limits (by being 
greater than) the surprise on 
sampling some data, given a 
generative model.

Homeostasis
The process whereby an open 
or closed system regulates its 
internal environment to 
maintain its states within 
bounds.

Entropy
The average surprise of 
outcomes sampled from a 
probability distribution or 
density. A density with low 
entropy means that, on 
average, the outcome is 
relatively predictable. Entropy 
is therefore a measure of 
uncertainty.

The free-energy principle:  
a unified brain theory?

Karl Friston

Abstract | A free-energy principle has been proposed recently that accounts for action, 
perception and learning. This Review looks at some key brain theories in the biological (for 
example, neural Darwinism) and physical (for example, information theory and optimal 
control theory) sciences from the free-energy perspective. Crucially, one key theme runs 
through each of these theories — optimization. Furthermore, if we look closely at what is 
optimized, the same quantity keeps emerging, namely value (expected reward, expected 
utility) or its complement, surprise (prediction error, expected cost). This is the quantity that 
is optimized under the free-energy principle, which suggests that several global brain 
theories might be unified within a free-energy framework.

REVIEWS

> Figure description (generated): Since no figure was provided, I cannot generate the detailed description. Please provide the academic PDF figure you would like me to describe.

Once you provide the image, I will structure my response according to your requirements:

1. **Overall Layout & Structure**
2. **Visual Components & Symbols**
3. **Labels, Keys & Legends**
4. **Data Trends & Details** (If applicable)
5. **Contextual Caption Integration** (Using the provided context: "The free-energy principle: a unified brain theory?")

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 127

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 2

a

b

Sensations

s~ = g(x~, ϑ) + z~

Action or control signals

a = arg min F(s~, μ)

Internal states

μ = arg min F(s~, μ)

External states

˙x~ = f(x~, a, ϑ) + w~

Environment
Agent

Free-energy bound on surprise

F = −<ln p(s~, ϑ | m)>q + <ln q(ϑ | μ)>q

Action minimizes prediction errors

F = D(q(ϑ | μ) || p(ϑ)) − <ln p(s~(a) | ϑ, m)>q

a = arg max Accuracy

Perception optimizes predictions

F = D(q(ϑ | μ) || p(ϑ | s~)) − ln p(s~

|  m)

μ = arg max Divergence
Surprise
(Surprisal or self information.) 
The negative log-probability of 
an outcome. An improbable 
outcome (for example, water 
flowing uphill) is therefore 
surprising.

Fluctuation theorem
(A term from statistical 
mechanics.) Deals with the 
probability that the entropy  
of a system that is far from the 
thermodynamic equilibrium 
will increase or decrease over  
a given amount of time. It 
states that the probability of 
the entropy decreasing 
becomes exponentially smaller 
with time.

Attractor
A set to which a dynamical 
system evolves after a long 
enough time. Points that  
get close to the attractor 
remain close, even under  
small perturbations.

Kullback-Leibler divergence
(Or information divergence, 
information gain or cross 
entropy.) A non-commutative 
measure of the non-negative 
difference between two 
probability distributions.

Recognition density
(Or ‘approximating conditional 
density’.) An approximate 
probability distribution of the 
causes of data (for example, 
sensory input). It is the product 
of inference or inverting a 
generative model.

In short, the long-term (distal) imperative — of main-
taining states within physiological bounds — translates 
into a short-term (proximal) avoidance of surprise. 
surprise here relates not just to the current state, which 
cannot be changed, but also to movement from one state 
to another, which can change. This motion can be com-
plicated and itinerant (wandering) provided that it revis-
its a small set of states, called a global random attractor10, 
that are compatible with survival (for example, driving a 
car within a small margin of error). It is this motion that 
the free-energy principle optimizes.

so far, all we have said is that biological agents must 
avoid surprises to ensure that their states remain within 
physiological bounds (see supplementary information s1 
(box) for a more formal argument). But how do they 
do this? A system cannot know whether its sensations 
are surprising and could not avoid them even if it did 
know. This is where free energy comes in: free energy is 
an upper bound on surprise, which means that if agents 
minimize free energy, they implicitly minimize surprise.

Crucially, free energy can be evaluated because it is a 
function of two things to which the agent has access: its 
sensory states and a recognition density that is encoded 
by its internal states (for example, neuronal activity 
and connection strengths). The recognition density is a 
probabilistic representation of what caused a particular 
sensation.

This (variational) free-energy construct was 
introduced into statistical physics to convert difficult 
probability-density integration problems into eas-
ier optimization problems11. It is an information 
theoretic quantity (like surprise), as opposed to a 
thermo dynamic quantity. variational free energy has 
been exploited in machine learning and statistics to 
solve many inference and learning problems12–14. In this 
setting, surprise is called the (negative) model evidence. 
This means that minimizing surprise is the same as 
maximizing the sensory evidence for an agent’s exist-
ence, if we regard the agent as a model of its world. In 
the present context, free energy provides the answer to

Box 1 | The free-energy principle

Part a of the figure shows the dependencies among the 
quantities that define free energy. These include the 
internal states of the brain μ(t) and quantities describing its 
exchange with the environment: sensory signals (and their 
motion) s˜(t) = [s,s′,s″…]T  plus action a(t). The environment 
is described by equations of motion, which specify the 
trajectory of its hidden states. The causes ϑ ⊃ {x˜, θ, γ } of 
sensory input comprise hidden states x˜(t), parameters θ 
and precisions γ controlling the amplitude of the random 
fluctuations  z˜(t) and  w˜(t). Internal brain states and action 
minimize free energy F(s˜,μ), which is a function of sensory 
input and a probabilistic representation q(ϑ|μ) of its causes. 
This representation is called the recognition density and is 
encoded by internal states μ.

The free energy depends on two probability densities: 
the recognition density q(ϑ|μ) and one that generates 
sensory samples and their causes, p(s˜,ϑ|m). The latter 
represents a probabilistic generative model (denoted by 
m), the form of which is entailed by the agent or brain.  
Part b of the figure provides alternative expressions for the 
free energy to show what its minimization entails: action 
can reduce free energy only by increasing accuracy (that is, 
selectively sampling data that are predicted). Conversely, 
optimizing brain states makes the representation an 
approximate conditional density on the causes of sensory 
input. This enables action to avoid surprising sensory 
encounters. A more formal description is provided below.

optimizing the sufficient statistics (representations)
Optimizing the recognition density makes it a posterior or conditional density on the causes of sensory data: this can be 
seen by expressing the free energy as surprise –In p(s˜,| m) plus a Kullback-Leibler divergence between the recognition and 
conditional densities (encoded by the ‘internal states’ in the figure). Because this difference is always positive, minimizing 
free energy makes the recognition density an approximate posterior probability. This means the agent implicitly infers or 
represents the causes of its sensory samples in a Bayes-optimal fashion. At the same time, the free energy becomes a tight 
bound on surprise, which is minimized through action.

optimizing action
Acting on the environment by minimizing free energy enforces a sampling of sensory data that is consistent with the 
current representation. This can be seen with a second rearrangement of the free energy as a mixture of accuracy and 
complexity. Crucially, action can only affect accuracy (encoded by the ‘external states’ in the figure). This means that  
the brain will reconfigure its sensory epithelia to sample inputs that are predicted by the recognition density — in other 
words, to minimize prediction error.

REVIEWS

> Figure description (generated): ## Figure Description: The Free-Energy Principle

This figure is a conceptual block diagram illustrating the relationship between different components of the Free-Energy Principle, divided into two main panels, **(a)** and **(b)**.

### Panel (a): Core Components of Free Energy Minimization

Panel (a) presents a flow diagram illustrating the relationship between environmental interaction, sensory processing, and internal state maintenance.

**Layout and Structure:**
The panel is structured horizontally with three main conceptual blocks: "Environment," a central processing block, and "Agent."

**Visual Components & Flow:**
1.  **Environment Block (Left):** A rectangular box labeled "Environment." An arrow points from this block towards the central processing area.
2.  **Central Processing Block (Middle):** This section contains two interconnected boxes representing the internal state dynamics:
    *   The top box is labeled **"Sensations."** Inside this box, the mathematical expression $\hat{s} = g(\vec{x}, \theta) + z$ is displayed.
    *   The bottom box is labeled **"External states."** Inside this box, the mathematical expression $\vec{x} = f(\hat{s}, \alpha, \theta) + w$ is displayed.
    *   An arrow flows from "Sensations" down to "External states," indicating a dependency or flow between these two internal representations.
3.  **Agent Block (Right):** A rectangular box labeled "Agent." An arrow points from the central processing area towards this block.
4.  **Internal States Block (Bottom Right):** Below the "Agent" box, there is a smaller block labeled **"Internal states."** Inside this block, the expression $\mu = \arg \min F(\hat{s}, \mu)$ is shown.

**Connections and Flow:**
*   An arrow originates from the "Environment" block, pointing towards the "Sensations" box.
*   The flow proceeds from "Sensations" $\rightarrow$ "External states."
*   An arrow connects the output of the internal state dynamics (implied from "External states") towards the "Agent" block.
*   The relationship $\mu = \arg \min F(\hat{s}, \mu)$ is positioned below the main flow, indicating the optimization goal related to internal states.

### Panel (b): Optimization and Predictive Structure

Panel (b) presents a more detailed, layered flow diagram focusing on the predictive nature of the system.

**Layout and Structure:**
This panel is structured vertically, showing a progression from sensory input to predictive optimization.

**Visual Components & Flow:**
1.  **Top Block (Input):** A box labeled **"Free-energy bound on surprise."** Inside this box, the expression $F = -\ln p(\hat{s}|\mu) + \ln q(\hat{s}|\mu)$ is displayed.
2.  **Middle Block (Dynamics):** A box labeled **"Action minimizes prediction error."** Inside this box, the expression $F = D_q[q(\hat{s}|\mu) || p(\hat{s}|\mu)] - \ln p(\hat{s}|\mu)$ is displayed.
3.  **Bottom Block (Optimization):** A box labeled **"Perception optimizes predictions."** Inside this box, the expression $F = D_q[q(\hat{s}|\mu) || p(\hat{s}|\mu)] - \ln p(\hat{s}|\mu)$ is displayed again, followed by the optimization goal $\mu = \arg \max \text{Divergence}$.

**Connections and Flow:**
*   An arrow flows from the "Free-energy bound on surprise" block down to the "Action minimizes prediction error" block.
*   A second arrow flows from the "Action minimizes prediction error" block down to the "Perception optimizes predictions" block.

**Summary of Notations:**
The figure utilizes standard mathematical notation, including:
*   $\hat{s}$: Representing sensory states.
*   $\vec{x}$: Representing external states.
*   $F$: Denoting the Free Energy function.
*   $\mu, \theta, z, w$: Representing various parameters or noise terms within the equations.
*   $D_q[\cdot || \cdot]$: Representing a divergence measure (likely Kullback-Leibler Divergence).

128 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 3

Generative model
A probabilistic model (joint 
density) of the dependencies 
between causes and 
consequences (data), from 
which samples can be 
generated. It is usually 
specified in terms of the 
likelihood of data, given their 
causes (parameters of a model) 
and priors on the causes.

Conditional density
(Or posterior density.) The 
probability distribution of 
causes or model parameters, 
given some data; that is, a 
probabilistic mapping from 
observed data to causes.

Prior
The probability distribution or 
density of the causes of data 
that encodes beliefs about 
those causes before observing 
the data.

Bayesian surprise
A measure of salience based 
on the Kullback-Leibler 
divergence between the 
recognition density (which 
encodes posterior beliefs) and 
the prior density. It  
measures the information that 
can be recognized in the data.

Bayesian brain hypothesis
The idea that the brain uses 
internal probabilistic 
(generative) models to update 
posterior beliefs, using sensory 
information, in an 
(approximately) Bayes-optimal 
fashion.

Analysis by synthesis
Any strategy (in speech coding) 
in which the parameters of a 
signal coder are evaluated by 
decoding (synthesizing) the 
signal and comparing it with 
the original input signal.

Epistemological automata
Possibly the first theory for why 
top-down influences (mediated 
by backward connections in 
the brain) might be important 
in perception and cognition.

Empirical prior
A prior induced by hierarchical 
models; empirical priors 
provide constraints on the 
recognition density in the usual 
way but depend on the data.

a fundamental question: how do self-organizing adap-
tive systems avoid surprising states? They can do this by 
minimizing their free energy. so what does this involve?

Implications: action and perception. Agents can 
suppress free energy by changing the two things it depends 
on: they can change sensory input by acting on the world 
or they can change their recognition density by chang-
ing their internal states. This distinction maps nicely 
onto action and perception (BOX 1). one can see what this 
means in more detail by considering three mathematically 
equivalent formulations of free energy (see supplementary 
information s2 (box) for a mathematical treatment).

The first formulation expresses free energy as energy 
minus entropy. This formulation is important for three 
reasons. First, it connects the concept of free energy as 
used in information theory with concepts used in sta-
tistical thermodynamics. second, it shows that the free 
energy can be evaluated by an agent because the energy 
is the surprise about the joint occurrence of sensations 
and their perceived causes, whereas the entropy is sim-
ply that of the agent’s own recognition density. Third, it 
shows that free energy rests on a generative model of the 
world, which is expressed in terms of the probability of a 
sensation and its causes occurring together. This means 
that an agent must have an implicit generative model of 
how causes conspire to produce sensory data. It is this 
model that defines both the nature of the agent and the 
quality of the free-energy bound on surprise.

The second formulation expresses free energy as 
surprise plus a divergence term. The (perceptual) diver-
gence is just the difference between the recognition den-
sity and the conditional density (or posterior density) of the 
causes of a sensation, given the sensory signals. This con-
ditional density represents the best possible guess about 
the true causes. The difference between the two densities 
is always non-negative and free energy is therefore an 
upper bound on surprise. Thus, minimizing free energy 
by changing the recognition density (without changing 
sensory data) reduces the perceptual divergence, so that 
the recognition density becomes the conditional density 
and the free energy becomes surprise.

The third formulation expresses free energy as com-
plexity minus accuracy, using terms from the model 
comparison literature. Complexity is the difference 
between the recognition density and the prior density 
on causes; it is also known as Bayesian surprise15 and is the 
difference between the prior density — which encodes 
beliefs about the state of the world before sensory data are 
assimilated — and posterior beliefs, which are encoded 
by the recognition density. Accuracy is simply the sur-
prise about sensations that are expected under the recog-
nition density. This formulation shows that minimizing 
free energy by changing sensory data (without changing 
the recognition density) must increase the accuracy of 
an agent’s predictions. In short, the agent will selectively 
sample the sensory inputs that it expects. This is known 
as active inference16. An intuitive example of this process 
(when it is raised into consciousness) would be feeling 
our way in darkness: we anticipate what we might touch 
next and then try to confirm those expectations.

In summary, the free energy rests on a model of how 
sensory data are generated and on a recognition density 
on the model’s parameters (that is, sensory causes). Free 
energy can be reduced only by changing the recognition 
density to change conditional expectations about what is 
sampled or by changing sensory samples (that is, sensory 
input) so that they conform to expectations. In what fol-
lows, I consider these implications in light of some key 
theories about the brain.

The Bayesian brain hypothesis
The Bayesian brain hypothesis17 uses Bayesian probability 
theory to formulate perception as a constructive process 
based on internal or generative models. The underlying 
idea is that the brain has a model of the world18–22 that 
it tries to optimize using sensory inputs23–28. This idea is 
related to analysis by synthesis20 and epistemological autom-
ata19. In this view, the brain is an inference machine that 
actively predicts and explains its sensations18,22,25. Central 
to this hypothesis is a probabilistic model that can gener-
ate predictions, against which sensory samples are tested 
to update beliefs about their causes. This generative 
model is decomposed into a likelihood (the probability of 
sensory data, given their causes) and a prior (the a priori 
probability of those causes). Perception then becomes the 
process of inverting the likelihood model (mapping from 
causes to sensations) to access the posterior probability of 
the causes, given sensory data (mapping from sensations 
to causes). This inversion is the same as minimizing the 
difference between the recognition and posterior densi-
ties to suppress free energy. Indeed, the free-energy for-
mulation was developed to finesse the difficult problem 
of exact inference by converting it into an easier optimi-
zation problem11–14. This has furnished some powerful 
approximation techniques for model identification and 
comparison (for example, variational Bayes or ensemble 
learning29). There are many interesting issues that attend 
the Bayesian brain hypothesis, which can be illuminated 
by the free-energy principle; we will focus on two.

The first is the form of the generative model and 
how it manifests in the brain. one criticism of Bayesian 
treatments is that they ignore the question of how prior 
beliefs, which are necessary for inference, are formed27. 
However, this criticism dissolves with hierarchical 
generative models, in which the priors themselves are 
optimized26,28. In hierarchical models, causes in one 
level generate subordinate causes in a lower level; sen-
sory data per se are generated at the lowest level (BOX 2). 
Minimizing the free energy effectively optimizes empiri-
cal priors (that is, the probability of causes at one level, 
given those in the level above). Crucially, because empir-
ical priors are linked hierarchically, they are informed 
by sensory data, enabling the brain to optimize its prior 
expectations online. This optimization makes every level 
in the hierarchy accountable to the others, furnishing an 
internally consistent representation of sensory causes at 
multiple levels of description. Not only do hierarchical 
models have a key role in statistics (for example, ran-
dom effects and parametric empirical Bayes models30,31), 
they may also be used by the brain, given the hierarchical 
arrangement of cortical sensory areas32–34.

REVIEWS

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 129

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 4

Sensory

input
ξv

(1)

ξx

(1)

˙μv

(i) = Dμv

(i)
(i + 1)
(i)
(i)
− (∂vε )Tξ
ξv
−

˙μx

(i) = Dμx

(i)
(i)
(i)
− (∂xε )Tξ
μθij = −∂θijεTξ
μγi = ½tr(∂γi Π(ξξT − Π(μγ)))

ξv

(2)

ξv

(3)

ξx

(2)

Lower cortical areas
Higher cortical areas
Synaptic plasticity
Synaptic gain

μx

(1)

μv

(1)

μx

(2)

μv

(2)
s~(t)

Forward:
prediction
error

Backward:
predictions

ξv

(i) = Πv

(i)
= Πv

(i)
(i)
εv

(i)
(μv
– g(μ ))
(i – 1)

ξx

(i) = Πx

(i)
= Πx

(i)
(i)
εx

(i)
(Dμx – f(μ ))
(i )

The second issue is the form of the recognition den-
sity that is encoded by physical attributes of the brain, 
such as synaptic activity, efficacy and gain. In general, 
any density is encoded by its sufficient statistics (for exam-
ple, the mean and variance of a Gaussian form). The way 
the brain encodes these statistics places important con-
straints on the sorts of schemes that underlie recognition: 
they range from free-form schemes (for example, particle 
filtering26 and probabilistic population codes35–38), 
which use a vast number of sufficient statistics, to sim-
pler forms, which make stronger assumptions about 
the shape of the recognition density, so that it can be 
encoded with a small number of sufficient statistics. The 
simplest assumed form is Gaussian, which requires only 
the conditional mean or expectation — this is known 
as the Laplace assumption39, under which the free energy 
is just the difference between the model’s predictions 
and the sensations or representations that are predicted. 
Minimizing free energy then corresponds to explaining 
away prediction errors. This is known as predictive coding 
and has become a popular framework for understand-
ing neuronal message passing among different levels of 
cortical hierarchies40. In this scheme, prediction error 
units compare conditional expectations with top-down 
predictions to elaborate a prediction error. This predic-
tion error is passed forward to drive the units in the 
level above that encode conditional expectations which 
optimize top-down predictions to explain away (reduce) 
prediction error in the level below. Here, explaining 
away just means countering excitatory bottom-up 
inputs to a prediction error neuron with inhibitory syn-
aptic inputs that are driven by top-down predictions 
(see BOX 2 and REFS 41,42 for detailed discussion). The 
reciprocal exchange of bottom-up prediction errors and 
top-down predictions proceeds until prediction error 
is minimized at all levels and conditional expectations 
are optimized. This scheme has been invoked to explain 
many features of early visual responses40,43 and provides 
a plausible account of repetition suppression and mis-
match responses in electrophysiology44. FIGURE 1 pro-
vides an example of perceptual categorization that uses 
this scheme.

Message passing of this sort is consistent with func-
tional asymmetries in real cortical hierarchies45, where 
forward connections (which convey prediction errors) 
are driving and backwards connections (which model 
the nonlinear generation of sensory input) have both 
driving and modulatory characteristics46. This asym-
metrical message passing is also a characteristic feature 
of adaptive resonance theory47,48, which has formal simi-
larities to predictive coding.

In summary, the theme underlying the Bayesian brain 
and predictive coding is that the brain is an inference 
engine that is trying to optimize probabilistic representa-
tions of what caused its sensory input. This optimization 
can be finessed using a (variational free-energy) bound 
on surprise. In short, the free-energy principle entails 
the Bayesian brain hypothesis and can be implemented 
by the many schemes considered in this field. Almost 
invariably, these involve some form of message passing 
or belief propagation among brain areas or units. This

Box 2 | Hierarchical message passing in the brain

The figure details a neuronal architecture that optimizes the conditional expectations of 
causes in hierarchical models of sensory input. It shows the putative cells of origin of forward 
driving connections that convey prediction error (grey arrows) from a lower area (for 
example, the lateral geniculate nucleus) to a higher area (for example, V1), and nonlinear 
backward connections (black arrows) that construct predictions41. These predictions try to 
explain away prediction error in lower levels. In this scheme, the sources of forward and 
backward connections are superficial and deep pyramidal cells (upper and lower triangles), 
respectively, where state units are black and error units are grey. The equations represent a 
gradient descent on free energy using the generative model below. The two upper equations 
describe the formation of prediction error encoded by error units, and the two lower 
equations represent recognition dynamics, using a gradient descent on free energy.

Generative models in the brain
To evaluate free energy one needs a generative model of how the sensorium is caused. 
Such models p(s˜,ϑ) = p(s˜ | ϑ) p(ϑ) combine the likelihood p(s˜ | ϑ) of getting some data given 
their causes and the prior beliefs about these causes, p(ϑ). The brain has to explain 
complicated dynamics on continuous states with hierarchical or deep causal structure 
and may use models with the following form

Z · 
 H
Z
X
 θ
Y


U I
Z
X
 θ
\


Z · 
K H
Z
KX
K θ
KY
K
X
Ks I
Z
KX
K θ
K\
K
…
…

Here, g(i) and f(i) are continuous nonlinear functions of (hidden and causal) states, with 
parameters θ(i). The random fluctuations z(t)(i) and w(t)(i) play the part of observation 
noise at the sensory level and state noise at higher levels. Causal states v(t)(i) link 
hierarchical levels, where the output of one level provides input to the next. Hidden 
states x(t)(i) link dynamics over time and endow the model with memory.  
Gaussian assumptions about the random fluctuations specify the likelihood  
and Gaussian assumptions about state noise furnish empirical priors in terms of 
predicted motion. These assumptions are encoded by their precision (or inverse 
variance), П(i)(γ), which are functions of precision parameters γ.

recognition dynamics and prediction error
If we assume that neuronal activity encodes the conditional expectation of states, then 
recognition can be formulated as a gradient descent on free energy. Under Gaussian 
assumptions, these recognition dynamics can be expressed compactly in terms  
of precision-weighted prediction errors ξ(i) =  П(i)(ε)(i) on the causal states and motion of 
hidden states. The ensuing equations (see the figure) suggest two neuronal populations 
that exchange messages: causal or hidden-state units encoding expected states and 
error units encoding prediction error. Under hierarchical models, error units receive 
messages from the state units in the same level and the level above, whereas state units 
are driven by error units in the same level and the level below. These provide bottom-up 
messages that drive conditional expectations μ(i) towards better predictions, which 
explain away prediction error. These top-down predictions correspond to g(μ(i)) and f(μ(i)). 
This scheme suggests that the only connections that link levels are forward connections 
conveying prediction error to state units and reciprocal backward connections that 
mediate predictions. See REFS 42,130 for details. Figure is modified from REF. 42.

REVIEWS

> Figure description (generated): ## Figure Description: Hierarchical Message Passing in the Brain

This figure presents a schematic diagram illustrating the concept of hierarchical message passing within the brain, divided into two main conceptual sections: a general circuit diagram and associated mathematical equations.

### 1. Overall Layout & Structure
The figure is structured horizontally, presenting a flow diagram that moves from "Sensory input" on the left to "Backward predictions" on the right. The diagram is divided into two main conceptual layers: a top layer showing the flow of information (the circuit schematic) and a bottom section providing mathematical definitions for the components.

### 2. Visual Components & Symbols (Circuit Schematic)
The circuit schematic depicts a multi-layered network structure:

*   **Nodes/Layers:** There are distinct layers represented by nodes.
    *   The leftmost layer is labeled **"Sensory input"**.
    *   There are intermediate layers, which appear to represent different levels of abstraction or processing. These layers are connected sequentially.
    *   The rightmost layer is labeled **"Backward predictions"**.
*   **Connections/Flow:** Arrows indicate the direction of information flow. The structure suggests a feedforward progression from sensory input towards predictions, interspersed with feedback loops.
*   **Specific Nodes/Labels within the Circuit:**
    *   The initial input node is labeled $\xi^{(0)}$.
    *   Subsequent processing layers are labeled with indices, such as $\xi^{(1)}$, $\xi^{(2)}$, and $\xi^{(3)}$.
    *   The diagram shows connections between these layers, indicating how information propagates.

### 3. Mathematical Notations and Equations
The figure includes two sets of mathematical equations, positioned below the circuit schematic:

**A. Equations associated with the Circuit Flow (Top Section):**
These equations are placed near the top of the diagram, associated with the flow between layers:

*   $\xi^{(n)} = \Pi^{(n)} \circ (\mu^{(n)} - g(\mu^{(n)}))$
*   $\xi^{(n+1)} = \Pi^{(n+1)} \circ (\mu^{(n+1)} - g(\mu^{(n+1)}))$

**B. Equations defining Local and Higher Cortical Areas (Bottom Section):**
These equations are presented in a block format below the main circuit diagram, defining the dynamics within specific processing areas:

*   **Lower cortical areas:**
    $$\mu_n = D\mu^{(n)} - (\theta \circ \xi^{(n)}) \circ \xi^{(n)}$$
    $$\mu_n = D\mu^{(n)} - (\theta \circ \xi^{(n)}) \circ \xi^{(n)}$$ (Note: This equation appears duplicated in the visual representation provided.)
*   **Higher cortical areas:**
    $$\mu_n = V\sigma(\xi^{(n)}) \circ \Pi(\mu_n)$$

### 4. Contextual Annotations and Labels
The diagram is annotated with descriptive labels corresponding to the functional areas:

*   **"Sensory input"**: Located on the far left.
*   **"Lower cortical areas"**: A label pointing to a section of the lower processing layers.
*   **"Higher cortical areas"**: A label pointing to a section of the upper processing layers.
*   **"Forward: prediction error"**: A label associated with the initial flow direction, indicating the transmission of prediction errors.
*   **"Backward: predictions"**: A label associated with the flow returning towards earlier layers, indicating the transmission of predictions.

In summary, the figure visually models a hierarchical processing system where sensory input flows forward through multiple cortical layers ($\xi^{(0)} \to \xi^{(1)} \to \dots$), generating predictions, while the system dynamics are governed by specific mathematical relationships defining local and higher cortical processing ($\mu_n$).

130 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 5

a  Perceptual inference

b  Perceptual categorization

c

0
0.2
0.4
0.6
0.8
1
–20

–10

0

10

20

30

40

50

5,000

4,000

3,000

2,000
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0

a

b

c

Time (s)

Time (s)

Estimated causes

Frequency (Hz)

µv1

µv1

10
15
20
25
30
35
1

1.5

2

2.5

3

3.5

a
b

c

v2

v1

Song a
Song b
Song c

v = v2

v1

Vocal centre
Syrinx
Sonogram

˙x  = f(x, v) = v1x1 − 2x3x1 − x2

18x2 − 18x1

2x1x2 − v2x3

allows us to connect the free-energy principle to another 
principled approach to sensory processing, namely 
information theory.

The principle of efficient coding
The principle of efficient coding suggests that the brain 
optimizes the mutual information (that is, the mutual 
predictability) between the sensorium and its internal 
representation, under constraints on the efficiency of 
those representations. This line of thinking was articu-
lated by Barlow49 in terms of a redundancy reduction 
principle (or principle of efficient coding) and formal-
ized later in terms of the infomax principle50. It has been 
applied in machine learning51, leading to methods 
like independent component analysis52, and in neuro-
biology, contributing to an understanding of the nature 
of neuronal responses53–56. This principle is extremely 
effective in predicting the empirical characteristics of 
classical receptive fields53 and provides a principled 
explanation for sparse coding55 and the segregation of 
processing streams in visual hierarchies57. It has been 
extended to cover dynamics and motion trajectories58,59 
and even used to infer the metabolic constraints on neu-
ronal processing60.

At its simplest, the infomax principle says that 
neuronal activity should encode sensory information in 
an efficient and parsimonious fashion. It considers the 
mapping between one set of variables (sensory states) 
and another (variables representing those states). At 
first glance, this seems to preclude a probabilistic repre-
sentation, because this would involve mapping between 
sensory states and a probability density. However, the 
infomax principle can be applied to the sufficient sta-
tistics of a recognition density. In this context, the info-
max principle becomes a special case of the free-energy 
principle, which arises when we ignore uncertainty 
in probabilistic representations (and when there is no 
action); see supplementary information s3 (box) for 
mathematical details). This is easy to see by noting that 
sensory signals are generated by causes. This means that it 
is sufficient to represent the causes to predict these 
signals. More formally, the infomax principle can be 
understood in terms of the decomposition of free energy 
into complexity and accuracy: mutual information is 
optimized when conditional expectations maximize 
accuracy (or minimize prediction error), and efficiency 
is assured by minimizing complexity. This ensures that 
no excessive parameters are applied in the generative 
model and leads to a parsimonious representation of 
sensory data that conforms to prior constraints on their 
causes. Interestingly, advanced model-optimization 
techniques use free-energy optimization to eliminate 
redundant model parameters61, suggesting that free-
energy optimization might provide a nice explanation 
for the synaptic pruning and homeostasis that take place 
in the brain during neurodevelopment62 and sleep63.

The infomax principle pertains to a forward mapping 
from sensory input to representations. How does this 
square with optimizing generative models, which map 
from causes to sensory inputs? These perspectives can be 
reconciled by noting that all recognition schemes based

Figure 1 | Birdsongs and perceptual categorization. a | The generative model of 
birdsong used in this simulation comprises a Lorenz attractor with two control parameters 
(or causal states) (v1,v2), which, in turn, delivers two control parameters (not shown) to a 
synthetic syrinx to produce ‘chirps’ that were modulated in amplitude and frequency (an 
example is shown as a sonogram). The chirps were then presented as a stimulus to a 
synthetic bird to see whether it could infer the underlying causal states and thereby 
categorize the song. This entails minimizing free energy by changing the internal 
representation (μv1,μv2) of the control parameters. Examples of this perceptual inference or 
categorization are shown below. b | Three simulated songs are shown in sonogram format. 
Each comprises a series of chirps, the frequency and number of which fall progressively 
from song a to song c, as a causal state (known as the Raleigh number; v1 in part a) is 
decreased. c | The graph on the left depicts the conditional expectations (μv1,μv2) of the 
causal states, shown as a function of peristimulus time for the three songs. It shows that 
the causes are identified after around 600 ms with high conditional precision (90% 
confidence intervals are shown in grey). The graph on the right shows the conditional 
density on the causes shortly before the end of the peristimulus time (that is, the dotted 
line in the left panel). The blue dots correspond to conditional expectations and the grey 
areas correspond to the 90% conditional confidence regions. Note that these encompass 
the true values (red dots) of (v1,v2) that were used to generate the songs. These results 
illustrate the nature of perceptual categorization under the inference scheme in BOX 2: 
here, recognition corresponds to mapping from a continuously changing and chaotic 
sensory input to a fixed point in perceptual space. Figure is reproduced, with permission, 
from REF. 130 © (2009) Elsevier.

> Figure caption (from PDF text): Figure 1 | Birdsongs and perceptual categorization. a | The generative model of 
birdsong used in this simulation comprises a Lorenz attractor with two control parameters 
(or causal states) (v1,v2), which, in turn, delivers two control parameters (not shown) to a 
synthetic syrinx to produce ‘chirps’ that were modulated in amplitude and frequency (an 
example is shown as a sonogram). The chirps were then presented as a stimulus to a 
synthetic bird to see whether it could infer the underlying causal states and thereby 
categorize the song. This entails minimizing free energy by changing the internal 
representation (μv1,μv2) of the control parameters. Examples of this perceptual inference or 
categorization are shown below. b | Three simulated songs are shown in sonogram format. 
Each comprises a series of chirps, the frequency and number of which fall progressively 
from song a to song c, as a causal state (known as the Raleigh number; v1 in part a) is 
decreased. c | The graph on the left depicts the conditional expectations (μv1,μv2) of the 
causal states, shown as a function of peristimulus time for the three songs. It shows that 
the causes are identified after around 600 ms with high conditional precision (90% 
confidence intervals are shown in grey). The graph on the right shows the conditional 
density on the causes shortly before the end of the peristimulus time (that is, the dotted 
line in the left panel). The blue dots correspond to conditional expectations and the grey 
areas correspond to the 90% conditional confidence regions. Note that these encompass 
the true values (red dots) of (v1,v2) that were used to generate the songs. These results 
illustrate the nature of perceptual categorization under the inference scheme in BOX 2: 
here, recognition corresponds to mapping from a continuously changing and chaotic 
sensory input to a fixed point in perceptual space. Figure is reproduced, with permission, 
from REF. 130 © (2009) Elsevier.
> Figure description (generated): ## Figure Description: Birdsongs and Perceptual Categorization

This figure presents a set of plots illustrating the perceptual inference of underlying causal states from simulated birdsong stimuli. The overall structure consists of a single, large graph area containing multiple overlaid time-series plots and annotations.

### 1. Overall Layout & Structure
The figure is dominated by a single, large two-dimensional plot area. The vertical axis represents the value of the causal states ($\mu_{v1}$ and $\mu_{v2}$), while the horizontal axis represents time (peristimulus time). The plot displays multiple colored lines representing conditional expectations ($\mu_{v1}, \mu_{v2}$) for three different simulated songs (labeled 'a', 'b', and 'c').

### 2. Visual Components & Symbols
*   **Axes:** The Y-axis ranges from -20 to 50, labeled with numerical ticks. The X-axis ranges from 0 to 1 (representing normalized time).
*   **Curves:** There are multiple continuous lines plotted, representing the conditional expectations ($\mu_{v1}$ and $\mu_{v2}$).
    *   The upper set of curves (labeled 'a', 'b') represents $\mu_{v1}$.
    *   The lower set of curves (labeled 'c') represents $\mu_{v2}$.
    *   Each curve is accompanied by a shaded grey area, which represents the 90% conditional confidence interval.
*   **Annotations:**
    *   The labels $\mu_{v1}$ and $\mu_{v2}$ are positioned near the respective sets of curves to identify which state is being plotted.
    *   A vertical dashed line is present near $x=0.9$, marking a specific point in time (shortly before the end of peristimulus time).
    *   The caption mentions "blue dots" corresponding to conditional expectations and "red dots" representing the true values, although these specific markers are not explicitly visible or labeled in the provided image crop beyond the general description.

### 3. Labels, Keys & Legends
*   **Y-Axis Labeling:** Numerical ticks are present from 0 to 50, with major markings at intervals of 10.
*   **X-Axis Labeling:** Numerical ticks are present from 0 to 1.
*   **State Labels:** $\mu_{v1}$ and $\mu_{v2}$ are used to label the vertical position of the respective sets of curves.
*   **Song Labels:** The songs are identified by letters 'a', 'b', and 'c' associated with the specific trajectories.

### 4. Data Trends & Details
The plot shows distinct trends for the three songs (a, b, c) across both causal states ($\mu_{v1}$ and $\mu_{v2}$) over time:

*   **$\mu_{v1}$ (Upper Curves):**
    *   Song 'a' shows the highest trajectory, remaining consistently high (around 30-35).
    *   Song 'b' shows an intermediate trajectory, hovering around 25-30.
    *   Song 'c' shows the lowest trajectory among the three, around 15-20.
    *   All three trajectories exhibit a relatively stable level after an initial transient period (around $x=0.2$).

*   **$\mu_{v2}$ (Lower Curves):**
    *   Song 'a' shows a trajectory that starts near zero, rises sharply to a peak (around 10-15) around $x=0.3$, and then gradually decreases, stabilizing near zero or slightly negative by the end of the time course.
    *   Song 'b' shows a trajectory that starts near zero, rises less steeply than 'a', and remains generally lower than song 'a's trajectory.
    *   Song 'c' shows a trajectory that remains close to zero for most of the duration, with some minor fluctuations.

*   **Confidence Intervals:** The grey shaded areas show that the conditional expectations are estimated with high precision, as indicated by the caption (90% confidence intervals).

### 5. Contextual Caption Integration
The caption clarifies that the plot depicts the **conditional expectations ($\mu_{v1}, \mu_{v2}$) of the causal states** as a function of peristimulus time for the three songs (a, b, c). It confirms that these results illustrate perceptual categorization: "recognition corresponds to mapping from a continuously changing and chaotic sensory input to a fixed point in perceptual space." The vertical dashed line marks the time point where the conditional density on the causes is shown in a separate panel (not fully visible here).

> Figure caption (from PDF text): Figure 1 | Birdsongs and perceptual categorization. a | The generative model of 
birdsong used in this simulation comprises a Lorenz attractor with two control parameters 
(or causal states) (v1,v2), which, in turn, delivers two control parameters (not shown) to a 
synthetic syrinx to produce ‘chirps’ that were modulated in amplitude and frequency (an 
example is shown as a sonogram). The chirps were then presented as a stimulus to a 
synthetic bird to see whether it could infer the underlying causal states and thereby 
categorize the song. This entails minimizing free energy by changing the internal 
representation (μv1,μv2) of the control parameters. Examples of this perceptual inference or 
categorization are shown below. b | Three simulated songs are shown in sonogram format. 
Each comprises a series of chirps, the frequency and number of which fall progressively 
from song a to song c, as a causal state (known as the Raleigh number; v1 in part a) is 
decreased. c | The graph on the left depicts the conditional expectations (μv1,μv2) of the 
causal states, shown as a function of peristimulus time for the three songs. It shows that 
the causes are identified after around 600 ms with high conditional precision (90% 
confidence intervals are shown in grey). The graph on the right shows the conditional 
density on the causes shortly before the end of the peristimulus time (that is, the dotted 
line in the left panel). The blue dots correspond to conditional expectations and the grey 
areas correspond to the 90% conditional confidence regions. Note that these encompass 
the true values (red dots) of (v1,v2) that were used to generate the songs. These results 
illustrate the nature of perceptual categorization under the inference scheme in BOX 2: 
here, recognition corresponds to mapping from a continuously changing and chaotic 
sensory input to a fixed point in perceptual space. Figure is reproduced, with permission, 
from REF. 130 © (2009) Elsevier.
> Figure description (generated): This figure presents a scatter plot illustrating the conditional expectations of causal states ($\mu_{v1}, \mu_{v2}$) for three different simulated songs (a, b, and c).

**1. Overall Layout & Structure:**
The figure is a single 2D scatter plot with two axes, representing the conditional expectations of the causal states. The data is organized into three distinct clusters or regions labeled 'a', 'b', and 'c'.

**2. Visual Components & Symbols:**
*   **Axes:** The horizontal axis (x-axis) ranges from approximately 10 to 35, and the vertical axis (y-axis) ranges from 1.0 to 3.5.
*   **Data Points:** There are several types of markers used:
    *   **Red Dots:** These represent the "true values" of $(v1, v2)$ used to generate the songs.
    *   **Blue Dots:** These represent the "conditional expectations" ($\mu_{v1}, \mu_{v2}$).
    *   **Grey Ellipses/Regions:** These represent the 90% conditional confidence regions surrounding the data points.
*   **Spatial Arrangement:** The three songs (a, b, and c) are positioned along the x-axis in decreasing order of their associated causal state values (as implied by the caption).
    *   **Region 'c' (Left):** This region is characterized by a large, elongated grey ellipse. It contains two markers: one red dot and one blue dot, both situated near the center of the ellipse.
    *   **Region 'b' (Middle):** This region is characterized by a smaller, more compact grey ellipse. It contains two markers: one red dot and one blue dot.
    *   **Region 'a' (Right):** This region is characterized by a narrow, vertically elongated grey ellipse. It contains two markers: one red dot and one blue dot.

**3. Labels, Keys & Legends:**
*   **Axes Labels:** No explicit axis labels are provided in the visible portion of the plot, but based on the caption, the axes represent the causal states $(v1, v2)$.
*   **Annotations:** The labels 'a', 'b', and 'c' are placed adjacent to their respective data clusters, identifying the three songs.
*   **Color Coding:** Red dots denote true values; blue dots denote conditional expectations; grey areas denote 90% confidence intervals.

**4. Data Trends & Details:**
*   **X-Axis Trend (Causal State):** The songs are ordered such that the causal state associated with 'c' is at the lowest x-value (around 14), followed by 'b' (around 25), and finally 'a' (around 30).
*   **Y-Axis Trend (Causal State):** The vertical positions of the markers generally show a slight decrease from region 'c' to region 'a', although the primary variation is along the x-axis.
*   **Confidence Intervals:** The grey ellipses show that for each song, the true values (red dots) are encompassed within their respective 90% conditional confidence regions.

**5. Contextual Caption Integration:**
The caption clarifies that the graph depicts the conditional expectations ($\mu_{v1}, \mu_{v2}$) of the causal states as a function of peristimulus time for the three songs. The blue dots are the conditional expectations, and the grey areas are the 90% conditional confidence regions. The red dots represent the true values of $(v1, v2)$ used to generate the songs. The arrangement illustrates that recognition corresponds to mapping from a continuously changing and chaotic sensory input (the song) to a fixed point in perceptual space.

REVIEWS

> Figure description (generated): This figure is divided into two main conceptual sections: "Vocal centre" on the left and "Syrinx" on the right, connected by an input vector notation.

### 1. Overall Layout & Structure
The figure is structured horizontally, presenting a dynamic system model (Vocal centre) alongside a biological structure diagram (Syrinx). A mathematical equation block is positioned below the main visual components.

### 2. Visual Components & Symbols

**A. Vocal Centre (Left Panel):**
*   This section displays a complex, swirling pattern resembling a strange attractor or phase space trajectory plot.
*   The background is a gradient, transitioning from dark grey/black on the left to lighter tones towards the center-right.
*   The pattern itself consists of numerous densely packed, small, dark dots forming intricate, nested spirals. This visualization suggests a chaotic or complex dynamical system.

**B. Connection/Input Notation:**
*   An arrow points from the "Vocal centre" visualization towards a notation block: $v = [V_1, V_2]$. This indicates that the state of the vocal centre is represented by a vector $v$ with two components, $V_1$ and $V_2$.

**C. Syrinx (Right Panel):**
*   This panel illustrates a biological structure, labeled "Syrinx." It is depicted as an anatomical cross-section or schematic of the syrinx structure.
*   The main body is colored light pink/salmon, forming a bifurcated or Y-shaped structure.
*   Along the inner walls of this structure, there are representations of cells or tissue layers:
    *   These structures are shown as elongated ovals/circles embedded within the pink tissue.
    *   The cells appear to be lined along the inner lumen walls, colored light green/teal.
*   An arrow originates from the general vicinity of the syrinx structure and points towards the right edge of the figure, suggesting an output or functional connection.

**D. Mathematical Block (Bottom):**
*   A large, rectangular block with a light orange/tan background contains mathematical expressions.

### 3. Labels, Keys & Legends
*   **Titles:** "Vocal centre" and "Syrinx."
*   **Variables/Notation:** $v = [V_1, V_2]$.
*   **Mathematical Equations (within the orange block):**
    $$\dot{x} = f(x, v) = \begin{bmatrix} 18x_2 - 18x_1 \\ v_1 x_1 - 2x_3 x_1 - x_2 \\ 2x_1 x_2 - v_2 x_3 \end{bmatrix}$$

### 4. Data Trends & Details
*   **Vocal Centre Plot:** The plot shows a clear trajectory converging into a central, complex spiral structure, characteristic of chaotic dynamics.
*   **Syrinx Diagram:** The diagram is structural; no quantitative data trends are present, but it illustrates the physical arrangement of tissue (pink) and cellular elements (green/teal).

### 5. Contextual Caption Integration
The figure visually links the abstract dynamical system model ("Vocal centre") to a specific biological structure ("Syrinx"). The mathematical block provides the governing equations ($\dot{x} = f(x, v)$) that likely describe the dynamics of the system, where $v$ (the input vector from the vocal centre) influences the state variables $x_1, x_2, x_3$ within the system dynamics.

> Figure description (generated): ## Figure Description

This figure, titled "Song a," presents a time-frequency representation or spectrogram of an auditory signal.

**1. Overall Layout & Structure:**
The figure consists of a single plot occupying the majority of the frame, set against a black background. The visualization style is that of a 2D plot where intensity (likely representing amplitude or energy) is mapped across time and frequency.

**2. Visual Components & Symbols:**
The plot area displays several distinct, thin, vertical or near-vertical streaks of light color (appearing reddish/orange against the black background). These streaks represent transient acoustic events.

*   **Left Side (Time $\approx 0.1$ to $0.2$):** There is a cluster of very bright, closely spaced vertical streaks located near the left edge of the plot.
*   **Middle Section (Time $\approx 0.3$ to $0.9$):** Several fainter, more spread-out vertical streaks are visible across the central and right portions of the plot. These appear to be slightly more dispersed in frequency than the initial cluster.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Song a" centered above the plot area.
*   **Y-Axis Labeling:** The vertical axis (y-axis) is labeled with numerical markers: "00", "00", and "00". These likely represent frequency bins or normalized frequency units, though the specific unit is not provided.
*   **X-Axis Labeling:** The horizontal axis (x-axis) is labeled with numerical markers: "0.0", "0.2", "0.4", "0.6", "0.8", and "1.0". These represent time, likely normalized from 0.0 to 1.0.

**4. Data Trends & Details:**
The plot shows the temporal evolution of acoustic energy. The most intense activity occurs early in the sequence (around $t=0.1$ to $t=0.2$). Following this initial burst, the energy events become less intense and more temporally spread out across the remainder of the time axis ($t=0.3$ to $t=1.0$). The streaks generally maintain a high vertical orientation, suggesting the energy is concentrated in specific frequency bands.

> Figure description (generated): ## Figure Description

This figure presents a single plot titled "Song b," which appears to be a time-series visualization, likely representing an auditory or neural signal over time.

**1. Overall Layout & Structure:**
The figure consists of a single plot displayed against a black background, with axes labeled below the plotting area. The visualization style is that of an amplitude or energy plot over time, characterized by vertical streaks of activity against a dark background.

**2. Visual Components & Symbols:**
*   **Background:** The plot area is predominantly black, indicating a low baseline or silence.
*   **Signal Traces:** Several distinct vertical streaks of reddish-brown activity are visible across the time axis.
    *   The first trace is located near $t=0.2$ seconds and appears relatively tall and distinct.
    *   Subsequent traces appear sequentially, spaced out in time: one around $t=0.4$ s, another near $t=0.5$ s, a third around $t=0.6$ s, and subsequent traces continuing towards the right edge of the plot up to $t=1.0$ s, though they appear progressively shorter or less intense than the initial trace.
*   **Axes:** The horizontal axis (x-axis) represents Time, and the vertical axis (y-axis) is implied by the height of the traces but lacks an explicit label in the visible area.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Song b" centered above the plot area.
*   **X-Axis Label:** The horizontal axis is labeled "Time (s)".
*   **Tick Marks & Values:** Major tick marks are present along the x-axis, labeled with values: $0.0$, $0.2$, $0.4$, $0.6$, $0.8$, and $1.0$.

**4. Data Trends & Details:**
The plot displays a sequence of discrete, transient events occurring over the one-second duration. The activity appears to be rhythmic or patterned:
*   The initial event at $t \approx 0.2$ s is the most prominent in terms of vertical extent.
*   The subsequent events are temporally spaced, suggesting a periodic or patterned occurrence within the "Song b" context.
*   The intensity/amplitude of these events appears to decrease slightly as time progresses from $t=0.2$ s towards $t=1.0$ s, although the overall pattern is one of repeated pulses.

> Figure description (generated): ## Figure Description

This figure, titled "Song c," presents a single-panel visualization that appears to be an auditory or temporal spectrogram/waveform representation, likely related to acoustic analysis of a song.

**1. Overall Layout & Structure:**
The figure consists of one primary plot area set against a black background. The visualization style is that of a time-domain or frequency-time plot, characterized by vertical streaks of color against a dark field.

**2. Visual Components & Symbols:**
The plot spans horizontally from $x=0.0$ to $x=1.0$, representing a normalized time axis. The vertical dimension is not explicitly labeled but represents the amplitude or frequency content of the signal.

Within this plot area, there are three distinct, vertically oriented, reddish-brown streaks or transients. These features appear to be transient bursts of energy:
*   **First Transient:** Located approximately between $x=0.35$ and $x=0.45$.
*   **Second Transient:** Located approximately between $x=0.58$ and $x=0.68$.
*   **Third Transient:** Located approximately between $x=0.75$ and $x=0.85$.

These transients are relatively narrow in the time domain but exhibit some vertical extent, suggesting a specific frequency content or amplitude modulation during these brief periods.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Song c" positioned above the plot area.
*   **X-Axis Labeling:** The horizontal axis is labeled with numerical markers: $0.0, 0.2, 0.4, 0.6, 0.8, 1.0$. These likely represent normalized time (e.g., seconds or a fraction of the total song duration).
*   **Y-Axis Labeling:** No explicit y-axis label is present, but the vertical extent represents the signal's magnitude or frequency.

**4. Data Trends & Details:**
The data shows three discrete, temporally separated events (the transients) occurring sequentially across the normalized time axis. The energy of these three events appears relatively consistent in shape and intensity, although precise quantitative measurements are not provided without a scale on the vertical axis. The background is uniformly black, indicating silence or zero signal energy outside these three events.

> Figure description (generated): This figure is composed of two distinct visual panels stacked vertically, presented without explicit panel lettering (e.g., A or B).

**Overall Layout & Structure:**
The figure is divided into two main sections. The upper section displays a technical image labeled "Sonogram," while the lower section displays a high-resolution photograph of wildlife.

**Visual Components & Symbols:**

*   **Upper Panel (Sonogram):** This panel contains a dark, nearly black background. Superimposed on this background are several thin, vertical, light-colored (appearing white or pale pinkish) lines. These lines are arranged roughly horizontally across the image frame, suggesting a time-series or spectral representation. An arrow points from the left margin toward this upper panel, indicating a connection or focus point.
*   **Lower Panel (Photograph):** This panel is a color photograph featuring a small bird perched on a branch covered in light-colored, drooping foliage (possibly catkins). The background is blurred and muted, suggesting a natural outdoor setting.

**Labels, Keys & Legends:**
*   The title above the upper panel reads: "**Sonogram**".
*   There is a large, dark arrow pointing from the left side of the figure toward the upper "Sonogram" panel.

**Data Trends & Details:**
*   The Sonogram shows multiple distinct, parallel vertical lines of varying heights and slight variations in their horizontal positioning across the frame.
*   The photograph displays a detailed depiction of a small, yellow-colored bird situated amidst green and pale foliage.

**Contextual Caption Integration:**
No specific contextual caption text was provided to integrate with the visual elements, so all descriptions are based solely on the visible components.

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 131

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 6

Sufficient statistics
Quantities that are sufficient to 
parameterize a probability 
density (for example, mean and 
covariance of a Gaussian 
density).

Laplace assumption
(Or Laplace approximation or 
method.) A saddle-point 
approximation of the integral 
of an exponential function, that 
uses a second-order Taylor 
expansion. When the function 
is a probability density, the 
implicit assumption is that  
the density is approximately 
Gaussian.

Predictive coding
A tool used in signal processing 
for representing a signal using 
a linear predictive (generative) 
model. It is a powerful speech 
analysis technique and was 
first considered in vision to 
explain lateral interactions in 
the retina.

Infomax
An optimization principle for 
neural networks (or functions) 
that map inputs to outputs. It 
says that the mapping should 
maximize the Shannon mutual 
information between the inputs 
and outputs, subject to 
constraints and/or noise 
processes.

Stochastic
Governed by random effects.

Biased competition
An attentional effect mediated 
by competitive interactions 
among neurons representing 
visual stimuli; these 
interactions can be biased in 
favour of behaviourally relevant 
stimuli by both spatial and 
non-spatial and both 
bottom-up and top-down 
processes.

on infomax can be cast as optimizing the parameters of a 
generative model64. For example, in sparse coding mod-
els55, the implicit priors posit independent causes that 
are sampled from a heavy-tailed or sparse distribution42. 
The fact that these models predict empirically observed 
receptive fields so well suggests that we are endowed 
with (or acquire) prior expectations that the causes of 
our sensations are largely independent and sparse.

In summary, the principle of efficient coding says 
that the brain should optimize the mutual information 
between its sensory signals and some parsimonious 
neuronal representations. This is the same as optimizing 
the parameters of a generative model to maximize the 
accuracy of predictions, under complexity constraints. 
Both are mandated by the free-energy principle, which 
can be regarded as a probabilistic generalization of the 
infomax principle. We now turn to more biologically 
inspired ideas about brain function that focus on neu-
ronal dynamics and plasticity. This takes us deeper into 
neurobiological mechanisms and the implementation of 
the theoretical principles outlined above.

The cell assembly and correlation theory
The cell assembly theory was proposed by Hebb65 and 
entails Hebbian — or associative — plasticity, which is a 
cornerstone of use-dependent or experience-dependent 
plasticity66, the correlation theory of von de Malsburg67,68

and other formal refinements to Hebbian plasticity 
per se69. The cell assembly theory posits that groups of 
interconnected neurons are formed through a strength-
ening of synaptic connections that depends on corre-
lated pre- and postsynaptic activity; that is, ‘cells that fire 
together wire together’. This enables the brain to distil 
statistical regularities from the sensorium. The correla-
tion theory considers the selective enabling of synaptic 
efficacy and its plasticity (also known as metaplastic-
ity70) by fast synchronous activity induced by different 
perceptual attributes of the same object (for example, a 
red bus in motion). This resolves a putative deficiency 
of classical plasticity, which cannot ascribe a presynaptic 
input to a particular cause (for example, redness) in the 
world67. The correlation theory underpins theoretical 
treatments of synchronized brain activity and its role in 
associating or binding attributes to specific objects or 
causes68,71. Another important field that rests on associa-
tive plasticity is the use of attractor networks as models 
of memory formation and retrieval72–74. so how do corre-
lations and associative plasticity figure in the free-energy 
formulation?

Hitherto, we have considered only inference on states 
of the world that cause sensory signals, whereby condi-
tional expectations about states are encoded by synaptic 
activity. However, the causes covered by the recognition 
density are not restricted to time-varying states (for 
example, the motion of an object in the visual field): 
they also include time-invariant regularities that endow 
the world with causal structure (for example, objects 
fall with constant acceleration). These regularities are 
parameters of the generative model and have to be 
inferred by the brain — in other words, the conditional 
expectations of these parameters that may be encoded

by synaptic efficacy (these are μθ in BOX 2) have to be 
optimized. This corresponds to optimizing connection 
strengths in the brain — that is, plasticity that under-
lines learning. so what form would this learning take? It 
transpires that a gradient descent on free energy (that is, 
changing connections to reduce free energy) is formally 
identical to Hebbian plasticity28,42 (BOX 2). This is because 
the parameters of the generative model determine how 
expected states (synaptic activity) are mixed to form pre-
dictions. Put simply, when the presynaptic predictions 
and postsynaptic prediction errors are highly correlated, 
the connection strength increases, so that predictions 
can suppress prediction errors more efficiently.

In short, the formation of cell assemblies reflects the 
encoding of causal regularities. This is just a restate-
ment of cell assembly theory in the context of a specific 
implementation (predictive coding) of the free-energy 
principle. It should be acknowledged that the learning 
rule in predictive coding is really a delta rule, which 
rests on Hebbian mechanisms; however, Hebb’s wider 
notions of cell assemblies were formulated from a non-
statistical perspective. Modern reformulations suggest 
that both inference on states (that is, perception) and 
inference on parameters (that is, learning) minimize 
free energy (that is, minimize prediction error) and 
serve to bound surprising exchanges with the world. so 
what about synchronization and the selective enabling 
of synapses?

Biased competition and attention
Causal regularities encoded by synaptic efficacy 
control the deterministic evolution of states in the world. 
However, stochastic (that is, random) fluctuations in 
these states play an important part in generating sen-
sory data. Their amplitude is usually represented as pre-
cision (or inverse variance), which encodes the reliability 
of prediction errors. Precision is important, especially 
in hierarchical schemes, because it controls the relative 
influence of bottom-up prediction errors and top-down 
predictions. so how is precision encoded in the brain? 
In predictive coding, precision modulates the amplitude 
of prediction errors (these are μγ in BOX 2), so that pre-
diction errors with high precision have a greater impact 
on units that encode conditional expectations. This 
means that precision corresponds to the synaptic gain of 
prediction error units. The most obvious candidates for 
controlling gain (and implicitly encoding precision) are 
classical neuromodulators like dopamine and acetylcho-
line, which provides a nice link to theories of attention 
and uncertainty75–77. Another candidate is fast synchro-
nized presynaptic input that lowers effective postsynaptic 
membrane time constants and increases synchronous 
gain78. This fits comfortably with the correlation theory 
and speaks to recent ideas about the role of synchronous 
activity in mediating attentional gain79,80.

In summary, the optimization of expected precision 
in terms of synaptic gain links attention to synaptic gain 
and synchronization. This link is central to theories of 
attentional gain and biased competition80–85, particularly 
in the context of neuromodulation86,87. The theories 
considered so far have dealt only with perception.

REVIEWS

132 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 7

Reentrant signalling
Reciprocal message passing 
among neuronal groups.

Reinforcement learning
An area of machine learning 
concerned with how an agent 
maximizes long-term reward. 
Reinforcement learning 
algorithms attempt to find a 
policy that maps states of the 
world to actions performed by 
the agent.

Optimal control theory
An optimization method 
(based on the calculus of 
variations) for deriving an 
optimal control law in a 
dynamical system. A control 
problem includes a cost 
function that is a function of 
state and control variables.

Bellman equation
(Or dynamic programming 
equation.) Named after 
Richard Bellman, it is a 
necessary condition for 
optimality associated with 
dynamic programming in 
optimal control theory.

However, from the point of view of the free-energy 
principle, perception just makes free energy a good 
proxy for surprise. To actually reduce surprise we need 
to act. In the next section, we retain a focus on cell 
assemblies but move to the selection and reinforcement 
of stimulus–response links.

Neural Darwinism and value learning
In the theory of neuronal group selection88, the emergence 
of neuronal assemblies is considered in the light of selec-
tive pressure. The theory has four elements: epigenetic 
mechanisms create a primary repertoire of neuronal 
connections, which are refined by experience-dependent 
plasticity to produce a secondary repertoire of neuro-
nal groups. These are selected and maintained through 
reentrant signalling among neuronal groups. As in cell 
assembly theory, plasticity rests on correlated pre- and 
postsynaptic activity, but here it is modulated by value. 
value is signalled by ascending neuromodulatory trans-
mitter systems and controls which neuronal groups 
are selected and which are not. The beauty of neural 
Darwinism is that it nests distinct selective processes 
within each other. In other words, it eschews a single unit 
of selection and exploits the notion of meta-selection 
(the selection of selective mechanisms; for example, see

REF. 89). In this context, (neuronal) value confers evolu-
tionary value (that is, adaptive fitness) by selecting neu-
ronal groups that meditate adaptive stimulus–stimulus 
associations and stimulus–response links. The capacity 
of value to do this is assured by natural selection, in the 
sense that neuronal value systems are themselves subject 
to selective pressure.

This theory, particularly value-dependent learning90, 
has deep connections with reinforcement learning and 
related approaches in engineering (see below), such as 
dynamic programming and temporal difference mod-
els91,92. This is because neuronal value systems reinforce 
connections to themselves, thereby enabling the brain 
to label a sensory state as valuable if, and only if, it leads to 
another valuable state. This ensures that agents move 
through a succession of states that have acquired value to 
access states (rewards) with genetically specified innate 
value. In short, the brain maximizes value, which may be 
reflected in the discharge of value systems (for example, 
dopaminergic systems92–96). so how does this relate to 
the optimization of free energy?

The answer is simple: value is inversely proportional 
to surprise, in the sense that the probability of a pheno-
type being in a particular state increases with the value 
of that state. Furthermore, the evolutionary value of 
a phenotype is the negative surprise averaged over all 
the states it experiences, which is simply its negative 
entropy. Indeed, the whole point of minimizing free 
energy (and implicitly entropy) is to ensure that agents 
spend most of their time in a small number of valuable 
states. This means that free energy is the complement of 
value, and its long-term average is the complement of 
adaptive fitness (also known as free fitness in evolution-
ary biology97). But how do agents know what is valu-
able? In other words, how does one generation tell the 
next which states have value (that is, are unsurprising)?

value or surprise is determined by the form of an agent’s 
generative model and its implicit priors — these specify 
the value of sensory states and, crucially, are heritable 
through genetic and epigenetic mechanisms. This means 
that prior expectations (that is, the primary repertoire) 
can prescribe a small number of attractive states with 
innate value. In turn, this enables natural selection to 
optimize prior expectations and ensure they are con-
sistent with the agent’s phenotype. Put simply, valuable 
states are just the states that the agent expects to fre-
quent. These expectations are constrained by the form of 
its generative model, which is specified genetically and 
fulfilled behaviourally, under active inference.

It is important to appreciate that prior expectations 
include not just what will be sampled from the world but 
also how the world is sampled. This means that natural 
selection may equip agents with the prior expectation 
that they will explore their environment until states 
with innate value are encountered. We will look at this 
more closely in the next section, where priors on motion 
through state space are cast in terms of policies in 
reinforcement learning.

Both neural Darwinism and the free-energy principle 
try to understand somatic changes in an individual in 
the context of evolution: neural Darwinism appeals to 
selective processes, whereas the free energy formulation 
considers the optimization of ensemble or population 
dynamics in terms of entropy and surprise. The key 
theme that emerges here is that (heritable) prior expecta-
tions can label things as innately valuable (unsurprising); 
but how can simply labelling states engender adaptive 
behaviour? In the next section, we return to reinforce-
ment learning and related formulations of action that try 
to explain adaptive behaviour purely in terms of labels 
or cost functions.

Optimal control theory and game theory
value is central to theories of brain function that are 
based on reinforcement learning and optimum con-
trol. The basic notion that underpins these treatments 
is that the brain optimizes value, which is expected 
reward or utility (or its complement — expected loss 
or cost). This is seen in behavioural psychology as rein-
forcement learning98, in computational neuroscience 
and machine learning as variants of dynamic program-
ming such as temporal difference learning99–101, and in 
economics as expected utility theory102. The notion of 
an expected reward or cost is crucial here; this is the 
cost expected over future states, given a particular policy 
that prescribes action or choices. A policy specifies the 
states to which an agent will move from any given state 
(‘motion through state space in continuous time’). This 
policy has to access sparse rewarding states using a cost 
function, which only labels states as costly or not. The 
problem of how the policy is optimized is formalized 
in optimal control theory as the Bellman equation and its 
variants99 (see supplementary information s4 (box)), 
which express value as a function of the optimal policy 
and a cost function. If one can solve the Bellman equa-
tion, one can associate each sensory state with a value 
and optimize the policy by ensuring that the next state

REVIEWS

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 133

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 8

svisual =
+ wvisual
J
V

sprop =
+ wprop
x2

x1

V = (v1, v2, v3)

J = J1 + J2 = (j1, j2)

Movement
trajectory

(0, 0)

x1

J1

J2
x2

Jointed arm
a

ξv

(1)

ξv

(1)

ξx

(1)
ξv

(2)

μx

(1)

μv

(1)

Action

Motor 
signals

Predictions
Prediction errors

˙a = −∂aεTξ

Optimal decision theory
(Or game theory.) An area of 
applied mathematics 
concerned with identifying the 
values, uncertainties and other 
constraints that determine an 
optimal decision.

Gradient ascent
(Or method of steepest 
ascent.) A first-order 
optimization scheme that finds 
a maximum of a function by 
changing its arguments in 
proportion to the gradient of 
the function at the current 
value. In short, a hill-climbing 
scheme. The opposite scheme 
is a gradient descent.

is the most valuable of the available states. In general, 
it is impossible to solve the Bellman equation exactly, 
but several approximations exist, ranging from simple 
Rescorla–Wagner models98 to more comprehensive for-
mulations like Q-learning100. Cost also has a key role in 
Bayesian decision theory, in which optimal decisions 
minimize expected cost in the context of uncertainty 
about outcomes; this is central to optimal decision theory 
(game theory) and behavioural economics102–104.

so what does free energy bring to the table? If one 
assumes that the optimal policy performs a gradient 
ascent on value, then it is easy to show that value is 
inversely proportional to surprise (see supplementary 
information s4 (box)). This means that free energy is 
(an upper bound on) expected cost, which makes sense 
as optimal control theory assumes that action mini-
mizes expected cost, whereas the free-energy principle 
states that it minimizes free energy. This is important

because it explains why agents must minimize expected 
cost. Furthermore, free energy provides a quantitative 
and seamless connection between the cost functions 
of reinforcement learning and value in evolutionary 
biology. Finally, the dynamical perspective provides a 
mechanistic insight into how policies are specified in the 
brain: according to the principle of optimality99 cost is the 
rate of change of value (see supplementary information 
s4 (box)), which depends on changes in sensory states. 
This suggests that optimal policies can be prescribed by 
prior expectations about the motion of sensory states. 
Put simply, priors induce a fixed-point attractor, and 
when the states arrive at the fixed point, value will stop 
changing and cost will be minimized. A simple exam-
ple is shown in FIG. 2, in which a cued arm movement 
is simulated using only prior expectations that the arm 
will be drawn to a fixed point (the target). This figure 
illustrates how computational motor control105–109 can 
be formulated in terms of priors and the suppression of 
sensory prediction errors (K.J.F., J. Daunizeau, J. Kilner 
and s.J. Kiebel, unpublished observations). More gener-
ally, it shows how rewards and goals can be considered 
as prior expectations that an action is obliged to fulfil16 
(see also REF. 110). It also suggests how natural selection 
could optimize behaviour through the genetic specifi-
cation of inheritable or innate priors that constrain the 
learning of empirical priors (BOX 2) and subsequent goal-
directed action.

It should be noted that just expecting to be attracted 
to some states may not be sufficient to attain those states. 
This is because one may have to approach attractors vicar-
iously through other states (for example, to avoid obsta-
cles) or conform to physical constraints on action. These 
are some of the more difficult problems of accessing 
distal rewards that reinforcement learning and opti-
mum control contend with. In these circumstances, 
an examination of the density dynamics, on which the 
free-energy principle is based, suggests that it is sufficient 
to keep moving until an a priori attractor is encountered 
(see supplementary information s5 (box)). This entails 
destroying unexpected (costly) fixed points in the envi-
ronment by making them unstable (like shifting to a new 
position when sitting uncomfortably). Mathematically, 
this means adopting a policy that ensures a positive 
divergence in costly states (intuitively, this is like being 
pushed through a liquid with negative viscosity or 
friction). see FIG. 3 for a solution to the classical 
mountain car problem using a simple prior that induces 
this sort of policy. This prior is on motion through state 
space (that is, changes in states) and enforces exploration 
until an attractive state is found. Priors of this sort may 
provide a principled way to understand the exploration–
exploitation trade-off111–113 and related issues in evolu-
tionary biology114. The implicit use of priors to induce 
dynamical instability also provides a key connection 
to dynamical systems theory approaches to the brain 
that emphasize the importance of itinerant dynamics, 
metastability, self-organized criticality and winner-
less competition115–123. These dynamical phenomena 
have a key role in synergetic and autopoietic accounts of 
adaptive behaviour5,124,125.

Figure 2 | A demonstration of cued reaching movements. The lower right part of the 
figure shows a motor plant, comprising a two-jointed arm with two hidden states, each of 
which corresponds to a particular angular position of the two joints; the current position 
of the finger (red circle) is the sum of the vectors describing the location of each joint. 
Here, causal states in the world are the position and brightness of the target (green 
circle). The arm obeys Newtonian mechanics, specified in terms of angular inertia and 
friction. The left part of the figure illustrates that the brain senses hidden states directly 
in terms of proprioceptive input (Sprop) that signals the angular positions (x1,x2) of the 
joints and indirectly through seeing the location of the finger in space (J1,J2). In addition, 
through visual input (Svisual) the agent senses the target location (v1,v2) and brightness (v3). 
Sensory prediction errors are passed to higher brain levels to optimize the conditional 
expectations of hidden states (that is, the angular position of the joints) and causal (that 
is, target) states. The ensuing predictions are sent back to suppress sensory prediction 
errors. At the same time, sensory prediction errors are also trying to suppress themselves 
by changing sensory input through action. The grey and black lines denote reciprocal 
message passing among neuronal populations that encode prediction error and 
conditional expectations; this architecture is the same as that depicted in BOX 2. The 
blue lines represent descending motor control signals from sensory prediction-error 
units. The agent’s generative model included priors on the motion of hidden states that 
effectively engage an invisible elastic band between the finger and target (when the 
target is illuminated). This induces a prior expectation that the finger will be drawn to  
the target, when cued appropriately. The insert shows the ensuing movement trajectory 
caused by action. The red circles indicate the initial and final positions of the finger, 
which reaches the target (green circle) quickly and smoothly; the blue line is the 
simulated trajectory.

> Figure caption (from PDF text): Figure 2 | A demonstration of cued reaching movements. The lower right part of the 
figure shows a motor plant, comprising a two-jointed arm with two hidden states, each of 
which corresponds to a particular angular position of the two joints; the current position 
of the finger (red circle) is the sum of the vectors describing the location of each joint. 
Here, causal states in the world are the position and brightness of the target (green 
circle). The arm obeys Newtonian mechanics, specified in terms of angular inertia and 
friction. The left part of the figure illustrates that the brain senses hidden states directly 
in terms of proprioceptive input (Sprop) that signals the angular positions (x1,x2) of the 
joints and indirectly through seeing the location of the finger in space (J1,J2). In addition, 
through visual input (Svisual) the agent senses the target location (v1,v2) and brightness (v3). 
Sensory prediction errors are passed to higher brain levels to optimize the conditional 
expectations of hidden states (that is, the angular position of the joints) and causal (that 
is, target) states. The ensuing predictions are sent back to suppress sensory prediction 
errors. At the same time, sensory prediction errors are also trying to suppress themselves 
by changing sensory input through action. The grey and black lines denote reciprocal 
message passing among neuronal populations that encode prediction error and 
conditional expectations; this architecture is the same as that depicted in BOX 2. The 
blue lines represent descending motor control signals from sensory prediction-error 
units. The agent’s generative model included priors on the motion of hidden states that 
effectively engage an invisible elastic band between the finger and target (when the 
target is illuminated). This induces a prior expectation that the finger will be drawn to  
the target, when cued appropriately. The insert shows the ensuing movement trajectory 
caused by action. The red circles indicate the initial and final positions of the finger, 
which reaches the target (green circle) quickly and smoothly; the blue line is the 
simulated trajectory.
> Figure description (generated): ## Detailed Figure Description

This figure presents a complex schematic illustrating a predictive coding architecture applied to cued reaching movements, integrating neural representations with a biomechanical model of an arm. The overall layout is divided into two main conceptual areas: the upper left section depicting brain-level predictive processing, and the lower right section detailing the motor plant (the two-jointed arm).

### 1. Overall Layout & Structure
The figure is structured as a multi-part diagram:
*   **Upper Left:** A schematic representation of brain activity, featuring interconnected nodes representing neural populations and signaling pathways.
*   **Center/Middle:** A set of equations defining sensory inputs ($S_{\text{visual}}$ and $S_{\text{prop}}$) and the action ($\vec{a}$).
*   **Lower Right:** A detailed illustration of a "Motor plant," showing the kinematics and trajectory of a two-jointed arm.
*   **Legend/Key:** A small legend in the upper right corner defines the meaning of arrows.

### 2. Visual Components & Symbols

#### A. Predictive Coding Schematic (Upper Left)
*   **Nodes:** Several interconnected, rounded nodes represent neural populations. These nodes are labeled with Greek letters and superscripts (e.g., $\xi_v^{(1)}$, $\mu_X^{(0)}$).
*   **Connections:** Arrows indicate the flow of information.
    *   **Black Arrows (Predictions):** Labeled "Predictions," these arrows flow from higher-level nodes down to lower-level nodes, representing top-down predictions.
    *   **Gray Arrows (Prediction Errors):** Labeled "Prediction errors," these arrows flow from lower-level nodes back up to higher-level nodes, representing sensory prediction errors.
*   **Inputs/Outputs:** The schematic connects to external inputs:
    *   A blue arrow labeled "Motor signals" descends from the upper network to a lower node.
    *   The nodes are linked by lines representing reciprocal message passing (as described in the caption).

#### B. Sensory and Motor Equations (Center)
*   **Sensory Inputs:** Two equations define sensory inputs:
    *   $S_{\text{visual}} = [V] + W_{\text{visual}}$
    *   $S_{\text{prop}} = [X_1, X_2] + W_{\text{prop}}$
*   **Action:** The action $\vec{a}$ is defined by the equation: $\vec{a} = -\partial_t \xi^T \xi$.
*   **Connections:** Dashed lines connect the nodes in the upper schematic to these equations, indicating how sensory inputs relate to the neural states.

#### C. Motor Plant (Lower Right)
*   **Arm Representation:** A diagram shows a two-jointed arm structure. The joints are represented by points, and the finger position is indicated by a red circle.
*   **Joint States:** The state variables $J_1$ and $J_2$ are associated with the joints.
*   **Trajectory Plot:** To the right of the arm diagram, there is a plot showing a movement trajectory.
    *   The **x-axis** and **y-axis** are not explicitly labeled with units, but the plot shows a smooth curve.
    *   The **blue line** represents the simulated trajectory.
    *   **Red Circles:** Mark the initial and final positions of the finger.
    *   **Green Circle:** Represents the target location.

### 3. Labels, Keys & Legends
*   **Legend:** The upper right corner contains a key:
    *   Black arrow $\rightarrow$ Predictions
    *   Gray arrow $\rightarrow$ Prediction errors
*   **Variables:** Key variables include: $\xi_v^{(1)}$, $\mu_X^{(0)}$, $S_{\text{visual}}$, $S_{\text{prop}}$, $\vec{a}$, $V$, $X_1, X_2$, $J_1, J_2$.
*   **Motor Plant Labels:** The motor plant is explicitly labeled as "Jointed arm."

### 4. Data Trends & Details
*   **Trajectory Plot:** The simulated trajectory (blue line) shows a smooth, directed movement from the initial red circle towards the target green circle. The caption notes this trajectory is "quickly and smoothly."
*   **State Representation:** The motor plant description specifies that the current finger position is the sum of vectors describing the location of each joint.

### 5. Contextual Caption Integration
The caption provides crucial context for interpreting the visual elements:
*   **Hidden States:** The two hidden states in the motor plant correspond to the angular positions ($x_1, x_2$) of the two joints.
*   **Sensory Inputs:**
    *   Proprioceptive input ($S_{\text{prop}}$) signals the angular positions ($x_1, x_2$).
    *   Visual input ($S_{\text{visual}}$) senses the target location ($\mathbf{v}_1, \mathbf{v}_2$) and brightness ($\mathbf{v}_3$).
*   **Information Flow:** Sensory prediction errors are passed to higher brain levels to optimize conditional expectations (joint angular positions) and causal states (target location). Predictions are sent back to suppress these errors.
*   **Generative Model:** The agent's generative model includes priors on motion that "effectively engage an invisible elastic band between the finger and target," inducing a prior expectation of attraction when cued.

REVIEWS

134 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 9

f =
=
˙x′

˙x

−∇xϕ − 1⁄8 x′ + σ(a)

x′

Equations of motion

-2
-1
0
1
2
0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

Position (x)

The mountain car problem

20
40
60
80
100
120
–3

–2

–1

0

1

2

3

Time (seconds)

Time (seconds)
20
40
60
80
100
120
–5

0

0

0

5

10

15

20

25

30

Conditional expectations

Height

ϕ(x)

μ(t)x

−c(t)

a(t)

Estimated states
Control signal

Position (x)

–2
–1
0
1
2
–30

–25

–20

–15

–10

–5

0

5

Loss functions (priors)

Force

c(x)

Position (x)
–2
–1
0
1
2
–2

–1

0

1

2

x′

Velocity

Trajectories
Action

a
b

Principle of optimality
An optimal policy has  
the property that whatever the 
initial state and initial decision, 
the remaining decisions must 
constitute an optimal policy 
with regard to the state 
resulting from the first decision.

Exploration–exploitation 
trade-off
Involves a balance between 
exploration (of uncharted 
territory) and exploitation (of 
current knowledge). In 
reinforcement learning, it has 
been studied mainly through 
the multi-armed bandit 
problem.

Dynamical systems theory
An area of applied 
mathematics that describes 
the behaviour of complex 
(possibly chaotic) dynamical 
systems as described by 
differential or difference 
equations.

Synergetics
Concerns the self-organization 
of patterns and structures in 
open systems far from 
thermodynamic equilibrium. It 
rests on the order parameter 
concept, which was generalized 
by Haken to the enslaving 
principle: that is, the dynamics 
of fast-relaxing (stable) modes 
are completely determined by 
the ‘slow’ dynamics of order 
parameters (the amplitudes of 
unstable modes).

Autopoietic
Referring to the fundamental 
dialectic between structure 
and function.

Helmholtzian
Refers to a device or scheme 
that uses a generative model to 
furnish a recognition density 
and learns hidden structures in 
data by optimizing the 
parameters of generative 
models.

In summary, optimal control and decision (game) 
theory start with the notion of cost or utility and try to 
construct value functions of states, which subsequently 
guide action. The free-energy formulation starts with 
a free-energy bound on the value of states, which is 
specified by priors on the motion of hidden environ-
mental states. These priors can incorporate any cost 
function to ensure that costly states are avoided. states 
with minimum cost can be set (by learning or evolu-
tion) in terms of prior expectations about motion and 
the attractors that ensue. In this view, the problem of 
finding sparse rewards in the environment is nature’s 
solution to the problem of how to minimize the entropy 
(average surprise or free energy) of an agent’s states: by 
ensuring they occupy a small set of attracting (that is, 
rewarding) states.

Conclusions and future directions
Although contrived to highlight commonalities, this 
Review suggests that many global theories of brain 
function can be united under a Helmholtzian percep-
tive of the brain as a generative model of the world it 
inhabits18,20,21,25 (FIG. 4); notable examples include the 
integration of the Bayesian brain and computational 
motor control theory, the objective functions shared 
by predictive coding and the infomax principle, 
hierarchical inference and theories of attention, the 
embedding of perception in natural selection and 
the link between optimum control and more exotic 
phenomena in dynamical systems theory. The constant 
theme in all these theories is that the brain optimizes 
a (free-energy) bound on surprise or its complement, 
value. This manifests as perception (so as to change

Figure 3 | solving the mountain car problem with prior expectations. a | How paradoxical but adaptive behaviour (for 
example, moving away from a target to ensure that it is secured later) emerges from simple priors on the motion of hidden 
states in the world. Shown is the landscape or potential energy function (with a minimum at position x = –0.5) that exerts 
forces on a mountain car. The car is shown at the target position on the hill at x =1, indicated by the red circle. The equations 
of motion of the car are shown below the plot. Crucially, at x = 0 the force on the car cannot be overcome by the agent, 
because a squashing function –1≤σ≤1 is applied to action to prevent it being greater than 1. This means that the agent can 
access the target only by starting halfway up the left hill to gain enough momentum to carry it up the other side. b | The 
results of active inference under priors that destabilize fixed points outside the target domain. The priors are encoded in a 
cost function c(x) (top left), which acts like negative friction. When ‘friction’ is negative the car expects to go faster (see 
Supplementary information S5 (box) for details). The inferred hidden states (upper right: position in blue, velocity in green 
and negative dissipation in red) show that the car explores its landscape until it encounters the target, and that friction then 
increases (that is, cost decreases) dramatically to prevent the car from escaping the target (by falling down the hill). The 
ensuing trajectory is shown in blue (bottom left). The paler lines provide exemplar trajectories from other trials, with 
different starting positions. In the real world, friction is constant. However, the car ‘expects’ friction to change as it changes 
position, thus enforcing exploration or exploitation. These expectations are fulfilled by action (lower right).

> Figure caption (from PDF text): Figure 3 | solving the mountain car problem with prior expectations. a | How paradoxical but adaptive behaviour (for 
example, moving away from a target to ensure that it is secured later) emerges from simple priors on the motion of hidden 
states in the world. Shown is the landscape or potential energy function (with a minimum at position x = –0.5) that exerts 
forces on a mountain car. The car is shown at the target position on the hill at x =1, indicated by the red circle. The equations 
of motion of the car are shown below the plot. Crucially, at x = 0 the force on the car cannot be overcome by the agent, 
because a squashing function –1≤σ≤1 is applied to action to prevent it being greater than 1. This means that the agent can 
access the target only by starting halfway up the left hill to gain enough momentum to carry it up the other side. b | The 
results of active inference under priors that destabilize fixed points outside the target domain. The priors are encoded in a 
cost function c(x) (top left), which acts like negative friction. When ‘friction’ is negative the car expects to go faster (see 
Supplementary information S5 (box) for details). The inferred hidden states (upper right: position in blue, velocity in green 
and negative dissipation in red) show that the car explores its landscape until it encounters the target, and that friction then 
increases (that is, cost decreases) dramatically to prevent the car from escaping the target (by falling down the hill). The 
ensuing trajectory is shown in blue (bottom left). The paler lines provide exemplar trajectories from other trials, with 
different starting positions. In the real world, friction is constant. However, the car ‘expects’ friction to change as it changes 
position, thus enforcing exploration or exploitation. These expectations are fulfilled by action (lower right).
> Figure description (generated): ## Figure Description: Action Plot

This figure displays a single time-series plot labeled "Action," representing the control signal $a(t)$ over time.

**1. Overall Layout & Structure:**
The figure consists of a single, large 2D line graph occupying the main visual space. The plot is set against a background color that appears to be a pale beige or tan, contrasting with the white axes and grid lines.

**2. Visual Components & Symbols:**
*   **Axes:** The plot has a horizontal x-axis (representing time) and a vertical y-axis (representing the control signal).
*   **Data Curve:** A single, prominent line graph traces the value of $a(t)$ over time. This curve exhibits significant dynamic behavior, including initial fluctuations, a sharp peak, and subsequent oscillations before settling near zero.
*   **Reference Line:** A dashed horizontal line is present across the plot, positioned at $y=0$, serving as a zero-reference point.

**3. Labels, Keys & Legends:**
*   **Title:** The plot is titled "Action."
*   **Y-Axis Label:** The vertical axis is labeled "Control Signal."
*   **X-Axis Label:** Although the x-axis lacks an explicit label in the visible portion, it represents time.
*   **Data Label:** The curve itself is annotated with the mathematical notation $a(t)$ near its peak.
*   **Axis Scales:**
    *   The y-axis ranges from -3 to 3, with major tick marks at intervals of 1 (i.e., -3, -2, -1, 0, 1, 2, 3).
    *   The x-axis ranges from 0 to 120, with major tick marks every 20 units (0, 20, 40, 60, 80, 100, 120).

**4. Data Trends & Details:**
The plot shows the following temporal progression for $a(t)$:
1.  **Initial Phase (0 to $\approx 45$):** The signal starts near zero, dips slightly below zero (reaching approximately -0.7), rises to a small positive peak ($\approx 1.0$), and then returns toward zero, showing moderate fluctuation.
2.  **Transition Phase ($\approx 45$ to $\approx 60$):** The signal undergoes a rapid, dramatic change. It drops sharply into negative territory, reaching its lowest point (approximately -2.8) around $t=60$.
3.  **Peak Action ($\approx 60$ to $\approx 70$):** Following the deep trough, the signal spikes sharply upward, reaching its maximum value (approximately 2.5) around $t=70$.
4.  **Settling Phase ($\approx 70$ onwards):** After the peak, the signal rapidly decays. It crosses the zero line and settles into small oscillations around $y=0$ for the remainder of the plotted time (up to $t=120$).

**5. Contextual Caption Integration:**
The caption identifies this plot as representing the "action" derived from active inference. Specifically, it relates to the dynamics of solving the mountain car problem. The caption notes that this action $a(t)$ is subject to a squashing function ($\text{-}1 \le \sigma \le 1$) which prevents the action from exceeding 1, although the plot shows values exceeding this limit (up to $\approx 2.5$), suggesting that $a(t)$ here might represent the unconstrained control signal or a specific phase of the process described. The caption further explains that these actions are generated based on expectations about how friction (cost) changes as the car moves.

> Figure caption (from PDF text): Figure 3 | solving the mountain car problem with prior expectations. a | How paradoxical but adaptive behaviour (for 
example, moving away from a target to ensure that it is secured later) emerges from simple priors on the motion of hidden 
states in the world. Shown is the landscape or potential energy function (with a minimum at position x = –0.5) that exerts 
forces on a mountain car. The car is shown at the target position on the hill at x =1, indicated by the red circle. The equations 
of motion of the car are shown below the plot. Crucially, at x = 0 the force on the car cannot be overcome by the agent, 
because a squashing function –1≤σ≤1 is applied to action to prevent it being greater than 1. This means that the agent can 
access the target only by starting halfway up the left hill to gain enough momentum to carry it up the other side. b | The 
results of active inference under priors that destabilize fixed points outside the target domain. The priors are encoded in a 
cost function c(x) (top left), which acts like negative friction. When ‘friction’ is negative the car expects to go faster (see 
Supplementary information S5 (box) for details). The inferred hidden states (upper right: position in blue, velocity in green 
and negative dissipation in red) show that the car explores its landscape until it encounters the target, and that friction then 
increases (that is, cost decreases) dramatically to prevent the car from escaping the target (by falling down the hill). The 
ensuing trajectory is shown in blue (bottom left). The paler lines provide exemplar trajectories from other trials, with 
different starting positions. In the real world, friction is constant. However, the car ‘expects’ friction to change as it changes 
position, thus enforcing exploration or exploitation. These expectations are fulfilled by action (lower right).
> Figure description (generated): This figure, labeled as Figure 3, presents a visualization related to the "mountain car problem" under prior expectations. The visual content appears to be divided into multiple conceptual parts, though the provided image snippet focuses primarily on one specific plot.

### 1. Overall Layout & Structure
The visible portion of the figure is dominated by a single, large 2D plot. Based on the caption, this plot likely corresponds to part (b) of the full figure, illustrating trajectories. The structure is a Cartesian coordinate plot showing paths in a state space.

### 2. Visual Components & Symbols
*   **Axes:** The plot has a horizontal (x-axis) and a vertical (y-axis).
*   **Trajectories:** Multiple curved lines are present, representing trajectories. These lines are colored in shades of blue/cyan and appear to spiral or follow complex paths around a central region.
*   **Target Position:** A distinct, solid red circle is located on the plot, marking a specific point.
*   **Background/Shading:** The area surrounding the trajectories is filled with a pale, yellowish-tan color.

### 3. Labels, Keys & Legends
*   **Y-Axis Label:** The vertical axis is labeled with the variable $x'$.
*   **X-Axis Label:** The horizontal axis is labeled with "Position (x)".
*   **Numerical Ticks:** Both axes have numerical tick marks ranging from -2 to 2.
    *   The y-axis ($x'$) ticks are marked at -2, -1, 0, 1, and 2.
    *   The x-axis (Position (x)) ticks are marked at -2, -1, 0, 1, and 2.

### 4. Data Trends & Details
*   **Trajectories:** The blue lines depict complex, looping trajectories that converge toward or interact with the red target circle.
*   **Target Location:** The red circle (the target) is situated near the coordinates $x \approx 1$ and $x' \approx 0$.
*   **Trajectory Dynamics:** The paler lines surrounding the main blue trajectories are described in the caption as "exemplar trajectories from other trials, with different starting positions," suggesting they represent variations of the observed behavior.

### 5. Contextual Caption Integration
The caption identifies this plot as showing "The ensuing trajectory is shown in blue (bottom left)" under the context of active inference with priors that destabilize fixed points.
*   The **red circle** represents the "target position on the hill at $x=1$."
*   The **blue lines** represent the "inferred hidden states" or trajectories of the car.
*   The caption explains that this behavior arises because the car "expects friction to change as it changes position," leading to exploration or exploitation dynamics.

REVIEWS

> Figure description (generated): ## Figure Description: The Mountain Ear Problem

This figure is a two-dimensional Cartesian plot illustrating the function $\phi(x)$ related to "The mountain ear problem."

**1. Overall Layout & Structure:**
The figure consists of a single plot area set against a light beige/tan background. It features standard Cartesian axes, indicating a function's relationship between an independent variable ($x$) and a dependent variable ($\phi(x)$).

**2. Visual Components & Symbols:**
*   **Axes:** A horizontal x-axis and a vertical y-axis define the coordinate system.
*   **Curve:** A continuous, smooth curve labeled $\phi(x)$ is plotted across the graph. This curve exhibits a characteristic "mountain" or U-shape, starting high on the left, decreasing to a minimum, and then increasing again.
*   **Data Point:** A distinct red circular marker is placed on the curve at a specific point.
*   **Vertical Dashed Line:** A vertical, dashed gray line intersects the plot at $x=1$. This line appears to be marking a specific critical value or point of interest on the x-axis.

**3. Labels, Keys & Legends:**
*   **Title (External):** The title above the figure reads: "The mountain ear problem".
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from 0.0 to 0.7, representing the value of $\phi(x)$.
*   **X-Axis Label:** The horizontal axis is labeled with numerical values ranging from -2.0 to 2.0, representing the variable $x$.
*   **Function Label:** The curve is explicitly labeled with the mathematical notation $\phi(x)$.

**4. Data Trends & Details:**
*   **Y-Axis Range:** The vertical axis ranges from 0.0 to 0.7, with major ticks marked every 0.1 (e.g., 0.1, 0.2, ..., 0.7).
*   **X-Axis Range:** The horizontal axis ranges from -2.0 to 2.0, with major ticks marked every 1.0 (e.g., -2, -1, 0, 1, 2).
*   **Curve Trend:** The function $\phi(x)$ starts at a high value (approximately 0.52) near $x=-2$. It decreases sharply, reaching a minimum value very close to 0.0 (approximately $y \approx 0.01$) around $x=0$. It then increases, passing through a local minimum near $x=1$ before rising again towards $y \approx 0.27$ at $x=2$.
*   **Specific Points:**
    *   The red data point is located precisely on the curve at $x=1$. Its corresponding y-value appears to be approximately 0.16.
    *   The vertical dashed line is positioned at $x=1$.

**5. Contextual Caption Integration:**
No specific contextual caption text was provided to integrate, so the description relies solely on the visual elements and labels present in the figure itself. The plot visually represents a non-monotonic function $\phi(x)$ exhibiting a local minimum, which is highlighted by the red marker at $x=1$ and the corresponding vertical reference line.

> Figure description (generated): This figure is a single-panel line graph illustrating the time evolution of two variables, $-c(t)$ and $\mu(t)^x$.

**1. Overall Layout & Structure:**
The figure consists of a single Cartesian coordinate plot. The background is shaded in a light tan/beige color, while the plotting area itself contains two distinct curves.

**2. Visual Components & Symbols:**
*   **Axes:** A horizontal x-axis and a vertical y-axis define the plot space.
*   **Curves:** Two distinct lines are plotted:
    *   One line, labeled $-c(t)$, is colored red.
    *   The second line, labeled $\mu(t)^x$, is colored dark blue/black.
*   **Grid/Ticks:** Major tick marks are present on both axes, indicating numerical values.

**3. Labels, Keys & Legends:**
*   **Y-Axis Label:** The vertical axis is labeled with numerical values ranging from -5 to 30, marked in increments of 5 (e.g., 0, 5, 10, ..., 30).
*   **X-Axis Label:** The horizontal axis is labeled with numerical values ranging from 0 to 120, marked in increments of 20 (e.g., 0, 20, 40, ..., 120).
*   **Annotations:** Two labels identify the plotted curves:
    *   "$-c(t)$" is positioned near the upper red curve.
    *   "$\mu(t)^x$" is positioned near the lower blue/black curve.

**4. Data Trends & Details:**
*   **Curve $-c(t)$ (Red):** This curve remains near zero for the initial period (from $t=0$ up to approximately $t=55$). Around $t \approx 60$, the curve exhibits a sharp, rapid increase. It rises steeply from near zero to reach a plateau value of approximately 25 by $t \approx 80$. It maintains this high level (around 25) through the end of the plotted range ($t=120$).
*   **Curve $\mu(t)^x$ (Blue/Black):** This curve remains close to zero throughout the entire time course. It shows minor fluctuations:
    *   It starts slightly below zero near $t=0$.
    *   It dips slightly negative between $t=20$ and $t=40$.
    *   It shows a small positive peak around $t=50$ (reaching slightly above 0).
    *   After the sharp rise of $-c(t)$ (around $t=60$), $\mu(t)^x$ settles back down and remains very close to the zero line for the remainder of the plot.

**5. Contextual Caption Integration:**
No external caption text was provided, so no specific contextual interpretation beyond the mathematical labels ($c(t)$, $\mu(t)^x$) can be offered.

> Figure description (generated): ## Figure Description: Loss Functions (plots)

This figure is a single-panel plot illustrating the shape of a loss function, $c(x)$, as a function of an input variable $x$.

**1. Overall Layout & Structure:**
The figure is a standard Cartesian coordinate plot, occupying the entire visual space. It features one primary curve representing the loss function and several horizontal reference lines.

**2. Visual Components & Symbols:**
*   **Axes:** A vertical (y-axis) and a horizontal (x-axis) are present.
*   **Loss Function Curve:** A continuous, smooth curve labeled $c(x)$ is plotted. This function exhibits a characteristic U-shape (a convex shape) with a distinct minimum point.
*   **Reference Lines:** Two horizontal dashed lines are present:
    *   One line is positioned at $y=0$.
    *   A second, implied horizontal line exists at the minimum value of the curve.
*   **Annotation:** A small, solid red circle is placed directly above the minimum point of the $c(x)$ curve, serving as a visual marker for the optimal or target state.

**3. Labels, Keys & Legends:**
*   **Title:** The figure is titled "Loss Functions (plots)" at the top.
*   **Y-Axis Label:** The vertical axis is labeled "Estimated states". The scale ranges from -30 to 5, with major tick marks every 5 units (e.g., -25, -20, -15, etc.).
*   **X-Axis Label:** The horizontal axis is not explicitly labeled with a variable name, but the scale ranges from -2 to 2.
*   **Function Label:** The curve is explicitly labeled with the mathematical notation $c(x)$.

**4. Data Trends & Details:**
*   **X-Axis Range:** The plot spans from $x = -2$ to $x = 2$.
*   **Y-Axis Range:** The plot spans from $y = -30$ to $y = 5$.
*   **Curve Trend:** The function $c(x)$ starts high (near 0) on the left, decreases sharply as $x$ approaches 1, reaches a deep minimum value (approximately $y \approx -28$) near $x=1$, and then rises sharply again, returning close to the zero line as $x$ approaches 2.
*   **Minimum Point:** The minimum of the function occurs at an $x$-value slightly greater than 1, where the corresponding $y$-value is the lowest point on the graph. The red circle highlights this minimum region.
*   **Zero Line:** The dashed line at $y=0$ serves as a baseline reference, indicating the state where the loss is zero.

**5. Contextual Caption Integration:**
The figure visually represents a typical optimization landscape where the goal is to minimize the loss function $c(x)$. The red circle marks the location of the minimum error state, which corresponds to the desired "Estimated states" value.

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 135

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 10

˙μv

(i) = Dμv

(i)
(i)
(i)
− ∂vε
Tξ
(i + 1)
− ξv

μθij = −∂θijεTξ

˙a = −∂aεTξ

Infomax and the redundancy
minimization principle

Maximization of the mutual 
information between sensations 
and representations

Probabilistic neuronal coding

Encoding a recognition density 
in terms of conditional 
expectations and uncertainty

The Bayesian brain hypothesis

Minimizing the difference between a 
recognition density and the conditional 
density on sensory causes

Computational motor control

Minimization of sensory 
prediction errors

Predictive coding and hierarchical inference

Minimization of prediction error 
with recurrent message passing

Perceptual learning and memory

Optimization of synaptic efficacy 
to represent causal structure 
in the sensorium

Associative plasticity

Optimization of synaptic efficacy

Optimal control and value learning

Optimization of a free-energy 
bound on surprise or value

Model selection and evolution

The free-energy principle

Optimizing the agent’s model and 
priors through neurodevelopment 
and natural selection

Minimization of the free energy of 
sensations and the representation 
of their causes

Attention and biased competition

Optimization of synaptic gain 
representing the precision 
(salience) of predictions

m = arg min ∫dtF

a, μ, m = arg min F (s~, μ | m)

a, μ = arg max V (s~

| m)

μ = arg max {I (s~, μ ) − H(μ)}

μθ = arg min ∫dtF

μγ = arg min ∫dtF

μ = arg min DKL(q(ϑ) || (p(ϑ | s~))

q(ϑ ) = N ( μ, Σ)

predictions) or action (so as to change the sensations 
that are predicted). Crucially, these predictions depend 
on prior expectations (that furnish policies), which 
are optimized at different (somatic and evolutionary) 
timescales and define what is valuable.

What does the free-energy principle portend for the 
future? If its main contribution is to integrate estab-
lished theories, then the answer is probably ‘not a lot’. 
Conversely, it may provide a framework in which cur-
rent debates could be resolved, for example whether 
dopamine encodes reward prediction error or sur-
prise126,127 — this is particularly important for under-
standing conditions like addiction, Parkinson’s disease 
and schizophrenia. Indeed, the free-energy formulation 
has already been used to explain the positive symptoms 
of schizophrenia in terms of false inference128. The free-
energy formulation could also provide new approaches

Figure 4 | The free-energy principle and other theories. Some of the theoretical constructs considered in this Review 
and how they relate to the free-energy principle (centre). The variables are described in BOXES 1,2 and a full explanation 
of the equations can be found in the Supplementary information S1–S4 (boxes).

> Figure caption (from PDF text): Figure 4 | The free-energy principle and other theories. Some of the theoretical constructs considered in this Review 
and how they relate to the free-energy principle (centre). The variables are described in BOXES 1,2 and a full explanation 
of the equations can be found in the Supplementary information S1–S4 (boxes).
> Figure description (generated): ## Detailed Figure Description: The Free-Energy Principle and Other Theories

This figure, titled "Figure 4 | The free-energy principle and other theories," presents a complex conceptual diagram illustrating the relationship between the Free-Energy Principle (FEP) and several other theoretical constructs in neuroscience. The structure is organized around a central concept, with surrounding boxes detailing related theories and their mathematical formulations.

### 1. Overall Layout & Structure
The diagram is structured as a central hub-and-spoke model, dominated by a large, stylized green brain/neural network graphic in the center. This central element is surrounded by several distinct conceptual boxes, each representing a specific theory or principle. Arrows indicate relationships and flow between these concepts.

### 2. Visual Components & Symbols
*   **Central Element:** A large, stylized graphic resembling a cross-section of a brain or neural network, colored predominantly in shades of green. This graphic serves as the visual anchor for the entire diagram.
*   **Conceptual Boxes:** There are multiple rectangular boxes surrounding the central graphic, each containing a theory name and associated mathematical equations.
*   **Connecting Elements:** Arrows connect the surrounding boxes to the central concept, implying that these theories relate to or are derived from the core principles.

### 3. Labels, Keys & Legends (Detailed Content)

The diagram is organized into several distinct theoretical modules:

**Top Row (Left to Right):**
1.  **Attention and biased competition:**
    *   $\mu_{\psi} = \arg \min \int d\text{tf}$
    *   Optimization of synaptic gain representing the precision (salience) of predictions
2.  **Predictive coding and hierarchical inference:**
    *   $\mu^{(l)} = D\mu^{(l)} - \partial_e \mathcal{L}^{(l)} - \xi_{l+1}$
    *   Minimization of prediction error with recurrent message passing
3.  **Computational motor control:**
    *   $\dot{a} = -\partial_e \mathcal{L}'$
    *   Minimization of sensory prediction errors

**Middle Row (Left to Right):**
4.  **Associative plasticity:**
    *   $\mu_{aq} = -\partial_e \xi'$
    *   Optimization of synaptic efficacy
5.  **The Bayesian brain hypothesis:** (Positioned centrally, slightly below the top row)
    *   $\mu = \arg \min D_{\text{KL}}(\mathbf{q}(\theta) || p(\theta|\mathbf{s}))$
6.  **Perceptual learning and memory:**
    *   $\mu_q = \arg \min \int d\text{tf}$
    *   Optimization of synaptic efficacy to represent causal structure in the sensorium

**Bottom Row (Left to Right):**
7.  **Probabilistic neuronal coding:**
    *   $q(\theta) = N(\mu, \Sigma)$
    *   Encoding a recognition density in terms of conditional expectations and uncertainty
8.  **The free-energy principle:** (Positioned centrally, below the Bayesian brain hypothesis)
    *   $\mu, \mu = \arg \min F(\mathbf{\mu}, \mathbf{m})$
    *   Minimization of the free energy of sensations and the representation of their causes
9.  **Model selection and evolution:**
    *   $m = \arg \min \int d\text{tf}$
    *   Optimizing the agent's model and priors through neurodevelopment and natural selection

**Right Side:**
10. **Optimal control and value learning:**
    *   $a, \mu = \arg \max V(\xi|\mathbf{m})$
    *   Optimization of a free-energy bound on surprise or value
11. **Infomax and the redundancy minimization principle:**
    *   $\mu = \arg \max I(\xi, \mathbf{m}) - H(\mathbf{m})$
    *   Maximization of the mutual information between sensations and representations

### 4. Contextual Caption Integration
The caption clarifies that the diagram illustrates "The free-energy principle and other theories." It specifies that the variables are described in associated boxes (Boxes 1, 2, etc., corresponding to the labeled modules) and that a full explanation of the equations is provided in Supplementary information S1–S4. The central concept, "The free-energy principle," is highlighted as the core framework connecting these diverse theories.

to old problems that might call for a reappraisal of 
conventional notions, particularly in reinforcement 
learning and motor control.

If the arguments underlying the free-energy principle 
hold, then the real challenge is to understand how it 
manifests in the brain. This speaks to a greater appre-
ciation of hierarchical message passing41, the func-
tional role of specific neurons and microcircuits and 
the dynamics they support (for example, what is the 
relationship between predictive coding, attention 
and dynamic co ordination in the brain?129). Beyond 
neuroscience, many exciting applications in engineering, 
robotics, embodied cognition and evolutionary biology 
suggest themselves; although fanciful, it is not difficult to 
imagine building little free-energy machines that garner 
and model sensory information (like our children) to 
maximize the evidence for their own existence.

1. 
Huang, G. Is this a unified theory of the brain?  
New Scientist 2658, 30–33 (2008).
2. 
Friston K., Kilner, J. & Harrison, L. A free energy  
principle for the brain. J. Physiol. Paris 100, 70–87 
(2006).
An overview of the free-energy principle that 
describes its motivation and relationship to 
generative models and predictive coding. This

paper focuses on perception and the 
neurobiological infrastructures involved.
3. 
Ashby, W. R. Principles of the self-organising dynamic 
system. J. Gen. Psychol. 37, 125–128 (1947).
4. 
Nicolis, G. & Prigogine, I. Self‑Organisation in Non‑
Equilibrium Systems (Wiley, New York, 1977).
5. 
Haken, H. Synergistics: an Introduction. Non‑
Equilibrium Phase Transition and Self‑Organisation in

Physics, Chemistry and Biology 3rd edn (Springer, 
New York, 1983).
6. 
Kauffman, S. The Origins of Order: Self‑Organization 
and Selection in Evolution (Oxford Univ. Press, Oxford, 
1993).
7. 
Bernard, C. Lectures on the Phenomena Common  
to Animals and Plants (Thomas, Springfield,  
1974).

REVIEWS

136 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 11

8. 
Applebaum, D. Probability and Information: an 
Integrated Approach (Cambridge Univ. Press, 
Cambridge, UK, 2008).
9. 
Evans, D. J. A non-equilibrium free energy theorem  
for deterministic systems. Mol. Physics 101,  
15551–11554 (2003).
10. Crauel, H. & Flandoli, F. Attractors for random 
dynamical systems. Probab. Theory Relat. Fields 100, 
365–393 (1994).
11. Feynman, R. P. Statistical Mechanics: a Set of Lectures 
(Benjamin, Reading, Massachusetts, 1972).
12. Hinton, G. E. & von Cramp, D. Keeping neural 
networks simple by minimising the description length 
of weights. Proc. 6th Annu. ACM Conf. Computational 
Learning Theory 5–13 (1993).
13. MacKay. D. J. C. Free-energy minimisation algorithm 
for decoding and cryptoanalysis. Electron. Lett. 31, 
445–447 (1995).
14. Neal, R. M. & Hinton, G. E. in Learning in Graphical 
Models (ed. Jordan, M. I.) 355–368 (Kluwer 
Academic, Dordrecht, 1998).
15. Itti, L. & Baldi, P. Bayesian surprise attracts human 
attention. Vision Res. 49, 1295–1306 (2009).
16. Friston, K., Daunizeau, J. & Kiebel, S. Active inference 
or reinforcement learning? PLoS ONE 4, e6421 
(2009).
17. Knill, D. C. & Pouget, A. The Bayesian brain: the role 
of uncertainty in neural coding and computation. 
Trends Neurosci. 27, 712–719 (2004).
A nice review of Bayesian theories of perception 
and sensorimotor control. Its focus is on Bayes 
optimality in the brain and the implicit nature of 
neuronal representations.
18. von Helmholtz, H. in Treatise on Physiological Optics 
Vol. III 3rd edn (Voss, Hamburg, 1909).
19. MacKay, D. M. in Automata Studies (eds Shannon, 
C. E. & McCarthy, J.) 235–251 (Princeton Univ. Press, 
Princeton, 1956).
20. Neisser, U. Cognitive Psychology 
(Appleton-Century-Crofts, New York, 1967).
21. Gregory, R. L. Perceptual illusions and brain models. 
Proc. R. Soc. Lond. B Biol. Sci. 171, 179–196 (1968).
22. Gregory, R. L. Perceptions as hypotheses. Philos. 
Trans. R. Soc. Lond. B Biol. Sci. 290, 181–197 (1980).
23. Ballard, D. H., Hinton, G. E. & Sejnowski, T. J. Parallel 
visual computation. Nature 306, 21–26 (1983).
24. Kawato, M., Hayakawa, H. & Inui, T. A forward-inverse 
optics model of reciprocal connections between visual 
areas. Network: Computation in Neural Systems 4, 
415–422 (1993).
25. Dayan, P., Hinton, G. E. & Neal, R. M. The Helmholtz 
machine. Neural Comput. 7, 889–904 (1995).
This paper introduces the central role of generative 
models and variational approaches to hierarchical 
self-supervised learning and relates this to the 
function of bottom-up and top-down cortical 
processing pathways.
26. Lee, T. S. & Mumford, D. Hierarchical Bayesian 
inference in the visual cortex. J. Opt. Soc. Am. A Opt. 
Image Sci. Vis. 20, 1434–1448 (2003).
27. Kersten, D., Mamassian, P. & Yuille, A. Object 
perception as Bayesian inference. Annu. Rev. Psychol. 
55, 271–304 (2004).
28. Friston, K. J. A theory of cortical responses. Philos. 
Trans. R. Soc. Lond. B Biol. Sci. 360, 815–836 
(2005).
29. Beal, M. J. Variational Algorithms for Approximate 
Bayesian Inference. Thesis, University College London 
(2003).
30. Efron, B. & Morris, C. Stein’s estimation rule and its 
competitors – an empirical Bayes approach. J. Am. 
Stats. Assoc. 68, 117–130 (1973).
31. Kass, R. E. & Steffey, D. Approximate Bayesian 
inference in conditionally independent hierarchical 
models (parametric empirical Bayes models). J. Am. 
Stat. Assoc. 407, 717–726 (1989).
32. Zeki, S. & Shipp, S. The functional logic of cortical 
connections. Nature 335, 311–317 (1988).
Describes the functional architecture of cortical 
hierarchies with a focus on patterns of anatomical 
connections in the visual cortex. It emphasizes the 
role of functional segregation and integration (that 
is, message passing among cortical areas).
33. Felleman, D. J. & Van Essen, D. C. Distributed 
hierarchical processing in the primate cerebral cortex. 
Cereb. Cortex 1, 1–47 (1991).
34. Mesulam, M. M. From sensation to cognition. Brain 
121, 1013–1052 (1998).
35. Sanger, T. Probability density estimation for the 
interpretation of neural population codes. 
J. Neurophysiol. 76, 2790–2793 (1996).

36. Zemel, R., Dayan, P. & Pouget, A. Probabilistic 
interpretation of population code. Neural Comput. 10, 
403–430 (1998).
37. Paulin, M. G. Evolution of the cerebellum as a 
neuronal machine for Bayesian state estimation. 
J. Neural Eng. 2, S219–S234 (2005).
38. Ma, W. J., Beck, J. M., Latham, P. E. & Pouget, A. 
Bayesian inference with probabilistic population 
codes. Nature Neurosci. 9, 1432–1438 (2006).
39. Friston, K., Mattout, J., Trujillo-Barreto, N., 
Ashburner, J. & Penny, W. Variational free energy and 
the Laplace approximation. Neuroimage 34,  
220–234 (2007).
40. Rao, R. P. & Ballard, D. H. Predictive coding in the 
visual cortex: a functional interpretation of some 
extra-classical receptive field effects. Nature Neurosci. 
2, 79–87 (1998).
Applies predictive coding to cortical processing to 
provide a compelling account of extra-classical 
receptive fields in the visual system. It emphasizes 
the importance of top-down projections in 
providing predictions, by modelling perceptual 
inference.
41. Mumford, D. On the computational architecture of the 
neocortex. II. The role of cortico-cortical loops. Biol. 
Cybern. 66, 241–251 (1992).
42. Friston, K. Hierarchical models in the brain. PLoS 
Comput. Biol. 4, e1000211 (2008).
43. Murray, S. O., Kersten, D., Olshausen, B. A., Schrater, P. 
& Woods, D. L. Shape perception reduces activity in 
human primary visual cortex. Proc. Natl Acad. Sci. 
USA 99, 15164–15169 (2002).
44. Garrido, M. I., Kilner, J. M., Kiebel, S. J. & Friston, 
K. J. Dynamic causal modeling of the response to 
frequency deviants. J. Neurophysiol. 101,  
2620–2631 (2009).
45. Sherman, S. M. & Guillery, R. W. On the actions that 
one nerve cell can have on another: distinguishing 
“drivers” from “modulators”. Proc. Natl Acad. Sci. USA 
95, 7121–7126 (1998).
46. Angelucci, A. & Bressloff, P. C. Contribution of 
feedforward, lateral and feedback connections to the 
classical receptive field center and extra-classical 
receptive field surround of primate V1 neurons.  
Prog. Brain Res. 154, 93–120 (2006).
47. Grossberg, S. Towards a unified theory of neocortex: 
laminar cortical circuits for vision and cognition.  
Prog. Brain Res. 165, 79–104 (2007).
48. Grossberg, S. & Versace, M. Spikes, synchrony, and 
attentive learning by laminar thalamocortical circuits. 
Brain Res. 1218, 278–312 (2008).
49. Barlow, H. in Sensory Communication (ed. Rosenblith, W.) 
217–234 (MIT Press, Cambridge, Massachusetts, 
1961).
50. Linsker, R. Perceptual neural organisation: some 
approaches based on network models and  
information theory. Annu. Rev. Neurosci. 13,  
257–281 (1990).
51. Oja, E. Neural networks, principal components, and 
subspaces. Int. J. Neural Syst. 1, 61–68 (1989).
52. Bell, A. J. & Sejnowski, T. J. An information 
maximisation approach to blind separation and blind 
de-convolution. Neural Comput. 7, 1129–1159 
(1995).
53. Atick, J. J. & Redlich, A. N. What does the retina know 
about natural scenes? Neural Comput. 4, 196–210 
(1992).
54. Optican, L. & Richmond, B. J. Temporal encoding of 
two-dimensional patterns by single units in primate 
inferior cortex. III Information theoretic analysis. 
J. Neurophysiol. 57, 132–146 (1987).
55. Olshausen, B. A. & Field, D. J. Emergence of simple-
cell receptive field properties by learning a sparse 
code for natural images. Nature 381, 607–609 
(1996).
56. Simoncelli, E. P. & Olshausen, B. A. Natural image 
statistics and neural representation. Annu. Rev. 
Neurosci. 24, 1193–1216 (2001).
A nice review of information theory in visual 
processing. It covers natural scene statistics and 
empirical tests of the efficient coding hypothesis in 
individual neurons and populations of neurons.
57. Friston, K. J. The labile brain. III. Transients and 
spatio-temporal receptive fields. Philos. Trans. R. Soc. 
Lond. B Biol. Sci. 355, 253–265 (2000).
58. Bialek, W., Nemenman, I. & Tishby, N. Predictability, 
complexity, and learning. Neural Comput. 13,  
2409–2463 (2001).
59. Lewen, G. D., Bialek, W. & de Ruyter van Steveninck, 
R. R. Neural coding of naturalistic motion stimuli. 
Network 12, 317–329 (2001).

60. Laughlin, S. B. Efficiency and complexity in neural 
coding. Novartis Found. Symp. 239, 177–187 
(2001).
61. Tipping, M. E. Sparse Bayesian learning and the 
Relevance Vector Machine. J. Machine Learn. Res. 1, 
211–244 (2001).
62. Paus, T., Keshavan, M. & Giedd, J. N. Why do many 
psychiatric disorders emerge during adolescence? 
Nature Rev. Neurosci. 9, 947–957 (2008).
63. Gilestro, G. F., Tononi, G. & Cirelli, C. Widespread 
changes in synaptic markers as a function of sleep and 
wakefulness in Drosophila. Science 324, 109–112 
(2009).
64. Roweis, S. & Ghahramani, Z. A unifying review of 
linear Gaussian models. Neural Comput. 11, 305–345 
(1999).
65. Hebb, D. O. The Organization of Behaviour (Wiley, 
New York, 1949).
66. Paulsen, O. & Sejnowski, T. J. Natural patterns of 
activity and long-term synaptic plasticity. Curr. Opin. 
Neurobiol. 10, 172–179 (2000).
67. von der Malsburg, C. The Correlation Theory of Brain 
Function. Internal Report 81–82, Dept. Neurobiology, 
Max-Planck-Institute for Biophysical Chemistry 
(1981).
68. Singer, W. & Gray, C. M. Visual feature integration and 
the temporal correlation hypothesis. Annu. Rev. 
Neurosci. 18, 555–586 (1995).
69. Bienenstock, E. L., Cooper, L. N. & Munro, P. W. 
Theory for the development of neuron selectivity: 
orientation specificity and binocular interaction in 
visual cortex. J. Neurosci. 2, 32–48 (1982).
70. Abraham, W. C. & Bear, M. F. Metaplasticity: the 
plasticity of synaptic plasticity. Trends Neurosci. 19, 
126–130 (1996).
71. Pareti, G. & De Palma, A. Does the brain oscillate? 
The dispute on neuronal synchronization. Neurol. Sci. 
25, 41–47 (2004).
72. Leutgeb, S., Leutgeb, J. K., Moser, M. B. & Moser, E. I. 
Place cells, spatial maps and the population code for 
memory. Curr. Opin. Neurobiol. 15, 738–746  
(2005).
73. Durstewitz, D. & Seamans, J. K. Beyond bistability: 
biophysics and temporal dynamics of working memory. 
Neuroscience 139, 119–133 (2006).
74. Anishchenko, A. & Treves, A. Autoassociative memory 
retrieval and spontaneous activity bumps in small-
world networks of integrate-and-fire neurons. 
J. Physiol. Paris 100, 225–236 (2006).
75. Abbott, L. F., Varela, J. A., Sen, K. & Nelson, S. B. 
Synaptic depression and cortical gain control. Science 
275, 220–224 (1997).
76. Yu, A. J. & Dayan, P. Uncertainty, neuromodulation 
and attention. Neuron 46, 681–692 (2005).
77. Doya, K. Metalearning and neuromodulation. Neural 
Netw. 15, 495–506 (2002).
78. Chawla, D., Lumer, E. D. & Friston, K. J. The 
relationship between synchronization among neuronal 
populations and their mean activity levels. Neural 
Comput. 11, 1389–1411 (1999).
79. Fries, P., Womelsdorf, T., Oostenveld, R. & Desimone, R. 
The effects of visual stimulation and selective visual 
attention on rhythmic neuronal synchronization in 
macaque area V4. J. Neurosci. 28, 4823–4835 
(2008).
80. Womelsdorf, T. & Fries, P. Neuronal coherence during 
selective attentional processing and sensory-motor 
integration. J. Physiol. Paris 100, 182–193 (2006).
81. Desimone, R. Neural mechanisms for visual memory 
and their role in attention. Proc. Natl Acad. Sci. USA 
93, 13494–13499 (1996).
A nice review of mnemonic effects (such as 
repetition suppression) on neuronal responses and 
how they bias the competitive interactions between 
stimulus representations in the cortex. It provides 
a good perspective on attentional mechanisms in 
the visual system that is empirically grounded.
82. Treisman, A. Feature binding, attention and object 
perception. Philos. Trans. R. Soc. Lond. B Biol. Sci. 
353, 1295–1306 (1998).
83. Maunsell, J. H. & Treue, S. Feature-based attention in 
visual cortex. Trends Neurosci. 29, 317–322 (2006).
84. Spratling, M. W. Predictive-coding as a model of 
biased competition in visual attention. Vision Res. 48, 
1391–1408 (2008).
85. Reynolds, J. H. & Heeger, D. J. The normalization 
model of attention. Neuron 61, 168–185 (2009).
86. Schroeder, C. E., Mehta, A. D. & Foxe, J. J. 
Determinants and mechanisms of attentional 
modulation of neural processing. Front. Biosci. 6, 
D672–D684 (2001).

REVIEWS

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 137

© 20
 Macmillan Publishers Limited. All rights reserved
10


---

## Page 12

87. Hirayama, J., Yoshimoto, J. & Ishii, S. Bayesian 
representation learning in the cortex regulated by 
acetylcholine. Neural Netw. 17, 1391–1400 (2004).
88. Edelman, G. M. Neural Darwinism: selection and 
reentrant signaling in higher brain function. Neuron 
10, 115–125 (1993).
89. Knobloch, F. Altruism and the hypothesis of meta-
selection in human evolution. J. Am. Acad. 
Psychoanal. 29, 339–354 (2001).
90. Friston, K. J., Tononi, G., Reeke, G. N. Jr, Sporns, O. & 
Edelman, G. M. Value-dependent selection in the 
brain: simulation in a synthetic neural model. 
Neuroscience 59, 229–243 (1994).
91. Sutton, R. S. & Barto, A. G. Toward a modern theory of 
adaptive networks: expectation and prediction. 
Psychol. Rev. 88, 135–170 (1981).
92. Montague, P. R., Dayan, P., Person, C. & Sejnowski, 
T. J. Bee foraging in uncertain environments using 
predictive Hebbian learning. Nature 377, 725–728 
(1995).
A computational treatment of behaviour that 
combines ideas from optimal control theory and 
dynamic programming with the neurobiology of 
reward. This provided an early example of value 
learning in the brain.
93. Schultz, W. Predictive reward signal of dopamine 
neurons. J. Neurophysiol. 80, 1–27 (1998).
94. Daw, N. D. & Doya, K. The computational 
neurobiology of learning and reward. Curr. Opin. 
Neurobiol. 16, 199–204 (2006).
95. Redgrave, P. & Gurney, K. The short-latency dopamine 
signal: a role in discovering novel actions? Nature Rev. 
Neurosci. 7, 967–975 (2006).
96. Berridge, K. C. The debate over dopamine’s role in 
reward: the case for incentive salience. 
Psychopharmacology (Berl.) 191, 391–431 (2007).
97. Sella, G. & Hirsh, A. E. The application of statistical 
physics to evolutionary biology. Proc. Natl Acad. Sci. 
USA 102, 9541–9546 (2005).
98. Rescorla, R. A. & Wagner, A. R. in Classical 
Conditioning II: Current Research and Theory (eds 
Black, A. H. & Prokasy, W. F.) 64–99 (Appleton 
Century Crofts, New York, 1972).
99. Bellman, R. On the Theory of Dynamic Programming. 
Proc. Natl Acad. Sci. USA 38, 716–719 (1952).
100. Watkins, C. J. C. H. & Dayan, P. Q-learning. Mach. 
Learn. 8, 279–292 (1992).
101. Todorov, E. in Advances in Neural Information 
Processing Systems (eds Scholkopf, B., Platt, J. & 
Hofmann T.) 19, 1369–1376 (MIT Press, 2006).
102. Camerer, C. F. Behavioural studies of strategic thinking 
in games. Trends Cogn. Sci. 7, 225–231 (2003).
103. Smith, J. M. & Price, G. R. The logic of animal conflict. 
Nature 246, 15–18 (1973).
104. Nash, J. Equilibrium points in n-person games.  
Proc. Natl Acad. Sci. USA 36, 48–49 (1950).
105. Wolpert, D. M. & Miall, R. C. Forward models for 
physiological motor control. Neural Netw. 9,  
1265–1279 (1996).

106. Todorov, E. & Jordan, M. I. Smoothness maximization 
along a predefined path accurately predicts the speed 
profiles of complex arm movements. J. Neurophysiol. 
80, 696–714 (1998).
107. Tseng, Y. W., Diedrichsen, J., Krakauer, J. W., 
Shadmehr, R. & Bastian, A. J. Sensory prediction-
errors drive cerebellum-dependent adaptation of 
reaching. J. Neurophysiol. 98, 54–62 (2007).
108. Bays, P. M. & Wolpert, D. M. Computational  
principles of sensorimotor control that minimize 
uncertainty and variability. J. Physiol. 578, 387–396 
(2007).
A nice overview of computational principles in 
motor control. Its focus is on representing 
uncertainty and optimal estimation when  
extracting the sensory information required for 
motor planning.
109. Shadmehr, R. & Krakauer, J. W. A computational 
neuroanatomy for motor control. Exp. Brain Res. 185, 
359–381 (2008).
110. Verschure, P. F., Voegtlin, T. & Douglas, R. J. 
Environmentally mediated synergy between 
perception and behaviour in mobile robots. Nature 
425, 620–624 (2003).
111. Cohen, J. D., McClure, S. M. & Yu, A. J. Should I stay 
or should I go? How the human brain manages the 
trade-off between exploitation and exploration. Philos. 
Trans. R. Soc. Lond. B Biol. Sci. 362, 933–942 
(2007).
112. Ishii, S., Yoshida, W. & Yoshimoto, J. Control of 
exploitation-exploration meta-parameter in 
reinforcement learning. Neural Netw. 15, 665–687 
(2002).
113. Usher, M., Cohen, J. D., Servan-Schreiber, D., 
Rajkowski, J. & Aston-Jones, G. The role of locus 
coeruleus in the regulation of cognitive performance. 
Science 283, 549–554 (1999).
114. Voigt, C. A., Kauffman, S. & Wang, Z. G. Rational 
evolutionary design: the theory of in vitro protein 
evolution. Adv. Protein Chem. 55, 79–160 (2000).
115. Freeman, W. J. Characterization of state transitions in 
spatially distributed, chaotic, nonlinear, dynamical 
systems in cerebral cortex. Integr. Physiol. Behav. Sci. 
29, 294–306 (1994).
116. Tsuda, I. Toward an interpretation of dynamic neural 
activity in terms of chaotic dynamical systems. Behav. 
Brain Sci. 24, 793–810 (2001).
117. Jirsa, V. K., Friedrich, R., Haken, H. & Kelso, J. A.  
A theoretical model of phase transitions in the human 
brain. Biol. Cybern. 71, 27–35 (1994).
This paper develops a theoretical model (based on 
synergetics and nonlinear oscillator theory) that 
reproduces observed dynamics and suggests a 
formulation of biophysical coupling among brain 
systems.
118. Breakspear, M. & Stam, C. J. Dynamics of a  
neural system with a multiscale architecture. Philos. 
Trans. R. Soc. Lond. B Biol. Sci. 360, 1051–1074 
(2005).

119. Bressler, S. L. & Tognoli, E. Operational principles of 
neurocognitive networks. Int. J. Psychophysiol. 60, 
139–148 (2006).
120. Werner, G. Brain dynamics across levels of 
organization. J. Physiol. Paris 101, 273–279 (2007).
121. Pasquale, V., Massobrio, P., Bologna, L. L., 
Chiappalone, M. & Martinoia, S. Self-organization and 
neuronal avalanches in networks of dissociated cortical 
neurons. Neuroscience 153, 1354–1369 (2008).
122. Kitzbichler, M. G., Smith, M. L., Christensen, S. R. & 
Bullmore, E. Broadband criticality of human brain 
network synchronization. PLoS Comput. Biol. 5, 
e1000314 (2009).
123. Rabinovich, M., Huerta, R. & Laurent, G. Transient 
dynamics for neural processing. Science 321 48–50 
(2008).
124. Tschacher, W. & Hake, H. Intentionality in non-
equilibrium systems? The functional aspects of self-
organised pattern formation. New Ideas Psychol. 25, 
1–15 (2007).
125. Maturana, H. R. & Varela, F. De máquinas y seres 
vivos (Editorial Universitaria, Santiago, 1972).  
English translation available in Maturana, H. R. & 
Varela, F. in Autopoiesis and Cognition (Reidel, 
Dordrecht, 1980).
126. Fiorillo, C. D., Tobler, P. N. & Schultz, W. Discrete 
coding of reward probability and uncertainty by 
dopamine neurons. Science 299, 1898–1902 
(2003).
127. Niv, Y., Duff, M. O. & Dayan, P. Dopamine,  
uncertainty and TD learning. Behav. Brain Funct. 1, 6 
(2005).
128. Fletcher, P. C. & Frith, C. D. Perceiving is believing: a 
Bayesian approach to explaining the positive 
symptoms of schizophrenia. Nature Rev. Neurosci. 10, 
48–58 (2009).
129. Phillips, W. A. & Silverstein, S. M. Convergence of 
biological and psychological perspectives on cognitive 
coordination in schizophrenia. Behav. Brain Sci. 26, 
65–82 (2003).
130. Friston, K. & Kiebel, S. Cortical circuits for perceptual 
inference. Neural Netw. 22, 1093–1104 (2009).

Acknowledgments
This work was funded by the Wellcome Trust. I would like to 
thank my colleagues at the Wellcome Trust Centre for 
Neuroimaging, the Institute of Cognitive Neuroscience and the 
Gatsby Computational Neuroscience Unit for collaborations 
and discussions.

Competing interests statement
The author declares no competing financial interests.

SUPPLEMENTARY INFORMATION
See online article: S1 (box) | S2 (box) | S3 (box) | S4 (box) |  
S5 (box)

All liNks Are AcTive iN The oNliNe pdf

REVIEWS

> Figure description (generated): The provided image does not contain a figure; it contains text related to author disclosures and supplementary information.

The visible content is:
1. **Disclosure Statement:** "The author declares no competing financial interests."
2. **Supplementary Information Box:** A shaded box titled "SUPPLEMENTARY INFORMATION" containing the following text:
    * "See online article: S1 (box) | S2 (box) | S3 (box) | S4 (box) | S5 (box)"
    * "ALL LINKS ARE ACTIVE IN THE ONLINE PDF"

Since there is no visual data, schematic, plot, or diagram present, a detailed description of its structure, components, trends, or labels cannot be provided. The content is purely textual metadata regarding supplementary materials.

138 | FEBRuARy 2010 | voluME 11 
 www.nature.com/reviews/neuro

© 20
 Macmillan Publishers Limited. All rights reserved
10
