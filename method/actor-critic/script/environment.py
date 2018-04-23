import numpy as np
import gym

class AtariPong():
    def __init__(self, gamma, seed):
        self._env = gym.make('Pong-v0')
        self._env.seed(seed)

        self.gamma = gamma
        self._prev_img = None

    def compute_returns(self, r):
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
            running_add = running_add * self.gamma + r[t]
            discounted_returns[t] = running_add

        # standardize to be unit normal
        # (helps control the gradient estimator variance)
        discounted_returns -= np.mean(discounted_returns)
        discounted_returns /= np.std(discounted_returns)

        return discounted_returns

    def step(self, action):
        img, reward, end_of_game, info = self._env.step(action)
        obs = self._observation(img)

        info['end_of_game'] = end_of_game
        info['end_of_episode'] = self._end_of_episode(reward)

        if end_of_game:
            self._prev_img = None

        return (obs, reward, info)

    def n_actions(self):
        return self._env.action_space.n

    def initial_observation(self):
        img = self._env.reset()
        return self._observation(img)

    def close(self):
        self._env.close()

    def render(self):
        self._env.render()

    def _end_of_episode(self, reward):
        return (reward != 0)

    def _observation(self, img):
        img = self._preprocess_image(img)

        if self._prev_img is None:
            obs =  np.zeros(img.size)
        else:
            obs = (img - prev_img)
            self._prev_img = img

        return obs

    def _preprocess_image(self, I):
        """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
        I = I[35:195] # crop
        I = I[::2,::2,0] # downsample by factor of 2
        I[I == 144] = 0  # erase background (background type 1)
        I[I == 109] = 0  # erase background (background type 2)
        I[I != 0] = 1    # everything else (paddles, ball) just set to 1
        return I.astype(np.float).ravel()
