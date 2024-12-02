import unittest
from days.day_02 import calculate_num_of_safe_reports

def extract_arrays_from_file(file_path):
    arrays = []
    with open(file_path, 'r') as file:
        for line in file:
            array = list(map(int, line.split()))
            arrays.append(array)
    return arrays

class TestSafeReports(unittest.TestCase):
    def test_calculate_num_of_safe_reports__base_case(self):
        file_path = 'tests/input_data/day_02_2_example.txt'
        arrays = extract_arrays_from_file(file_path)
        self.assertEqual(
            calculate_num_of_safe_reports(arrays), 2
        )

    def test_calculate_num_of_safe_reports(self):
        file_path = 'tests/input_data/day_02_2.txt'
        arrays = extract_arrays_from_file(file_path)
        self.assertEqual(
            calculate_num_of_safe_reports(arrays), 639
        )
    
    def test_calculate_num_of_safe_reports__big_jump(self):
        reports = [[1, 2, 3, 4, 8]]
        self.assertEqual(
            calculate_num_of_safe_reports(reports), 0
        )
        
    def test_calculate_num_of_safe_reports__increase_then_decrease(self):
        reports = [[1, 2, 3, 4, 5, 4, 3]]
        self.assertEqual(
            calculate_num_of_safe_reports(reports), 0
        )
    
    def test_calculate_num_of_safe_reports__safe_report(self):
        reports = [[1, 2, 5, 6, 8]]
        self.assertEqual(
            calculate_num_of_safe_reports(reports), 1
        )

if __name__ == "__main__":
    unittest.main()