field_size = int(input())
energy = 15
collected_nectar = 0
bee_position = ()
is_restoration_used = False

field_matrix = []
for row in range(field_size):
    current_row = [x for x in input()]
    if "B" in current_row:
        bee_position = (row, current_row.index("B"))
    field_matrix.append(current_row)

field_matrix[bee_position[0]][bee_position[1]] = "-"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while True:
    direction = input()
    current_row, current_col = bee_position

    new_row = current_row + directions[direction][0]
    new_col = current_col + directions[direction][1]
    energy -= 1

    if new_row not in range(field_size):
        new_row = new_row + field_size if new_row < 0 else new_row - field_size
    elif new_col not in range(field_size):
        new_col = new_col + field_size if new_col < 0 else new_col - field_size
    bee_position = (new_row, new_col)
    current_element = field_matrix[new_row][new_col]

    if current_element == "H":
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")

        field_matrix[new_row][new_col] = "B"
        break

    elif current_element.isdigit():
        collected_nectar += int(current_element)
        field_matrix[new_row][new_col] = "-"

    if energy == 0:
        if not is_restoration_used:
            if collected_nectar > 30:
                energy += collected_nectar - 30
                collected_nectar = 30
                is_restoration_used = True
            else:
                print("This is the end! Beesy ran out of energy.")
                field_matrix[new_row][new_col] = "B"
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            field_matrix[new_row][new_col] = "B"
            break

for row in field_matrix:
    print(''.join(row))

# test inputs:

# 5
# --B--
# H-987
# -4812
# 5----
# 2----
# down
# right
# right
# down
# left
# left
# left
# down
# left
# up
# up
# up

# 4
# B999
# --5-
# ---H
# ----
# right
# right
# right
# down
# left
# left
# left
# left
# down

# 4
# B---
# 1991
# ----
# ---H
# down
# right
# right
# right
# down
# down
# left

# 6
# B-----
# 111111
# ------
# 111111
# ------
# H-----
# down
# right
# right
# right
# right
# right
# down
# left
# left
# left
# left
# left
# down
# right
# right
# right
# right
# right


