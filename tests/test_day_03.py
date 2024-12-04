import unittest
from days.day_03 import (
    get_uncorrupted_matches,
    get_uncorrupted_multiplications,
    get_uncorrupted_multiplications_with_instructions,
)


def extract_text_from_file(file_path):
    arrays = []
    with open(file_path, "r") as file:
        for line in file:
            arrays.append(line)
        return arrays


class TestMulRegex(unittest.TestCase):
    def test_mul_regex__1(self):
        self.assertEqual(
            get_uncorrupted_matches("fewmul(123,123)fewi"), ["mul(123,123)"]
        )

    def test_mul_regex__2(self):
        self.assertEqual(
            get_uncorrupted_matches("fewmul(123,23)femul(21,$)fewgg"), ["mul(123,23)"]
        )

    def test_mul_regex__base_case(self):
        self.assertEqual(
            get_uncorrupted_matches(
                "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
            ),
            ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"],
        )


class TestGetUncorruptedMultiplications(unittest.TestCase):
    def test_get_uncorrupted_multiplications__base_case(self):
        self.assertEqual(
            get_uncorrupted_multiplications(
                "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
            ),
            161,
        )

    def test_get_uncorrupted_multiplications(self):
        lines = extract_text_from_file("tests/input_data/day_03.txt")
        total = 0
        for line in lines:
            total += get_uncorrupted_multiplications(line)
        self.assertEqual(total, 167090022)


class TestGetUncorruptedMultiplicationsWithInstructions(unittest.TestCase):
    def test_get_uncorrupted_multiplications_with_instructions__base_case(self):
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
            ),
            48,
        )

    def test_get_uncorrupted_multiplications_with_instructions__with_dos(self):
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "xmul(2,4)%&mul[3,7]!@do()^do_not_mul(5,5)+mul(32,64]thendo()(mul(11,8)mul(8,5))"
            ),
            161,
        )
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "xmul(2,4)%&mul[3,7]!@do()don't()do()^do_not_mul(5,5)+mul(32,64]thendo()(mul(11,8)mul(8,5))"
            ),
            161,
        )

    def test_get_uncorrupted_multiplications_with_instructions__with_donts(self):
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "don't()xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))don't()"
            ),
            0,
        )
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "don't()xmul(2,4)%&mul[3,7]!@do()^do_not_mul(5,5)+mul(32,64]thendo()(mul(11,8)mul(8,5))don't()"
            ),
            153,
        )
        self.assertEqual(
            get_uncorrupted_multiplications_with_instructions(
                "xmul(2,4)%&mul[3,7]!@do()^do_not_mul(5,5)+mul(32,64]thendo()(mul(11,8)mul(8,5))dont()"
            ),
            161,
        )

    def test_get_uncorrupted_multiplications_with_instructions(self):
        lines = extract_text_from_file("tests/input_data/day_03.txt")
        total = 0
        for line in lines:
            total += get_uncorrupted_multiplications_with_instructions(line)
        self.assertEqual(total, 89823704)
