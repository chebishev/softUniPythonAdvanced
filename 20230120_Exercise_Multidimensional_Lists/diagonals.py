rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

left_diagonal = []
right_diagonal = []
for row in range(len(matrix)):
    col = row
    left_diagonal.append(matrix[row][col])
    col = len(matrix[row]) - 1 - row
    right_diagonal.append(matrix[row][col])


print(f"Primary diagonal: {', '.join(str(x) for x in left_diagonal)}. Sum: {sum(left_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in right_diagonal)}. Sum: {sum(right_diagonal)}")

# test inputs:

# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9