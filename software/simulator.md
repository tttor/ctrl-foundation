# simulators

## Physics engines
* MuJoCo
* Bullet 
* ODE
* DART
* Box2d, 
* Simbody
* PhysX
* Havok

## Full-blown simulators:
* [TORCS](http://torcs.sourceforge.net/), [gym_torcs](https://github.com/ugo-nama-kun/gym_torcs)
* [ALE](https://github.com/mgbellemare/Arcade-Learning-Environment): 
  tasks with high-dimensional state inputs and discrete actions
* [Gazebo](http://gazebosim.org/)
* [V-REP](http://www.coppeliarobotics.com/)

## Survey
@article{Erez2015,
author = {Erez, Tom and Tassa, Yuval and Todorov, Emanuel},
file = {:home/tor/people/xother/simulator/07139807.pdf:pdf},
isbn = {9781479969234},
pages = {4397--4404},
title = {{Simulation Tools for Model-Based Robotics : Comparison of Bullet , Havok , MuJoCo , ODE and PhysX}},
year = {2015}
}
In \cite{Erez2015}: MuJoCo wins the robotics-related tests.
MuJoCo was both the fastest and the most accurate on constrained sys-
tems relevant to robotics, and was capable of stable grasping
at a much larger time step.
On systems composed of many disconnected bodies it was the slowest in term of raw CPU
speed (while ODE was the fastest), however it remained the
most accurate overall.
In grasping, Mujoco produces qualitatively accurate simulation (in terms of not
dropping the object) with large time steps, i.e 16 ms

@article{Ivaldi2015,
archivePrefix = {arXiv},
arxivId = {1402.7050},
author = {Ivaldi, Serena and Peters, Jan and Padois, Vincent and Nori, Francesco},
doi = {10.1109/HUMANOIDS.2014.7041462},
eprint = {1402.7050},
file = {:home/tor/people/jan/07041462.pdf:pdf},
isbn = {9781479971749},
issn = {21640580},
journal = {IEEE-RAS International Conference on Humanoid Robots},
pages = {842--849},
title = {{Tools for simulating humanoid robot dynamics: A survey based on user feedback}},
volume = {2015-February},
year = {2015}
}

@article{Roennau2013,
author = {Roennau, A and Sutter, F and Heppner, G and Oberlaender, J and Dillmann, R},
file = {:home/tor/people/xother/simulator/06766527.pdf:pdf},
isbn = {9781479927227},
keywords = {1,bullet,comparison and evaluation,dynamics,engines,fig,for physics,legged locomotion,ode,physics engine,physx,robot simulation,robots,virtual run-time experiments developed,walking},
title = {{Evaluation of Physics Engines for Robotic Simulations with a Special Focus on the Dynamics of Walking Robots}},
year = {2013}
}
