# Guide actor-critic for continuous control
* Voot Tangkaratt et al

## problem
* existing actor-critic methods only
use values or gradients of the critic to update the policy parameter

## idea: guide actor-critic (GAC).
* GAC
  * learns a **guide actor** that locally maximizes the critic
    * updates the guide actor by performing second-order optimization in the action space where
      the curvature matrix is based on the Hessians of the critic.
  * updates the policy parameter based on the guide actor by supervised learning.

## result
* the deterministic policy gradient method is a special case of GAC when the Hes-
sians are ignored.

## comment
* finish!
* "promising" means there is no significant advantage over other methods
> we show that our method is a promising ...
