import unittest
from days.day_01 import calculate_distance_between_lists


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


if __name__ == "__main__":
    unittest.main()
