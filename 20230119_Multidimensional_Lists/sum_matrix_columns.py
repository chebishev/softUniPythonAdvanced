rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    columns_sum = 0
    for row in range(rows):
        columns_sum += matrix[row][col]
    print(columns_sum)

# test inputs:

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
