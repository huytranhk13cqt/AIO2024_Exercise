import unittest

from practice_exercise.sliding_window import max_sliding_window


class TestMaxSlidingWindow(unittest.TestCase):
    def test_max_sliding_window(self):
        # Test case 1
        num_lst = [1, 3, 5, 2, 8, 7, 4]
        size_slide_window = 3
        expected_result = [5, 5, 8, 8, 8]
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 2
        num_lst = [10, 9, 8, 7, 6, 5, 4]
        size_slide_window = 2
        expected_result = [10, 9, 8, 7, 6, 5]
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 3
        num_lst = [1, 2, 3, 4, 5]
        size_slide_window = 5
        expected_result = [5]
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 4
        num_lst = [1, 3, 2, 5, 4]
        size_slide_window = 1
        expected_result = [1, 3, 2, 5, 4]
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 5
        num_lst = []
        size_slide_window = 3
        expected_result = []
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 6
        num_lst = [1]
        size_slide_window = 1
        expected_result = [1]
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)

        # Test case 7: Sliding window size larger than list
        num_lst = [1, 2, 3]
        size_slide_window = 4
        expected_result = []
        self.assertEqual(max_sliding_window(
            num_lst, size_slide_window), expected_result)


if __name__ == "__main__":
    unittest.main()
