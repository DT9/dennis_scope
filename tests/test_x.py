import unittest
from .context import src


class XTest(unittest.TestCase):

    def test_constructor_size(self):
        # user enters no number
        x = src.X()
        self.assertEqual(x.size, 1)
        # user enters a postive number
        size = 3
        x = src.X(size)
        self.assertEqual(x.size, size)

    def test_x_of_size_3(self):
        x = src.X()
        x.build(3)
        result = (
            "*       *\n"
            "  *   *\n"
            "    *\n"
            "  *   *\n"
            "*       *"
        )
        self.assertEqual(x.pretty_x,result)

    def test_build_middle(self):
        size = 3
        x = src.X()
        result = "    *"
        middle = x._build_middle(size)
        self.assertEqual(result,middle)
        
    def test_negative(self):
        # user enters a negative number
        x = src.X(-9)
        self.assertEqual("*",x.pretty_x)

if __name__ == '__main__':
    unittest.main()
