import tensorflow as tf

from .meta import FunctionalLayer, InputLayer
from .meta import model_from, derive
from .meta import find_in_graph

from ..parameters import glorot_uniform_init

__all__ = [
  'const_input', 'variable_input',
  
  'FunctionLayer', 'custom', 'nonlinearity',
  'ConcatLayer', 'concat',
  'FlattenLayer', 'flatten',
  'ReshapeLayer', 'reshape',
  'TransposeLayer', 'transpose',

  'ElementwiseLayer', 'ElementwiseSumLayer', 'ElementwiseMeanLayer',
  'ElementwiseMaxLayer', 'ElementwiseMinLayer',

  'elementwise', 'elementwise_sum', 'elementwise_mean',
  'elementwise_max', 'elementwise_min',

  'SquareDifference', 'square_difference'
]

class ConstInput(InputLayer):
  def __init__(self, const, name=None):
    self.value = tf.constant(const)
    super(ConstInput, self).__init__(shape=const.shape, name=name)

  def get_output_for(self):
    return self.value

class VariableInput(InputLayer):
  def __init__(self, shape, V=glorot_uniform_init(), name=None):
    self.parameters = [V(shape, trainable=True)]

    super(VariableInput, self).__init__(shape=shape, name=name)

  def get_output_for(self, V):
    return V

const_input = lambda const, name=None: \
  lambda : ConstInput(const, name=name)

variable_input = lambda shape, V=glorot_uniform_init(), name=None: \
  lambda : VariableInput(shape, V, name=name)


class FunctionLayer(FunctionalLayer):
  def __init__(self, f, *incoming, name=None):
    if name is None:
      name = f.__name__

    super(FunctionLayer, self).__init__(*incoming, name=name)

    self.f = f

  def get_output_for(self, *incoming):
    return self.f(*incoming)

  def get_output_shape_for(self, *input_shapes):
    return input_shapes[0]

custom = lambda f, name=None: lambda *incoming: FunctionLayer(f, *incoming, name=name)
nonlinearity = custom


class ConcatLayer(FunctionalLayer):
  def __init__(self, *incoming, axis=-1, name=None):
    super(ConcatLayer, self).__init__(*incoming, name=name)

    assert len(incoming) > 0

    self.axis = axis

  def get_output_for(self, *inputs):
    return tf.concat(values=inputs, axis=self.axis, name=str(self) + '_concat')

  def get_output_shape_for(self, *input_shapes):
    first = input_shapes[0]
    axis = (self.axis + len(first)) % len(first)

    return tuple([
      first[i] if i != axis else sum([s[i] for s in input_shapes])
      for i in range(len(first))
    ])


concat = lambda axis=-1, name=None: lambda *incoming: ConcatLayer(*incoming, axis=axis, name=name)

class ExpandConcatLayer(FunctionalLayer):
  def __init__(self, *incoming, name=None):
    super(ExpandConcatLayer, self).__init__(*incoming, name=name)
    assert len(incoming) > 0

  def get_output_for(self, *inputs):
    max_len = max([ len(input.shape) for input in inputs ])
    expanded = [
      tf.expand_dims(input, axis=-1) if len(input.shape) < max_len else input
      for input in inputs
    ]

    return tf.concat(expanded, axis=-1)

  def get_output_shape_for(self, *input_shapes):
    original = input_shapes[0]

    return original[:-1] + (sum([shape[-1] for shape in input_shapes]), )


expand_concat = lambda name=None: lambda *incoming: ExpandConcatLayer(*incoming, name=name)

from functools import reduce as _reduce

class FlattenLayer(FunctionalLayer):
  def __init__(self, incoming, outdim=2, name=None):
    super(FlattenLayer, self).__init__(incoming, name=name)

    self.outdim = outdim

  def get_output_for(self, incoming):
    in_shape = tf.shape(incoming)

    out_shape = tf.stack([
      in_shape[i] for i in range(self.outdim - 1)
    ] + [
      tf.reduce_prod(in_shape[self.outdim - 1:])
    ])

    return tf.reshape(incoming, out_shape)

  def get_output_shape_for(self, input_shapes):
    return input_shapes[:self.outdim - 1] + (
      _reduce(
        lambda a, b: a * b if a is not None and b is not None else None,
        input_shapes[self.outdim - 1:],
        1
      ),
    )

