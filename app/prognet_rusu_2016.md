# Sim-to-Real Robot Learning from Pixels with Progressive Nets
1st Conference on Robot Learning (CoRL 2017), Mountain View, United States;
https://arxiv.org/abs/1610.04286

## problem
* Applying end-to-end learning to solve complex, interactive, pixel-driven control tasks (pixel-to-action scenarios) on a robot
* Deep Reinforcement Learning algorithms are too slow to achieve performance on a real robot, but 
  their potential has been demonstrated in simulated environments
 
## observation
* to fulfill the potential of deep reinforcement learning applied in real-world robotic domains,
  * learning needs to become many times more efficient. 
  * One route to achieving this is via transfer learning from simulation-trained agents. 
*  to use transfer learning methods to bridge the reality gap that separates simulation from real world domains.

## idea: progressive networks
* A progressive network 
  * starts with a single column:
    a deep neural network having L layers with hidden activations $h_i^{(1)} \in R_{n_i} , 
    with $n_i$ the number of units at layer $i \le L$, and parameters Θ(1) trained to convergence. 
  * When switching to a second task, the parameters Θ(1) are “frozen” and 
    a new column with parameters Θ(2) is instantiated (with random initialization), where l
    ayer hi (2)  receives (2)  (1) input from both hi−1 and hi−1 via lateral connections.

## setup
* tasks are learned using end-to-end deep RL, with RGB inputs and joint velocity output actions.

## result
* rather than relying on model-based trajectory optimisation, the task learning is
  accomplished using only deep reinforcement learning and sparse rewards.
* the inductive bias imparted by the features and encoded policy of the simulation net is enough to 
  give a dramatic learning speed-up on the real robot.
