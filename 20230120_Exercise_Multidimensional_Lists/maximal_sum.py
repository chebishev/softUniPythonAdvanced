def check_rectangle(row_index, col_index):
    checked_sum = 0
    for checked_row in range(row_index, row_index + 3):
        for checked_col in range(col_index, col_index + 3):
            checked_sum += matrix[checked_row][checked_col]
    return checked_sum


rows, cols = list(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for row in range(rows)]
max_sum = float("-inf")
max_coordinates = []
max_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = check_rectangle(row, col)
        if current_sum > max_sum:
            max_sum = current_sum
            max_coordinates = [row, col]

print(f"Sum = {max_sum}")
final_matrix = []
for row in range(max_coordinates[0], max_coordinates[0] + 3):
    for col in range(max_coordinates[1], max_coordinates[1] + 3):
        final_matrix.append(matrix[row][col])
    print(*final_matrix, sep=" ")
    final_matrix = []

# test inputs:

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
