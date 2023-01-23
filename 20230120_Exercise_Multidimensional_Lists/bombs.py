def index_is_valid(row_index, col_index):
    if 0 <= row_index < matrix_size and 0 <= col_index < matrix_size:
        return True


def blow_alive_cells_in_radius(row_index, col_index):
    detonation_power = bomb_field[row][col]

    for coordinates in explosion_radius:
        current_row = row_index + coordinates[0]
        current_col = col_index + coordinates[1]

        if index_is_valid(current_row, current_col):
            if bomb_field[current_row][current_col] > 0:
                bomb_field[current_row][current_col] -= detonation_power


matrix_size = int(input())
bomb_field = [[int(x) for x in input().split()] for row in range(matrix_size)]

bomb_coordinates = []
for item in input().split():
    row, col = item.split(",")
    bomb_coordinates.append((int(row), int(col)))

explosion_radius = (
    (0, 0),  # current_position
    (-1, -1),  # up_left_diagonal
    (-1, 0),  # up
    (-1, 1),  # up_right_diagonal
    (0, -1),  # left
    (0, 1),  # right
    (1, -1),  # down_left_diagonal
    (1, 0),  # down
    (1, 1)  # down_right_diagonal
)
for position in bomb_coordinates:
    row = position[0]
    col = position[1]

    if index_is_valid(row, col):
        if bomb_field[row][col] <= 0:
            continue
        blow_alive_cells_in_radius(row, col)

active_cells = []
for row in bomb_field:
    for number in row:
        active_cells.append(number) if number > 0 else None

print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")
for row in bomb_field:
    print(f"{' '.join(str(x) for x in row)}")

# test inputs:

# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0

# 3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2
