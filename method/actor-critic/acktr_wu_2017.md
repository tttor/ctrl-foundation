# Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation
* Yuhuai Wu, et al
* nips2017: poster
* https://papers.nips.cc/paper/7112-scalable-trust-region-method-for-deep-reinforcement-learning-using-kronecker-factored-approximation
* https://arxiv.org/abs/1708.05144
* https://blog.openai.com/baselines-acktr-a2c/
* https://github.com/openai/baselines/tree/master/baselines/acktr # tf
  * https://github.com/tttor/baselines/tree/study-acktr/baselines/acktr
* https://github.com/openai/baselines-results
* https://github.com/emansim/acktr
* https://www.youtube.com/watch?v=0rrffaYuUi4
* https://www.youtube.com/watch?v=gtM87w1xGoM

## problem
* still does **not exist** a scalable, sample-efficient, and
  general-purpose instantiation of the natural policy gradient.
  * SGD and related first-order methods explore weight space inefficiently
  * TRPO is impractical for large models and suffers from sample inefficiency
    * requires many steps of conjugate gradient to obtain a single parameter update, and
    * accurately estimating the curvature requires a large number of samples in each batch;
* computational challenges when applying natural gradient methods:
  mainly associated with efficiently storing the Fisher matrix as well as computing its inverse.
  * for tractability:
    * to use the compatible function approximator (a linear function approximator).
  * to avoid the computational burden:
    TRPO approximately solves the linear system using conjugate gradient with
    fast Fisher matrix-vector products,
    * but, shortcomings:
      * requires repeated computation of Fisher vector products,
        preventing it from scaling to the larger architectures typically used in
        experiments on learning from image observations in Atari and MuJoCo.
      * requires a large batch of rollouts in order to accurately estimate curvature.
      * generally less sample efficient
        (although TRPO shows better per-iteration progress than
        policy gradient methods trained with first-order optimizers such as Adam)
    * K-FAC avoids both issues by
      * using tractable Fisher matrix approximations and
      * keeping a running average of curvature statistics during training.

## observation
* to effectively reduce the sample size (improve the sample efficiency)
  * to use more advanced optimization techniques for gradient updates
    * applying K-FAC to policy optimization

## idea: actor-critic Kronecker-factored trust region (ACKTR)
* to optimize **both the actor and the critic** using
  Kronecker-factored approximate curvature (K-FAC) with trust region
  * K-FAC to approximate the natural gradient update for actor-critic methods,
    with trust region optimization for stability
* applying a natural gradient update **to the critic**
  * previously, a natural gradient update only to the actor
  * assume the output of the critic is defined to be a Gaussian distribution
* define the joint distribution of the policy and the value distribution by
  assuming independence of the two output distributions, i.e., $p(a, v|s) = \pi(a|s) p(v|s)$, and
  construct the Fisher metric with respect to $p(a, v|s)$,
* apply K-FAC to approximate the Fisher matrix to perform updates simultaneously.

## setup
* task
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
* critic/value network:
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

## result
* performance: ACKTR > (A2C, TRPO)
  * discrete ctrl:
    * > A2C in terms of sample efficiency
      (i.e., speed of convergence per number of timesteps) by a significant margin in all games.
  * cont ctrl:
    * > A2C, TRPO on six out of eight MuJoCo tasks and
    * competitively with A2C on the other two tasks (Walker2d and Swimmer).
* per-update computation cost of ACKTR is only 10% to 25% higher than SGD-based methods.
* the benefit increases substantially
  * when using a larger batch size with ACKTR compared to with A2C, see fig 5c
* improvements by ACKTR to the actor compared to the baseline A2C,
  regardless of which norm we use to optimize the critic
  * improvements brought by using the Gauss-Newton norm for optimizing the critic are more substantial in terms of
    sample efficiency and episode rewards at the end of training.
  * the Gauss-Newton norm also helps stabilize the training,
    as we observe larger variance in the results over random seeds with the Euclidean norm.

## background
* story: from standard to natural gradient
  * To minimize a nonconvex function J(θ),
    the method of steepest descent calculates the update ∆θ that minimizes J(θ + ∆θ),
    subject to the constraint that ||∆θ||B < 1,
    where || · ||B is the norm defined by $|| x ||_B = (x^T B x)^{\frac{1}{2}}$ , and B is a positive semidefinite matrix.
  * The solution to the constraint optimization problem has the form $\Delta \theta \propto -B^{-1} \nabla_{\theta} J$,
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
      computing and storing the exact Fisher matrix and its inverse is impractical, so we have to resort to approximations.
* Natural gradient methods (cf standard gradients)
  * exact computation is intractable
    * because it requires inverting the Fisher information matrix.
  * follow the steepest descent direction that uses the Fisher metric as the underlying metric,
    a metric that is based not on the choice of coordinates but rather on the manifold (i.e., the surface).
  * constructs the norm using the Fisher information matrix F, a local quadratic approximation to the KL divergence.
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
  * uses a Kronecker-factored approximation to the Fisher matrix to perform efficient approximate natural gradient updates.
  * each update is comparable in cost to an SGD update, and
  * it keeps a running average of curvature information, allowing it to use small batches.
* TRPO avoids explicitly storing and inverting the Fisher matrix by using Fisher-vector products [21].
  * To avoid repeated computation of Fisher-vector products,
    * Wang et al. [28] solve the **constrained optimization** problem with a linear approximation of
      **KL divergence** between a running average of the policy network and the current policy network.
* active line of research:
  * designing an advantage function that provides **both low-variance and low-bias** gradient estimates

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
* (-) setup for random seeds varies across plots and tables
* (?) why those 6 games?
  * ans: see Table 4 at appendix B, with Q-learning, one seed
* (?) episode rewards == return?
  * ans: yes, see Table 1
* (?) what does this mean?
> a distributed approach leads to rapidly diminishing returns of
  sample efficiency as the degree of parallelism increases.
* (?) where does the constraint come from?
> To minimize a nonconvex function J(θ), the method of steepest descent calculates the update ∆θ that minimizes J(θ + ∆θ),
  subject to the constraint that  ...
