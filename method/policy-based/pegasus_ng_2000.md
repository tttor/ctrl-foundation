# PEGASUS: A policy search method for large MDPs and POMDPs 
* Andrew Y. Ng, Michael Jordan

## problem
* For large POMDPs, the value and Q-functions are sometimes complicated and difficult to approximate, 
  even though there may be simple, compactly representable policies that perform very well.

## observation
* Any (PO)MDP can be transformed into an “equivalent” POMDP in which 
  all state transitions (given the current state and action) are deterministic.
* most computer implementations of generative models also provide deterministic simulative models

## idea: pegasus (Policy Evaluation-of-Goodness And Search Using Scenarios)
* **deterministic** simulative model:
  * assume we have an implementation of a generative model, with the difference that 
    * it has **no internal random number generator**, so that 
    * it has to ask us to provide it with random numbers whenever 
      it needs them (such as if it needs a source of randomness to draw samples from the POMDP’s transition distributions).
  * this reduce the problem of policy search in an ar- bitrary POMDP to 
    one in which all the transitions are deterministic:
    * that is, a POMDP in which taking an action  in a state will always deterministically result in 
      transitioning to some fixed state  
* defined an estimate for the value of every policy, and 
  finally performed policy search by optimizing these estimates.
* Transformation of (PO)MDPs, `$M$` to `$M'$`
  * steps:
    * the action space and discount factor remain the same
    * the state space of `$M'$` is `$S \times [0,1]^{\inf}$`
    * see more on the paper ....
  * Hence, the problem of policy search in general POMDPs is reduced to 
    the problem of policy search in POMDPs with deterministic transition dynamics.
* PEGASUS: A method for policy search
  * Having used `m` scenarios to define `$\hat{V}_{M'} (\pi)$` for all `$\pi$`, 
    we may search over policies to optimize `$\hat{V}_{M'} (\pi)$` 
  * Since `$\hat{V}_{M'} (\pi)$` is a deterministic function, 
    the search procedure only needs to optimize a deterministic function,
    
## setup
* task
  * gridworld POMDP, with 8 observations 
  * riding a bicycle with complex continuous state/continuous actions
    * where the objective is to ride to a goal one kilometer away. 
    * actions: torque to the handle bar and the displacement of the rider's center of gravity

## comment
* below statement about result (in Conclusion) is not strong
> our method working well.
* missing comparisons with other methods 
  
