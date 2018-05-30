# Bayesian Policy Gradient and Actor-Critic Algorithms
* Mohammad Ghavamzadeh et al
* jmlr2016
* http://jmlr.org/papers/v17/10-245.html

## observation
* Existing AC algorithms are based on parametric critics that are updated to optimize frequentist fitness criteria. 
  * By “frequentist” we mean algorithms that return a point estimate of the value function, rather than 
    a complete posterior distribution computed using Bayes’ rule. 
* Both conventional and natural policy gradient and actor-critic methods rely on MonteCarlo (MC) techniques in 
  estimating the gradient of the performance measure. 
  * MC estimation is a frequentist procedure, and as such violates the likelihood principle
  * although MC estimates are unbiased, they tend to suffer from high variance, or alternatively, 
    require excessive sample sizes

## idea: Bayesian policy gradient (BPG)
* propose a Bayesian framework for policy gradient, based on modeling the policy gradient as a Gaussian process. 
  * This reduces the number of samples needed to obtain accurate gradient estimates
  * considers system trajectories as its basic observable unit,  
    * it does not require the dynamics within trajectories to be of any particular form, and 
    * thus, can be easily extended to partially observable problems.
* to model the gradient of the expected return with respect to the policy parameters,
  which is of the form of an integral, as Gaussian processes (GPs)
* Bayesian policy gradient (BPG) algorithms use GPs to define a prior distribution over the gradient of the expected return, 
  and compute its posterior conditioned on the observed data
* extend BPG framework to Bayesian actor-critic (BAC)
  * in order to  take advantage of the Markov property when the system is Markovian.

## setup
* task:
  * mountain car problem (Sutton and Barto, 1998), and 
  * the continuous state and continuous action ship steering domain (Miller et al., 1990).

## result
* BAC provides more accurate estimates of the policy gradient than 
  either of the two BPG models for the same amount of data

## background
* the conventional frequentist: (Monte-Carlo based) policy gradient estimation procedure.
* effort to reduce variance in policy gradient
  * to use an artificial discount factor
    * this introduces bias into the gradient estimates.
  * to subtract a reinforcement baseline from the average reward estimate in the updates of PG algorithms
  * to replace the policy gradient estimate with an estimate of the so-called natural policy gradient
    * motivation: a change in the way the policy is parametrized should not influence the result of the policy update.
    * the move to natural-gradient amounts to linearly transforming the gradient using 
      the inverse Fisher information matrix of the policy
  * to use an explicit representation for the value function of the policy, ie actor-critic algorithms.
  
* actor-critic is supplanted in SARSA (Rummery and Niranjan, 1994), that 
  estimate action-value functions and use them directly to select actions without 
  maintaining an explicit representation of the policy.
  * appealing because of its simplicity, 
  * but when combined with function approximation was found to be unreliable,
    often failing to converge  
    
    
## comment
* ? why not compare to openai mujoco tasks?
