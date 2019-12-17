import unittest

from core import fibonacci


class TestFibonacciN(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci.fibonacci_nth(1), 1)

    def test_5(self):
        self.assertEqual(fibonacci.fibonacci_nth(5), 5)

    def test_10(self):
        self.assertEqual(fibonacci.fibonacci_nth(10), 55)
