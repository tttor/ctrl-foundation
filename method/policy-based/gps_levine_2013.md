# Guided Policy Search
* Sergey Levine, Vladlen Koltun
* icml2013
* http://proceedings.mlr.press/v28/levine13.html
* https://graphics.stanford.edu/projects/gpspaper/gps_full.pdf
* http://rll.berkeley.edu/gps/

## problem
* complex policies with hundreds of parameters often requires numerous samples and 
  often falling into poor local optima.
  
## idea
* a guided policy search algorithm that uses trajectory optimization to 
  direct policy learning and avoid poor local optima.
* use differential dynamic programming to generate suitable guiding samples,
  which assist the policy search by exploring high-reward regions
* GPS: a policy search that incorporates guiding samples into the policy search. 
  * These samples are drawn from a distribution built around a DDP solution,
    which can be initialized from demonstrations. 

## result
* proposed sampling scheme and regularizer are essential for good performance, and 
* the learned policies can generalize successfully to new environments.

## background
* Standard likelihood ratio methods 
  * require new samples from the current policy at each gradient step, 
  * do not admit off-policy samples, and 
  * require the learning rate to be chosen carefully to ensure convergence.
  
## comment
* GPS uses importance sampling as a way to reduce variance
