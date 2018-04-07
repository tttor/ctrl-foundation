# Reinforcement Learning: State-of-the-Art
* Wiering, Marco and van Otterlo, Martijn
* Springer Publishing Company, Incorporated, 2012

## 7: Reinforcement Learning in Continuous State and Action Spaces (Hado van Hasselt)
To update the parameters:
* gradient-based and
* gradient-free ways

This chapter covers:
* gradient-based temporal-difference learning,
* evolutionary strategies,
* policy-gradient algorithms and
* (natural) actor-critic methods.

Taxonomy of problems:
* the problem of control, which
means we want to find action-selection policies that yield high returns,
* the problem of prediction, which
aims to estimate the value of a given policy.

Methodologies to Solve a Continuous MDP
* Model Approximation:
Since S, A and $\gamma$ are assumed to be known,
this amounts to learning an approximation for the functions T and R.
Because of the Markov property, these functions only depend on local data.
The problem of estimating these functions then translates to a fairly standard supervised learning problem.
Learning the model may not be trivial, but in general it is easier than
learning the value of a policy or optimizing the policy directly.
However, if the accuracy of the model is debatable, the resulting policy may not be
better than a policy that is based directly on the samples that were used to construct the approximate model.
Even so, it may be easier to approximate the value directly than to infer the values from an approximate
model. For reasons of space, we will not consider model approximation further.
* Value Approximation.
* Policy Approximation.

next: 7.2 Function Approximation
p212

## 18: Reinforcement Learning in Robotics: A Survey
Reinforcement Learning in Robotics: A Survey

To apply reinforcement learning to behavior generation for real robots.
a particular focus of our chapter lies on
the choice between model-based and model-free as well as between value function-
based and policy search methods.

(a) The OBELIX robot is a wheeled mobile robot that learned to push
boxes (Mahadevan and Connell, 1992) with a value function-based approach (Picture reprint
with permission of Sridhar Mahadevan). (b) The Zebra Zero robot is a robot arm that learned a
peg-in-hole insertion task (Gullapalli et al, 1994) with a model-free policy gradient approach
(Picture reprint with permission of Rod Grupen). (c) The control of such autonomous blimps
(Picture reprint with permission of Axel Rottmann) was learned with both a value function
based approach (Rottmann et al, 2007) and model-based policy search (Ko et al, 2007). (d)
The Sacros humanoid DB learned a pole-balancing task (Schaal, 1997) using forward models
(Picture reprint with permission of Stefan Schaal).

Robotics is characterized by high dimensionality due to the many degrees of free-
dom of modern anthropomorphic robots. Experience on the real system is costly and
often hard to reproduce. However, it usually cannot be replaced by simulations, at
least for highly dynamic tasks, as even small modeling errors accumulate to sub-
stantially different dynamic behavior. Another challenge faced in robot reinforce-
ment learning is the generation of appropriate reward functions. Good rewards that
lead the systems quickly to success are needed to cope with the cost of real-world
experience but are a substantial manual contribution.
Many real-world problems in robotics are best represented with high-dimensional,
continuous states and actions. Every single trial run is costly.
A robot requires that the algorithm
runs in real-time and that it is capable of dealing with delays in the sensing and
execution which are inherent in physical systems

In fact, many of the methods that scale to more interesting tasks
are model-based (Atkeson et al, 1997; Abbeel et al, 2007) and often employ pol-
icy search rather than value function-based approaches (Gullapalli et al, 1994;
Miyamoto et al, 1996; Kohl and Stone, 2004; Tedrake et al, 2005; Peters and Schaal,
2008a,b; Kober and Peters, 2009).
Kaelbling et al (1996): "we must give up tabula rasa learning techniques and
begin to incorporate bias that will give leverage to the learning process"

