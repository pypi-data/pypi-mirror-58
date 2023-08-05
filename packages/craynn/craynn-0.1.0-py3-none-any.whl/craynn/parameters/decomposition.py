import tensorflow as tf

from .common import glorot_normal_init
from .meta import Parameter, parameter_model

__all__ = [
  'DecompositionParameter',
  'decomposition'
]

class DecompositionParameter(Parameter):
  def __init__(self, shape, n, w1=glorot_normal_init(), w2=glorot_normal_init(), properties=None, name=None):
    super(DecompositionParameter, self).__init__(shape=shape, properties=properties, name=name)

    shape1 = (shape[0], n) + shape[2:]
    shape2 = (n, shape[1]) + shape[2:]

    self.w1 = w1(
      shape=shape1,
      **self.properties,
      name=(name + '_w1') if name is not None else None
    )

    self.w2 = w2(
      shape=shape2,
      **self.properties,
      name=(name + '_w2') if name is not None else None
    )

  def get_output_for(self, w1, w2):
    return tf.tensordot(w1, w2, axes=[(1,), (0,)])

  def variables(self):
    return self.w1.variables() + self.w2.variables()

decomposition = parameter_model(DecompositionParameter)