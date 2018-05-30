# Bayesian Policy Gradient and Actor-Critic Algorithms
* Mohammad Ghavamzadeh et al
* Journal of Machine Learning Research 17 (2016) 1-53
* http://jmlr.org/papers/v17/10-245.html

## idea
* propose a Bayesian framework for policy gradient, based on modeling the policy gradient as a Gaussian process. 
  * This reduces the number of samples needed to obtain accurate gradient estimates
  * considers system trajectories as its basic observable unit,  
    * it does not require the dynamics within trajectories to be of any particular form, and 
    * thus, can be easily extended to partially observable problems.
