# Guide actor-critic for continuous control
* Voot Tangkaratt et al
* iclr2018: poster
* https://openreview.net/pdf?id=BJk59JZ0b
* https://openreview.net/forum?id=BJk59JZ0b
* https://arxiv.org/abs/1705.07606
* https://github.com/voot-t/guide-actor-critic

## problem
* existing actor-critic methods **only** use values or gradients of the critic to update the policy parameter
  * ignore higher-order ones such as gradients and Hessians w.r.t. actions of the critic
  * they only use the value of the critic, i.e., the zero-th order information, and
    ignore higher-order ones such as gradients and Hessians w.r.t. actions of the critic1.
    * To the best of our knowledge, the only actor-critic methods
      that use gradients of the critic to update the actor are deterministic policy gradients (DPG) (Silver
      et al., 2014) and stochastic value gradients (Heess et al., 2015). However, these two methods do not
      utilize the second-order information of the critic

## observation
* the Hessian of the critic can accelerate actor learning which leads to higher data efficiency
  * this is different from using the gradient of the critic w.r.t. critic parameters to **update the critic itself**

## idea: guide actor-critic (GAC).
* the actor update of GAC utilizes the second-order information of the critic
  in a computationally efficient manner;
  by separating actor learning into two steps.
  * first step, we learn a non-parameterized Gaussian actor that locally maximizes the critic
    under a Kullback-Leibler (KL) divergence constraint.
  * the Gaussian guide actor is used as a guide for learning a parameterized actor
    by supervised learning
* proof of second-order optimization in action space

## setup
?

## result
* learning the mean of the Gaussian actor is equivalent to
  performing a second-order update in the action space where the curvature matrix is given by Hessians of the critic and
  the step-size is controlled by the KL constraint.
* the deterministic policy gradient method is a special case of GAC when the Hessians are ignored.
* contrib: guide actor

## background
* the main idea of second-order methods is to rotate the gradient by the inverse of a curvature matrix.
  * eg the Newton method
    * where its curvature matrix is the Hessian of the objective function w.r.t. the optimization variables
  * eg natural gradient method
    * uses the Fisher information matrix (FIM) as the curvature matrix
    * Unlike the Hessian matrix, FIM provides information about changes of the policy measured by
      an approximated KL divergence

## comment
* key: second order of the critic to update the **guide** actor
* (-) no comparison with ACKTR
* (-) "promising" means there is no significant advantage over other methods
> we show that our method is a promising ...
* ?: not sure what does this mean:
  * actor there means the guide actor
> The goal of these methods is to learn an actor that maximizes the critic
* ?: how to do this?
> Gaussian actor is used as a guide for learning a parameterized actor by supervised learning
* ?: guide actor is gaussian?
  * ans: yes
> on page 5: First, we assume that the actor is the Gaussian distribution
<!-- * This seems not totally right
  * should be:
    the actor is update in the direction of gradient of policy performance
  * what does it mean with "maximize critic"?
    * this is from Equ 5
    * but, the goal is to max expected return from start state, ie $V(s_0)$
> Actor-critic methods solve reinforcement learning problems by updating a param-
eterized policy known as an actor in a direction that increases an estimate of the
expected return known as a critic.
> The goal of these methods is to learn an actor that maximizes the critic.
> we learn a non-parameterized Gaussian actor that
locally maximizes the critic under a Kullback-Leibler (KL) divergence constraint -->
* still do not understand about
  how to use gradient or 2nd order info of the critic in pol grad theorem, recall that policy grad is the grad of expected return from start state
>  they only use the value
of the critic, i.e., the zero-th order information, and ignore higher-order ones such as gradients and
Hessians w.r.t. actions of the critic
