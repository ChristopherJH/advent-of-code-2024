import unittest
from days.day_02 import (
    calculate_num_of_safe_reports,
    calculate_num_of_safe_reports_with_dampener,
)
from utils.file_helpers import extract_nums_as_arrays_from_file


class TestSafeReports(unittest.TestCase):
    def test_calculate_num_of_safe_reports__base_case(self):
        file_path = "tests/input_data/day_02_1_example.txt"
        arrays = extract_nums_as_arrays_from_file(file_path)
        self.assertEqual(calculate_num_of_safe_reports(arrays), 2)

    def test_calculate_num_of_safe_reports(self):
        file_path = "tests/input_data/day_02_1.txt"
        arrays = extract_nums_as_arrays_from_file(file_path)
        self.assertEqual(calculate_num_of_safe_reports(arrays), 639)

    def test_calculate_num_of_safe_reports__big_jump(self):
        reports = [[1, 2, 3, 4, 8]]
        self.assertEqual(calculate_num_of_safe_reports(reports), 0)

    def test_calculate_num_of_safe_reports__increase_then_decrease(self):
        reports = [[1, 2, 3, 4, 5, 4, 3]]
        self.assertEqual(calculate_num_of_safe_reports(reports), 0)

    def test_calculate_num_of_safe_reports__safe_report(self):
        reports = [[1, 2, 5, 6, 8]]
        self.assertEqual(calculate_num_of_safe_reports(reports), 1)


class TestSafeReportsWithDampener(unittest.TestCase):
    def test_calculate_num_of_safe_reports_with_dampener__base_case(self):
        file_path = "tests/input_data/day_02_1_example.txt"
        arrays = extract_nums_as_arrays_from_file(file_path)
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(arrays), 4)

    def test_calculate_num_of_safe_reports_with_dampener(self):
        file_path = "tests/input_data/day_02_1.txt"
        arrays = extract_nums_as_arrays_from_file(file_path)
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(arrays), 674)

    def test_calculate_num_of_safe_reports_with_dampener__remove_reverse_order_safe(
        self,
    ):
        reports = [[1, 2, 3, 4, 5, 4, 6]]
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(reports), 1)

    def test_calculate_num_of_safe_reports_with_dampener__big_jump_safe(self):
        reports = [[1, 2, 3, 10, 5, 6]]
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(reports), 1)

    def test_calculate_num_of_safe_reports_with_dampener__big_jump_unsafe(self):
        reports = [[1, 2, 3, 10, 12, 5, 6]]
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(reports), 0)

    def test_calculate_num_of_safe_reports_with_dampener__big_jump_end_safe(self):
        reports = [[1, 2, 3, 10]]
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(reports), 1)

    def test_calculate_num_of_safe_reports_with_dampener__big_jump_start_safe(self):
        reports = [[10, 1, 2, 3]]
        self.assertEqual(calculate_num_of_safe_reports_with_dampener(reports), 1)


if __name__ == "__main__":
    unittest.main()
