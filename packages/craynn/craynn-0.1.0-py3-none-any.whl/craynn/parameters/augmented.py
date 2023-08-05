from ..meta import derive
from .meta import Parameter
from .common import const_init

__all__ = [
  'scaled',
  'biased',
  'default_dependency_strategy'
]

def default_dependency_strategy(param):
  if param.properties.get('weights', False):
    return scaled(param, dependency_strategy=default_dependency_strategy)
  elif param.properties.get('biases', False):
    return biased(param, dependency_strategy=default_dependency_strategy)
  else:
    return param

class AugmentedParameter(Parameter):
  def __init__(self, param : Parameter, op, augment):
    self.op = op

    self.augments = [
      augment(var.shape)
      for var in param.variables()
    ]

    self.param = param
    super(AugmentedParameter, self).__init__(param.shape, properties=param.properties, name=param.name)

  def get_augments(self):
    return self.augments

  def variables(self):
    return self.param.variables()

  def get_output_for(self, *vars):
    return self.param.get_output_for(*(
        self.op(var, augment())
        for augment, var in zip(self.augments, vars)
    ))

  def apply(self):
    for var, augment in zip(self.param.variables(), self.augments):
      var.assign(self.op(var, augment()))

def _scale(var, augment):
  return var * augment

def _bias(var, augment):
  return var + augment

ScaledParameter = derive('ScaledParameter').based_on(AugmentedParameter).with_fixed(
  op=_scale,
  augment=lambda shape: const_init(value=1, augment=True)(shape=())
)

scaled = ScaledParameter

BiasedParameter = derive('BiasedParameter').based_on(AugmentedParameter).with_fixed(
  op=_bias,
  augment=lambda shape: const_init(value=0, augment=True)(shape=())
)

biased = BiasedParameter


