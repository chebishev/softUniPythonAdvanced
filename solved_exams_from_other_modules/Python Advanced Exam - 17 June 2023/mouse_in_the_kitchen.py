rows, cols = [int(x) for x in input().split(',')]
cupboard_area = []
mouse_position = ()
last_position = ()
available_cheese = 0
danger = False
invalid_index = False
for row in range(rows):
    cupboard_area.append([])
    for col in input():
        current_element = col
        if current_element == "M":
            mouse_position = (row, len(cupboard_area[row]))
            current_element = "*"
        elif current_element == "C":
            available_cheese += 1
        cupboard_area[row].append(current_element)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    current_row, current_col = mouse_position

    if command == "danger":
        danger = True
        print("Mouse will come back later!")
        break

    last_position = current_row + directions[command][0], current_col + directions[command][1]
    new_row, new_col = last_position
    if new_row not in range(rows) or new_col not in range(cols):
        invalid_index = True
        print("No more cheese for tonight!")
        break

    current_element = cupboard_area[new_row][new_col]

    if current_element == 'C':
        available_cheese -= 1
        if available_cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
        else:
            cupboard_area[new_row][new_col] = "*"

    elif current_element == 'T':
        print("Mouse is trapped!")
        break

    elif current_element == "@":
        continue

    mouse_position = last_position

if danger or invalid_index:
    cupboard_area[mouse_position[0]][mouse_position[1]] = "M"
else:
    cupboard_area[last_position[0]][last_position[1]] = "M"
for row in cupboard_area:
    print(''.join(row))

# test inputs:

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger

# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger

# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger
