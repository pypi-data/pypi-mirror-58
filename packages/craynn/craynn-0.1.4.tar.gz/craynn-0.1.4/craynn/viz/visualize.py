### With a little shame stolen from nolearn

"""
Copyright (c) 2012-2015 Daniel Nouri

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from ..layers import Layer, DenseLayer, InputLayer, get_output_shape, get_layers
from ..layers.inspect import get_number_of_parameters, get_total_number_of_parameters
from ..networks import Network

__all__ = [
  'draw_to_file',
  'draw_to_notebook',
  'viz_all_params',
  'viz_params'
]

_color_set = [
  ### blue
  ('#a6cee3', '#1f78b4'),
  ### green
  ('#b2df8a', '#33a02c'),
  ### red
  ('#fb9a99', '#e31a1c'),
  ### orange
  ('#fdbf6f', '#ff7f00'),
  ### magenta
  ('#cab2d6', '#6a3d9a'),
  ### yellow/brown
  ('#ffff99', '#b15928'),
]

def _stable_hash(data):
  from hashlib import blake2b
  return int.from_bytes(blake2b(data.encode('utf-16be'), digest_size=8).digest(), byteorder='big')

def get_color(layer_class):
  layer_type = layer_class.__name__.lower()

  hashed = _stable_hash(layer_class.__name__) % len(_color_set[0])

  if 'conv' in layer_type:
    return _color_set[0][hashed]

  if issubclass(layer_class, DenseLayer) or 'dense' in layer_type:
    return _color_set[1][hashed]

  if issubclass(layer_class, InputLayer) or 'input' is layer_type:
    return _color_set[2][hashed]

  if 'pool' in layer_type:
    return _color_set[3][hashed]

  if 'recurrent' in layer_type:
    return _color_set[4][hashed]

  return _color_set[5][hashed]

def viz_params(**kwargs):
  def f(layer):
    param_info = get_number_of_parameters(layer, **kwargs).items()
    if len(param_info) > 0:
      return ','.join([ '%s: %d' % (k.name, v) for k, v in param_info ])
    else:
      return None

def viz_all_params(**properties):
  def number_of_params(layer):
    n = get_number_of_parameters(layer, **properties)
    if n > 0:
      return '%d' % n
    else:
      return None

  return number_of_params

def viz_name(force_class_name=False, remove_layer_from_class_name=True, kernel_info=True):
  def name(layer):
    layer_class = layer.__class__.__name__.split('.')[-1]

    if remove_layer_from_class_name:
      layer_class = layer_class.replace('Layer', '')
      layer_class = layer_class.replace('layer', '')

    kernel_info = []
    if hasattr(layer, 'kernel_size'):
      kernel_info.append(
        'x'.join('%d' % k for k in layer.kernel_size)
      )

    if hasattr(layer, 'stride'):
      if any(s != 1 for s in layer.stride):
        kernel_info.append(
          'stride=%s' % (
            'x'.join('%d' % k for k in layer.stride),
          )
        )

    if hasattr(layer, 'padding'):
      if layer.padding != 'valid':
        kernel_info.append('pad=%s' % layer.padding)

    if layer.name is None or force_class_name:
      result = layer_class
    else:
      result = '%s : %s' % (layer.name, layer_class)

    if kernel_info:
      return '%s %s' % (result, ', '.join(kernel_info))
    else:
      return result

  return name

default_display_properties = [
  (None, viz_name()),
  ('#params', viz_all_params()),
  ('output shape', get_output_shape),
]

def make_graph(layers, properties_to_display=default_display_properties):
  import pydotplus as pydot

  graph = pydot.Dot('network', graph_type='digraph')

  layer_indx = dict([
    (layer, 'node%d' % i) for i, layer in enumerate(layers)
  ])

  nodes = dict()

  properties_spec = []

  for spec in properties_to_display:
    try:
      name, prop = spec
      properties_spec.append((name, prop))
    except ValueError:
      properties_spec.append((None, spec))

  for layer in layers:
    info = []
    for prop_name, prop in properties_spec:
      try:
        result = prop(layer)
        if result is None:
          continue

        if prop_name is not None:
          info.append('%s: %s' % (prop_name, result))
        else:
          info.append('%s' % result)
      except Exception as e:
        import warnings
        warnings.warn('Failed to evaluate property %s [%s]' % (prop_name, e))

    nodes[layer] = pydot.Node(
      name=layer_indx[layer], shape='record',
      label='\n'.join(info),
      fillcolor=get_color(layer.__class__), style='filled'
    )

  for node in nodes.values():
    graph.add_node(node)

  for layer in layers:
    for incoming in getattr(layer, 'incoming', list()):
      graph.add_edge(pydot.Edge(nodes[incoming], nodes[layer]))

  graph.set('splines', 'ortho')

  return graph


def get_png(layers_or_layer_or_network, properties_to_display=default_display_properties):
  import pydotplus as pydot

  try:
    if isinstance(layers_or_layer_or_network, Network):
      layers_or_layer = layers_or_layer_or_network.layers()
    else:
      layers_or_layer = layers_or_layer_or_network

    graph = make_graph(get_layers(layers_or_layer), properties_to_display)

    return graph.create(format='png')
  except pydot.InvocationException as e:
    import traceback
    tb = traceback.format_exc()

    import warnings
    warnings.warn(tb)

def draw_to_file(layers_or_layer_or_network, path, properties_to_display=default_display_properties):
  png = get_png(layers_or_layer_or_network, properties_to_display=properties_to_display)

  with open(path, 'wb') as f:
    f.write(png)


def draw_to_notebook(layers_or_layer_or_network, properties_to_display=default_display_properties):
  from IPython.display import Image

  png = get_png(layers_or_layer_or_network, properties_to_display=properties_to_display)

  return Image(png)
