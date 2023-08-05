from inspect import *

__all__ = [
  'get_signature',
  'save_parameters', 'set_parameters', 'load_parameters',
  'eval_network', 'NetworkMode'
]

class NetworkMode(object):
  def __init__(self, nn, modes):
    self.nn = nn
    self.modes = modes

  def __call__(self, *args, **kwargs):
    return self.nn.mode_call(args, kwargs, **self.modes)

  def mode(self, **modes):
    modes.update(self.modes)
    return NetworkMode(self.nn, modes)

def get_signature(inputs):
  return Signature(
    parameters=[
      Parameter(name=input.name, kind=Parameter.POSITIONAL_OR_KEYWORD)
      for input in inputs
    ]
  )

def set_parameters(session, nn, values : list):
  import tensorflow as tf
  vars = nn.variables()

  session.run(tf.group([
    tf.assign(var, value)
    for var, value in zip(vars, values)
  ]))

def load_parameters(session, nn, path : str):
  import pickle

  with open(path, 'rb') as f:
    values = pickle.load(f)

  return set_parameters(session, nn, values)

def save_parameters(session, nn, path : str):
  import pickle

  vars = nn.variables()
  values = session.run(vars)

  with open(path, 'wb') as f:
    pickle.dump(values, f)


def eval_network_fixed_batch(session, graph, outputs, substitutes, batch_size=1):
  from ..utils import traverse

  tensor_substitutes = dict([
    (graph[layer], value)
    for layer, value in substitutes.items()
  ])

  tensor_outputs = [
    graph[layer] for layer in outputs
  ]

  return traverse(session, tensor_outputs, tensor_substitutes.values(), tensor_substitutes.keys(), batch_size=batch_size)


def eval_network(session, graph, outputs, substitutes, batch_size=1):
  return eval_network_fixed_batch(session, graph, outputs, substitutes, batch_size=batch_size)
