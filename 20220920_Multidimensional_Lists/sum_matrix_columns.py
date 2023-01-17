# getting the values of rows and cols from the input
rows, cols = (int(x) for x in input().split(", "))

# filling the matrix with range(rows) with comprehension that takes integer
# for every iteration through the current input().split()
matrix = [[int(x) for x in input().split()] for row in range(rows)]

# getting the columns first to stay on the current column while iterate
# through the rows
for col in range(cols):
    current_col_sum = 0
    for row in range(rows):
        current_col_sum += matrix[row][col]
    print(current_col_sum)

# test inputs:

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
