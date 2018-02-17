# Deepmind AlphaZero - Mastering Games Without Human Knowledge
nips 2017
david silver

deep rl symposium, workshop

## misc:
* alphagoZero > alphagoMaster > alphago,
* go: 10^170 states
* chess: 10^48 states
* shogi: japanese chess
* mcts > alphabeta search

## alphagoZero:
* no human data, self-play rl, starting from random
* no human handcradted feature
* single neural network, policy and value network combined into one resnet
* simple search, no random rollout, use nn to evaluate
* less complexity, more generality

## alphago:
* policy neuralnetwork
* value (conv)neuralnetwork
* training pipeline:
  humanExpert --supervisedLearning-> policyNetwork --rl--> valueNetwork
* reducing breath with policy network
* reducing depth with value network
* use mcts

## seach-based polity iter:
* search-based (instead of greedy) policy improvement
* search-based policy evaluatino
