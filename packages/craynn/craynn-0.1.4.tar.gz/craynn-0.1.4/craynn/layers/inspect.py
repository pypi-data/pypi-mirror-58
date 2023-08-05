from .meta import *

import numpy as np


__all__ = [
  'get_number_of_parameters',
  'get_total_number_of_parameters',
  'graph_description'
]

def get_number_of_parameters(layer, **properties):
  params = get_parameters(layer, **properties)
  shapes = [ tuple(param().shape.as_list()) for param in params ]
  nums_weights = [ np.prod(shape, dtype='int64') for shape in shapes ]

  return sum(nums_weights)

def get_total_number_of_parameters(layer_or_layers, **properties):
  layers = get_layers(layer_or_layers)

  return sum([
    get_number_of_parameters(layer, **properties)
    for layer in layers
  ])

def get_attributes(layer, attributes):
  values = dict()

  for name, attr in attributes.items():
    if type(attr) is str:
      if hasattr(layer, attr):
        values[name] = getattr(layer, attr)
    elif callable(attr):
      values[name] = attr(layer)

  return values

def param_description(param):
  return '{name} {shape}: {properties}'.format(
    name=param.name if param.name is not None else param.__class__.__name__,
    shape=tuple(param().shape.as_list()),
    properties=', '.join(['%s=%s' % (k, v) for k, v in param.properties.items()])
  )

def layer_description(layer, output_shape, attributes, short=True):
  attrs = get_attributes(layer, attributes)
  additional = [ '%s=%s' % (k, v) for k, v in attrs.items() ]

  if short:
    return '{name}{clazz} ({nparams} params): {out_shape}{additional}'.format(
      name='' if layer.name is None else ('%s ' % layer.name),
      clazz=layer.__class__.__name__,
      out_shape=output_shape,
      nparams=get_number_of_parameters(layer),
      additional='' if len(additional) == 0 else ('\n  %s' % ', '.join(additional))
    )
  else:
    head = '{name}{clazz}: {out_shape}{additional}'.format(
      name='' if layer.name is None else ('%s ' % layer.name),
      clazz=layer.__class__.__name__,
      out_shape=output_shape,
      additional='' if len(additional) == 0 else ('\n  %s' % '\n  '.join(additional))
    )

    params = get_parameters(layer)
    if len(params) == 0:
      return head
    else:
      params_info ='\n  '.join([ param_description(param) for param in params ])

      total_number_of_params = 'number of params: %s' % get_number_of_parameters(layer)

      return '{head}\n  {params}\n  {total}'.format(
        head=head,
        params=params_info,
        total=total_number_of_params
      )

def graph_description(layer_or_layers, short=True, inputs=None, **attributes):
  all_layers = get_layers(layer_or_layers)

  if inputs is None:
    inputs = [
      layer for layer in all_layers
      if not hasattr(layer, 'incoming')
    ]

  outputs = layer_or_layers

  shapes = get_all_output_shapes(layer_or_layers)

  input_summary = ', '.join([
    ('%s' % shapes[layer]) if layer.name is None else ('%s: %s' % (layer.name, shapes[layer]))
    for layer in inputs
  ])

  output_summary = ', '.join([
    '{shape}'.format(shape=shapes[layer])
    for layer in outputs
  ])

  layer_delim = '\n' if short else '\n\n'

  layers_info = layer_delim.join([
    layer_description(layer, shapes[layer], attributes=attributes, short=short)
    for layer in all_layers
  ])

  summary = '{input_summary} -> {output_summary}\n{total}\n{sep}\n{layers_description}'.format(
    input_summary=input_summary,
    total='total number of params: %d' % get_total_number_of_parameters(layer_or_layers),
    sep='=' * 32,
    output_summary=output_summary,
    layers_description=layers_info
  )

  return summary