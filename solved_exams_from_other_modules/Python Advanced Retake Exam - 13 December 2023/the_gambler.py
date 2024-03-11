board_size = int(input())
board = []
start_position = ()
money = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(board_size):
    current_row = [x for x in input()]
    board.append(current_row)
    if "G" in current_row:
        g_spot = current_row.index("G")
        start_position = (row, g_spot)
        board[row][g_spot] = "-"

command = input()
while command != "end":
    current_row, current_col = start_position
    next_row = current_row + directions[command][0]
    next_col = current_col + directions[command][1]

    if 0 < next_row >= board_size or 0 < next_col >= board_size:
        print("Game over! You lost everything!")
        break

    start_position = (next_row, next_col)
    current_symbol = board[next_row][next_col]
    board[next_row][next_col] = "-"
    if current_symbol == "W":
        money += 100
    elif current_symbol == "P":
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            break
    elif current_symbol == "J":
        money += 100000
        print("You win the Jackpot!")
        break

    command = input()

if money > 0:
    board[start_position[0]][start_position[1]] = "G"
    print(f"End of the game. Total amount: {money}$")
    for row in board:
        print("".join(row))

# test inputs:

# 4
# W-GW
# W--W
# --P-
# ----
# down
# down
# end

# 4
# G---
# WWWW
# P---
# PJ--
# right
# right
# right
# down
# left
# left
# end

# 4
# ---G
# W-W-
# ---P
# --JW
# left
# down
# down
# down
# right
# end
