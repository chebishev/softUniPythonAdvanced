from collections import deque


def check_diagonal(player, row, col):
    diagonals_dictionary = {
        "White": {
            "left": (-1, -1),
            "right": (-1, 1)
        },
        "Black": {
            "left": (1, 1),
            "right": (1, -1)
        }
        
    }
    for direction, position in diagonals_dictionary[player].items():
        row_check = row + position[0]
        col_check = col + position[1]
        if chess_board[row_check][col_check] != "-":
            return (True, row_check, col_check)
    else:
        return (False,)


def check_queen(player, row):
    if player == "White" and row == 0:
        return True
    elif player == "Black" and row == 7:
        return True
    return False


chess_board_dict = {
    "rows": {
        0: 8,
        1: 7,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1
    },
    "cols": {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }
}

moves = {
    "White": (-1, 0),
    "Black": (1, 0)
}

players = deque(["White", "Black"])
board_size = 8
chess_board = []

current_positions = {
    "White": [],
    "Black": []
}

for row in range(board_size):
    current_row = input().split()
    chess_board.append(current_row)

    if "w" in current_row:
        current_positions["White"] = [row, current_row.index("w")]

    if "b" in current_row:
        current_positions["Black"] = [row, current_row.index("b")]

while True:

    current_player = players[0]
    current_row = current_positions[current_player][0]
    current_col = current_positions[current_player][1]
    
    result = check_diagonal(current_player, current_row, current_col)
    if result[0]:
        print(f"Game over! {current_player} win, capture on {chess_board_dict['cols'][result[2]]}{chess_board_dict['rows'][result[1]]}.")
        break

    new_row = current_row + moves[current_player][0]
    new_col = current_col + moves[current_player][1]
    
    if check_queen(current_player, new_row):
        print(f"Game over! {current_player} pawn is promoted to a queen at {chess_board_dict['cols'][new_col]}{chess_board_dict['rows'][new_row]}.")
        break

    chess_board[current_row][current_col] = "-"
    current_positions[current_player] = [new_row, new_col]
    chess_board[new_row][new_col] = current_player[0].lower()
    players.rotate(1)

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
