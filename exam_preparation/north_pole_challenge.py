def check_outside_workshop(index, border):
    if index < 0:
        return border - 1
    elif index == border:
        return 0
    else:
        return index


rows, cols = (int(x) for x in input() if x.isdigit())
my_position = (0, 0)
available_items = 0
workshop = []
# filling the matrix
for row in range(rows):
    # getting current row
    current_row = input().split()
    # appending current row to the matrix
    workshop.append(current_row)
    for col in range(cols):
        # getting my position
        if workshop[row][col] == "Y":
            my_position = (row, col)
        # counting all available for collecting items
        elif workshop[row][col] != ".":
            available_items += 1
# marking current position with "x"
workshop[my_position[0]][my_position[1]] = "x"

items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}
translate_items = {
    "D": "Christmas decorations",
    "G": "Gifts",
    "C": "Cookies"
}
directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}
all_items_found = False
while True:
    command = input()
    if command == "End":
        break

    direction, steps = command.split('-')
    for step in range(int(steps)):
        if all_items_found:
            break
        # get the row for next step
        new_row = my_position[0] + directions[direction][0]
        # if it is outside the borders this function will change it to a number in the other side of the workshop
        next_row = check_outside_workshop(new_row, rows)
        # getting the column for next step
        new_col = my_position[1] + directions[direction][1]
        # change the value if it is outside the workshop
        next_col = check_outside_workshop(new_col, cols)
        # getting the item on the new coordinates in order to collect it and mark it with "x"
        next_item = workshop[next_row][next_col]
        if next_item in ("C", "D", "G"):
            available_items -= 1
            items[translate_items[next_item]] += 1

            if available_items == 0:
                all_items_found = True
        workshop[next_row][next_col] = "x"
        my_position = (next_row, next_col)
    if all_items_found:
        break

workshop[my_position[0]][my_position[1]] = "Y"
if all_items_found:
    print("Merry Christmas!")
print("You've collected:")
for k, v in items.items():
    print(f"- {v} {k}")
for row in workshop:
    print(' '.join(row))
# test inputs:

# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End

# 5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3

# 5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End
