# dim1: policy-based, value-based, ...

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
  
## policy- and value-based
* Actor-critic
