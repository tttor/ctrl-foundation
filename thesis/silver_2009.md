# David Silver: Reinforcement Learning and Simulation-Based Search in Computer Go, 2009

Richard Sutton, Department of Computing Science, University of Alberta
Martin Müller, Department of Computing Science, University of Alberta
Csaba Szepesvari, Department of Computing Science, University of Alberta
Jonathan Schaeffer, Department of Computing Science, University of Alberta
Petr Musilek, Electrical and Computer Engineering, University of Alberta
Andrew Ng, Computer Science, Stanford University

### abs
* Learning and planning are two fundamental problems in artificial intelligence.
* learning:
  by RL, e.g. temporal diff learning
* planning:
    by simulation-based search, e.g. mcts
* introduce
    * temporal-difference search:
    that combines elements of both
    reinforcement learning and simulation-based search methods
    * the Dyna-2 architecture:
    which combines temporal-difference learning with temporal-difference search.
* apply to the game of 9 × 9 Go.

### ch 1: intro
So before we consider any broader challenges in artificial intelligence, and
attempt to tackle continuous action, continuous state, partially observable, and infinite horizon problems, perhaps we
should consider computer Go.

rl use:
it has been used to defeat human champions at
games of skill (Tesauro, 1994); in robotics, to fly stunt manoeuvres in robot-controlled helicopters
(Abbeel et al., 2007). In neuroscience it is used to model the human brain (Schultz et al., 1997); in
psychology to predict animal behaviour (Sutton and Barto, 1990). In economics, it is used to under-
stand the decisions of human investors (Choi et al., 2007), and to build automated trading systems
(Nevmyvaka et al., 2006). In engineering, it has been used to allocate bandwidth to mobile phones
(Singh and Bertsekas, 1997) and to manage complex power systems (Ernst et al., 2005).

thesis:
that an agent can both learn and plan effectively using reinforcement learning algorithms

contrib:
temporal-difference search algorithm
with the (fifth) idea of temporality

Using state abstraction, the value function can be approximated by a parameterised function
of the features, using many fewer parameters than there are states.

The idea of temporality
is to focus the agent’s representation on the current region of the state space – the subproblem it is
facing right now – rather than attempting to approximate the entire state space.

Bootstrapping provides a mechanism for reducing the variance of the agent’s
evaluation. Rather than waiting until the final outcome is reached, the idea of bootstrapping is to
make an evaluation based on subsequent evaluations.

in two-player games,
game-tree search algorithms such as alpha-beta search and Monte-Carlo tree search have achieved remarkable success

idea:
The value of each feature is learnt online, from many training games of self-play from the current position.

Monte-Carlo tree search suffers from a number of
serious deficiencies:
* The first time a position is encountered, its value is completely unknown.
* Each position is evaluated independently, with no generalisation between similar positions.
* Many simulations are required before Monte-Carlo can establish a high confidence estimate
of the value.
* The overall performance depends critically on the rollout policy used to complete simulations.

This thesis extends the core concept of Monte-Carlo search into a broader framework for simulation- based search, which specifically addresses these weaknesses:
* New positions are assigned initial values using a learnt, global evaluation function (Chapters
7, 8).
* Positions are evaluated by a linear combination of features (Chapters 6 and 7), or by general-
ising between the value of the same move in similar situations (Chapter 8).
* Positions are evaluated by applying temporal-difference learning, rather than Monte-Carlo, to
the simulations (Chapters 6 and 7).
* The rollout policy is learnt and optimised automatically by simulation balancing (Chapter 9).

### Chapter 2: Reinforcement Learning
This thesis is concerned primarily with fully observable tasks;
unless otherwise specified all states s are assumed to be Markov. It is also primarily concerned with
MDPs in which both the state space S and the action space A are finite.

Model-based reinforcement learning methods, such as dynamic programming, assume that the
dynamics of the MDP are known. Model-free reinforcement learning methods, such as Monte-Carlo
evaluation or temporal-difference learning, learn directly from experience and do not assume any
knowledge of the environment’s dynamics.

Value-based reinforcement learning algorithms use an iterative cycle of policy evaluation and policy improvement.

