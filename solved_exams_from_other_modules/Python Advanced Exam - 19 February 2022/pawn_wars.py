from collections import deque


def check_diagonal(indices):
    left_row, left_col, right_row, right_col = indices
    if (current_row + left_row, current_col + left_col) == position[players[1]]:
        return True
    elif (current_row + right_row, current_col + right_col) == position[players[1]]:
        return True


def is_queen():
    next_row = current_row + move[current_player]
    if next_row == 0 \
            or next_row == 7:
        return True


chess_board = []

# initial positions of the players
position = {
    "White": (0, 0),
    "Black": (0, 0)
}
# possible row movements of each player
move = {
    "White": -1,
    "Black": 1
}
# diagonals for eventual capture
diagonals = {
    "White": [-1, -1, -1, 1],
    "Black": [1, 1, 1, -1]
}
# easier way to translate rows, cols into chessboard positions
rows_translate = [8, 7, 6, 5, 4, 3, 2, 1]
cols_translate = ["a", "b", "c", "d", "e", "f", "g"]

# reading the matrix
for row in range(8):
    current_row = input().split()
    chess_board.append(current_row)
    if "w" in current_row:
        # getting position of white player
        position["White"] = (row, current_row.index("w"))
        # getting position of black player
    if "b" in current_row:
        position["Black"] = (row, current_row.index("b"))

# creating deque which will rotate on each move
players = deque(["White", "Black"])

while True:
    current_player = players[0]
    current_row, current_col = position[current_player]

    if check_diagonal(diagonals[current_player]):
        print(f"Game over! {current_player} win, capture on "
              # getting the col, row positions of the other player and turning them into the chess position
              f"{cols_translate[position[players[1]][1]]}{rows_translate[position[players[1]][0]]}.")
        break

    elif is_queen():
        print(f"Game over! {current_player} pawn is promoted to a queen at "
              f"{cols_translate[current_col]}{rows_translate[current_row + move[current_player]]}.")
        break

    else:
        # updating the position of the current player
        position[current_player] = (current_row + move[current_player], current_col)

    # switching players
    players.rotate()

# test inputs:

# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -

# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - w - - - - - -
# - - - - - - - -
