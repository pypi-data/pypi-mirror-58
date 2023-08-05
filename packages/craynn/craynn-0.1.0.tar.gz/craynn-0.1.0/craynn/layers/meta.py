from builtins import getattr

from ..meta import *

__all__ = [
  'Layer',
  'InputLayer',

  'FunctionalLayer',

  'custom_layer',

  'CompositeLayer',
  'composite',

  'propagate',
  'reduce_graph',
  'find_in_graph',

  'get_output',
  'get_all_outputs',

  'get_output_shape',
  'get_all_output_shapes',

  'get_parameters',
  'get_all_parameters',

  'get_variables',
  'get_all_variables',

  'get_layers',
  'get_inputs_layers',

  'model_selector',

  'model_from_class',
  'model_from',

  'modify_graph'
]


class Layer(object):
  def __init__(self, name=None):
    self.name = name

  def __str__(self):
    if not hasattr(self, 'name') or self.name is None:
      return self.__class__.__name__
    else:
      return self.name

  def __repr__(self):
    return str(self)

  def get_output_shape_for(self, *input_shapes, **kwargs):
    raise NotImplementedError

  def get_output_for(self, *args, **kwargs):
    raise NotImplementedError


class InputLayer(Layer):
  def __init__(self, shape, name=None):
    self.shape = shape

    super(InputLayer, self).__init__(name)

  def get_output_shape_for(self):
    return self.shape

  def get_output_for(self, *args, **kwargs):
    raise ValueError('Input was asked to return a value, this should not have happened.')


class FunctionalLayer(Layer):
  def __init__(self, *incoming, name=None):
    self.incoming = incoming
    super(FunctionalLayer, self).__init__(name)


class CustomLayer(FunctionalLayer):
  def __init__(self, f, shape_f, *incoming, name=None):
    super(CustomLayer, self).__init__(*incoming, name=name)
    self.f = f
    self.shape_f = shape_f

  def get_output_for(self, *args):
    return self.f(*args)

  def get_output_shape_for(self, *input_shapes):
    return self.shape_f(*input_shapes)

_default_shape_f = lambda *input_shapes: input_shapes[0]
custom_layer = lambda f, shape_f=_default_shape_f, name=None: lambda *incoming: CustomLayer(f, shape_f, *incoming, name=name)


class CompositeLayer(FunctionalLayer):
  def  __init__(self, *incoming, subnetwork, name=None):
    super(CompositeLayer, self).__init__(*incoming, name=name)

    self.subnetwork = subnetwork(*incoming)
    self.subnetwork_layers = get_subgraph(self.subnetwork, incoming)

    self.parameters = [
      param
      for layer in self.subnetwork_layers
      for param in getattr(layer, 'params', [])
    ]

  def get_output_for(self, *args, **kwargs):
    substitutes = dict(zip(self.incoming, args))
    return get_output(self.subnetwork, substitutes=substitutes, **kwargs)

  def get_output_shape_for(self, *input_shapes, **kwargs):
    substitutes = dict(zip(self.incoming, input_shapes))
    return get_output_shape(self.subnetwork, substitutes=substitutes, **kwargs)

composite = lambda subnetwork, name=None: lambda *incoming: CompositeLayer(*incoming, subnetwork=subnetwork, name=None)

def propagate(f, layers, substitutes=None):
  if substitutes is not None:
    known_results = dict(substitutes.items())
  else:
    known_results = dict()

  stack = list()
  stack.extend(layers)

  while len(stack) > 0:
    current_layer = stack.pop()

    if current_layer in known_results:
      continue

    incoming = getattr(current_layer, 'incoming', list())

    unknown_dependencies = [
      layer
      for layer in incoming
      if layer not in known_results
    ]

    if len(unknown_dependencies) == 0:
      known_results[current_layer] = f(
        current_layer,
        [ known_results[layer] for layer in incoming ]
      )

    else:
      stack.append(current_layer)
      stack.extend(unknown_dependencies)

  return known_results

def map_graph(f, layer_or_layers):
  """
  A wrapper over `propagate` for functions that does not depend on incoming values.
    Results are topologically ordered.

  :param f: `Layer -> value`
  :param layer_or_layers: layers (or a single layer) on which to compute `f` (including all dependencies).
  :return: topologically ordered outputs.
  """

  if isinstance(layer_or_layers, Layer):
    layers = [layer_or_layers]
  else:
    layers = layer_or_layers

  return list(propagate(
    f=lambda layer, *args: f(layer),
    layers=layers,
    substitutes=dict()
  ).values())

