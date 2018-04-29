# Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation
* Yuhuai Wu, et al
* https://arxiv.org/abs/1708.05144
* https://github.com/openai/baselines/tree/master/baselines/acktr

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
* computational challenges when applying natural gradient methods, mainly associated with 
  efficiently storing the Fisher matrix as well as computing its inverse.
  * For tractability: using the compatible function approximator (a linear function approximator). 
  * To avoid the computational burden, Trust Region Policy Optimization (TRPO) [22] approximately solves 
    the linear system using conjugate gradient with fast Fisher matrix-vector products; 
    * but shortcomings:
      * requires repeated computation of Fisher vector products, 
        preventing it from scaling to the larger architectures typically used in experiments on learning from 
         image observations in Atari and MuJoCo. 
      * requires a large batch of rollouts in order to accurately estimate curvature. 
      * generally less sample efficient (Although TRPO shows better per-iteration progress than 
        policy gradient methods trained with first-order optimizers such as Adam)
    * K-FAC avoids both issues by 
      * using tractable Fisher matrix approximations and 
      * keeping a running average of curvature statistics during training.  

## observation
* One way to effectively reduce the sample size is to use more advanced optimization techniques for gradient updates
* applying K-FAC to policy optimization could improve the sample efficiency of the current deep RL methods

## idea: Kronecker-factored trust region (ACKTR)
* extend the framework of natural policy gradient and
  propose to optimize **both the actor and the critic** using Kronecker-factored approximate curvature (K-FAC) with trust region
  * K-FAC to approximate the natural gradient update for actor-critic methods, with trust region optimization for stability
  * optimizing both the actor and the critic using natural gradient updates
* propose also applying a natural gradient update to the critic
  (The previous natural policy gradient method applied a natural gradient update only to the actor)
  
## setup
* to avoid instability in training,
  it is often beneficial to use an architecture where the two networks share lower-layer representations but
  have distinct output layers
* env:
  * discrete ctrl: Atari environments [4] and 
  * continuous ctrl: the MuJoCo [27] tasks
    * low-dimensional state-space representation 
    * directly from pixel representation
* baselines
  * a synchronous and batched version of the asynchronous advantage actor critic model (A3C) [18], called A2C , and 
  * TRPO [22].
* plots on: episode reward vs number of timesteps
  
## result
* ACKTR substantially improves both sample efficiency and the final performance of the agent
  compared to the state-of-the-art on-policy actor-critic method A2C [18] and the famous trust region optimizer TRPO [22].
* the per-update computation cost of ACKTR is only 10% to 25% higher than SGD-based methods.
* regardless of which norm we use to optimize the critic, there are improvements brought by 
  applying ACKTR to the actor compared to the baseline A2C
  * improvements brought by using the Gauss-Newton norm for optimizing the critic are more substantial in terms of 
    sample efficiency and episode rewards at the end of training. 
  * the Gauss-Newton norm also helps stabilize the training, 
    as we observe larger variance in the results over random seeds with the Euclidean norm.
* the benefit increases substantially when using a larger batch size with ACKTR compared to with A2C.

## misc
* Natural gradient methods (cf standard gradients)
  * follow the steepest descent direction that uses the Fisher metric as the underlying metric,
    a metric that is based not on the choice of coordinates but rather on the manifold (i.e., the surface).
  * constructs the norm using the Fisher information matrix F, a local quadratic approximation to the KL divergence.
    * This norm is independent of the model parameterization `\theta` on the class of probability distributions,
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
  
* active line of research:
  designing an advantage function that provides **both low-variance and low-bias** gradient estimates
  
## comment
* the essense is to use KFAC to approximate the natural gradient updates,
  yet another optimizer, see https://www.tensorflow.org/api_docs/python/tf/contrib/kfac

