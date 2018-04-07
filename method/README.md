# method

## taxonomy
* source of experience
  * `model-free` (direct RL): `source= realWorld`
    * in robotics (cf Atari games), be aware of
      * _true_ model-free:
        trained with the **real** world
      * _pseudo_ model-free:
        trained with a **generative** model (typically offline, before execution)
    * pros and cons
      * (+) have the advantage of handling arbitrary dynamical systems with minimal bias
      * (-) less sample-efficient, high sample complexity
      * (-) require policies with carefully designed, low-dimensional parameterizations
  * `model-based` (indirect RL): `source= model`
    * consists of: planning and model learning
    * pros and cons
      * (+) sample-efficient
      * (+) model learning transfers across tasks and environment configurations (learning physics)
      * (-) suffer from significant bias, complex unknown dynamics cannot always be modeled accurately enough
      * (-) 2 sources of approximation error: learn model, estimate a value function using the learned model
  * hybrid: dyna (`true model-free` + and `model-based`)

* base for iteration
  * `policy-based` (policy-search, policy iteration)
    * gradient-free
    * gradient-based
  * `value-based` (value iteration)
  * hybrid: Actor-critic (`actor:policy-based` + `critic:value-based`)

* when policy compiled/learned with respect to execution/action time
  * `offline`
    * policy learned: before execution
  * `online`
    * policy learned: in between 2 execution (interleaved)
    * aka: decision-time planning
  * `background`
    * policy learned: in paralel with execution
  * hybrid: (`online` + `offline` + `background`)

## misc
* other dimensions:
  on-policy _vs_ off-policy,
  episodic _vs_ continuing tasks,
  average _vs_ cumulative discounted rewards,
  actor-/citic-only _vs_ actor-critic,
  shallow _vs_ deep learning,
  without-prior (non-Bayesian) _vs_ with-prior (Bayesian),
  plain _vs_ hierarchical structure,
  offline _vs_ online planning,
  (onlinePlanning or modelFreeRL) _vs_ (onlinePlanning + modelLearning + modelFreeRL),
  see also [summary of part 1 in Intro to RL book](https://github.com/tttor/rl-foundation/blob/master/book/rl-intro-sutton2018/part_01_summary.md)
* policy representation
  * time-varying linear-Gaussian (TVLG)
  * deep neural networks, rbf networks
  * dynamic movement primitives
  * belief tree
* Temporal Difference (TD):
  MonteCarlo and DynamicsProgramming
