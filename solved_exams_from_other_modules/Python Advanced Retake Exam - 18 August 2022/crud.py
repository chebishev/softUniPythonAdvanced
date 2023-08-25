information_table = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(6):
    current_row = input().split()
    information_table.append(current_row)

row, col = input().split(", ")
row = int(row[1:])
col = int(col[:-1])

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split(", ")
    action = command[0]
    direction = command[1]
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]
    current_value = information_table[new_row][new_col]
    if action == "Create":
        value = command[2]
        if current_value == ".":
            information_table[new_row][new_col] = value

    elif action == "Update":
        value = command[2]
        if current_value != ".":
            information_table[new_row][new_col] = value

    elif action == "Delete":
        information_table[new_row][new_col] = "."

    elif action == "Read":
        if current_value != ".":
            print(current_value)

    row = new_row
    col = new_col

for row in information_table:
    print(' '.join(row))

# test inputs:

# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop

# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop

# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop
