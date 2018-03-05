# Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics
ICML 2017: https://arxiv.org/abs/1706.04317

## problem
* task-to-task transfer

## idea: Schema Networks
*  an object-
oriented generative physics simulator capable
of disentangling multiple causes of events and
reasoning backward through causes to achieve
goals.
* can learn the dynamics of an
environment directly from data
*  learning objective for Schema Networks is de-
signed to understand causality within these environments;
 Instead of learning policies to maximize re-
wards,


## setup
compare
Schema Networks with Asynchronous Advan-
tage Actor-Critic and Progressive Networks on a
suite of Breakout variations, reporting results on
training efficiency and zero-shot generalization,

The environments considered in this work are conceptually
diverse but also simplified in a number of ways with re-
spect to the real world: states, actions, and rewards are all
discretized as binary random variables; the dynamics of the
environments are deterministic; and there is no uncertainty
in the observed entity states.

## comments
* use physics engine
