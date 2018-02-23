# PILCO: Gaussian Processes for Data-Efficient Learning in Robotics and Control
https://doi.org/10.1109/TPAMI.2013.218

## problems
* autonomous reinforcement learning (RL) approaches typically require many interactions with 
the system to learn controllers, which is a practical limitation in real systems
* current learning approaches typically require task-specific knowledge in form of expert demonstrations, realistic simulators, pre-shaped policies, or specific knowledge about the underlying dynamics

## ideas
* learn a probabilistic, non-parametric Gaussian process transition model of the system.
* explicitly incorporating model uncertainty into long-term planning and controller learning 
(so that our approach reduces the effects of model errors)
