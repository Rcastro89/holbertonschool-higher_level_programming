#!/usr/bin/python3
"""print sorted"""


class MyList(list):
    """class inherits from list"""

    def print_sorted(self):
        """print sorted list"""

        print(sorted(self))
