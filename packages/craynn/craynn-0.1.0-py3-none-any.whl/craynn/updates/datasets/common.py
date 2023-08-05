from .meta import Dataset

__all__ = [
  'MappedDataset', 'ZippedDataset'
]

class MappedDataset(Dataset):
  def __init__(self, dataset : Dataset, f, batch_size=1):
    super(MappedDataset, self).__init__()

    self.f = f
    self.dataset = dataset
    self.batch_size = batch_size

  def _get_single(self, item):
    result = self._get_slice(
      slice(item, item + 1) if item != -1 else slice(item, None)
    )

    return tuple(
      r.reshape(r.shape[1:])
      for r in result
    )

  def _get_slice(self, item):
    result = self.f(
      *self.dataset._get_slice(item)
    )

    return result if isinstance(result, tuple) else (result, )

  def _get_sparse(self, item):
    result = self.f(
      *self.dataset._get_sparse(item)
    )

    return result if isinstance(result, tuple) else (result,)

  def get_subset(self, item):
    return self.dataset.subset(item).map(self.f)

  def size(self):
    return self.dataset.size()

  def data(self):
    from .utils import xmap

    result = xmap(
      self.f,
      self.dataset.indexed_seq(batch_size=self.batch_size),
      size=len(self.dataset)
    )

    return result if isinstance(result, tuple) else (result,)

  def shapes(self):
    size = len(self.dataset)
    probe = self._get_slice(slice(0, 1))

    return tuple(
      (size, ) + p.shape[1]
      for p in probe
    )


class ZippedDataset(Dataset):
  def __init__(self, first : Dataset, second : Dataset):
    super(ZippedDataset, self).__init__()

    self.first = first
    self.second = second

  def _get_single(self, item):
    return self.first._get_single(item) + self.second._get_single(item)

  def _get_slice(self, item):
    return self.first._get_slice(item) + self.second._get_slice(item)

  def _get_sparse(self, item):
    return self.first._get_sparse(item) + self.second._get_sparse(item)

  def get_subset(self, item):
    return self.first.subset(item).zip(self.second.subset(item))

  def size(self):
    return self.first.size()

  def data(self):
    return self.first.data() + self.second.data()

  def shapes(self):
    return self.first.shapes() + self.second.shapes()