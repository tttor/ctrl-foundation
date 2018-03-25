# 15 Neuroscience

## 15.7 Neural Actor–Critic
Actor–critic algorithms learn both policies and value functions.
* The ‘actor’
  * is the com ponent that learns policies,
  * Based on these critiques, the actor continually updates its policy.
* the ‘critic’
  * is the component that learns about whatever policy is currently being followed by the actor
    in order to ‘criticize’ the actor’s action choices.
  * uses a TD algorithm to learn the state-value function for the actor’s current policy.
  * to critique the actor’s action choices by sending TD errors, δ, to the actor.

Implementation of an actor–critic algorithm as an artificial neural network:
* The critic consists of
  * a single neuron-like unit, V, whose output activity represents state values, and
  * a component shown as the diamond labeled TD that computes TD errors by
    combining V’s output with reward signals and with previous state values
* The actor network has
  * a single layer of k actor units labeled Ai , i = 1, . . . , k.
  * The output of each actor unit is a component of a k-dimensional action vector.
