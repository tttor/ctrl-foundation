# Model-based Bayesian Reinforcement Learning with Generalized Priors
asmuth_2013

In Bayesian approach, knowledge given to the algorithm before any action or from its own related experience is formalized into a prior.
The Bayesian-based machine learning takes the prior and combined it with the observation to create a posterior.

Proposed two different approaches to Bayesian model-based RL, namely: BOSS and BFS3.
BOSS is the model-sampling approach, whereas BFS3 is the experience-sampling approach.

Asmuth also makes a strict distinction between planning (control) and RL.
The former always assumes known model and there is no need to learn about and explore the environment.
Planning focuses on efficient ways to act, once given a model.
In contrast, the latter assumes that the some portion of the world must be learned to develop good agent behavior.
The Bayesian RL its efforts on building complex models that can be used as priorsin learning, and
works on efficient inference approximations.
Given unknown worlds, there is exploitation/exploration trade-off.

The optimal policy is `$\phi^{*} = argmax_{\phi} R_{\phi}$, with $R_{\phi} = \sum_{t=0}^{\infty} \gamma^{t} E_{\phi}[r_t]$`.
The value of a state, $V(s)$, is related to the Q-value of a state-action, $Q (s, a)$ via
```
\begin{equation}
V(s) = max_{a} Q(s,a)
\end{equation}
\begin{equation}
Q(s,a) = R(s,a) + \gamma \sum_{s'}^{} T(s,a,s') s' V(s')
\end{equation}
```

Optimality guarantees for an RL algorithm include:
* convergence:
  if it will provably act with the optimal policy in the limit, or after an infinite number of steps, e.g. Q-learning
* probably-approximately-correct MDP (PAC-MDP):
  if it will, with high probability, make approximately optimal decision for all but polynomial number of steps, e.g R-MAX
* bayes-optimal:
  is an optimality guarantee made in the context of an MDP prior.
* Probably Approximately Correct for Bayes Adaptive MDPs (PAC-BAMDP):
  if it, with probability $1-\delta$, make $\epsilon$-Bayes optimal decisions for all but polynomial number of steps

Bayesian inference is based on Bayes rule as follows:
```
\begin{equation}
P(H|E) = \frac{P(E|H) P(H)}{P(E)}
\end{equation}
where $P(H|E)$ is the posterior,
$P(E|H)$ is the probability of Evidence conditioned on the Hypothesis (the data likelihood),
$P(H)$ is the prior, and $P(E)$ plays the role of a normalizing factor.
```
