#!/usr/bin/python


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.median = None

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

        if self.median == None:
            print("First time - setting median to %d" % num)
            self.median = num
            return

        if not self.min_heap and not self.max_heap:
            if num == self.median:
                self.min_heap.append(num)
                self.min_heap.append(self.median)
            elif num < self.median:
                self.max_heap.append(num)
                self.min_heap.append(self.median)
            else:
                self.min_heap.append(num)
                self.max_heap.append(self.median)
        else:
            if self.min_heap and max(self.min_heap) == num:
                self.min_heap.append(num)
            elif self.max_heap and min(self.max_heap) == num:
                self.max_heap.append(num)
            else:
                if num < self.median:
                    self.max_heap.append(num)
                else:
                    self.min_heap.append(num)


        num_max = len(self.max_heap)
        num_min = len(self.min_heap)
        if num_max == num_min:
            self.median = float(max(self.min_heap) + min(self.max_heap)) / 2.0
        else:
            if num_max > num_min:
                self.median = min(self.max_heap)
            else:
                self.median = max(self.min_heap)

        print "Inserting %d" % num
        print "Median = %d" % self.median
        print "max_heap = %s" % self.max_heap
        print "min_heap = %s" % self.min_heap
        return

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return self.median

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(0)
mf.addNum(0)
mf.addNum(1)
mf.addNum(1)
mf.addNum(0)
mf.addNum(0)
mf.addNum(1)
mf.addNum(0)
mf.addNum(1)
print(mf.findMedian())
