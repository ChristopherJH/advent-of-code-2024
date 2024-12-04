import re


def get_uncorrupted_matches(memory: str):
    """Gets all instances of the uncorrupted multiplications"""
    return re.findall(r"mul\([0-9]{0,3},[0-9]{0,3}\)", memory)


def extract_multiplication_value(mul_string: str):
    xy_list = re.findall(r"\d+", mul_string)
    return int(xy_list[0]) * int(xy_list[1])


def get_uncorrupted_multiplications(memory: str):
    """Takes in a corrupted string and extracts all instances of mul(X,Y) from it and calculates the total value"""
    uncorrupted_matches = get_uncorrupted_matches(memory)
    total = 0

    for mul_string in uncorrupted_matches:
        sub_total = extract_multiplication_value(mul_string)
        total += sub_total

    return total


def get_multiplications_with_dont_instructions(memory: str):
    """Get's all mul(X,Y) values that should be ignored"""
    dont_strings = []
    test_string = memory
    dont_total = 0

    while True:
        dont_index = test_string.find("don't()")
        # If no don't's left, stop
        if dont_index == -1:
            break

        do_index = test_string.find("do()")
        # If a don't but no do's left, append rest of string to dont list
        if do_index == -1:
            dont_strings.append(test_string[dont_index + 7 :])
            break

        # If an unnecessary do comes before a dont, ignore it
        if do_index < dont_index:
            test_string = test_string[
                (do_index + 2) :
            ]  # splice from further along to make sure we don't include the do() multiple times
            continue

        # If a valid dont and do, append the string between them to dont list and move string along to next section
        dont_strings.append(test_string[dont_index + 5 : do_index])
        test_string = test_string[(do_index + 2) :]

    for string in dont_strings:
        dont_total += get_uncorrupted_multiplications(string)

    return dont_total


def get_uncorrupted_multiplications_with_instructions(memory: str):
    """Takes in a corrupted string and extracts all instances of mul(X,Y) from it and calculates the total value. Ignoring mul(X,Y) values that come after don't()'s"""
    total = get_uncorrupted_multiplications(memory)
    dont_total = get_multiplications_with_dont_instructions(memory)

    return total - dont_total
