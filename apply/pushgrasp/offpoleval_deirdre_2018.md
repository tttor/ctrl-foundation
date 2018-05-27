# Deep Reinforcement Learning for Vision-Based Robotic Grasping: A Simulated Comparative Evaluation of Off-Policy Methods
* Quillen, Deirdre; Jang, Eric
* icra2018

## idea
evaluate  the  benchmark  tasks  against  a  variety  of  Q-
function  estimation  methods,  a  method  previously  proposed
for  robotic  grasping  with  deep  neural  network  models,  and
a  novel  approach  based  on  a  combination  of  Monte  Carlo
return  estimation  and  an  off-policy  correction

## result
DQL performs better on both
grasping tasks than other algorithms in low-data regimes, for
both off-policy and on-policy learning, and additionally hav-
ing the desirable property of being relatively robust to choice
of hyperparameters.

 in  robotic
settings  where  off-policy  data  is  available,  single-network
methods may be preferred for stability, and methods that use
(corrected) full episode returns should be preferred when data
is  plentiful,  while  bootstrapped  methods  are  better  in  low
data regimes

off vs on policy
supervised is best
ddpg is hyperparam sensitive

## comment
? vary the gripper shapes?
  ans: not trained
? movable obj
  ans: there is ball-shape obj
? grasp not from the top?
