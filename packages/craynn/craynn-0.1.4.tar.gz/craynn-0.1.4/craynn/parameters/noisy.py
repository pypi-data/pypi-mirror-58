import tensorflow as tf

from .meta import Parameter, parameter_model
from .common import default_weight_init

__all__ = [
  'NoisyParameter',
  'noisy'
]

class NoisyParameter(Parameter):
  def __init__(self, shape, eps=1e-3, w=default_weight_init, name=None, **properties):
    super(NoisyParameter, self).__init__(shape=shape, properties=properties, name=name)

    self.w = w(
      shape=shape,
      **properties,
      name=(name + '_w') if name is not None else None
    )
    self.eps = tf.constant(eps, dtype=tf.float32, shape=())

  def get_output_for(self, w):
    return w + tf.random.normal(shape=tf.shape(w), stddev=self.eps, dtype=w.dtype)

  def variables(self):
    return self.w.variables()

noisy = parameter_model(NoisyParameter)
