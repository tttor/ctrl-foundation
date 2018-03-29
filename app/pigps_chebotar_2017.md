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
* train the network (CNN layers) in two stages
  * pre-trained with a proxy pose detection objective. 
    * collect camera images while manually moving the object of interest into vari- ous poses, and 
      automatically label each image by using a geometry-based pose estimator based on the point pair feature (PPF) algorithm 
    * collect images of the robot learning the task with PI2 (without vision), and 
      label these images with the pose of the robot end-effector obtained from forward kinematics. 
      Each pose is represented as a 9- DoF vector, containing the positions of three points rigidly attached to 
      the object (or robot), represented in the world frame. 
    * trained using SGD with momentum to predict the end- effector and object poses, using a standard Euclidean loss.    
  * trained using path integral guided policy search to produce the joint torques, while 
    the weights in the convolutional layers are frozen. 
        
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
* training is initialized from 5 **demonstrations**, and 
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
    the training data are in the form of demonstration and initial+final images from end-to-end runs
* note the use of **demonstration** to initilize training
* it is interesting to see that NN as func approximator is very powerful in that it can map images to joint torques

