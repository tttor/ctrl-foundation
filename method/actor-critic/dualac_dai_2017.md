# Boosting the Actor with Dual Critic
∗ Bo Dai1, Albert Shaw1, Niao He, Lihong Li, Le Song

## problem
* Lagrangian dual form yields a game-theoretic view for the roles of the actor and the dual critic
  * such a framework for actor and dual critic allows them to be optimized for the same objective function,
  * parametering the actor and dual critic **unfortunately induces instablity** in optimization

## idea: Dual Actor-Critic
* derived in a principled way from the Lagrangian dual form of the Bellman optimality equation,
  * which can be viewed as a two-player game between the actor and a critic-like function,
    which is named as dual critic
* has the desired property that
  * the actor and dual critic are updated cooperatively to optimize the same objective function,
    * providing a more transparent way for learning the critic that
      is directly related to the objective function of the actor.
* exploits stochastic dual ascent algorithm for the path regularized, multi-step bootstrapping two-player
game

## result
TODO: more
