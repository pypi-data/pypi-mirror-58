import tensorflow as tf

from .meta import *

from ..parameters import zeros_init

__all__ = [
  'SoftmaxGate',
  'softmax_gate'
]

class SoftmaxGate(FunctionalLayer):
  def __init__(self, *incoming, w=zeros_init(), name=None):
    super(SoftmaxGate, self).__init__(*incoming, name=name)

    self.parameters = [
      w(shape=(len(incoming),), weights=True, trainable=True, name='w')
    ]

  def get_output_for(self, w, *inputs):
    stacked = tf.stack(inputs, axis=1)
    dim_def = [None, Ellipsis] + [None] * (len(inputs[0].shape) - 1)
    coefs = tf.nn.softmax(w)

    return tf.reduce_sum(stacked * coefs[dim_def], axis=1)

  def get_output_shape_for(self, *input_shapes):
    return input_shapes[0]

softmax_gate = model_from(SoftmaxGate)()