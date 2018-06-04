 # mpc: model predictive control
 
* MPC is related to online planning (which plan wrt current belief) but different in that
  * it does not use markov assumption, so not formulated in POMDP
  * main components are cost-fn and optimizer
* see robust MPC for uncertainty handling

## resource
* http://www.mpc.berkeley.edu
* http://deepmpc.cs.cornell.edu/
> Defining `X_{t:k}` as the system state from time `t` through time `k`, and `U_{t:k}` similarly for system inputs, 
a model-predictive controller works by finding a set of optimal inputs `U^*_{t+1:t+T}` which minimize some cost function
`C(\hat{X}_{t+1:t+T}, U_{t+1:t+T})` over predicted state `\hat{X}` and control inputs `U` for some finite time horizon `T`
