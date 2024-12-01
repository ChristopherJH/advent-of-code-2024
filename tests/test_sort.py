import unittest
from utils.sort import sort


class TestSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort_one_element(self):
        self.assertEqual(sort([1]), [1])

    def test_sort__ordered(self):
        self.assertEqual(sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort__duplicates(self):
        self.assertEqual(sort([1, 2, 3, 3, 3, 4, 5, 3]), [1, 2, 3, 3, 3, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
