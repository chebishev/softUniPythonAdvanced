rows, cols = [int(x) for x in input().split()]
palindrome_matrix = []

for row in range(rows):
    ch_row = row + 97   # for easier conversion to char
    palindrome_matrix.append([])  # creating empty list in the main matrix
    for col in range(cols):
        current_string = chr(ch_row) + chr(ch_row + col) + chr(ch_row)  # concatenating generated letters into string
        palindrome_matrix[row].append(current_string)  # appending current_string to the current row
    print(*palindrome_matrix[row])   # printing current row

# test inputs:

# 4 6

# 3 2
