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
  
## observation
* One way to effectively reduce the sample size is to use more advanced optimization techniques for gradient updates
* applying K-FAC to policy optimization could improve the sample efficiency of the current deep RL methods

## idea: Kronecker-factored trust region (ACKTR)
* extend the framework of natural policy gradient and 
  propose to optimize **both the actor and the critic** using Kronecker-factored approximate curvature (K-FAC) with trust region
  * K-FAC to approximate the natural gradient update for actor-critic methods, with trust region optimization for stability
  * optimizing both the actor and the critic using natural gradient updates

## setup
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
