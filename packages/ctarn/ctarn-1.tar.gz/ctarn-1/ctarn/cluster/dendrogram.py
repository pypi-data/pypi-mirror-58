from abc import ABCMeta, abstractmethod
from typing import Iterable

import numpy as np


class Node(list, metaclass=ABCMeta):
    pred: None = None

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    def _is_last(self):
        return self.pred is None or self is self.pred[-1]


class Leaf(Node):
    @property
    def size(self):
        return len(self)

    @property
    def items(self):
        return list(self)

    def __str__(self, prefix=''):
        return f'{prefix}{"└" if self._is_last() else "├"}── {len(self)}'


class Dendrogram(Node):
    @property
    def size(self):
        return sum([child.size for child in self])

    @property
    def items(self):
        return sum([child.items for child in self], [])

    @property
    def leaves(self):
        return sum([([child] if type(child) is Leaf else child.leaves) for child in self], [])

    @property
    def end_branches(self):
        return [self] if self.is_end_branch() else sum([c.end_branches for c in self if type(c) is Dendrogram], [])

    def __init__(self, seq: Iterable[Node] = None):
        if seq is None:
            seq = []
        for node in seq:
            node.pred = self
        super(Dendrogram, self).__init__(seq)

    def __setitem__(self, key, value):
        if type(key) is int:
            self[key].pred = None
            value.pred = self
        else:  # slice
            for old, new in zip(self[key], value):
                old.pred = None
                new.pred = self
        return super(Dendrogram, self).__setitem__(key, value)

    def __delitem__(self, key):
        if type(key) is int:
            self[key].pred = None
        else:  # slice
            for item in self[key]:
                item.pred = None
        return super(Dendrogram, self).__delitem__(key)

    def __add__(self, other):
        raise NotImplementedError('addition is not available; use append() or extend() instead.')

    def __iadd__(self, other):
        raise NotImplementedError('addition is not available; use append() or extend() instead.')

    def append(self, item):
        item.pred = self
        return super(Dendrogram, self).append(item)

    def insert(self, i, item):
        item.pred = self
        return super(Dendrogram, self).insert(i, item)

    def pop(self, i=0):
        self[i].pred = None
        return super(Dendrogram, self).pop(i)

    def remove(self, item):
        item.pred = None
        return super(Dendrogram, self).remove(item)

    def clear(self):
        for item in self:
            item.pred = None
        return super(Dendrogram, self).clear()

    def copy(self):
        cp = super(Dendrogram, self).copy()
        for item in cp:
            item.pred = cp
        return cp

    def extend(self, other):
        for item in other:
            item.pred = self
        return super(Dendrogram, self).extend(other)

    def __str__(self, prefix=''):
        line = f'{prefix}{"└" if self._is_last() else "├"}── {len(self.items)}'
        prefix += (' ' if self._is_last() else '│') + '   '
        return '\n'.join([line] + [child.__str__(prefix=prefix) for child in self])

    def is_end_branch(self):
        return np.array([type(child) is Leaf for child in self]).all()

    def clean(self):
        for child in [child for child in self if len(child) == 0]:
            self.remove(child)
        for branch in [child for child in self if type(child) is Dendrogram]:
            branch.clean()
            if len(branch) < 2:
                self.extend(branch)
                self.remove(branch)
        return self

    def label(self):
        labels = -np.ones(self.size, dtype=int)
        for label, leaf in enumerate(self.leaves):
            labels[leaf] = label
        return list(labels)
