matrix_size = int(input())
diagonals_dictionary = {
    "left": [],
    "right": [],
    "difference": lambda x, y: abs(sum(x) - sum(y))
}
matrix = [[int(x) for x in input().split()] for row in range(matrix_size)]

for row in range(matrix_size):
    diagonals_dictionary["left"].append(matrix[row][row])
    diagonals_dictionary["right"].append(matrix[row][matrix_size - 1 - row])

print(diagonals_dictionary["difference"](diagonals_dictionary["left"], diagonals_dictionary["right"]))

# test inputs:

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14