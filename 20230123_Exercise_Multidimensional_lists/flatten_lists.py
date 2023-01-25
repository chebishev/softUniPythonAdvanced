print(*[' '.join(element) for element in [string.split() for string in input().split("|")][::-1] if element])

# another version:

# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(string) for string in numbers[::-1] if string])

# test inputs:

# 1 2 3 |4 5 6 |  7  88

# 7 | 4  5|1 0| 2 5 |3

# 1| 4 5 6 7  |  8 9
