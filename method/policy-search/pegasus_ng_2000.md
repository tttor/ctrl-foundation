# PEGASUS: A policy search method for large MDPs and POMDPs 
* Andrew Y. Ng, Michael Jordan

## problem
* For large POMDPs, the value and Q-functions are sometimes complicated and difficult to approximate, 
  even though there may be simple, compactly representable policies that perform very well.

## observation
* Any (PO)MDP can be transformed into an “equivalent” POMDP in which 
  all state transitions (given the current state and action) are deterministic.

## idea: pegasus
* deterministic simulative model:
  * assume we have an implementation of a generative model, with the difference that 
    it has **no internal random number generator**, so that it has to ask us to provide it with random numbers whenever 
    it needs them (such as if it needs a source of randomness to draw samples from the POMDP’s transition distributions).
    
