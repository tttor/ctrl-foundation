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
    * cost is based on the deviation of the final pose of the bottle from the goal pose
* pose detection using CNN,  visual features from the robot’s camera
* 7-DoF robotic arm with a two finger gripper
* a camera mounted behind the arm looking over the shoulder
* ctrl: torque commands to all seven joints
* eval metric: success rate
* training is initialized from 5 demonstrations, and 
* the convolutional layers are trained using 
  * 2708 images with object poses and 
  * 14070 task execution images with end-effector poses

## result
* outperforms the prior LQR-based local policy optimizer 
* on-policy sampling significantly increases the generalization ability of these policies.

## comment
* essentially GPS + PI^2
* for neural network policy, how do we use RL?
  * is it correct to say: that NN-policy is essentially supervised learning? where
    the training data are from demonstration and initial+final images from end-to-end runs
* it is interesting to see that NN as func approximator is very powerful in that it can map images to joint torques

