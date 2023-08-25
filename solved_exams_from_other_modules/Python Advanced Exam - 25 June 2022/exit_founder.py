from collections import deque

players = deque(input().split(", "))
maze_board = []
resting_players = []
for index in range(6):
    current_row = input().split()
    maze_board.append(current_row)

while True:
    current_player = players[0]
    row, col = [int(ch) for ch in input() if ch.isdigit()]
    current_move = maze_board[row][col]
    if current_player not in resting_players:
        if current_move == "E":
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif current_move == "T":
            print(f"{current_player} is out of the game! The winner is {players[1]}.")
            break
        elif current_move == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            resting_players.append(current_player)
            players.rotate(1)
        else:
            players.rotate(1)
    else:
        players.rotate(1)
        resting_players.remove(current_player)

# test inputs:

# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)

# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)

# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
