#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: Dynamic Array

Author: JerryWoo
Date: 2018-07-17
"""

import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list
    """

    def __init__(self):
        """Create an empty array
        """
        # count actual elements
        self._n = 0
        # default array capacity
        self._capacity = 1
        # array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array
        """
        return self._n

    def __getitem__(self, k):
        """Return element at index k
        """
        if k < 0:
            k = self._n + k
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward
        """
        # (for simplicity, we assume 0 <= k <= n in this version)
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)
        """
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')

    def pop(self, *idx):
        """Remove and return item at index (default last)
        """
        if self._n == 0:
            raise IndexError('list is empty')
        if len(idx) > 1:
            raise TypeError('pop() take at most 1 argument but %d given' % len(idx))
        if len(idx) == 0:
            idx = self._n - 1
        else:
            idx = idx[0]
        if idx < 0:
            idx = self._n + idx
        if not 0 <= idx < self._n:
            raise IndexError('index is out of range')
        item = self._A[idx]
        for k in range(idx, self._n - 1):
            self._A[k] = self._A[k + 1]
        self._A[self._n - 1] = None
        self._n -= 1
        return item

    def _resize(self, c):
        """Resize internal array to capacity c
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c


    def _make_array(self, c):
        """Return new array with capacity c
        """
        return (c * ctypes.py_object)()
