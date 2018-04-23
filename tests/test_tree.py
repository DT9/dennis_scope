import unittest
from .context import src

class TreeTest(unittest.TestCase):

    def test_constructor_size(self):
        # user enters no number
        tree = src.Tree()
        self.assertEqual(tree.size, 1)
        # user enters a postive number
        size = 3
        tree = src.Tree(size)
        self.assertEqual(tree.size, size)

    def test_tree_of_size_3(self):
        tree = src.Tree()
        tree.build(3)
        result = (
            "  *\n"
            " ***\n"
            "*****"
        )
        self.assertEqual(tree.pretty_tree,result)
        
    def test_negative(self):
        # user enters a negative number
        tree = src.Tree(-9)
        self.assertEqual("",tree.pretty_tree)

if __name__ == '__main__':
    unittest.main()
