# Trust Region Policy Optimization
https://arxiv.org/abs/1502.05477
(ICML 2015)

## Idea: TRPO (trust region policy optimization)
* two variants of this algorithm: 
  * **the single-path method**, which can be ap- plied in the model-free setting; 
  * **the vine method**, which requires the system to be restored to particular states, 
  which is typically only possible in simulation.
* prelim
  * advantage fn: $A_{\pi}(s,a) = Q_{\pi}(s,a) - V_{\pi}(s)$
  * Equ.2 implies that any policy update $\pi \mapsto \bar{\pi}$ that
    has a **nonnegative expected advantage at every state** $s$ is guaranteed to increase
   the policy performance, or leave it constant in the case that the expected advantage is zero everywhere.
  * in the approximate setting, it will typically be unavoidable, due to estimation and approximation error, that 
  there will be some states s for which the expected advantage is negative,
    * introduce a local approximation to the policy performance $\nu$, Equ.3
  * conservative policy iteration, for which they could provide explicit lower bounds on the improvement of $\nu$.

## Result
* suggest:
  * The use of recurrent policies with hidden state, could further make it possible to roll state estimation and 
  control into the same policy in the partially-observed setting. 
  * By combining TRPO with model learning, it would also be possible to substantially reduce its sample complexity, 
  making it applicable to real-world settings where samples are expensive.
  
## Misc
* policy optimization can be classified into three broad categories: 
  * **policy iteration methods**, which alternate between estimating the value function under the current policy and improving the policy (Bertsekas, 2005); 
  * **policy gradient methods**, which use an estimator of the gradient of the expected return (total reward) obtained from sample trajectories (Peters & Schaal, 2008a) (and which, as we later discuss, have a close connection to policy iteration); and 
  * **derivative-free optimization methods**, which treat the return as a black box function to be optimized 
  in terms of the policy parameters (Szita & Lorincz, 2006)
    * the cross-entropy method (CEM) and 
    * covariance matrix adaptation (CMA)
* Classic: that the update performed by exact policy iteration, which uses the deterministic policy 
  $\pi(s) = argmax_a A_{\pi}(s, a)$ improves the policy if there is at least **one state-action pair** 
  with a positive advantage value and nonzero state visitation probability, otherwise 
  the algorithm has converged to the optimal policy
