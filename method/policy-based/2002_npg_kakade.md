# Natural policy gradient
* S.A. Kakade
* nips2002

## problem
* the standard gradient descent rule is non-covariant
  * the rule !:l.()i = oJ] f / a()i is dimensionally inconsistent
    since the left hand side has units of ()i and the right hand side has units of l/()i
    (and all ()i do not necessarily have the same dimensions).

## idea
* present a covariant gradient by defining a metric based on the
  underlying structure of the policy
* make the connection to policy iteration
  by showing that the natural gradient is moving toward choosing a greedy optimal
  action.
* make the assumption that every policy 7r is **ergodic**,
  * ie has a well-defined stationary distribution p7

## result
* the F does not asymptotically converge to the Hessian, so
  conjugate gradient methods might be more sensible asymptotically.
* far from the converge point, the Hessian is not necessarily
  informative, and the natural gradient could be more efficient
  * natural gradient is pushing the policy toward choosing greedy optimal actions.
    Often, the region (in parameter space) far from from the maximum is where large
    performance changes could occur. Sufficiently close to the maximum, little perfor-
    mance change occurs (due to the small gradient), so although conjugate methods
    might converge faster near the maximum, the corresponding performance change
    might be negligible.
*  suggests that the plateau phenomenon might not be as severe using this nat grad method.

## background
* Amari [1], it is better to define a metric based not
  on the choice of coordinates but rather on the manifold (ie the surface) that these
  coordinates parameterize.
* This function approximator is
  compatible with the policy in the sense that if we use the approximations f7r (s, a; w)
  in lieu of their true values to compute the gradient (equation 1), then the result
  would still be exact

## comment
* ? non-covariant?
> the standard gradient descent rule is non-covariant
