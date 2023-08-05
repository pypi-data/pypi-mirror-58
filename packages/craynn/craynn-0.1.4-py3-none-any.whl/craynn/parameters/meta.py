import tensorflow as tf

from .parameter_utils import combine_properties, init_name
from ..meta import bind

__all__ = [
  'Parameter',
  'ConstantParameter',
  'FreeParameter',
  'UnboundParameter', 'BoundParameter',

  'constant_parameter',
  'free_parameter',
  'unbound_parameter',
  'bound_parameter',

  'as_free_parameter',
  'parameter_model'
]

class Parameter(object):
  def __init__(self, shape, properties, name=None):
    self.shape = shape
    self.name = name

    if properties is None:
      self.properties = dict()
    else:
      self.properties = properties

  def __call__(self):
    return self.get_output_for(*self.dependencies())

  def get_output_for(self, *vars):
    raise NotImplementedError()

  def dependencies(self):
    """
    Returns variables this parameter depends on, i.e. ones
    required for `get_output_for` method.
    `dependencies()` can be different from `variables()` if `Parameter`
    does not own variables, like a shared parameter.

    :return: list of `tf.Variable`
    """
    return self.variables()

  def variables(self):
    """
    Returns variables that are owned by the parameter.
    A variable shared between multiple parameters must be owned by only one of the parameters,
    however, might appear in `dependencies()` multiple times.

    :return: list of `tf.Variable`
    """
    raise NotImplementedError()

  def reset(self):
    raise NotImplementedError()

  def __str__(self):
    name = self.__class__.__name__ if self.name is None else self.name
    shape = 'x'.join([ '%d' % (s, ) for s in self.shape ])
    props = [('shape', shape)] + list(self.properties.items())

    return '%s (%s)' % (
      name,
      ', '.join([ '%s=%s' % (k, v) for k, v in props ])
    )

  def __repr__(self):
    return str(self)

class ConstantParameter(Parameter):
  def __init__(self, value, properties=None, name=None):
    super(ConstantParameter, self).__init__(value.shape, properties, name=name)

    self._original_value = value
    self._value = tf.constant(value, dtype=value.dtype, shape=value.shape, name=name)

  def __call__(self):
    return self._value

  def get_output_for(self,):
    return self._value

  def variables(self):
    return []

  def reset(self):
    return self._value


def constant_parameter(value, dtype=tf.float32, name=None, **properties):
  def constructor(shape, **additional_properties):
    import numpy as np

    try:
      dtype_ = dtype.as_numpy_dtype
    except AttributeError:
      dtype_ = dtype

    if not isinstance(value, np.ndarray):
      v = np.array(value, dtype=dtype_)
    else:
      v = value

    v = np.broadcast_to(v, shape)
    props = combine_properties(properties, additional_properties)

    return ConstantParameter(v, properties=props, name=name)

  return constructor


class FreeParameter(Parameter):
  ### everything for pickle
  def __init__(self, initializer, initializer_arguments, properties=None, name=None):
    super(FreeParameter, self).__init__(initializer_arguments['shape'], properties, name)

    self._initializer = initializer
    self._initializer_arguments = initializer_arguments

    self.initial = initializer(**initializer_arguments)
    self._value = tf.Variable(
      initial_value=self.initial,
      name=name,
      dtype=self.initial.dtype,
      trainable=self.properties.get('trainable', False)
    )

  def get_output_for(self, value):
    return value

  def variables(self):
    return [self._value,]

  def reset(self):
    return self._value.assign(
      self._initializer(**self._initializer_arguments)
    )

free_parameter = FreeParameter


def parameter_model2(clazz):
  from inspect import signature, Signature, Parameter
  from ..meta import get_kwargs

  original_signature = signature(clazz)

  assert any([
    param.name == 'shape'
    for param in original_signature.parameters.values()
  ]), 'Decorated function or class must have a "shape" argument.'

  accepted_kwargs = get_kwargs(clazz)

  def wrapped(name=None, **kwargs):
    external_name = name

    def constructor(shape, name=None, **additional_properties):
      if external_name is not None:
        name = external_name

      if name is not None:
        name = init_name(name)

      constructor_kwargs = dict([
        (k, v) for k, v in kwargs.items() if k in accepted_kwargs
      ])

      if 'name' in accepted_kwargs:
        constructor_kwargs['name'] = name

      properties = dict([
        (k, v) for k, v in kwargs.items() if k not in accepted_kwargs
      ])
      properties = combine_properties(properties, additional_properties)

      clazz_args, clazz_kwargs = bind(original_signature, shape=shape, **constructor_kwargs, properties=properties)

      return clazz(*clazz_args, **clazz_kwargs)

    return constructor

  new_signature = Signature(
    parameters=[
        param for param in original_signature.parameters.values() if param.name != 'shape'
      ] + ([] if 'name' in accepted_kwargs else [
        Parameter('name', kind=Parameter.POSITIONAL_OR_KEYWORD, annotation='str')
      ]),
    return_annotation=original_signature.return_annotation
  )

  wrapped.__signature__ = new_signature
  wrapped.__doc__ = clazz.__doc__

  return wrapped

class ParameterConstructor(object):
  def __init__(self, user_defined_properties, external_name=None):
    self._user_defined_properties = user_defined_properties
    self._external_name = external_name

  def user_defined_properties(self):
    return self._user_defined_properties

  def __call__(self, shape, name=None, **additional_properties):
    raise NotImplementedError

