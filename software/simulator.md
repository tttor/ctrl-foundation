# simulators

## Full-blown simulators:
* [TORCS](http://torcs.sourceforge.net/), [gym_torcs](https://github.com/ugo-nama-kun/gym_torcs)
* [ALE](https://github.com/mgbellemare/Arcade-Learning-Environment): 
  tasks with high-dimensional state inputs and discrete actions
* [DeepMindLab](https://github.com/deepmind/lab)
* DeepMind Control Suite: https://github.com/deepmind/dm_control
* [ai2thor](http://ai2thor.allenai.org/): Photorealistic Interactive Environments for AI Agents
* [NVIDIA Isaac Robot Simulator](https://www.nvidia.com/en-us/deep-learning-ai/industries/robotics/): the faster, safer, smarter way to train robots
* [ELF](https://github.com/facebookresearch/ELF)
* [Gazebo](http://gazebosim.org/)
* [V-REP](http://www.coppeliarobotics.com/)

## Physics engines
* MuJoCo
* Box2d, 
* Others: Bullet, ODE, DART, Simbody, PhysX, Havok

## Survey
* Simulation Tools for Model-Based Robotics : Comparison of Bullet , Havok , MuJoCo , ODE and PhysX (Erez, 2015)
  * MuJoCo wins the robotics-related tests.
  * MuJoCo was both the fastest and the most accurate on constrained sys tems relevant to robotics, and 
    was capable of stable grasping at a much larger time step.
  * On systems composed of many disconnected bodies it was the slowest in term of raw CPU speed (while ODE was the fastest),
    however it remained the most accurate overall.
  * In grasping, Mujoco produces qualitatively accurate simulation (in terms of not dropping the object) with 
    large time steps, i.e 16 ms
* Tools for simulating humanoid robot dynamics: A survey based on user feedback (Ivaldi, 2015)
* Evaluation of Physics Engines for Robotic Simulations with a Special Focus on the Dynamics of Walking Robots (Roennau, 2013)
