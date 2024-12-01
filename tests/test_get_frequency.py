import unittest
from utils.get_frequency import get_frequency


class TestGetFrequency(unittest.TestCase):
    def test_get_frequency(self):
        self.assertEqual(get_frequency([3, 2, 2, 1, 1]), {1: 2, 2: 2, 3: 1})

    def test_get_frequency__empty_list(self):
        self.assertEqual(get_frequency([]), {})

    def test_get_frequency__same_elements(self):
        self.assertEqual(get_frequency([1, 1, 1, 1, 1]), {1: 5})


if __name__ == "__main__":
    unittest.main()
