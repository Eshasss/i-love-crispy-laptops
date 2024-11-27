import unittest
from tree import Node, Set, Dict, Compare, Comparable

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(8)
        self.node.add(4)
        self.node.add(7)
        self.node.add(23)
        self.node.add(12)

    def test_add(self):
        self.node.add(10)
        self.assertTrue(self.node.search(10))

    def test_search(self):
        self.assertIsNotNone(self.node.search(7))
        self.assertIsNone(self.node.search(100))

    def test_correct(self): # не очень понятно как тесты писать но ок
        self.assertTrue(self.node.correct())

    def test_delete(self):
        self.node.delete(7)
        self.assertIsNone(self.node.search(7))

    def test_to_list(self):
        self.assertEqual(self.node.to_list(), [4, 7, 8, 12, 23])

    def test_merge(self):
        node2 = Node(12)
        node2.add(6)
        node2.add(10)
        node2.add(38)
        node2.add(3)
        node2.add(2)
        self.node.merge(node2)
        self.assertTrue(self.node.correct())
        self.assertEqual(self.node.to_list(), [2, 3, 4, 6, 7, 8, 10, 12, 23, 38])

class TestSet(unittest.TestCase):

    def setUp(self):
        self.set1 = Set([1, 2, 3])
        self.set2 = Set([3, 4, 5])

    def test_add(self):
        self.set1.add(4)
        self.assertIn(4, self.set1)

    def test_delete(self):
        self.set1.delete(2)
        self.assertNotIn(2, self.set1)

    def test_union(self):
        union_set = self.set1 | self.set2
        self.assertEqual(union_set.node.to_list(), [3])

    def test_intersection(self):
        intersection_set = self.set1 & self.set2
        self.assertEqual(intersection_set.node.to_list(), [1, 2, 3, 4, 5])

    def test_is_subset(self):
        self.assertTrue(self.set1.is_subset(self.set2))
        self.assertFalse(self.set2.is_subset(self.set1))

    def test_is_empty(self):
        empty_set = Set([])
        self.assertTrue(empty_set.is_empty())
        self.assertFalse(self.set1.is_empty())

class TestDict(unittest.TestCase):

    def setUp(self):
        self.dict1 = Dict([('hello', 1), ('world', [1, 2, 3]), ('how', 123.5), ('are', 'you')])

    def test_add(self):
        self.dict1.node.add(('new', 'value'))
        self.assertIn('new', self.dict1)

    def test_delete(self):
        self.dict1.node.delete(('hello', 1))
        self.assertNotIn('hello', self.dict1)

    def test_search(self):
        self.assertTrue(self.dict1.search_tuple(self.dict1.node, 'world'))
        self.assertFalse(self.dict1.search_tuple(self.dict1.node, 'hochu_spat'))

if __name__ == '__main__':
    unittest.main()