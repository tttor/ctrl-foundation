# method

## taxonomy
* source of experience
  * `source= realWorld`: model-free (direct RL)
    * in robotics (cf Atari games), be aware of
      * _true_ model-free:
        trained with the **real** world
      * _pseudo_ model-free:
        trained with a **generative** model (typically offline, before execution)
    * pros and cons
      * (+) have the advantage of handling arbitrary dynamical systems with minimal bias
      * (-) less sample-efficient, high sample complexity
      * (-) require policies with carefully designed, low-dimensional parameterizations
  * `source= model`: model-based (indirect RL)
    * consists of: planning and model learning
    * pros and cons
      * (+) sample-efficient
      * (+) model learning transfers across tasks and environment configurations (learning physics)
      * (-) suffer from significant bias, complex unknown dynamics cannot always be modeled accurately enough
      * (-) 2 sources of approximation error: learn model, estimate a value function using the learned model
    * sample-efficient:
      PILCO_2015, TEXPLORE_2013,...
  * hybrid: dyna (true model-free and model-based RL)

* base for iteration
  * policy-based (policy-search, policy iteration)
    * gradient-free
    * gradient-based
  * value-based (value iteration)
  * hybrid: Actor-critic: value-based and policy-based

* when policy compiled/learned with respect to execution/action time
  * offline
    * policy compiled/learned: before execution
  * online
    * policy compiled/learned: during execution (in paralel)

## misc
* on-policy _vs_ off-policy,
  episodic _vs_ continuing tasks,
  average _vs_ cumulative discounted rewards,
  actor-/citic-only _vs_ actor-critic,
  shallow _vs_ deep learning,
  without-prior (non-Bayesian) _vs_ with-prior (Bayesian),
  plain _vs_ hierarchical structure,
  offline _vs_ online planning,
  (onlinePlanning or modelFreeRL) _vs_ (onlinePlanning + modelLearning + modelFreeRL)
* policy representation
  * time-varying linear-Gaussian (TVLG)
  * deep neural networks, rbf networks
  * dynamic movement primitives
  * belief tree
* Temporal Difference (TD):
  MonteCarlo and DynamicsProgramming
