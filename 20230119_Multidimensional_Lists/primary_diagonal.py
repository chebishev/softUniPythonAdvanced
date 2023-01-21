matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(sum(matrix[row][row] for row in range(len(matrix))))

# test inputs:

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 3
# 1 2 3
# 4 5 6
# 7 8 9
