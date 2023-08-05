import tensorflow as tf
import collections

from .meta import Dataset

class VariableDataset(Dataset):
  def __init__(self, *variables):
    self.variables = tuple(variables)

    super(VariableDataset, self).__init__()

  @classmethod
  def _slice_class(cls):
    from .subsets import SlicedSubset
    return SlicedSubset

  def _get_single(self, item):
    return tuple(
      var[item]
      for var in self.variables
    )

  def _get_slice(self, item):
    return tuple(
      var[item]
      for var in self.variables
    )

  def _get_sparse(self, item):
    return tuple(
      tf.gather(var, item)
      for var in self.variables
    )

  def size(self):
    return tf.shape(self.variables[0])[0]

  @tf.function
  def assign(self, *data):
    return [
      var.assign(value)
      for var, value in zip(self.variables, data)
    ]

  def data(self):
    return self.variables

  def shapes(self):
    return tuple(
      var.shape for var in self.variables
    )

def empty_dataset(*shapes, dtypes=tf.float32):
  assert len(shapes) > 0

  if isinstance(dtypes, str) or isinstance(dtypes, tf.dtypes.DType):
    dtypes = [dtypes for _ in shapes]

  shapes = [
    shape_or_array.shape if hasattr(shape_or_array, 'shape') else shape_or_array
    for shape_or_array in shapes
  ]

  general_shapes = [
    (None,) + shape[1:]
    for shape in shapes
  ]

  if not isinstance(dtypes, collections.Iterable) or isinstance(dtypes, str):
    default_dtype = dtypes
    dtypes = []

    for shape_or_array in shapes:
      if hasattr(shape_or_array, 'dtype'):
        dtypes.append(shape_or_array.dtype)
      else:
        dtypes.append(default_dtype)

  variables = [
    tf.Variable(
      initial_value=tf.zeros(shape, dtype=dtype),
      dtype=dtype,
      validate_shape=False,
      shape=general_shape,
    ) for shape, general_shape, dtype in zip(shapes, general_shapes, dtypes)
  ]

  return VariableDataset(*variables)


def variable_dataset(*data):
  dataset = empty_dataset(
    *(d.shape for d in data),
    dtypes=tuple(str(d.dtype) for d in data)
  )
  dataset.assign(*data)
  return dataset