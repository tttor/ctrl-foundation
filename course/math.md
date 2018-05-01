# math

## optimization: n-order
* "0th order methods" (Black box optimization)
  * blackbox stochastic search
  * Markov Chain Monte Carlo methods
  * evolutionary algorithms
* 1st order methods
  * plain grad., steepest descent, conjugate grad., Rprop, stochastic grad. 
  * adaptive stepsize heuristics
* 2nd order methods
  * Newton, Gauss-Newton, Quasi-Newton, (L)BFGS
  * constrained case, primal-dual Newton 
 
## optimization: convex, nonconvex
* https://www.solver.com/convex-optimization
* http://www.cs.cornell.edu/courses/cs6787/2017fa/Lecture7.pdf'
* https://stats.stackexchange.com/questions/106334/cost-function-of-neural-network-is-non-convex
* NIPS Workshop on Nonconvex Optimization for Machine Learning: Theory and Practice

## gradient
* https://en.wikipedia.org/wiki/Gradient
  * the gradient is a multi-variable generalization of the derivative.
  * While a derivative can be defined on functions of a single variable,
    for functions of several variables, the gradient takes its place.
  * The gradient is a vector-valued function, as opposed to a derivative, which is scalar-valued.
* https://github.com/tttor/talk/blob/master/tor/cvx-sgd-20180316/cvx_sgd_vektor_20180316121822.pdf # page 9/14
  * grad of differentiable fn is a vector of partial derivative of f

## logit
* https://en.wikipedia.org/wiki/Logit
  * If `p` is a probability, then `p/(1 − p)` is the corresponding odds;
  * the logit of the probability is the logarithm of the odds.
  * `logit(p) = log[p/(1-p)]`

## variate == random variable
* A variate is a generalization of the concept of a random variable 
  that is defined without reference to a particular type of probabilistic experiment. 
  It is defined as the set of all random variables that obey a given probabilistic law.
* http://mathworld.wolfram.com/Variate.html
