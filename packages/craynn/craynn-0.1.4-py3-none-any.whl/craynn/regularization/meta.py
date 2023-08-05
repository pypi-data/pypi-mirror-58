from ..layers import get_all_parameters

__all__ = [
  'apply_regularization'
]

def apply_regularization(layer, reg, **properties):
  params = get_all_parameters(layer, **properties)
  regularizers = []
  variables = []

  for param in params:
    result = reg(param)
    if isinstance(result, tuple):
      r, vs = result
      regularizers.append(r)
      variables.extend(vs)
    else:
      regularizers.append(result)

  return sum(regularizers), variables
