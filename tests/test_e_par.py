import unittest

from code import par


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
