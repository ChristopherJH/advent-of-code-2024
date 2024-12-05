import unittest
from days.day_05 import get_middle_sum_of_correctly_ordered_pages


def get_page_data_from_file(file_path):
    page_ordering_rules = []
    pages_to_produce = []
    with open(file_path, "r") as file:
        for line in file:
            print(line)

            rule = list(map(int, line.split("|")))
            # remove newline character
            if rule[-1] == "\n":
                rule.pop()
            page_ordering_rules.append(rule)
    return rule


def process_file(file_path):
    page_ordering_rules = []
    pages_to_produce = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        # Process lines with '|' character
        for line in lines:
            if "|" in line:
                parts = line.strip().split("|")
                page_ordering_rules.append(list(map(int, parts)))
            elif "," in line:
                comma_separated_array = line.strip().split(",")
                pages_to_produce.append(list(map(int, comma_separated_array)))

    return page_ordering_rules, pages_to_produce


class TestSearchXmasCrossword(unittest.TestCase):
    def test_get_middle_sum_of_correctly_ordered_pages__base_case(self):
        page_data = process_file("tests/input_data/day_05_1_example.txt")
        page_ordering_rules = page_data[0]
        pages_to_produce = page_data[1]
        self.assertEqual(get_middle_sum_of_correctly_ordered_pages(page_ordering_rules, pages_to_produce), 143)

    def test_get_middle_sum_of_correctly_ordered_pages(self):
        page_data = process_file("tests/input_data/day_05_1.txt")
        page_ordering_rules = page_data[0]
        pages_to_produce = page_data[1]
        self.assertEqual(get_middle_sum_of_correctly_ordered_pages(page_ordering_rules, pages_to_produce), 6949)