#!/usr/bin/env python2

# Based on:
# http://karpathy.github.io/2016/05/31/rl/
# https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5

import sys
import time

import numpy as np
import cPickle as pickle

# https://github.com/tambetm/simple_dqn/issues/28
# sudo -H pip install "gym[atari]"
import gym

## actions in pong
up_action = 2 # 2 or 4
down_action = 5 # 3 or 5

def main(argv):
    if len(argv)!=2:
        print('USAGE:')
        print('python2 pong_policy_grad <test/train>')
        return

    mode = argv[1]
    model_fpath = '/home/tor/xprmt/tmp/pong_policy_grad.model'

    if mode=='train':
        train(n_episodes=3, model_fpath=model_fpath)
    elif mode=='test':
        test(n_episodes=1, model_fpath=model_fpath)
    else:
        print('unknown mode!')
        return

## test ########################################################################
def test(n_episodes, model_fpath, render=True):
    model = pickle.load(open(model_fpath, 'rb'))
    D = 80 * 80 # input dimensionality: 80x80 grid
    gamma = 0.99 # discount factor for reward

    for episode_idx in xrange(n_episodes):
        print('testing episode_idx= '+str(episode_idx)+': begin')

        ## init env
        env = gym.make("Pong-v0")
        observation = env.reset() # returns an initial observation
        prev_x = None # used in computing the difference frame
        episode_r = []

        step_idx = 0
        while True:
            if render: env.render()

            ## prepro
            ## x: input
            cur_x = prepro(observation)
            if (prev_x is not None):
                x = cur_x - prev_x
            else:
                x = np.zeros(D)
            prev_x = cur_x

            ## forward the policy network and
            ## sample an action from the returned probability
            ## up_prob: probability of action 2
            up_prob, _ = policy_forward(x, model)
            if np.random.uniform() < up_prob:# roll the dice!
                action = up_action
            else:
                action = down_action

            ## step the environment and get new measurements
            observation, reward, end_of_round, info = env.step(action)
            episode_r.append(reward)
            print('step_idx= '+str(step_idx)+' -> r= '+str(reward))

            ## check if terminal
            if terminal(reward):
                break;

            step_idx += 1
            time.sleep(1/60.0)

        ## closure per episode
        r_counter = {0: 0, 1: 0, -1: 0}
        for r in episode_r: r_counter[r] += 1

        print('n_steps= '+str(step_idx+1))
        print('r_counter= '+str(r_counter))
        print('testing episode_idx= '+str(episode_idx)+': end')

    try:
        print('Waiting for ctrl+C ...')
        while True:
            pass
    except KeyboardInterrupt:
        pass

