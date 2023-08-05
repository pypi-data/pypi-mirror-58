import tensorflow as tf

from .common import zeros_init, glorot_normal_init
from .meta import Parameter, parameter_model

__all__ = [
  'SoftmaxParameter',
  'softmax_parameter',

  'PositiveParameter',
  'positive_parameter',
]

class SoftmaxParameter(Parameter):
  def __init__(self, shape, scale=1, w=zeros_init(), properties=None, name=None):
    if properties is None:
      properties = dict()

    self.w = w(shape=shape, **properties, name=(name + '_w') if name is not None else None)
    self.activation = tf.nn.softmax(self.w(), axis=0)

    if scale != 1:
      self.activation = self.activation * scale
    
    super(SoftmaxParameter, self).__init__(shape, properties, name=name)

  def __call__(self):
    return self.activation

  def dependencies(self):
    return [self.w]

  def own_variables(self):
    return []

softmax_parameter = parameter_model(SoftmaxParameter)


class PositiveParameter(Parameter):
  def __init__(self, shape, w=glorot_normal_init(gain=0.5), properties=None, name=None):
    if properties is None:
      properties = dict()

    self.w = w(shape=shape, **properties, name=(name + '_w') if name is not None else None)
    self.activation = tf.nn.softplus(self.w())

    super(PositiveParameter, self).__init__(shape, properties, name=name)

  def __call__(self):
    return self.activation

  def dependencies(self):
    return [self.w]

  def own_variables(self):
    return []


positive_parameter = parameter_model(PositiveParameter)