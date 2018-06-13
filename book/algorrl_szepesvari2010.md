# Algorithms for Reinforcement Learning
* Csaba Szepesvári
* 2010 by Morgan & Claypool

## abstract
Distingushing factors of reinforcement learning from supervised learning:
* only partial feedback is given to the learner about the learner’s predictions.
* the predictions may have long term effects through influencing the future state of the controlled system;
  time plays a special role

## preface
Standard approach to ‘solve’ MDPs is to use dynamic programming:
* transforms the problem of finding a good controller into the problem of finding a good value function.
* not scalable

Key ideas:
* to use samples to compactly represent the dynamics of the control problem
  * allows one to deal with learning scenarios when the dynamics is unknown.
  * even if the dynamics is available, exact reasoning that uses it might be intractable on its own
* to use powerful function approximation methods to compactly represent value functions
  * allows dealing with large, high-dimensional state- and action-space

This book:
* MDP
* only for the total expected discounted reward criterion.
  (widely used and the easiest to deal with mathematically)

Types of reinforcement problems and approaches.
* prediction
* control
  * value iter
  * policy iter
  * policy search

## ch 2: Value Prediction Problems
### 2.1 temporal difference learning in finite state spaces
* TD learning uses bootstrapping: predictions are used as targets during the course of learning.
* TD(λ): algorithm that unifies TD learning and (vanilla) Monte-Carlo methods

#### 2.1.1 tabular td(0)
TODO

### 3.1 a catalog of learning problems
Types of reinforcement problems
* interaction
  * active learning
  * online learning
* no interaction

In planning, primary concern:
* running time
* memory requirements

### 3.4 actor-critic methods
Actor-critic methods implement **generalized** policy iteration (GPI)
* recall: (**perfect**) policy iteration works by alternating between
  a complete policy evaluation and a **complete** policy improvement step

GPI:
* Algorithms that update the policy before it is completely evaluated,
* with two closely interacting processes
  * actor: aims at improving the current policy
  * critic: evaluates the current policy (thus helping the actor.)
* may generate a policy that is sub-stantially worse than the previous one.
  * Thus, the quality of the sequence of generated policies may oscillate or
    even diverge when the policy evaluation step is incomplete, irrespective of
    whether policy improvement is exact or approximate

The policy that is used to generate the samples (i.e., the **behavior policy**) could be different from
the one that is evaluated and improved in the actor-critic system (i.e., the **target policy**).
* This can be useful because the critic must learn about actions not preferred by the current target policy
  so that the critic can improve the target policy.
* the target policy is usually a stochastic policy.
* the behavior policy often mixes a certain (small) amount of exploration into the target policy.

#### 3.4.1 implementing a critic
the critic:
* to estimate the (action) value of the current target policy of the actor
  (so this is a value prediction problem)

##### SARSA
* use of the current State, current Action, next Reward, next State, and next Action
* When $\pi$ is fixed, SARSA is just TD(0) applied to state-action pairs.
* extension: SARSA(\lamda)

##### LSTD-Q(λ)
TODO

#### 3.4.2 implementing an actor
Policy improvement can be implemented in two ways:
* to move the current policy towards the **greedy policy** underlying
  the approximate action-value function obtained from the critic
* to perform gradient ascent directly on the performance surface underlying
  a chosen parametric policy class.

##### Greedy improvements
* to let the critic evaluate the current policy based on a lot of data and then
  switch to the policy that is greedy with respect to the obtained action-value function

##### Policy gradient
* perform stochastic gradient ascent on the performance surface induced by
  a smoothly parameterized policy class of stochastic stationary policies.

## ch4: For Further Exploration
## 4.1 further reading
* off-line planning in the worst-case can scale exponentially with the dimensionality of the state space
* online planning (i.e., planning for the “current state”) can break the curse of dimensionality by
  amortizing the planning effort over multiple time steps

## 4.2 applications
* http://www.cs.ualberta.ca/~szepesva/RESEARCH/RLApplications.html
* http://umichrl.pbworks.com/Successes-of-Reinforcement-Learning.

## 4.3 software
RL-Glue and RL-Library packages;
other RL software packages are CLSquare, PIQLE, RL Toolbox, JRLF and LibPG.
