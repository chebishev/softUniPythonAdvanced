import sys


def valid_start_index(current_row, current_col):
    if current_row < len(matrix) - 1 and current_col < len(matrix[row]) - 1:
        return True


rows, cols = (int(x) for x in input().split(", "))
matrix = []
sub_matrix = []
# This will be the square that we will move:
# Current position, right, current_down, current_right_diagonal
directions = ((0, 0), (0, 1), (1, 0), (1, 1))
max_sum = -sys.maxsize
# filling the matrix
for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows):
    for col in range(cols):

        if valid_start_index(row, col):
            current_position = matrix[row + directions[0][0]][col + directions[0][1]]
            step_right = matrix[row + directions[1][0]][col + directions[1][1]]
            down_from_current = matrix[row + directions[2][0]][col + directions[2][1]]
            right_diagonal = matrix[row + directions[3][0]][col + directions[3][1]]
            current_sum = current_position + step_right + down_from_current + right_diagonal

            if current_sum > max_sum:
                max_sum = current_sum
                sub_matrix = [[current_position, step_right], [down_from_current, right_diagonal]]

print(*sub_matrix[0], sep=" ")
print(*sub_matrix[1], sep=" ")
print(max_sum)

# test inputs:

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
