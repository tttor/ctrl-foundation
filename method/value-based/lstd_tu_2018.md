# Least-Squares Temporal Difference Learning for the Linear Quadratic Regulator
* Stephen Tu, Benjamin Recht,
* icml2018
* https://people.eecs.berkeley.edu/~brecht/l2c-icml2018/
* https://www.youtube.com/watch?v=WpHPMqzufJY

# problem
* low sample efficiency of RL
* A more rigorous foundation could help to differentiate
  between whether RL suffers from fundamental statistical
  limitations in the continuous setting, or if more sample effi-
  cient estimators are possible.
* how well do model-free RL methods perform on the LQR problem.

# idea
*  studied the number of samples needed for the LSTD
estimator to return a ε-accurate solution in relative error
for the value function associated to a fixed policy π for LQR.

# setup
* compare model-free Least-Squares Policy Iteration (LSPI) algorithm (Lagoudakis & Parr, 2003)
  * WITH the model-based methods proposed in Dean et al.
* compare model-free policy iteration (LSPI) to two model-based
methods: (a) the naı̈ve nominal model controller which
uses a controller designed assuming that the nominal model
has zero error, and (b) a controller based on a semidefinite
relaxation to the non-convex robust control problem with
static state-feedback.

# result
* an upper bound on the necessary length of a single trajectory
  to estimate the value function of a stabilizing state-feedback policy
  * Letting n denote the dimension of the state and ig-
    noring instance specific factors, we establish that roughly
    n2 /ε2 samples are sufficient to estimate the value function
    up to ε-relative error.
* model-free LSPI can be substantially less sample efficient
  and less robust compared to model-based methods

# background
* LSTD:
  * Given a
    sample trajectory from a Markov Decision Process (MDP)
    in feedback with a fixed policy π, LSTD computes the value
    function V π associated to π
  * the linear-architecture assumption, which states that the
    value function can be expressed as a linear function after
    applying a known non-linear transformation to the state

# comment
* specific to LSPI+LSTD estimator for LQR:
  * ie sample complexity of the LSTD estimator on LQR
  * in model-free, and value-based classes
  * no policy grad
* key concepts:
  * LQR, LSTD, LSPI
* is not this obvious already? that model-based is one way to improve (world-)sample efficiency
>  Empirically, we demonstrated
that model-free policy iteration (LSPI) requires substantially
more samples on certain LQR instances than the model-
based methods from Dean et al.

