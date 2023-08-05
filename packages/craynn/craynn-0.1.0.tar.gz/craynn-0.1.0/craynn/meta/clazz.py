from inspect import signature, Signature, Parameter, _empty

__all__ = [
  'derive',
  'carry',
  'bind',

  'CarringExpression',
]

def get_var_arguments(signature):
  var_arguments = [
    name for name, param in signature.parameters.items()
    if param.kind == Parameter.VAR_POSITIONAL
  ]

  if len(var_arguments) == 0:
    return None
  else:
    return var_arguments[0]

def bind(signature, **kwargs):
  resolved_args = []
  resolved_kwargs = {}

  it = iter(signature.parameters.items())

  for name, param in it:
    if name not in kwargs:
      break

    if param.kind in [Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD]:
      resolved_args.append(kwargs[name])
    elif param.kind == Parameter.VAR_POSITIONAL:
      resolved_args.extend(kwargs[name])
      break

  for name, param in it:
    if name in kwargs:
      resolved_kwargs[name] = kwargs[name]

  return tuple(resolved_args), resolved_kwargs

class From(object):
  def __init__(self, what, base_class):
    self.what = what
    self.base_class = base_class

  def with_fixed(self, **kwargs):
    return fix_params_in_a_class(self.what, self.base_class, kwargs)

class Deriver(object):
  def __init__(self, what):
    self.what = what

  def based_on(self, base_class):
    return From(self.what, base_class)

derive = Deriver

def fix_params_in_a_class(name, base_class, fixing):
  original_signature = signature(base_class.__init__)

  new_signature = Signature(
    parameters=[
      param
      for name, param in original_signature.parameters.items()
      if name not in fixing
    ],
    return_annotation=original_signature.return_annotation
  )

  def new_init(self, *args, **kwargs):
    arguments = new_signature.bind(self, *args, **kwargs)
    arguments.apply_defaults()

    updated_kwargs = arguments.arguments.copy()
    updated_kwargs.update(fixing)

    args, kwargs = bind(original_signature, **updated_kwargs)

    base_class.__init__(*args, **kwargs)


  new_init.__signature__ = new_signature

  return type(name, (base_class, ), {
    '__init__' : new_init
  })

def carry(original, fixed, defaults, carried_arguments):
  original_signature = signature(original)

  for k in defaults:
    if k not in original_signature.parameters:
      raise ValueError('Attempting to provide default value for invalid argument %s.' % k)

  for k in fixed:
    if k not in original_signature.parameters:
      raise ValueError('Attempting to fix value of invalid argument %s!' % k)

  for k in carried_arguments:
    if k not in original_signature.parameters:
      raise ValueError('Attempting to carry invalid argument %s!' % k)

  mutual_keys = set(defaults.keys()) & set(fixed.keys())
  if len(mutual_keys) > 0:
    raise ValueError('The same arguments are fixed and provided default value for: %s!' % list(mutual_keys))

  mutual_keys = set(fixed.keys()) & set(carried_arguments)
  if len(mutual_keys) > 0:
    raise ValueError('The same arguments are fixed and carried: %s!' % list(mutual_keys))

  mutual_keys = set(defaults.keys()) & set(carried_arguments)
  if len(mutual_keys) > 0:
    raise ValueError('The same arguments are carried and provided default value for: %s!' % list(mutual_keys))

  ### replacing default values
  original_sig_with_defaults = Signature(
    parameters=[
      param.replace(default=defaults.get(name, param.default))
      for name, param in original_signature.parameters.items()
    ],
    return_annotation=original_signature.return_annotation
  )

  carried_arguments_set = set(carried_arguments)

  constructor_signature = Signature(
    parameters=[
      param.replace(kind=Parameter.POSITIONAL_OR_KEYWORD)
      for name, param in original_sig_with_defaults.parameters.items()
      if name not in fixed and name not in carried_arguments_set
    ],
    return_annotation=original_sig_with_defaults.return_annotation
  )

  model_signature = Signature(
    parameters=[
      param
      for name, param in original_sig_with_defaults.parameters.items()
      if name in carried_arguments_set
    ],
    return_annotation=original_sig_with_defaults.return_annotation
  )

  def constructor(*args, **kwargs):
    ### checking if all arguments are specified
    constructor_arguments = constructor_signature.bind(*args, **kwargs)
    constructor_arguments.apply_defaults()

    updated_arguments = constructor_arguments.arguments.copy()

    for k, v in fixed.items():
      updated_arguments[k] = v

    def model(*model_args, **model_kwargs):
      model_arguments = model_signature.bind(*model_args, **model_kwargs)
      args, kwargs = bind(original_signature, **model_arguments.arguments, **updated_arguments)

      result = original(*args, **kwargs)
      return result

    model.__signature__ = model_signature

    return model

  fixed_arguments_doc = ', '.join([
    '%s=%s' % (k, v) for k, v in fixed.items()
  ])

  constructor.__doc__ = "%s(%s)%s" % (original.__name__, fixed_arguments_doc, ('\n%s' % original.__doc__) if original.__doc__ is not None else '')
  constructor.__signature__ = constructor_signature

  return constructor

class CarringExpression(object):
  """
  Allows nice syntax for `carry` method:
  carry(<function>, ['param1', 'param2']).with_fixed(param1=value1).with_defaults(param3=value3)()
  """
  def __init__(self, original, fixed=None, defaults=None, carried=None):
    self.original = original

    self.fixed = dict() if fixed is None else fixed
    self.defaults = dict() if defaults is None else defaults
    self.carried = dict() if carried is None else carried

  def __call__(self):
    return carry(self.original, self.fixed, self.defaults, self.carried)

  def with_defaults(self, **kwargs):
    self.defaults.update(kwargs)
    return self

  def with_fixed(self, **kwargs):
    self.fixed.update(kwargs)
    return self