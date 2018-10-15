# Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation
* Yuhuai Wu, et al
* nips2017: poster
* https://papers.nips.cc/paper/7112-scalable-trust-region-method-for-deep-reinforcement-learning-using-kronecker-factored-approximation
* https://arxiv.org/abs/1708.05144
* https://blog.openai.com/baselines-acktr-a2c/
* https://github.com/openai/baselines/tree/master/baselines/acktr # tf
  * https://github.com/tttor/baselines/tree/study-acktr/baselines/acktr
* https://github.com/ikostrikov/pytorch-a2c-ppo-acktr/blob/master/algo/a2c_acktr.py
* https://github.com/openai/baselines-results
* https://github.com/emansim/acktr
* https://www.youtube.com/watch?v=0rrffaYuUi4
* https://www.youtube.com/watch?v=gtM87w1xGoM
* https://www.reddit.com/r/MachineLearning/comments/6uk1q8/r_openai_baselines_acktr/

## problem
* still does **not exist** a scalable, sample-efficient, and
  general-purpose instantiation of the **natural** policy gradient.
  * SGD and related first-order methods explore weight space inefficiently
  * TRPO is **impractical for large models** and suffers from sample inefficiency
    * requires **many steps of conjugate gradient** to obtain a single parameter update, and
    * accurately estimating the curvature requires a large number of samples in each batch;
* computational challenges when applying **natural** gradient methods:
  * mainly associated with efficiently storing the Fisher matrix as well as computing its inverse.
  * example solution
    * for tractability:
      to use the compatible function approximator (a linear function approximator).
    * to avoid the computational burden:
      TRPO approximately solves the linear system using conjugate gradient with
      fast Fisher matrix-vector products, BUT
      * requires repeated computation of Fisher vector products,
        preventing it from scaling to the larger architectures typically used in
        experiments on learning from image observations in Atari and MuJoCo.
      * requires a large batch of rollouts in order to accurately estimate curvature.
      * generally less sample efficient
        (although TRPO shows better per-iteration progress than
        policy gradient methods trained with first-order optimizers such as Adam)

## observation
* to effectively reduce the sample size (improve the sample efficiency)
  * to use more advanced optimization techniques for gradient updates
    * applying K-FAC to policy optimization

## idea: actor-critic Kronecker-factored trust region (ACKTR)
* to optimize **both the actor and the critic** using
  Kronecker-factored approximate curvature (K-FAC) **with trust region**
  * applying a natural gradient update **to the critic**
    * previously, a **natural** gradient update **only to the actor**
    * assume the output of the critic is defined to be a Gaussian distribution
  * K-FAC to approximate the natural gradient update for actor-critic methods
    * to extend the natural policy gradient algorithm to optimize value functions
      via **Gauss-Newton approximation**
  * with trust region optimization for stability.
    * because: Schulman et al. [22] observed that SGD-like update rule can result in large updates
      to the policy, causing the algorithm to prematurely converge to a near-deterministic policy
  * use the factorized Tikhonov damping approach
* define the joint distribution of the policy and the value distribution by
  assuming independence of the two output distributions, i.e., $p(a, v|s) = \pi(a|s) p(v|s)$, and
  construct the Fisher metric with respect to $p(a, v|s)$,
* apply **K-FAC to approximate the Fisher matrix** to perform updates simultaneously.
* assume the output of the critic v is defined to be
  a Gaussian distribution p(v|st ) ∼ N (v; V (st), σ 2 ).
  * The Fisher matrix for the critic is defined with respect to this Gaussian output distribution.
  * In practice, we can simply set σ to 1, which is equivalent to the vanilla Gauss-Newton method

## setup
* advantage function as
  * the k-step returns with function approximation,
* discrete ctrl: Atari env
  * 6 games: Beamrider, Breakout Pong, Q-bert, Seaquest, Space Invaders
  * to avoid instability in training:
    use an architecture where the **two networks share lower-layer** representations but
    have **distinct output layers**
* continuous ctrl: MuJoCo env
  * 6 tasks
  * input
    * low-dimensional state-space representation
    * directly from pixel representation
  * **separating the policy and value function networks** resulted in
    better empirical performance in both ACKTR and A2C
* baselines
  * A2C: a synchronous and batched version of A3C
  * TRPO [22]
* eval metric:
  * plot episode reward vs number of timesteps
    * to show sample efficiency: i.e., speed of convergence per number of timesteps
    * shaded region denotes the standard deviation over 2 (Atari) and 3 (Mujoco) random seeds.
  * table: rewards col, #episode col
    * present the mean of rewards of the last 100 episodes in training for 50 million timesteps,
      as well as the number of episodes required to achieve human performance [17]
  * table:
    * row: method
    * col: env (atari, mujoco)
    * cell: timesteps per second
  * plot: with different batch size
