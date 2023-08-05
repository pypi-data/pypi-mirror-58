import numpy as np
import tensorflow as tf

from ..meta import derive
from .meta import FunctionalLayer, model_from, get_output_shape

__all__ = [
  'NoiseLayer', 'noise',
  'GaussianNoiseLayer', 'gaussian_noise',

  'GaussianRandomVariableLayer', 'gaussian_rv',
  'DropoutLayer', 'dropout'
]

class NoiseLayer(FunctionalLayer):
  def __init__(self, incoming, noise_op, std=1.0e-3, name=None):
    super(NoiseLayer, self).__init__(incoming, name=name)

    self.noise_op = noise_op
    self.std = std

  def get_output_for(self, input, deterministic=False):
    if deterministic:
      return input
    else:
      return input + self.noise_op(shape=tf.shape(input), dtype=input.dtype) * self.std

  def get_output_shape_for(self, input_shape):
    return input_shape


noise = model_from(NoiseLayer)()

GaussianNoiseLayer = derive('GaussianNoiseLayer').based_on(NoiseLayer).with_fixed(noise_op=tf.random.normal)
gaussian_noise = model_from(GaussianNoiseLayer)()

class DropoutLayer(FunctionalLayer):
  def __init__(self, incoming, p=0.2, name=None):
    super(DropoutLayer, self).__init__(incoming, name=name)
    self.p = p

  def get_output_for(self, input, deterministic=False):
    if deterministic:
      return input
    else:
      return tf.nn.dropout(input, rate=self.p, noise_shape=None, name=self.name)

  def get_output_shape_for(self, input_shape):
    return input_shape

dropout = model_from(DropoutLayer)()

class GaussianRandomVariableLayer(FunctionalLayer):
  def __init__(self, *incoming, name=None):
    assert len(incoming) == 2

    super(GaussianRandomVariableLayer, self).__init__(*incoming, name=name)

  def get_output_for(self, *inputs, deterministic=False):
    if deterministic:
      return inputs[0]
    else:
      mean, std = inputs
      u = tf.random.normal(shape=mean.shape, dtype=mean.dtype)
      return u * std + mean

  def get_output_shape_for(self, *input_shapes):
    return input_shapes[0]

gaussian_rv = model_from(GaussianRandomVariableLayer)()

