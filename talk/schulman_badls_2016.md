# Deep Reinforcement Learning: Policy Gradients and Q-Learning
John Schulman,
Bay Area Deep Learning School,
(September 24, 2016)

Deep Reinforcement Learning:
Reinforcement learning using neural networks to approximate
functions
* Policies (select next action)
* Value functions (measure goodness of states or state-action pairs)
* Models (predict next states and rewards)

Summary of differences between RL and supervised learning:
* You don’t have full access to the function you’re trying to
optimize—must query it through interaction.
* Interacting with a stateful world: input x t depend on your
previous actions

Other methods worth investigating first, before applying deepRL
* Derivative-free optimization
  (simulated annealing, cross entropy method, SPSA)

Parameterized Policies:
* A family of policies indexed by parameter vector $\theta in R^d$
  * Deterministic:
    * $a = \pi(s, \theta)$
  * Stochastic:
    * $pi(a | s, \theta)$
* Analogous to classification or regression with input s, output a.
  * Discrete action space:
    * network outputs vector of probabilities
  * Continuous action space:
    * network outputs mean and diagonal covariance of Gaussian

Policy Gradient Methods:
* Score Function Gradient Estimator
  * Derivation via Importance Sampling
* using good trajectories (high R) as supervised examples in classification / regression
* Introduce Baseline:
  * increase logprob of action proportionally to how much returns are better than expected

Step sizes a big deal in RL
* Step too far → bad policy
* Next batch: collected under bad policy
* Can’t recover, collapse in performance!

Trust Region Policy Optimization:
* limit KL divergence between action distribution of
  pre-update and post-update policy
* Closely related to previous natural policy gradient methods

Further Variance Reduction
* Use value functions for more variance reduction (at the cost of bias): actor-critic methods
* Reparameterization trick: instead of increasing the
  probability of the good actions, push the actions towards (hopefully) better actions

the Current State of Affairs
* Policy gradient methods
  * Vanilla policy gradient (including A3C)
  * Natural policy gradient and trust region methods (including TRPO)
* Q-function methods
  * DQN and relatives: like value iteration, approximates B
  * SARSA: also found to perform well
* Comparison Q-fn vs policy-grad:
  * Q-function methods are more sample efficient when they work but
    don’t work as generally as policy gradient methods
  * Policy gradient methods easier to debug and understand
