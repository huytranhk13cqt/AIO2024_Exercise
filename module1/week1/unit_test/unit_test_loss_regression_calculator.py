import math
import unittest
from unittest.mock import patch

from practice_exercise.loss_regression_calculator import valid_input, loss_regression_calculator


class TestLossRegressionCalculator(unittest.TestCase):

    def test_valid_input_valid_inputs(self):
        self.assertEqual(valid_input('10', 'MAE'), (10, 'MAE'))
        self.assertEqual(valid_input('20', 'MSE'), (20, 'MSE'))
        self.assertEqual(valid_input('30', 'RMSE'), (30, 'RMSE'))

    def test_valid_input_invalid_samples(self):
        self.assertEqual(valid_input('abc', 'MAE'), (False, "Number of samples must be an integer"))
        self.assertEqual(valid_input('10.5', 'MSE'), (False, "Number of samples must be an integer"))

    def test_valid_input_invalid_loss_name(self):
        self.assertEqual(valid_input('10', 'XYZ'), (False, "XYZ is not supported"))

    @patch('random.uniform')
    def test_loss_regression_calculator_mae(self, mock_random):
        mock_random.side_effect = [2, 4, 3, 5, 6, 8]  # y_true, y_pred pairs
        result = loss_regression_calculator('3', 'MAE')
        self.assertTrue(result[0])
        self.assertAlmostEqual(result[1], 2.0)

    @patch('random.uniform')
    def test_loss_regression_calculator_mse(self, mock_random):
        mock_random.side_effect = [2, 4, 3, 5, 6, 8]  # y_true, y_pred pairs
        result = loss_regression_calculator('3', 'MSE')
        self.assertTrue(result[0])
        self.assertAlmostEqual(result[1], 4.0)

    @patch('random.uniform')
    def test_loss_regression_calculator_rmse(self, mock_random):
        mock_random.side_effect = [2, 4, 3, 5, 6, 8]  # y_true, y_pred pairs
        result = loss_regression_calculator('3', 'RMSE')
        self.assertTrue(result[0])
        self.assertAlmostEqual(result[1], math.sqrt(4.0))


if __name__ == '__main__':
    unittest.main()
