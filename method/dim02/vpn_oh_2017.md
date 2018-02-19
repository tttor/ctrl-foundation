# vpn_oh_2017

## problems
* stochastic environment where careful planning is required but 
building an accurate observation-prediction model is difficult
* What if we could predict future rewards and values directly without predicting future observations?

## ideas
* Value Prediction Network (VPN) that
  * learn to predict values via Q-learning and rewards via supervised learning
  * perform lookahead planning to choose actions and compute bootstrapped target Q-values.
* VPN: a value-prediction model that can directly generate/predict the value/reward of future states 
without  generating future observations.

## setup
* Atari games
