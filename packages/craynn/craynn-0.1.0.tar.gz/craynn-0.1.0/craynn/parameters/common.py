import numpy as np
import tensorflow as tf

from .meta import *
from .parameter_utils import *

__all__ = [
  'zeros_init',
  'ones_init',
  'const_init',
  'normal_init',
  'uniform_init',
  'glorot_normal_init',
  'glorot_uniform_init',

  'glorot_scaling',

  'glorot_normal_double_init',

  'default_weight_init',
  'default_bias_init',

  'shared_parameter'
]

zeros_init = as_free_parameter(tf.zeros)
ones_init = as_free_parameter(tf.ones)


def _const_init(shape, value, dtype='float32', name=None):
  if hasattr(value, 'shape') and len(value.shape) > 0:
    assert value.shape == shape, \
      'If `value` is a non-scalar array then `shape` (%s) must be equal to `value.shape` (%s)' % (shape, value.shape)

    return tf.constant(value, dtype=dtype, name=init_name(name))
  else:
    return tf.ones(shape=shape, dtype=dtype, name=init_name(name)) * \
           tf.constant(value, dtype=dtype)

const_init = as_free_parameter(_const_init)

normal_init = as_free_parameter(tf.random.normal)

uniform_init = as_free_parameter(tf.random.uniform)


def glorot_scaling(shape, gain=1.0):
  in_units, out_units = shape[-2:]
  receptive_field_area = np.prod(shape[:-2])

  return gain * np.sqrt(2.0 / ((in_units + out_units) * receptive_field_area))


def _glorot_normal_init(shape, gain=1.0, dtype='float32', name=None):
  if len(shape) < 2:
    return tf.random.normal(shape=shape, mean=0.0, stddev=gain, dtype=dtype, name=init_name(name))
  else:
    scale = glorot_scaling(shape, gain)
    return tf.random.normal(shape=shape, mean=0.0, stddev=scale, dtype=dtype, name=init_name(name))

def _double_glorot_normal_init(shape, target_shape, gain=1.0, dtype='float32', name=None):
  gain = glorot_scaling(target_shape, gain=gain)
  return _glorot_normal_init(shape, gain=gain, dtype=dtype, name=name)


glorot_normal_init = as_free_parameter(_glorot_normal_init)
glorot_normal_double_init = as_free_parameter(_double_glorot_normal_init)


def _glorot_uniform_init(shape, gain=1.0, dtype='float32', name=None):
  if len(shape) < 2:
    return tf.random.normal(shape=shape, mean=0.0, stddev=gain, dtype=dtype, name=init_name(name))
  else:
    scale = tf.constant(
      glorot_scaling(shape, gain) * np.sqrt(3),
      dtype=dtype
    )

    return tf.random.uniform(shape=shape, minval=-scale, maxval=scale, dtype=dtype, name=name)

glorot_uniform_init = as_free_parameter(_glorot_uniform_init)


default_weight_init = glorot_normal_init(gain=1.0)
default_bias_init = zeros_init()


class SharedParameter(Parameter):
  def __init__(self, parent : Parameter, properties, name=None):
    self.parent = parent
    
    super(SharedParameter, self).__init__(
      self.parent.shape,
      properties=properties,
      name=name
    )

  def dependencies(self):
    return self.parent.dependencies()

  def variables(self):
    ### shared parameters do not own variables, so
    ### this method outputs empty list.
    return []

  def get_output_for(self, *vars):
    return self.parent.get_output_for(*vars)

  def reset(self):
    pass

  def __str__(self):
    return 'SharedParameter[parent=%s]' % (self.parent, )


class ParameterCloneMachine(object):
  def __init__(self, parameter_constructor):
    self.parameter_constructor = parameter_constructor
    self.parameter = None

  def __call__(self, shape, name=None, **additional_properties):
    if self.parameter is None:
      self.parameter = self.parameter_constructor(shape, name, **additional_properties)
      return self.parameter
    else:
      assert shape == self.parameter.shape, 'Can not clone parameter for different shape.'

      return SharedParameter(
        self.parameter,
        properties=combine_properties(
          self.parameter_constructor.user_defined_properties(),
          additional_properties
        ),
        name=name
      )

shared_parameter = ParameterCloneMachine