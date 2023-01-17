matrix = [[int(x) for x in input().split()] for row in range(int(input()))]
diagonal_sum = 0

for row in range(len(matrix)):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)

# test inputs:

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 3
# 1 2 3
# 4 5 6
# 7 8 9
