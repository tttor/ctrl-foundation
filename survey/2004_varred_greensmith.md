# Variance Reduction Techniques for Gradient Estimates in Reinforcement Learning
* Evan Greensmith et al
* Journal of Machine Learning Research 5 (2004) 1471–1530

## abs
* the baseline and actor-critic methods can be interpreted as
  additive control variate variance reduction methods
* here, consider
  * the expected average reward performance measure
  * GPOMDP algorithm for estimating performance gradients in pomdp
*  For actor-critic algorithms, we show that using the true value function
as the critic can be suboptimal.

## intro
* Determining the gradient requires the calculation of an integral.
> We can produce an estimate of this integral through Monte Carlo techniques.
This changes the integration problem into one of calculating a weighted average of samples.
It turns out that these samples can be generated purely by watching the controller act in the environment (see Section 3.3).
However, this estimation tends to have a high variance associated with it, which
means a large number of steps is needed to obtain a good estimate.
* show that this may not be the best approach: selecting a value function to be equal
to the true discounted value function is not always the best choice

## 3.3 Monte Carlo Estimation
* Integrals can be estimated through the use of Monte Carlo techniques by averaging over samples
  taken from a particular distribution
