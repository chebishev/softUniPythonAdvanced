matrix_size = int(input())
armor = 300
jet_position = ()
enemies = 4

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

sky_matrix = []

for row in range(matrix_size):
    current_row = input()
    sky_matrix.append([])
    for col in range(matrix_size):
        current_element = current_row[col]
        if current_element == "J":
            jet_position = (row, col)
            current_element = "-"
        sky_matrix[row].append(current_element)

while True:
    direction = input()

    current_row, current_col = jet_position
    new_row = current_row + directions[direction][0]
    new_col = current_col + directions[direction][1]
    jet_position = (new_row, new_col)

    current_element = sky_matrix[new_row][new_col]
    if current_element == "R":
        armor = 300
        sky_matrix[new_row][new_col] = "-"

    elif current_element == "E":
        if enemies == 1:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            enemies -= 1
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
                break
            sky_matrix[new_row][new_col] = "-"

sky_matrix[jet_position[0]][jet_position[1]] = "J"

[print("".join(row)) for row in sky_matrix]

# test inputs:

# 5
# -R---
# -J--E
# -E---
# --E-E
# -R---
# up
# down
# down
# down
# right
# right
# right

# 4
# -R--
# -JEE
# -E-R
# --E-
# right
# right
# down
# left
# left
# down
# right
