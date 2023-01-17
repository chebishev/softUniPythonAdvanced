first_range, second_range = (int(x) for x in input().split())
first_set = set()
second_set = set()
for _ in range(first_range):
    first_set.add(int(input()))

for _ in range(second_range):
    second_set.add(int(input()))

print(*(first_set.intersection(second_set)), sep="\n")

# variant 2:
# first_range, second_range = (int(x) for x in input().split())
# print(*(set(int(input()) for x in range(first_range)) & (set(int(input()) for x in range(second_range)))), sep="\n")

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
