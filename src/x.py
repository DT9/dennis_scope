"""
.. module:: x
    :synopsis: module for printing ascii X's
 
.. moduleauthor:: Dennis Truong
"""
import sys
import argparse


class X:
    """Class for printing ascii X's

    This class provides some basic methods for instantiating, building, and printing an ascii X
    """

    def __init__(self, size=1):
        """A simple initialization method.
        Args:
            Size - height of X
        """
        self.size = size
        self.pretty_x = None
        self.build(size)

    def _build_line(self, index, size):
        """private method that creates an ascii line based on the height and position.
        Args:
            index - position of x
            size - height of x
        """
        left_spaces = ' ' * 2*(size - (index + 1))
        middle_spaces = ' ' * (4*index-1)
        return left_spaces + '*' + middle_spaces + '*'

    def _build_middle(self, size):
        """private method for creating the middle of the X.
        Args:
            Size - height of X
        """
        return ' ' * (2 * (size - 1)) + '*'

    def _gen_pyramid(self, start, end, step=1):
        """Generates a pyramid based on the range of an array
        Args:
            start - start index
            end - end index
            step - step size
        """
        for i in range(start, end, step):
            yield self._build_line(i, self.size)

    def _build_X(self, size):
        """Builds top, middle, and end of the X.
        Args:
            Size - height of X
        """
        yield from self._gen_pyramid(size-1, 0, -1)
        yield self._build_middle(size)
        yield from self._gen_pyramid(1, size)

    def build(self, size):
        """Public method to build X and cache it.
        Args:
            Size - height of X
        """
        self.size = size
        x_list = self._build_X(size)
        self.pretty_x = '\n'.join(x_list)

    def print_x(self):
        """Pretty prints X"""
        print(self.pretty_x)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="ScopeAR X Printer")
    parser.add_argument("height", type=int)
    args = parser.parse_args()

    height = args.height
    x = X(height)
    x.print_x()
