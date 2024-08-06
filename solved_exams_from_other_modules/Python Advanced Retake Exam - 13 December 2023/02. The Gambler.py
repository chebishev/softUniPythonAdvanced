board_size = int(input())
game_board = []
player_position = ()
initial_amount = 100
jackpot_won = False

for row in range(board_size):
    game_board.append(list(input()))
    if "G" in game_board[row]:
        player_position = (row, game_board[row].index("G"))
        game_board[row][player_position[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def print_board():
    game_board[player_position[0]][player_position[1]] = "G"
    for row in game_board:
        print("".join(row))


command = input()
# break case 1: end command
while command != "end":

    row = player_position[0] + directions[command][0]
    col = player_position[1] + directions[command][1]

    # break case 2: out of bounds
    if row < 0 or row >= board_size or col < 0 or col >= board_size:
        print("Game over! You lost everything!")
        break

    player_position = (row, col)
    current_element = game_board[row][col]
    if current_element == "W":
        initial_amount += 100
        game_board[row][col] = "-"
    elif current_element == "P":
        initial_amount -= 200
        # break case 3: Penalty
        if initial_amount <= 0:
            print("Game over! You lost everything!")
            break
    elif current_element == "J":
        initial_amount += 100000
        jackpot_won = True
        break

    command = input()
else:
    # only if "end" command is received
    print(f"End of the game. Total amount: {initial_amount}$")
    print_board()

if jackpot_won:
    print(f"You win the Jackpot! End of the game. Total amount: {initial_amount}$")
    print_board()


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
