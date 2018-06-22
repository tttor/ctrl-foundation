# script for actor-critic

## setup env
* `sudo apt-get install python3-pip python3-dev python-virtualenv`
* `virtualenv --system-site-packages -p python3 <virtual_env_dir>`
* `source <virtual_env_dir>/bin/activate`
* `pip install -r requirements.txt`

## tutor
* https://github.com/yukezhu/tensorflow-reinforce/blob/master/rl/pg_actor_critic.py
* https://github.com/dennybritz/reinforcement-learning/blob/master/PolicyGradient/Continuous%20MountainCar%20Actor%20Critic%20Solution.ipynb
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/blob/master/contents/8_Actor_Critic_Advantage/AC_CartPole.py

### a3c
* [Arthur Juliani @medium.com](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2)
  * Tensorflow,  3D Doom environment
  * based on DennyBritz and OpenAI.
  * classes: AC_Network, Worker
  * https://github.com/awjuliani/DeepRL-Agents/blob/master/A3C-Doom.ipynb
* https://jaromiru.com/2017/03/26/lets-make-an-a3c-implementation/
  * Python, Keras and OpenAI Gym (CartPole)
  * implement 4 classes: Environment, Agent, Brain and Optimizer.
  * https://github.com/jaara/AI-blog/blob/master/CartPole-A3C.py
* https://cgnicholls.github.io/reinforcement-learning/2017/03/27/a3c.html
  * use a feedforward convolutional neural network, not includes a recurrent layer
  * focus on the discrete action
  * ATARI game: Space Invaders
  * https://github.com/cgnicholls/reinforcement-learning/tree/master/a3c
* https://drive.google.com/file/d/1dFfDv-alQs6E_wyRmd3F2ZHKCVxhEIxY/view
  * https://github.com/greydanus/baby-a3c
  * https://github.com/ikostrikov/pytorch-a3c
* https://github.com/openai/universe-starter-agent/blob/master/a3c.py
* https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient/a3c
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/10_A3C
* https://github.com/Grzego/async-rl
* https://github.com/muupan/async-rl
* https://github.com/miyosuda/async_deep_reinforce
* https://github.com/chainer/chainerrl/blob/master/examples/gym/train_a3c_gym.py
* https://github.com/tensorlayer/tensorlayer/blob/master/example/tutorial_bipedalwalker_a3c_continuous_action.py
* https://github.com/reinforceio/tensorforce/blob/master/examples/openai_gym_async.py 
* https://github.com/liampetti/A3C-LSTM
* https://github.com/rlcode/reinforcement-learning/blob/master/2-cartpole/5-a3c/cartpole_a3c.py
* https://github.com/andreimuntean/A3C
* https://github.com/coreylynch/async-rl/blob/master/a3c.py
* https://github.com/NVlabs/GA3C