Bootstrapping is a general method for reducing the variance of an estimate, by updating a guess from a guess.

Temporal-difference learning is a model-free method for policy evaluation that bootstraps
the value function from subsequent estimates of the value function.

The idea of the TD(λ) algorithm is to bootstrap the value of a state from the subsequent values
many steps into the future. The parameter λ determines the temporal span over which bootstrapping
occurs. At one extreme, TD(0) bootstraps the value of a state only from its immediate successor.
At the other extreme, TD(1) updates the value of a state from the final return; it is equivalent to
Monte-Carlo evaluation.

To implement TD(λ) incrementally, an eligibility trace e(s) is maintained for each state:
accumulating eligibility trace,
replacing eligibility trace

The Sarsa algorithm (Rummery and Niranjan, 1994) combines temporal difference learning with
epsilon-greedy policy improvement. The action value function is evaluated by the TD(λ) algorithm. An
epsilon-greedy policy is used to combine exploration (selecting a random action with probability epsilon) with
exploitation (selecting argmax Q(s, a) with probability 1 − epsilon).

Similarly, Monte-Carlo control (Sutton and Barto, 1998) combines Monte-Carlo evaluation with
epsilon-greedy policy improvement

Monte-Carlo control is equivalent to the Sarsa algorithm with λ = 1 and updates applied offline after each episode (Sutton and Barto, 1998)

Instead of updating a value function, the idea of policy gradient reinforcement learning is to directly
update the parameters of the agent’s policy by gradient ascent, so as to maximise the agent’s aver-
age reward per time-step.

Policy gradient methods are typically higher variance and therefore less
efficient than value-based approaches, but they have three significant advantages. First, they are
able to directly learn mixed strategies that are a stochastic balance of different actions. Second, they
have better convergence properties than value-based methods: they are guaranteed to converge on a
policy that is at least locally optimal. Finally, they are able to learn a parameterised policy even in
problems with continuous action spaces.

Actor-critic algorithms combine the advantages of policy gradient methods with the efficiency of value-based reinforcement learning.
They consist of two components: an actor that updates the
agent’s policy, and a critic that updates the action value function.

approach to balancing exploration with exploitation:
epsilon-greedy, softmax policy, to apply the principle of optimism in the face of uncertainty: UCB1

### Chapter 3: Search and Planning
Most planning methods use a model of the environment.
* This model can either be solved directly, by applying model-based reinforcement learning methods (model-based planning), or
* indirectly, by sampling the model and applying model-free reinforcement learning methods (sample-based planning).

In sample-based planning
the agent samples experience from a model of the world: it simulates an action at each computational step, observes its consequences, and updates its policy. This symmetry between learning
and planning has an important consequence: algorithms for reinforcement learning can also become
algorithms for planning, simply by substituting simulated experience in place of real experience.

Sample-based planning requires a generative model that can sample state transitions and rewards. However, it is not necessary to know these probability distributions;
the next state and reward could, for example, be generated by a black box simulator. In complex
problems, such as large MDPs or two-player games, it can be much easier to provide a generative
model (e.g. a program simulating the environment or the opponent’s behaviour) than to describe the
complete probability distribution.

in sample-based planning:
Given a generative model, the agent can sample experience and receive a hypothetical reward.
The agent’s task is to learn how to maximise its total expected reward, from this hypothetical experi-
ence. Thus, each model specifies a new reinforcement learning problem, which itself can be solved
by model-free reinforcement learning algorithms.

### comments
* my work is, at least, David's in robotics (manipulation)
* the idea of the temporality is similar to that of online planning
* rl in partially observable states
* interesting taxonomy, in ch 2:
    * model-based planning, where the model is described in P(s'|s,a) and R(s,a)
    * sample-based planning, where the model is described as a generative model that can sample state transitions and rewards
* well, the taxonomy, model-based and sample-based planning, is not necessary or not accurate in the wording, becauase sample-based planning also uses a model, in this case, generative model that do not explicitly show T, and R, so perhaps, better to distinguish this as explicit and implicit transition and reward functions,
this becomes apparent in using physics engine in planning,
a) sample transition from the engine to recover/learn/estimate T, or
b) use it as generative model in every planning step
