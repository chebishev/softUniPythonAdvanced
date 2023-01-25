matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for line in range(matrix_size)]
operations = {
    "Add": lambda x, y: x + y,
    "Subtract": lambda x, y: x - y
}

while True:
    command = input()
    if command == "END":
        break

    action, *args = command.split()
    row, col, second_number = (int(x) for x in args)
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        matrix[row][col] = operations[action](matrix[row][col], second_number)
    else:
        print("Invalid coordinates")

for row in matrix:
    print(" ".join(str(x) for x in row))

# test inputs:

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
