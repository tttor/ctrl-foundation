# Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation
* Yuhuai Wu, et al
* https://arxiv.org/abs/1708.05144

## problem
* neural networks (to represent control policies) are still trained using simple variants of stochastic gradient descent (SGD).
  * SGD and related first-order methods explore weight space inefficient
* a distributed approach leads to rapidly diminishing returns of sample efficiency as the degree of parallelism increases.
  * those approachesreduce training time by executing multiple agents to interact with the environment simultaneously
* the exact computation of the natural gradient is intractable because
  it requires inverting the Fisher information matrix.
* Trust-region policy optimization (TRPO) is impractical for large models and suffers from sample inefficien
  * it typically requires many steps of conjugate gradient to obtain a single parameter update, and
    accurately estimating the curvature requires a large number of samples in each batch;
* On Natural gradient: there still does not exist a scalable, sample-efficient, and
  general-purpose instantiation of the natural policy gradient.
* define the joint distribution of the policy and the value distribution by
  assuming independence of the two output distributions, i.e., `$p(a, v|s) = \pi(a|s) p(v|s)$`, and
  construct the Fisher metric with respect to `$p(a, v|s)$`,
* apply K-FAC to approximate the Fisher matrix to perform updates simultaneously.

## observation
* One way to effectively reduce the sample size is to use more advanced optimization techniques for gradient updates
* applying K-FAC to policy optimization could improve the sample efficiency of the current deep RL methods

## idea: Kronecker-factored trust region (ACKTR)
* extend the framework of natural policy gradient and
  propose to optimize **both the actor and the critic** using Kronecker-factored approximate curvature (K-FAC) with trust region
  * K-FAC to approximate the natural gradient update for actor-critic methods, with trust region optimization for stability
  * optimizing both the actor and the critic using natural gradient updates

## setup
* to avoid instability in training,
  it is often beneficial to use an architecture where the two networks share lower-layer representations but
  have distinct output layers
* in the Atari environments [4] and the MuJoCo [27] tasks

## result
* ACKTR substantially improves both sample efficiency and the final performance of the agent
  compared to the state-of-the-art on-policy actor-critic method A2C [18] and the famous trust region optimizer TRPO [22].
* the per-update computation cost of ACKTR is only 10% to 25% higher than SGD-based methods.

## misc
* Natural gradient methods follow the steepest descent direction that
  uses the Fisher metric as the underlying metric,
  a metric that is based not on the choice of coordinates but rather on the manifold (i.e., the surface).
* TRPO avoids explicitly storing and  inverting the Fisher matrix by using Fisher-vector products [21].
* Kronecker-factored approximated curvature (K-FAC)
  * each update is comparable in cost to an SGD update, and
  * it keeps a running average of curvature information, allowing it to use small batches.
* The method of natural gradient constructs the norm using the Fisher information matrix F,
  a local quadratic approximation to the KL divergence.
  * This norm is independent of the model parameterization `\theta` on the class of probability distributions,
    providing a more stable and effective update.
  * However, since modern neural networks may contain millions of parameters,
    computing and storing the exact Fisher matrix and its inverse is impractical, so we have to resort to approximations.
  * Kronecker-factored approximate curvature (K-FAC) [16] uses
    a Kronecker-factored approximation to the Fisher matrix to perform efficient approximate natural gradient updates.
* natural gradient performed with SGD-like updates can result in large updates to the policy, causing
  the algorithm to prematurely converge to a near-deterministic policy.
  * advocate instead using a trust region approach, whereby
    the update is scaled down to modify the policy distribution (in terms of KL divergence) by at most a specified amount.
