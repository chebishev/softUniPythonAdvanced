import sys

field_size = int(input())
# B is a bunny
# X is a trap
field = []
bunny_position = []
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
max_eggs = -sys.maxsize
best_path = []
best_direction = ""

for row in range(field_size):
    current_row = input().split()
    field.append(current_row)
    if "B" in current_row:
        bunny_position = [row, current_row.index("B")]

for direction in directions:
    current_path = []
    row, col = bunny_position
    current_eggs = 0
    eggs_counter = 0
    while True:
        row += directions[direction][0]
        col += directions[direction][1]
        if 0 <= row < field_size and 0 <= col < field_size:
            if field[row][col] == "X":
                break
            else:
                current_eggs += int(field[row][col])
                current_path.append([row, col])
                eggs_counter += 1
        else:
            break

    if eggs_counter:
        if current_eggs > max_eggs:
            max_eggs = current_eggs
            best_path = current_path
            best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)

# test inputs:

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
