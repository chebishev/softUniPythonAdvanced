def position_is_valid(row_index, col_index):
    if 0 <= row_index < neighbourhood_size and 0 <= col_index < neighbourhood_size:
        return True


def cookie_found(row_index, col_index, presents, kids):
    cookie_radius = (
        (0, 0),  # current_position
        (-1, -1),  # up_left_diagonal
        (-1, 0),  # up
        (-1, 1),  # up_right_diagonal
        (0, -1),  # left
        (0, 1),  # right
        (1, -1),  # down_left_diagonal
        (1, 0),  # down
        (1, 1)  # down_right_diagonal
    )
    for position in cookie_radius:
        new_row = row_index + position[0]
        new_col = col_index + position[1]
        new_spot = neighbourhood[new_row][new_col]
        if position_is_valid(new_row, new_col):
            if presents:
                if new_spot == "V":
                    presents -= 1
                    kids += 1
                elif new_spot == "X":
                    presents -= 1
                neighbourhood[new_row][new_col] = "-"
        if not presents:
            return presents, kids
        return presents, kids


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
            number_of_presents, nice_kids_visited = cookie_found(next_row, next_col, number_of_presents, nice_kids_visited)

        elif current_position == "V":
            nice_kids_visited += 1
        neighbourhood[next_row][next_col] = "-"
        santa_position = [next_row, next_col]

    if number_of_presents == 0:
        if all_nice_kids > nice_kids_visited:
            print("Santa ran out of presents!")
        break

neighbourhood[santa_position[0]][santa_position[1]] = "S"
for row in neighbourhood:
    print(' '.join(x for x in row))
