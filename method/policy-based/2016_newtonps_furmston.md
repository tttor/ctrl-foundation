# Approximate Newton Methods for Policy Search in Markov Decision Processes
* Thomas Furmston et al
* jmlr2017
* http://jmlr.org/papers/v17/15-414.html
* https://arxiv.org/abs/1507.08271 # A Gauss-Newton Method for MDPs

## problem
* (stochastic) gradient ascent
  (as in (Williams, 1992; Baxter and Bartlett, 2001; Sutton et al., 2000))
  suffers from
  * not scale invariant
  * the search direction is often poorly-scaled,
    ( i.e., the variation of the
    objective function differs dramatically along the different components of the gradient.)
    * leads to a poor rate of convergence
    * makes the construction of a good step size sequence a difficult problem

## observation
* less attention is the application of Newton’s method to Markov decision processes.
  * the construction and inversion of the Hessian is too computationally expensive to be feasible
  * the objective function of a MDP is typically not concave, and
    * so the Hessian is not guaranteed to be negative-definite
    * the search direction of Newton’s method may not be an ascent direction
  * the variance of sample-based estimators of the Hessian will be larger than
    that of estimators of the gradient.

## idea
* consider whether an analogue to the Gauss-Newton
  method exists, so that the benefits of such methods can be applied to MDPs
* the Gauss-Newton Methods
  * drops the Hessian terms which are difficult to estimate, but
    are expected to be negligible in the vicinity of local optima
* the second Gauss-Newton method has important performance guarantees including:
  * a guaranteed ascent direction;
  * **linear** convergence to a local optimum under a step size which does not depend upon unknown quantities;
  * invariance to affine transformations of the parameter space; and
  * efficient estimation procedures for the preconditioning matrix.
  * (closely related to both the EM and natural gradient algorithms)
  * $\mathcal{H}_2$ incorporates information about the reward structure
    of the objective function that is not present in the Fisher information matrix.
* consider a diagonal form of the approximation for both forms of
  Gauss- Newton methods.

## setup
* task:
  * the synthetic two-dimensional non-linear MDP con-
    sidered in the work of Vlassis et al. (2009).
  * N -link Rigid Manipulator Experiment
  * Tetris Experiment
  * robot arm application:
    * ball-in-a-cup domain
    * use the Simulation Lab (Schaal, 2006) environment
* consider gradient ascent, natural gradient ascent,
  expectation maximisation and the second Gauss-Newton metho
* repeated the experiment 100 times, each time
  with a different random initialisation of the system.
* The **step size** sequences of gradient ascent, natural gradient ascent and
  the Gauss-Newton method were **all tuned for performance**
* To account for this variation the
  results from each run of the experiment are normalized by the maximal value achieved be-
  tween the algorithms in that run.
  * This means that the results displayed are the percentages
    of reward received in comparison to the best results among the algorithms considered in the experiment.

## result
* provide a novel analysis of the Hessian of the total expected reward,
  which is a standard objective function for policy optimization
* whether policy parameterisation is sufficiently rich, in the sense that
  it is $\epsilon$-value-consistent with
  an appropriately small value of $\epsilon$,
  * then the remaining terms in the Hessian become negligible in the vicinity of a local optimum
* (second Gauss-Newton) > EM-algorithm
* contrib
  * present an analysis of the Hessian of the total expected reward,
  * provide two Gauss-Newton type methods for policy optimization in MDPs
  * relate the search direction of our second Gauss-Newton algorithm to
    that of expectation maximization (which provides new insights into the latter algo-
    rithm when used for policy search), and we also discuss its relationship to the natural
    gradient algorithm.
* future work is
  * to extend this analysis to the stochastic
    setting, in which these quantities are estimated from samples of the MDP, either through a
    Monte-Carlo approach or in a stochastic approximation framework.

## background
* Policy search algorithms
  * are typically specialized applications of techniques from numerical optimization
    (Nocedal and Wright, 2006; Dempster et al., 1977).
  * As such, the controller is given a differentiable parameterisation and
    an objective function is defined in terms of this parameterisation.
* Two approaches that have proven to be particularly popular are
  (as alternative to policy gradient ascent)
  * expectation maximization (Dempster et al., 1977)
    * EM searches for the optimal policy by iteratively optimizinglower bound on the objective function
  * natural gradient ascent
* desirable properties of the natural gradient approach:
  * the Fisher in- formation matrix is always positive-semidefinite, regardless of the policy parameterisation
  * the search direction is invariant to the parameterisation of the policy
  * the natural gradient update direction
    can be obtained by regressing the state-action value function, or the advantage function,
    using a compatible function approximator (Sutton et al., 2000), and minimizing a square
    loss weighted by the (discounted) trajectory distribution (Kakade, 2002)
  * the rate of convergence of natural gradient ascent
    is **the same as gradient ascent**, i.e., linear, although,
    it has been noted to be substantially faster in practice.
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
* It is **not possible** to calculate the gradient exactly for
  many real-world MDPs of interest.
  * in discrete domains the size of the state-action space may be too large for enu- meration over these sets to be feasible.   * in continuous domains the presence of non-linearities in the transition dynamics makes
    the calculation of the occupancy marginals an intractable problem.
  * it can be the case that P and R are unknown in practice.
  * preferable to directly estimate the gradient using samples obtained from the environment,
    rather than building a model of the MDP
    * eg Monte carlo policy gradient, actor-critic policy gradient methods
* Various techniques have been proposed in the literature to estimate the gradient, including
  * the method of finite-differences (Kiefer and Wolfowitz, 1952; Kohl and Stone, 2004; Tedrake and Zhang,
2005),
  * simultaneous perturbation methods (Spall, 1992; Spall and Cristion, 1998; Srinivasan
et al., 2006) and
  * likelihood-ratio methods (Glynn, 1986, 1990; Williams, 1992; Baxter and
Bartlett, 2001; Konda and Tsitsiklis, 2003, 1999; Sutton et al., 2000; Bhatnagar et al., 2009;
Kober and Peters, 2011), including
    * Monte-Carlo methods (Williams, 1992; Baxter and Bartlett, 2001) and
    * actor-critic methods (Konda and Tsitsiklis, 2003, 1999; Sutton et al., 2000; Bhatnagar et al., 2009; Kober and Peters, 2011).

## comment
* no neural network (either as policy rep or fn approx or both)
* no standard test sets, eg openai gym env
* no comparison with other recent methods, eg. A2C
* ? shared param, w, for both actor and critic?
