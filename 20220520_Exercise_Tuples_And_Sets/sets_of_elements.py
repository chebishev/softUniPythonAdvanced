first_range, second_range = [int(x) for x in input().split()]
print(*(set(int(input()) for x in range(first_range)).intersection(set(int(input()) for x in range(second_range)))), sep="\n")

# test inputs:

# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5

# 2 2
# 1
# 3
# 1
# 5
