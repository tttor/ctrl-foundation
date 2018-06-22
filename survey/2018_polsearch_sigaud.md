2018_polsearch_sigaud.md

## intro
* Sample efficiency can be declined into three aspects:
  * (1) data efficiency, i.e. extracting more information
from available data (definition taken from (Deisen-
roth and Rasmussen, 2011)),
  * (2) sample choice, i.e.
obtaining data in which more information is avail-
able and
  * (3) sample reuse, i.e. improving a policy
several times by using the same samples more than
once through experience replay.
* important distinction in the policy search
domain is
  * whether the optimization method is
    * episode-based or
    * step-based

## 2. Policy search without a utility model
* Policy search without a util-
ity model is generally less data efficient
than SGD. Though sample reuse is tech-
nically possible, in practice it is seldom
used.Despite their lesser sample efficiency,
some of these methods are highly paral-
lelizable and offer a viable alternative to
deep RL provided enough computational re-
sources

## 3. Policy search with a model in the space of policy parameters
* Bayesian optimization (BO) is an instance of op-
timization with a model in θ where, instead of
learning a single model, a distribution over proba-
bilities of such models is updated through Bayesian
inference. The distribution over models is initial-
ized with some prior, and each new sample, con-
sidered as some new evidence, helps adjusting the
model distribution towards a peak at the true value
while keeping track of the variance over models.
* Message 2: Bayesian Optimization is BBO
managing a distribution over models in the
policy parameter space. Its sample effi-
ciency benefits from active choice of sam-
ples, but performing global search results in
a lesser scalability. Thus, it **cannot** be ap-
plied as such to deep neural network repre-
sentations.

## 4. Directed exploration methods
* Message 3: Looking for diversity only in
a user defined outcome space is an efficient
way to perform exploration, and can help
solve sparse or deceptive reward problems,
where more standard exploration would fail.
Directed exploration methods are thus use-
ful complements to other methods covered
in this survey.
* many policy search algorithms alternate between
  * collecting new step sam-
ples from the current policy to compute a new critic
(in iterative approaches, see Section 5.2) or
  * improve the current critic (in incremental approaches, see
Section 5.3) and using this critic to improve the
current policy (see Figure 3 for an illustration).
* a replay buffer is at the heart of the emergence of
modern actor-critic approaches in deep RL
  * Stabil-ity is improved by drawing the samples randomly
from the replay buffer and
  * sample efficiency can be
further improved by better choosing the samples,
using prioritized experience replay
* Message 4: Being step-based, deep RL
methods make a better use of their sam-
ple information. In particular, actor-critic
methods benefit from being incremental and
give rise to a lot of sample reuse in approxi-
mating the critic with deep neural networks
using a replay buffer.

## 6. Discussion
* policy search methods
which build a model of the utility function are gen-
erally more sample efficient than methods which do
not.
* Several elements speak in favor of the higher sam-
ple efficiency of learning a critic.
  * First, it can give
rise to more sample reuse than learning a model of
the utility function in Θ.
  * Second, learning from
each step separately makes a better use of the in-
formation available from a trajectory than learning
from global episodes.

### 6.3. Iterative versus incremental learning of a critic
* incremental update of a critic may
seem superior to iterative updates, for three rea-
sons.
  * First, by avoiding to compute the critic again
at each iteration, it is computationally more effi-
cient.
  * Second, immediate updates favor data ef-
ficiency because the policy is improved as soon as
possible, which in turn helps generating better sam-
ples.
  * Third, being based on bootstrap methods,
they give rise to more sample reuse.
* **However**, Two factors must be taken
into account, as described below.
  * Trading bias against variance
    * Instead of performing bootstrap
updates of a critic over one step, one can do so
over N steps. The larger N , the closer to Monte
Carlo estimation, thus tuning N is a way of con-
trolling the bias-variance compromise.
  * Off-policy versus on-policy updates
    * In most iterative policy gradient methods, the
samples are discarded from one iteration to the next
and these methods are generally on-policy. By con-
trast, incremental methods using a replay buffer are
generally off-policy
    * when learning a critic incrementally, using off-
policy updates is more flexible because the samples
can come from any policy, but these off-policy up-
dates introduce bias in the estimation of the critic.
* Message 6: Incremental methods are supe-
rior to iterative methods in many respects,
but iterative methods are more stable be-
cause they decorrelate the problem of esti-
mating the utility function from the problem
of descending its gradient, and they suffer
from less bias.

## 7. Conclusion
* deep RL is generally more sample efficient than
evolutionary methods
* higher sample efficiency of deep RL methods, and
particularly incremental actor-critic architectures,
results from several mechanisms.
  * They benefit from
better approximation capability of non-linear crit-
ics and the incorporation of an adapted step size in
SGD,
  * they model the utility function in the state-
action space, and
  * they benefit from massive sample reuse using a replay buffer.
* the field of policy search is the
object of an intensive race for increased perfor-
mance, stability and sample efficiency.
