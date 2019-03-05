# schulman_2016

# abs
* goal:
  * making policy gradient methods more sample-efficient and reliable, especially
    when used with expressive nonlinear function approximators such as neural networks.
* how to ensure that policy updates lead to monotonic improvement, and
* how to optimally update a policy given a batch of sampled trajectories.
* propose: trust region policy optimization (TRPO), GAE

# 1: intro
* Deep learning is based on a simple recipe:
  * choose a loss function,
  * choose an expressive function approximator (a deep neural network), and
  * optimize the parameters with gradient descent.
* In reinforcement learning, we have two orthogonal choices:
  * what kind of objective to optimize (involving a policy, value function, or dynamics model), and
  * what kind of function approximators to use.

* A taxonomy of model-free RL algorithms
  * Policy optimization:
    view reinforcement learning as a numerical optimization problem where
    we optimize the expected reward with respect to the policy’s parameters.
    * derivative free optimization (DFO) algorithms:
      work by perturbing the policy parameters in many different ways,
      measuring the performance, and then moving in the direction of good performance.
      * cross-entropy method [SL06],
      * covariance matrix adaptation [WP09],
      * natural evolution strategies [Wie+08] (these three use Gaussian distributions); and
      * HyperNEAT, which also evolves the network topology [Hau+12].
      * evolutionary-based algorithms
    * policy gradient:
    are capable of optimizing much larger policies than DFO algorithms.
  * approximate dynamic programming (ADP).
    * value iter
    * policy iter
  * actor-critic methods:
    that combine elements from both policy optimization and dynamic programming.
* Stochastic policies have several advantages:
  * Even with a discrete action space, it’s possible to make an infinitesimal change to a
    stochastic policy. That enables policy gradient methods, which estimate the gradient
    of performance with respect to the policy parameters. Policy gradients do not make
    sense with a discrete action space.
  * We can use the score function gradient estimator, which tries to make good actions more probable.
  * The randomness inherent in the policy leads to exploration, which is crucial for
    most learning problems. On the other hand,
    stochastic policies explore poorly in many problems, and policy gradient methods
    often converge to suboptimal solutions.
* Simplifying the problem of reinforcement learning to a more well-understood kind of
  optimization with stochastic gradients, bring challenges:
  * Most prior applications of deep learning involve an objective where we have access
  to the loss function and how it depends on the parameters of our function approx-
  imator. On the other hand, reinforcement learning involves a dynamics model that
  is unknown and possibly nondifferentiable. We can still obtain gradient estimates,
  but they have high variance, which leads to slow learning.
  * In the typical supervised learning setting, the input data doesn’t depend on the
  current predictor; on the other hand, in reinforcement learning, the input data
  strongly depends on the current policy. The dependence of the state distribution
  on the policy makes it harder to devise stable reinforcement learning algorithms.
* this thesis develops policy optimization methods that are more stable and sample effi-
  cient than their predecessors and that work effectively when using neural networks as
  function approximators
  * after collecting a batch of data using the current policy, how should we update the policy?
    * trust region policy optimization (TRPO)
  * analyzes this credit assignment problem, and
    how we can reduce the variance of policy gradient estimation through the use of value functions.
    * GAE: generalized advantage estimation, with TRPO
  * to unify reinforcement learning and these other problems that involve optimizing expectations
    * the formalism of stochastic computation graphs,

# 2: background
The episodic setting of reinforcement learning:
where the agent’s experience is broken up into a series of episodes, i.e.
sequences with a finite number of states, actions and rewards.
The episode ends when a terminal state s T is reached.

In certain problem settings, we will also be concerned with an initial state distribution
μ(s), which is the probability distribution that the initial state $s_0$ is sampled from.

The goal is to find a policy that optimizes the expected total reward per episode.

The partially-observed setting is equivalent to the fully-observed setting because
we can call the observation history $h_t$ the state of the system.
That is, a POMDP can be written as an MDP (with infinite state space).
When using function approximation, the partially observed setting is
not much different conceptually from the fully-observed setting.

## 2.4 Policies
parameterized stochastic policies: $\pi_{\theta}(a|s)$;
$\theta \in \mathbb{R}^d$ is a parameter vector that specifies the policy.
So $max_{\pi} E[R | \pi]$ becomes $max_{\theta} E[R | \pi_{\theta}]$, i.e.
an optimization problem with respect to $\theta \in \mathbb{R}^d$.

The parameterization of the policy:
* With a discrete action space, we use a neural network that outputs
  action probabilities, i.e., the final layer is a softmax layer.
* With a continuous action space, we use a neural network that outputs
the mean of a Gaussian distribution, with a separate set of parameters
specifying a diagonal covariance matrix.

Since the optimal policy
in an MDP or POMDP is deterministic, we don’t lose much by using a simple action
distribution (e.g., a diagonal covariance matrix, rather than a full covariance matrix or a
more complicated multi-model distribution.)

