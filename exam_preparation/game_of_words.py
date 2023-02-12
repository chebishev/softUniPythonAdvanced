initial_string = input()
matrix_size = int(input())
matrix = []
player_position = ()
for row in range(matrix_size):
    current_row = input()
    matrix.append([x for x in current_row])
    if "P" in current_row:
        col = current_row.index("P")
        player_position = (row, col)
        matrix[row][col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
number_of_moves = int(input())
for _ in range(number_of_moves):
    next_move = input()
    next_row = player_position[0] + directions[next_move][0]
    next_col = player_position[1] + directions[next_move][1]
    if next_row not in range(matrix_size) or next_col not in range(matrix_size):
        if initial_string:
            initial_string = initial_string[:-1]
            continue
    else:
        current_element = matrix[next_row][next_col]
        if current_element != "-":
            initial_string += current_element
            matrix[next_row][next_col] = "-"
            player_position = (next_row, next_col)
        else:
            player_position = (next_row, next_col)

matrix[player_position[0]][player_position[1]] = "P"
print(initial_string)
for row in matrix:
    print(''.join(row))

# test inputs:

# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right
