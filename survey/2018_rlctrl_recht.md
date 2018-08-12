# A Tour of Reinforcement Learning The View from Continuous Control
* Benjamin Recht

# intro
Controls is the theory
of designing complex actions from well-specified models, while reinforcement learning often makes
intricate, model-free predictions from data alone.

try to put RL and controls techniques on the same footing through a case study of
the linear quadratic regulator (LQR) with unknown dynamics.

to build
robust, safe learning systems that interact with an uncertain physical environment and that will
surely require tools from both the machine learning and controls community

# 2 What is reinforcement learning?
The important point is that
we can’t solve this optimization problem using standard optimization methods unless we know the
dynamics. We must learn something about the dynamical system and subsequently choose the best
policy based on our knowledge.

We want the
expected reward to be high for our derived policy, but we also need the number of oracle queries
to be small.
 What’s the most efficient way
to use all of the data that’s collected in order to improve future performance?
What is the best way to tie this information together in order to improve performance?

## 2.1 Connections to supervised learning
TODO
