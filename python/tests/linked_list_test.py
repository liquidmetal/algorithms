#!/usr/bin/python

import unittest
from lists.linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def tearDown(self):
        self.ll = None
        pass

    def test_insert(self):
        self.ll.insert(5)
        self.assertEqual(self.ll.toList(), [5])
        self.assertNotEqual(self.ll.toList(), [6])

        self.ll.insert(10)
        self.assertEqual(self.ll.toList(), [5, 10])

    def test_insert_after(self):
        self.ll.insert(5)
        self.ll.insert(10)

        self.ll.insert_after(6, 7)
        self.assertEqual(self.ll.toList(), [5, 7, 10])

        self.ll.insert_after(100, 1000)
        self.assertEqual(self.ll.toList(), [5, 7, 10, 1000])

    def test_delete(self):
        self.ll.insert(5)
        self.ll.delete(5)
        self.assertEqual(self.ll.toList(), [])

        self.ll.insert(10)
        self.ll.insert(100)
        self.ll.insert(1000)
        self.ll.delete(100)
        self.assertEqual(self.ll.toList(), [10, 1000])

        self.ll.delete(1000)
        self.assertEqual(self.ll.toList(), [10])

        self.ll.delete(10)
        self.assertEqual(self.ll.toList(), [])

        self.ll.delete(100)
        self.assertEqual(self.ll.toList(), [])

    def test_delete_at(self):
        self.ll.delete_at(0)
        self.assertEqual(len(self.ll), 0)

        self.ll.insert(5)
        self.ll.delete_at(0)
        self.assertEqual(len(self.ll), 0)

        self.ll.push(10)
        self.ll.push(100)
        self.ll.push(1000)
        self.ll.delete_at(2)
        self.assertEqual(self.ll.toList(), [1000,100])

    def test_length(self):
        self.assertEqual(len(self.ll), 0)

        self.ll.insert(5)
        self.assertEqual(len(self.ll), 1)

        self.ll.insert(5)
        self.assertEqual(len(self.ll), 2)

        self.ll.insert(10)
        self.ll.insert(100)
        self.ll.insert(1000)
        self.ll.delete(100)
        self.assertEqual(len(self.ll), 4)

    def test_contains(self):
        self.assertFalse(5 in self.ll)

        self.ll.insert(5)
        self.assertTrue(5 in self.ll)

        self.ll.push(0)
        self.assertTrue(0 in self.ll)
        self.assertFalse(3 in self.ll)


    def test_push(self):
        self.ll.push(5)
        self.assertEqual(self.ll.toList(), [5])

        self.ll.push(10)
        self.assertEqual(self.ll.toList(), [10, 5])

    def test_pop(self):
        self.ll.push(5)
        self.assertEqual(self.ll.pop(), 5)
        self.assertEqual(self.ll.toList(), [])

        self.ll.push(1)
        self.ll.push(2)
        self.ll.push(3)
        self.ll.push(4)
        self.ll.push(100)
        self.assertEqual(self.ll.pop(), 100)
        self.assertEqual(self.ll.toList(), [4, 3, 2, 1])

    def test_swap_at(self):
        self.ll.push(5)
        self.ll.push(4)
        self.ll.push(3)
        self.ll.push(2)
        self.ll.push(1)

        self.ll.swap_at(1, 3)
        self.assertEqual(self.ll.toList(), [1, 4, 3, 2, 5])

        self.ll.swap_at(0, 4)
        self.assertEqual(self.ll.toList(), [5, 4, 3, 2, 1])

        self.ll.swap_at(0, 1)
        self.assertEqual(self.ll.toList(), [4, 5, 3, 2, 1])

        self.ll.swap_at(4, 3)
        self.assertEqual(self.ll.toList(), [4, 5, 3, 1, 2])

    def test_kth(self):
        self.ll.push(5)
        self.ll.push(4)
        self.ll.push(3)
        self.ll.push(2)
        self.ll.push(1)

        self.assertEqual(self.ll.kth(0), 1)
        self.assertEqual(self.ll.kth(3), 4)

    def test_last_kth(self):
        self.ll.push(5)
        self.ll.push(4)
        self.ll.push(3)
        self.ll.push(2)
        self.ll.push(1)

        self.assertEqual(self.ll.last_kth(1), 5)
        self.assertEqual(self.ll.last_kth(3), 3)

    def test_count(self):
        self.ll.push(5)
        self.ll.push(4)
        self.ll.push(3)
        self.ll.push(5)
        self.ll.push(1)

        self.assertEqual(self.ll.count(1), 1)
        self.assertEqual(self.ll.count(5), 2)

    def test_reverse(self):
        self.ll.push(5)
        self.ll.push(4)
        self.ll.push(3)
        self.ll.push(2)
        self.ll.push(1)

        self.ll.reverse()

        self.assertEqual(self.ll.toList(), [5, 4, 3, 2, 1])
