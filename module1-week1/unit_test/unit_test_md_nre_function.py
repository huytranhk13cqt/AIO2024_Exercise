import unittest

from practice_exercise.md_nre_function import validate_input, mean_difference_nth_root_error


class TestMathFunctions(unittest.TestCase):

    # Test validate_input function with valid inputs
    def test_validate_input_valid(self):
        try:
            validate_input(1, 1, 2, 3)
        except ValueError:
            self.fail("validate_input() raised ValueError unexpectedly")

    # Test validate_input function with invalid y
    def test_validate_input_invalid_y(self):
        with self.assertRaises(ValueError) as context:
            validate_input("a", 1, 2, 3)
        self.assertEqual(str(context.exception), "y must be numeric value")

    # Test validate_input function with invalid y_hat
    def test_validate_input_invalid_y_hat(self):
        with self.assertRaises(ValueError) as context:
            validate_input(1, "a", 2, 3)
        self.assertEqual(str(context.exception), "y_hat must be numeric value")

    # Test validate_input function with invalid n
    def test_validate_input_invalid_n(self):
        with self.assertRaises(ValueError) as context:
            validate_input(1, 1, -2, 3)
        self.assertEqual(str(context.exception), "n must be a positive numeric value")
        with self.assertRaises(ValueError) as context:
            validate_input(1, 1, "a", 3)
        self.assertEqual(str(context.exception), "n must be numeric value")

    # Test validate_input function with invalid p
    def test_validate_input_invalid_p(self):
        with self.assertRaises(ValueError) as context:
            validate_input(1, 1, 2, -3)
        self.assertEqual(str(context.exception), "p must be a positive numeric value")
        with self.assertRaises(ValueError) as context:
            validate_input(1, 1, 2, "a")
        self.assertEqual(str(context.exception), "p must be numeric value")

    # Test mean_difference_nth_root_error function
    def test_mean_difference_nth_root_error(self):
        self.assertAlmostEqual(mean_difference_nth_root_error(4, 1, 2, 2), 3 ** 2)
        self.assertAlmostEqual(mean_difference_nth_root_error(8, 1, 3, 3), (2 - 1) ** 3)


if __name__ == '__main__':
    unittest.main()
