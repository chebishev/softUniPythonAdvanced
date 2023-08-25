board_size = 8
chessboard = []
queens_positions = []

for row in range(board_size):
    chessboard.append(input().split())
    for col in range(board_size):
        current_element = chessboard[row][col]
        if current_element == "Q":
            queens_positions.append([row, col])

directions = {
    "up_left": (-1, -1),
    "up": (-1, 0),
    "up_right": (-1, 1),
    "right": (0, 1),
    "down_right": (1, 1),
    "down": (1, 0),
    "down_left": (1, -1),
    "left": (0, -1)
}

winning_queens = []

for queen in queens_positions:
    row, col = queen
    for direction in directions:
        next_row, next_col = row + directions[direction][0], col + directions[direction][1]
        while next_row in range(8) and next_col in range(8):
            current_element = chessboard[next_row][next_col]
            if current_element == "Q":
                break
            elif current_element == "K":
                winning_queens.append([row, col])
                break
            else:
                next_row, next_col = next_row + directions[direction][0], next_col + directions[direction][1]

if winning_queens:
    print(*winning_queens, sep="\n")
else:
    print("The king is safe!")

# test inputs:

# . . . . . . . .
# Q . . . . . . .
# . K . . . Q . .
# . . . Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .

# . . . . . . . .
# . . . Q . . . .
# . . . . . . . .
# . . . . . . . .
# Q . . . Q . . .
# . . K . . . . .
# . . . . . . Q .
# . . . Q . . . .
