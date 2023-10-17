#!/usr/bin/python3
"""define MyList class"""


class MyList(list):
    """define it attribute"""

    def print_sorted(self):
        self_cp = self.copy()
        self_cp.sort()
        print(self_cp)
