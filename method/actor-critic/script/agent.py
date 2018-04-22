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
        data['obss'] = np.vstack(data['obss'])
        data['labels'] = np.vstack(data['labels'])
        data['rewards'] = np.vstack(data['rewards'])
        data['returns'] = self._compute_returns(data['rewards'], self.gamma)

        self._actor_net.update(data)

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

    def _compute_returns(self, r, gamma):
        """ take 1D float array of rewards and compute discounted reward """
        # https://github.com/AbhishekAshokDubey/RL/blob/master/ping-pong/tf_ping_pong_policyGradient.py
        # https://github.com/hunkim/ReinforcementZeroToAll/issues/1
        # input : np.array([1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,1.0])
        # output: np.array([ 1., 0.96059601, 0.970299, 0.9801, 0.99, 1., 0.9801, 0.99, 1.])
        discounted_returns = np.zeros_like(r)
        running_add = 0
        for t in reversed(range(0, r.size)):
            if r[t] != 0:
                running_add = 0 # reset the sum, since this was a game boundary (pong specific!)
            running_add = running_add * gamma + r[t]
            discounted_returns[t] = running_add

        # standardize to be unit normal
        # (helps control the gradient estimator variance)
        discounted_returns -= np.mean(discounted_returns)
        discounted_returns /= np.std(discounted_returns)

        return discounted_returns
