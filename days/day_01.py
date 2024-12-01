from utils.sort import sort

def calculate_distance_between_lists(list_1: list, list_2: list):
    sorted_list_1 = sort(list_1)
    sorted_list_2 = sort(list_2)
    distance = 0
    
    if len(sorted_list_1) != len(sorted_list_2):
        raise ValueError('Lists are not of equal size!')
    
    for i in range(len(sorted_list_1)):
        distance += abs(sorted_list_1[i] - sorted_list_2[i])
        
    return distance
        
        






