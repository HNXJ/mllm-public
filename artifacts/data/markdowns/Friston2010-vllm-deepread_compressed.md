## 

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
resist a natural tendency to disorder3-6. What follows is 
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
constantly changing environment3-6. From the point 
of view of the brain, the environment includes both 
the external and the internal milieu. This maintenance 
of order is seen at many levels and distinguishes bio-
logical from other self-organizing systems; indeed, the 
physiology of biological systems can be reduced almost 
entirely to their homeostasis7. More precisely, the rep-
ertoire of physiological and sensory states in which an 
organism can be is limited, and these states define the 
organism's phenotype. Mathematically, this means that 
the probability of these (interoceptive and exterocep-
tive) sensory states must have low entropy; in other 
words, there is a high probability that a system will 
be in any of a small number of states, and a low prob-
ability that it will be in the remaining states. Entropy 
is also the average self information or 'surprise'8 
(more formally, it is the negative log-probability of an 
outcome). Here, 'a fish out of water' would be in a sur-
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
through each of these theories - optimization. Furthermore, if we look closely at what is 
optimized, the same quantity keeps emerging, namely value (expected reward, expected 
utility) or its complement, surprise (prediction error, expected cost). This is the quantity that 
is optimized under the free-energy principle, which suggests that several global brain 
theories might be unified within a free-energy framework.

REVIEWS

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

---

## 

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
(Or 'approximating conditional 
density'.) An approximate 
probability distribution of the 
causes of data (for example, 
sensory input). It is the product 
of inference or inverting a 
generative model.

In short, the long-term (distal) imperative - of main-
taining states within physiological bounds - translates 
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
solve many inference and learning problems12-14. In this 
setting, surprise is called the (negative) model evidence. 
This means that minimizing surprise is the same as 
maximizing the sensory evidence for an agent's exist-
ence, if we regard the agent as a model of its world. In 
the present context, free energy provides the answer to

Box 1 | The free-energy principle

Part a of the figure shows the dependencies among the 
quantities that define free energy. These include the 
internal states of the brain μ(t) and quantities describing its 
exchange with the environment: sensory signals (and their 
motion) s˜(t) = [s,s′,s″...]T  plus action a(t). The environment 
is described by equations of motion, which specify the 
trajectory of its hidden states. The causes ϑ ⊃ {x˜, θ, γ } of 
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
seen by expressing the free energy as surprise -In p(s˜,| m) plus a Kullback-Leibler divergence between the recognition and 
conditional densities (encoded by the 'internal states' in the figure). Because this difference is always positive, minimizing 
free energy makes the recognition density an approximate posterior probability. This means the agent implicitly infers or 
represents the causes of its sensory samples in a Bayes-optimal fashion. At the same time, the free energy becomes a tight 
bound on surprise, which is minimized through action.

optimizing action
Acting on the environment by minimizing free energy enforces a sampling of sensory data that is consistent with the 
current representation. This can be seen with a second rearrangement of the free energy as a mixture of accuracy and 
complexity. Crucially, action can only affect accuracy (encoded by the 'external states' in the figure). This means that  
the brain will reconfigure its sensory epithelia to sample inputs that are predicted by the recognition density - in other 
words, to minimize prediction error.

REVIEWS

This figure is a conceptual block diagram illustrating the relationship between different components of the Free-Energy Principle, divided into two main panels, **(a)** and **(b)**.

## 

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
ply that of the agent's own recognition density. Third, it 
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
difference between the prior density - which encodes 
beliefs about the state of the world before sensory data are 
assimilated - and posterior beliefs, which are encoded 
by the recognition density. Accuracy is simply the sur-
prise about sensations that are expected under the recog-
nition density. This formulation shows that minimizing 
free energy by changing sensory data (without changing 
the recognition density) must increase the accuracy of 
an agent's predictions. In short, the agent will selectively 
sample the sensory inputs that it expects. This is known 
as active inference16. An intuitive example of this process 
(when it is raised into consciousness) would be feeling 
our way in darkness: we anticipate what we might touch 
next and then try to confirm those expectations.

In summary, the free energy rests on a model of how 
sensory data are generated and on a recognition density 
on the model's parameters (that is, sensory causes). Free 
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
idea is that the brain has a model of the world18-22 that 
it tries to optimize using sensory inputs23-28. This idea is 
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
zation problem11-14. This has furnished some powerful 
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
arrangement of cortical sensory areas32-34.

REVIEWS

NATuRE REvIEWs | NeuroscieNce 
 voluME 11 | FEBRuARy 2010 | 129

© 20
 Macmillan Publishers Limited. All rights reserved

---

## 

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
- g(μ ))
(i - 1)

ξx

(i) = Πx

(i)
= Πx

(i)
(i)
εx

(i)
(Dμx - f(μ ))
(i )

The second issue is the form of the recognition den-
sity that is encoded by physical attributes of the brain, 
such as synaptic activity, efficacy and gain. In general, 
any density is encoded by its sufficient statistics (for exam-
ple, the mean and variance of a Gaussian form). The way 
the brain encodes these statistics places important con-
straints on the sorts of schemes that underlie recognition: 
they range from free-form schemes (for example, particle 
filtering26 and probabilistic population codes35-38), 
which use a vast number of sufficient statistics, to sim-
pler forms, which make stronger assumptions about 
the shape of the recognition density, so that it can be 
encoded with a small number of sufficient statistics. The 
simplest assumed form is Gaussian, which requires only 
the conditional mean or expectation - this is known 
as the Laplace assumption39, under which the free energy 
is just the difference between the model's predictions 
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

Y


U I
Z
X
 θ

\


Z · 
K H
Z
KX
K θ
K
Y
K
X
Ks I
Z
KX
K θ
K
\
K
...
...

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

This figure presents a schematic diagram illustrating the concept of hierarchical message passing within the brain, divided into two main conceptual sections: a general circuit diagram and associated mathematical equations.

## 

a  Perceptual inference

b  Perceptual categorization

c

0.2
0.4
0.6
0.8

-20

-10

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

1.5

2.5

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
of neuronal responses53-56. This principle is extremely 
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
synthetic syrinx to produce 'chirps' that were modulated in amplitude and frequency (an 
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
synthetic syrinx to produce 'chirps' that were modulated in amplitude and frequency (an 
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

This figure presents a set of plots illustrating the perceptual inference of underlying causal states from simulated birdsong stimuli. The overall structure consists of a single, large graph area containing multiple overlaid time-series plots and annotations.