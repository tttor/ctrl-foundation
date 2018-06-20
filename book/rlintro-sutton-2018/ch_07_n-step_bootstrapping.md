# 7:  n-step Bootstrapping

here: n-step TD methods that
* generalize both monte-carlo and temporal-difference methods
* span a spectrum with MC methods at one end and one-step TD methods at the other.
* enable bootstrapping to occur over multiple steps, freeing us from the tyranny of the single time step.

## 7.1 n-step TD Prediction
Monte Carlo (MC)
* perform an update for each state based on the entire sequence of observed rewards
  from that state until the end of the episode.
* target is the return

(one-step) TD methods
* based on just the one next reward, bootstrapping from the value of the state
  one step later as a proxy for the remaining rewards
* change an earlier estimate based on how it differs from a later estimate (bootstrap).
* the target is the first reward plus the discounted estimated value of the next state

n-step TD methods:
* methods in which the temporal difference extends over n steps
* the generalization of TD and Monte Carlo methods to n-step methods can potentially
  perform better than either of the two extreme methods.
* All n-step returns can be considered approximations to the full return,
  truncated after n steps and then corrected for the remaining missing terms by $V_{t+n-1} (S_{t+n})$

Note that n-step returns for n > 1 involve future rewards and states that are not
available at the time of transition from t to t + 1.
No real algorithm can use the n-step return until after it has seen R_{t+n} and computed V {t+n-1}.
The first time these are available is t + n.

Note that no changes at all are made during the first n-1 steps of each episode.
To make up for that, an equal number of additional updates are made at the end of the episode, after
termination and before starting the next episode.

Error reduction property of n-step returns:
the worst error of the expected n-step return is guaranteed to be less than or equal to
$\gamma^n$ times the worst error under $V_{t+n-1}$

## 7.2 n-step Sarsa
TODO

