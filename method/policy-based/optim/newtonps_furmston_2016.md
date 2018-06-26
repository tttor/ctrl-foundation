# Approximate Newton Methods for Policy Search in Markov Decision Processes
* Thomas Furmston et al
* jmlr2017
* http://jmlr.org/papers/v17/15-414.html

## 1. Introduction
* (stochastic) gradient ascent suffers from
  *  not scale invariant
  * the search direction is often poorly-scaled,
    *  leads to a poor rate of convergence
* less attention is the application of Newton’s method to Markov decision processes.
  *  the construction and inversion of the Hessian is too computationally expensive to be feasible
  * the objective function of a MDP is typically not concave, and
    * so the Hessian is not guaranteed to be negative-definite
    * the search direction of Newton’s method may not be an ascent direction
  *  the variance of sample-based estimators of the Hessian will be larger than that of estimators of the gradient.
* to efficiently mimic Newton’s method
  * quasi-Newton methods
    * designed to efficiently mimic Newton’s method using only evaluations of
      the gradient obtained during previous iterations of the algorithm.
  * Gauss-Newton method
    * is particular to non-linear least squares objective functions, for which the Hessian has a particular structure.
    * Due to this structure there exist certain terms in the Hessian that can be used as a useful proxy for the Hessian

## 2. Preliminaries and Background
* two forms of policy search algorithm in this paper:
  * methods based on iteratively optimizing a lower-bound on the objective function,
    e.g. the expectation maximization (EM) algorithm
  * gradient-based optimization methods
* Policy search update using
  * gradient ascent
  * Natural Gradient Ascent

## 3. The Hessian of the Total Expected Discounted Return
TODO

## 4. Gauss-Newton Methods for Markov Decision Processes
### 4.1 The Gauss-Newton Methods
* drops the Hessian terms which are difficult to estimate, but
  are expected to be negligible in the vicinity of local optima

## comment
* relatively old work:
  no neural network, no openai gym env
