# method

## taxonomy
* source of experience
  * `model-free` (direct RL): `source= realWorld`
    * the agent directly learns an optimal (or good) action-selection strategy from the collected data.
    * may be more efficient in cases where the solution space (e.g., policy space) exhibits more regularity than 
      the underlying dynamics
    * in robotics (cf Atari games where there is no real world; both real and sim are in simulator)
      * _true_ model-free:
        * trained with the **real** world
        * real experience is expensive
      * _pseudo_ model-free:
        * trained with a **generative** model 
        * typically offline, before execution
        * aka planning because this also uses a generative model
        * sim2real gap problem when deploying the trained policy to real world       
    * pros and cons
      * (+) have the advantage of handling arbitrary dynamical systems with minimal bias
      * (-) less sample-efficient, high sample complexity
      * (-) require policies with carefully designed, low-dimensional parameterizations
  * `model-based` (indirect RL): `source= model`
    * the agent uses the collected data to first build a model of the domain’s dynamics and 
      then uses this model to optimize its policy.
    * consists of: planning and model learning
    * pros and cons
      * (+) sample-efficient; better results with less data
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
  * hybrid: actor-critic (`actor:policy-based` + `critic:value-based`)

* when policy compiled/learned with respect to execution/action time
  * `offline`
    * policy learned (planned) before execution
    * consider all contingencies so does not scale up
  * `online`
    * aka: decision-time planning
    * plan from the **current** belief (typically, each step), so
      * potentially can handle large-scale planning
      * handle model changes naturally
    * policy learned: 
      in between 2 execution (interleaved) and **in background** (in paralel with execution)
  * hybrid: (`offline` + `online`)

* other dimensions:
  on-policy _vs_ off-policy,
  episodic _vs_ continuing tasks,
  average _vs_ cumulative discounted rewards,
  shallow _vs_ deep learning,
  without-prior (non-Bayesian) _vs_ with-prior (Bayesian),
  plain _vs_ hierarchical structure,
  (onlinePlanning or modelFreeRL) _vs_ (onlinePlanning + modelLearning + modelFreeRL),
  see also [summary of part 1 in Intro to RL book](https://github.com/tttor/rl-foundation/blob/master/book/rl-intro-sutton2018/part_01_summary.md)

## topics
Deep RL,
Bayesian RL,
RL in POMDP,
Hierarchical RL,
Inverse RL,
Safe RL,
Transfer learning in RL,
Curriculum learning in RL,
Multiagent RL,
Evolutionary RL,
...

## policy representation
* neural networks
  * tutor: 
    * https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/02_nn_random_agent.py
* belief tree
* dynamic movement primitives
* time-varying linear-Gaussian (TVLG)

## misc
* Temporal Difference (TD):
  MonteCarlo and DynamicsProgramming
* generalised policy iteration: interleaving policy evaluation with policy improvement 
  * Policy evaluation:
    * estimate the action-value function, 
    * eg, by Monte-Carlo evaluation or temporal-difference learning. 
  * Policy improvement:
    * update the policy with respect to the (estimated) action-value function
    * eg, a greedy maximisation (or soft maximisation) of the action-value function
