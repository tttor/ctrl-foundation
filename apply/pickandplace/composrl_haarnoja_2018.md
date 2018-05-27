# Composable Deep Reinforcement Learning for Robotic Manipulation
* Haarnoja, Tuomas
* icra2018
* https://github.com/haarnoja/softqlearning

## problem
* how  maximum  entropy  policies  trained  using  soft
  Q-learning  can  be  applied  to  real-world  robotic  manipulation.
* the sample complexity of model-free methods tends
  to be quite high, and is increased further by the inclusion of
  high-capacity function approximators.
* Can  we  instead  devise  model-free  reinforcement  learning
  algorithms that are efficient enough to train multilayer neural
  network  models  directly  in  the  real  world,  without  reliance
  on simulation, demonstrations, or multiple robots?

## observation
* hypothesize  that  the  maximum  entropy  principle  [6]
  can  yield  an  effective  framework  for  practical,  real-world
  deep reinforcement learning due to the following two properties

## idea
?

## result
* soft Q-learning is substantially more sample efficient than prior model-free deep
  reinforcement learning methods, and that compositionality can
  be  performed  for  both  simulated  and  real-world  tasks.
* Q-learning  substantially  outper-
  forms  prior  model-free  deep  reinforcement  learning
* derive a bound on the error between the composed
  policy  and  the  optimal  policy  for  the  composed  reward
  function.   This   bound   suggests   that   policies   with   higher
  entropy  may  be  easier  to  compose
* softQ > NAF > DDPGs

## background
* 2 important  features  of  soft  Q-learning.
  * soft Q-learning can learn multimodal exploration strategies by
    learning  policies  represented  by  expressive  energy-based  models.
  * policies learned with soft Q-learning can be composed to create new policies,
    sand that the optimality of the resulting policy can be bounded in terms of
    the divergence between the  composed policies

## comment
* ? soft Q-learning: critic-only?
* ? tried in open ai mujoco tasks?
* ? fig 2: how to combine policy?
* ? why decompose? who decompse? lower the level of autonomy
