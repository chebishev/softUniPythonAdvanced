board_size = int(input())
chess_board = []
for row in range(board_size):
    chess_board.append([])
    current_row = input()
    for col in current_row:
        chess_board[row].append(col)

possible_moves = (
    (-2, -1),   # up left
    (-2, 1),     # up right
    (-1, -2),    # left up
    (-1, 2),    # right up
    (1, -2),    # left down
    (1, 2),     # right down
    (2, -1),    # down left
    (2, 1)      # down right
)

knights_to_be_removed = set()
while True:
    max_attacks = 0
    max_attacks_horse = []

    for row in range(board_size):
        for col in range(board_size):
            if chess_board[row][col] == "K":
                current_attacks = 0

                for position in possible_moves:
                    new_row = row + position[0]
                    new_col = col + position[1]
                    if 0 <= new_col < board_size and 0 <= new_row < board_size:
                        if chess_board[new_row][new_col] == "K":
                            current_attacks += 1

                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    max_attacks_horse = (row, col)

    if max_attacks_horse:
        knights_to_be_removed.add(max_attacks_horse)
        chess_board[max_attacks_horse[0]][max_attacks_horse[1]] = "0"
    else:
        break

print(len(knights_to_be_removed))

# test inputs:

# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# 2
# KK
# KK

# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
