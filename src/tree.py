"""
.. module:: Tree
    :synopsis: module for printing ascii Trees
 
.. moduleauthor:: Dennis Truong
"""
import sys
import argparse


class Tree:
    """Class for printing ascii Tree's

    This class provides some basic methods for instantiating, building, and printing an ascii Tree
    """

    def __init__(self, size=1):
        """A simple initialization method.
        Args:
            Size - height of Tree
        """
        self.x = None
        self.size = size
        self.pretty_tree = None
        self.build(size)

    def _build_line(self, index, size):
        """private method that creates an ascii line based on the height and position.
        Args:
            index - position of tree
            size - height of tree
        """
        spaces = ' ' * (size - (index + 1))
        stars = '*' * (2 * index + 1)
        return spaces + stars

    def _build_tree(self, start, end, step=1):
        """Generates a tree based on the range of an array. 
        Args:
            start - start index
            end - end index
            step - step size
        """
        for i in range(start, end, step):
            yield self._build_line(i, self.size)

    def build(self, size):
        """Public method to build a tree and cache it.
        Args:
            Size - height of tree
        """
        self.size = size
        self.x = self._build_tree(0, size)
        self.pretty_tree = '\n'.join(self.x)

    def print_tree(self):
        """Pretty prints a tree"""
        print(self.pretty_tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="ScopeAR Tree Printer")
    parser.add_argument("height", type=int)
    args = parser.parse_args()
    
    height = args.height
    tree = Tree(height)
    tree.print_tree()
