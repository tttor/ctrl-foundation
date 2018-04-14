# 17: Frontiers

## 17.1 General Value Functions and Auxiliary Tasks
* a general value function, or GVF

## 17.2 Temporal Abstraction via Options
* Can the MDP framework be stretched to cover all the levels simultaneously?
* to formalize an MDP at a detailed level, with a small time step, yet
  enable planning at higher levels using extended courses of action that
  correspond to many base-level time steps.
  * need a notion of course of action that
    * extends **over many time steps** and
    * includes a notion of termination.
* define an **option** `\omega = < \pi{\omega}, \gamma_{\omega}`...
* a hierarchical policy:
  selects from options rather than actions, where
  options, when selected, execute until termination

## 17.3 Observations and State
TODO
