# Learning Neural Network Policies with Guided Policy Search
Sergey Levine and Pieter Abbeel;
NIPS 2014;

## problem
* robotic manipulation tasks 
  * in partially observed environments 
  * with numerous contact discontinuities and underactuation

## observation
* Stabilizing linear-Gaussian controllers is easier than stabilizing arbitrary policies

## idea
* a hybrid method that fits **local, time-varying linear dynamics models**, which 
  are not accurate enough for standard model-based policy search. 
  * use these local linear models to efficiently optimize a time-varying linear-Gaussian controller, which 
    induces an approximately Gaussian distribution over trajectories. 
  * to restrict the change in the trajectory distribution at each iteration, so that 
    the time-varying linear model remains valid under the new distribution. 
  * Since the trajectory distribution is approximately Gaussian, this can be done efficiently, 
    in terms of both sample count and computation time.
* optimizes a time-varying linear-Gaussian policy $p(u_t|x_t) = N(K_t x_t + k_t, C_t)$, which 
  allows for a particularly efficient optimization method when 
  the initial state distribution is narrow and approximately Gaussian. 
* builds on the iterative linear-Gaussian regulator (iLQG), which 
  optimizes trajectories by iteratively constructing locally optimal linear feedback controllers under 
  a local linearization of the dynamics and a quadratic expansion of the cost
  * unlike iLQG, our method operates on systems where the dynamics are unknown.

## setup
* neural network policies
* task: 
  * peg insertion: the precise position of the hole is unknown at test time.  
  * high-dimensional octopus arm control, swimming, and bipedal walking.
  
## misc
* trajectory-centric policy learning, e.g dynamics motion primitives (DMPs)
* Policy search consists of **optimizing** the parameters θ of a policy πθ(ut|xt), which is 
  a distribution over actions $u_t$ conditioned on states $x_t$, 
  with respect to the **expectation of a cost** (x_t,u_t)$, denoted $E_{\pi_{\theta}}[\sum_{t=1}^T (xt,ut)]$. 
  * The expectation is under the policy and the dynamics p(xt+1|xt,ut), which 
    together form a distribution over trajectories τ. 
* a time-varying linear-Gaussian policy $p(u_t|x_t) = N(K_t x_t + k_t, C_t)$

## comment
* use local linear-Gaussian approx to the dynamics
