# pilqr_chebotar_2017

## problems
* real-world applications of RL have to contend with two often opposing requirements: 
  * data-efficient learning and 
  * the ability to handle complex, unknown dynamical systems that might be difficult to model
* Can we combine the efficiency of model-based algorithms with 
the final performance of model-free algorithms in a method that
we can practically use on real-world physical systems?

## ideas
* PILQR: a procedure for optimizing TVLG (time-varying linear-Gaussian) policies that integrates both 
  * fast model-based updates via iterative linear-Gaussian model fitting and 
  * corrective model-free updates via the PI2 framework.

## setups
* complex tasks, such as hockey and power plug plugging

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
?