def reduce_graph(operator, strict=False):
  """
    Wraps operator into `propagate`-operator.

  :param operator: `Layer` -> function
  :param strict: if `False` use `apply_with_kwargs` wrapper on `operator` which filters key word arguments before passing
    them into propagated function; otherwise, passes `**kwargs` directly to the propagated function.
  :return: a getter, function `(list of layer, substitution dictionary=None, **kwargs) -> value`
    that computes the operator output for `layers`.
  """
  def getter(layers_or_layer, substitutes=None, **kwargs):
    from ..meta import apply_with_kwargs

    if isinstance(layers_or_layer, Layer):
      layers = [layers_or_layer]
    else:
      layers = layers_or_layer

    if substitutes is None:
      substitutes = dict()

    if strict:
      wrapped_operator = lambda layer, incoming: operator(layer)(*incoming, **kwargs)
    else:
      wrapped_operator = lambda layer, incoming: apply_with_kwargs(operator(layer), *incoming, **kwargs)

    results = propagate(wrapped_operator, layers, substitutes)

    if isinstance(layers_or_layer, Layer):
      return results[layers_or_layer]
    else:
      return [results[layer] for layer in layers]

  return getter

def find_in_graph(predicate, layers):
  visited = set()
  stack = list(layers)

  while len(stack) > 0:
    current = stack.pop()
    if current in visited:
      continue

    if predicate(current):
      return current

    incoming = getattr(current, 'incoming', list())
    stack.extend(incoming)

  return None

def modify_graph(f, layers):
  """
  This function dynamically changes graph with outputs `layers` by propagating operator `f`
  from outputs to the inputs. Operator `f` receives a layer and must output tuple `(layer replacement, subgraph)`,
  where:
    - layer_replacement: must be either:
      - None: to remove current layer from the graph;
      - a `craynn.layers.meta.FunctionalLayer` instance: to replace current layer with, the instance will be copied and have incoming overridden;
      - a layer model: a replacement for the current layer.
    - subgraph: list of layers for further propagation. Must be a subset of incoming layers of the original layer.

  This function allows, for example, to prune graph.

  *Note*: this function might make shallow copies of the layers and override `incoming` value.
    Inappropriate operator may result in invalid graph. For example, removing second convolution from
    `conv(8) -> conv(16) -> conv(32)` will leave the last convolution mismatched kernel.

  *Note*: inputs layers are never copied.
  """

  import copy

  def propagate_operator(layer):
    replacement, subgraph = f(layer)

    subgraph_replacement = [
      layer
      for incoming in subgraph
      for layer in propagate_operator(incoming)
    ]

    if replacement is None:
      return [
        layer
        for sg in subgraph_replacement
        for layer in propagate_operator(sg)
      ]
    elif callable(replacement):
      replacement = replacement(*subgraph_replacement)
      return [ replacement ]
    elif isinstance(replacement, Layer):
      if hasattr(replacement, 'incoming'):
        replacement = copy.copy(replacement)
        replacement.incoming = tuple(subgraph_replacement)
      else:
        replacement = replacement

      return [ replacement ]
    else:
      raise ValueError('operator return value is not understood: %s.' % replacement)


  return [ output for layer in layers for output in propagate_operator(layer) ]

def layer_output(layer, *inputs, **modes):
  param_values = [
    param() for param in getattr(layer, 'parameters', [])
  ]

  return apply_with_kwargs(layer.get_output_for, *param_values, *inputs, **modes)


get_output = reduce_graph(lambda layer: lambda *inputs, **modes: layer_output(layer, *inputs, **modes), strict=True)

def get_all_outputs(layer_or_layers, substitutes, **modes):
  operator = lambda layer, inputs: layer_output(layer, *inputs, **modes)

  if isinstance(layer_or_layers, Layer):
    layers = [layer_or_layers]
  else:
    layers = layer_or_layers

  return propagate(operator, layers, substitutes)

get_output_shape = reduce_graph(lambda layer: layer.get_output_shape_for, strict=False)

get_all_output_shapes = lambda layers, substitutes=None, **kwargs: propagate(
  lambda layer, args: apply_with_kwargs(layer.get_output_shape_for, *args, **kwargs),
  layers, substitutes=substitutes
)

get_layers = lambda layers_or_layer: map_graph(lambda layer: layer, layers_or_layer)

get_inputs_layers = lambda layers_or_layer: [
  layer
  for layer in get_layers(layers_or_layer)
  if len(getattr(layer, 'incoming', [])) == 0
]

