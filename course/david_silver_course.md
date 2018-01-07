# [david_silver_course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

### 01: intro
* in engineering, rl is close to optimal control
* rl has similar principles with active learning,
where agent actions affect the subsequent data it receives
* most fundamental quantity: reward
* job is to maximise cumulative reward
* reward hypothesis:
all goals can be described by the maximisation of expected cumulative reward
* rl can handle multi-objective optimization as
it chooses action each time step,
and along the way it has to manage how to tradeoff several objectives
* state summarizes history (markov state), $S_t = f(H_t)$
* differentiate: environment state (may be partially observable) vs
agent state, $S^a_t = f(H_t)$
* markov assumption:
the future is independent of the past given the present,
or the state is a sufficient statistic of the future
* The environment state is always Markov
* mostly in this course full observability, i.e mdp
* stochastic policy $\phi(a|s) = P(a|s)$
* value function:
$v_\phi(s) = E_\phi[R_{t+1} + \lambda R_{t+2} + \ldots | S_t = s]$
* model at least predict the next state (transition distribution) and
the next reward, model is optional aka model-free
* rl agent taxonomy A:
a) value-based (policy is implicit),
b) policy-based (policy is explicit, work directly on the policy,
without storing value function)
c) actor-critic (store both policy and value function)
* rl agent taxonomy B:
a) model-free
b) model-based (first, build up the model, e.g dynamic model)
* two fundamental problems in sequential decision making
a) rl (the agent interacts with the environment,
the environment is initially unknown)
b) planning (given model, (without any external real interaction)

### 02: Markov Decision Processes
*  any pomdp problems can be converted to mdp
*  a state $S_t$ is Markov if $P(S_{t+1}|S_t) = P(S_{t+1}|S_1,\ldots,S_t)$
*  state transition matrix, each row sums to one, either stationary or non-stationary
*  A Markov process is a memoryless random process, i.e.
a sequence of random states $S_1 , S_2 , \ldots$ with the Markov property.
*  terminal state: absorbing state, self-loop
*  A Markov reward process is a Markov chain with values,
i.e. $<S,P,R,\lambda>$, where
$R$ is a reward function, $R_s = E[R_{t+1} | S_t = s]$
*  The return $G_t$ is the total discounted reward from time-step $t$, G for Goal,
$G_t = \sum_{k=0}^{\inf} R_{t+k+1}$,
no expectation here because $G$ is a random sample.
*  $\lambda \in [0,1]$
0: shortsighted (myopic), prefer reward now,
1: farsighted
*  why discounts:
math convenient (avoid infinite return),
future is more uncertain: Uncertainty about the future may not be fully represented,
*  if all sequences terminate, then undiscounted Markov reward processes are possible to use
*  value function $v(s) = E[G_t|S_t = s]$
*  bellman equ (is a linear equ),
The value function can be decomposed into two parts:
a) immediate reward $R_{t+1}$
b) discounted value of successor state $\lambda v(S_{t+1})$
*  analytical solution for Bellman is $O(n^3$ for $n$ states,
alternatives: iterative methods, e.g. dynamic programming, monte carlo evalution
*  A policy is a distribution over actions given states,
which fully defines the agent behaviour;
*  in MDP, policies are stationary (time-independent),
as policies depend on the current state, not history
*  given an MDP and a policy,
the transition prob: $P_(s,s')^{\phi} = \sum_{a \in A} \phi(a|s) P_{s,s'}^a$, and
reward function: $R_(s)^{\phi} = \sum_{a \in A} \phi(a|s) P_{s,s'}^a$
*  value func:
a) state-value function,
b) action-value function
*  value func: immediate reware plus a discounted value of next state
*  The optimal value function specifies the best possible performance in the MDP
*  Define a partial ordering over policies
$\phi \ge \phi' if v_{\phi}(s) \ge v_{\phi'}(s), \forall s$
*  There is always a deterministic optimal policy for any MDP
*  two step lookahead, for
a) action, that we choose
b) next state, where we end up with
*  Bellman Optimality Equation is non-linear, due to the max operator,
solve using iterative method
*  handling imperfect models:
a) explicitly represent the uncertainty on MDP: Bayesian RL
b) factor the uncertainty in MDP representation, i.e POMDP (?)
c) accept that the model is not perfect, then use variable discount factors
*  major extensions of MDP:
a) Infinite and continuous MDPs,
b) Partially observable MDPs,
c) Undiscounted, average reward MDPs

