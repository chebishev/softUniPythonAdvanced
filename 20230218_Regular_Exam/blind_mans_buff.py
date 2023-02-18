rows, columns = [int(x) for x in input().split()]
# search for "B" on random position
# obstacles - "O"
# 3 other players - "P"
playground = []
my_position = []
touched_opponents = 0
moves = 0

for row in range(rows):
    current_row = input().split()
    playground.append(current_row)
    for column in range(columns):
        current_element = playground[row][column]
        if current_element == "B":
            my_position = [row, column]
            playground[row][column] = "-"

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while True:
    command = input()
    if command == "Finish":
        break

    next_row = my_position[0] + directions[command][0]
    next_column = my_position[1] + directions[command][1]
    if 0 <= next_row < rows and 0 <= next_column < columns:
        next_element = playground[next_row][next_column]
        if next_element == "O":
            continue

        moves += 1
        if next_element == "P":
            touched_opponents += 1
            if touched_opponents == 3:
                break
            playground[next_row][next_column] = "-"

        my_position = [next_row, next_column]


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")

# test inputs:

# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish

# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
