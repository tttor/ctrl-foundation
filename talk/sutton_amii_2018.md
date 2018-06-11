# the next big step in ai: planning with a learned model
* Amii Presents Tea Time Talk with Rich Sutton (May 28, 2018)
* https://www.youtube.com/watch?v=6-Uiq8-wKrg

* now, pretty good at
  * model-free
  * planning in games, where a perfect model is available via game rules
* lack of method for planning when model is imperfect (when it is learned)

* intelligence is just
  * knowing a lot about the world
  * being able to use that knowledge to achieve goals

* in MDP, straigfwd: model of the dynamics of the world: T = p(s'|s,a), R(s,a)
* a learned model is NOT only about dynamics, but also state
  * partial observability
  * learn the representation
* the agent state is produced by the state-update fn:
  `S_{t+1} = u(S_t, A_t, O_{t+1}`
* the interaction:
  * the goal of dynamics learning is to predict state
  * the goal of state learning is to enable good dynamics learning

* the bitter lesson
  * the less we build in, the better thing works
    * eg: deep learning with no engineered features; alpha-go zero

* some pieces of the answer
  * non linear dyna
  * options, option models
  * etc

* what should the projection's next-state output be?
  * distribution model
  * sample model
  * expectation model
