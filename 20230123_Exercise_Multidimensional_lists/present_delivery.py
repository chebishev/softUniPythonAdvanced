def position_is_valid(row_index, col_index):
    if 0 <= row_index < neighbourhood_size and 0 <= col_index < neighbourhood_size:
        return True


number_of_presents = int(input())
neighbourhood_size = int(input())
neighbourhood = []
santa_position = []
all_nice_kids = 0
nice_kids_visited = 0
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(neighbourhood_size):
    current_row = input().split()
    neighbourhood.append(current_row)
    if "S" in current_row:
        santa_position = [row, current_row.index("S")]
        neighbourhood[row][santa_position[1]] = "-"
    all_nice_kids += current_row.count("V")

while True:
    command = input()
    if command == "Christmas morning":
        break

    next_row = santa_position[0] + directions[command][0]
    next_col = santa_position[1] + directions[command][1]
    if position_is_valid(next_row, next_col):
        current_position = neighbourhood[next_row][next_col]
        if current_position == "C":
            for position in directions:
                new_row = next_row + directions[position][0]
                new_col = next_col + directions[position][1]
                new_spot = neighbourhood[new_row][new_col]
                if number_of_presents:
                    if new_spot == "V":
                        nice_kids_visited += 1
                        number_of_presents -= 1
                    elif new_spot == "X":
                        number_of_presents -= 1
                    neighbourhood[new_row][new_col] = "-"
                else:
                    break

        elif current_position == "V":
            nice_kids_visited += 1
            number_of_presents -= 1
        neighbourhood[next_row][next_col] = "-"
        santa_position = [next_row, next_col]

    if number_of_presents == 0:
        if all_nice_kids > nice_kids_visited:
            print("Santa ran out of presents!")
        break

neighbourhood[santa_position[0]][santa_position[1]] = "S"
for row in neighbourhood:
    print(' '.join(x for x in row))

if all_nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids - nice_kids_visited} nice kid/s.")