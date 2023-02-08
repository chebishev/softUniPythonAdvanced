board_size = 6
board = []
for row in range(board_size):
    current_row = input().split()
    board.append(current_row)

points = 0
prizes = {
    "Football": lambda x: x if 100 <= x < 200 else None,
    "Teddy Bear": lambda x: x if 200 <= x < 300 else None,
    "Lego Construction Set": lambda x: x if x >= 300 else None,
}

found_buckets = []
for hit in range(3):
    current_coordinates = input()[1:-1]
    row, col = (int(x) for x in current_coordinates.split(", "))
    if 0 <= row < board_size and 0 <= col < board_size:
        current_try = board[row][col]
        if current_try == "B":
            if (row, col) not in found_buckets:
                found_buckets.append((row, col))
                for index in range(6):
                    if index == row:
                        continue
                    points += int(board[index][col])

for k in prizes:
    if prizes[k](points) is not None:
        print(f"Good job! You scored {points} points, and you've won {k}.")
        break
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")

# test inputs:

# 10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)

# B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)
