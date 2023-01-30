numbers_list = list(map(int, input().split(", ")))
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)

# test inputs:

# 2, 5, 10

# 4, 5, 6, 1, 3

# 1, 4, 5

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
