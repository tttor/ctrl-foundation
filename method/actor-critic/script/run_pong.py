import sys

from agent import ActorCriticAgent
from environment import AtariPong

def main():
    if len(sys.argv) != 4:
        print('USAGE:')
        print('python3 pong.py <train/test> <n_episodes> <log_dir>')

    mode = sys.argv[1]; assert mode in ['train', 'test']
    train = (True if mode=='train' else False)
    n_episodes = int(sys.argv[2])
    log_dir = sys.argv[3]

    run(train, n_episodes, log_dir, render=False)

def run(train, n_episodes, log_dir, render=False):
    env = AtariPong()
    agent = ActorCriticAgent( env.n_actions() )

    step_idx = 0 # an episode consists of n>=1 steps
    episode_idx = 0 # "episode" refers to "rally"
    game_idx = 0 # a game consists of n episodes

    rewards = [] # per game
    obss = [] # per game

    obs = env.initial_observation()

    while (episode_idx < n_episodes):
        action = agent.action(obs)
        obs, reward, info = env.step(action)

        obss.append(obs)
        rewards.append(reward)

        if info['end_of_episode']:
            episode_idx += 1
            step_idx = 0

            if info['end_of_game']:
                ## train
                if train == True:
                    pass

                ## set for the next game
                obs = env.initial_observation()
                game_idx += 1
                rewards = []
                obss = []
        else
            step_idx += 1

if __name__ == '__main__':
    main()
