def extract_nums_as_arrays_from_file(file_path):
    arrays = []
    with open(file_path, "r") as file:
        for line in file:
            array = list(map(int, line.split()))
            arrays.append(array)
    return arrays