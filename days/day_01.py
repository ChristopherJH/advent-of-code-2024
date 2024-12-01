from utils.sort import sort
from utils.get_frequency import get_frequency


def calculate_distance_between_lists(list_1: list, list_2: list):
    sorted_list_1 = sort(list_1)
    sorted_list_2 = sort(list_2)
    distance = 0

    if len(sorted_list_1) != len(sorted_list_2):
        raise ValueError("Lists are not of equal size!")

    for i in range(len(sorted_list_1)):
        distance += abs(sorted_list_1[i] - sorted_list_2[i])

    return distance


def calculate_similarity_score(list_1: list, list_2: list):
    list_1_frequency_obj = get_frequency(list_1)
    list_2_frequency_obj = get_frequency(list_2)
    similarity_score = 0

    list_1_frequency_obj_keys = list(list_1_frequency_obj.keys())
    for val in list_1_frequency_obj_keys:
        list_2_frequency = (
            list_2_frequency_obj[val] if val in list_2_frequency_obj else 0
        )
        similarity_score += list_1_frequency_obj[val] * val * list_2_frequency

    return similarity_score
