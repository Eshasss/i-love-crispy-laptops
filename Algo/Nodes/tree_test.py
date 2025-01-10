import unittest
from tree import Node, Set, Dict, Compare, Comparable
from avltree import AVLNode, AVLSet, AVLDict

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(8)
        self.node.add(4)
        self.node.add(7)
        self.node.add(23)
        self.node.add(12)
        self.node.add(2)
        self.node.add(3)
        self.node.add(1)
        self.node.add(28)
        self.node.add(41)
        self.node.add(13)

    def test_add(self):
        self.node.add(10)
        self.assertTrue(self.node.search(10))

    def test_search(self):
        self.assertIsNotNone(self.node.search(7))
        self.assertIsNone(self.node.search(100))

    def test_correct(self): # не очень понятно как тесты писать но ок. Здесь верное дерево??
        self.assertTrue(self.node.correct())

    def test_delete_leave(self):
        self.node.delete(13) 
        print(self.node)
        self.assertIsNone(self.node.search(13))

    def test_delete_one_child(self):
        self.node.delete(28) 
        self.assertIsNone(self.node.search(28))

    def test_delete_two_child(self):
        self.node.delete(2) 
        self.assertIsNone(self.node.search(2))

    def test_delete_root(self):
        self.node.delete(8) 
        self.assertIsNone(self.node.search(8))
    

    def test_to_list(self):
        self.assertEqual(self.node.to_list(), [1, 2, 3, 4, 7, 8, 12, 13, 23, 28, 41])

    def test_merge(self):
        node2 = Node(12)
        node2.add(6)
        node2.add(10)
        node2.add(38)
        node2.add(3)
        node2.add(2)
        self.node.merge(node2)
        self.assertTrue(self.node.correct())
        self.assertEqual(self.node.to_list(), [[1, 2, 3, 4, 7, 8, 10, 12, 13, 23, 28, 38, 41]])

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
        self.dict1.node.add(('bla', 'pupupu'))
        self.assertIn('bla', self.dict1)

    def test_delete(self):
        self.dict1.node.delete(('hello', 1))
        self.assertNotIn('hello', self.dict1)

    def test_search(self):
        self.assertTrue(self.dict1.search_tuple(self.dict1.node, 'world'))
        self.assertFalse(self.dict1.search_tuple(self.dict1.node, 'hochu_spat'))


class TestAVLSet(unittest.TestCase):
    
    def test_add(self):
        avl_set = AVLSet([5, 10, 15])
        avl_set.add(20)
        self.assertIn(20, avl_set)
        self.assertIsNotNone(avl_set.node.search(20))
    
    def test_delete(self):
        avl_set = AVLSet([5, 10, 15, 20])
        avl_set.delete(10)
        self.assertNotIn(10, avl_set)
        self.assertIsNone(avl_set.node.search(10))
    
    def test_merge(self):
        avl_set1 = AVLSet([5, 10, 15])
        avl_set2 = AVLSet([20, 25, 30])
        avl_set1.node.merge(avl_set2.node)
    
        for val in [20, 25, 30]:
            self.assertIn(val, avl_set1)
            self.assertIsNotNone(avl_set1.node.search(val))
    
    def test_is_subset(self):
        avl_set1 = AVLSet([5, 10, 15, 20])
        avl_set2 = AVLSet([10, 15])
        self.assertTrue(avl_set2.is_subset(avl_set1))
        
        avl_set3 = AVLSet([25, 30])
        self.assertFalse(avl_set3.is_subset(avl_set1))
    
    def test_is_empty(self):
        avl_set = AVLSet([5, 10, 15])
        self.assertFalse(avl_set.is_empty())
        
        empty_set = AVLSet([])
        self.assertTrue(empty_set.is_empty())

class TestAVLNode(unittest.TestCase):
    def setUp(self):
        self.node = AVLNode(2)
        self.node.add(1)
        self.node.add(3)
        
    def test_delete(self):
        root = AVLNode(10)
        root.add(5)
        root.add(15)
        
        root.delete(5)
        self.assertIsNone(root.search(5))
        self.assertIsNotNone(root.search(10))
    
    def test_balance_after_delete(self):
        root = AVLNode(10)
        root.add(5)
        root.add(15)
        root.add(20)
        root.delete(15)
        self.assertTrue(root.correct())  
    
    def test_merge(self):
        root1 = AVLNode(10)
        root1.add(5)
        root1.add(15)
        root2 = AVLNode(20)
        root2.add(25)
        root2.add(30)
        root1.merge(root2)
        self.assertIsNotNone(root1.search(20))
        self.assertIsNotNone(root1.search(25))
        self.assertIsNotNone(root1.search(30))



if __name__ == "__main__":
    unittest.main()