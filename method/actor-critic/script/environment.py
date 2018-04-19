import gym
import numpy as np

class AtariPong():
    def __init__(self):
        self._env = gym.make('Pong-v0')
        self._prev_img = None

    def n_actions(self):
        return self._env.action_space.n

    def step(self, action):
        img, reward, end_of_game, info = self._env.step(action)
        obs = _observation(img)

        info['end_of_game'] = end_of_game
        info['end_of_episode'] = _end_of_episode(reward)

        if end_of_game:
            prev_img = None

        return (obs, reward, info)

    def initial_observation(self):
        return self._env.reset()

    def _end_of_episode(self, reward):
        return (reward != 0)

    def _observation(self, img):
        img = _preprocess_image(img)

        if self.prev_img is None:
            obs =  np.zeros(img.size)
        else:
            obs = (img - prev_img)
            self.prev_img = img

        return obs

    def _preprocess_image(I):
        """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
        I = I[35:195] # crop
        I = I[::2,::2,0] # downsample by factor of 2
        I[I == 144] = 0  # erase background (background type 1)
        I[I == 109] = 0  # erase background (background type 2)
        I[I != 0] = 1    # everything else (paddles, ball) just set to 1
        return I.astype(np.float).ravel()
