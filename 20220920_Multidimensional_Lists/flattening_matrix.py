rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

print([item for sublist in matrix for item in sublist])
# print([item for row in matrix for item in row])

# it's the same as:
# flatten_list = []
# for sublist in matrix:
#     for item in sublist:
#         flatten_list.append(item)

# test inputs:

# 2
# 1, 2, 3
# 4, 5, 6

# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
