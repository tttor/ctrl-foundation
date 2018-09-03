# How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments
* Cédric Colas, Olivier Sigaud and Pierre-Yves Oudeyer
* https://github.com/flowersteam/rl-difference-testing

# abs
* explain how the number of random seeds relates to the probabilities of statistical errors
  *  for both the t-test and the bootstrap confidence interval test

# intro
* scientific papers often omit parts of the implementation tricks
* Henderson et al., 2017),
  * that different implementations of the same algorithm with the same set of hyper-parameters
    led to drastically different results.
  * running the same algorithm 10
    times with the same hyper-parameters using 10 different random seeds and
    averaging performance over two splits of 5 seeds can lead to learning curves
    seemingly coming from different statistical distributions.
  * to use more random seeds, to average more different
  trials in order to obtain a more robust measure of the algorithm performance

# 2 Definition of the statistical problem
*  the mean characterizes the expected value of a realization,
* the standard deviation
  evaluates the square root of the squared deviations to this mean, or in simpler
  words, how far from the mean the realization are expected to fall.
* the values of μ and σ are unknown
  * to compute their unbiased estimations x and s:
    called the **empirical mean**, and s is called the **empirical standard deviation**, Equ 1
  * The larger the sample size N , the more confidence one can be in the estimations.
* Testing for a difference between the performances of two algorithms (μ1 and
  μ2 ) is mathematically equivalent to **testing a difference** between their difference
  μdiff and 0.

## 2.2 Comparing performances with a difference test
TODO
