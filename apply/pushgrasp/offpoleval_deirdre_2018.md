# Deep Reinforcement Learning for Vision-Based Robotic Grasping: A Simulated Comparative Evaluation of Off-Policy Methods
* Quillen, Deirdre; Jang, Eric
* icra2018: interactive ppt

## problem
* proliferation of algorithms makes it difficult to discern which particular approach would be best 
  suited for **rich, diverse, and highly varied situations tasks** like grasping.

## idea
* simulated benchmark for robotic grasping that emphasizes off- policy learning and generalization to unseen objects
* evaluate  the  benchmark  tasks  against  
  * a  variety  of  Q-function  estimation  methods,  
  * a  method  previously  proposed for  robotic  grasping  with  deep  neural  network  models,  and
  * a  novel  approach  based  on  a  combination  of  Monte  Carlo return  estimation  and  an  off-policy  correction

## setup
* baseline:
  PCL, DDPG, ...
* tool: pybullet

## result
* DQL performs better on both grasping tasks than other algorithms 
  * in low-data regimes, 
  * for both off-policy and on-policy learning, and 
  * having the desirable property of being relatively robust to choice of hyperparameters.
* the use of an **actor network** substantially **reduces stability**, 
  leading to poor performance and severe hyperparameter sensitivity
* in  robotic settings  where  off-policy  data  is  available,  
  * single-network methods may be preferred for stability, and 
  * methods that use (corrected) full episode returns should be preferred when data is  plentiful,  while  
    bootstrapped  methods  are  better  in  low data regimes

## background
* if the learning is conducted primarily on-policy, 
  the robot must repeatedly revisit previously seen objects to avoid forgetting, 
  making it difficult to handle extremely diverse grasping scenarios
  * Off-policy reinforcement learning methods might therefore be preferred for tasks such as grasping, where 
    the wide variety of previously seen objects is crucial for generalization.


## comment
* ? vary the gripper shapes?
  ans: not trained
* ? movable obj
  ans: there is ball-shape obj
* ? grasp not from the top? this is always from the top
