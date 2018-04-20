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
* Combining pushing and grasping policies for sequential manipulation
  * current work limit the types of synergistic behaviors between pushing and grasping that can be performed

## idea: VPG: visual pushing for grasping
* a model-free rl framework for learning pushing and grasping policies in
  a mutually supportive way (complementary)
* to discover and learn synergies between pushing and grasping from experience through
  model-free deep reinforcement learning (in particular, Q-learning).
  * learn joint pushing and grasping policies through self-supervised trial and error.
    * Pushing actions are useful only if, in time, enable grasping.
  * train our policies end-to-end with a deep network that
    * takes in visual observations and
    * outputs expected return (i.e. in the form of Q values) for potential pushing and grasping actions.
* state rep: RGB-D image
  * RGB color
  * height from bottom, D
* 2 primitive actions, defined in workspace
  * pushing: execute straight trajetory
  * grasping: both fingers attempt to move x cm below q
* learning fully convolutional action-value fn
  * huber loss
* reward

## setup
* two fully convolutional networks that
  map from visual observations to actions:
  * one infers the utility of pushes for a dense pixel-wise sampling of end effector orientations and locations, while
  * the other does the same for grasping.
* Both networks are trained jointly in a Q-learning framework and are entirely self-supervised by trial and error,
  where rewards are provided from successful grasps
* experiments in both simulation and real-world
* pytorch
* test time: greedy deterministic, small learning rate to avoid getting stuck

## result
* the synergy between planning non-prehensile (pushing) and prehensile (grasping) actions **can be learned** from ex- perience.
* our system learns to perform complex sequences of pushing and grasping on a real robot in tractable training times.
* the pushing policies enlarge the set of scenarios in which grasping succeeds, and
* both policies working in tandem produce complex interactions with objects (beyond our expectations) that
  support more efficient picking (e.g. pushing multiple blocks at a time, separating two objects,
  breaking up a cluster of objects through a chain of reactions that improves grasping)
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
* this uses (basic) Q-learning with vanilla DQN + FCN
* extensive engineering indeed to make the pipeline work
* questions
  * how did they train? pseudo or real model-free? offline or online?
  * self-supervised trial and error? in real or sim?
    * ans: robot automatically perform data collection by trial and error,
      both in sim and real
