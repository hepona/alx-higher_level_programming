#!/usr/bin/python3
"""define a class"""


class Node:
    """define Node attribute"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""define SinglyLinkedList class"""


class SinglyLinkedList:
    """define SinglyLinkedList attribute"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        nw_node = Node(value)
        if self.__head is None or nw_node.data >= self.__head.data:
            nw_node.next_node = None
            self.__head = nw_node
        else:
            self.__head.next_node = nw_node
            nw_node.next_node = None
