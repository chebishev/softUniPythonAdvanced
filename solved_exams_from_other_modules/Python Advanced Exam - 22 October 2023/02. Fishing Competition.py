def check_index(index):
    if index >= matrix_size:
        index = 0
    elif index < 0:
        index = matrix_size - 1
    return index


matrix_size = int(input())
fishing_area = []
boat_position = []
fish_needed = 20
fish_caught = 0

for row in range(matrix_size):
    fishing_area.append(list(input()))
    if "S" in fishing_area[row]:
        current_row = row
        current_col = fishing_area[row].index("S")
        boat_position = [current_row, current_col]
        fishing_area[row][current_col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)}

command = input()

while command != "collect the nets":
    row = boat_position[0] + directions[command][0]
    col = boat_position[1] + directions[command][1]

    row = check_index(row)
    col = check_index(col)
    boat_position = [row, col]
    current_element = fishing_area[row][col]
    if current_element == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{row},{col}]")
        break
    elif current_element != "-":
        current_catch = int(current_element)
        fish_caught += current_catch
        fishing_area[row][col] = "-"

    command = input()
else:
    if fish_caught >= fish_needed:
        print("Success! You managed to reach the quota!")
    else:
        needed_fish = fish_needed - fish_caught
        print(f"You didn't catch enough fish and didn't reach the quota! You need {needed_fish} tons of fish more.")
    if fish_caught > 0:
        print(f"Amount of fish caught: {fish_caught} tons.")

    fishing_area[boat_position[0]][boat_position[1]] = "S"
    for row in fishing_area:
        print("".join(row))

# test inputs:

# 4
# ---S
# ----
# 9-5-
# 34--
# down
# down
# right
# down
# collect the nets

# 5
# S---9
# 777-1
# W333-
# 11111
# -----
# down
# down
# right
# down
# collect the nets

# 5
# S---9
# 777-1
# --5--
# 11W11
# 988--
# down
# down
# down
# down
# down
# down
# right
# right
# right
# collect the nets