flatten = lambda outdim=2, name=None: lambda incoming: FlattenLayer(incoming, outdim=outdim, name=name)

class ReshapeLayer(FunctionalLayer):
  def __init__(self, incoming, new_shape, name=None):
    super(ReshapeLayer, self).__init__(incoming, name=name)

    assert len([dim for dim in new_shape if dim < 0]) < 2, 'ambiguous new shape'

    self.new_shape = tuple([ (-1 if s is None else s) for s in new_shape ])

  def get_output_for(self, incoming):
    return tf.reshape(incoming, self.new_shape, name=str(self) + '_reshape')

  def get_output_shape_for(self, input_shape):
    import numpy as np

    if -1 in self.new_shape:
      if all(dim is not None for dim in input_shape):
        total = np.prod(input_shape, dtype='int64')
        known_dims = np.prod([ dim for dim in self.new_shape if dim is not None], dtype='int64')
        assert total % known_dims == 0, 'can not broadcast %s into %s' % (input_shape, self.new_shape)
        inferred = total // known_dims

        return tuple(dim if dim is not None else inferred for dim in self.new_shape)
      else:
        return tuple(dim if dim >= 0 else None for dim in self.new_shape)

    else:
      return self.new_shape

reshape = lambda new_shape, name=None: lambda incoming: ReshapeLayer(incoming, new_shape, name=name)

class TransposeLayer(FunctionalLayer):
  def __init__(self, incoming, perm, name=None):
    super(TransposeLayer, self).__init__(incoming, name=name)
    self.perm = perm

  def get_output_shape_for(self, input_shape):
    return tuple([ input_shape[i] for i in self.perm ])

  def get_output_for(self, input):
    return tf.transpose(input, perm=self.perm)

transpose = lambda perm, name=None: lambda incoming: TransposeLayer(incoming, perm=perm, name=name)

class ElementwiseLayer(FunctionalLayer):
  def __init__(self, *incoming, op, name=None):
    super(ElementwiseLayer, self).__init__(*incoming, name=name)
    self.op = op

  def get_output_for(self, *inputs):
    return self.op(*inputs)

  def get_output_shape_for(self, *input_shapes):
    for shape in input_shapes[1:]:
      if tuple(shape) != tuple(input_shapes[0]):
        raise ValueError('An elementwise operation requires all input shapes to be the same!')

    return input_shapes[0]

elementwise = model_from(ElementwiseLayer)()


ElementwiseSumLayer = derive('ElementwiseSumLayer').based_on(ElementwiseLayer).with_fixed(
  op=lambda *inputs: sum(inputs)
)
elementwise_sum = model_from(ElementwiseSumLayer)()

ElementwiseMeanLayer = derive('ElementwiseMeanLayer').based_on(ElementwiseLayer).with_fixed(
  op=lambda *inputs: sum(inputs) / len(inputs)
)
elementwise_mean = model_from(ElementwiseMeanLayer)()

from functools import reduce

ElementwiseMaxLayer = derive('ElementwiseMaxLayer').based_on(ElementwiseLayer).with_fixed(
  op=lambda *inputs: reduce(tf.maximum, inputs)
)
elementwise_max = model_from(ElementwiseMaxLayer)()

ElementwiseMinLayer = derive('ElementwiseMinLayer').based_on(ElementwiseLayer).with_fixed(
  op=lambda *inputs: reduce(tf.minimum, inputs)
)
elementwise_min = model_from(ElementwiseMinLayer)()


class SquareDifference(FunctionalLayer):
  def __init__(self, incoming1, incoming2, axes=None, name=None):
    from .meta import get_output_shape

    super(SquareDifference, self).__init__(incoming1, incoming2, name=name)
    if axes is None:
      shape = get_output_shape(incoming1)
      self.axes = list(range(len(shape)))[1:]
    else:
      self.axes = axes

  def get_output_for(self, input1, input2):
    return tf.reduce_mean(
      (input1 - input2) ** 2,
      axis=self.axes
    )

  def get_output_shape_for(self, shape1, shape2):
    return [ s for i, s in enumerate(shape1) if i not in self.axes]

square_difference = lambda axes=None, name=None: lambda incoming1, incoming2: SquareDifference(
  incoming1, incoming2, axes=axes, name=name
)