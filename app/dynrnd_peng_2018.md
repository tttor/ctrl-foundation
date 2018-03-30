# Sim-to-Real Transfer of Robotic Control with Dynamics Randomization
https://arxiv.org/abs/1710.06537;
https://www.youtube.com/watch?v=XUW0cnvqbwM;
https://xbpeng.github.io/projects/SimToReal/index.html

## problem
* reality gap:
  strategies that are successful in simulation may **not**
  transfer to their real world counterparts
* most DeepRL algorithms
  * high sample complexities, very data inefficient
  * safety concerns in real-world deployment

## idea: dynamics randomization (with HER and RDPG)
* train a policy using an approximate dynamics model $\hat{p} \approx  p^{\star}$ that is easier to sample from.
  * $\hat{p}$ assumes the form of a physics simulation
* train a policy that can perform a task under a variety of different dynamics models
* introduce a set of dynamics parameters $\mu$ that parameterizes the dynamics of the simulation $\hat{p}$
* maximize the expected return across a distribution of dynamics models

## setup
* task: a puck pushing task using a 7-DOF Fetch Robotics arm
* action: target joint angles for a position controller, for each DOF, size= 7
* simulators: MuJoCo physics engine (timestep of 0.002s)
* method:
  * Hindsight Experience Relay (HER)
  * Recurrent Deterministic Policy Gradient (RDPG)
* randomization includes:
  * Mass of each link in the robot’s body
  * Damping of each joint
  * Mass, friction, and damping of the puck
  * Height of the table
  * Gains for the position controller
  * Timestep between actions
  * Observation noise
* eval metric: success rate;
  compared on the simulated and real robot for the pushing task;
  Policies are trained using only data from simulation.

## result
* the use of dynamics randomization
  to train recurrent policies that are capable of adapting
  to unfamiliar dynamics at runtime.

## misc
* Simulations are attractive environments for training agents as
  * they provide an abundant source of data and
  * alleviate certain safety concerns during the training process.
* Guided Policy Search (GPS) is capable of training policies directly on a realrobot.
* sim2real can be viewed as an instance of **domain adaptation**, where
  a model trained in a source domain is transfered to a new target domain.

## comments
* rely on HER and RDPG
* model-free with generative models (physics engine)
  * by using generative models for model-free, then this is essentially planning
  * the randomization of dynamics is a way to deal with uncertain MDP models, 
    another way is to formulate such uncertainty in POMDP models, e.g. Bayesian-RL
