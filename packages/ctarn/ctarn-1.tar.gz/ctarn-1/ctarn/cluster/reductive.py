import networkx as nx

from ctarn.cluster.dendrogram import Leaf, Dendrogram as Dend


class ReductiveClustering:
    graph = None
    links = None
    dend = None

    def __init__(self, selector, connector, pre_connector=None):
        self.select = selector
        self.connect = connector
        self.pre_connect = pre_connector

    def fit(self, graph):
        if type(graph) is nx.DiGraph:
            self.graph = graph
        else:
            self.graph = nx.empty_graph(len(graph), create_using=nx.DiGraph)
            for node, nbrs in enumerate(graph):
                self.graph.add_weighted_edges_from([(node, nbr, idx) for idx, nbr in enumerate(nbrs)])

        self.links = nx.empty_graph(self.graph.nodes, create_using=nx.DiGraph)

        if self.pre_connect is not None:
            self.graph = self.pre_connect(set(self.graph.nodes), graph=self.graph)
        self.dend = Dend([self._cluster(self.graph.subgraph(s)) for s in nx.strongly_connected_components(self.graph)])
        self.dend.clean()
        return self

    def _cluster(self, graph):
        rep = self.select(graph=graph)  # representatives
        if len(rep) == 0 or len(rep) == len(graph.nodes):
            root = self._link(list(graph.nodes))
            return Leaf(map(lambda node: int(node), [root] + list(nx.descendants(self.links, root))))
        else:
            self._link(rep, graph)
            graph = self.connect(nodes=rep, graph=graph.subgraph(rep))
            return Dend([self._cluster(graph.subgraph(s)) for s in nx.strongly_connected_components(graph)])

    def _link(self, nodes, graph=None):
        if graph is None:
            root = nodes.pop()
            self.links.add_edges_from([(root, node) for node in nodes])
            return root
        else:
            for node in set(graph.nodes) - nodes:
                for u, v in nx.bfs_edges(graph, node):
                    if v in nodes:
                        self.links.add_edge(v, node)
                        break
                else:
                    raise RuntimeError(f'failed to link {node} to another node: not found; it should not happen.')
