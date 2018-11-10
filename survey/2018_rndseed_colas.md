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
* draw a sample xdiff from Xdiff by subtracting two samples x1 and x2 obtained from X1 and X2
* consider asympothotic perf:
  Each point of a
  learning curve is the average cumulated reward over 10 evaluation episodes.
  The measure of performance Xi of Algo i is the average performance over
  the last 10 points (i.e. last 100 evaluation episodes)

## 2.2 Comparing performances with a difference test
* define the null hypothesis H0 and the alternate hypothesis Ha .
  * These hypotheses refer to the two-tail case
* The p-value answers
the following question: how probable is it to observe this sample or a more
extreme one, given that there is no true difference in the performances of both
algorithms?
* It is important to note that, when one is conduct-
  ing NE experiments, the false positive rate grows linearly with the number of
  experiments. In this case, one should use correction for multiple comparisons
  such as the Bonferroni correction
  * a false positive, to claim that there is a true difference when there is not.

## 2.3 Statistical errors
* Table 1: Hypothesis testing
  * true/false positive/negative for $H_0$, $H_a$
* The type-I error rejects H0 when it is true, also called false positive.
  * Choosing a significance level of α enforces a probability of
    type-I error α, under the assumptions of the statistical test.
  * The type-II error fails to reject H0 when it is false, also called false negative.
* A difference is said statistically significant when a statistical test
passed. One can reject the null hypothesis when 1) p-value< α; 2)
CI1 does not contain 0; 3) CI2 does not contain xdiff .

# 3 Choice of the appropriate statistical test
## 3.1 T-test and Welch’s t-test
* The t-statistics are assumed to follow a t-distribution, which is bell-shaped and
whose width depends on the degree of freedom. The higher this degree, the
thinner the distribution.
* next section gives
standard guidelines to select N so as to meet requirements for both α and β.

## 3.2 Bootstrapped confidence intervals
TODO

# conclusion
* Use the Welch’s t-test over the bootstrap confidence interval test.
* Set the significance level of a test to lower values (α < 0.05) so as
to make sure the probability of type-I error (empirical α) keeps
below 0.05.
* Correct for multiple comparisons in order to avoid the linear growth
of false positive with the number of experiments.
* Use at least n = 20 samples in the pilot study to compute robust
estimates of the standard deviations of both algorithms.
* Use larger sample size N than the one prescribed by the power
analysis. This helps compensating for potential inaccuracies in
the estimations of the standard deviations of the algorithms and
reduces the probability of type-II errors.

# comment
* ? still do not understand, $CI_2$, sec 2.2
* ? Correction procedures can be applied to correct for multiple comparisons.?
  (last bullets in Message 1)
* here, a priori refers to knowledge of whether the mean of experimnt 1 is greater than experiment 2
```
When an a priori on which algorithm
performs best is available, (say Algo1), one can use the one-tail version:
```
