from .meta import achain
from ..layers import find_in_graph

__all__ = [
  'with_inputs',
  'select', 'seek', 'nothing'
]

### Surprisingly, `nothing` is quite useful
nothing = lambda *incoming: incoming

def _selector(*items, search_subgraph=False):
  def selector(*incomings):
    results = []

    for item in items:
      if isinstance(item, int):
        results.append(incomings[item])
      elif isinstance(item, slice):
        results.extend(incomings[item])
      elif isinstance(item, str):
        if search_subgraph:
          layer = find_in_graph(lambda layer: getattr(layer, 'name', None) == item, incomings)
          if layer is None:
            raise IndexError('There are not any layers named %s in the incoming subgraph.' % item)

          results.append(layer)
        else:
          matches = [incoming for incoming in incomings if incoming.name == item]
          if len(matches) == 0:
            raise IndexError('There are not any layers named %s among inputs' % item)
          else:
            results.extend(matches)
      else:
        raise ValueError('Items must be intergers, slices or layer names, got %s' % (item, ))


    return results
  return selector

def _with_inputs(*items, search_subgraph=False):
  def contructor(*definition):
    op = achain(*definition)

    def subnet(*incomings):
      selected_incomings = _selector(*items, search_subgraph=search_subgraph)(*incomings)
      is_selected = [
        incoming in selected_incomings
        for incoming in incomings
      ]

      op_results = op(*selected_incomings)

      if not isinstance(op_results, list) and not isinstance(op_results, tuple):
        op_results = (op_results, )
      else:
        op_results = tuple(op_results)

      if len(op_results) < len(selected_incomings):
        op_results = op_results + (None, ) * (len(items) - len(op_results))

      op_results_indx = 0
      results = []

      for i in range(len(incomings)):
        if is_selected[i]:
          results.append(op_results[op_results_indx])
          op_results_indx += 1
        else:
          results.append(incomings[i])

      n = len(selected_incomings)
      results.extend(op_results[n:])

      return [
        result
        for result in results
        if result is not None
      ]

    return subnet
  return contructor

class WithInputs(object):
  def __init__(self, search_subgraph=False):
    self.search_subgraph = search_subgraph

  def __call__(self, *items):
    return _with_inputs(*items, search_subgraph=self.search_subgraph)

  def __getitem__(self, items):
    if not isinstance(items, tuple):
      items = (items, )

    return _with_inputs(*items, search_subgraph=self.search_subgraph)


with_inputs = WithInputs(search_subgraph=False)


class Select(object):
  def __init__(self, search_subgraph=False):
    self.search_subgraph = search_subgraph

  def __call__(self, *items):
    def constructor(*definition):
      return achain(
        _selector(*items, search_subgraph=self.search_subgraph),
        *definition
      )

    return constructor

  def __getitem__(self, items):
    if not isinstance(items, tuple):
      items = (items, )

    return self(*items)

select = Select(search_subgraph=False)
seek = Select(search_subgraph=True)