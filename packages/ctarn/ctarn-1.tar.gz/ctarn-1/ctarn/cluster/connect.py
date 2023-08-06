from abc import ABCMeta, abstractmethod
from collections import OrderedDict

import networkx as nx


class Connector(metaclass=ABCMeta):
    def __init__(self, size=None, depth=None):
        self.size = size
        self.depth = depth

    def __call__(self, nodes, graph, **kwargs):
        kwargs['graph'] = graph
        if kwargs.get('size') is None:
            kwargs['size'] = self.size
        if kwargs.get('depth') is None:
            kwargs['depth'] = self.depth
        return self._connect(nodes, **kwargs)

    def _connect(self, nodes, **kwargs):
        graph = nx.empty_graph(nodes, create_using=nx.DiGraph)
        for node in nodes:
            nbrs = self.search(node, **kwargs)
            nbrs = sorted(nbrs.keys(), key=lambda nbr: nbrs[nbr])
            graph.add_weighted_edges_from([(node, nbr, idx) for idx, nbr in zip(range(kwargs['size']), nbrs)])
        return graph

    def search(self, node, **kwargs):
        nbrs = OrderedDict()
        for _, nbr in nx.bfs_edges(kwargs['graph'], node, depth_limit=kwargs['depth']):
            nbrs[nbr] = self.metric(node, nbr, **kwargs)
        return nbrs

    @abstractmethod
    def metric(self, a, b, **kwargs):
        pass


class BFSConnector(Connector):
    def metric(self, a, b, **kwargs):
        return 1


class SharedNeighborConnector(Connector):
    def metric(self, a, b, **kwargs):
        graph = kwargs['graph']
        union = len(set(graph.succ[a]) | set(graph.succ[b]) | {a, b})
        intersection = graph.out_degree[a] + graph.out_degree[b] + 2 - union
        return - intersection / union


class StaticConnector(Connector):
    def __init__(self, metric=None, size=None, depth=None):
        self.metric_ = metric
        super(StaticConnector, self).__init__(size=size, depth=depth)

    def __call__(self, nodes, graph, **kwargs):
        if kwargs.get('metric') is None:
            kwargs['metric'] = self.metric_
        return super(StaticConnector, self).__call__(nodes, graph, **kwargs)

    def metric(self, a, b, **kwargs):
        return kwargs['metric'](a, b)
