# Configuration Lattices for Planar Contact Manipulation Under Uncertainty
* Michael Koval, David Hsu, Nancy Pollard and Siddhartha Srinivasa
* Conference Paper, Workshop on the Algorithmic Foundations of Robotics, December, 2016
* https://www.ri.cmu.edu/publications/configuration-lattices-for-planar-contact-manipulation-under-uncertainty/

## problem
* a robot using real-time feedback from contact sensors to reliably manipulate a movable object on a cluttered tabletop

## idea
* formulate the problem of planar contact manipulation under uncertainty as a POMDP
  in the joint space of robot configurations and poses of the movable object;
  * state $s = (q, x_o) \in S$ is 
    * the configuration of the robot $q \in Q$
    * the pose of the movable object $x_o \in X_o = SE(3)$
  * an action $a = (\xi, t) \in a$ is 
    * a trajectory $\xi: [0, t ] \mapsto q$ that starts in configuration $\xi(0)$ and 
      ends configuration $\xi(t)$ at time $t$,
      which means joint-position controller with time contraint~$T$;
      restrict to actions that are instantiated from one of a finite set of action templates;
  * observation $o \in \{0, 1\}^{n_o}$ from its $n_o$ binary contact sensors
  * goal is to push the movable object into a hand-relative goal region
  * the stochastic transition model in terms of a deterministic quasistatic physics model
    by introducing noise into its parameters
  * reward function that assigns $R(s, a) = 0$ for states  in the goal region and $R(s, a) = −1$ otherwise.
* simplify the problem by constraining the end effector to a fixed transformation
  relative to the support surface and build a lattice in configuration space
  (represents the robot’s configuration space as a state lattice)
* configurations in the lattice are connected by action templates that start and end on lattice points
  and are penalized if rendered infeasible by kinematic constraints
* to construct this lattice, 
  (lazily construct a discrete lattice in the robot’s configuration space;
  to defer collision checking until an action is queried by the planner)
  * select a configuration qlat (xr) using an iterative inverse kinematics solver initialized with 
    the solution of an adjacent lattice point.
  * use a cartesian motion planner to find a trajectory that connects adjacent points while satisfying the action template.
* guide the search with heuristics derived from an unconstrained relaxation of the problem.
* plan to take information gathering actions to force the bottle into contact with one of its sensors
* theorem: an optimal policy of Lat-POMDP will not execute an infeasible action in belief $b$ if ...

## assumption
* operates in an environment with known obstacles
* quasistatic assumption: friction is high enough to neglect acceleration of the object,
  i.e. the object stops moving as soon as it leaves contact
* uncertainty over object pose dominates controller and proprioceptive error;
  therefore, we treat $q$ as fully-observable (perfect proprioception) and
  assume that the manipulator is perfectly position controlled (deterministic transition model for robot configuration).
* have access to a local planner that returns a singleton action from the set of all possible
  instantiations of action template or to indicate failure, due to kinematic constraints or robot collision.
* assume that an observation model is available
* the robot’s end effector and the movable object are constrained to have
  a fixed transformation relative to the support surface; this means the object is never toppled.
*  access to an inverse kinematics function that returns a single solution that satisfies or
  $\emptyset$ if no such solution exists, because not reachable or in collision
* movable object only contacts the end effector, not other parts of the
  robot or the environment
* an observation model is assumed available
  
## setups
* solve the POMDP using DESPOT,
  guided with upper and lower bounds derived from a relaxation of the
  problem that considers only the pose of the movable object relative to the hand.
* Box2D physics simulator:
  simulate uncertainty in the model by sampling the hand-object friction coefficient and
  center of the object-table pressure distribution at each timestep
* Forward kinematics, inverse kinematics, and collision detection is provided by
  the Dynamic Animation and Robotics Toolkit (DART)
*  discretize a region  around the palm at a 1 cm resolution
*  a simulation of HERB [44], with a 7-DOF Barrett WAM arm ,
  to push a bottle into the center of its palm on a table littered with obstacles
* parameterize object pose as $(x_o, y_o, \theta_o )$
* discretize the space of the end effector poses by constructing a state
  lattice with a translational and an angular resolutions

## result
* a near-optimal policy for Lat-POMDP using DESPOT [43] guided by upper and lower bounds derived from Rel-POMDP
* Lat-DESPOT outperforms five baseline algorithms on cluttered environments:
  it achieves a 90% success rate on all environments, compared to the best baseline (Lift-SARSOP) that
  achieves only a 20% success rate on difficult problems
* suggests:
  * a stochastic model that considers the probability of hitting an obstacle.
  * non-planar motion
  * planning in environments that contain multiple movable objects
  * generating multiple inverse kinematic solutions for each lattice point and
    instantiating an action template for each

## misc
* kinematic constraints: reachability, joint limits, and collision.
* the choice of $-1$ reward is arbitrary: any negative reward would suffice.

## comment
* simulated robots only
* the configuration lattice is 2-dim xy planar with resolution of 1 cm;
  end effector is at a fixed height
* the assumption of observation model is possible because the experiments are only in simulator,
  in real world, we have to formulate it from empirical data
* note the action space that consists of action templates
* set table to be littered with obstacles, but assume that
  the target object can only be in contact with the robot
* why assume that observation error dominates transition error?
  does separate transition error significantly make the problem more complex?
