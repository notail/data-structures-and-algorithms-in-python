#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Stack implementation

Author: JerryWoo
Date: 2018-07-18
"""

class EmptyException(Exception):
    pass

class ArrayStack:
    """LIFO stack implementation using a python list as underlying storage
    """

    def __init__(self):
        """Create an empty stack
        """
        self._data = []
    
    def __len__(self):
        """Return the number of elements in the stack
        """
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty
        """
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack
        """
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return then element from the top of this stack

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data.pop()
