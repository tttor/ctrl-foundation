# [David Silver, Deep RL, RDLM 2015](http://videolectures.net/rldm2015_silver_reinforcement_learning/)
Tutorial: Deep Reinforcement Learning
David Silver, Google DeepMind

DeepRL:
* Deep Value Functions
* Deep Policies
* Deep Models

Powerful RL requires powerful representations,
one way is via deep representation (learning)

Deep representation:
* is a composition of many functions
* Its gradient can be backpropagated by the chain rule

A deep neural network is typically composed of:
* Linear transformations
* Non-linear activation functions
  * step fn
  * linear fn
  * threshold logic
  * sigmoid fn

Weight Sharing:
* Recurrent neural network shares weights between time-steps;
which is suitable for partial obsevability in reinforcement learning
* Convolutional neural network shares weights between local regions

A loss function measures goodness of output:
* log likelihood
* mean-squared err

NN:
* The loss is appended to the forward computation
* Gradient of loss is appended to the backward computation

Minimize Loss via Stochastic Gradient Descent,
we may end up with local optima, but in deep learning:
* should not worry a lot for getting stuck in local optima
* in DL, this stuck does not happen
* in hi dim space, with very high prob local optima is almost as good as global optima
* as the size of params get larger and larger, you should worry less and less about local optima
* have to be careful about param initialization

Simple ingredients solve supervised learning problems
* Use deep network as a function approximator
* Define loss function
* Optimise parameters end-to-end by SGD

Use deep network to represent value function / policy / model
* Optimise value function / policy /model end-to-end
* Using stochastic gradient descent

Bellman Equation
* Bellman expectation equation
  * Policy iteration algorithms solve Bellman expectation equation
* Bellman optimality equation
  * Value iteration algorithms solve Bellman optimality equation

Policy Iteration with Non-Linear Sarsa
* Represent value function by Q-network with weights w
* Define objective function by mean-squared error in Q-values
* Leading to the following Sarsa gradient
* Optimise objective end-to-end by SGD,

Stability Issues with Deep RL, <br/>
Naive Q-learning oscillates or diverges with neural nets
* Data is sequential:
  * Successive samples are correlated, non-iid
* Policy changes rapidly with slight changes to Q-values
  * Policy may oscillate
  * Distribution of data can swing from one extreme to another
* Scale of rewards and Q-values is unknown
  * Naive Q-learning gradients can be large unstable when backpropagated

DQN provides a stable solution to deep value-based RL;
(the effect of these strategy are proven empirically):
* Use experience replay;
  disadvantage: can not use eligibility traces, this is what is sacrificed here;
  one naive solution is to use short replay, but yes this is an open question
  * Break correlations in data, bring us back to iid setting
  * Learn from all past policies
  * Using off-policy Q-learning
  (you learn with a policy you used before, that is different from the current (now) policy)
* Freeze target Q-network
  * Avoid oscillations
  * Break correlations between Q-network and target
* Clip rewards or normalize network adaptively to sensible range
  * Robust gradients
  * (later, we do not clip but normalize the reward, Normalized DQN)

DQN in Atari
* End-to-end learning of values Q(s, a) from pixels s
* Input state s is stack of raw pixels from last 4 frames
* Output is Q(s, a) for 18 joystick/button positions
* Reward is change in score for that step

Policy Gradient for Continuous Actions
* Represent policy by deep network a = π(s, u) with weights u
* Define objective function as total discounted reward
* Optimise objective end-to-end by SGD,
i.e. Adjust policy parameters u to achieve more reward
* Policy gradient is the direction that most improves Q,
this lead to Deterministic Actor-Critic

Deterministic Actor-Critic (Use two networks);<br/>
Critic estimates value of current policy by Q-learning;<br/>
Actor updates policy in direction that improves Q
* Actor is a policy π(s, u) with parameters u
* Critic is value function Q(s, a, w ) with parameters w
* Critic provides loss function for actor
* Gradient backpropagates from critic into actor

Naive actor-critic oscillates or diverges with neural nets: <br/>
Deterministic Deep Policy Gradient (DDPG) provides a stable solution, via:
* Use experience replay for both actor and critic
* Freeze target network to avoid oscillations

DDPG for Continuous Control
* End-to-end learning of control policy from raw pixels s
* Input state s is stack of raw pixels from last 4 frames
* Two separate convnets are used for Q and π
* Physics are simulated in MuJoCo

Deep Model for model-based RL:
* Learn a transition model of the environment using deep network
* Plan using the transition model
e.g. Lookahead using transition model to find optimal actions
* Define objective function measuring goodness of model
e.g. number of bits to reconstruct next state
* Optimise objective by SGD

Challenges of Model-Based RL (case: the game of GO using monte-carlo search)
* Compounding errors
  * Errors in the transition model compound over the trajectory
  * By the end of a long trajectory, rewards can be totally wrong
  * Model-based RL has failed (so far) in Atari
* Deep networks of value/policy can “plan” implicitly
  * Each layer of network performs arbitrary computational step
  * n-layer network can “lookahead” n steps
  * Are transition models required at all?

Comment
* improve DQN in Atari for some types of games that are now below human level,
e.g montezuma's revenge (which needs planning), private eye, gravitar
* in this version of DQN Atari, we do not impose biological constraint,
e.g noise, reaction time, there is only one human playing for the graph,
the point here is just about representation learning
* atari dqn, and ddpg demo are model-free (w/o planning)
* Model-based RL has failed (so far) in Atari
* misconception: we have to spend ages to tune hyperparam, e.g network architecture;
(david: for what has been shown, we use first architecture and it work, so
we may think of NN as blackbox)
* open problem: RL in partial observability
* vanishing gradient problem?
