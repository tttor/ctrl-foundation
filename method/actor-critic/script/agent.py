import numpy as np

from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self, action_space, initial_observation):
        assert len(action_space)==2

        input_dim = initial_observation.size
        output_dim = 1 # as len(action_space)==2 (==len(action_labels))

        self._actor_net = ActorNeuralNetwork(input_dim, output_dim)
        self._critic_net = CriticNeuralNetwork()

        self.gamma = 0.999
        self.action_space = action_space


    def act(self, obs):
        idx = self._act_random()
        label = self._label_action(idx)
        return (idx, label)

    def train_actor(self, data):
        # self._actor_net.update(data)
        pass

    def train_critic(self, data):
        pass

    def _act_random(self):
        minv = min(self.action_space.keys())
        maxv = max(self.action_space.keys())
        return np.random.randint(minv, maxv+1, size=1)[0]

    def _label_action(self, action_idx):
        if self.action_space[action_idx] == 'up':
            label = 1
        else:
            label = 0
        return label