## train #######################################################################
def train(n_episodes, model_fpath, resume=False, render=False):
    ## init model (=neuralNet)
    D = 80 * 80 # input dimensionality: 80x80 grid
    H = 200 # number of hidden layer neurons
    batch_size = 1 # every how many episodes to do a param update?
    learning_rate = 1e-4
    gamma = 0.99 # discount factor for reward
    decay_rate = 0.99 # decay factor for RMSProp leaky sum of grad^2

    if resume:
        model = pickle.load(open(model_fpath, 'rb'))
    else:
      model = {}
      model['W1'] = np.random.randn(H,D) / np.sqrt(D) # "Xavier" initialization
      model['W2'] = np.random.randn(H) / np.sqrt(H)

    grad_buffer = { k : np.zeros_like(v) for k,v in model.iteritems() } # for batch learning
    rmsprop_cache = { k : np.zeros_like(v) for k,v in model.iteritems() }

    for episode_idx in xrange(n_episodes):
        print('training episode_idx= '+str(episode_idx)+': begin')

        ## init env
        env = gym.make("Pong-v0")
        observation = env.reset() # returns an initial observation
        prev_x = None # used in computing the difference frame

        ## init bookeeper for an episode
        episode_x = [] # x: input
        episode_h = [] # h: hidden state
        episode_dlogp = []
        episode_r = [] # r: reward

        while True:
            if render: env.render()

            ## preprocess x: input
            cur_x = prepro(observation)
            if (prev_x is not None):
                x = cur_x - prev_x
            else:
                x = np.zeros(D)
            prev_x = cur_x

            ## forward the policy network and
            ## sample an action from the returned probability
            ## up_prob: probability of taking UP action,
            ##          hence the probability to take DOWN is '1 - up_prob'.
            ## h: hidden state (inside the net)
            up_prob, h = policy_forward(x, model)
            if np.random.uniform() < up_prob:# roll the dice!
                action = up_action
            else:
                action = down_action

            ## fake the label, y
            ## Yugnaynehc commented on 3 Nov 2017 at https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5
            ## When the taken action was UP, the probability is aprob, so the gradient is (1 - aprob), and
            ## when the taken action was DOWN, the probability is (1 - aprob), so the gradient is 1 - (1-aprob) = 0 - aprob = -aprob.
            ## MariaNivedha commented on 16 Feb at https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5
            ## Suppose if we get aprob=0.4 and on random, we get to sample for DOWN action, then
            ## we do gradient (0-0.4=-0.4) since this -ve 0.4 tells to move down to the lower boundary 0
            ## (which is highest probability of taking the DOWN action).
            ## Suppose if we get aprob=0.4 and on random, we get to sample for UP action, then
            ## we do gradient(1-0.4=0.6) since this +ve 0.6 tells to move up to the upper boundary 1
            ## (which is highest probability of taking the UP action)
            if action == up_action:
                y = 1.0
            else:
                y = 0.0

            # compute grad that encourages the action that was taken to be taken
            # http://cs231n.github.io/neural-networks-2/#losses
            dlogp = y - up_prob

            ## step the environment and get new measurements
            observation, reward, end_of_round, info = env.step(action)

            ## record various intermediates (needed later for backprop)
            episode_x.append(x) # observation
            episode_h.append(h) # hidden state
            episode_dlogp.append(dlogp)
            episode_r.append(reward)

            if terminal(reward): # does this episode end?
                ## stack together all inputs, hidden states, action gradients, and rewards for this episode
                episode_x = np.vstack(episode_x)
                episode_h = np.vstack(episode_h)
                episode_dlogp = np.vstack(episode_dlogp)
                episode_r = np.vstack(episode_r)

                ## compute the discounted reward backwards through time
                episode_discounted_r = get_discounted_rewards(episode_r, gamma)

                ## standardize to be unit normal
                ## (helps control the gradient estimator variance)
                episode_discounted_r -= np.mean(episode_discounted_r)
                episode_discounted_r /= np.std(episode_discounted_r)

                ## modulate the gradient with the episode return
                ## (PG magic happens right here.)
                episode_dlogp *= episode_discounted_r

                ## compute grad
                grad = policy_backward(episode_x, episode_h, episode_dlogp, model)

                ## accumulate grad over batch
                for layer_key in model:
                    grad_buffer[layer_key] += grad[layer_key] # element-wise add

                ## perform rmsprop parameter update every batch_size episodes
                if ( (episode_idx+1) % batch_size ) == 0:
                    print('perform rmsprop parameter update...')
                    for k,v in model.iteritems():
                        g = grad_buffer[k] # gradient
                        rmsprop_cache[k] = decay_rate * rmsprop_cache[k] + (1 - decay_rate) * g**2
                        model[k] += learning_rate * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)
                        grad_buffer[k] = np.zeros_like(v) # reset batch gradient buffer

                    pickle.dump(model, open(model_fpath, 'wb'))

                ## end this episode(==rally)
                break

        print('training episode_idx= '+str(episode_idx)+': end')

## util ########################################################################
def terminal(reward):
    if reward != 0:
        return True
    else:
        return False

def prepro(I):
    """ prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector """
    I = I[35:195] # crop
    I = I[::2,::2,0] # downsample by factor of 2
    I[I == 144] = 0 # erase background (background type 1)
    I[I == 109] = 0 # erase background (background type 2)
    I[I != 0] = 1 # everything else (paddles, ball) just set to 1
    return I.astype(np.float).ravel()

def policy_forward(x, model):
    h = np.dot(model['W1'], x)
    h[h<0] = 0 # ReLU nonlinearity
    logp = np.dot(model['W2'], h)
    p = sigmoid(logp)
    return p, h # return probability of taking action 2, and hidden state

def policy_backward(epx, eph, epdlogp, model):
    """ backward pass. (eph is array of intermediate hidden states) """
    dW2 = np.dot(eph.T, epdlogp).ravel()
    dh = np.outer(epdlogp, model['W2'])
    dh[eph <= 0] = 0 # backprop relu
    dW1 = np.dot(dh.T, epx)
    return {'W1':dW1, 'W2':dW2}

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x)) # sigmoid "squashing" function to interval [0,1]

def get_discounted_rewards(r, gamma):
    """ take 1D float array of rewards and compute discounted reward """
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(xrange(0, r.size)):
        if r[t] != 0:
            running_add = 0 # reset the sum, since this was a game boundary (pong specific!)
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r

################################################################################
if __name__ == '__main__':
    main(sys.argv)
