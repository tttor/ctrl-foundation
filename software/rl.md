# RL software

See also a curated list in awesome-rl\footnote{\url{https://github.com/aikorea/awesome-rl}}.
Software includes:
\begin{itemize}
\item BURLAP \cite{MacGlashan2017}
\item OpenAI Gym \cite{Brockman2016}
\item PyBrain \cite{Schaul2010}
\item RL-Glue \cite{Tanner2009}
\item AI-Toolbox: \url{https://github.com/Svalorzen/AI-Toolbox}
\end{itemize}

To date (Nov 23, 2017), available packages in ROS for model-based and model-free RL are limited to the following. Surely, any package can be used in ROS with some efforts.
\begin{itemize}
\item rl-texplore-ros-pkg \cite{Hester2012}\footnote{\url{https://github.com/toddhester/rl-texplore-ros-pkg}}
\item OpenAI Gym with ros-bridge from ErleRobotics \cite{Zamora2016} \footnote{\url{https://github.com/erlerobot/gym-gazebo/}}
\end{itemize}

### OpenAI Gym \cite{Brockman2016}
OpenAI Gym\footnote{\url{https://github.com/openai/gym} and \url{https://openai.com/}} is a toolkit for developing and comparing reinforcement learning algorithms.
OpenAI Gym has interfaces with physics engines, such as: Mujoco and Box2D.
OpenAI is quite young and under heady development.
There was a bridge to ROS, i.e. rosbridge\footnote{\url{https://github.com/openai/rosbridge}}, but now is abandoned as they changed to a different system.
Gym-gazebo~\cite{Zamora2016} extends
OpenAI Gym for robotics using the Robot Operating System (ROS) and the Gazebo simulator.

Useful modules in OpenAI Gym:
\begin{itemize}
\item OpenAI Baselines\footnote{\url{https://github.com/openai/baselines}}
is a set of high-quality implementations of reinforcement learning algorithms.
This mostly is about deep RL.
\item RoboSchool: Open-source software for robot simulation, integrated with OpenAI Gym.
To replicate Gym MuJoCo environments.
\item rllab\footnote{\url{https://github.com/rll/rllab}} is a framework for developing and evaluating reinforcement learning algorithms.
rllab is a work in progress, input is welcome. The available documentation is limited for now.
\end{itemize}

### BURLAP \cite{MacGlashan2017}

Burlap stands for Brown-UMBC Reinforcement Learning And Planning.
BURLAP uses a highly flexible system for defining states and and actions of nearly any kind of form, supporting discrete continuous, and relational domains. Planning and learning algorithms range from classic forward search planning to value function-based stochastic planning and learning algorithms. Also included is a set of analysis tools such as a common framework for the visualization of domains and agent performance in various domains.

### rltexplore-ros-pkg
The rltexplore-ros-pkg\footnote{\url{https://github.com/toddhester/rl-texplore-ros-pkg}}
directory contains a ROS stack for reinforcement learning (RL). The
code in this repository provides agents, environments, and multiple ways for
them to communicate (through ROS messages, or by including the agent and
environment libraries)

Initially developed in 2011, updated in 2015 for Indigo.