* actor/policy network:
  * Gaussian MLP
  * The log standard deviation of a Gaussian policy was parameterized as a
    bias in a final layer of policy network that didn’t depend on input state
* critic/value network:
  * to minimize the squared
    difference between the bootstrapped k-step returns $\hat{R}_t$ and the prediction value
  * [in: 28] --wh1--> [h1: 64] --wh2--> [h2: 64] --whfinal--> [out:1]
  * MLP (fully connected, dense)
  * predict Advantage values, not Q values
    * advantage fn is defined as k-step returns with fn approx
  * https://www.tensorflow.org/api_docs/python/tf/nn/elu
* multi-threading is for optimization (network operations), not for rollout
  * https://www.tensorflow.org/api_docs/python/tf/train/QueueRunner
  * https://www.tensorflow.org/api_docs/python/tf/train/Coordinator
* observation filter is crucial!
  * $y = (x-mean)/std$
    using running estimates of mean,std
* is this learning under various init state (jpos, target pose)?
  * ans: yes, reset() is called at every rollout()
* loss vs loss_sampled?
  * ans: loss = surr
```
surr = - tf.reduce_mean(adv_n * logprob_n)
surr_sampled = - tf.reduce_mean(logprob_n) # Sampled loss of the policy
```
* ACKTR and A2C trained with batch sizes of 2500 and TRPO trained with a batch size of 25000.

## result
* performance: ACKTR > (A2C, TRPO)
  * discrete ctrl:
    * > A2C in terms of sample efficiency
      (i.e., speed of convergence per number of timesteps) by a significant margin in all games.
  * cont ctrl:
    * > A2C, TRPO on six out of eight MuJoCo tasks and
    * competitively with A2C on the other two tasks (Walker2d and Swimmer).
* per-update computation cost of ACKTR is only 10% to 25% higher than SGD-based methods.
* the benefit increases substantially: when using a larger batch size with ACKTR
  compared to with A2C, see fig 5c
* improvements by ACKTR to the actor compared to the baseline A2C
  (regardless of which norm we use to optimize the critic)
  * improvements brought by using the Gauss-Newton norm for optimizing the critic are more substantial in terms of
    sample efficiency and episode rewards at the end of training.
  * the Gauss-Newton norm also helps stabilize the training,
    as we observe larger variance in the results over random seeds with the Euclidean norm.
* ACKTR as the **first scalable trust region natural gradient** method for
  actor-critic methods
  * first to propose optimizing **both the actor and the critic** using natural gradient updates.
  * first to train several non-trivial tasks in continuous control directly from
    raw pixel observation space
* the improvements brought by using the Gauss-Newton norm for optimizing the critic are
  more substantial in terms of sample efficiency and episode rewards at the end of training. In addition,
  the Gauss-Newton norm also helps stabilize the training, as we observe larger variance in the results over random seeds with the Euclidean norm.
  * adaptive Gauss-Newton doesn’t provide any significant improvement over vanilla Gauss-Newton.

## background
* story: from standard to natural gradient
  * To minimize a nonconvex function $J(\theta)$,
    the method of steepest descent calculates the update $\Delta \theta$ that minimizes $J(\theta + \Delta \theta)$,
    subject to the constraint that $|| \Delta \theta ||_B < 1$,
    where $||·||_B$ is the norm defined by $|| x ||_B = (x^T B x)^{\frac{1}{2}}$ , and
    $B$ is a positive semidefinite matrix.
  * The solution to the constraint optimization problem has the form
    $\Delta \theta \propto -B^{-1} \nabla_{\theta} J$,
    where $\nabla_{\theta} J$  is the standard gradient.
  * When the norm is Euclidean, i.e., B = I, this becomes the commonly used method of gradient descent.
    * However, the Euclidean norm of the change depends on the parameterization θ.
      This is not favorable because the parameterization of the model is an arbitrary choice, and
      it should not affect the optimization trajectory.
  * The method of natural gradient constructs the norm using the Fisher information matrix F,
    a local quadratic approximation to the KL divergence.
    * This norm is independent of the model parameterization θ on the class of probability distributions,
      providing a more stable and effective update.
    * However, since modern neural networks may contain millions of parameters,
      computing and storing the **exact Fisher matrix and its inverse is impractical**
