import tensorflow as tf

__all__ = [
  'normalize_axis'
]

def normalize_axis(tensor_or_dim, axis):
  if isinstance(tensor_or_dim, int):
    dim = tensor_or_dim
  else:
    dim = len(tensor_or_dim.shape)

  if isinstance(axis, int):
    return (axis % dim, )
  else:
    return tuple(a % dim for a in axis)