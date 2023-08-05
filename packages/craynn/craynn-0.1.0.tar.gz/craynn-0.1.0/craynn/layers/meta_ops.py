from .meta import FunctionalLayer

__all__ = [
  'MetaLayer', 'meta',

  'binary_const_input',
  'binary_var_input',
  'glorot_dense'
]

class MetaLayer(FunctionalLayer):
  def __init__(self, incoming, incoming_parameters, op, name=None):
    """
    Redirects outputs of `incoming_parameters` to parameters of `incoming` layer.
    :param incoming: tuple of incoming data layers
    :param incoming_parameters: tuple of incoming parameter layers
    :param op: operation to wrap
    """
    if name is None:
      name = 'Meta[%s]' % (op.__class__.__name__ if op.name is None else op.name, )

    super(MetaLayer, self).__init__(*incoming, *incoming_parameters, name=name)

    self.incoming_data = incoming
    self.incoming_parameters = incoming_parameters

    self.op = op
    self.parameters = []

  def get_output_shape_for(self, *input_shapes, **modes):
    data_shapes = input_shapes[:len(self.incoming_data)]
    return self.op.get_output_shape_for(*data_shapes, **modes)

  def get_output_for(self, *inputs, **modes):
    n = len(self.incoming_data)
    data = inputs[:n]
    params = inputs[n:]
    return self.op.get_output_for(*params, *data, **modes)

class Meta(object):
  def __call__(self, op):
    return lambda incoming_input, *incoming_params, name=None: \
      MetaLayer(incoming_input, incoming_params, op=op, name=name)

  def __getitem__(self, op):
    return self(op)

meta = Meta()

from .common import const_input, variable_input
from ..utils import binary_encoding
from ..parameters import const_init

binary_const_input = lambda n, name=None: const_input(binary_encoding(range(n), size=n), name=name)

def binary_var_input(n, name=None):
  value = binary_encoding(range(n), size=n)
  return variable_input(shape=value.shape, V=const_init(value=value), name=name)

from ..layers import dense
from ..nonlinearities import linear
from ..parameters import glorot_normal_double_init, zeros_init


glorot_dense = lambda num_units, target_shape, name=None: \
  dense(
    num_units,
    W=glorot_normal_double_init(gain=0.1, target_shape=target_shape),
    b=zeros_init(),
    activation=linear(),
    name=name
  )