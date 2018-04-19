import sys

from agent import ActorCriticAgent
from environment import AtariPong

def main():
    if len(sys.argv) != 4:
        print('USAGE:')
        print('python3 pong.py <train/test> <n_episodes> <log_dir>')

    mode = sys.argv[1]
    n_episodes = int(sys.argv[2])
    log_dir = sys.argv[3]

    if mode=='train':
        train(n_episodes, log_dir, render=False)
    elif mode=='test':
        test(n_episodes, log_dir, render=True)
    else:
        print('unknown mode!')
        return

def train(n_episodes, log_dir, render=False):
    env = AtariPong()
    agent = ActorCriticAgent( env.n_actions() )

    episode_idx = 0 # "episode" refers to "rally"
    game_idx = 0 # a game consists of n episodes
    obs = env.initial_observation()

    while (episode_idx < n_episodes):
        action = agent.action(obs)
        obs, reward, info = env.step(action)

        if info['end_of_episode']:
            episode_idx += 1

        if info['end_of_game']:
            obs = env.initial_observation()
            game_idx += 1

def test(n_episodes, log_dir, render=True):
    pass

if __name__ == '__main__':
    main()
