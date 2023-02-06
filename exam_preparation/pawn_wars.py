from collections import deque


def check_diagonal(coordinates):
    if coordinates == players_info[players[1]]['position']:
        return True


def winning_position():
    x, y = players_info[players[1]]['position']
    return f"{chess_board_dict['cols'][y]}{chess_board_dict['rows'][x]}"


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

chess_board = []
white_position = (0, 0)
black_position = (0, 0)
for row in range(8):
    current_row = input().split()
    chess_board.append(current_row)
    if "w" in current_row:
        white_position = (row, current_row.index("w"))
    if "b" in current_row:
        black_position = (row, current_row.index("b"))

players = deque(["White", "Black"])
players_info = {
    "White": {
        "position": white_position,
        "move": -1,
        "diagonals": {
            "left": (-1, -1),
            "right": (-1, 1)
        },
        "queen": 0
    },
    "Black": {
        "position": black_position,
        "move": 1,
        "diagonals": {
            "left": (-1, -1),
            "right": (-1, 1)
        },
        "queen": 7
    }
}

while True:

    current_player = players[0]
    current_row, current_col = players_info[current_player]['position']
    left_diagonal = (current_row + players_info[current_player]['diagonals']["left"][0],
                     current_col + players_info[current_player]['diagonals']["left"][1])
    right_diagonal = (current_row + players_info[current_player]['diagonals']["right"][0],
                      current_col + players_info[current_player]['diagonals']["right"][1])
    if check_diagonal(left_diagonal):
        square = winning_position()
        print(f"Game over! {current_player} win, capture on {square}.")
        break
    elif check_diagonal(right_diagonal):
        square = winning_position()
        print(f"Game over! {current_player} win, capture on {square}.")
        break

    new_row = current_row + players_info[current_player]['move']
    if new_row == players_info[current_player]["queen"]:
        square = f"{chess_board_dict['cols'][current_col]}{chess_board_dict['rows'][new_row]}"
        print(f"Game over! {current_player} pawn is promoted to a queen at {square}.")
        break

    players_info[current_player]['position'] = (new_row, current_col)
    players.rotate(1)
