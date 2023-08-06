import networkx as nx
import numpy as np


def graph_nbrs(graph):
    return {node: list(graph.succ[node]) + [node] for node in graph}


def smooth_labels(labels, nbrs, n=1):
    if type(nbrs) is nx.DiGraph:
        nbrs = graph_nbrs(nbrs)
    for _ in range(n):
        labels = np.array([np.bincount(labels[nbrs[node]]).argmax() for node in range(len(labels))], dtype=int)
    return list(labels)


def smooth_dendrogram(dend, nbrs, n=1):
    if type(nbrs) is nx.DiGraph:
        nbrs = graph_nbrs(nbrs)
    labels = np.array(smooth_labels(np.array(dend.label()), nbrs, n=n), dtype=int)
    for i, leaf in enumerate(dend.leaves):
        leaf.clear()
        leaf.extend([int(node) for node in np.arange(len(labels))[labels == i]])
    dend.clean()
