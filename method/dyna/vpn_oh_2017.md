# Value Prediction Network
* Junhyuk Oh et al
* 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA

## problems
* stochastic environment where careful planning is required but 
  building an accurate observation-prediction model is difficult
* What if we could predict future rewards and values directly without predicting future observations?

## ideas: Value Prediction Network (VPN)
* VPN:
  * learn to predict values via Q-learning and rewards via supervised learning
  * perform lookahead planning to choose actions and compute bootstrapped target Q-values.
* VPN learns:
  * an option-value function $Q_{\theta} (x_t, o_t)$ through a neural network parameterized by $\theta$ like model-free RL, 
  * the dynamics of the rewards/values to perform planning.
* VPN's 4 modules parameterized by $\theta$:
  * encoding: maps the observation (x) to the abstract state (s) using neural networks
  * value: estimates the value of the abstract-state
  * outcome: predicts the option-reward $r$ for executing the option $o$ at abstract-state $s$
  * transition: transforms the abstract-state to the next abstract-state

## setup
* task: 2d navigation, Atari games
* model-free baseline: DQN, VPN(1)

## comment
* everything is predicted via  deep-network, see VPN modules
* why not implement mcts for planning?
