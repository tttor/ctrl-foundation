# Reinforcement learning for non-prehensile manipulation: Transfer from simulation to physical system
* Kendall Lowrey, Svetoslav Kolev, Jeremy Dao, Aravind Rajeswaran, Emanuel Todorov
* https://arxiv.org/abs/1803.10371
* https://sites.google.com/view/phantomsim2real

## problem
* (Most) Reinforcement learning's results have been limited to simulation due to 
  * the need for a large number of samples and 
  * the lack of automated-yet-safe data collection methods.
*  mismatch between the simulator and the real world in model-based RL

## idea
* a modified form of the natural policy gradient algorithm for learning,
  applied to a **carefully identified** simulation model.

## setup
* three Phantom robots pushing an object to various desired target positions.

## result   
* The resulting policies, **trained entirely in simulation**, work well on the physical system without additional training. 
* training with an ensemble of models makes the learned policies more **robust to modeling errors**, thus 
  compensating for difficulties in system identification. 
  
