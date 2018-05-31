# Integrating a Partial Model into Model Free Reinforcement Learning
* Aviv Tamar et al
* Journal of Machine Learning Research 13 (2012) 1927-1966
* http://www.jmlr.org/papers/volume13/tamar12a/tamar12a.pdf

## problem
* Model free RL algorithms typically operate without explicit knowledge of the underlying environment,
  * therefore, when such knowledge is available,
    using these algorithms ‘out of the box’ is clearly suboptimal
*  the concept of combining model free and model based
algorithms has received very little attention in the RL literature, and theoretical guarantees to its
advantages are lacking.

## observation
* Given the complementary advantages of both approaches,
  * we suggest a novel procedure which augments a model free algorithm with a partial model.
*  this dichotomy between algorithmic approaches, although
popular, is not necessarily desirable. As an example, consider a scenario where some parts of the
environment are known in advance, but computational resources are limited, restricting the use of
proper model based approaches.

## idea: Integrated Partial Model (IPM)
*  hybrid algorithm switches between a model based and a model
free mode, depending on the current state and the agent’s knowledge
* a hybrid approach applicable to cases where partial model infor-
mation is available in a specific form which we term partially known MDP
* provide a method for integrating such information into RL algorithms of the Stochastic Approximation (SA) type
*  to bound the term δθ, which is the error in the value function, and can be seen as
the total bias induced by the IPM method with the inaccurate model
* IPM Policy Gradient, IPM Q-learning

## result
*  Our method improves the asymptotic behavior of the algorithm, and at each iteration reduces the esti-
mation variance due to the uncertainty in the environment.
* We have proved mathematically (for TD(0)) and demonstrated in simulation (for Policy Gradient and Q-learning) an improvement in the algorithm’s overall performance.
* limitation
  * have not addressed the question of how the partially known model can be acquired
  * IPM method adds to the algorithm a computational cost of
    `O(Kmax)` evaluations of F (θn , xn , un, xn+1 ) at each iteration.

## background
* While it can be shown that both approaches, under mild conditions,
  asymptotically reach the same optimal policy
  on typical MDP’s, it is known that each approach possesses distinct merits.
