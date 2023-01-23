from collections import deque

rows, cols = [int(x) for x in input().split()]
string = input()
snake_moves = []
letters_queue = deque()

while len(string) < rows * cols:
    string += string

for ch in string:
    letters_queue.append(ch)

for row in range(rows):
    snake_moves.append([])
    for col in range(cols):
        snake_moves[row].append(letters_queue.popleft())
    if row % 2 != 0:
        snake_moves[row] = snake_moves[row][::-1]

for current_row in snake_moves:
    print(f"{''.join(current_row)}")

# test inputs:

# 5 6
# SoftUni

# 1 4
# Python
