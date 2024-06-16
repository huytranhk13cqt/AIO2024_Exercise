import unittest

from practice_exercise.count_chars import count_chars


class TestCountChars(unittest.TestCase):
    def test_count_chars(self):
        self.assertEqual(count_chars("smiles"), {
                         'e': 1, 'i': 1, 'l': 1, 'm': 1, 's': 2})
        self.assertEqual(count_chars(""), {})
        self.assertEqual(count_chars("AAbbCC"), {'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(count_chars("123"), {'1': 1, '2': 1, '3': 1})
        self.assertEqual(count_chars("Hello, World!"), {
                         ' ': 1, '!': 1, ',': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1})


if __name__ == '__main__':
    unittest.main()
