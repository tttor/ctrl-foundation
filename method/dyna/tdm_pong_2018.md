# Temporal Difference Models: Model-Free Deep RL for Model-Based Control
* Vitchyr Pong et al
* iclr2018: poster
* https://openreview.net/forum?id=Skw0n-W0Z
* https://arxiv.org/abs/1802.09081
* https://github.com/vitchyr/rlkit
* http://bair.berkeley.edu/blog/2018/04/26/tdm/

## problem
* model-free: low sample efficiency in model-free
* model-based: often does not achieve the same asymptotic performance as model-free RL due to model bias

## observation
* A limiting factor in classic model-free RL is that the learning signal consists only of scalar rewards, 
  ignoring much of the rich information contained in state transition tuples
