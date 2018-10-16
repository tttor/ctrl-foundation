# Natural actor–critic algorithms
* Shalabh Bhatnagar and Richard S. Sutton and Mohammad Ghavamzadeh and Mark Lee
* Automatica 2009

# intro
* Theoretical analysis and empirical evaluations
have highlighted a major shortcoming of these algorithms, namely,
the high variance of their gradient estimates, and thus the slow
convergence and sample inefficiency.
* the policy
gradient in (1) is replaced with a natural version. This is motivated
by the intuition that a change in the policy parameterization
should not influence the result of the policy update. In terms
of the policy update rule (1), the move to natural gradient
amounts to linearly transforming the gradient using the inverse
Fisher information matrix of the policy
* Actor–critic methods are based on
the simultaneous online estimation of the parameters of two
structures, called the actor and the critic. The actor corresponds to
a conventional action–selection policy, mapping states to actions
in a probabilistic manner. The critic corresponds to a conventional
state-value function, mapping states to expected cumulative
future reward. Thus, the critic addresses a problem of prediction,
whereas the actor is concerned with control.
