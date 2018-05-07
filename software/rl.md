# RL software

## type 0: big guy 
* OpenAI: https://github.com/openai/baselines
* Ray RLlib: http://ray.readthedocs.io/en/latest/rllib.html
* ChainerRL: https://github.com/chainer/chainerrl
* Tensorlayer: https://github.com/tensorlayer/tensorlayer
* Tensorforce: https://github.com/reinforceio/tensorforce
* KerasRL: https://github.com/keras-rl/keras-rl
* FitML: https://github.com/FitMachineLearning/FitML

## type 1: people power
* https://github.com/dennybritz/reinforcement-learning
* https://github.com/hunkim/ReinforcementZeroToAll
* https://github.com/ikostrikov/pytorch-rl
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow
* https://github.com/rll/rllab
* https://github.com/rlcode/reinforcement-learning
* https://github.com/ShangtongZhang/DeepRL
* https://github.com/vitchyr/rlkit

## type 2: old
* PyBrain: http://pybrain.org/
* AI-Toolbox: https://github.com/Svalorzen/AI-Toolbox
* BURLAP: http://burlap.cs.brown.edu/
* RL-Glue: http://glue.rl-community.org/wiki/Main_Page

## environment
see also: [simulator](https://github.com/tttor/rl-foundation/blob/master/software/simulator.md)
* https://github.com/openai/gym
* https://github.com/openai/universe
* https://github.com/openai/roboschool
* https://github.com/openai/retro

## ROS-enabled
Available packages in ROS for model-based and model-free RL: <br/>
(Surely, any package can be used in ROS with some efforts.)
* rl-texplore-ros-pkg: https://github.com/toddhester/rl-texplore-ros-pkg
* OpenAI Gym with ros-bridge
  * from ErleRobotics: https://github.com/erlerobot/gym-gazebo/
  * earlier bridge, now abandoned: https://github.com/openai/rosbridge
  
## misc
* list openai gym env
```
def list_env():
    from gym import envs
    env_ids = [spec.id for spec in envs.registry.all()]
    print("Total Number of environments are", len(env_ids))
    for env_id in sorted(env_ids):
        print(env_id)
```
