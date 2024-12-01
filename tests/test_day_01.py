import unittest
from days.day_01 import calculate_distance_between_lists, calculate_similarity_score


class TestSort(unittest.TestCase):
    def test_calculate_distance_between_lists(self):
        self.assertEqual(
            calculate_distance_between_lists([5, 4, 5, 2, 3], [1, 2, 3, 4, 5]), 4
        )

    def test_calculate_distance_between_lists__no_distance(self):
        self.assertEqual(
            calculate_distance_between_lists([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 0
        )

    def test_calculate_distance_between_lists__same_list(self):
        self.assertEqual(
            calculate_distance_between_lists([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]), 0
        )

    def test_calculate_distance_between_lists__errors_for_different_lengths(self):
        with self.assertRaises(ValueError):
            calculate_distance_between_lists([1], [1, 1])


class TestSimilarityScore(unittest.TestCase):
    def test_calculate_similarity_score(self):
        self.assertEqual(
            calculate_similarity_score([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 15
        )

    def test_calculate_similarity_score__base_case(self):
        self.assertEqual(
            calculate_similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]), 31
        )

    def test_calculate_similarity_score__multiple_occurences(self):
        self.assertEqual(
            calculate_similarity_score([5, 5, 5, 4, 3, 2, 2, 1], [1, 2, 2, 3, 4, 5]), 31
        )

    def test_calculate_similarity_score__empty(self):
        self.assertEqual(calculate_similarity_score([], []), 0)


if __name__ == "__main__":
    unittest.main()
