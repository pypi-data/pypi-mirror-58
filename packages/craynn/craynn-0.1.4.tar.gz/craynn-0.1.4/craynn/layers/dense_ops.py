import tensorflow as tf

from ..parameters import default_weight_init, default_bias_init

from .meta import FunctionalLayer, get_output_shape, model_from
from ..nonlinearities import default_semibounded_nonlinearity


__all__ = [
  'DenseLayer',
  'dense',

  'TensorDenseLayer',
  'tensor_dense',

  'BatchDenseLayer',
  'batch_dense',
]

class DenseLayer(FunctionalLayer):
  def __init__(self, incoming, num_units,
               activation=default_semibounded_nonlinearity,
               W=default_weight_init,
               b=default_bias_init,
               name=None):
    super(DenseLayer, self).__init__(incoming, name=name)
    input_shape = get_output_shape(incoming)
    self.num_units = num_units

    if len(input_shape) != 2:
      raise ValueError('Dense layer accepts only 2D tensors got [%s]!' % input_shape)

    self.parameters = [
      W(shape=(input_shape[1], num_units), name='W', weights=True, trainable=True),
      b(shape=(num_units,), name='b', biases=True, trainable=True)
    ]

    self.activation = activation

  def get_output_for(self, W, b, input):
    return self.activation(
      tf.matmul(input, W) + b[None, :]
    )

  def get_output_shape_for(self, input_shape):
    if len(input_shape) != 2:
      raise ValueError('Dense layer accepts only 2D tensors!')

    return (input_shape[0], self.num_units)


dense = model_from(DenseLayer).with_fixed().with_defaults()()

class TensorDenseLayer(FunctionalLayer):
  def __init__(self, incoming, num_units,
               activation=default_semibounded_nonlinearity,
               W=default_weight_init,
               b=default_bias_init,
               axis=-1,
               name=None):
    super(TensorDenseLayer, self).__init__(incoming, name=name)
    input_shape = get_output_shape(incoming)
    self.num_units = num_units

    self.axis = (len(input_shape) + axis) % len(input_shape)

    self.parameters = [
      W(shape=(input_shape[self.axis], num_units), name='W', weights=True, trainable=True),
      b(shape=(num_units,), name='b', biases=True, trainable=True)
    ]

    self.b_broadcast = [ (None if i != self.axis else slice(None, None, None)) for i in range(len(input_shape)) ]

    self.activation = activation

  def get_output_for(self, W, b, input):
    return self.activation(
      tf.tensordot(input, W, axes=[(self.axis, ), (0, )]) + b[self.b_broadcast]
    )

  def get_output_shape_for(self, input_shape):
    return tuple([
      (input_shape[i] if i != self.axis else self.num_units)
      for i in range(len(input_shape))
    ])


tensor_dense = model_from(TensorDenseLayer).with_fixed().with_defaults()()


class BatchDenseLayer(FunctionalLayer):
  def __init__(self, incoming, num_units, num_batches,
               activation=default_semibounded_nonlinearity,
               W=default_weight_init,
               b=default_bias_init,
               axis=-1,
               name=None):
    super(BatchDenseLayer, self).__init__(incoming, name=name)
    input_shape = get_output_shape(incoming)
    self.num_batches = num_batches
    self.num_units = num_units

    self.axis = (len(input_shape) + axis) % len(input_shape)

    self.parameters = [
      W(shape=(input_shape[self.axis], num_batches, num_units), name='W', weights=True, trainable=True),
      b(shape=(num_batches, num_units,), name='b', biases=True, trainable=True)
    ]

    self.b_broadcast = tuple([None] * (len(input_shape) - 1) + [slice(None, None, None)] * 2)

    self.activation = activation

  def get_output_for(self, W, b, input):
    return self.activation(
      tf.tensordot(input, W, axes=[(self.axis, ), (0, )]) + b[self.b_broadcast]
    )

  def get_output_shape_for(self, input_shape):
    return tuple([
      input_shape[i]
      for i in range(len(input_shape))
      if i != self.axis
    ]) + (self.num_batches, self.num_units)


batch_dense = model_from(BatchDenseLayer).with_fixed().with_defaults()()