# John Schulman 1 Deep Reinforcement Learning
* MLSS, May 2016, Cadiz
* goo.gl/5wsgbJ

* focus on
  * policy gradient,
  * deep rl,
    * rl using **nonlinear** fn approx
  * episodic setting:
    * goal: maximize expected reward per episode


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

<!--
Gerald Tesauro. “Temporal difference learning and TD-Gammon”. In: Communications of the ACM 38.3
(1995), pp. 58–68.
 -->
