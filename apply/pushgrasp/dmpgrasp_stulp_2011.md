# Learning to Grasp under Uncertainty
* Freek Stulp, Evangelos Theodorou, Jonas Buchli, Stefan Schaal
* http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5979644

## problem
* enables robots to  learn motion primitives that are robust towards state estimation
  uncertainties: to maneuver into a pose at which closing the hand to perform
  the grasp is more likely to succeed.
* a very challenging reinforcement learning (RL) problem, because:
  * the problem space is continuous and high-dimensional;
  * the terminal reward is boolean, and hence not very informative;
  * the actual and observed location vary randomly during learning, so the same
    grasp might sometimes succeed and sometimes fail, which leads to a noisy reward signal;
  * the reaching trajectory and actual grasp are not independent, and must be optimized simultaneously.

## observation
* key to acquiring robust motion primitives is to sample the actual pose of the object from
  a distribution that represents the state estimation uncertainty.

## idea
* using Dynamic Movement Primitives and
  the probabilistic model-free RL algorithm Policy Improvement with Path Integrals (PI2).
  * a DMP is initialized with a preshape and grasp posture as determined by
    the open-source grasp planner GRASPIT! [12].
  * This DMP is then optimized for successful grasping with model-free
    probabilistic reinforcement learning, where the cost function
    is a boolean that specifies whether the grasp was successful or not.

## assumption
* it is always preferable to use a motion primitive that has been
  trained to deal with state estimation uncertainty, rather than one that has not.
* During learning, the robot al ways assumes the object is at the mode of the probability
  distribution representing the position of the object.

## setup
* simulator: Simulation Laboratory (SL) software package
* A grasp is deemed successful if the relative position of
  the object to the gripper is within 3mm of the relative position determined by GRASPIT !
* simulation, with a Barret arm (7DOF) and hand (4DOF)

## result
* an approach that optimizes grasp
  success probability in the face of state estimation uncertainty.

## misc
* hand preshaping: the movement of the hand towards the grasp
* Dynamic Movement Primitives (DMPs):
  a flexible representation for motion primitives, which consist of
  a set of dynamic system equations that generate goal-directed movements.

## comment
* model-free, but used simulator to simulate real-world
* offline as states
> The resulting motion primitive does not explicitly reason
about state estimation uncertainties on-line; these uncertain-
ties are rather compiled implicitly into the motion primitive
during learning.
* this paper is more on low-level control
