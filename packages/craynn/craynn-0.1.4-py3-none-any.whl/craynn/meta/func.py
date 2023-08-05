from inspect import signature

__all__ = [
  'get_kwargs',
  'apply_with_kwargs'
]

def get_kwargs(func):
  params = signature(func).parameters
  return [p.name for p in params.values()]

def apply_with_kwargs(f, *args, **kwargs):
  accepted_kwargs = get_kwargs(f)
  passed_kwargs = dict()

  for k, v in kwargs.items():
    if k in accepted_kwargs:
      passed_kwargs[k] = v

  return f(*args, **passed_kwargs)