import numpy as np
import tensorflow as tf

__all__ = [
  'sliced_seq',
  'xeval',
  'xmap'
]

def sliced_seq(size, batch_size=None):
  if batch_size is not None:
    n_batches = size // batch_size + (1 if size % batch_size != 0 else 0)

    for i in range(n_batches):
      yield slice(i * batch_size, min((i + 1) * batch_size, size))
  else:
    for s in range(size):
      yield s

def xeval(f, indexed_seq, size):
  """
  Evaluates `f` on `variables` with mini-batches.
  `f` must preserve the first dimension of the arguments.

  If `f` returns a single tensor (e.g. `return a_tensor`, but not `return (a_tensor, )`),
  `tfeval` returns a single array. Otherwise, it returns a tuple of arrays, with elements
  corresponding to each return value.

  `batch_size` sets size of mini-batches.
  `batch_size=None` is equivalent to `batch_size=1`
  but tensors in mini-batches lack the batch dimension, e.g.:

  `tfeval(f, a, b, batch_size=1)` makes the following calls:
  ```
  f(a[0:1], b[0:1]),
  f(a[1:2], b[1:2]),
  ...
  ```

  while with `batch_size=None`:

  ```
  f(a[0], b[0]),
  f(a[1], b[1]),
  ...
  ```
  """
  results = None
  singular = False

  make_buffer = lambda xs, bdim=1: tuple([
    np.ndarray(shape=(size,) + x.shape[bdim:], dtype=x.dtype.as_numpy_dtype)
    for x in xs
  ])

  for indx, batch in indexed_seq:
    batch_results = f(*batch)

    if not isinstance(batch_results, tuple):
      batch_results = (batch_results, )
      singular = True

    if results is None:
      results = make_buffer(batch_results, 0 if isinstance(indx, int) else 1)

    for br, r in zip(batch_results, results):
      r[indx] = br

  if len(results) == 1 and singular:
    return results[0]
  else:
    return results

def xmap(f, indexed_seq, size):
  """
  Similar to `xeval` but returns a single or multiple instances of `tf.Variable` instead.
  """
  make_buffer = lambda rs, bdim=1: tuple(
    tf.Variable(
      initial_value=tf.zeros((size,) + r.shape[bdim:], dtype=r.dtype),
      shape=(None,) + r.shape[bdim:],
      dtype=r.dtype,
      validate_shape=False,
    )
    for r in rs
  )

  results = None
  singular = False
  broadcasts = None

  index = None
  index_broadcasts = list()

  for indx, batch in indexed_seq:
    batch_results = f(*batch)

    if not isinstance(batch_results, tuple):
      batch_results = (batch_results, )
      singular = True

    if results is None:
      results = make_buffer(batch_results, 0 if isinstance(indx, int) else 1)

      broadcasts = tuple(
        (None,) + tuple(slice(None, None, None) for _ in br.shape)
        for br in batch_results
      )

      index_broadcasts = tuple(
        (slice(None, None, None), ) + tuple(None for _ in br.shape[1:])
        for br in batch_results
      )

      if not isinstance(indx, int):
        index = tf.range(size)

    if isinstance(indx, int):
      for br, r, broadcast in zip(batch_results, results, broadcasts):
        r.scatter_nd_update(
          indices=[[indx]],
          updates=br[broadcast]
        )
    else:
      for br, r, broadcast in zip(batch_results, results, index_broadcasts):
        r.scatter_nd_update(
          indices=index[indx][broadcast],
          updates=br
        )

  if len(results) == 1 and singular:
    return results[0]
  else:
    return results
