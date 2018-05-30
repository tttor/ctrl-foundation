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
* robot RL poses 3 main challenges,
  * high-dimensional continuous state and action spaces,
  * strong real- time requirements, and
  * the high costs of robot interactions with its environment.
* PS is often the RL approach of choice in robotics since
  it is better at coping with the inherent challenges of robot reinforcement learning.
* policy-based, value-based, see [../method/README.md](../method/README.md)
* Two ways of implementing cautious exploration are to either
  * avoid significant changes in the policy [57] or
  * explicitly discourage entering undesired regions in the state space [21].

### 1.2 Policy Search Taxonomy
* The policy updates in **both** model-free and model-based policy search are based on either
  * policy gradients (PG),
  * expectation maximization (EM)-based updates, or
  * information- theoretic insights (Inf.Th.)
* In the model-based case, we can either use
  * stochastic trajectory generation
    * the learned models are used as simulator for sampling trajectories.
      * Hence, learned models can easily be combined with model-free policy search approaches
        by  exchanging the “robot” with the learned model of the robot’s dynamics.
  * deterministic trajectory prediction.
    * does not sample trajectories, but analytically predicts the trajectory distribution
    * Typically, is computationally more involved than sampling trajectories from the system.
      * However, for the subsequent policy update, deterministic trajectory prediction can
        allow for analytic computation of gradients, which
        can be advantageous over stochastic trajectory generation, where
        these gradients can only be approximated

### 1.3 Typical Policy Representations Typical
* 2 categories
  * time-independent representations `\pi(x)`
    * use the same policy for all time steps, and,
      hence, often require a complex parametrization
    * eg: linear policies
  * time-dependent representations `\pi(x, t)`
    * can use different policies for different time steps,
      allowing for a potentially simpler structure of the individual policies can be used.
* 2 formulation
  * deterministic formulation
  * stochastic formulations,
    * typically a zero-mean Gaussian noise vector is added to `\pi_{\theta} (x, t)`.
      * the parameter vector `\theta` typically also includes the (co)variance matrix
        used for generating the noise
* policy representations  in robot learning
  * linear policies,
    * `\pi_{theta} = \theta \phi(x)`,
      where `\phi` is a basis fn vector
    * time-independent
    * only depends linearly on the policy parameters
    * specifying the basis functions by hand is typically a difficult task
  * radial basis function networks,
    * nonlinear time-independent policy representation
    * the basis functions are considered as free parameters that need to be learned
    * difficult to learn due to the high number of nonlinear parameters
    * are local representations, they are hard to scale to high-dimensional state spaces.
  * dynamic movement primitives
    * time-dependent
    * use non-linear dynamical systems for generating the movement of the robot.
    * key principle:
      to a use a linear spring-damper system which is modulated by
      a non-linear forcing function
  * central pattern generators for robot walking [24] and
  * feed-forward neural networks

## 4: Conclusion and Discussion
### 4.1 Conclusion
* distinguished between
  * the used policy evaluation strategy,
  * policy update strategy,
    * policy gradients,
    * expectation-maximization,
    * information-theoretic policy updates
    * policy updates based on path integrals
  * exploration strategy.

### 4.2 Current State of the Art
* Most applications of model-free policy search rely on
  imitation learning to initialize the learning process.

### 4.3 Future Challenges and Research Topics.
* the combination of model-free policy search with learned models
  seems to be a promising approach,
  * most model-based approaches greedily exploit the learned model
    by using gradient-based approaches.
    * Model-free policy update strategies could be used to avoid
      a greedy optimization, and,
    * hence, the additional exploration might in the end
      improve the quality of the learned models.
  * to smoothly switch from model-based policy search in the initial learning phase
    to model-free policy search when sufficiently much data is available for
    model-free policy updates.
    * In such case, the model could guide the initial exploration into
      relevant areas of the parameter space.
    * For fine-tuning the policy, real trajectory samples are used, and,
      hence, the policy update is not affected from model errors.
* to incorporate structured and hierarchical learning methods into policy search.
  * hierarchical approaches have so far not been explored for model-based reinforcement learning.
  * the use of hierarchical robot control policies used in robot learning is
    largely unexplored and will become a new important subfield in robot learning
* Non-parametric methods, such as Gaussian processes or
  LWBR already provide the necessary flexibility but might be difficult
  to scale to high-dimensional systems
* So far, many applications included single-stroke tasks such
  as hitting a baseball or catching a ball with a cup.
  * The next step is to integrate robot learning into large-scale tasks which
    require the execution of a multitude of single movements.

<!--
policy search based on paths from determiniistic sample based motion planners?

J. G. Schneider. Exploiting Model Uncertainty Estimates for Safe Dynamic Control Learning. In Advances in Neural Information Processing Systems. Morgan Kaufman Publishers, 1997.

A. Kupcsik, M. P. Deisenroth, J. Peters, and G. Neumann. Data-
Efficient Generalization of Robot Skills with Contextual Policy
Search. In Proceedings of the AAAI Conference on Artificial In-
telligence, 2013.

Policy Gradient methods for planning
doug aberdeen
 -->
