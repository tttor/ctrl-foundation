#!/usr/bin/env python3
import sys
import time

from agent import ActorCriticAgent
from environment import AtariPong

def main():
    if len(sys.argv) != 4:
        print('USAGE:')
        print('python3 pong.py <train/test> <n_episodes> <log_dir>')
        return

    mode = sys.argv[1]; assert mode in ['train', 'test']
    train = (True if mode=='train' else False)
    n_episodes = int(sys.argv[2])
    log_dir = sys.argv[3]

    run(train, n_episodes, log_dir, render=True)

def run(train, n_episodes, log_dir, render=False):
    ## init
    env = AtariPong()
    agent = ActorCriticAgent( env.action_space() )
    step_idx = 0 # an episode consists of n>=1 steps
    episode_idx = 0 # "episode" refers to "rally"
    game_idx = 0 # a game consists of n>=1 episodes
    discounted_return = 0
    obs = env.initial_observation()

    ## bookkeeper per game because training is done at then of a game
    if train == True:
        training_data = {'obss': [], 'rewards': [], 'labels': []}

    ## main loop
    while (episode_idx < n_episodes):
        print('episode_idx= '+str(episode_idx)+ \
              ' @step_idx= '+str(step_idx)+ \
              ' @game_idx= '+str(game_idx))

        if render:
            env.render()
            time.sleep(1/60.0)

        ## step!
        action, label = agent.act(obs)
        obs, reward, info = env.step(action)

        discounted_return += ((agent.gamma**step_idx) * reward)

        ## collect data for training
        if train == True:
            training_data['obss'].append(obs)
            training_data['rewards'].append(reward)
            training_data['labels'].append(label)

        ## close episode
        if info['end_of_episode']:
            print('episode_idx= '+str(episode_idx)+ \
                  ': ended with G= '+str('%.3f'%discounted_return))

            episode_idx += 1
            step_idx = 0
            discounted_return = 0

            if info['end_of_game']  or (episode_idx == n_episodes):
                ## train
                if train == True:
                    print('training...')
                    agent.train_critic(training_data)
                    agent.train_actor(training_data)

                    ## reset training data
                    training_data = {'obss': [], 'rewards': [], 'labels': []}

                ## set for the next game
                obs = env.initial_observation()
                game_idx += 1
        else:
            step_idx += 1

    env.close()

if __name__ == '__main__':
    main()
