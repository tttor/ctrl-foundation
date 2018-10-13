# Chapter 11 Off-policy Methods with Approximation

* in off-policy learning,
  * we seek to learn a value function for a target policy $\pi$,
    given data due to a different behavior policy b.
  * In the prediction case, both policies are static and given, and
    we seek to learn either state values or action values
  * In the control case,
    * action values are learned, and
    * both policies typically change during learning
      * $\pi$ being the greedy policy with respect to q̂, and
      * $b$ being something more exploratory
        such as the $\epsilon$-greedy policy with respect to $\hat{q}$.
*  challenge of off-policy learning with function approximation
  * because the distribution of updates in the off-policy case is
    not according to the on-policy distribution.
  * The on-policy distribution is important to
    the stability of semi-gradient methods.
  * Two general approaches have been explored to deal with this.
    * One is to use importance sampling methods again, this time to warp the
      update distribution back to the on-policy distribution, so that semi-gradient methods
      are guaranteed to converge (in the linear case).
    * The other is to develop true gradient
      methods that do not rely on any special distribution for stability.

# 11.1 Semi-gradient Methods
TODO

# 11.2
TODO

# 11.3 The Deadly Triad
* the deadly triad:
  the danger of instability and
  divergence arises whenever we combine all of the following three elements
  * fn approx
    * most clearly cannot be given up
  * Bootstrapping:
    * Update targets that include existing estimates (as in dynamic pro-
      gramming or TD methods) rather than relying exclusively on actual rewards and
      complete returns (as in MC methods).
  * Off-policy training
    * Training on a distribution of transitions other than that produced by the target policy.
    * Eg: Sweeping through the state space and updating all states
      uniformly, as in dynamic programming, does not respect the target policy
* the danger is
  * not due to control or to generalized policy iteration.
    * but the instability arises in the simpler prediction
      case whenever it includes all three elements of the deadly triad.
  * not due to learning or to uncertainties about the environment, because
    it occurs just as strongly in planning methods, such as dynamic programming,
    in which the environment is completely known.
* State aggregation or nonparametric methods whose complexity grows with data are
  **too weak or too expensive.**
* Least-squares methods such as LSTD are of quadratic complexity and are therefore too
  expensive for large problems
* Doing without bootstrapping is possible, at the cost of computational and data efficiency.
  * Perhaps most important are the losses in computational efficiency
  * The savings in communication and memory made possible by bootstrapping are great
  * The losses in data efficiency by giving up bootstrapping are also significant.
  * Bootstrapping often results in faster learning
    because it allows learning to take advantage of the state property, the ability to recognize
    a state upon returning to it
  * bootstrapping can impair learning on
    problems where the state representation is poor and causes poor generalization
* off-policy learning; can we give that up?
  * On-policy methods are often adequate.
    * For model-free reinforcement learning, one can simply use Sarsa rather than Q-learning.
  * off-policy learning is essential to other anticipated use cases
    * eg; the agent learns not just a single value function and single policy,
      but large numbers of them in parallel.

# 11.4 Linear Value-function Geometry
TODO

# 11.5 Gradient Descent in the Bellman Error
TODO

# 11.6 The Bellman Error is Not Learnable
TODO

# 11.7 Gradient-TD Methods
TODO

# 11.8 Emphatic-TD Methods
TODO

# 11.9 Reducing Variance
* Off-policy learning is inherently of greater variance than on-policy learning.
  * Eg:  You can’t expect to learn how to drive by cooking dinner
  * Only if the target and behavior policies are related,
    if they visit similar states and take similar actions, should
    one be able to make significant progress in o↵-policy training.
* The raison d’être of o↵-policy learning is
  * to enable generalization to this vast number of related-but-not-identical policies.
* The problem remains of how to make the best use of the experience.
  * that we have some methods that are stable in expected value
    (if the step sizes are set right), attention naturally turns to reducing the variance of the estimates.

# 11.10 Summary
* reason to seek off-policy algorithms
  * to give flexibility in dealing with the tradeo↵ between exploration and exploitation.
  * to free behavior from learning, and avoid the tyranny of the target policy.
* challenge of o↵-policy learning
  * correcting the targets of learning for the behavior policy
  * the instability of semi-gradient TD methods that involve bootstrapping.