### 03: Planning by DP
* intro
  * planning vs rl: are just different problem setting
  * dynamic: sequential
  * programming: optimizing policy
  * dp is for problem with 2 props:
  a) optimal substructure
  b) overlapping subproblems
  * mdp satisfies both problem prob for dp:
  a) bellman provides recursive decomposition
  b) value fn stores and reuses solution
* policy iteration (policy iteration always converges to $\phi^star$):
Given a policy,
a)evaluate the given policy to obtain $v\phi$
b)improve the policy by acting greedily by$v_\phi$
* value iteration
* extension to DP
* policy eval:
  even with random policy, if we keep iterating V(s) (do one step lookahead)
  then we can end up with optimal policy (by behave optimally/greedily),
  which is greedy wrt the iterated V(s)
* policy iteration (always converge to phi^star)
  * given a policy
  * evaluate the given policy
  * improve the policy by acting greedily (deterministic)
* by acting greedily, we never act worse
* in mdp, there is always, at least one, deterministic optimal policy
* policy iter (applying bellman equ with one step look ahead) stops/converger
  when it satisfies bellman optimality equ,
  you can _not_ stop at the local max
* stopping condition in value iter loop:
  * epsilon-converge of value fn
  * stop after k iter
* value iter:
If we know the solution to subproblems v* (s')
Then solution v∗ (s) can be found by one-step lookahead
* value iter works on
  * on loopy mdp
  * even when there is no final state
* relationship:
  value iter vs policy iter?
  ans:
  Unlike policy iteration, there is no explicit policy,
  value fn directly iterate value fn,
  in value iter, the value fn may not equal to any V_phi of any phi
  value iter uses belman optimality equ
  policy iter uses belman expectaion equ (policy eval) + greedy policy improvement
* value iter: O(mn^2) for m actions and n states
  action-value iter: O(m^2 n^2)
* asynch dp:
  * in-place dp, leads to prioritized sweeping,
    backup states with the largest remaining bellman error
  * prioritized sweeping
  * real time dynamics programming:
    use real-experience (real states that the robot ends with) to select state to back up
* dp uses full-width backup

### 04:  Model-Free Prediction
* model-free prediction
    monte carlo learning
    TD
    TD(lambda)

* this class: model-free prediction (policy eval)
    estimate the value fn of unknown mdp given a policy

* monte carlo rl
    goal: learning value fn from episodes under a policy
    use empirical mean return, instead of expected return

* types: (best depends on the task domain)
  * first-visit monte carlo policy eval
  * every-visit monte carlo policy eval

* incremental mean:
  the mean of a seq can be computed incrementally

* incremental monte calo updates
  alpha as a constanst learning param to forget old episodes,
  useful when dealing with non-stationary env

* TD learns from incomplete episodes, by boostrapping (update a guess toward a guess)

* In TD, the error term:
  TDerror = (  R_{t+1} + \lambda V(S_{t+1}) - V(S_t)  )

* MC
    high variance, zero bias
    converges to solution with minimun squared-error
    does not exploit markov prop
    does not boostrap

  TD
    low variance, some bias
    converges to solution of max likehood markov model
    exploit markov property
    does bootstrap

* TD(lambda)
  Let TD target look n steps into the future,
  TD(0): n = 1
  which n is the best?

* TD-lambda, lambda return, lambda \in [0,1],
  use geometric weighting (due to memoryless property)
  combine multiple n-step episodes, n varies
  average n-step returns,
  like MC, can only be computed from complete episodes

* eligibility traces combines
 frequency and recency heuristic

* TD(lamda=0) is TD(0)
  TD(lamda=1) is MC

### 05: model-free control
* dychotomy:
  on policy: learn a policy phi from expericen sampled from phi
  off policy
* generalized policy iter with MC
  * need many episodes
  * exploration issue, due to always greedy
Greedy policy improvement over V (s) requires model of MDP
Greedy policy improvement over Q(s, a) is model-free
* epsilon-greedy
does guarantee that we have make progress: improve policy
* monte carlo policy iteration
  policy eval: using q
  policy improvement:  eps-greedy

* GLIE: greedy in the Limit with Infinite Exploration
eps-greedy is GLIE if eps reduces to zero, e.g. eps = 1/k
GLIE monte carlo control,
TD in control: SARSA (on-policy alg),

* n-step SARSA
SARSA(lambda)

* Monte carlo does not work in practice in off policy learning (the variace is huge),
  use TD instead for off policy learning

* Q learning (off policy)== SARSAMAX
  improve both behaviour and target policy

* policy eval:
  even with random policy, if we keep iterating V(s) (do one step lookahead)
  then we can end up with optimal policy (by behave optimally/greedily),
  which is greedy wrt the iterated V(s)

* policy iteration (always converge to phi^star)
  * given a policy
  * evaluate the given policy
  * improve the policy by acting greedily (deterministic)

* by acting greedily, we never act worse

* in mdp, there is always, at least one, deterministic optimal policy

* policy iter (applying bellman equ with one step look ahead) stops/converger
  when it satisfies bellman optimality equ,
  you can _not_ stop at the local max

* stopping condition in value iter loop:
  * epsilon-converge of value fn
  * stop after k iter

* value iter:
If we know the solution to subproblems v* (s')
Then solution v∗ (s) can be found by one-step lookahead

* value iter works on
  * on loopy mdp
  * even when there is no final state

* relationship:
  value iter vs policy iter?
  ans:
  Unlike policy iteration, there is no explicit policy,
  value fn directly iterate value fn,
  in value iter, the value fn may not equal to any V_phi of any phi
  value iter uses belman optimality equ
  policy iter uses belman expectaion equ (policy eval) + greedy policy improvement

* value iter: O(mn^2) for m actions and n states
  action-value iter: O(m^2 n^2)

* asynch dp:
  * in-place dp, leads to prioritized sweeping,
    backup states with the largest remaining bellman error
  * prioritized sweeping
  * real time dynamics programming:
    use real-experience (real states that the robot ends with) to select state to back up

* dp uses full-width backup

### 06: value func approx

* incremetal/online method
* batch method

* large problems:
  table loopup is not scalable, it is a special case of fn approx
  so fn approx (now, for value fn)
  plus, too slow to learn value of each individual states (fn approximator allows to generalize)

* \hat{v(s,w)} approx v_\phi(s),
with |w| << |S|

* approx arch:
state-value fn approx (supervised learning)
    s -> [nn/svm/gp/...] ->\hat{v}(s,w)
action-value fn appox
    s,a -> [nn/svm/gp/...] ->\hat{q}(s,a,w)
action-value fn appox 2
    s -> [nn/svm/gp/...] ->\hat{q}(s,a_1,w), \hat{q}(s,a_2,w), ..., \hat{q}(s,a_m,w)

* ml considerations (which fn approx):
  * differentialble  func approx:
    neural network
    linear combinations of feature
  * non-stationary
  * non iid

* stochastic gradient descent (sgd)
    obj = minimize the mean square error
    "stochastic" GD = samples the gradient

* linear value fn approx
    linear combination of features
    obj fn in quadratic in parameter
    SGD converges to global minimum (due to convex shape of quadratic obj fn)
    table lookup is a special case of linear value fn approx

* incremental prediction alg
    for MC, the target is the return
    for TD, the target is TD target, $R_{t+1} + \gamma \hat(v)(S_{t+1},w)$

* MC fn approx

* should we use eligibility traces in sarsa?

* TD on policy and off policy: may not converge in policy eval (prediction for non linear func approx

* Gradient TD fixes the problem with standard TD

* batch RL
  * nonbatch: see one example, update, throw away that sample
  * solution: least square via SGD with experience replay

* experience replay in deep Q network,
  * here NN is stable due to:
     experience replay: decorelate the data
     fixed/frozen Q-target (fixed old value, not the latest Q value)

* DQN in atari

* linear least square prediction
We do not know true values v t π
In practice, our “training data” must use noisy or biased samples of v t π
    LSMC
    LSTD
    LSTD(lambda)

* Least Squares Policy Iteration Algorithm

### 07: Policy Gradient Methods
* policy gradient
method that optimze policy directly
adjust the policy in the direction of gradient to make it better
directly paramaterize the policy
to be able to scale
use gradient ascent

* actor critic:
combines both value iter (value-based) and policy gradient

* phi_thate(s,a) = P (a|s.theta)

* Advantages:
Better convergence properties
Effective in high-dimensional or continuous action spaces
Can learn stochastic policies

* Disadvantages:
Typically converge to a local rather than global optimum
Evaluating a policy is typically inefficient and high variance

* rock-paper-scissor game
optimal behaviour: uniform random stochastic policy (nash equilibrium)

* alias-gridworld
optimal: stoc policy

* stoch policy is likely superior for POMDP,
POMDP: MDP when you use state func approx, where your state representetaion limit your view of state

* given a policy phi_theta(s,a) with param theta, find the best theta that max J_theta
in episodic: use the start value of the start state,
in continuing: use the average value over states
or average reward per time step

* Some approaches do not use gradient
Hill climbing
Simplex / amoeba / Nelder Mead
Genetic algorithms

* Greater efficiency often possible using gradient
Gradient descent
Conjugate gradient
Quasi-newton

* approx gradient
finite diff policy gradient

* AIBO soccer, aibo walk policy
peter stone
policy search

* policy is differentiable, at least, at point where you pick actions

* solving policy gradient analytically
score fn: using log .. related to likelihood ratio

* softmax policy
prob of action is proportional to exponentiated weights

* gaussian policy
common in cont action space

* policy gradient theorem
for any differentiable policy,
the gradient depends on  long term value Q_{phi_theta}(s,a)
monte carlo policy gradient: REINFORCE

* puck world example

* actor-critic method
    monte carlo gradient still has high variance
    use a critic to estimate the action-value function,
    The critic is policy evaluation

* qac: q actor critic

* reduce variance using baseline
A good baseline is the state value function

* critics at diff time scales

* natural policy gradient
* natural actor critic

### 08: integrated planning and learning
model:
something that describes transition dynamic T, and reward fn R
(here, assume S, A are known)
Typically assume conditional independence between state transitions and rewards

Advantages:
Can efficiently learn model by supervised learning methods
Can reason about model uncertainty

Disadvantages:
First learn a model, then construct a value function
two sources of approximation error

Examples of Model:
Table Lookup Model: use empirical counts
Linear Expectation Model
Linear Gaussian Model
Gaussian Process Model
Deep Belief Network Model
...

Table lookup:
  Model is an explicit MDP, P̂, R̂
  parametric:
    Count visits N(s, a) to each state action pair
  non parametric:
    At each time-step t, record experience tuple hS t , A t , R t+1 , S t+1 i
    To sample model, randomly pick tuple matching hs, a, ·, ·i

sample based planning
  Sample experience from model
  Apply model-free RL to samples

Performance of model-based RL is limited to optimal policy for approximate MDP
i.e. Model-based RL is only as good as the estimated model
When the model is inaccurate, planning process will compute a suboptimal policy
Solution 1: when model is wrong, use model-free RL
Solution 2: reason explicitly about model uncertainty

2 source of experience
true mdp (from world)
approx mdp (from model)

dyna-q with inaccurate model
env changes that make either easier or harder

planning via simulation based search
  Forward search paradigm using sample-based planning
  Simulate episodes of experience from now with the model
  Apply model-free RL to simulated episodes
    Monte-Carlo control → Monte-Carlo search
    Sarsa → TD search

forward search
  focus on MDP that starts right now (online planning principle)

game of go
  self play
  applying monte carlo tree seach
    Highly selective best-first search
    Evaluates states dynamically (unlike e.g. DP)
    Uses sampling to break curse of dimensionality
    Works for “black-box” models (only requires samples)
    Computationally efficient, anytime, parallelisable

temporal diff seach
  For model-free reinforcement learning, bootstrapping is helpful
    TD learning reduces variance but increases bias
    TD learning is usually more efficient than MC
    TD(λ) can be much more efficient than MC
  For simulation-based search, bootstrapping is also helpful
    TD search reduces variance but increases bias
    TD search is usually more efficient than MC search
    TD(λ) search can be much more efficient than MC search

Dyna-2
the agent stores two sets of feature weights
  Long-term memory
    updated from real experience using TD learning
  Short-term (working) memory
    is updated from simulated experience
Over value function is sum of long and short-term memories

### Comments:
* rl is essentially trial-and-error learning, the question then is
how much the accumulative reward is achieved eventually, and
how fast (how long) the agent achieves such rewards.
* david mostly applied in games, not robots :)
* rl begins with mdp and real world (no model, model-free),
whereas planning is from model (simulated world, model-based) and mostly pomdp
* agent state is equivalent to agent observation
* representation of state? consider deep RL
* david explains from
markov chain (mc) that contains state and transition prob,
markov reward (mr) = (mc + reward),
markov decision = (mr + action)

* multi agent RL?
* rl in pomdp?
* planning outputs stochastic policy?
