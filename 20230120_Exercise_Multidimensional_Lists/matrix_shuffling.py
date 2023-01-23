rows, cols = list(map(int, input().split()))
matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])

while True:

    input_line = input()
    if input_line == "END":
        break

    if input_line.startswith("swap "):
        input_line = input_line.split()
        if len(input_line) != 5:
            print("Invalid input!")
            continue
        else:
            action = input_line[0]
            old_row, old_col, new_row, new_col = [int(input_line[x]) for x in range(1, 5)]
            if 0 <= old_row < len(matrix) and 0 <= new_row < len(matrix) \
                    and 0 <= old_col < cols and 0 <= new_col < cols:
                matrix[old_row][old_col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[old_row][old_col]
                for current_row in matrix:
                    print(f"{' '.join(current_row)}")
            else:
                print("Invalid input!")
                continue

# test inputs:

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END

# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
