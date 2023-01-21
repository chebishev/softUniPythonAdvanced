# getting the values for rows and columns from comma separated string:
rows, columns = [int(x) for x in input().split(", ")]

# filling the matrix with comprehension:
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

# getting the sum of all elements in the matrix without declaring a variable
print(sum((sum(row) for row in matrix)))

# printing the whole matrix as it is
print(matrix)

# older solution:
# rows, cols = (int(x) for x in input().split(", "))
# matrix = []
# matrix_sum = 0
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
#     matrix_sum += sum(matrix[row])
#
# print(matrix_sum)
# print(matrix)

# test inputs:

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
