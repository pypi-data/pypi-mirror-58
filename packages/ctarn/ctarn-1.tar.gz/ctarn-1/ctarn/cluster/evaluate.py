import numpy as np
from sklearn import metrics


class PartitionEvaluation:
    def __init__(self, labels_true, labels_pred, name=None):
        self.labels_true = labels_true
        self.labels_pred = labels_pred
        self.name = name
        self.n_true = len(np.unique(labels_true))
        self.n_pred = len(np.unique(labels_pred))
        self.ari = metrics.adjusted_rand_score(labels_true, labels_pred)
        self.ami = metrics.adjusted_mutual_info_score(labels_true, labels_pred)
        self.nmi = metrics.normalized_mutual_info_score(labels_true, labels_pred)

    def __str__(self):
        return ' '.join([
            f'{self.name + ": " if self.name is not None else ""}',
            f'N={self.n_pred:4d}/{self.n_true:4d}',
            f'ARI={self.ari:6.4f}',
            f'AMI={self.ami:6.4f}',
            f'NMI={self.nmi:6.4f}',
        ])
