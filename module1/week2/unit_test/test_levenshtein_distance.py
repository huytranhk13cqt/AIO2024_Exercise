import unittest

from practice_exercise.levenshtein_distance import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):
    def test_levenshtein_distance(self):
        # Test case 1
        source = "kitten"
        target = "sitting"
        expected_result = 3
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 2
        source = "flaw"
        target = "lawn"
        expected_result = 2
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 3
        source = "intention"
        target = "execution"
        expected_result = 5
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 4
        source = ""
        target = "abc"
        expected_result = 3
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 5
        source = "abc"
        target = ""
        expected_result = 3
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 6
        source = "abc"
        target = "abc"
        expected_result = 0
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 7
        source = "a"
        target = "a"
        expected_result = 0
        self.assertEqual(levenshtein_distance(source, target), expected_result)

        # Test case 8
        source = "a"
        target = "b"
        expected_result = 1
        self.assertEqual(levenshtein_distance(source, target), expected_result)


if __name__ == "__main__":
    unittest.main()
