__all__ = [
  'chain', 'achain', 'repeat',
  'subnetwork'
]

def flatten(l):
  if isinstance(l, list):
    return [ flatten(x) for x in l ]
  else:
    return l

def _chain(incoming, definition):
  net = incoming

  for layer in definition:
    if hasattr(layer, '__iter__'):
      net = _chain(net, layer)
    elif layer is None:
      pass
    else:
      net = layer(net)

  return net

chain = lambda *definition: lambda incoming: _chain(incoming, definition)

def _achain(incoming, definition):
  net = incoming

  if not isinstance(net, tuple) and not isinstance(net, list):
    net = [net]

  if not hasattr(definition, '__iter__'):
    try:
      net = definition(*net)
    except Exception as e:
      raise Exception('An error occurred while try to apply %s to %s' % (definition, net)) from e
  elif isinstance(definition, list):
    results = []
    for op in definition:
      try:
        result = _achain(net, op)
      except Exception as e:
        raise Exception('An error occurred while try to apply %s to %s' % (op, net)) from e

      if isinstance(result, tuple) or isinstance(result, list):
        results.extend(result)
      else:
        results.append(result)

    net = results

  elif isinstance(definition, tuple):
    for op in definition:
      try:
        net = _achain(net, op)
      except Exception as e:
        raise Exception('An error occurred while try to apply %s to %s' % (op, net)) from e
  else:
    raise RuntimeError('Unknown chain definition: %s' % (definition, ))

  return net

achain = lambda *definition: lambda *incoming: _achain(incoming, definition)

repeat = lambda n: lambda *definition: achain(
  (achain(*definition), ) * n
)

def subnetwork(inputs, outputs):
  """
  Applies existing graph substituting inputs by a new set of incoming layers.
  This procedure make shallow copies of layers, thus all parameters are shared.
  """
  from ..layers.meta import propagate
  from copy import copy

  def model(*incoming):
    assert len(incoming) == len(inputs), 'wrong number of incoming layers'

    substitutes = dict(zip(inputs, incoming))
    def mutator(layer, layer_incoming):
      new_layer = copy(layer)

      if hasattr(new_layer, 'incoming'):
        new_layer.incoming = layer_incoming

      return new_layer

    mutated = propagate(mutator, outputs, substitutes=substitutes)
    return [ mutated[output] for output in outputs ]

  return model
