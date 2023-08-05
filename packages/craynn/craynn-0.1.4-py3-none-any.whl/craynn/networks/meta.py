import tensorflow as tf

from .. import layers
from ..subnetworks import achain

from .network_utils import *

__all__ = [
  'Network', 'network',
  'modify_network'
]

class Network(object):
  def __init__(self, inputs, outputs, **modes):
    self.inputs = inputs
    self.outputs = outputs
    self.modes = modes

    try:
      self.__call__.__signature__ = get_signature(inputs)
    except:
      pass

    named_layers = dict()
    for layer in self.layers():
      if layer.name is None:
        continue

      if layer.name not in named_layers:
        named_layers[layer.name] = layer
      else:
        if isinstance(layer, layers.InputLayer) and isinstance(named_layers[layer.name], layers.InputLayer):
          raise Exception('Collision in input names: %s' % layer.name)

    self._named_layers = named_layers

    self._mode_cache = dict()

  def subnet(self, inputs=None, outputs=None):
    if inputs is None:
      inputs = self.inputs
    else:
      inputs = [
        input if isinstance(input, layers.Layer) else self._named_layers[input]
        for input in inputs
      ]

    if outputs is None:
      outputs = self.outputs
    else:
      outputs = [
        output if isinstance(output, layers.Layer) else self._named_layers[output]
        for output in outputs
      ]

    return Network(inputs, outputs)

  def _as_subnet(self, *incoming):
    from ..subnetworks import subnetwork
    return subnetwork(self.inputs, self.outputs)(*incoming)

  def _map_inputs(self, args, kwargs):
    substitutes = dict(zip(self.inputs, args))

    for name, value in kwargs.items():
      if name in self._named_layers:
        layer = self._named_layers[name]
      else:
        raise Exception('There is no layer with name %s' % (name,))

      if layer in substitutes:
        raise Exception('Value for layer %s is provided twice, via a positional and a keyword arguments' % (name,))

      substitutes[layer] = value

    return substitutes

  @tf.function(autograph=False)
  def __call__(self, *args, **kwargs):
    is_arg_layer = [isinstance(arg, layers.Layer) for arg in args]

    if all(is_arg_layer) and len(is_arg_layer) > 0:
      if len(kwargs) != 0:
        raise Exception('Network as a SubnetworkLayer does not accept kwargs')
      return self._as_subnet(*args)

    if any(is_arg_layer) or any([ isinstance(arg, layers.Layer) for arg in kwargs.values() ]):
      raise NotImplementedError('Network can not be called on a mixture of layers and tensors yet.')

    substitutes = self._map_inputs(args, kwargs)

    try:
      return layers.get_output(self.outputs, substitutes=substitutes, **self.modes)

    except Exception as e:
      inputs_wo_substitute = [
        layer
        for layer in self.inputs
        if layer not in substitutes
      ]

      if len(inputs_wo_substitute) > 0:
        raise ValueError('Not all inputs were provided value, this might be the cause of the error.') from e
      else:
        raise


  def mode(self, **modes):
    if len(modes) == 0:
      return self

    new_modes = self.modes.copy()
    for k, v in modes.items():
      new_modes[k] = v

    mode_key = tuple(new_modes.items())
    if mode_key not in self._mode_cache:
      self._mode_cache[mode_key] = Network(self.inputs, self.outputs, **new_modes)

    self._mode_cache[mode_key]._mode_cache = self._mode_cache

    return self._mode_cache[mode_key]


  def reset(self):
    return [
      param.reset()
      for param in self.parameters()
    ]

  def parameters(self, **properties):
    return layers.get_all_parameters(self.outputs, **properties)

  def variables(self, trainable=None, **properties):
    return layers.get_all_variables(self.outputs, trainable=trainable, **properties)

  def assign(self, variable_values):
    for var, value in zip(self.variables(), variable_values):
      var.assign(value)

  def description(self, short=True, **attributes):
    from ..layers.inspect import graph_description
    return graph_description(self.outputs, short=short, inputs=self.inputs, **attributes)

  def __str__(self):
    return self.description(short=True)

  def __repr__(self):
    return self.description(short=True)

  def total_number_of_parameters(self, **properties):
    from ..layers.inspect import get_total_number_of_parameters
    return get_total_number_of_parameters(self.outputs, **properties)

  def layers(self):
    return layers.get_layers(self.outputs)

  def input_shapes(self):
    return layers.get_output_shape(self.inputs)

  def output_shapes(self):
    return layers.get_output_shape(self.outputs)

  def reg_l2(self, weights=True, **properties):
    from ..regularization import reg_l2
    reg = reg_l2()
    return sum([
      reg(param)
      for param in self.parameters(weights=weights, **properties)
    ])


def __is_shape(shape_or_layer):
  return hasattr(shape_or_layer, '__iter__') and all([ (type(s) is int or s is None) for s in shape_or_layer ])

def _get_input_layer(shape_or_layer, name=None, index=None):
  if __is_shape(shape_or_layer) :
    shape = shape_or_layer

    if name is not None:
      return layers.InputLayer(shape=shape, name=name)
    elif index is not None:
      return layers.InputLayer(shape=shape, name='input%d' % index)
    else:
      return layers.InputLayer(shape=shape, name='input')

  elif isinstance(shape_or_layer, layers.Layer):
    return shape_or_layer


def _make_network(factory, inputs, named_inputs):
  input_layers = []

  for i, input in enumerate(inputs):
    input_layers.append(_get_input_layer(input, name=None, index=i))

  for i, (name, input) in enumerate(named_inputs.items()):
    input_layers.append(_get_input_layer(input, name=name, index=i))

  explicit_names = [ layer.name for layer in input_layers if layer.name is not None ]
  assert len(set(explicit_names)) == len(explicit_names)

  outputs = factory(*input_layers)

  if isinstance(outputs, layers.Layer):
    outputs = [outputs]

  return Network(input_layers, outputs)


network = lambda *inputs, **named_inputs: lambda *factory: \
  _make_network(achain(*factory), inputs, named_inputs)

network.__doc__ = \
"""
Allows nice syntax:
```
  net(session)(input1, input2, ..., named_input=)(
    constructor
  )
```

or

```
  net(session)(input)(
    constructor
  )
```

for single input.
"""

def modify_network(operator, nn : Network):
  """
  Performs `craynn.layers.meta.modify_graph` of network's graph...
  See `craynn.layers.meta.modify_graph` documentation for details.
  :param operator: modification operator.
  :param nn: an instance of Network.
  :return: modified network.
  """
  modified = layers.modify_graph(operator, nn.outputs)
  return nn.__class__(nn.inputs, modified, *nn._args, **nn._kwargs)