import math
import unittest

from practice_exercise.approximation import factorial, sin_approximation, cos_approximation, sinh_approximation, \
    cosh_approximation


class TestMathFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(4), 24)
        self.assertTrue(math.isnan(factorial(-1)))

    def test_sin_approximation(self):
        self.assertAlmostEqual(sin_approximation(0, 5), 0, places=5)
        self.assertAlmostEqual(sin_approximation(math.pi / 2, 10), 1, places=5)
        self.assertAlmostEqual(sin_approximation(math.pi, 10), 0, places=5)

    def test_cos_approximation(self):
        self.assertAlmostEqual(cos_approximation(0, 5), 1, places=5)
        self.assertAlmostEqual(cos_approximation(math.pi / 2, 10), 0, places=5)
        self.assertAlmostEqual(cos_approximation(math.pi, 10), -1, places=5)

    def test_sinh_approximation(self):
        self.assertAlmostEqual(sinh_approximation(0, 5), 0, places=5)
        self.assertAlmostEqual(sinh_approximation(1, 10), math.sinh(1), places=5)
        self.assertAlmostEqual(sinh_approximation(-1, 10), math.sinh(-1), places=5)

    def test_cosh_approximation(self):
        self.assertAlmostEqual(cosh_approximation(0, 5), 1, places=5)
        self.assertAlmostEqual(cosh_approximation(1, 10), math.cosh(1), places=5)
        self.assertAlmostEqual(cosh_approximation(-1, 10), math.cosh(-1), places=5)


if __name__ == '__main__':
    unittest.main()
