longest_set = set()
for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_range = tuple(int(x) for x in first_range.split(","))
    second_range = tuple(int(x) for x in second_range.split(","))
    first_set = set(x for x in range(first_range[0], first_range[1] + 1))
    second_set = set(x for x in range(second_range[0], second_range[1] + 1))
    current_longest_set = first_set.intersection(second_set)
    if len(current_longest_set) > len(longest_set):
        longest_set = current_longest_set

print(f"Longest intersection is [", end="")
print(*longest_set, sep=', ', end="")
print(f"] with length {len(longest_set)}")

# variant 2:
# rows = int(input())
# longest = []
# for row in range(rows):
#     first_range, second_range = input().split("-")
#     first_start, first_end = (int(x) for x in first_range.split(","))
#     second_start, second_end = (int(x) for x in second_range.split(","))
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
#     result = first_set.intersection(second_set)
#     longest.append(result)
#
# longest = sorted(longest, key=len, reverse=True)
# print(f"Longest intersection is [{', '.join(str(x) for x in longest[0])}] with length {len(longest[0])}")

# test inputs:

# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10

# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11