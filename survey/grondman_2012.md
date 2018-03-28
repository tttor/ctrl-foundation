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
      
