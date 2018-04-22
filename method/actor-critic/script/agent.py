import numpy as np

from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self, n_actions):
        self._actor_net = ActorNeuralNetwork()
        self._critic_net = CriticNeuralNetwork()

        self.gamma = 0.999
        self.n_actions = n_actions

    def action(self, obs):
        action_idx = self._random_action()
        return action_idx

    def _random_action(self):
        return np.random.randint(0, self.n_actions, size=1)[0]