18.2.1 Curse of Dimensionality:
In robotics, tasks with such problems are often made more accessible to the robot
engineer by shifting some of the complexity to a lower layer of functionality. In
the ball paddling example, we can simplify by controlling the robot in racket space
(which is lower-dimensional as the racket is orientation-invariant around the string’s
mounting point) with an operational space control law (Nakanishi et al, 2008). Many
commercial robot systems also encapsulate some of the state and action components
in an embedded control system (e.g., trajectory fragments are frequently used as
actions for industrial robots); however, this form of a state dimensionality reduction
severely limits the dynamic capabilities of the robot according to our experience
(Schaal et al, 2002; Peters et al, 2010b).
The reinforcement learning community has a long history of dealing with dimen-
sionality using computational abstractions. It offers a larger set of applicable tools
ranging from adaptive discretizations (Buşoniu et al, 2010) over function approxi-
mation approaches (Sutton and Barto, 1998) to macro actions or options (Barto and
Mahadevan, 2003). Macro actions would allow decomposing a task in elementary
components and quite naturally translate to robotics. For example, a macro action
“move one meter to the left” could be achieved by a lower level controller that takes
care of accelerating, moving, and stopping while ensuring the precision. Using a
limited set of manually generated macro actions, standard reinforcement learning
approaches can be made tractable for navigational tasks for mobile robots. How-
ever, the automatic generation of such sets of macro actions is the key issue in order
to enable such approaches

18.2.2 Curse of Real-World Samples:
to apply reinforcement learning in
robotics, safe exploration becomes a key issue of the learning process; a problem
often neglected in the general reinforcement learning community.
As the dynamics of a robot can change due to many external factors ranging
from temperature to wear, the learning process may never fully converge, i.e., it
needs a ‘tracking solution’ (Sutton et al, 2007).
For such reasons, real-world samples are expensive in terms of time, labor and,
potentially, finances. Thus, sample efficient algorithms that are able to learn from
a small number of trials are essential.

18.2.3 Curse of Real-World Interactions:
On physical systems there are always delays in sensing and actuation.
Usually the robot needs to
get commands at fixed frequency and for dynamic tasks the movement cannot be
paused. Thus, the agent has to select actions in real-time.
More critically there are also communica-
tion delays in the actuation as well as delays due to the fact that a physical cannot
instantly change its movement.

18.2.5 Curse of Goal Specification
Inverse reinforcement learning, also known as apprenticeship learning, is a
promising alternative to specifying the reward function manually. Instead, it as-
sumes that the reward function can be reconstructed from a set of expert demon-
strations.

Challenges in Robot Reinforcement Learning
* Curse of Dimensionality
* Curse of Real-World Samples
* Curse of Real-World Interactions
* Curse of Model Errors
* Curse of Goal Specification

in real-world domains the average reward is often more suitable than a discounted
formulation due to its stability properties (Peters et al, 2004). In order to incor-
porate exploration, the policy is considered a conditional probability distribution
π(s,a) = f(a|s,θ) with parameters θ .

Value function based approaches often do not translate well into high dimensional robotics as
proper representations for the value function become intractable and even finding the
optimal action can already be a hard problem. A particularly drastic problem is the
error propagation in value functions where a small change in the policy may cause
a large change in the value function which again causes a large change in the policy.
While this may lead faster to good, possibly globally optimal solutions, such a learn-
ing process is considerably more dangerous when applied on real systems where it is
likely to cause significant damage.

Policy search (the primal formulation) appears more natural to robotics.
* allows a natural integration of expert knowledge, e.g., through initializations of the policy.
* allows domain-appropriate pre-structuring of the policy in an approximate form
without changing the original problem.
* Optimal policies often have a lot less parameters than optimal value functions,
e.g., in linear quadratic control, the value function has quadratically many parameters
while the policy only requires linearly many parameters.
* Extensions to continuous state and action spaces follow straightforwardly.
* Local search in policy space can directly lead to good results as exhibited by
early hill-climbing approaches (Kirk, 1970).
* Additional constraints can be incorporated naturally

