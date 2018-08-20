# Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator
* Maryam Fazel et al
* icml2018
* http://proceedings.mlr.press/v80/fazel18a/fazel18a.pdf

## problem
* even in the most basic continuous
control problem (that of linear quadratic regu-
lators), these methods must solve a non-convex
optimization problem, where little is understood
about their efficiency from both computational
and statistical perspectives.
* little is understood as to how direct (model-
free) policy gradient methods fare.

## idea
* builds bridges between these two lines of work,
namely, between optimal control theory and sample based
reinforcement learning methods, using ideas from mathe-
matical optimization

## result
* showing that (model
free) policy gradient methods globally converge to
the optimal solution and are efficient (polynomi-
ally so in relevant problem dependent quantities)
with regards to their sample and computational
complexities
* provided provable guarantees that model-
based gradient methods and model-free (sample based) pol-
icy gradient methods convergence to the globally optimal
solution, with finite polynomial computational and sam-
ple complexities
* showed how the Gauss-Newton algorithm improves
over even the natural policy gradient method, in the ex-
act case. A practically relevant question for the Gauss-
Newton method would be how to both: a) construct a
sample based estimator b) extend this scheme to deal
with (non-linear) parametric policies.
* provide a guarantee
that the natural gradient method enjoys a considerably
improved convergence rate over its naive gradient coun-
terpart
