# Value Iteration Networks
* Aviv Tamar, Yi Wu, Garrett Thomas, Sergey Levine, and Pieter Abbeel
* 30th Conference on Neural Information Processing Systems (NIPS 2016), Barcelona, Spain.

## problem

## idea: value iteration network (VIN)
* a fully differentiable neural network with a planning module embedded within.
  * learn to plan
* key:
  * a novel differentiable pproximation of the value-iteration algorithm, 
    * which can be represented as a convolutional neural network, and 
      trained end-to-end using standard backpropagation.

