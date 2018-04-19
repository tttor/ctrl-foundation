from actor import ActorNeuralNetwork
from critic import CriticNeuralNetwork

class ActorCriticAgent():
    def __init__(self):
        self._actor_net = ActorNeuralNetwork()
        self._critic_net = CriticNeuralNetwork()

    def action(self, obs):
        self._actor_net.
