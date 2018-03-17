# Universal Value Function Approximators
32nd International Conference on Machine Learning, Lille, France, 2015

## observation
* Value functions are a core component of rein- forcement learning systems

## idea: UVFA
* to construct a single function approximator $V(s;\theta)$ that
  estimates the long-term reward from any state $s$, using parameters $\theta$
* universal value function approximators (UVFAs):  $V(s, g; \theta)$ that
  generalise not just over states s but also over goals g.
* efficient technique for **supervised learning** of UVFAs,
  * by factoring observed values into separate embedding vectors for state and goal, and
  * then learning a mapping from s and g to these factored embedding vectors.

## result
* suggest: UVFAs can be used
  * for transfer learning to new tasks with the same dynamics but different goals.
  * as features (the state embedding) to represent state
  * to generate temporally abstract options
  * a universal option model

## misc
* **General** value functions $V_g(s)$ (Sutton et al., 2011) represent the utility of any state s in 
  achieving a **given goal g** (e.g. a waypoint), represented by a **pseudo-reward** function that 
  takes the place of the real rewards in the problem.
* a **collection of value functions** can be used as a **predictive representation of state**, where 
  the predicted values themselves are used as a feature vector (Sutton & Tanner, 2005; Schaul & Ring, 2013).

## comment
* key is supervised learning (+ feature learning)
