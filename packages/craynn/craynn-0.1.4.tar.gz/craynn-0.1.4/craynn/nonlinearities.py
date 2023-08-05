import tensorflow as tf

__all__ = [
  'sigmoid',
  'leaky_sigmoid',
  'tanh',
  'leaky_tanh',
  'relu',
  'leaky_relu',
  'softplus',
  'softmax',
  'elu',
  'linear',

  'gaussian',

  'default_semibounded_nonlinearity',
  'default_bounded_nonlinearity',
  'default_nonlinearity'
]

class Nonlinearity(object):
  def __init__(self, nonlinearity, hyperparameters):
    self.nonlinearity = nonlinearity
    self.hyperparameters = hyperparameters

  def __call__(self, x):
    return self.nonlinearity(x)

  def __str__(self):
    return '%s(%s)' % (
      self.__class__.__name__,
      ', '.join([
        '%s=%s' % (k, v) for k, v in self.hyperparameters.items()
      ])
    )

def nonlinearity_from(f):
  import inspect

  signature = inspect.signature(f)
  name_parameter, = [
    signature.parameters[p] for p in signature.parameters if p == 'name'
  ]

  name = name_parameter.default

  def __init__(self, *args, **kwargs):
    bound = signature.bind(*args, **kwargs)
    bound.apply_defaults()

    g = f(*bound.args, **bound.kwargs)

    hyperparameters = bound.arguments.copy()
    hyperparameters.pop('name', None)

    Nonlinearity.__init__(self, g, hyperparameters)

  clazz = type(
    name,
    (Nonlinearity, ),
    dict(__init__ = __init__)
  )

  return clazz

sigmoid = nonlinearity_from(
  lambda name='sigmoid': lambda x: tf.nn.sigmoid(x, name=name)
)

leaky_sigmoid = nonlinearity_from(
  lambda leakiness=0.05, name='leaky_sigmoid': lambda x: \
    tf.nn.sigmoid(x, name=name) + leakiness * x
)

tanh = nonlinearity_from(
  lambda name='tanh': lambda x: tf.tanh(x, name=name)
)

leaky_tanh = nonlinearity_from(
  lambda leakiness=0.05, name='leaky_tanh': lambda x: \
    tf.tanh(x, name=name) + leakiness * x
)

relu = nonlinearity_from(
  lambda name='ReLU': lambda x: tf.nn.relu(x, name=name)
)

leaky_relu = nonlinearity_from(
  lambda leakiness=0.05, name='leaky_ReLU': \
    lambda x: tf.nn.leaky_relu(x, alpha=leakiness, name=name)
)

softplus = nonlinearity_from(
  lambda name='softplus': lambda x: tf.nn.softplus(x)
)
softmax = nonlinearity_from(
  lambda name='softmax': lambda x: tf.nn.softmax(x, name=name)
)

elu = nonlinearity_from(
  lambda name='ELU': lambda x: tf.nn.elu(x, name=name)
)

linear = nonlinearity_from(
  lambda name='linear': lambda x: x
)

gaussian = nonlinearity_from(
  lambda name='gaussian': lambda x: tf.exp(-x ** 2, name=name)
)

default_bounded_nonlinearity = sigmoid()

### well, leaky relu is not exactly semi-bounded...
default_semibounded_nonlinearity = leaky_relu(0.05)

default_nonlinearity = default_semibounded_nonlinearity