# High-Dimensional Continuous Control Using Generalized Advantage Estimation
* John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, Pieter Abbeel
* iclr2016: poster
* https://arxiv.org/abs/1506.02438

## problem
* bias is more pernicious
  * even with an unlimited number of samples, bias can cause the algorithm to fail to converge,
    or to converge to a poor solution that is not even a local optimum

## idea: GAE
* key to variance reduction is to obtain good estimates of the advantage function
* generalized advantage estimator, which has two parameters γ, λ which adjust the bias-variance tradeoff.
* propose the use of a trust region optimization method for the value function