* Natural gradient methods (cf standard gradients)
  * follow the steepest descent direction that uses the Fisher metric as the underlying metric,
    a metric that is based not on the choice of coordinates but rather
    on the manifold (i.e., the surface).
  * exact computation is intractable
    * because it requires inverting the Fisher information matrix.
  * constructs the norm using the Fisher information matrix F,
    a local quadratic approximation to the KL divergence.
    * This norm is independent of the model parameterization $\theta$ on the class of probability distributions,
      providing a more stable and effective update.
    * However, since modern neural networks may contain millions of parameters,
      computing and storing the exact Fisher matrix and its inverse is impractical, so we have to resort to approximations.
  * if performed with SGD-like updates, it can result in large updates to the policy, causing
    the algorithm to prematurely converge to a near-deterministic policy.
    * advocate instead using a trust region approach, whereby
      the update is scaled down to modify the policy distribution (in terms of KL divergence) by
      at most a specified amount.
* Kronecker-factored approximate curvature (K-FAC) [16]
  * uses a Kronecker-factored approximation to the Fisher matrix to perform
    efficient approximate natural gradient updates.
  * each update is comparable in cost to an SGD update, and
  * keeps a running average of curvature information, allowing it to use small batches.
* TRPO avoids explicitly storing and inverting the Fisher matrix by using Fisher-vector products [21].
  * To avoid repeated computation of Fisher-vector products,
    * Wang et al. [28] solve the **constrained optimization** problem with a linear approximation of
      **KL divergence** between a running average of the policy network and the current policy network.
* active line of research:
  * designing an advantage function that provides **both low-variance and low-bias** gradient estimates
* Learning the critic can be
  thought of as a least-squares function approximation problem, albeit one with a **moving target**
  * In the setting of least-squares function approximation,
    the second-order algorithm of choice is commonly Gauss-Newton
  * The Gauss-Newton matrix is equivalent to the Fisher matrix for a Gaussian observation model
* in the context of deep RL, Schulman et al. [22] observed that such an update rule
  can result in large updates to the policy, causing the algorithm to prematurely converge
  to a near-deterministic policy.
  They advocate instead using a trust region approach, whereby the update is scaled down to modify the
  policy distribution (in terms of KL divergence) by at most a specified amount.
* In a large-scale distributed learning setting, large batch size is used in optimization.
  * Therefore, in such a setting, it is preferable to use a method that can scale well with batch size.

## comment
* ACKTR= KFAC + trustRegion + A2C
  * ACKTR is on-policy
  * KFAC is second-order optimizer
    * https://arxiv.org/abs/1503.05671
    * https://www.tensorflow.org/api_docs/python/tf/contrib/kfac
    * https://github.com/tttor/baselines/blob/study-acktr/baselines/acktr/kfac.py
* from nips reviewers:
  * more on application papers, ie apply KFAC to RL
  * comparison with x-axis representing optimization time instead of number of iterations,
    thus taking into account the complexity of the different algorithms
  * compare ADAM perform relative to ACKTR
* cf PPOKFAC: https://arxiv.org/abs/1801.05566
  * ACKTR > PPOKFAC
* note: KFAC alone is not enough, need to use trust-region for stability
* the use of KFAC for critic looks like just to show-off, we may use Gauss-Newton method
>  The Fisher matrix for the critic is defined with
respect to this Gaussian output distribution. In practice, we can simply set σ to 1, which is equivalent
to the vanilla Gauss-Newton method.
* this looks like some contradiction
  * sec 3.1
> But to avoid instability in training, it is often beneficial to use an architecture where the
two networks share lower-layer representations but have distinct output layers
  * A.2 Continuous control
> For experiments with low-dimensional state space as an input we used two separate neural networks
with 64 hidden units per layer in a two-layer network

* (-) setup for random seeds varies across plots and tables
* (-) performance varies across task: who wins, who loses

* (?) fisher info matrix does NOT include Q? in sec 3.1
  * ans: yes, see
    Bagnell and Schneider (2003) that (10) that shows
    the Fisher information matrix of the distribution over trajectories in the state-action space, given π.
* (?) why those 6 games?
  * ans: see Table 4 at appendix B, with Q-learning, one seed
* (?) episode rewards == return?
  * ans: yes, see Table 1
* (?) what does this mean?
> a distributed approach leads to rapidly diminishing returns of
  sample efficiency as the degree of parallelism increases.
* (?) where does the constraint come from?
> To minimize a nonconvex function J(θ), the method of steepest descent calculates the update ∆θ that minimizes J(θ + ∆θ),subject to the constraint that  ...
