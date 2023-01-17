number_of_rows = int(input())
matrix = []
output_dict = {}
for row in range(number_of_rows):
    matrix.append([x for x in input()])

symbol_to_find = input()

for row in range(number_of_rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol_to_find:
            output_dict[symbol_to_find] = (row, col)
            break
    if output_dict:
        print(output_dict[symbol_to_find])
        break
else:
    print(f"{symbol_to_find} does not occur in the matrix")

# test inputs:

# 3
# ABC
# DEF
# X!@
# !

# 4
# asdd
# xczc
# qwee
# qefw
# 4
