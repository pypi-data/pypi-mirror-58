#!/usr/bin/env python3

import argparse
import os
import pickle

import numpy as np
from scipy.spatial.distance import euclidean

from ctarn.cluster import BFSConnector, SharedNeighborConnector, StaticConnector
from ctarn.cluster import PartitionEvaluation
from ctarn.cluster import RandomSelector, IndegreeSelector, MutualNeighborSelector
from ctarn.cluster import ReductiveClustering
from ctarn.cluster import SimpleSoftPruner, SimpleHardPruner
from ctarn.cluster import smooth_dendrogram
from ctarn.util.dataset import load_array
from ctarn.util.visualize import draw_labels, draw_dendrogram

SELECTORS = {
    'rand': RandomSelector,
    'id': IndegreeSelector,
    'mn': MutualNeighborSelector,
}
CONNECTORS = {
    'bfs': BFSConnector,
    'sn': SharedNeighborConnector,
    'l2': StaticConnector,
}
PRUNERS = {
    'soft': SimpleSoftPruner,
    'hard': SimpleHardPruner,
}


def main():
    parser = argparse.ArgumentParser(description='Reductive Clustering')
    parser.add_argument('data', type=str, metavar='path')
    parser.add_argument('--selector', choices=SELECTORS.keys(), metavar='name', default='id')
    parser.add_argument('--rate', type=float, metavar='float', default=0.8)
    parser.add_argument('--connector', choices=CONNECTORS.keys(), metavar='name', default='bfs')
    parser.add_argument('--size', type=int, metavar='int', default=16)
    parser.add_argument('--depth', type=int, metavar='int', default=2)
    parser.add_argument('--pruner', choices=PRUNERS.keys(), metavar='name', default='soft')
    parser.add_argument('--no_smooth', action='store_true')
    args = parser.parse_args()

    data_dir = os.path.dirname(args.data)
    name = os.path.basename(data_dir) + '_' + os.path.splitext(os.path.basename(args.data))[0]
    feat = load_array(os.path.join(data_dir, 'feat'))
    gt = load_array(os.path.join(data_dir, 'label'))
    layout = load_array(os.path.join(data_dir, 'layout'))
    graph = load_array(os.path.splitext(args.data)[0])

    conf_str = '_'.join([
        args.selector, 'r' + str(args.rate),
        args.connector, 's' + str(args.size), 'd' + str(args.depth),
        args.pruner,
    ])

    tmp = os.path.join('output.tmp', name, conf_str)
    if not os.path.isdir(tmp):
        os.makedirs(tmp)

    selector = SELECTORS[args.selector](rate=args.rate)
    if args.connector == 'l2':
        connector = StaticConnector(size=args.size, depth=args.depth, metric=lambda a, b: euclidean(feat[a], feat[b]))
    else:
        connector = CONNECTORS[args.connector](size=args.size, depth=args.depth)
    pre_connector = SharedNeighborConnector(size=args.size, depth=args.depth)
    rc = ReductiveClustering(selector=selector, connector=connector, pre_connector=pre_connector).fit(graph)

    def evaluate(dend, method=None):
        def get_path(suffix):
            return os.path.join(tmp, f'{method}.{suffix}')

        title = f'RC ({method})' if method is not None else 'RC'
        print(title)
        pickle.dump(dend, open(get_path('dend.pkl'), 'wb'))
        print(dend)
        labels = dend.label()
        np.save(get_path('labels.npy'), labels)
        if gt is not None:
            evaluation = PartitionEvaluation(gt, labels, name=title)
            pickle.dump(evaluation, open(get_path('eval.pkl'), 'wb'))
            print(evaluation)
        if layout is not None:
            draw_dendrogram(dend, layout, path=get_path('dend.gif'))
            draw_labels(labels, layout, path=get_path('labels.png'))

    evaluate(rc.dend, 'raw')
    if not args.no_smooth:
        smooth_dendrogram(rc.dend, rc.graph, n=16)
        evaluate(rc.dend, 'smooth')

    if gt is not None:
        if layout is not None:
            draw_labels(gt, layout, path=os.path.join(tmp, 'gt.png'))

        prune = PRUNERS[args.pruner]()
        prune(rc.dend, n=len(np.unique(gt)))
        evaluate(rc.dend, 'prune')
        if not args.no_smooth:
            smooth_dendrogram(rc.dend, rc.graph, n=16)
            evaluate(rc.dend, 'prune_smooth')


if __name__ == '__main__':
    main()
