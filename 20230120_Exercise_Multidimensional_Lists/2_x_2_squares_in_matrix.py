def check_square(row_index, col_index):
    check_equal_values = set()
    current_position = matrix[row_index][col_index]
    right = matrix[row_index][col_index + 1]
    down = matrix[row_index + 1][col_index]
    right_diagonal = matrix[row_index + 1][col_index + 1]
    for item in (current_position, right, down, right_diagonal):
        check_equal_values.add(item)
    if len(check_equal_values) == 1:
        return True

rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]
square_counter = 0

for row in range(rows -1):
    for column in range(columns - 1):
        if check_square(row, column):
            square_counter += 1

print(square_counter)

# test inputs:

# 3 4
# A B B D
# E B B B
# I J B B

# 2 2
# a b
# c d