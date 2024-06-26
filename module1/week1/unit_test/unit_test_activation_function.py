import unittest

from practice_exercise.simulate_activation_function import sigmoid_calculator, relu_calculator, elu_calculator, \
    validate_input, activation_function_calculator


class TestActivationFunctionCalculator(unittest.TestCase):
    # Test the sigmoid_calculator function with known values
    def test_sigmoid_calculator(self):
        self.assertAlmostEqual(sigmoid_calculator(0.5), 0.6224593312018546, places=5)
        self.assertAlmostEqual(sigmoid_calculator(-1), 0.2689414213699951, places=5)

    # Test the relu_calculator function with known values
    def test_relu_calculator(self):
        self.assertEqual(relu_calculator(0.5), 0.5)
        self.assertEqual(relu_calculator(-1), 0)

    # Test the elu_calculator function with known values
    def test_elu_calculator(self):
        self.assertEqual(elu_calculator(0.5), 0.5)
        self.assertAlmostEqual(elu_calculator(-1), -0.03160602794142788, places=5)

    # Test the validate_input function with various inputs
    def test_validate_input(self):
        self.assertTrue(validate_input('sigmoid', 0.5))
        self.assertTrue(validate_input('relu', -1))
        self.assertTrue(validate_input('elu', 2))
        self.assertFalse(validate_input('tanh', 0.5))
        self.assertFalse(validate_input('sigmoid', 'a'))

    # Test activation_function_calculator with sigmoid function
    def test_activation_function_calculator_sigmoid(self):
        self.assertAlmostEqual(activation_function_calculator('sigmoid', 0.5), 0.6224593312018546, places=3)
        self.assertAlmostEqual(activation_function_calculator('sigmoid', -1), 0.2689414213699951, places=3)

    # Test activation_function_calculator with relu function
    def test_activation_function_calculator_relu(self):
        self.assertEqual(activation_function_calculator('relu', 0.5), 0.5)
        self.assertEqual(activation_function_calculator('relu', -1), 0)

    # Test activation_function_calculator with elu function
    def test_activation_function_calculator_elu(self):
        self.assertEqual(activation_function_calculator('elu', 0.5), 0.5)
        self.assertAlmostEqual(activation_function_calculator('elu', -1), -0.03160602794142788, places=3)

    # Test activation_function_calculator with an invalid function name
    def test_activation_function_calculator_invalid_func(self):
        with self.assertRaises(SystemExit):
            activation_function_calculator('tanh', 0.5)

    # Test activation_function_calculator with an invalid input
    def test_activation_function_calculator_invalid_input(self):
        with self.assertRaises(SystemExit):
            activation_function_calculator('sigmoid', 'a')


if __name__ == '__main__':
    unittest.main()
