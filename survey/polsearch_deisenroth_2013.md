# A Survey on Policy Search for Robotics
* Marc Peter Deisenroth, Gerhard Neumann and Jan Peters
* Foundations and Trends in Robotics Vol. 2, No 1–2 (2013) 1–141 2013
* DOI: 10.1561/2300000021

## abs
* Policy search
  * focuses on finding good parameters for a given policy parametrization.
  * well suited for robotics as it can cope with high-dimensional state and action spaces
* model-based, model-free, see [../method/README.md](../method/README.md)

## 1: intro
### 1.1 Robot Control as a Reinforcement Learning Problem
* robot RL poses three main challenges,
  * high-dimensional continuous state and action spaces,
  * strong real- time requirements, and
  * the high costs of robot interactions with its environment.
* policy-based, value-based, see [../method/README.md](../method/README.md)
* Two ways of implementing cautious exploration are to either
  * avoid significant changes in the policy [57] or
  * explicitly discourage entering undesired regions in the state space [21].
* PS is often the RL ap- proach of choice in robotics since it is better at coping with the inherent challenges of robot reinforcement learning.

### 1.2 Policy Search Taxonomy
* The policy updates in both model-free and model- based policy search are based on either
  * policy gradients (PG),
  * expectation maximization (EM)-based updates, or
  * information- theoretic insights (Inf.Th.)
* In the model-based case (right sub-tree), we can either use
  * stochastic trajectory generation
    * the learned models are used as simulator for sampling trajectories.
      * Hence, learned models can easily be combined with model-free policy search approaches
        by  exchanging the “robot” with the learned model of the robot’s dynamics.
  * deterministic trajectory prediction.
    * does not sample trajectories, but analytically predicts the trajectory distribution
    * Typically, is computationally more involved than sampling trajectories from the system.
      * However, for the subse- quent policy update, deterministic trajectory prediction can
        allow for analytic computation of gradients, which
        can be advantageous over stochastic trajectory generation, where
        these gradients can only be approximated

### 1.3 Typical Policy Representations Typical
TODO

<!--
policy search based on paths from determiniistic sample based motion planners?

J. G. Schneider. Exploiting Model Uncertainty Estimates for Safe Dynamic Control Learning. In Advances in Neural Information Processing Systems. Morgan Kaufman Publishers, 1997.
 -->
