# actor-critic

## variant
* [ACKTR: Actor Critic using Kronecker-Factored Trust Region (Wu,2017)](https://arxiv.org/abs/1708.05144)
* [Reactor: A Sample-Efficient Actor-Critic Architecture (Gruslys, 2017)](https://arxiv.org/abs/1704.04651)
* [A3C: Asynchronous(Synchronous) advantage actor-critic (Mnih, 2016)](https://arxiv.org/pdf/1602.01783.pdf)
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
  * https://github.com/ikostrikov/pytorch-a3c
  * https://github.com/rlcode/reinforcement-learning/blob/master/2-cartpole/5-a3c/cartpole_a3c.py
  * https://github.com/andreimuntean/A3C
  * https://github.com/coreylynch/async-rl/blob/master/a3c.py
  * https://github.com/NVlabs/GA3C
* [Natural Actor-Critic (Peters, 2008)](https://www.sciencedirect.com/science/article/pii/S0925231208000532)

## actor-critic based
* 2016: Progressive Nets
* 2015: Deep DPG

## foundation
### book
TODO

### talk, lecture, tutorial
* http://mi.eng.cam.ac.uk/~mg436/LectureSlides/MLSALT7/L5.pdf
* http://www.inf.ed.ac.uk/teaching/courses/rl/slides15/rl12.pdf
* http://www.rage.net/~greg/2016-07-05-ActorCritic-with-OpenAI-Gym.html
* [Survey: 2012: Grondman: A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients](http://ieeexplore.ieee.org/abstract/document/6392457/), see [survey](https://github.com/tttor/rl-foundation/tree/master/survey)
