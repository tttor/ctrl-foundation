import numpy as np

from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self, n_actions, initial_observation):
        input_dim = initial_observation.size
        output_dim = n_actions

        self._actor_net = ActorNeuralNetwork(input_dim, output_dim)
        self._critic_net = CriticNeuralNetwork()

        self.gamma = 0.999
        self.n_actions = n_actions

    def act(self, obs):
        probs = self._actor_net.forward_prop(obs)
        idx = np.random.choice(self.n_actions, p=probs)

        labels = np.zeros_like(probs)
        labels[idx] = 1

        return (idx, labels)

    def train_actor(self, data):
        data['obss'] = np.vstack(data['obss'])
        data['labels'] = np.vstack(data['labels'])
        data['rewards'] = np.vstack(data['rewards'])
        data['returns'] = self._compute_returns(data['rewards'], self.gamma)

        self._actor_net.update(data)

    def train_critic(self, data):
        pass

    def _act_random(self):
        return np.random.randint(0, self.n_actions, size=1)[0]

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
