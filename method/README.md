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
  * TRPO: Trust Region Policy Optimization (Schulman, 2015)
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
* model learning transfers across tasks and environment configurations (learning physics)
### cons
* suffer from significant bias, since complex unknown dynamics cannot always be modeled accurately enough
* 2 sources of approximation error: learn model, estimate a value function using the learned model

### method: 
* sample-efficient:
PILCO_2015, TEXPLORE_2013,
...

### method: planning
* online: 
DESPOT_2017, POMCP_2010, AEMS_2007, ...
* offline:
SARSOP, PBVI_2003, Perseus_2005, HSVI, ...
(most are point-based approaches that
sample belief states by simulating some random interactions of the agent with the environment and 
then maintain at most one $\alpha$-vector per sampled belief state)

### combining offline and online planning approaches, 
By using policies computed offline
* as macro actions to shorten the search horizon or
* as default policies at the leaves of the search tree in online planning or
* to provide (tight) lower and upper bounds (as heuristics) used in online search.

Most offline methods used in combination with online methods are based on approximation in that
they use the underlying MDP (the $(S, A, T, R)$ components of the POMDP model) to
compute lower bounds (e.g. Blind policy, point-based algorithms) and
upper bounds (e.g. MDP, QMDP, FIB) on the exact value function.

## model-based and model-free
### method
[PILQR_2017](https://github.com/tttor/rl-foundation/blob/master/method/dim02/pilqr_chebotar_2017.md),
[VPN_2017](https://github.com/tttor/rl-foundation/blob/master/method/dim02/vpn_oh_2017.md),
[Dyna2_2008](https://github.com/tttor/rl-foundation/blob/master/method/dim02/dyna2_silver_2008.md),
Dyna_1990

# [hybrids: methods that combine 2 (or more) methods]
* Temporal Difference (TD): MonteCarlo and DynamicsProgramming
* Actor-critic: value-based and policy-based

# [misc]
* on-policy _vs_ off-policy,
