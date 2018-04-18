# Learning Synergies between Pushing and Grasping with Self-supervised Deep Reinforcement Learning
* Andy Zeng et al
* http://vpg.cs.princeton.edu
* https://arxiv.org/abs/1803.09956

## problem
* learning complementary pushing and grasping policies simultaneously from scratch with deep reinforcement learning.

## observation
* Skilled robotic manipulation benefits from complex synergies between 
  * non-prehensile (e.g. pushing) and 
    * pushing can help rearrange cluttered objects to make space for arms and fingers
  * pre- hensile (e.g. grasping) actions: 
    * grasping can help displace objects to make pushing movements more precise and collision-free.

## idea
* a framework for learning pushing and grasping policies in a mutually supportive way.

## setup
* two fully convolutional networks that 
  map from visual observations to actions: 
  * one infers the utility of pushes for a dense pixel-wise sampling of end effector orientations and locations, while 
  * the other does the same for grasping. 
* Both networks are trained jointly in a Q-learning framework and are entirely self-supervised by trial and error, 
  where rewards are provided from successful grasps
* experiments in both simulation and real-world

## result
* the synergy between planning non-prehensile (pushing) and prehensile (grasping) actions **can be learned** from ex- perience.
* our system learns to perform complex sequences of pushing and grasping on a real robot in tractable training times.
* limitation
  * motion primitives are defined with parameters specified on a regular grid (heightmap), which 
    provides learning efficiency with deep networks, but limits expressiveness
  * train our system only with blocks and test with a limited range of other shapes
  * study only synergies between pushing and grasping, which 
    are just two examples of the larger family of primitive manipulation actions, 
    e.g. rolling, toppling, squeezing, levering, stacking, among others
  
## comment
* syn between push+grasp brings to nav among movable obstacles
* the result of "... can be learned from experience" is somewhat not strong
* questions
  * how did they train? pseudo or real model-free?
  
