import numpy as np

from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self, n_actions, initial_observation):
        self.n_actions = n_actions

        self._actor_net = ActorNeuralNetwork(input_dim=initial_observation.size,
                                             output_dim=n_actions)

        self._critic_net = CriticNeuralNetwork()

    def act(self, obs):
        probs = self._actor_net.forward_prop(obs)
        idx = np.random.choice(self.n_actions, p=probs)

        ## "fake" true label
        ## assume whatever action taken is the right action to take, later
        ## this will be modulated by the Advantage, e.g. return
        labels = np.zeros_like(probs)
        labels[idx] = 1

        return (idx, labels)

    def train(self, data):
        _train_critic(training_data)
        _train_actor(training_data)

    def _train_actor(self, data):
        self._actor_net.update(data)

    def _train_critic(self, data):
        pass

    def _act_random(self):
        return np.random.randint(0, self.n_actions, size=1)[0]
