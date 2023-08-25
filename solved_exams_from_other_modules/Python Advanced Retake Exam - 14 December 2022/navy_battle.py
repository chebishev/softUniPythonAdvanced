sea_size = int(input())
sea_map = []
submarine_position = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

mines_counter = 0
destroyed_battle_cruisers = 0

for row in range(sea_size):
    current_row = [ch for ch in input()]
    sea_map.append(current_row)
    if "S" in current_row:
        submarine_position = [row, current_row.index("S")]
        sea_map[row][submarine_position[1]] = "-"

while True:
    current_move = input()
    next_row = submarine_position[0] + directions[current_move][0]
    next_col = submarine_position[1] + directions[current_move][1]
    current_position = sea_map[next_row][next_col]
    submarine_position = [next_row, next_col]
    if current_position == "*":
        mines_counter += 1
        if mines_counter == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
            break
    elif current_position == "C":
        destroyed_battle_cruisers += 1
        if destroyed_battle_cruisers == 3:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    sea_map[next_row][next_col] = "-"

sea_map[submarine_position[0]][submarine_position[1]] = "S"
for row in sea_map:
    print("".join(row))

# test inputs:

# 5
# *--*-
# -S-*C
# -*---
# -----
# -C-*C
# right
# down
# left
# up
# right
# right
# right
# down
# down
# down
# up
# left
# left
# left
# down

# 5
# *--*-
# -S-*C
# -*---
# -----
# *C-*C
# right
# right
# up
# left
# left
# left