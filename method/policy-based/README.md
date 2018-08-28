# Policy-based
Here is for model-free policy-based approaches. </br>
For model-based policy-based approaches, goto [method/model-based/planning/policy-based](https://github.com/tttor/rl-foundation/tree/master/method/model-based/planning/policy-based).

## taxonomy
* gradient-free
  * cross-entropy method
* gradient-based:
  * analytical (closed-form) solution:
    PILCO, PEGASUS
  * based on policy gradient theorem: stochastic and deterministic
    * actor-baseline (action-value fn **not** used for bootstrapping; iterative approaches)
    * actor-critic (action-value fn used for bootstrapping; incremental approaches)
* based on expectation maximization (EM)
* policy-prior seach

## tutor
* Quora
  * https://www.quora.com/Why-does-the-policy-gradient-method-have-a-high-variance
  * https://www.quora.com/What-is-the-difference-between-policy-gradient-methods-and-actor-critic-methods
* Jan Peter: Policy Search: Methods and Applications
  * https://icml.cc/2015/tutorials/PolicySearch.pdf
* http://karpathy.github.io/2016/05/31/rl/
  * https://www.youtube.com/watch?v=tqrcjHuNdmQ
  * https://www.youtube.com/watch?v=PDbXPBwOavc
  * https://medium.com/@dhruvp/956b57d4f6e0
* https://theneuralperspective.com/2016/11/25/reinforcement-learning-rl-policy-gradients-i/
  * https://theneuralperspective.com/2016/11/26/1656/
  * https://github.com/GokuMohandas/the-neural-perspective/tree/master/reinforcement-learning
* https://cgnicholls.github.io/reinforcement-learning/2016/08/20/reinforcement-learning.html
  * https://cgnicholls.github.io/reinforcement-learning/2016/08/21/reinforcement-learning-2.html
  * https://github.com/cgnicholls/reinforcement-learning/blob/master/cartpole/crossentropy.py
  * https://github.com/cgnicholls/reinforcement-learning/blob/master/cartpole/vanillapolicygradient.py
* https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/7_Policy_gradient_softmax
* https://www.oreilly.com/ideas/reinforcement-learning-with-tensorflow

## policy representation
* neural networks
  * tutor:
    * https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/02_nn_random_agent.py
* belief tree
* dynamic movement primitives
* time-varying linear-Gaussian (TVLG)

# Actor-critic
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

# Those that focus on optimization
* 2018: Accelerating Natural Gradient with Higher-Order Invariance: https://arxiv.org/abs/1803.01273
* 2018: https://github.com/tttor/rl-foundation/blob/master/method/policy-based/ppokfac_song_2018.md
* 2017: https://github.com/tttor/rl-foundation/blob/master/method/policy-based/acktr_wu_2017.md
