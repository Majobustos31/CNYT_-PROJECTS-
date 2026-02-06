import unittest
import math
from complexlib.libreria_complejos import *

class TestComplexOperations(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(suma((-1, 1), (1, -1)), (0, 0))

    def test_resta(self):
        self.assertEqual(resta((5, 3), (2, 1)), (3, 2))
        self.assertEqual(resta((0, 0), (1, 1)), (-1, -1))

    def test_producto(self):
        self.assertEqual(producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(producto((0, 1), (0, 1)), (-1, 0))

    def test_division(self):
        self.assertAlmostEqual(division((1, 1), (1, -1))[0], 0)
        self.assertAlmostEqual(division((1, 1), (1, -1))[1], 1)

    def test_modulo(self):
        self.assertEqual(modulo((3, 4)), 5)
        self.assertEqual(modulo((0, 0)), 0)

    def test_conjugado(self):
        self.assertEqual(conjugado((3, -4)), (3, 4))
        self.assertEqual(conjugado((0, 5)), (0, -5))

    def test_fase(self):
        self.assertAlmostEqual(fase((1, 1)), math.pi / 4)
        self.assertAlmostEqual(fase((0, 1)), math.pi / 2)

    def test_cartesiano_a_polar(self):
        r, theta = cartesiano_a_polar((1, 0))
        self.assertEqual(r, 1)
        self.assertEqual(theta, 0)

    def test_polar_a_cartesiano(self):
        x, y = polar_a_cartesiano((1, math.pi/2))
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 1)

if __name__ == "__main__":
    unittest.main()