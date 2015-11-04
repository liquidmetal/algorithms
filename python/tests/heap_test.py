from heap.min_heap import MinHeap
import unittest

class MinHeapTests(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def tearDown(self):
        self.heap = None

    def test_insert1(self):
        self.heap.insert(5)
        self.assertEquals(self.heap._data, [5])

        self.heap.insert(10)
        self.assertEquals(self.heap._data, [5, 10])

        self.heap.insert(2)
        self.assertEquals(self.heap._data, [2, 10, 5])

        self.heap.insert(1)
        self.assertEquals(self.heap._data, [1, 2, 5, 10])

        self.heap.insert(100)
        self.assertEquals(self.heap._data, [1, 2, 5, 10, 100])

    def test_insert2(self):
        self.heap.insert(100)
        self.assertEquals(self.heap._data, [100])

        self.heap.insert(99)
        self.assertEquals(self.heap._data, [99, 100])

        self.heap.insert(98)
        self.assertEquals(self.heap._data, [98, 100, 99])

        self.heap.insert(97)
        self.assertEquals(self.heap._data, [97, 98, 99, 100])

        self.heap.insert(96)
        self.assertEquals(self.heap._data, [96, 97, 99, 100, 98])

        self.heap.insert(95)
        self.assertEquals(self.heap._data, [95, 97, 96, 100, 98, 99])

        self.heap.insert(94)
        self.assertEquals(self.heap._data, [94, 97, 95, 100, 98, 99, 96])

        self.heap.insert(93)
        self.assertEquals(self.heap._data, [93, 94, 95, 97, 98, 99, 96, 100])

        self.heap.insert(92)
        self.assertEquals(self.heap._data, [92, 93, 95, 94, 98, 99, 96, 100, 97])

        self.heap.insert(101)
        self.heap.insert(102)
        self.heap.insert(103)
        self.heap.insert(104)
        self.heap.insert(105)
        self.heap.insert(106)
        self.assertEquals(self.heap._data, [92, 93, 95, 94, 98, 99, 96, 100, 97, 101, 102, 103, 104, 105, 106])

        self.heap.insert(90)
        self.assertEquals(self.heap._data, [90, 92, 95, 93, 98, 99, 96, 94, 97, 101, 102, 103, 104, 105, 106, 100])




    def test_delete1(self):
        self.heap.insert(5)
        self.heap.insert(10)
        self.heap.insert(2)
        self.heap.insert(1)
        self.heap.insert(100)

        self.heap.delete(1)
        print self.heap._data

    def test_delete2(self):
        pass
