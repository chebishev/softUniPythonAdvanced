def position_is_valid(row_index, col_index):
    if 0 <= row_index < rows and 0 <= col_index < cols:
        return True


rows, cols = list(map(int, input().split()))
field = []
player_position = ()
bunnies_positions = set()
new_bunnies_positions = set()
player_inside_field = True
player_is_dead = False
moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


for row in range(rows):
    field.append([])
    current_row = input()
    for col in range(len(current_row)):
        current_element = current_row[col]
        field[row].append(current_element)
        if current_element == "P":
            player_position = (row, col)
            field[row][col] = "."
        elif current_element == "B":
            bunnies_positions.add((row, col))

directions = input()
for move in directions:
    next_row, next_col = moves[move]
    new_row = player_position[0] + next_row
    new_col = player_position[1] + next_col
    if not position_is_valid(new_row, new_col):
        player_inside_field = False
    else:
        player_position = (new_row, new_col)
    for position in bunnies_positions:
        for direction in moves:
            bunny_row = position[0] + moves[direction][0]
            bunny_col = position[1] + moves[direction][1]
            if position_is_valid(bunny_row, bunny_col):
                field[bunny_row][bunny_col] = "B"
                new_bunnies_positions.add((bunny_row, bunny_col))
    if field[player_position[0]][player_position[1]] == "B":
        player_is_dead = True
    bunnies_positions = bunnies_positions.union(new_bunnies_positions)
    new_bunnies_positions = set()
    if player_is_dead or not player_inside_field:
        break
for row in field:
    print(''.join(row))
if not player_inside_field:
    print(f"won: ", end="")
elif player_is_dead:
    print(f"dead: ", end="")
print(*player_position)

# test inputs:

# 5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR

# 4 5
# .....
# .....
# .B...
# ...P.
# LLLLLLLL

# 5 8
# .......B
# ...B....
# ....B..B
# ........
# ..P.....
# ULLL
