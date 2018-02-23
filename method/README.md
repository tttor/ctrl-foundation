# method

# [policy-based, value-based]

## policy-based (policy-seach)
### policy representation
* time-varying linear-Gaussian (TVLG)
* deep neural networks, rbf networks
* dynamic movement primitives
### methods:
* gradient-free
  * cross-entropy method
* gradient-based
  * TRPO: Trust Region Policy Optimization (Schulman, 2017)
  * DPG, DDPG
* misc:
  * TNPG: Truncated Natural Policy Gradient
  * PILCO
  * GPS: Guided Policy Search, 2013
  * PEGASUS, 2000 

## value-based
* Deep Q-network

# [model-free, model-based]

## model-free
### pros
* have the advantage of handling arbitrary dynamical systems with minimal bias
### cons
 * less sample-efficient, high sample complexity
### methods
?

## model-based
### pros
* sample-efficient
* Model learning transfers across tasks and environment configurations (learning physics)

### cons
* suffer from significant bias, since complex unknown dynamics cannot always be modeled accurately enough
* Two sources of approximation error: learn model, estimate a value function using the learned model: 

### method: model learning
?

### method: planning
DESPOT_2017,
POMCP_2010,
AEMS

## model-based and model-free
### method
[PILQR_2017](https://github.com/tttor/rl-foundation/blob/master/method/dim02/pilqr_chebotar_2017.md),
[VPN_2017](https://github.com/tttor/rl-foundation/blob/master/method/dim02/vpn_oh_2017.md),
[Dyna2_2008](https://github.com/tttor/rl-foundation/blob/master/method/dim02/dyna2_silver_2008.md),
Dyna_1990

# [hybrids: methods that combine 2 (or more) methods]
* Temporal Difference (TD)
  * MonteCarlo and DynamicsProgramming
* Actor-critic
  * value-based and policy-based

# [misc]
* on-policy _vs_ off-policy,
