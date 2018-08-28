# Approximate Newton Methods for Policy Search in Markov Decision Processes
* Thomas Furmston et al
* jmlr2017
* http://jmlr.org/papers/v17/15-414.html

## problem
* (stochastic) gradient ascent suffers from
  * not scale invariant
  * the search direction is often poorly-scaled,
    *  leads to a poor rate of convergence
 
## observation
* less attention is the application of Newton’s method to Markov decision processes.
  *  the construction and inversion of the Hessian is too computationally expensive to be feasible
  * the objective function of a MDP is typically not concave, and
    * so the Hessian is not guaranteed to be negative-definite
    * the search direction of Newton’s method may not be an ascent direction
  *  the variance of sample-based estimators of the Hessian will be larger than that of estimators of the gradient.

## idea
* the Gauss-Newton Methods
  * drops the Hessian terms which are difficult to estimate, but
    are expected to be negligible in the vicinity of local optima
## setup
* task: robot arm application: ball-in-a-cup domain

## result
* provide a novel analysis of the Hessian of the total expected reward, 
  which is a standard objective function for policy optimization
* whenthe policy parameterisation is sufficiently rich, in the sense that it is $\epsilon$-value-consistent with 
  an appropriately small value of $\epsilon$, 
  * then the remaining terms in the Hessian become negligible in the vicinity of a local optimum
* (second Gauss-Newton) > EM-algorithm

## background
* to efficiently mimic Newton’s method (Approximate Newton methods)
  * quasi-Newton methods
    * designed to efficiently mimic Newton’s method using only evaluations of
      the gradient obtained during previous iterations of the algorithm.
  * Gauss-Newton method
    * is particular to non-linear least squares objective functions, for which the Hessian has a particular structure.
    * Due to this structure there exist certain terms in the Hessian that can be used as a useful proxy for the Hessian
* two forms of policy search algorithm
  * methods based on iteratively optimizing a lower-bound on the objective function,
    e.g. the expectation maximization (EM) algorithm
  * gradient-based optimization methods
* Policy search update using
  * gradient ascent
  * Natural Gradient Ascent
* It is **not possible** to calculate the gradient exactly for many real-world MDPs of interest.
  * in discrete domains the size of the state-action space may be too large for enu- meration over these sets to be feasible.   * in continuous domains the presence of non-linearities in the transition dynamics makes 
    the calculation of the occupancy marginals an intractable problem. 
  * it can be the case that P and R are unknown in practice. 
  * preferable to directly estimate the gradient using samples obtained from the environment, 
    rather than building a model of the MDP
    * eg Monte carlo policy gradient, actor-critic policy gradient methods

## comment
* relatively old work:
  no neural network, no openai gym env
* pol grad theorem differs in the $log \pi(\cdot)$
  * Theorem 1 (in this paper)
  * Equ 13.5 (Sutton's book)
  
