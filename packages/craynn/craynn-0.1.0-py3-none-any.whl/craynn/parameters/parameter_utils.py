import tensorflow as tf

__all__ = [
  'combine_properties',
  'init_name'
]

def combine_properties(manual_properties, default_properties):
  props = default_properties.copy()
  props.update(manual_properties)

  return props

init_name = lambda name: name + '_init' if name is not None else None

def copy_variable(variable : tf.Variable, validate_shape=False, **kwargs):
  return tf.Variable(
    initial_value=variable.initial_value,
    dtype=variable.dtype,
    trainable=variable.trainable,
    validate_shape=validate_shape,
    **kwargs
  )