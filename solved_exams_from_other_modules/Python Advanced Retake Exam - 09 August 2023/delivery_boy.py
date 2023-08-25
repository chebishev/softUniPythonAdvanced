# •	'B' - Represents the starting position of the delivery boy.
# •	'A' - Represents an address where a pizza needs to be delivered.
# •	'*' - Represents an obstacle or an area where the delivery boy cannot drive.
# •	'P' - Represents the pizza restaurant.
# •	'-' – Represents the road, the delivery boy can drive over it.

dimensions = [int(x) for x in input().split()]
initial_boy_position = ()
boy_position = ()
field = []
is_collected = False

for row in range(dimensions[0]):
    field.append([])
    for col in input():
        if col == 'B':
            boy_position = (row, len(field[row]))
            initial_boy_position = boy_position
            col = '-'
        field[row].append(col)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    current_row, current_col = boy_position
    new_row, new_col = current_row + directions[direction][0], current_col + directions[direction][1]

    # out of boundaries check
    if new_row not in range(dimensions[0]) or new_col not in range(dimensions[1]):
        field[initial_boy_position[0]][initial_boy_position[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    if field[new_row][new_col] == 'A':
        if not is_collected:
            boy_position = (new_row, new_col)
        else:
            field[new_row][new_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            field[initial_boy_position[0]][initial_boy_position[1]] = 'B'
            break
    elif field[new_row][new_col] == 'P':
        field[new_row][new_col] = 'R'
        is_collected = True
        boy_position = (new_row, new_col)
        print("Pizza is collected. 10 minutes for delivery.")
    elif field[new_row][new_col] == '*':
        continue
    else:
        field[new_row][new_col] = '.'
        boy_position = (new_row, new_col)

print(*[''.join(row) for row in field], sep="\n")

# test inputs:

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# right
# right
# right
# right
# up
# up
# up

# 5 6
# *----A
# *B***-
# *-***-
# *----P
# ******
# down
# down
# left
# right
# right
# right
# right
# right
# up
