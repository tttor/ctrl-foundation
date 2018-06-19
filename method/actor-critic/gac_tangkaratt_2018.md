# Guide actor-critic for continuous control
* Voot Tangkaratt et al
* iclr2018: poster
* https://openreview.net/pdf?id=BJk59JZ0b
* https://openreview.net/forum?id=BJk59JZ0b
* https://arxiv.org/abs/1705.07606
* https://github.com/voot-t/guide-actor-critic

## problem
* existing actor-critic methods **only**
  use values or gradients of the critic to update the policy parameter

## idea: guide actor-critic (GAC).
* learns a **guide actor** that locally maximizes the critic
  * updates the guide actor by performing **second-order optimization** in the action space 
    * where the curvature matrix is based on the Hessians of the critic.
* updates the policy parameter based on the guide actor by supervised learning.

## setup

## result
* the deterministic policy gradient method is a special case of GAC when
  the Hessians are ignored.
* contrib: guide actor

## comment
* "promising" means there is no significant advantage over other methods
> we show that our method is a promising ...
