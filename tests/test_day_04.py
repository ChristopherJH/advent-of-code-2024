import unittest
from days.day_04 import get_xmas_count_from_crossword


def get_crossword_from_file(file_path):
    arrays = []
    with open(file_path, "r") as file:
        for line in file:
            array = list(map(str, list(line)))
            # remove newline character
            if array[-1] == "\n":
                array.pop()
            arrays.append(array)
    return arrays


class TestSearchXmasCrossword(unittest.TestCase):
    def test_search_xmas_crossword__base_case(self):
        crossword = get_crossword_from_file("tests/input_data/day_04_1_example.txt")
        self.assertEqual(get_xmas_count_from_crossword(crossword), 18)

    def test_search_xmas_crossword(self):
        crossword = get_crossword_from_file("tests/input_data/day_04_1.txt")
        self.assertEqual(get_xmas_count_from_crossword(crossword), 2685)

    def test_search_xmas_crossword__one_row(self):
        self.assertEqual(
            get_xmas_count_from_crossword(
                [["X", "M", "A", "S", "X", "M", "A", "X", "M", "A", "S", "A", "M", "X"]]
            ),
            3,
        )

    def test_search_xmas_crossword__one_column(self):
        self.assertEqual(
            get_xmas_count_from_crossword(
                [
                    ["X"],
                    ["M"],
                    ["A"],
                    ["S"],
                    ["X"],
                    ["M"],
                    ["A"],
                    ["X"],
                    ["M"],
                    ["A"],
                    ["S"],
                    ["A"],
                    ["M"],
                    ["X"],
                ]
            ),
            3,
        )
