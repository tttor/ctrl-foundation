# Statistical reinforcement learning
* Masashi Sugiyama
* Chapman & Hall/CRC
* 2015 by Taylor & Francis Group, LLC

## Foreword
* in rl, the env is modeled as mdp that provides immediate reward and
  state info to the agent however, the agent does not have access to the
  transition structure and needs to choose actions to max its overal
  reward
* algo
  * policy search: manipulate policy params
  * policy iteration: estimate value func

## Preface
* reward to evaluate the validity of predicted output
* reward is usually much easier, less costly than giving supervision
* various supervised and unsupervised learning are also utilized in rl

## ch 1: intro
* rl
  * knowing transitions intuitively means knowing the map
  * knowing the reward intuitevely means knowing the location of the goal states
  * the valuc func can be obtainded using dynamic programming (dp)
  * dp is essentially a general method for solving complex opt problem by
    breaking down into recursive subproblems,
    assuming many subproblems are actually the same, dp solves overlapped subproblem once
    and reuse the solution to reduce comp cost
  * the illustration of car climbing in fig 1.9-10 is seemingly intuitive, but
    * `imo,, with epsilon-greedy action selection the car will move to the right first, then`
    * `in epsilon random, it will choose left, then observer left can deliver to higher right, then choose left again. etc`
  * again, the term model indicates a model of transition probability
  * learning trasnsition model is hard estimation problem, so if there is no prior then model-free is promising

* model-free policy approx
  * value funct approximatino corresponds to a regression problem.
  * fig 1.13 is basically q-learning
  * disadv:
    * policy is learnt via value funct,
      hence improving the quality of value func approx does not necessarily contribute to improving the quality of resulting policy
    * a small chanhe in value func can cause big diff in policy, leading to instastabily in control
    * the maximization of Q wrt a is expensive when A is continuous

* model-free policy search
  * to dinf a policy that max return
  * may lead to instability due to the stochasticity of the policies,
  * alternatively, policy-prior search

* model-based rl
  * explicitly learns the transitinon func and uset the learn env model for policy learning
  * model-based is useful when data-colletion (trials) in real robots is expensive
  * but estimating the transiton model from limited amount of data and multi-dim cont space is also hard

## part2: model free policy iter
* policy iteration (= policy eval + policy improvement)
  vs policy search

## ch 2: policy iter with value fn approx
* learning value fn from data can actually be regarded as a regression problem: least-square policy iter
* regression is formulated as minimization of goodness-of-fit and regularization terms, e.g
  l2-regularizer (ridge regression) and l1-regularization (lasso: least absolute shrinkage and selection operator)

## ch 3: basis design for value fn approx
* alternative to gaussian kernel (that cannot approx discontinuous fn well):
  geodesic gaussian kernels,
  ordinary gaussian kernels
* mdp-induced graph
* ordinary gaussian kernel,
  $K(s,s') = exp(- \frac{ED(s,s')}{2\sigma^2})$, where
  $ED(s,s') = || x - x' ||$
* geodesic (=shortest path (SP)):
  $K(s,s') = exp(- \frac{SP(s,s')}{2\sigma^2})$,

* conditional density estimation
via gaussian process estimation

when the conditioning variable $(s,a)$ are discrete, the conditional density can be estimated by standard density estimators such as
kernel density estimation by only using samples.
$\epsilon$-KDE extends this idea to the continuous case, but not scale to hi dim problem.

Least-squares conditiona density estimation by sugiyama;
as a non-parametric conditional density estimator

* model-based rl
the procedure in page 161-162 is ridiculous:
run model-free inside model-based loop,
it seems the author did not read RL book by suton (a;though it is listed in biblio)

* numerical examples
comparison between model-based and model-free

* remarks
model based pgpe with lscde

## ch?: dimensionality reduction for transition model estimation
* for hi dim action and state spaces

* sufficient dim red
to find a low-dimensional expression of input $(s,a)$ that contains "sufficient" info about $s'$

* remarks
  * squared-loss conditional entropy (SCE) for dim red,
  this allows performing dim red and conditional density estimation simultaneously

## comments
* perhaps, this book should be titled: machine learning methods for RL :)
* this book is more on application of sugiyama's learning methods to rl