General reinforcement learning has yielded three kinds of policy search approaches that
have translated particularly well into the domain of robotics:
* policy gradients approaches based on likelihood-ratio estimation (Sutton et al, 2000),
REINFORCE (Williams, 1992)
* policy updates inspired by expectation maximization (Toussaint et al, 2010),
e.g., reward-weighted regression (Peters and Schaal, 2008a), PoWER (Kober and Peters,
2009), MCEM (Vlassis et al, 2009) and cost-regularized kernel regression (Kober
et al, 2010).
* the path integral methods (Kappen, 2005), PI 2 (Theodorou et al, 2010)

Policy search methods require a choice of policy representation that limits the number
of representable policies to enhance learning speed,

Having lower-dimensional states or actions eases most reinforcement learning prob-
lems significantly, particularly in the context of robotics.
Approaches: Hand Crafted, Learned from Data, Meta-Actions, Relational Representatio,

Function Approximation
* Neural networks as function approximators for continuous states
and actions have been used by various groups
* As neural networks are globally affected from
local errors, much work has focused on simply generalizing from neighboring cells.
* Locally weighted regression is known to be a particularly efficient function approximator
* Using GPs as function approximator for the value function

Prior knowledge can be included in the form of initial policies, initial models, or a predefined
structure of the task. These approaches significantly reduce the search space and,
thus, speed up the learning process.
* Prior Knowledge through Demonstrations:
Demonstrations by a Teacher, remote controlling the robot, kinesthetic teach-in (taking it by the hand and moving it), Demonstrations obtained by motion capture
* Prior Knowledge through Task Structuring
(Often a task can be decomposed hierarchically into basic components or
in a sequence of increasingly difficult tasks.):
Hierarchical Reinforcement Learning, Progressive Tasks.
* Directing Exploration with Prior Knowledge:

A popular approach is to combine simulations and
real evaluations by only testing promising policies on the real system and using it
to collect new data to refine the simulation

Model-free algorithms try to directly learn the value function or the policy. Model-
based approaches jointly learn a model of the system and the value function or the
policy.

In model-based:
If the learning methods require predicting the future or using derivatives, the
inaccuracies may accumulate quickly, and, thus, significantly amplify noise and er-
rors. These effects lead to value functions or policies that work well in the model
but poorly on the real system.
A solution is to overestimate the noise, to introduce a
controlled amount of inconsistency (Atkeson, 1998), or to use a crude model to find
a policy that compensates the derivative of the behavior in the model and on the real
system (Abbeel et al, 2006).

The idea of combining learning in simulation and in the real environment has been
popularized by the Dyna-architecture (Sutton, 1990) in reinforcement learning.

Bakker, B., Zhumatiy, V., Gruener, G., Schmidhuber, J.: Quasi-online reinforcement learning
for robots. In: IEEE International Conference on Robotics and Automation, ICRA (2006)

Nemec, B., Tamošiūnaitė, M., Wörgötter, F., Ude, A.: Task adaptation through exploration
and action sequencing. In: IEEE-RAS International Conference on Humanoid Robots,
Humanoids (2009)

Gräve, K., Stückler, J., Behnke, S.: Learning motion skills from expert demonstrations and
own experience using gaussian process regression. In: Joint International Symposium on
Robotics (ISR) and German Conference on Robotics, ROBOTIK (2010)

Kroemer, O., Detry, R., Piater, J., Peters, J.: Active learning using mean shift optimization for
robot grasping. In: IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS) (2009)
Kroemer, O., Detry, R., Piater, J., Peters, J.: Combining active learning and reactive control
for robot grasping. Robotics and Autonomous Systems 58(9), 1105–1116 (2010)

Pastor, P., Kalakrishnan, M., Chitta, S., Theodorou, E., Schaal, S.: Skill learning and task
outcome prediction for manipulation. In: IEEE International Conference on Robotics and
Automation (ICRA) (2011)

Wang, B., Li, J., Liu, H.: A heuristic reinforcement learning for robot approaching objects.
In: IEEE Conference on Robotics, Automation and Mechatronics (2006)

