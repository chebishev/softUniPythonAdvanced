rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([x for x in input()])

needed_symbol = input()

for row in range(rows):
    if needed_symbol in matrix[row]:
        current_column = matrix[row].index(needed_symbol)
        result = (row, current_column)
        print(result)
        break
else:
    print(f"{needed_symbol} not in the matrix")

# another solution with actual matrix scan row, col by row, col:
# number_of_rows = int(input())
# matrix = []
# output_dict = {}
# for row in range(number_of_rows):
#     matrix.append([x for x in input()])
#
# symbol_to_find = input()
#
# for row in range(number_of_rows):
#     for col in range(len(matrix[row])):
#         if matrix[row][col] == symbol_to_find:
#             output_dict[symbol_to_find] = (row, col)
#             break
#     if output_dict:
#         print(output_dict[symbol_to_find])
#         break
# else:
#     print(f"{symbol_to_find} does not occur in the matrix")

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
