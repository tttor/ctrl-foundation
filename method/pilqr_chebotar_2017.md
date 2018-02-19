# pilqr_chebotar_2017

## problems
* real-world applications of RL have to contend with two often opposing requirements: 
  * data-efficient learning and 
  * the ability to handle complex, unknown dynamical systems that might be difficult to model
* Can we combine the efficiency of model-based algorithms with 
the final performance of model-free algorithms in a method that
we can practically use on real-world physical systems?

## ideas: PILQR
* a procedure for optimizing TVLG (time-varying linear-Gaussian) policies that integrates both 
  * fast model-based updates via iterative linear-Gaussian model fitting and 
  * corrective model-free updates via the PI2 framework.
* hybrid-ism: 
  * for model-based, based on iLQR, KL-constrained LQR (LQR-FLM)
  * for model-free, based on PI2
* Integrating Model-Based Updates into PI2
  * the PI2 update can be broken up into two parts, 
    * one part using a model-based cost approximation and 
    * another part using the residual cost error after this approximation. 
  * integrating model-based updates into PI2 by 
    * using our extension of LQR-FLM to optimize the linear-quadratic cost approximation and 
    * performing a subsequent update with PI2 on the residual cost.
    
## setups
* simulated: gripper pusher, door opening, reacher
* real: hockey, power plug plugging

## results
* PILQR prop:
   * naturally trades off between model-based and model-free updates based on the amount of model error, 
   * can easily be extended with a KL-divergence constraint for stable learning, and 
   * can be effectively used for real-world robotic learning.
* limitation
  * specific to TVLG policies
  * requires the ability to reset the environment into consistent initial states
  * both the model-based and model-free update requires a continuous action space
  
## comments
* essentially the integration of PI2 and LQR-FLM
