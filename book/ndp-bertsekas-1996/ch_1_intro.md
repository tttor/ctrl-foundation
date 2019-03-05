# ch_1_intro.md

* The cost-to-go Bellman satisfies some form of Bellman's equation
  $J^{\star}(i) = min_u E[ g(i, u, j) + J^{\star}(j) | i, u ]$
* Bellman's curse of dimensionality
  * due to very large numbers of states and controls

# 1.1 cost-to-go approx in DP
* $\tilde{J}$: scoring fn or approx cost-to-go fn
* the value $\tilde{J}(j, r)$: the score or approximate cost-to-go
* Q-factor
  * $Q^\star(i, u) = E[ g(i,u,j) + J^\star(j) | i, u ]$
* (suboptimal) control
  * $\tilde{\mu}(i) = \argmin_u \tilde{Q}(i, u, r)$

# 1.2 approx arch
checked!

# 1.3 sim and trainig
* simulation is used
  * for generate training data
    * to evaluate by simulation the cost-to-go fn of given (suboptimal) policies
    * try to iteratively improve these policies based on the simulation outcomes
  * when the systems are hard to model but easy to simulate
    * explicit detail mathematical model is not available or cumbersome, or impossible
    * the system can only be observed via a software simulator or as it operated in real time
  * simulation can implicitly identify the most important or most representative states of the systems
* me: this simulation is also termed: generative model

# 1.4 neuro DP
* this book:
  * value-based
  * model-based
  * finite state and action (control)
* mention briefly about: approximation in policy space (aka policy based),
  argue:
  * that policy parameterization can be hard for some problem
  * the minimization of the objective can be difficult because the gradient may not be easily calculated

