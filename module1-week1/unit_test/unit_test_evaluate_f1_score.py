import unittest

from practice_exercise.evaluate_f1_score import valid_input_f1_score, evaluate_model_f1_score


class TestF1ScoreFunctions(unittest.TestCase):

    def test_valid_input_f1_score(self):
        self.assertTrue(valid_input_f1_score(11, 5, 3))
        self.assertTrue(valid_input_f1_score(1, 1, 1))

        self.assertFalse(valid_input_f1_score('10', 5, 3))
        self.assertFalse(valid_input_f1_score(10, '5', 3))
        self.assertFalse(valid_input_f1_score(10, 5, '3'))

        self.assertFalse(valid_input_f1_score(0, 5, 3))
        self.assertFalse(valid_input_f1_score(10, -1, 3))
        self.assertFalse(valid_input_f1_score(10, 5, 0))

    def test_evaluate_model_f1_score(self):
        precision, recall, f1_score = evaluate_model_f1_score(10, 5, 3)
        self.assertAlmostEqual(precision, 0.6667, places=4)
        self.assertAlmostEqual(recall, 0.7692, places=4)
        self.assertAlmostEqual(f1_score, 0.7143, places=4)

        precision, recall, f1_score = evaluate_model_f1_score(1, 1, 1)
        self.assertAlmostEqual(precision, 0.5, places=4)
        self.assertAlmostEqual(recall, 0.5, places=4)
        self.assertAlmostEqual(f1_score, 0.5, places=4)

    def test_evaluate_model_f1_score_invalid_input(self):
        # Test với các đầu vào không hợp lệ
        with self.assertRaises(SystemExit):
            evaluate_model_f1_score('10', 5, 3)

        with self.assertRaises(SystemExit):
            evaluate_model_f1_score(10, '5', 3)

        with self.assertRaises(SystemExit):
            evaluate_model_f1_score(10, 5, '3')

        with self.assertRaises(SystemExit):
            evaluate_model_f1_score(0, 5, 3)

        with self.assertRaises(SystemExit):
            evaluate_model_f1_score(10, -1, 3)

        with self.assertRaises(SystemExit):
            evaluate_model_f1_score(10, 5, 0)


if __name__ == '__main__':
    unittest.main()
