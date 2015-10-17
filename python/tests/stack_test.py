from stack.stack import Stack
import unittest

class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

        self.stack.push(100)
        self.assertEqual(self.stack.peek(), 100)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEquals(self.stack.pop(), 4)
        self.assertEquals(self.stack.pop(), 3)
        self.assertEquals(self.stack.pop(), 2)
        self.assertEquals(self.stack.pop(), 1)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEquals(self.stack.peek(), 4)
        self.stack.pop()
        self.assertEquals(self.stack.peek(), 3)
        self.stack.pop()
        self.assertEquals(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEquals(self.stack.peek(), 1)
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()
       
    def test_reverse(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)

        self.stack.reverse()

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 5)
