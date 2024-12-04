directions_to_search = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1],
]


def get_xmas_count_from_cell(
    x_index: int, y_index: int, crossword_array: list[list[str]]
):
    xmas_count = 0
    max_x = len(crossword_array[0])
    max_y = len(crossword_array)

    # search for xmas in every direction
    for _, direction in enumerate(directions_to_search):
        search_term = "XMAS"
        for i in range(1, 4):
            # Check if location exists on crossword
            x_coord = x_index + (i * direction[0])
            y_coord = y_index + (i * direction[1])
            if 0 <= x_coord < max_x and 0 <= y_coord < max_y:
                # If no match, move onto next direction
                if (
                    crossword_array[y_coord][
                        x_coord
                    ]
                    == search_term[i]
                ):
                    if i == 3:
                        # a full match has been found, increment xmas_count
                        xmas_count += 1
                else:
                    break
            else:
                break

    return xmas_count


def get_xmas_count_from_crossword(crossword_array: list[list[str]]):
    total_xmas_count = 0

    for y_index, row in enumerate(crossword_array):
        for x_index, val in enumerate(row):
            # for each value, check if cell is "X", if so, start searching for "XMAS", else continue
            if val == "X":
                total_xmas_count += get_xmas_count_from_cell(
                    x_index, y_index, crossword_array
                )
            else:
                continue

    return total_xmas_count
