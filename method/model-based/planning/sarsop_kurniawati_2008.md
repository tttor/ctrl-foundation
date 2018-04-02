# SARSOP: Efficient Point-Based POMDP Planning by Approximating Optimally Reachable Belief Spaces
* Hanna Kurniawati, David Hsu, Wee Sun Lee

## problem
* high computational complexity of POMDP mathematical framework for solving motion planning in uncertain and dynamic environ
* difficult to sample a representative set of points from B, due to its large size

## idea: SARSOP (Successive Approximations of the Reachable Space under Optimal Policies)
* new point-based POMDP algorithm that
  exploits the notion of optimally reachable belief spaces to improve computational efficiency.
* approximating optimally reachable spaces through sampling led to the more
  effective sampling and pruning strategies
* to sample near  the subset of belief points reachable from `$b_0$` under optimal sequences of actions,
* to compute successive approximations of `$R^* (b_0)$` and converge to it iteratively.
  * relies on heuristic exploration to sample `R(b_0)` and
  * improves sampling over time through a simple on-line learning technique.
  * usesa bounding technique to avoid sampling in regions that
    are unlikely to be optimal and focus sampling on the region near `$R^* (b_0)$`,
    the subset of B most relevant to the POMDP solution.
* By pruning away sampled points that are suboptimal, i.e., outside `$R^* (b_0)$`,
  we can reduce the size of the set of hyperplanes (which represent the value function),
  thus further improving computational efficiency.
* to sample the optimally reachable space through
  learning-enhanced exploration and a bounding technique.

## setup
* In simulation:
  coastal navigation, grasping, mobile robot exploration, and target tracking,
* compare against: HSVI2 (zmdp v1.1.3)

## result
* SARSOP substantially outperformed HSVI2 (In five out of the six tasks)
* On Rock Sample, SARSOP did not perform as well as HSVI2
  * HSVI2 implements an α-vector masking technique, which
    opportunistically computes only selected entries in the α-vectors.

## misc
* Point-based algorithms have greatly improved the speed of
  POMDP solution by sampling from the reachable space.
* one key idea of point-based POMDP algorithms is
  to sample a set of points from B and use it as an approximate representation of B,
  instead of representing B exactly.
* some point-based algorithms sample only the subset of belief points reachable
  from a given initial point under arbitrary sequences of actions
* One important idea shared by the point-based algorithms is
  (They differ in how they sample the belief space and perform backup operations.)
  * to sample a representative set of points from the belief space B and
  * compute an approximately optimal value function by performing backup operations
    over the sampled points rather than the entire B.
