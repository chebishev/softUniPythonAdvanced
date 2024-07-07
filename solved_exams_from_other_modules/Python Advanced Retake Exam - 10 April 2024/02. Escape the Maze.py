maze_size = int(input())
health = 100
traveller_position = ()
maze_matrix = []

for row in range(maze_size):
    current_row = input()
    maze_matrix.append([])
    for col in range(maze_size):
        current_col = current_row[col]
        if current_col == "P":
            traveller_position = (row, col)
            current_col = "-"
        maze_matrix[row].append(current_col)

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while True:
    direction = input()

    current_row, current_col = traveller_position
    new_row = current_row + directions[direction][0]
    new_col = current_col + directions[direction][1]

    if new_row not in range(maze_size) or new_col not in range(maze_size):
        continue

    current_element = maze_matrix[new_row][new_col]
    if current_element == "M":
        health -= 40
        if health <= 0:
            health = 0
            maze_matrix[new_row][new_col] = "P"
            print("Player is dead. Maze over!")
            break
        else:
            maze_matrix[new_row][new_col] = "-"

    elif current_element == "H":
        health += 15
        if health >= 100:
            health = 100
        maze_matrix[new_row][new_col] = "-"
    elif current_element == "X":
        maze_matrix[new_row][new_col] = "P"
        print("Player escaped the maze. Danger passed!")
        break

    traveller_position = (new_row, new_col)

print(f"Player's health: {health} units")
[print(''.join(row)) for row in maze_matrix]

# test inputs:

# 5
# -----
# -PM--
# -M---
# ---H-
# -X---
# down
# right
# down
# down
# left

# 8
# --H-----
# ---P---X
# --------
# --M--M--
# --H--M--
# H-----M-
# --------
# ------H-
# down
# right
# right
# down
# down
# right
# down
# left
# up
# up

# 4
# ----
# P-H-
# ----
# X---
# right
# right
# right
# right
# down
# down
# down
# left
# left
# left


