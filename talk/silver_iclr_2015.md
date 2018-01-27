# [David Silver, Deep RL, ICLR 2015](https://iclr.cc/archive/www/doku.php%3Fid=iclr2015:main.html)

deeprl:combine deep learning with reinforcement learning
* How good is action a in state s?
* Neural network can be a good function approximator for RL

Dichotomy:
* Policy-based RL,
* Value-based RL,
* Model-based RL

Can we apply deep learning to RL?
* Use deep network to represent value function / policy / model
* Optimise value function / policy /model end-to-end
* Using stochastic gradient descent

Deep Q-learning:
* Represent value function by deep Q-network with weights w, Q(s,a,w) approx Q^{\phi}(s,a)
* Define objective function by mean-squared error in Q-values
* Optimise objective end-to-end by SGD

Naive Q-learning oscillates or diverges with neural nets
* Data is sequential:
Successive samples are correlated, non-iid
* Policy changes rapidly with slight changes to Q-values
Policy may oscillate,
Distribution of data can swing from one extreme to another
* Scale of rewards and Q-values is unknown:
Naive Q-learning gradients can be large unstable when backpropagated

Deep Q-Network:
DQN provides a stable solution to deep value-based RL
* Use experience replay (from which we sample iid data)
    * Break correlations in data, bring us back to iid setting
    * Learn from all past policies
* Freeze target Q-network
    * Avoid oscillations
    * Break correlations between Q-network and target
* Clip rewards or normalize network adaptively to sensible range
    * Robust gradients

DQN for atari games:
End-to-end learning of values Q(s, a) from pixels s

Normalized DQN:
Normalized DQN uses true (unclipped) reward signal,
Output is scaled and translated into Q-values,

Gorila (GOogle ReInforcement Learning Architecture)

Deterministic Policy Gradient for Continuous Actions:
Deterministic Actor-Critic;
Use two networks: an actor and a critic
    * Critic estimates value of current policy by Q-learning
    * Actor updates policy in direction that improves Q

Deterministic Deep Actor-Critic;
* Use experience replay for both actor and critic
* Use target Q-network to avoid oscillations

Model-Based RL:
Learn a transition model of the environment;
Represent transition model p(r , s 0 | s, a) by deep network;
Define objective function measuring goodness of model

Challenges of Model-Based RL
* Compounding errors
    * Errors in the transition model compound over the trajectory
    * By the end of a long trajectory, rewards can be totally wrong
    * Model-based RL has failed (so far) in Atari
* Deep networks of value/policy can “plan” implicitly
    * Each layer of network performs arbitrary computational step
    * n-layer network can “lookahead” n steps
    * Are transition models required at all?

Conclusion
* RL provides a general-purpose framework for AI
* RL problems can be solved by end-to-end deep learning
* A single agent can now solve many challenging tasks
* Reinforcement learning + deep learning = AI
