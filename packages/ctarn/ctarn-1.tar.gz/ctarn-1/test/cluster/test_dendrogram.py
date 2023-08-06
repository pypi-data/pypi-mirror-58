import random
from unittest import TestCase

from ctarn.cluster.dendrogram import Leaf, Dendrogram as Dend


class TestLeaf(TestCase):
    def test_size(self):
        n = random.randint(1, 16)
        lst = [random.random() for _ in range(n)]
        self.assertEqual(n, Leaf(lst).size)

    def test_items(self):
        lst = [random.random() for _ in range(random.randint(1, 16))]
        self.assertListEqual(lst, Leaf(lst).items)

    def test___str__(self):
        n = random.randint(1, 16)
        leaf = Leaf([random.random() for _ in range(n)])
        self.assertEqual(f'└── {n}', str(leaf))


class TestDend(TestCase):
    ns = [random.randint(1, 16) for _ in range(8)]
    ls = [Leaf([random.random() for _ in range(n)]) for n in ns]
    d_00 = Dend([ls[0], ls[1]])
    d_0 = Dend([d_00, ls[2], ls[3]])
    d_1 = Dend([ls[4], ls[5]])
    d = Dend([d_0, d_1, ls[6], ls[7]])

    def test_size(self):
        self.assertEqual(sum(self.ns[0:2]), self.d_00.size)
        self.assertEqual(sum(self.ns[0:4]), self.d_0.size)
        self.assertEqual(sum(self.ns[4:6]), self.d_1.size)
        self.assertEqual(sum(self.ns), self.d.size)

    def test_items(self):
        self.assertListEqual(sum([l.items for l in self.ls[0:2]], []), self.d_00.items)
        self.assertListEqual(sum([l.items for l in self.ls[0:4]], []), self.d_0.items)
        self.assertListEqual(sum([l.items for l in self.ls[4:6]], []), self.d_1.items)
        self.assertListEqual(sum([l.items for l in self.ls], []), self.d.items)

    def test_leaves(self):
        self.assertListEqual(self.ls[0:2], self.d_00.leaves)
        self.assertListEqual(self.ls[0:4], self.d_0.leaves)
        self.assertListEqual(self.ls[4:6], self.d_1.leaves)
        self.assertListEqual(self.ls, self.d.leaves)

    def test_end_branches(self):
        self.assertListEqual([self.d_00], self.d_00.end_branches)
        self.assertListEqual([self.d_00], self.d_0.end_branches)
        self.assertListEqual([self.d_1], self.d_1.end_branches)
        self.assertListEqual([self.d_00, self.d_1], self.d.end_branches)

    def test___init__(self):
        for leaf in self.ls[0:2]:
            self.assertEqual(self.d_00, leaf.pred)
        self.assertEqual(self.d_0, self.d_00.pred)
        self.assertEqual(self.d, self.d_0.pred)
        self.assertEqual(self.d, self.d_1.pred)

    def test___setitem__(self):
        ls = [Leaf([n]) for n in range(8)]
        d = Dend([ls[0]])
        d[0] = ls[1]
        self.assertEqual(ls[1], d[0])
        self.assertEqual(None, ls[0].pred)
        self.assertEqual(d, ls[1].pred)
        d = Dend(ls[:4])
        d[1:3] = ls[4:6]
        self.assertListEqual(ls[4:6], d[1:3])
        self.assertListEqual([None, None], [ls[1].pred, ls[2].pred])
        self.assertListEqual([d, d], [ls[4].pred, ls[5].pred])

    def test___delitem__(self):
        ls = [Leaf([n]) for n in range(8)]
        d = Dend(ls)
        del d[0]
        self.assertEqual(7, len(d))
        self.assertEqual(None, ls[0].pred)
        del d[:3]
        self.assertEqual(4, len(d))
        self.assertListEqual([None] * 3, [leaf.pred for leaf in ls[1:4]])

    def test_append(self):
        leaf = Leaf()
        d = Dend()
        d.append(leaf)
        self.assertEqual(leaf, d[-1])
        self.assertEqual(d, leaf.pred)

    def test_insert(self):
        leaf = Leaf()
        d = Dend()
        d.insert(0, leaf)
        self.assertEqual(leaf, d[0])
        self.assertEqual(d, leaf.pred)

    def test_pop(self):
        d = Dend([Leaf()])
        self.assertEqual(d, d[0].pred)
        leaf = d.pop()
        self.assertEqual(0, len(d))
        self.assertEqual(None, leaf.pred)

    def test_remove(self):
        leaf = Leaf()
        d = Dend([leaf])
        self.assertEqual(d, leaf.pred)
        d.remove(leaf)
        self.assertEqual(0, len(d))
        self.assertEqual(None, leaf.pred)

    def test_clear(self):
        leaf = Leaf()
        d = Dend([leaf])
        self.assertEqual(d, leaf.pred)
        d.clear()
        self.assertEqual(0, len(d))
        self.assertEqual(None, leaf.pred)

    def test_copy(self):
        a = Dend([Leaf()])
        b = a.copy()
        self.assertEqual(a, a[0].pred)
        self.assertEqual(b, b[0].pred)

    def test_extend(self):
        d = Dend()
        d.extend([Leaf(), Leaf()])
        self.assertEqual(2, len(d))
        for leaf in d:
            self.assertEqual(d, leaf.pred)

    def test___str__(self):
        expectation = (f'└── {sum(self.ns)}\n'
                       f'    ├── {sum(self.ns[0:4])}\n'
                       f'    │   ├── {sum(self.ns[0:2])}\n'
                       f'    │   │   ├── {self.ns[0]}\n'
                       f'    │   │   └── {self.ns[1]}\n'
                       f'    │   ├── {self.ns[2]}\n'
                       f'    │   └── {self.ns[3]}\n'
                       f'    ├── {sum(self.ns[4:6])}\n'
                       f'    │   ├── {self.ns[4]}\n'
                       f'    │   └── {self.ns[5]}\n'
                       f'    ├── {self.ns[6]}\n'
                       f'    └── {self.ns[7]}')
        self.assertEqual(expectation, str(self.d))

    def test_is_end_branch(self):
        self.assertTrue(self.d_00.is_end_branch())
        self.assertFalse(self.d_0.is_end_branch())
        self.assertTrue(self.d_1.is_end_branch())
        self.assertFalse(self.d.is_end_branch())

    def test_clean(self):
        self.assertEqual(Dend(), Dend([Leaf()]).clean())
        self.assertEqual(Dend(), Dend([Dend([Leaf()])]).clean())
        self.assertEqual(Dend(), Dend([Dend([Leaf()]), Dend([Leaf()])]).clean())
        self.assertEqual(Dend([Leaf([0])]), Dend([Dend([Leaf([0])]), Dend([Leaf()])]).clean())
        self.assertEqual(Dend(), Dend([Leaf(), Leaf(), Leaf()]).clean())

    def test_label(self):
        ls = [Leaf([0, 1]), Leaf([2, 4]), Leaf([3, 5])]
        d = Dend([Dend([ls[0], ls[1]]), ls[2]])
        labels = d.label()
        self.assertEqual([0, 0, 1, 2, 1, 2], labels)
