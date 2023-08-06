from abc import ABCMeta, abstractmethod

import numpy as np


class Selector(metaclass=ABCMeta):
    def __init__(self, rate=None, thres=None):
        self.rate = rate
        self.thres = thres

    def __call__(self, graph, **kwargs):
        if kwargs.get('rate') is None and kwargs.get('thres') is None:
            kwargs['rate'], kwargs['thres'] = self.rate, self.thres

        if kwargs.get('rate') is None and kwargs.get('thres') is None:
            raise ValueError('neither thres nor rate has been specified.')
        elif kwargs.get('rate') is not None and kwargs.get('thres') is not None:
            raise Warning('both rate and thres are specified; rate will be ignored.')

        return self._select(graph, **kwargs)

    def _select(self, graph, **kwargs):
        scores = self.measure(graph, **kwargs)
        thres = kwargs.get('thres')
        if thres is None:
            if kwargs['rate'] <= 0:
                return set()
            if kwargs['rate'] >= 1:
                return scores.keys()
            n = int(len(scores) * (1 - kwargs['rate']))
            thres = np.partition(np.array(list(scores.values())), n)[n]
        return set(filter(lambda item: scores[item] >= thres, scores.keys()))

    @abstractmethod
    def measure(self, graph, **kwargs):
        pass


class RandomSelector(Selector):
    def measure(self, graph, **kwargs):
        return {node: np.random.random() for node in graph.nodes}


class IndegreeSelector(Selector):
    def measure(self, graph, **kwargs):
        return dict(graph.in_degree)


class MutualNeighborSelector(Selector):
    def measure(self, graph, **kwargs):
        return {node: len([nbr for nbr in graph.succ[node] if graph.has_edge(nbr, node)]) for node in graph.nodes}
