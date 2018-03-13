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
    with $n_i$ the number of units at layer $i \le L$, and parameters $\theta^{(1)}$ trained to convergence.
  * When switching to a second task, the parameters $\theta^{(1)}$ are “frozen” and
    a new column with parameters $\theta^{(2)}$ is instantiated (with random initialization), where
    layer $h_i^{(2)}$ receives input from both $h_{i-1}^{(2)}$ and $h_{i-1}^{(1)}$ via lateral connections.
* Application to Reinforcement Learning
  * each column is trained to solve a particular Markov Decision Process (MDP):
  * the k-th column thus defines a policy $\pi(k)(a | s)$ taking as input a state s given
    by the environment, and generating probabilities over actions
 (s).

## setup
* tasks are learned using end-to-end deep RL, with RGB inputs and joint velocity output actions.
* compare A3C to DQN
* Jaco arm, the agent policy controls 9 degrees(6 DOF arm + 3 actuated fingers) of freedom
  using velocity commands
* Each joint policy i has three actions
  * a fixed positive velocity,
  * a fixed negative velocity, and
  * a zero velocity
* MuJoCo physics simulator
* both feedforward and recurrent neural networks;
  Both have convolutional input layers followed by either a fully connected layer or an LSTM (Long Short Term Memory networks)
* task: reaching to a visual target

## result
* rather than relying on model-based trajectory optimisation, the task learning is
  accomplished using only deep reinforcement learning and sparse rewards.
* the inductive bias imparted by the features and encoded policy of the simulation net is enough to
  give a dramatic learning speed-up on the real robot.
* A3C has been shown to converge faster than DQN

## comment
* this is full of neural-networks
* no obstacle in reaching task
* too big to implement by ourselves;
  first, needs to have our own working code on deeplearning and deeprl