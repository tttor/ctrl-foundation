# Using Inaccurate Models in Reinforcement Learning
* Pieter Abbeel et al
* icml2006

## problem
* for high-dimensional continuous-state tasks, it can
be extremely difficult to build an accurate
model, and thus often the algorithm returns
a policy that works in simulation but not in
real-life. 
* model-free RL,
tends to require infeasibly large numbers of
real-life trials.

## idea
* to succes sively “ground” the policy evaluations using
real-life trials, but to rely on the approximate model to suggest local changes.

## result
* demonstrate that, when given only a crude model and a small number of real-life trials,
  our algorithm can obtain near-optimal performance in the real system.