## 2.5
Derivative-free optimization, e.g.
Cross entropy method (CEM) is a simple but effective evolutionary algorithm,
which works with Gaussian distributions, repeatedly updating the mean and
variance of a distribution over candidate parameters.

Policy gradient methods:
repeatedly estimating the gradient of the policy’s performance with respect to its parameters.

## 2.6 policy gradients
* The simplest way to derive them is to use the **score function gradient estimator**,
  a general method for estimating gradients of expectations
* in practice, we will generally choose the baseline to
  approximate the value function,

# 3: trust region policy optimization (TRPO)
* http://www.stat.yale.edu/~pollard/Books/1984book/pollard1984.pdf

## 3.1
To update the policy, we should improve a certain surrogate
objective as much as possible, while changing the policy as little as possible, where this
change is measured as a KL divergence between action distributions.

We show that by
bounding the size of the policy update, we can bound the change in state distributions,
guaranteeing policy improvement despite non-trivial step sizes

## 3.2 preliminaries

## 3.3
* principal theoretical result is
  * that the policy improvement bound in Equation (8) can
    be extended to general stochastic policies, rather than just mixture polices,
    by replacing α with a distance measure between π and π̃.
*  Note that for now, we assume exact evaluation of the advantage values

## 3.4
* In practice, if we used the penalty coefficient C recommended by the theory above, the
  step sizes would be very small. One way to take larger steps in a robust way is to use a
  constraint on the KL divergence between the new policy and the old policy, i.e., a trust
  region constraint

## 3.6
* Our theory ignores estimation error for the advantage function
  Kakade and Langford [KL02] consider this error in their derivation, and the same arguments would
  hold in the setting of this chapter, but we omit them for simplicity.

## 3.8
* used δ = 0.01 for all experiments.
* For the natural
  gradient method, we swept through the possible values of the stepsize in factors of three,
  and took the best value according to the final performance
* results provide empirical evidence that constraining the KL divergence is a more robust way to
  choose step sizes and make fast, consistent progress, compared to using a fixed penalty.

## 3.9
* proved monotonic improvement for an algorithm that repeatedly optimizes a
  local approximation to the expected return of the policy with a KL divergence penalty,
  and we showed that an approximation to this method that incorporates a KL divergence
  constraint achieves good empirical results on a range of challenging policy learning tasks,
  outperforming prior methods.

## 3.12
* to efficiently approximately solve the following constrained optimization problem,
  * (1) compute a search direction, using a
    linear approximation to objective and quadratic approximation to the constraint; and
  * (2) perform a line search in that direction, ensuring that we improve the nonlinear objective
    while satisfying the nonlinear constraint.

# 4: geralized advantage estimator (GAE)
Two main challenges with policy gradient methods:
* the large number of samples typically required, and
* the difficulty of obtaining monotonic improvement despite the nonstationarity of the incoming data.

GAE:
significantly
reduce variance of the policy gradient estimators while maintaining a tolerable level of bias

next: 4.2 preliminaries

# 5: stochastic computation graphs
Success of neural networks
* the simplicity of the backpropagation algorithm, which
  allows one to efficiently compute the gradient of any loss function defined as a composition of differentiable functions
* the backpropagation algorithm is only sufficient when the loss function is a deterministic,
  differentiable function of the parameter vector.
* convolutional neural networks in vision [LeC+98] and LSTMs for sequence data

a combination of stochastic and deterministic operations yields recent models of attention [Mni+14] and memory [ZS15]
* (1) likelihood maximization in probabilistic models with latent variables [Nea90; NH98], and
* (2) policy gradients in reinforcement learning [Gly90; Sut+99;Wil92].

# 6: conclusion
* stochastic computation graphs make the point that policy
  gradient methods for reinforcement learning are an instance of a more general class of
  techniques for optimizing objectives defined as expectations.
* Frontiers:
  * Shared representations for control and prediction.
  * Hierarchy: how to automatically learn these high-level actions, or
    what kind of optimization objective will encourage the policy to be more “hierarchical”.
  * Exploration:
    exploration methods that can be applied in challenging real-world settings such as robotics.
  * Using learned models to problems with high-dimensional state spaces.
  * Finer-grained credit assignment:
    to do better credit assignment with the help of a model of the system.

## comments
* ? sec 1.5: doubt on what the last sentence means?
> That enables policy gradient methods, which estimate the gradient
of performance with respect to the policy parameters. Policy gradients do not make
sense with a discrete action space.
* ? ch6: this seems not to use end-to-end from raw image to torque?
> "first, we need to map the raw input into more useful representations
(for example, parse the image into a set of objects andtheir locations);
second, we need to map these representations to the actions."
* ? ch6: Silver ever said: those local minima are likely as good as global minima in hi-dim param space;
> "Policy gradient methods are prone to converging to suboptimal policies, as we observed
many times while doing the empirical work in this thesis."
