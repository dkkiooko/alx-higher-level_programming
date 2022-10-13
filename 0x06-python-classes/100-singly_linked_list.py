#!/usr/bin/python3
class Node:
    """defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """instantiate a Node object

        Args:
            data (int): data stored in new Node
            next_node (Node, optional): either of two nodes connected
                to current Node. Defaults to None.
        """
        self.data = (data)
        self.next_node = (next_node)

    @property
    def data(self):
        """retrieve data stored in Node

        Returns:
            int: integer stored in Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data

        Args:
            data (int): integer to set in Node

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next Node

        Returns:
            Node: Node next to current node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the next Node

        Args:
            next_node (Node): Node that is next to current Node

        Raises:
            TypeError: Node must be connected to Node obj or None
        """
        if (not isinstance(value, Node)) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """singly linked list
    """
    def __init__(self):
        """head of linked list is None

        Args:
            data (int): value stored in particular Node
            next_node (Node, optional): Node object
                in linked list. Defaults to None.
        """
        self.__head = None

    def __str__(self):
        """string of all values stored in linked list

        Returns:
            str: all the elements in linked list on a new line
        """
        ret = ""
        node = self.__head
        while node:
            ret += str(node.data) + "\n"
            node = node.next_node
        return ret[:-1]

    def sorted_insert(self, value):
        """insert elements in linked list in ascending order

        Args:
            value (int): a number stored in a Node
        """
        New = Node(value)
        temp = self.__head
        if temp is None:
            self.__head = New
            return

        if value < temp.data:
            New.next_node = self.__head
            self.__head = New
            return

        while (temp.next_node and (value > temp.next_node.data)):
            temp = temp.next_node
        New.next_node = temp.next_node
        temp.next_node = New
