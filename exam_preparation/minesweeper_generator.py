def is_valid(index):
    if 0 <= index < mine_field_size:
        return True


def check_directions(row_index, col_index):
    counter = 0
    for direction in directions:
        next_row = row_index + direction[0]
        next_col = col_index + direction[1]
        if is_valid(next_row) and is_valid(next_col):
            next_position = mine_field[next_row][next_col]
            if next_position == "*":
                counter += 1
    return counter


mine_field_size = int(input())
mines_count = int(input())

mine_field = [[0] * mine_field_size for row in range(mine_field_size)]

for _ in range(mines_count):
    line = input()[1:-1].split(", ")
    row, col = (int(x) for x in line)
    mine_field[row][col] = "*"

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for row in range(mine_field_size):
    for col in range(mine_field_size):
        current_position = mine_field[row][col]
        if current_position != "*":
            mine_field[row][col] = check_directions(row, col)

for row in mine_field:
    print(' '.join(str(x) for x in row))

# test inputs:

# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)

# 5
# 3
# (1, 1)
# (2, 4)
# (4, 1)