def parameter_model(clazz):
  from inspect import signature, Signature, Parameter as FParameter
  from ..meta import get_kwargs

  original_signature = signature(clazz)

  assert any([
    param.name == 'shape'
    for param in original_signature.parameters.values()
  ]), 'Decorated function or class must have a "shape" argument.'

  assert any([
    param.name == 'properties'
    for param in original_signature.parameters.values()
  ]), 'Decorated function or class must have a "properties" argument.'

  accepted_kwargs = get_kwargs(clazz)

  def __init__(self, name=None, **kwargs):
    user_defined_properties = dict([
      (k, v) for k, v in kwargs.items()
      if k not in accepted_kwargs
    ])

    self.constructor_kwargs = dict([
      (k, v) for k, v in kwargs.items()
      if k in accepted_kwargs
    ])

    ParameterConstructor.__init__(self, user_defined_properties, external_name=name)

  new_signature = Signature(
    parameters=[
       FParameter('self', kind=FParameter.POSITIONAL_ONLY)
     ] + [
       param for param in original_signature.parameters.values() if param.name != 'shape'
     ] + ([] if 'name' in accepted_kwargs else [
      FParameter('name', kind=FParameter.POSITIONAL_OR_KEYWORD, annotation='str')
    ]),
    return_annotation=original_signature.return_annotation
  )

  __init__.__signature__ = new_signature
  __init__.__doc__ = clazz.__doc__

  def __call__(self, shape, name=None, **additional_properties):
    if self._external_name is not None:
      name = self._external_name

    if name is not None:
      name = init_name(name)

    constructor_kwargs = self.constructor_kwargs.copy()

    if 'name' in accepted_kwargs:
      constructor_kwargs['name'] = name

    properties = combine_properties(self._user_defined_properties, additional_properties)

    clazz_args, clazz_kwargs = bind(original_signature, shape=shape, **constructor_kwargs, properties=properties)

    return clazz(*clazz_args, **clazz_kwargs)

  return type(
    clazz.__name__,
    (ParameterConstructor, ),
    dict(
      __init__=__init__,
      __call__=__call__
    )
  )

def as_free_parameter(f):
  from inspect import signature, Signature, Parameter as FParameter
  from ..meta import get_kwargs

  f_signature = signature(f)

  assert not any([
    param.kind == FParameter.VAR_KEYWORD
    for param in f_signature.parameters.values()
  ]), 'parameter decorator does not accept functions with `**kwargs`.'

  assert any([
    param.name == 'shape'
    for param in f_signature.parameters.values()
  ]), 'Decorated function must have a "shape" argument.'

  accepted_kwargs = get_kwargs(f)

  def __init__(self, *args, name=None, **kwargs):
    self.external_name = name
    self.args = args
    self.kwargs = kwargs

    user_defined_properties = dict([
      (k, v) for k, v in kwargs.items() if k not in accepted_kwargs
    ])

    self.function_kwargs = dict([
      (k, v) for k, v in kwargs.items() if k in accepted_kwargs
    ])

    ParameterConstructor.__init__(self, user_defined_properties, external_name=name)

  new_signature = Signature(
    parameters=[
      FParameter('self', kind=FParameter.POSITIONAL_ONLY)
    ] + [
      param for param in f_signature.parameters.values() if param.name != 'shape'
    ] + ([] if 'name' in accepted_kwargs else [
      FParameter('name', kind=FParameter.POSITIONAL_OR_KEYWORD, annotation='str')
    ]) + [
      FParameter('properties', kind=FParameter.VAR_KEYWORD)
    ],
    return_annotation=f_signature.return_annotation
  )

  __init__.__signature__ = new_signature
  __init__.__doc__ = f.__doc__

  def __call__(self, shape, name=None, **additional_properties):
    if self._external_name is not None:
      name = self._external_name

    if name is not None:
      name = init_name(name)

    function_kwargs = self.function_kwargs.copy()

    if 'name' in accepted_kwargs:
      function_kwargs['name'] = name

    arguments = f_signature.bind(*self.args, shape=shape, **function_kwargs)
    arguments.apply_defaults()

    return FreeParameter(
      initializer=f, initializer_arguments=arguments.arguments,
      name=name, properties=combine_properties(self._user_defined_properties, additional_properties)
    )

  clazz = type(
    f.__name__,
    (ParameterConstructor, ),
    dict(
      __init__=__init__,
      __call__=__call__
    )
  )

  return clazz

class BoundParameter(Parameter):
  def __init__(self, value, shape=None, properties=None, name=None):
    super(BoundParameter, self).__init__(shape, properties, name)

    self.value = value
    self.shape = tuple(value.shape.as_list()) if shape is None else shape
    self.dtype = value.dtype

  def get_output_for(self,):
    return self.value

  def variables(self):
    return []

  def __str__(self):
    return '%s [%s]: %s' % (
      self.__class__.__name__ if self.name is None else self.name,
      self.value,
      str(self.shape),
    )

bound_parameter = lambda value, shape=None, name=None, **properties: \
  BoundParameter(value, shape, properties=properties, name=name)

class UnboundParameter(Parameter):
  def __init__(self, shape, dtype='float32', properties=None, name=None):
    super(UnboundParameter, self).__init__(shape, properties, name)

    self.shape = shape
    self.dtype = dtype

  def get_output_for(self, ):
    raise NotImplementedError('Unbound parameters are meant to be substituted.')

  def own_variables(self):
    raise NotImplementedError('Unbound parameters are meant to be substituted.')

  def __str__(self):
    return '%s: %s' % (
      self.__class__.__name__ if self.name is None else self.name,
      str(self.shape)
    )

unbound_parameter = parameter_model(UnboundParameter)