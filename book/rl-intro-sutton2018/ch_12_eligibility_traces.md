# 12: Eligibility Traces
Eligibility traces:
* `$\lambda=1$`: Monte Carlo
* `$\lambda=0$`: one-step TD
* intermediate methods that are often better than either extreme method
* provide a way of implementing Monte Carlo methods online and on continuing problems without episodes.
* The mechanism is
  * a short-term memory vector, the eligibility trace `z_t \in R^d` , that
    parallels the long-term weight vector `w_t \in R^d` .
* The rough idea is that
  * when a component of `w_t` participates in producing an estimated value, then
    the corresponding component of `z_t` is bumped up and then begins to fade away.
  * Learning will then occur in that component of `w_t` if a nonzero TD error occurs
    before the trace falls back to zero.
  * The trace-decay parameter `\lambda \in [0, 1]` determines the rate at which the trace falls.
* computational advantage of eligibility traces over n-step methods
  * only a single trace vector is required **rather than** a store of the last n feature vectors.
  * Learning also occurs continually and uniformly in time **rather tha**
    being delayed and then catching up at the end of the episode.
  * learning can occur and affect behavior immediately after a state is encountered
    **rather than** being delayed n steps

## 12.1 The λ-return
Note that
* a valid update can be done not just toward any n-step return, but
  toward any average of n-step returns.
* compound update:
  An update that averages simpler component updates

The TD(λ) algorithm:
* as one particular way of averaging n-step updates.
* This average contains all the n-step updates,
  each weighted proportional to λ n−1 (where λ ∈ [0, 1]), and
  is normalized by a factor of 1 − λ to ensure that the weights sum to 1 (see Figure 12.1).
* λ-return: `G^{\lambda}_t = (1 - \lambda)  \sum_{n=1}^{\inf} \lambda^{n-1} G_{t:t+n}`
* The parameter λ characterizes
  how fast the exponential weighting in falls off, and thus
  how far into the future the λ-return algorithm looks in determining its update.

off-line λ-return algorithm.
* makes no changes to the weight vector during the episode.
* at the end of the episode, a whole sequence of off-line updates are made according to
  our usual semi-gradient rule, using the λ-return as the target

**forward view** of a learning algorithm:
For each state visited, we look forward in time to all the future rewards and
decide how best to combine them

## 12.2 TD(λ)
TD(λ) improves over the off-line λ-return algorithm
* it updates the weight vector on every step of an episode rather than only at the end, and
  thus its estimates may be better sooner.
* its computations are equally distributed in time rather that all at the end of the episode.
* it can be applied to continuing problems rather than just episodic problems

With function approximation, the eligibility trace is
* a vector `z_t ∈ R^d` with the same number of components as the weight vector `w_t`
* the weight vector is a long-term memory, accumulating over the lifetime of the system,
* the eligibility trace is a short-term memory, typically lasting less time than the length of an episode.

Eligibility traces assist in the learning process;
their only consequence is that they affect the weight vector, and
then the weight vector determines the estimated value.

TD(1) is a way of implementing Monte Carlo algorithms
* Whereas the earlier Monte Carlo methods were limited to episodic tasks,
  TD(1) can be applied to discounted continuing tasks as well.
* Moreover, TD(1) can be performed incrementally and on-line.
* On-line TD(1) learns in an n-step TD way from the incomplete ongoing episode, where
  the n steps are all the way up to the current step.
  * If something unusually good or bad happens during an episode,
    control methods based on TD(1) can learn immediately and
    alter their behavior on that same episode.

## 12.3 n-step Truncated λ-return Methods
TODO
