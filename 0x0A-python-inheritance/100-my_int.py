#!/usr/bin/python3
"""define a class MyInt"""
class MyInt(int):
    """define it's attribute"""
    def __init__(self):
        super().__init__()
    def __eq__(self, other):
        if isinstance(other, MyInt):
            return super().__eq__(other)
        return False

    def __ne__(self, other):
        if isinstance(other, MyInt):
            return super().__ne__(other)
        return True
