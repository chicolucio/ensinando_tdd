import unittest

from core import par


class TestPar(unittest.TestCase):
    def test_e_par_2(self):
        self.assertTrue(par.e_par(2))

    def test_e_par_neg4(self):
        self.assertTrue(par.e_par(-4))

    def test_e_par_3(self):
        self.assertFalse(par.e_par(3))

    def test_e_par_neg3(self):
        self.assertFalse(par.e_par(-3))

    def test_e_par_0(self):
        self.assertTrue(par.e_par(0))

    def test_e_par_string(self):
        self.assertRaises(TypeError, par.e_par, 'string')

    def test_e_par_float(self):
        self.assertRaises(TypeError, par.e_par, 2.5)
