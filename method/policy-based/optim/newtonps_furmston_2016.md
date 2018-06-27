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

## comment
* relatively old work:
  no neural network, no openai gym env
