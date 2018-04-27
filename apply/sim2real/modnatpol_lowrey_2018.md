# Reinforcement learning for non-prehensile manipulation: Transfer from simulation to physical system
* Kendall Lowrey, Svetoslav Kolev, Jeremy Dao, Aravind Rajeswaran, Emanuel Todorov
* https://arxiv.org/abs/1803.10371
* https://sites.google.com/view/phantomsim2real

## problem
* (Most continuous) RL's results have been limited to simulation due to 
  * the need for a large number of samples and 
  * the lack of automated-yet-safe data collection methods.
*  mismatch between the simulator and the real world in model-based RL
* few successful applications to real robots have been in tasks involving position or velocity control that 
  avoid some difficulties of torque-controlled platforms.

## idea
* a modified form of the natural policy gradient algorithm for learning,
  applied to a **carefully identified** simulation model.
* To obtain an accurate simulation model, we fit the parameters of the simulation model using 
  a physically consistent system identification procedure 
* To assess, as well as mitigate, the effects of modeling errors,
  we compare learning with respect to three different models: 
  * (i) the nominal model obtained from system identification; 
  * (ii) a modified model where we intentionally misspecify some model parameters; 
  * (iii) an ensemble of models where the mean is wrong but the variance is large enough to include the nominal model. 

## setup
* three Phantom robots pushing an object to various desired target positions.
* use a normalized natural policy gradient (NPG)
* avoid the use of an estimator (i.e. the use of a model to predict state like a Kalman filter) by 
  learning a function that directly converts from sensor values to motor torques.
* parametrize policiy as a multivariate Gaussian with diagonal covariance.
* implemented our RL code and interfaced with the MuJoCo simulator with the Julia programming language
* rely on a Vicon motion capture system ; assume the object remains upright and do not include orientation
* For system ID we collected various behaviors with the robots, 
  ranging from effector motion in free space to infer intrinsic robot parameters, to 
  manipulation examples such as touching, pushing and sliding between 
  the end effector and the object to infer contact parameters.

## result   
* The resulting policies, **trained entirely in simulation**, work well on the physical system without additional training. 
* training with an **ensemble of models** makes the learned policies more **robust to modeling errors**, thus 
  compensating for difficulties in system identification. 
* simulation based policy learning approach also conveniently allows for building robust controllers by 
  creating ensembles of models by varying physical parameters.
  * it can partially make up for incorrectly measured / identified model parameters.
  * allowing for more conservative policies to enable appropriate data collection for actual model improvement
  
## misc
* Leveraging a model in simulation can provide a useful policy to begin robot operation, which
  can subsequently be fine-tuned on hardware in a model-free mode.

## comment
* full observability
