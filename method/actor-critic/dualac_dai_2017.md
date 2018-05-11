# Boosting the Actor with Dual Critic
* Bo Dai1, Albert Shaw1, Niao He, Lihong Li, Le Song
* iclr2018: poster
* https://arxiv.org/abs/1712.10282
* https://openreview.net/forum?id=BkUp6GZRW

## problem
* While the use of a critic is important for the efficiency of actor-critic algorithms, 
  it is not entirely clear **how the critic should be optimized to facilitate improvement** of the actor.
* Lagrangian dual form yields a game-theoretic view for the roles of the actor and the dual critic
  * such a framework for actor and dual critic allows them to be optimized for the same objective function,
  * parametering the actor and dual critic **unfortunately induces instablity** in optimization

## idea: Dual Actor-Critic
* derived in a principled way from the Lagrangian dual form of the Bellman optimality equation,
  * which can be viewed as a two-player game between the actor and a critic-like function,
    which is named as dual critic
* the actor and dual-critic are **updated cooperatively** to optimize the same objective function,
  * providing a more transparent way for learning the critic that
    is directly related to the objective function of the actor.
* exploits stochastic dual ascent algorithm for the path regularized,
  multi-step bootstrapping two-player game
* propose path regularization for enhanced numerical stability.
* The dual actor-critic algorithm includes both 
  the learning of optimal value function and optimal policy in a unified framework based on 
  the duality of the linear programming (LP) representation of Bellman optimality equation

## background
* An actor-critic algorithm has two components: the actor (policy) and the critic (value function). 
  * As in policy-search methods, actor is updated towards the direction of policy improvement. 
  * However, the update directions are computed with the help of the critic, which 
    can be more efficiently learned as in value-function-based methods
    * Although the use of a critic may introduce bias in learning the actor, 
      its reduces variance and thus the sample complexity as well, compared to pure policy-search algorithms.
    * temporal-difference methods are perhaps the most popular choice to learn the critic, especially 
      when nonlinear function approximation is used
      
## result
* TODO: finish!
* how did someone come up with ...Lagrangian...?
