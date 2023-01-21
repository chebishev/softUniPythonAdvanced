rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([])
    for number in input().split(", "):
        matrix[row].append(int(number))

output_matrix = []
for row in matrix:
    for number in row:
        output_matrix.append(number)

print(output_matrix)

# One row solution:
# print([item for sublist in [[int(x) for x in input().split(", ")] for _ in range(int(input()))] for item in sublist])

# another solution:
# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
#
# print([item for sublist in matrix for item in sublist])

# test inputs:

# 2
# 1, 2, 3
# 4, 5, 6

# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
