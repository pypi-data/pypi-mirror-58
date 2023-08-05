import numpy as np
import tensorflow as tf

from .. import layers
from ..parameters import FreeParameter

__all__ = [
  'normalize_weights'
]


def normalize_weights(network, batch_f, weights=True, biases=True):
  """
  WARNING: this procedure assumes that output of each layer is sublinear with respect to its inputs, i.e.:
  `f(x, scale * W, b) <= scale * f(x, W, b)`
  and
  `f(x, W, b + offset) <= f(x, W, b) + offset`

  While this assumption is satisfied for the most of the commonly used layers, care should be taken.
  """
  for layer in network.layers():
    if weights:
      weight_parameters = layers.get_parameters(layer, weights=True)
    else:
      weight_parameters = []

    if biases:
      bias_parameters = layers.get_parameters(layer, biases=True)
    else:
      bias_parameters = []

    W_vars = [
      var
      for weight in weight_parameters
      if isinstance(weight, FreeParameter)

      for var in weight.variables()
    ]

    b_vars = [
      var
      for bias in bias_parameters
      if isinstance(bias, FreeParameter)

      for var in bias.variables()
    ]

    if len(b_vars) > 0:
      output = layers.get_output(layer, substitutes=dict(zip(network.inputs, batch_f())))
      mean = np.mean(output)

      offset = mean / len(b_vars)

      for var in b_vars:
        var.assign(var - offset)

    if len(W_vars) > 0:
      output = layers.get_output(layer, substitutes=dict(zip(network.inputs, batch_f())))
      std = np.std(output)

      scale = np.power(1 / std, 1 / len(W_vars))

      for var in W_vars:
        var.assign(var * scale)

def __normalize_output(
  network, batch_f, optimizer=None,
  n_iters=16 * 1024,
  target_mean=0.0, target_variance=1.0,
  strategy=None
):
  augmented_parameters = {
    layer : [
      strategy(param)
      for param in layers.get_parameters(layer)
    ]
    for layer in network.layers()
  }

  augments = [
    augments()
    for layer in augmented_parameters
    for param in augmented_parameters[layer]
    for augments in param.get_augments()
  ]

  def layer_output(layer, *inputs, **modes):
    param_values = [
      param()
      for param in augmented_parameters[layer]
    ]

    return apply_with_kwargs(layer.get_output_for, *param_values, *inputs, **modes)

  get_output = layers.reduce_graph(lambda layer: lambda *inputs, **modes: layer_output(layer, *inputs, **modes), strict=True)

  @tf.function(autograph=False)
  def call():
    args = batch_f()
    result, = get_output(network.outputs, substitutes=dict(zip(network.inputs, args)))
    return result

  @tf.function
  def target():
    result = call()
    mean = tf.reduce_mean(result)
    variance = tf.reduce_mean((result - mean) ** 2)

    return (mean - target_mean) ** 2 + (variance - target_variance) ** 2

  opt = optimizer(target, augments)

  for _ in range(n_iters):
    opt()

  for layer in augmented_parameters:
    for param in augmented_parameters[layer]:
      param.apply()





