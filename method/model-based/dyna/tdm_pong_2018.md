# Temporal Difference Models: Model-Free Deep RL for Model-Based Control
* Vitchyr Pong et al
* iclr2018: poster
* https://openreview.net/forum?id=Skw0n-W0Z
* https://arxiv.org/abs/1802.09081
* https://github.com/vitchyr/rlkit
* http://bair.berkeley.edu/blog/2018/04/26/tdm/

## problem
* model-free:
  * low sample efficiency
  * learns only from the reward: experience that receives no reward provides minimal supervision to the learner.
  * less efficient but achieve the best asymptotic performance

* model-based:
  * often does not achieve the same asymptotic performance as model-free RL due to model bias;
    when the dynamics cannot be learned perfectly,
  * obtain a large amount of supervision from every sample,
    since they can use each sample to better learn how to predict the system dynamics
  * more efficient but do not produce policies that are as optimal.

## observation
* A limiting factor in classic model-free RL is that the learning signal consists only of scalar rewards,
  ignoring much of the rich information contained in state transition tuples

## idea
* makes use of this connection
between model-based and model-free learning to learn a specific type of goal-conditioned value
function, which we call a temporal difference model (TDM).

## setup
* task: 7-DoF Reacher, Pusher, Half Cheetah, Ant
* metric: final distance to goal _vs_ number of environment samples
