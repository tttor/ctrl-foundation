# A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients 
Ivo Grondman, Lucian Busoniu, Gabriel A. D. Lopes, and Robert Babuska;
IEEE TRANSACTIONS ON SYSTEMS, MAN, AND CYBERNETICS—PART C: APPLICATIONS AND REVIEWS, VOL. 42, NO. 6, NOVEMBER 2012

## abs
* focus on methods that can work in an **online setting** and use **function approximation** in order to 
  deal with **continuous** state and action spaces.
  
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
* seems not include the deep-net as fn approx
