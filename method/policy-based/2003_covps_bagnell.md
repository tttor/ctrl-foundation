# Covariant Policy Search
* J. Andrew Bagnell and Jeff Schneider

## problem
* non-covariant behavior of policy gradient reinforcement learning algorithms.
  * non-covariant; that is, a simple re-parameterization of the policy typically leads to a
    different gradient direction.

## observ
* The policy gradient approach is amenable
  to analysis by information geometric methods

## idea
* propose a natural metric on controller
parameterization that results from considering the
manifold of probability distributions over paths in-
duced by a stochastic controller.
  * leads to a covariant gradient ascent rule.
*  take a proper mani-
fold, the distribution over paths induced by the controller, and
compute a metric based on that.

## background
* Policy search has numerous advantages: do-
main knowledge may be easily encoded in a policy, the policy
may require less representational power than a value-function
approximation, there are simple extensions to the multi-agent
domain, and convergent algorithms are known.
