def get_frequency(input_list: list):
    frequency_obj = {}
    for i, val in enumerate(input_list):
        if val in frequency_obj:
            frequency_obj[val] += 1
        else:
            frequency_obj[val] = 1

    return frequency_obj
