# Asymmetric Actor Critic for Image-Based Robot Learning
* Lerrel Pinto Marcin Andrychowicz Peter Welinder Wojciech Zaremba, Pieter Abbeel

## observation
* training on a physical system can be expensive and dangerous,
  * which has sparked significant interest in learning control policies using a physics simulator.
* While several recent works have shown promising results in transferring policies
  trained in simulation to the real world, they often do **not fully utilize**
  the advantage of working with a simulator

## idea
* exploit the full state observability in the simulator to train
  better policies which take as input only partial observations (RGBD images).
* asymmetric actor-critic,
  * a powerful way of utilizing the full state observability in a simulator.
  * the critic is trained on full states while
  * the actor (or policy) gets rendered images as input.
* combine this method with domain randomization

## setup
* tasks like picking, pushing, and moving a block.

## result
* simulation to real world transfer **without** training on any real world data
  * Coupled with domain randomizationL able to learn visual policies that
    works in the real world while being trained solely in a simulator
* superior to the much stronger imitation learning with DAgger baseline,
  even though it was trained without an expert
