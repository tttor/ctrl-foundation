# sutton_2017.md
* http://www.incompleteideas.net/book/the-book-2nd.html
* https://github.com/ShangtongZhang/reinforcement-learning-an-introduction

## ch 1
* Most distinguishing features of RL:
  * being a close loop
  * no direct instruction on what action to take
  * action consequences play out over extended period
  * trade-off between exploration and exploitation
  * trying to maximize a reward signal instead of trying to find hidden structure
  * learning from interaction
  * toward simpler and fewer general principles of artificial intelligence
  * time really matters (sequential, not iid)

* Most work in planning does not consider planning's role in real-time decision making (specifically offline planning) or
the question of where the predictive models necessary for planning would come from.
When reinforcement learning involves planning, it has to address the interplay between planning and real-time action selection,
as well as the question of how environment models are acquired and improved.
Note also that, the most important component of almost all reinforcement learning algorithms we consider is
a method for efficiently estimating values

* Four subelements of RL:
  * a policy
  * a reward signal
  * a value function
  * a model of environment (optional\footnote{used for planning in model-based RL})

* Evolutionary methods for RL evaluate the lifetime behavior of, typically, many non-learning agents,
each using a different policy for interacting with its environment,
and select those that are able to obtain the most reward.
Evolutionary methods have advantages on problems in which the learning agent cannot accurately
sense the state of its environment, or if the space of policies is sufficiently small, or
can be structured so that good policies are common or easy to find
or if a lot of time is available for the search.


* In Tic-Tac-Toe, one learns a model of the opponent’s behavior, up to some level of confidence,
and then apply dynamic programming to compute an optimal solution given the approximate opponent model.

## ch 6
* The simplest TD update is
\begin{equation}
V(S_t) \leftarrow V(S_t) + \alpha [ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) ]
\end{equation}

* The SARSA (on-policy) and Q-learning (off-policy) are as follows, respectively:
\begin{equation}
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~Q(S_{t+1},A_{t+1}) - Q(S_{t},A_{t})]
\end{equation}
\begin{equation}
Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~max_a Q(S_{t+1},a) - Q(S_{t},A_{t})]
\end{equation}

## ch 8
Model-based RL requires a model of the environment, model-free RL does not.
Model-based methods rely on planning as their primary component, while model-free methods primarily rely on learning.
Model here refers to anything that an agent can use to predict how the environment will respond to its actions.

A unified view of planning and learning is based on two basic ideas:
\begin{itemize}
\item all state-space planning methods involve computing value functions as a key intermediate step toward improving the policy, and
\item they compute value functions by backup operations applied to simulated experience.
\end{itemize}

One way to integrate learning and planning processes is simply by allowing both
to update the same estimated value function.
Any of the learning methods can be converted into planning methods simply by
applying them to simulated (model-generated) experience rather than to real experience.
The most natural approach is for all processes to proceed asynchronously and in parallel.

Planning should be done online in very small steps.
Within a (online) planning agent, there are at least two roles for real experience:
\begin{itemize}
\item used to improve the model (to make it more accurately match the real environment),
i.e model learning, or system identification (in adaptive control)
    \begin{itemize}
    \item make fuller use of a limited amount of experience and thus
    achieve a better policy with fewer environmental interactions.
    \item can efficiently learn model by supervised learning methods
    \item can reason about model uncertainty
    \item two sources of approximation error: model and value function
    \end{itemize}
\item used to directly improve the value function and policy using some kinds of
reinforcement learning methods, i.e. direct RL (model-free learning)
    \begin{itemize}
    \item much simpler and
    \item are not affected by biases in the design of the model.
    \end{itemize}
\end{itemize}

In Dyna-Q algorithm, the same reinforcement learning method is used both for
learning from real experience and for planning from simulated experience.

There are two ways of thinking about planning:
\begin{itemize}
\item \emph{background planning:}
using simulated experience to gradually improve a policy or value function,
\item \emph{decision time planning:}
using simulated experience to select an action for the current state,
this is also called online planning;
the values and policy are specific to the current state and the action choices available there,
so much so that the values and policy created by the planning process are typically discarded after
being used to select the current action.
\end{itemize}

In model learning, the goal is to estimate a model from experience $\{S_1, A_1, R_2, ..., S_t \}$.
That is a supervised learning problem, where:
$(S_1, A_1) \mapsto (S_2, R_2), (S_2, A_2) \mapsto (S_3, R_3), \ldots, (S_{t-1}, A_{t-1}) \mapsto (S_t, R_t)$.
Learning $s, a \mapsto r$ is a regression problem, whereas
learning $s, a \mapsto s'$ is a density estimation problem.

## priority
* 13 Policy Gradient Methods

