# RL software

## type 0: big guy 
* OpenAI: https://github.com/openai/baselines
* Tensorforce: https://github.com/reinforceio/tensorforce
* Ray RLlib: http://ray.readthedocs.io/en/latest/rllib.html
* ChainerRL: https://github.com/chainer/chainerrl
* KerasRL: https://github.com/keras-rl/keras-rl

## type 1: people power
### pytorch
* https://github.com/higgsfield/RL-Adventure-2
  * https://github.com/higgsfield/RL-Adventure
* https://github.com/ikostrikov/pytorch-rl
  * https://github.com/ikostrikov/pytorch-a2c-ppo-acktr
* https://github.com/kengz/SLM-Lab
* https://github.com/ShangtongZhang/DeepRL
* https://github.com/vitchyr/rlkit

### tensorflow
* https://github.com/dennybritz/reinforcement-learning
* https://github.com/hunkim/ReinforcementZeroToAll
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow
* https://github.com/NervanaSystems/coach
* https://github.com/rlcode/reinforcement-learning
* https://github.com/rll/rllab

## type 2: old
* PyBrain: http://pybrain.org/
* AI-Toolbox: https://github.com/Svalorzen/AI-Toolbox
* BURLAP: http://burlap.cs.brown.edu/
* RL-Glue: http://glue.rl-community.org/wiki/Main_Page

# Environment
* see also: [simulator](https://github.com/tttor/rl-foundation/blob/master/software/simulator.md)

## OpenAI Gym
* https://github.com/openai/gym
* https://github.com/openai/gym/wiki/Table-of-environments
* https://stackoverflow.com/questions/44404281/openai-gym-understanding-action-space-notation-spaces-box
> `Box` means that you are dealing with real valued quantities
* v1 vs v2: https://stackoverflow.com/questions/48861523/how-to-solve-environment-error-in-open-ai-gym
> 2018-01-24: All continuous control environments now use mujoco_py >= 1.50. Versions have been updated accordingly to -v2, e.g. HalfCheetah-v2. Performance should be similar (see https://github.com/openai/gym/pull/834) but there are likely some differences due to changes in MuJoCo.
* https://stackoverflow.com/questions/48980368/list-all-environment-id-in-openai-gym

## Others
* https://github.com/openai/universe
* https://github.com/openai/roboschool
* https://github.com/openai/retro

# ROS-enabled
Available packages in ROS for model-based and model-free RL: <br/>
(Surely, any package can be used in ROS with some efforts.)
* rl-texplore-ros-pkg: https://github.com/toddhester/rl-texplore-ros-pkg
* OpenAI Gym with ros-bridge
  * from ErleRobotics: https://github.com/erlerobot/gym-gazebo/
  * earlier bridge, now abandoned: https://github.com/openai/rosbridge
