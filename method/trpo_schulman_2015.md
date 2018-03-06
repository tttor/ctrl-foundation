# Trust Region Policy Optimization
https://arxiv.org/abs/1502.05477
(ICML 2015)

## Idea: TRPO (trust region policy optimization)
* two variants of this algorithm: 
  * **the single-path method**, which can be ap- plied in the model-free setting; 
  * **the vine method**, which requires the system to be restored to particular states, 
  which is typically only possible in simulation.

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
