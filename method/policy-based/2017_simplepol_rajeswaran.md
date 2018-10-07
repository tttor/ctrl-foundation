2017_simplepol_rajeswaran.md
* nips2017: poseter
* https://sites.google.com/view/simple-pol
* https://papers.nips.cc/paper/7233-towards-generalization-and-simplicity-in-continuous-control

## problem
* the need for simplicity and generalization in RL
* The complexity of systems solvable with deepRL methods is not yet at the
  level of what can be achieved with trajectory optimization (planning) in simulation [5, 6, 7], or with
  hand-crafted controllers on physical robots (e.g. Boston Dynamics).
  * However, RL approaches are exciting because they are generic, model-free, and highly automated.
* When advances in a field are largely empirical in nature, it is important to understand the relative
  contributions of representations, optimization methods, and task design or modeling: both as a
  sanity check and to scale up to harder tasks.
* in line with Occam’s razor, the simplest
reasonable approaches should be tried and understood first. A thorough understanding of these factors
is unfortunately lacking in the community.

## idea
* What are the simplest set of ingredients needed to succeed in some of the popular benchmarks?
* Training with a diverse initial state
  distribution induces more global policies with better generalization.
  * the standard training and testing
  scenarios for these tasks are shown to be very limited and prone to over-fitting, thus
  giving rise to only trajectory-centric policies.
* Policy Architecture
  * Linear policy:
    * the policy mapping is $a_t \sim N(W s_t + b, \sigma)$, and the goal is to learn W , b, and σ
  * RBF policy

## setup
* compare with TRPO

## result
* policies with simple linear and RBF parameterizations can
  be trained to solve a variety of widely studied continuous control tasks, including
  the gym-v1 benchmarks.
  * The performance of these trained policies are **competitive**
    with state of the art results, obtained with more elaborate parameterizations such as
    fully connected neural networks.
* suggests that complex policy architectures should not be a default choice unless side-
  by-side comparisons with simpler alternatives suggest otherwise.

## comment
* note the word ``competitive``, then: does this simple representation scale?
* this seems not right
> Though we were able to train neural network policies that match the
results reported in literature, we have used publicly available prior results for an objective comparison.
