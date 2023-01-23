def index_is_valid(row_index, col_index):
    if 0 <= row_index < field_size and 0 <= col_index < field_size:
        return True


field_size = int(input())
directions = input().split()
moves_dictionary = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
exit_position = ()
miner_position = ()
mine = []
available_coal = 0
collected_coal = 0
# c -> coal
# s -> miner
# e -> the end of the route
# * -> standard field
for row in range(field_size):
    current_row = input().split()
    mine.append(current_row)
    available_coal += current_row.count("c")
    if "s" in current_row:
        col = current_row.index("s")
        miner_position = (row, col)
        mine[row][col] = "*"
    if "e" in current_row:
        col = current_row.index("e")
        exit_position = (row, col)

for step in directions:
    current_step = moves_dictionary[step]
    next_row = miner_position[0] + current_step[0]
    next_col = miner_position[1] + current_step[1]
    if index_is_valid(next_row, next_col):
        if mine[next_row][next_col] == "c":
            collected_coal += 1
            mine[next_row][next_col] = "*"
            miner_position = (next_row, next_col)
        elif mine[next_row][next_col] == "e":
            print(f"Game over! {exit_position}")
            break
        else:
            miner_position = (next_row, next_col)
else:
    if collected_coal == available_coal:
        print(f"You collected all coal! {miner_position}")
    else:
        print(f"{available_coal - collected_coal} pieces of coal left. {miner_position}")

# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *

# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
