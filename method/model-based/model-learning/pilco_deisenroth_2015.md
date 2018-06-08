# PILCO: Gaussian Processes for Data-Efficient Learning in Robotics and Control
* Marc Peter Deisenroth, Dieter Fox, and Carl Edward Rasmussen
* ieee transactions on pattern analysis and machine intelligence, vol. 37, no. 2, february 2015
* https://doi.org/10.1109/TPAMI.2013.218
* 10.1.1.225.4072.pdf

## problem
* autonomous reinforcement learning (RL) approaches typically require many interactions with
  the system to learn controllers, which is impractical, slow, and time consuming; aka data inefficiency;
  current solutions require task-specific knowledge in form of
  * expert demonstrations,
  * realistic simulators,
  * pre-shaped policies, or
  * specific knowledge about the underlying dynamics
* model-based RL can suffer severely from model errors,i.e.,
  they inherently assume that the learned model resembles the real environment sufficiently accurately

## idea: Probabilistic Inference for Learning Control (PILCO)
* learn a probabilistic, non-parametric Gaussian process **transition model** of the system.
  * a probabilistic model places a posterior distribution on plausible transition functions and
    expresses the level of uncertainty about the model itself.
* explicitly incorporating model uncertainty into long-term planning and controller learning
  (so that our approach reduces the effects of model errors)
* PILCO is a policy search method and does **not require** state space discretization.
  * closed-form Bayesian averaging over infinitely many plausible dynamics models is possible by using non- parametric GPs.

## result
* nonparametric Bayesian models can play a fundamental role in classical control set-ups, while
  avoiding the typically excessive reliance on explicit models
* a concrete example of the importance of Bayesian modeling and inference for **fast learning from scratch**
* limitation:
  * limited to episodic set-ups.

## comment
* not yet: neural nets for learning transition model?
* seems strong relation with bayesian RL
* ? Model uncertainty is easily evaluated?
