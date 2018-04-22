import numpy as np

from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self, n_actions, initial_observation):
        input_dim = initial_observation.size
        output_dim = n_actions

        self._actor_net = ActorNeuralNetwork(input_dim, output_dim)
        self._critic_net = CriticNeuralNetwork()
        self.n_actions = n_actions

    def act(self, obs):
        probs = self._actor_net.forward_prop(obs)
        idx = np.random.choice(self.n_actions, p=probs)

        labels = np.zeros_like(probs)
        labels[idx] = 1

        return (idx, labels)

    def train_actor(self, data):
        self._actor_net.update(data)

    def train_critic(self, data):
        pass

    def _act_random(self):
        return np.random.randint(0, self.n_actions, size=1)[0]
