# Path Integral Guided Policy Search
2017 IEEE International Conference on Robotics and Automation (ICRA)

## problem

## idea: path integral guided policy search
* extend GPS in the following ways: 
  * the use of a model-free local optimizer based on path integral stochastic optimal control, which 
    enables us to learn local policies for tasks with highly discontinuous contact dynamics; and 
  * enable GPS to train on a new set of task instances in every iteration by using on-policy sampling: 
    this increases the diversity of the instances that the policy is trained on, and 
    is crucial for achieving good generalization. 
*  main contributions 
  * a KL-constrained PI2 method for local policy optimization, 
  * a global policy sampling scheme for guided policy search that allows new task instances to be sampled at each iteration, 
    so as to increase the diversity of the data for training the global policy and thereby improve generalization.

## setup
* tasks:
  * door opening task and 
  * a pick-and-place task: localizing and grasping an object and then placing it upright at a desired target location
* pose detection using CNN,  visual features from the robot’s camera

## result
* outperforms the prior LQR-based local policy optimizer 
* on-policy sampling significantly increases the generalization ability of these policies.

## comment
* essentially GPS + PI^2
