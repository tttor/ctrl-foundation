# Natural policy gradient
* S.A. Kakade
* nips2002

## problem
* the standard gradient descent rule is non-covariant

## result
*  the F does not asymptotically con-
verge to the Hessian, so conjugate gradient methods might be more sensible asymptotically.

## background
*  Amari [1], it is better to define a metric based not
on the choice of coordinates but rather on the manifold (ie the surface) that these
coordinates parameterize. 
* This function approximator is
compatible with the policy in the sense that if we use the approximations f7r (s, a; w)
in lieu of their true values to compute the gradient (equation 1), then the result
would still be exact

## comment
* ? non-covariant?
? the standard gradient descent rule is non-covariant
