# Planning
We plan with respect to the given model.
In the context of RL, planning is part of model-based RL, where
we learn the model and plan with respect to the learned model, 
see also 
[ref](https://www.quora.com/What-is-the-difference-between-reinforcement-learning-and-planning),
[ref2](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/dyna.pdf).
Typically in planning, the model refers to the POMDP model consisting of 7 components: `$(S, A, T, R, O, Z, \lambda)$`.

There are two (+ 1 hybrid) approaches in POMDP planning,
* offline
  * plan before execution.
  * consider all contingencies.
  * does not scale up well.
* online planners
  * interleave planning with execution.
  * typically plans each step from the current belief.
    * potentially can handle large-scale planning.
* hybrid: combination of both online and offline planning approaches.

## online planning
DESPOT_2017, POMCP_2010, AEMS_2007, ...
Real-Time Dynamic Programming (RTDP-BEL)~\cite{Geffner1998},
Real-Time Belief Space Search (RTBSS)~\cite{Paquet2005},
Randomized Belief-Space Replanning (RBSR)~\cite{Hauser2010},
Planning under uncertainty with macro-actions (PUMA)~\cite{He2010},
SOVI: Simple Online Value Iteration~\cite{Shani2005},
Factored Hybrid Heuristic Online Planning (FHHOP)~\cite{Zhang2012}.

## offline planning
SARSOP, PBVI_2003, Perseus_2005, HSVI, ...
(most are point-based approaches that
sample belief states by simulating some random interactions of the agent
with the environment and then maintain at most one $\alpha$-vector per sampled belief state)

## combining offline and online planning approaches,
By using policies computed offline
* as macro actions to shorten the search horizon or
* as default policies at the leaves of the search tree in online planning or
* to provide (tight) lower and upper bounds (as heuristics) used in online search.

Most offline methods used in combination with online methods are based on approximation in that
they use the underlying MDP (the $(S, A, T, R)$ components of the POMDP model) to
compute lower bounds (e.g. Blind policy, point-based algorithms) and
upper bounds (e.g. MDP, QMDP, FIB) on the exact value function.

## bayesian framework
The Bayesian framework is used in POMDP planning whenever there is uncertainty in the POMDP model itself.
For example, uncertain (and unknown) transition probabilities.
Since the world model is not given (the agent has to build the model from scratch),
the exploitation-exploration balance is more significant here.
This is also formulated in some other fields, including
``optimal learning''\footnote{http://optimallearning.princeton.edu/} and
``dual control'', whose the controller's objectives are twofold:
(1) Action: To control the system as well as possible based on current system knowledge
(2) Investigation: To experiment with the system so as to learn about its behavior and control it better in the future.

In Bayesian framework, one needs to specify prior distribution.
Afterwards, we calcute the posterior based on prior and current observation.

Bayes-based (PO)MDP is also studied in the field of model-based reinforcement learning.
Some use the term ``planning'' (to denote decision making processes) once the model is obtained, even if the model remains uncertain.
The model here provides a way to access or sample the dynamics of the environment so that trajectories can be internally simulated.
