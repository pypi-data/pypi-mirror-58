import tensorflow as tf

__all__ = [
  'Dataset'
]

class Dataset(object):
  def __init__(self):
    ### allows nice `dataset.subset[:100] syntax`
    self.subset = SubsetConstructor(self)

  ### for a signle item
  def _get_single(self, item):
    raise NotImplementedError()

  ### for slices
  def _get_slice(self, item):
    raise NotImplementedError()

  ### for any index arrays
  def _get_sparse(self, item):
    raise NotImplementedError()

  def get_subset(self, item):
    from .subsets import SlicedSubset, IndexedSubset
    if isinstance(item, slice):
      return SlicedSubset(self, item)
    else:
      return IndexedSubset(self, item)

  def size(self):
    raise NotImplementedError()

  def data(self):
    """
    Returns tensors held by the dataset.
    Warning: may result in allocation of a new dataset.
    """
    raise NotImplementedError()

  def numpy(self):
    return tuple(
      d.numpy()
      for d in self.data()
    )

  def materialize(self):
    from .variable import variable_dataset
    return variable_dataset(*self.data())

  def shapes(self):
    raise NotImplementedError()

  def __getitem__(self, item):
    if isinstance(item, int):
      return self._get_single(item)
    elif isinstance(item, slice):
      return self._get_slice(item)
    else:
      return self._get_sparse(item)

  def __len__(self):
    return int(self.size())

  def seq(self, batch_size=1):
    from .utils import sliced_seq

    if batch_size is None:
      for i in range(len(self)):
        yield self._get_single(i)
    else:
      for indx in sliced_seq(self.size(), batch_size=batch_size):
        yield self._get_slice(indx)

  def indexed_seq(self, batch_size=1):
    from .utils import sliced_seq

    if batch_size is None:
      for i in range(len(self)):
        yield i, self._get_single(i)
    else:
      for indx in sliced_seq(self.size(), batch_size=batch_size):
        yield indx, self._get_slice(indx)

  def batch(self, batch_size=1):
    if batch_size is None:
      indx = tf.random.uniform(
        shape=(),
        dtype=tf.int32,
        minval=0,
        maxval=self.size()
      )

      return self._get_single(indx)
    else:
      indx = tf.random.uniform(
        shape=(batch_size, ),
        dtype=tf.int32,
        minval=0,
        maxval=self.size()
      )

      return self._get_sparse(indx)

  def eval(self, f=None, batch_size=1):
    if f is None:
      return self.numpy()
    else:
      return self.map(f, batch_size=batch_size).numpy()

  def map(self, f, batch_size=1):
    from .common import MappedDataset
    return MappedDataset(self, f, batch_size=batch_size)

  def zip(self, other):
    from .common import ZippedDataset
    return ZippedDataset(self, other)

class SubsetConstructor(object):
  def __init__(self, dataset : Dataset):
    self.dataset = dataset

  def __getitem__(self, item):
    return self(item)

  def __call__(self, item):
    if isinstance(item, int):
      item = slice(item, item + 1,) if item != -1 else slice(item, None)

    return self.dataset.get_subset(item)