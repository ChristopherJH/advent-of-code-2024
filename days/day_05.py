from collections import Counter


def generate_order_dictionary(order_elements: list[list[int]]):
    """Given page ordering rules, generates an object outlining the numbers before and after for each number in the input
    Example output:
        dictionary = {
            47: {"before": [97, 75], "after": [53, 13, 61, 29]},
            53: {"before": [47, 75, 61, 97], "after": [29, 13]},
            97: {"before": [], "after": [13, 61, 47, 29, 53, 75]},
            13: {"before": [97, 61, 29, 47, 75, 53], "after": []},
            61: {"before": [97, 47, 75], "after": [13, 53, 29]},
            75: {"before": [97], "after": [29, 53, 47, 61, 13]},
            29: {"before": [75, 97, 53, 61, 47], "after": [13]},
        }
    """
    order_dict: dict[int, dict[str, list[int]]] = {}

    # Iterate through each order element
    for order_element in order_elements:
        first_val = order_element[0]
        second_val = order_element[1]

        # Ensure the keys exist in the dictionary
        order_dict.setdefault(first_val, {"before": [], "after": []})
        order_dict.setdefault(second_val, {"before": [], "after": []})

        # For each element, add the second value to the first values "after" array, and vice versa
        order_dict[first_val]["after"].append(second_val)
        order_dict[second_val]["before"].append(first_val)

    return order_dict


def contains_all_elements(array1, array2):
    """Returns True if all the elements in array2 appear in array1"""
    return all(element in array1 for element in array2)


def do_page_numbers_obey_rules(
    order_dict: dict[int, dict[str, list[int]]], page_numbers: list[int]
):
    """Returns True if all the page numbers in page_numbers follow the page ordering rules"""
    for i, page_number in enumerate(page_numbers):
        page_rules = order_dict[page_number]
        page_numbers_before = page_numbers.copy()[:i]
        page_numbers_after = page_numbers.copy()[i + 1 :]

        if not contains_all_elements(page_rules["before"], page_numbers_before):
            return False
        if not contains_all_elements(page_rules["after"], page_numbers_after):
            return False

    return True


def get_middle_sum_of_correctly_ordered_pages(
    page_ordering_rules: list[list[int]], pages_to_produce: list[list[int]]
):
    """Returns the sum of all the middle pages numbers in the correctly ordered lists of pages_to_produce"""
    order_dict = generate_order_dictionary(page_ordering_rules)
    total = 0

    for page_numbers in pages_to_produce:
        if do_page_numbers_obey_rules(order_dict, page_numbers):
            middle_index = len(page_numbers) // 2
            total += page_numbers[middle_index]

    return total