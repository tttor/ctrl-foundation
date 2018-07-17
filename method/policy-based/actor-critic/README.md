# actor-critic

## variant
* [Reactor: A Sample-Efficient Actor-Critic Architecture, 2018](reactor_gruslys_2018.md)
* [GAC: Guide actor-critic, 2018](gac_tangkaratt_2018.md)
* [TD3: Twin Delayed Deep Deterministic, 2018](td3_fujimoto_2018.md)
* [ACKTR: Actor Critic using Kronecker-Factored Trust Region, 2017](acktr_wu_2017.md)
* [Q-prop, 2017](qprop_gu_2017.md)
* [ACER: Sample efficient actor-critic with experience replay, 2017](acer_wang_2017.md)
* [Dual-AC: Boosting the Actor with Dual Critic, 2017](dualac_dai_2017.md)
* [PGQL: Combining policy gradient and q-learning, 2017](pgql_donoghue_2017.md)
* [PCL: Bridging the Gap Between Value and Policy Based Reinforcement Learning, 2017](pcl_nachum_2017.md)
* [Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor, 2017](sac_haarnoja_2017.md)
* [A3C: Asynchronous advantage actor-critic, 2016](a3c_mnih_2016.md)
* [BPAC: Bayesian Policy Gradient and Actor-Critic Algorithms, 2016](bpgac_ghavamzadeh_2016.md) # Gaussian processes, **not** neural nets
* [Deep DPG, 2015](ddpg_lilicrap_2015.md)

### legend
* [Off-PAC: off-Policy Actor-Critic, 2012](offpac_degris_2012.md)
* [Natural Actor-Critic, 2008](nac_peters_2008.md)
* [Actor-Critic Algorithms, 1999](ac_konda_1999.md)

## foundation
### book
* RL Intro (Sutton, 2018): 13.5, 15.7

### talk, lecture, tutorial
* http://mi.eng.cam.ac.uk/~mg436/LectureSlides/MLSALT7/L5.pdf
* http://www.inf.ed.ac.uk/teaching/courses/rl/slides15/rl12.pdf
* http://www.rage.net/~greg/2016-07-05-ActorCritic-with-OpenAI-Gym.html
* [Survey: 2012: Grondman: A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients](http://ieeexplore.ieee.org/abstract/document/6392457/), see [survey](https://github.com/tttor/rl-foundation/tree/master/survey)

### tutor
* https://github.com/yukezhu/tensorflow-reinforce/blob/master/rl/pg_actor_critic.py
* https://github.com/dennybritz/reinforcement-learning/blob/master/PolicyGradient/Continuous%20MountainCar%20Actor%20Critic%20Solution.ipynb
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/blob/master/contents/8_Actor_Critic_Advantage/AC_CartPole.py

#### a3c
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
