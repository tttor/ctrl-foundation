# John Schulman 1 Deep Reinforcement Learning
* MLSS, May 2016, Cadiz
* goo.gl/5wsgbJ

* focus on
  * policy gradient,
  * deep rl,
    * rl using **nonlinear** fn approx
  * episodic setting:
    * goal: maximize expected reward per episode, `max E[R|theta]`


## taxonomy
* policy optimization
  * DFO (derivative free optimization) / Evolution
  * Policy gradients
* dynamic programming
  * policy iter
  * value iter
    * q learning
* hybrid: actor-critic
  * policy grad that use value fn

## def
* Markov Decision Process (MDP) defined by (S, A, P), where
* S: state space
* A: action space
* `P(r, s' | s, a)`: a transition probability distribution
* `\mu`: Initial state distribution
* `\gamma`: discount factor
* obj
  * max \nu(\theta) = E[r_0, r_1, ...,r_{T-1} | \pi]

## policy
* deterministic: `a = \pi(s)`
* stoc policy: `a \sim \pi(a|s)`
* parameterized policy: `\pi_{\theta}`,
  Analogous to classification or regression with input `s`, output `a`;
  eg: for neural network stochastic policies:
  * Discrete action space:
    * network outputs vector of probabilities
  * Continuous action space:
    * network outputs mean and diagonal covariance of Gaussian

## Derivative Free Optimization Approach
* Ignore all other information other than R collected during episode
* eg: Cross-Entropy Method,  Covariance Matrix Adaptation
  * Evolutionary algorithm
* Cross entropy
  * Initialize μ ∈ Rd , σ ∈ Rd
  * for iteration = 1, 2, . . . do
    * Collect n samples of θi ∼ N(μ, diag(σ))
    * Perform a noisy evaluation Ri ∼ θi
    * Select the top p% of samples (e.g. p = 20),..call the elite set
    * Fit a Gaussian distribution, with diagonal covariance, to the elite set,
      obtaining a new μ, σ.
  * Return the final μ

## policy grad
* intuition:
  * collect a bunch of trajectory
  * make the good traj more probable (bad ones less probable)
  * make the good actions more probable (actorcritic, GAE)
  * push the actions towards good actions
* for unbiased gradient estimator:
  * sample `x_i \sim p(x|\theta)`
  * compute gradient `\hat{g_i} = f(x_i) \nabla_{\theta} log p(x_i|\theta}`
    * need to be able to compute and differentiate density `p(x|\theta)` wrt `\theta`

* `\hat{g_i} = f(x_i) \nabla_{\theta} log p(x_i|\theta}`
  * `f(x)` measures how good the sample `x` is
  * Moving in the direction `\hat{g_i} ` pushes up the logprob of the sample,
    in proportion to how good it is
  * Valid even if f (x) is discontinuous, and unknown, or
    sample space (containing x) is a discrete set

* Now random variable x is a whole trajectory
  * Interpretation: using good trajectories (high R) as supervised
    examples in classification / regression

* Policy Gradient with Baseline
  * only pushes up the density for better-than-average `x_i`
  * Increase logprob of action at proportionally to how much
    returns are better than expected
  * Later: use value functions to further isolate effect of action, at the cost of bias

<!--
Gerald Tesauro. “Temporal difference learning and TD-Gammon”. In: Communications of the ACM 38.3
(1995), pp. 58–68.

John Schulman, Nicolas Heess, et al. “Gradient Estimation Using Stochastic Computation Graphs”. In:
Advances in Neural Information Processing Systems. 2015, pp. 3510–3522.
 -->
