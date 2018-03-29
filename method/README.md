# method

* policy-based (policy-search, policy iteration)
  * gradient-free
    * cross-entropy method
  * gradient-based
    * TRPO: Trust Region Policy Optimization (Schulman, 2015)
    * DPG, Deep DPG, Recurrent DPG
  * misc:
    * TNPG: Truncated Natural Policy Gradient
    * PILCO
    * GPS: Guided Policy Search, 2013
    * PEGASUS, 2000
    * DMP: Dynamic Motion Primitives

* value-based (value iteration)
  * Deep Q-network
  * UVFA_2015

* model-free
  * TODO

* model-based
  * sample-efficient:
    PILCO_2015, TEXPLORE_2013,...
  * planning

* hybrids: methods that combine 2 (or more) methods
  * Temporal Difference (TD): MonteCarlo and DynamicsProgramming
  * Actor-critic: value-based and policy-based
    * Async Advantage Actor-Critic (A3C)
  * model-based and model-free (here, we call this `dyna`)
    * PILQR_2017, VPN_2017
    * Dyna2_2008, Dyna_1990

## model-free
* pros
  * have the advantage of handling arbitrary dynamical systems with minimal bias
* cons
  * less sample-efficient, high sample complexity
  * require policies with carefully designed, low-dimensional parameterizations

## model-based
* pros
  * sample-efficient
  * model learning transfers across tasks and environment configurations (learning physics)
* cons
  * suffer from significant bias, since complex unknown dynamics cannot
    always be modeled accurately enough
  * 2 sources of approximation error: learn model, estimate a value function
    using the learned model
    
## misc
* on-policy _vs_ off-policy, episodic _vs_ continuing tasks, average _vs_ cumulative discounted rewards, 
* actor-only, critic-only, and actor-critic methods
* hybrids: methods that combine 2 (or more) methods
  * Temporal Difference (TD): MonteCarlo and DynamicsProgramming
  * Actor-critic: value-based and policy-based
  * Dyna: model-based and model-free
* policy representation
  * time-varying linear-Gaussian (TVLG)
  * deep neural networks, rbf networks
  * dynamic movement primitives
