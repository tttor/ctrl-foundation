# High-Dimensional Continuous Control Using Generalized Advantage Estimation
* John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, Pieter Abbeel
* iclr2016: poster
* https://arxiv.org/abs/1506.02438
* https://sites.google.com/site/gaepapersupp/
* https://danieltakeshi.github.io/2017/04/02/notes-on-the-generalized-advantage-estimation-paper/

## problem
* main challenges in policy gradient are
  * the large number of samples typically required, and
  * the difficulty of obtaining stable and steady improvement despite the nonstationarity of the incoming data.
* while high variance necessitates using more samples, **bias is more pernicious**
  * even with an unlimited number of samples, bias can cause the algorithm to fail to converge,
    or to converge to a poor solution that is not even a local optimum

## observation
* key to variance reduction is to obtain good estimates of the advantage function

## idea: GAE:  generalized advantage estimator
* use a **trust region optimization** method for the value function
* GAE has two parameters $\gamma$ and $\lambda$ which adjust the bias-variance tradeoff.
  * allows us to smoothly interpolate between the high-bias estimator (λ = 0) and the low-bias estimator (λ = 1).
* GAE, Equ 16,  as a variance reduction scheme
* The choice Ψt = Aπ (st, at ) yields almost the lowest possible variance,
  (in practice, the  advantage function is not known and must be estimated)
  * This statement can be intuitively justified by
  the following interpretation of the policy gradient: that a step in the policy gradient direction should
  increase the probability of better-than-average actions and decrease the probability of worse-than-average actions.

## setup
* combine this idea with trust region policy optimization and a trust region algorithm that optimizes a value function,
  * both represented by neural networks.

## result
* the bias is prohibitively large when using a one-step estimate of the returns
* contrib
  * address the first challenge by using value functions to substan-
   tially reduce the variance of policy gradient estimates at the cost of some bias, with
   an exponentially-weighted estimator of the advantage function that is analogous
   to TD(λ).
  * address the second challenge by using trust region optimization
    procedure for both the policy and the value function, which are represented by neural networks.
* future:
  * the relationship between value function estimation error and policy gradient estimation error.
  * shared function approximation architecture for the policy and the value function,

## background
* credit assignment problem:
  * the long time delay between actions and their positive or negative effect on rewards
* the variance of the gradient estimator scales unfavorably with the time horizon,
  * since the effect of an action is confounded with the effects of past and future actions.
* actor-critic methods use a value function rather than the empirical returns,
  obtaining an estimator with lower variance at the cost of introducing bias

## comment
* contrib
  * accurate estimate of critic (ie the advantage fn, $\hat{A}$)
  * using Trust Region to optimize the value function
* "...bias is more pernicious" is related to TD3 paper
* ? trust region opt for value fn, and what opt is for policy network?
* as said:
  * GAE where lambda=1 is equal to one-step actor-critic in Sutton book, where they use TD-residual
  * GAE where lambda=0 is equal to return minus predicted state-value as baseline
> Equ 16...  closely
analogous to the one used to define TD(λ) (Sutton & Barto, 1998), however TD(λ) is an estimator
of the value function, whereas here we are estimating the advantage function.

