# Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics
ICML 2017: https://arxiv.org/abs/1706.04317

## problem
* task-to-task transfer
* to efficiently generalize experience in one scenario to other similar scenarios
* modeling causality: the ability to reason about previous observations and explain away alternative causes.

## idea: Schema Networks
* is an object-oriented generative physics simulator (a structured generative model of an MDP)
  * capable of disentangling multiple causes of events and reasoning backward through causes to achieve goals.
  * for object-oriented reinforcement learning and planning
* incorporate key desiderata for the flexible and compositional transfer of learned prior knowledge to new settings. 
  * 1) Knowledge is represented with “schemas” – local cause-effect relationships involving one or more object entities; 
  * 2) In a new setting, these cause-effect relationships are traversed to guide action selection; and 
  * 3) The representation deals with uncertainty, multiple-causation, and explaining away in a principled way.  

* can learn the dynamics of an
environment directly from data
*  learning objective for Schema Networks is de-
signed to understand causality within these environments;
 Instead of learning policies to maximize re-
wards,


## setup
* evaluate the end-to-end system on Break-out variations
* compare against 
  * Asynchronous Advantage Actor-Critic (A3C) (Mnih et al., 2016) and 
  * Progres-sive Networks (PNs) (Rusu et al., 2016), which extends A3C explicitly to handle transfer. 
* reporting results on training efficiency and zero-shot generalization,

The environments considered in this work are conceptually
diverse but also simplified in a number of ways with re-
spect to the real world: states, actions, and rewards are all
discretized as binary random variables; the dynamics of the
environments are deterministic; and there is no uncertainty
in the observed entity states.

## comments
* use physics engine
