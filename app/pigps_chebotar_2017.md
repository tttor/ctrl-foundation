# Path Integral Guided Policy Search
2017 IEEE International Conference on Robotics and Automation (ICRA)

## problem

## idea
* extend GPS in the following ways: 
  * the use of a model-free local optimizer based on path integral stochastic optimal control, which 
    enables us to learn local policies for tasks with highly discontinuous contact dynamics; and 
  * enable GPS to train on a new set of task instances in every iteration by using on-policy sampling: 
    this increases the diversity of the instances that the policy is trained on, and 
    is crucial for achieving good generalization. 
    
## setup
* door opening task and a pick-and-place task

## result
* outperforms the prior LQR-based local policy optimizer 
* on-policy sampling significantly increases the generalization ability of these policies.
