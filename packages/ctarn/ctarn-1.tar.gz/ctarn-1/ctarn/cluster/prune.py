from ctarn.cluster.dendrogram import Leaf, Dendrogram


class SimpleSoftPruner:
    def __call__(self, dend: Dendrogram, n: int):
        dend.clean()
        while len(dend.leaves) > n:
            leaf = min(dend.leaves, key=lambda x: x.size)
            pred = leaf.pred
            pred.remove(leaf)
            bro = min(pred, key=lambda x: x.size)
            if type(bro) is Leaf:
                bro.extend(leaf)
            else:  # Dend
                bro.append(leaf)
            if len(pred) == 1 and pred.pred is not None:
                pred.pred.append(bro)
                pred.pred.remove(pred)
        return dend


class SimpleHardPruner:
    def __call__(self, dend: Dendrogram, n: int, rate=0.8):
        dend.clean()
        top_n_thres = dend.size * rate
        while True:
            leaves = sorted(dend.leaves, key=lambda x: x.size, reverse=True)
            top_n = sum([leaf.size for _, leaf in zip(range(n), leaves)])
            if top_n > top_n_thres:
                break
            end_branches = dend.end_branches
            if len(end_branches) == 0:
                break
            branch = min(end_branches, key=lambda x: x.size)
            if len(leaves) + 1 - len(branch) < n:
                break
            pred = branch.pred
            pred.remove(branch)
            pred.append(Leaf(branch.items))
        return dend
