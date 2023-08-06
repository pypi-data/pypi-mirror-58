#!/usr/bin/env python3

import argparse
import os

import numpy as np
import scipy.io as sio
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
from sklearn.neighbors import NearestNeighbors

from ctarn.util.visualize import draw_labels


def save_dataset(path, dataset):
    feat = dataset['feat']
    label = dataset['label']
    if not os.path.isdir(path):
        os.makedirs(path)
    print(f'{path}: {{feat:{feat.shape}, label:{label.shape}, N:{len(np.unique(label))}}}...', end=' ', flush=True)
    np.save(os.path.join(path, 'feat.npy'), feat)
    np.save(os.path.join(path, 'label.npy'), label)
    sio.savemat(os.path.join(path, 'data.mat'), dataset)
    print('saved.')


def save_array(path, array):
    path += '.npy'
    np.save(path, array)
    print(f'{path} saved.')


def load_array(path):
    path += '.npy'
    return np.load(path) if os.path.isfile(path) else None


def save_fig(path, fig):
    path += '.png'
    fig.savefig(path)
    print(f'{path} saved.')


def download(name):
    name, version = name.split("@")
    dataset = fetch_openml(name, version=version)
    labels = -np.ones(len(dataset.target), dtype=int)
    for idx, label in enumerate(np.unique(dataset.target)):
        labels[dataset.target == label] = idx
    return dict(name=dataset.details['name'], feat=dataset.data, label=labels)


def sample(path, n):
    feat, label = np.load(os.path.join(path, 'feat.npy')), np.load(os.path.join(path, 'label.npy'))
    assert feat.shape[0] == label.shape[0]
    c = np.random.choice(feat.shape[0], n, replace=False)
    return dict(feat=feat[c], label=label[c])


def knn(path, k):
    feat = np.load(os.path.join(path, 'feat.npy'))
    print(f'{path}: building {k}-nn graph...')
    return NearestNeighbors(n_neighbors=k, n_jobs=-1).fit(feat).kneighbors(return_distance=False)


def tsne(path, dim):
    feat = np.load(os.path.join(path, 'feat.npy'))
    print(f'{path}: running t-sne(dim={dim})...')
    return TSNE(n_components=dim, n_jobs=-1).fit_transform(feat)


def main():
    parser = argparse.ArgumentParser(description='Dataset Helper')
    subparsers = parser.add_subparsers(dest='cmd', help='command')

    parser_get = subparsers.add_parser('get', help='download datasets')
    parser_get.add_argument('--dst', type=str, default='data.tmp', metavar='path', help='output directory')
    parser_get.add_argument('names', type=str, nargs='+', metavar='name', help='fetch from https://www.openml.org')

    parser_sample = subparsers.add_parser('sample', help='generate subsets')
    parser_sample.add_argument('num', type=int, help='target size')
    parser_sample.add_argument('paths', nargs='+', metavar='path', help='source datasets')

    parser_graph = subparsers.add_parser('graph', help='construct similarity graphs')
    parser_graph.add_argument('k', type=str, metavar='start[:stop[:step]]', help='size of k-nn graph')
    parser_graph.add_argument('paths', nargs='+', metavar='path', help='source datasets')

    parser_reduce = subparsers.add_parser('reduce', help='reduce to low dimensions')
    parser_reduce.add_argument('dim', type=int, help='target dimension')
    parser_reduce.add_argument('paths', nargs='+', metavar='path', help='source datasets')

    parser_show = subparsers.add_parser('show', help='generate layouts')
    parser_show.add_argument('paths', nargs='+', metavar='path', help='source datasets')

    args = parser.parse_args()

    if args.cmd == 'get':
        for name in args.names:
            dataset = download(name)
            save_dataset(os.path.join(args.dst, name), dataset)
    elif args.cmd == 'sample':
        for path in args.paths:
            dataset = sample(path, args.num)
            save_dataset(os.path.join(path, str(args.num)), dataset)
    elif args.cmd == 'graph':
        k = [int(n) for n in args.k.split(':')]
        ks = k if len(k) == 1 else list(range(*k))
        for path in args.paths:
            nn = knn(path, max(ks))
            for k in ks:
                save_array(os.path.join(path, f'knn-{k}'), nn[:, :k])
    elif args.cmd == 'reduce':
        for path in args.paths:
            feat = tsne(path, args.dim)
            save_array(os.path.join(path, f'tsne-{args.dim}'), feat)
    elif args.cmd == 'show':
        for path in args.paths:
            layout = tsne(path, 2)
            save_array(os.path.join(path, f'layout'), layout)
            labels = load_array(os.path.join(path, 'label'))
            fig = draw_labels(labels, layout)
            save_fig(os.path.join(path, 'layout'), fig)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
