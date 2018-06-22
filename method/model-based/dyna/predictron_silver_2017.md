# The Predictron: End-To-End Learning and Planning
* D Silver et al
* icml2017
* http://proceedings.mlr.press/v70/silver17a
* https://vimeo.com/238243832

## problem
* to learn models that are effective in the context of planning

## idea: predictron
* consists of a fully abstract model, represented by
a Markov reward process, that can be rolled for-
ward multiple “imagined” planning steps. Each
forward pass of the predictron accumulates in-
ternal rewards and values over multiple plan-
ning depths.
* is a single differentiable architecture that
rolls forward an internal model to estimate external values.
* the model is fully abstract: it need not correspond
to the real environment in any human understandable fash-
ion, so long as its rolled-forward “plans” accurately predict
outcomes in the true environment.
* may be viewed as a novel network architecture that incorporates several separable ideas.
  * First, the
predictron outputs a value by accumulating rewards over
a series of internal planning steps.
  * Second, each forward
pass of the predictron outputs values at multiple planning
depths.
  * Third, these values may be combined together, also
within a single forward pass, to output an overall ensemble
value.
  * Finally, the different values output by the predictron
may be encouraged to be self-consistent with each other,
to provide an additional signal during learning