## 19: Conclusions, Future Directions and Outlook
Online planning:
* Monte Carlo Tree Search (MCTS)
* Model-based predictive control (MPC)

To use adaptive state partitioning to cluster similar states in an abstract
state, and to estimate transition probabilities between abstract states given some
discrete action. This approach may lead to models which do not obey the Markov
property anymore, and therefore it can make sense to combine them with memory
of previous states and actions.

Safe exploration and issues for real-time learning. When RL is applied directly
on robots or for controlling other physical devices, it would be very important that
the system is not damaged by the adaptive controllers that often learn without any
form of a-priori knowlegde, i.e., from Tabula Rasa. Also in the case of training RL
agents that interact with human users, it is not desirable that the RL agent explores
many actions so that the human user can be frustrated by the stupid actions of the
agent (Westra, 2011). Therefore, in such cases it may be necessary to combine RL
with pre-existing, safe, controllers. RL can then be used to change the output of the
controller in many circumstances, but the controller may also prevent the RL agent
from changing its generated actions.

19.2.1 Things That Are Not Yet Known:
* What is the best function approximator?
* Convergence proofs for general algorithms.
* Optimal exploration.
* Scaling up issues: to solve basically any control problem
* How does the brain do RL?

19.2.3 Interesting Directions
* Better world modelling techniques.
* Highly parallel RL.
* Combining RL with learning from demonstration.
* Novel queueing problems.
* RL for learning to play very complex games.

19.2.4 Experts on Future Developments
* Ashvin Shah:
autonomous development of useful abstractions and hierarchies so that re-
liance on prior knowledge and guidance can continue to be limited.
* Lucian Busoniu:
the scarcity of convincing benchmarks, especially in the
area of RL applied to physical systems, where RL is often still benchmarked on
problems that are simple and/or solvable by more classical techniques, such as the
car on the hill, inverted pendulum, or bicycle balancing. In this context of real-time
control of physical systems, a fundamental requirement that has to be addressed is
guaranteeing safety: the learning process must not damage the system or endanger
its users. The interplay between this requirement and exploration is expected to play
a key role here, as are control-theoretic insights such as those into the stability of
systems.
* Todd Hester:
will focus on algorithms that
are simultaneously sample efficient enough to work with limited data even in large,
continuous state spaces and computationally efficient enough to work in real time.
Model-based RL
* Lihong Li:
What we need is a mathematical theory on generalization for function approximation in RL.
* Ann Nowé:
multi-agent RL: in heterogeneous, unknown interactions.
* Frans Oliehoek:
to deepen our understanding of generalization and function approximation, especially in combination with feature selection methods.
The
problem with the notion of state and the associated Markov property is that they
trivialize the dynamic prediction problem. The curse of dimensionality is a direct
consequence of this and I believe that it can be mitigated by explicitly learning,
representing and exploiting the influence of state variables, features and actions on
each other.
* Jan Peters:
return back to the basic questions and solve these with more solid answers
as done in supervised learning, while working on better applications;
to look more at the primal problem
of RL (as done e.g., in (Peters et al, 2010)) and look how changes in the primal
change the dual.
* Shimon Whiteson:
will probably place an increasing emphasis on getting humans in the loop;
much remains to be done to exploit
developments from the field of human-computer interaction, better understand what
kinds of prior knowledge humans can express, and devise methods for learning from
the implicit and explicit feedback they can provide. The field of RL could benefit
from the development of both richer representations for learning and more practical
strategies for exploration;
In addition, even the most efficient strategies for exploration are
much too dangerous for many realistic tasks. An important goal is the development
of practical strategies for safely exploring in tasks with substantial risk of catas-
trophic failure.

## priority:
* 19 Conclusions, Future Directions and Outlook
* 18 Reinforcement Learning in Robotics: A Survey
* 11 Bayesian Reinforcement Learning
* 4 Learning and Using Models
* 7 Reinforcement Learning in Continuous State and Action Spaces
