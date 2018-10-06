# An Empirical Analysis of Proximal Policy Optimization with Kronecker-factored Natural Gradients
* https://arxiv.org/abs/1801.05566

## problem
* Both PPO and ACKTR are state-of-the-art in their respective regimes
  * PPO obtains the advantage through the clipping objective function that can be easily optimized
  * ACKTR achieves higher performance through (an approximation of) natural gradient updates.
  * How would an algorithm perform if we combine the advantages of both fronts?

## idea
* PPOKFAC: combines the PPO objective and K-FAC natural gradient optimization
* perform a range of empirical analysis on various aspects of the algorithm, such as
  * sample complexity,
  * training speed, and
  * sensitivity to batch size and training epochs.
* adopt the trust region formulation of K-FAC and
  choose the learning rate according to the following schedule ...
  * decreases learning rate when the new policy seems to be deviating far from the old one, while
    increases learning rate with the new policy is too close.
* For the actor,
  * use the Fisher information matrix over the policy function
* For the critic,
  * use the Gauss-Newton matrix,
    (which is equivalent to the Fisher for a Gaussian observation model)
* the K-FAC optimizer takes in a single large batch and updates only once.
  * SGD: each batch consists of 2048 state-action pairs and is updated for 10 epochs with a minibatch of size 64
* PPOKFAC: consider the batch size schedule:
  * feeding the optimizers large batches at a time with fewer number of updates.
  * find that this has superior performance empirically than updating with minibatches
    * suggests that one K-FAC update is much more efficient than one SGD update

## setup
* report the mean of rewards of the last 100 episodes in training as a function of training timesteps
* use 4 and 10 million timesteps
* actor: uses Fisher information matrix over the policy function,
* critic: uses the Gauss-Newton matrix
* the ACKTR case, however, the K-FAC optimizer takes in a single large batch and
  updates only once.
  * aka fullbatch
* use Adaptive Selection of Learning Rate

## result
* PPOKFAC > PPOSGD
  * in terms of sample complexity and speed in a range of MuJoCo environments,
    while being scalable in terms of batch size.
  * PPO is with SGD with a fixed linear decaying learning-rate schedule
* PPOKFAC < ACKTR (A2C + KFAC)
* adding more epochs is not necessarily helpful for sample efficiency
* combining the advantages of both sides does not seem to improve sample complexity as expected;
  * the objective and optimization procedure that works for SGD does not necessarily work for K-FAC
  * the PPO objective implicitly defines a trust region through ratio clipping, and
    this overlaps with the learning rate selection criteria of ACKTR.
  * ACKTR takes much larger step-sizes than PPO and
    taking more iterations with such a step size might hurt performance (for example, in value function estimation).
* ACKTR performance is relatively stable under
  different batch sizes even at the same number of timesteps, which suggests that updates with larger batches
  are more efficient.

## background
* Policy gradient methods: current state-of-the-art
  (take different approaches to better sample efficiency)
  * Proximal Policy Optimization ( Schulman et al. [2017])
    * considers a particular “clipping” objective that mimics a trust-region,
    * penalizes the new policy to be far from the old policy without explicitly enforcing the trust region constraint.
    * optimized through stochastic gradients descent (PPO-SGD)
  * ACKTR [Wu et al., 2017].
    * considers approximated natural gradients that balances speed and optimization.

## comment
* ? Does not this make it is hard to converged?
> increases learning rate with the new policy is too close
* ? Does they separate actor and critic nets?
