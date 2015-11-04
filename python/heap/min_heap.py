#!/usr/bin/python

import math, sys

class MinHeap(object):
    def __init__(self):
        # The underlying data
        self._data = []
        return

    def get_min(self):
        # Returns the smallest element
        if self._data:
            return self._data[0]

        return None

    def extract_min(self):
        self._heapify()
        return

    def _heapify_up(self):
        # The last element was just added - ensure it satisfies the min heap property
        currIdx = len(self._data) - 1

        done = False
        while not done:
            parentIdx = self._parent(currIdx)
            if currIdx == 0 or self._data[parentIdx] <= self._data[currIdx]:
                done = True
                break

            # We need to swap the parent and the current index
            currVal = self._data[currIdx]
            parentVal = self._data[parentIdx]

            self._data[parentIdx] = currVal
            self._data[currIdx] = parentVal

            currIdx = parentIdx
        return

    def _heapify_down(self, currIdx):
        done = False
        while not done:
            leftIdx = self._left(currIdx)
            rightIdx = self._right(currIdx)

            leftVal = None
            if len(self._data) > leftIdx:
                leftVal = self._data[leftIdx]

            rightVal = None
            if len(self._data) > rightIdx:
                rightVal = self._data[rightIdx]

            # Is this a leaf?
            if not leftVal and not rightVal:
                done = True
                return

            minVal = None
            minIdx = None
            if leftVal and not rightVal:
                minVal = leftVal
                minIdx = leftIdx
            else:
                if leftVal > rightVal:
                    minVal = rightVal
                    minIdx = rightIdx
                else:
                    minVal = leftVal
                    minIdx = leftIdx

            currVal = self._data[currIdx]

            if currVal > minVal:
                # Charlie, we need a swap in here.
                self._data[minIdx] = currVal
                self._data[currIdx] = minVal

                self._heapify_down(minIdx)
            else:
                break
        return

    def insert(self, value):
        # append at the very end
        self._data.append(value)
       
        # Please fix this node 
        currIdx = len(self._data) - 1
        self._heapify_up()
        return

    def delete(self, value):
        if not self._data:
            # Nothing to do here
            return

        # Change that value into 
        idx = self._data.index(value)
        self._data[idx] = self._data.pop()

        self._heapify_down(idx)

        pass

    def _parent(self, index):
        # The parent will always exist
        return int(math.floor((index-1)/2))

    def _left(self, index):
        return 2*index + 1

    def _right(self, index):
        return 2*index + 2
