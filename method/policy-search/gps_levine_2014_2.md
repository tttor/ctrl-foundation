# Learning Neural Network Policies with Guided Policy Search
NIPS 2014

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
 
## setup
* neural network policies
* task: 
  * peg insertion: the precise position of the hole is unknown at test time.  
  * high-dimensional octopus arm control, swimming, and bipedal walking.
  
## misc
* trajectory-centric policy learning, e.g dynamics motion primitives (DMPs)

## comment
