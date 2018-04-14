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
    * pros and cons
      * (+) apply to a wider range of problems, eg when Q-fn is too complex 
      * (+) faster convergence rate 
      * (+) easily applied to continuous action space, since capable of learning stochastic policies
      * (-) high variance (due to monte carlo method) in estimating the gradient
      * (-) tend to converge to a local optimal
  * `value-based` (value iteration)
    * pros and cons
      * (+) low variance, high bias (due to bootstrapping): more stable performance
      * (-) need to discretize action for continuous action space
  * hybrid: Actor-critic (`actor:policy-based` + `critic:value-based`)

* when policy compiled/learned with respect to execution/action time
  * `offline`
    * policy learned (planned) before execution
    * consider all contingencies so does not scale up
  * `online`
    * aka: decision-time planning
    * policy learned: in between 2 execution (interleaved)
    * typically plans **each** step from the **current** belief, so
      potentially can handle large-scale planning
    * handle model changes naturally
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
