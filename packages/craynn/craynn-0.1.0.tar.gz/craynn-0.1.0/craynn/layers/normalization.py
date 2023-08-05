### inspired by
### https://github.com/Lasagne/Lasagne/blob/master/lasagne/layers/normalization.py#L124-L326

import tensorflow as tf

from ..nonlinearities import linear
from .meta import FunctionalLayer, get_output_shape, model_from
from ..parameters import zeros_init, ones_init, const_init

__all__ = [
  'BatchNormLayer',
  'batch_norm',

  'LayerNormLayer',
  'layer_norm',

  'RollingNormalizationLayer',
  'rolling_normalization',

  'NormalizationLayer',
  'norm'
]

class BatchNormLayer(FunctionalLayer):
  def __init__(self, incoming, gamma=ones_init(), beta=zeros_init(),
               axes=(0, ), activation=linear(), epsilon=1.0e-4, name=None):
    self.epsilon = tf.constant(epsilon, dtype='float32')

    incoming_shape = get_output_shape(incoming)
    if axes == 'auto':
      axes = list(range(len(incoming_shape) - 1))
    self.axes = axes

    self.parameter_shape = tuple([
      d
      for i, d in enumerate(incoming_shape)
      if i not in self.axes
    ])

    self.broadcast = tuple([
      (None if i in axes else slice(None, None, None)) for i, _ in enumerate(incoming_shape)
    ])

    self.parameters = []

    if gamma is not None:
      self.parameters.append(
        gamma(self.parameter_shape, weights=True, normalization_scales=True, trainable=True)
      )

    if beta is not None:
      self.parameters.append(
        beta(self.parameter_shape, biases=True, normalization_biases=True, trainable=True)
      )

    self.scale = gamma is not None
    self.bias = beta is not None

    self.activation = activation

    super(BatchNormLayer, self).__init__(incoming, name=name)

  def get_output_for(self, *args):
    input = args[-1]

    if self.scale:
      gamma = args[0]
    else:
      gamma = None

    if self.bias:
      beta = args[1] if self.scale else args[0]
    else:
      beta = None

    input_mean = tf.reduce_mean(input, axis=self.axes)
    input_var = tf.reduce_mean((input - input_mean[self.broadcast]) ** 2, axis=self.axes)
    input_inverse_std = 1 / tf.sqrt(input_var + self.epsilon)

    y = (input - input_mean[self.broadcast]) * input_inverse_std[self.broadcast]

    scaled = y if gamma is None else y * gamma[self.broadcast]
    biased = scaled if beta is None else scaled + beta[self.broadcast]

    return self.activation(biased)

  def get_output_shape_for(self, input_shape):
    return input_shape

batch_norm = model_from(BatchNormLayer)()


class LayerNormLayer(FunctionalLayer):
  def __init__(self, incoming, axes='auto', epsilon=1.0e-4, name=None):
    self.epsilon = tf.constant(epsilon, dtype='float32')

    incoming_shape = get_output_shape(incoming)
    if axes == 'auto':
      axes = tuple(range(1, len(incoming_shape) - 1))

    self.axes = axes

    self.broadcast = tuple([
      (tf.newaxis if i in axes else slice(None, None, None)) for i, _ in enumerate(incoming_shape)
    ])

    super(LayerNormLayer, self).__init__(incoming, name=name)

  def get_output_for(self, input):
    input_mean = tf.reduce_mean(input, axis=self.axes)
    input_var = tf.reduce_mean((input - input_mean[self.broadcast]) ** 2, axis=self.axes)
    input_inverse_std = 1 / tf.sqrt(input_var + self.epsilon)

    return (input - input_mean[self.broadcast]) * input_inverse_std[self.broadcast]

  def get_output_shape_for(self, input_shape):
    return input_shape


layer_norm = model_from(LayerNormLayer)()

class RollingNormalizationLayer(FunctionalLayer):
  def __init__(self, incoming, gamma=ones_init(), beta=zeros_init(),
               axes=(0,), rho=0.99, epsilon=1e-2, name=None):
    self.epsilon = tf.constant(epsilon, dtype='float32')
    self.rho = tf.constant(rho, dtype='float32')
    self.crho = tf.constant(1 - rho, dtype='float32')

    incoming_shape = get_output_shape(incoming)
    if axes == 'auto':
      axes = list(range(len(incoming_shape) - 1))
    self.axes = axes

    self.parameter_shape = tuple([
      d
      for i, d in enumerate(incoming_shape)
      if i not in self.axes
    ])

    self.broadcast = tuple([
      (None if i in axes else slice(None, None, None)) for i, _ in enumerate(incoming_shape)
    ])

    self.parameters = [
      gamma(self.parameter_shape, weights=True, normalization_scales=True, trainable=False),
      beta(self.parameter_shape, biases=True, normalization_biases=True, trainable=False)
    ]

    super(RollingNormalizationLayer, self).__init__(incoming, name=name)

  def get_output_for(self, gamma, beta, input, deterministic=False, normalization=True):
    if not deterministic and normalization:
      input_mean = tf.reduce_mean(input, axis=self.axes)
      beta.assign(
        self.rho * beta + self.crho * input_mean
      )

      input_var = tf.reduce_mean((input - input_mean[self.broadcast]) ** 2, axis=self.axes)
      input_inverse_std = 1 / tf.sqrt(input_var + self.epsilon)

      gamma.assign(
        self.rho * gamma + self.crho * input_inverse_std
      )

    return input * gamma[self.broadcast] + beta[self.broadcast]

  def get_output_shape_for(self, input_shape):
    return input_shape

rolling_normalization = model_from(RollingNormalizationLayer)()


class NormalizationLayer(FunctionalLayer):
  def __init__(self, incoming, gamma=const_init(value=0.5), beta=zeros_init(),
               axes=(0,), name=None):

    incoming_shape = get_output_shape(incoming)
    if axes == 'auto':
      axes = list(range(len(incoming_shape) - 1))
    self.axes = axes

    self.parameter_shape = tuple([
      d
      for i, d in enumerate(incoming_shape)
      if i not in self.axes
    ])

    self.broadcast = tuple([
      (None if i in axes else slice(None, None, None)) for i, _ in enumerate(incoming_shape)
    ])

    self.parameters = [
      gamma(self.parameter_shape, weights=True, normalization_scales=True, trainable=True),
      beta(self.parameter_shape, biases=True, normalization_biases=True, trainable=True)
    ]

    super(NormalizationLayer, self).__init__(incoming, name=name)

  def get_output_for(self, gamma, beta, input):
    return input * tf.nn.softplus(gamma)[self.broadcast] + beta[self.broadcast]

  def get_output_shape_for(self, input_shape):
    return input_shape

norm = model_from(NormalizationLayer)()