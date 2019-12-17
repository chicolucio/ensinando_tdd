import unittest

from core import fatorial
import ddt


@ddt.ddt
class FatorialTest(unittest.TestCase):
    @ddt.data(fatorial.fatorial_for, fatorial.fatorial_while, fatorial.fatorial_recursivo)
    def test_0(self, param):
        self.assertEqual(param(0), 1)

    @ddt.data(fatorial.fatorial_for, fatorial.fatorial_while, fatorial.fatorial_recursivo)
    def test_1(self, param):
        self.assertEqual(param(1), 1)

    @ddt.data(fatorial.fatorial_for, fatorial.fatorial_while, fatorial.fatorial_recursivo)
    def test_3(self, param):
        self.assertEqual(param(3), 6)

    @ddt.data(fatorial.fatorial_for, fatorial.fatorial_while, fatorial.fatorial_recursivo)
    def test_5(self, param):
        self.assertEqual(param(5), 120)

    def test_neg1(self):
        with self.assertRaises(ValueError):
            fatorial.fatorial_for(-1)
            fatorial.fatorial_while(-1)
            fatorial.fatorial_recursivo(-1)

    def test_float_2(self):
        with self.assertRaises(ValueError):
            fatorial.fatorial_for(2.0)
            fatorial.fatorial_while(2.0)
            fatorial.fatorial_recursivo(2.0)