def get_subgraph(layer_or_layers, origins):
  if isinstance(layer_or_layers, Layer):
    layers = [layer_or_layers]
  else:
    layers = layer_or_layers


  return [
    layer

    for layer, is_origin in propagate(
      lambda layer, *args, **kwargs: False,
      layers, substitutes=dict([
        (origin, True) for origin in origins
      ])
    ).items()

    if not is_origin
  ]

def get_parameters(layer: Layer, **properties):
  """
  Get parameters that satisfy all `properties`.
  A parameter satisfies a property `prop = value` if:
    - value is None;
    - the parameter has property `prop` and its value equals to `value` or
    - the parameter lacks property `prop` and `value = False`.

  Note, that `prop = None` matches all parameters, this is done to
  place commonly used properties to default arguments and enable autocomplete for them.

  Parameters
  ----------
  layer layer parameters of which are considered.
  properties list of properties

  Returns
  -------
  list of parameters
  """
  parameters = getattr(layer, 'parameters', [])
  check_props = lambda param: all([
    (param.properties.get(k, False) == v) or (v is None)
    for k, v in properties.items()
  ])

  return [
    param
    for param in parameters
    if check_props(param)
  ]

def get_all_parameters(layer_or_layers, **properties):
  collected_params = map_graph(lambda layer: get_parameters(layer, **properties), layer_or_layers)
  return [ param for params in collected_params for param in params ]

def get_variables(layer: FunctionalLayer, **properties):
  """
  Collects all free variables from parameters with `properties` (see `get_params` for details).

  Returns
  -------
  list of free variables
  """

  return [
    variable
    for param in get_parameters(layer, **properties)
    for variable in param.variables()
  ]

def get_all_variables(layer_or_layers, **properties):
  collected_variables = map_graph(lambda layer: get_variables(layer, **properties), layer_or_layers)
  return [ param for params in collected_variables for param in params ]


def model_selector(criterion):
  """Decorator, changes signature and inserts checks into a layer model selector.

  This is a wrapper which inserts a common procedures for a selector:
  - signature checks for each model (must all be the same);
  - binding of model parameters;
  - replacement of selector signature by models' shared signature.

  Model selector is a meta layer model that selects a particular layer model from a provided list
  based on properties of incoming layer, i.e. defers selection of a model until network construction.

  Type of the selector: `list of models` -> `incoming layer` -> `layer`.

  Parameters
  ----------
  criterion : Selector
    selector to modify. This function can assume that models have the same signature (i.e. accept the same parameters).

  Returns
  -------
  Selector
    Selector with changed signature and validity checks.

  Examples
  -------
  Selecting model with proper dimensionality for convolutional layer
  based on dimensionality of the incoming layer:

  >>> @model_selector
  >>> def dimensionality_selector(models):
  >>>   def common_model(incoming):
  >>>     ndim = get_output_shape(incoming) - 2
  >>>     return models[ndim]
  >>>   return common_model
  """
  from inspect import signature

  def selector(models):
    assert len(models) > 0
    models_signatures = [
      signature(model) for model in models
      if model is not None
    ]

    if len(set(models_signatures)) != 1:
      pretty_signatures = '\n  '.join([ str(signature) for signature in set(models_signatures)])
      raise ValueError('All models must have the same signature, got:%s' % pretty_signatures)

    common_signature = models_signatures[0]

    bound_criterion = criterion(models)

    def common_model(*args, **kwargs):
      common_signature.bind(*args, **kwargs)

      def model(incoming):
        selected_model = bound_criterion(incoming)
        if selected_model is None:
          raise ValueError('Invalid incoming layer!')

        layer = selected_model(*args, **kwargs)(incoming)
        return layer

      return model

    common_model.__signature__ = common_signature
    return common_model

  return selector

def model_from_class(clazz, fixed, defaults):
  import inspect
  signature = inspect.signature(clazz)

  if 'incoming' in signature.parameters.keys():
    return carry(clazz, fixed, defaults, carried_arguments=['incoming'])
  elif 'incomings' in signature.parameters.keys():
    return carry(clazz, fixed, defaults, carried_arguments=['incomings'])

def model_from(clazz):
  import inspect
  signature = inspect.signature(clazz)

  if 'incoming' in signature.parameters.keys():
    return CarringExpression(clazz, carried=['incoming'])
  elif 'incomings' in signature.parameters.keys():
    return CarringExpression(clazz, carried=['incomings'])
  else:
    return CarringExpression(clazz, carried=[])
