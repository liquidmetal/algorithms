from trees.trees import BinaryTree
from trees.trees import BinaryTreeNode
import unittest

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        level1_0 = BinaryTreeNode('d')
        level1_1 = BinaryTreeNode('i')

        level2_0 = BinaryTreeNode('b')
        level2_1 = BinaryTreeNode('e')
        level2_2 = BinaryTreeNode('j')
        level2_3 = BinaryTreeNode('m')

        level3_0 = BinaryTreeNode('a')
        level3_1 = BinaryTreeNode('c')
        level3_2 = BinaryTreeNode('f')
        level3_3 = BinaryTreeNode('g')
        level3_4 = BinaryTreeNode('k')
        level3_5 = BinaryTreeNode('l')
        level3_6 = BinaryTreeNode('n')
        level3_7 = BinaryTreeNode('o')

        level1_0.set_left(level2_0)
        level1_0.set_right(level2_1)
        level1_1.set_left(level2_2)
        level1_1.set_right(level2_3)

        level2_0.set_left(level3_0)
        level2_0.set_right(level3_1)
        level2_1.set_left(level3_2)
        level2_1.set_right(level3_3)
        level2_2.set_left(level3_4)
        level2_2.set_right(level3_5)
        level2_3.set_left(level3_6)
        level2_3.set_right(level3_7)

        balanced_tree = BinaryTreeNode('h')
        balanced_tree.set_left(level1_0)
        balanced_tree.set_right(level1_1)

        self.balanced_tree = BinaryTree(balanced_tree)
        return

    def tearDown(self):
        self.balanced_tree = None

    def test_level_order_traversal(self):
        out = self.balanced_tree.traversal_level_order()
        self.assertEquals(out, "hdibejmacfgklno")

    def test_leaf_count(self):
        self.assertEqual(self.balanced_tree.leaf_count(), 8)
