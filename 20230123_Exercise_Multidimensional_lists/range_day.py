def position_is_valid(row_index, col_index):
    if 0 <= row_index < 5 and 0 <= col_index < 5:
        return True


field = []
my_position = []
all_targets = 0
targets_hit = []
current_targets = 0
all_targets_hit = False
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
for row in range(5):
    current_row = input().split()
    field.append(current_row)
    if "A" in current_row:
        my_position = [row, current_row.index("A")]
        field[row][my_position[1]] = "."
    all_targets += current_row.count("x")

number_of_commands = int(input())
for command in range(number_of_commands):
    if all_targets_hit:
        break
    current_command = input().split()
    action = current_command[0]
    direction = current_command[1]

    if action == "shoot":
        new_row = directions[direction][0] + my_position[0]
        new_col = directions[direction][1] + my_position[1]
        while position_is_valid(new_row, new_col):
            new_position = field[new_row][new_col]

            if new_position == "x":
                targets_hit.append([new_row, new_col])
                current_targets += 1
                field[new_row][new_col] = "."
                if current_targets == all_targets:
                    all_targets_hit = True
                break
            new_row += directions[direction][0]
            new_col += directions[direction][1]
    elif action == "move":
        steps = int(current_command[2])
        current_position = my_position
        new_row = 0
        new_col = 0
        for step in range(steps):
            new_row = directions[direction][0] + current_position[0]
            new_col = directions[direction][1] + current_position[1]
            current_position = [new_row, new_col]
        if position_is_valid(new_row, new_col):
            if field[new_row][new_col] == ".":
                my_position = current_position


if all_targets_hit:
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - current_targets} targets left.")
print(*targets_hit, sep="\n")

# test inputs:

# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right

# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left
