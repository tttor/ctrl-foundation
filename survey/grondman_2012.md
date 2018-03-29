# A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients 
Ivo Grondman, Lucian Busoniu, Gabriel A. D. Lopes, and Robert Babuska;
IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART C: APPLICATIONS AND REVIEWS, VOL. 42, NO. 6, NOVEMBER 2012

## abs
* focus on methods that can work in an **online setting** and use **function approximation** in order to 
  deal with **continuous** state and action spaces.
  
## intro
* actor-only
  * typically work with a parameterized family of policies overwhich optimization procedures can be used directly. 
  * benefit of a parameterized policy: 
    * a spectrum of continuous actions can be generated, 
    * **but** the optimization methods used (typically policy gradient methods) suffer from 
      high variance in the estimates of the gradient, leading to slow learning [1]–[5].
* critic-only
  * use temporal difference (TD) learning have a **lower variance** in the estimates of expected returns [3], [5], [6].
  * way of deriving a policy: by selecting greedy actions [7]: 
  * usually discretize the continuous action space, after which 
    the optimization over the action space becomes a matter of enumeration. 
* Actor-critic 
  * the parameterized actor brings the advantage of computing continuous actions without 
    the need for optimization procedures on a value function, 
  * the critic supplies the actor with low-variance knowledge of the performance. 
    * the critic’s estimate of the expected return allows for the actor to update with gradients that 
      have lower variance, speeding up the learning process.
    * The lower variance is traded for a larger bias at the start of learning when 
      the critic’s estimates are far from accurate [5].
  * usually have good convergence properties, in contrast with critic-only methods [1].
* focus is put on actor-critic algorithms based on policy gradients, distinction is made between algorithms that use 
  * a standard (sometimes also called vanilla) gradient and 
  * the natural gradient

## actor-critic in the context of reinforcement learning
* critic-only methods
  * Q-learning, SARSA
* Actor-Only Methods and the Policy Gradient Policy
  * the SRV [32] and Williams’ REINFORCE algorithms
  * A policy gradient method is generally obtained by parameterizing the policy by the parameter vector
  * main advantage: 
    * strong convergence property, which is naturally inherited from gradient descent methods
  * drawback:
    * the estimated gradient may have a large variance [19], [43]. 
    * every gradient is calculated without using any knowledge of past estimates [1], [44]
* Actor-Critic Algorithms Actor-critic
  * the large variance in the policy gradients of actor-only methods is countered by adding a critic
  * usually preserve the desirable convergence properties of policy gradient methods, cf critic-only methods
  * the policy is **not** directly inferred from the value function by using (11),
    **Instead**, the policy is updated in the policy gradient direction using only a small step size
  * the critic
    * to evaluate the current policy prescribed by the actor;
      evaluation by any policy evaluation method, such as TD or residual gradients [25].
    * approximates and updates the value function using samples;
      which is then used to update the actor’s policy parameters in the direction of performance improvement
    * responsible for processing the rewards it receives, i.e., 
      evaluating the quality of the current policy by adapting the value function estimate.
  * the actor
    * responsible for generating a control input u,given the current state x. 
    * After a number of policy evaluation steps by the critic, the actor is updated by using information from the critic.

## standard gradient actor-critic algorithms
* fuzzy actor-critic reinforcement learning network (FACRLN),
  * uses only one fuzzy neural network based on radial basis functions for both the actor and the critic.
* consolidated actor-critic model (CACM)    
  * that there is redundancy in learning separate networks for the actor and critic
  * set up a single neural network, using sigmoid functions instead of fuzzy rules, and 
    use it for both the actor and the critic
    
## discussion + outlook
* rules of thumb should help in selecting: whether a critic-only, actor-only, or actor-critic algorithm
  * type of control policy that should be learned
    * If it is necessary for the control policy to produce actions in a continuous space, 
      critic-only algorithms are no longer an option, as calculating a control law would require solving 
      the possibly non-convex optimization procedure of (11) over the continuous action space.
    * If the controller only needs to generate actions in a (small) countable, finite space, 
      it makes sense to use critic-only methods, as (11) can be solved by enumeration. 
    * Using a critic-only method also overcomes the problem of high-variance gradients in actor-only methods and 
      the introduction of more tuning parameters (e.g., extra learning rates) in actor-critic methods.
  * (quasi-)stationary MDP vs nonstationary environments
    * If the problem is modeled by a (quasi-)stationary MDP (with a continuous state and action space.), 
      actor-critic methods should provide policy gradients with lower variance than actor-only methods.
    * Actor-only methods are, however, more resilient to fast changing nonstationary environments, in which 
      a critic would be incapable of keeping up with the time-varying nature of the process and 
      would not provide useful information to the ac- tor, canceling the advantages of using actor-critic algorithms. 
 * choosing the right features for the actor and critic
   * consensus: the features for the actor and critic do **not** have to be chosen independently
     (Several actor-critic algorithms use the exact same set of features for both the actor and the critic)
   * policy gradient theorem indicates that best to first choose a parameterization for the actor, 
     after which compatible features for the critic can be derived  
   * Adding **state-dependent features** to the value function on top of the **compatible features** remains 
     an important task as this is the only way to further **reduce the variance in the policy gradient estimates**
* Choosing a good parameterization for the policy
* the speed of learning; affected by 
  * the quality of the gradient estimate
  * Balancing the exploration and exploitation of a policy
  * choosing good learning rate schedules
* even though the field of natural gradient actor-critic methods is still a very promising area for future re- search, 
  it does not always showsuperior performance compared with other methods.    

## comment
* seems not include the deep-net as fn approx, but indeed emphasize fn approx
