rows = int(input())
longest = set()
result = set()
for row in range(rows):
    first_range, second_range = input().split("-")
    first_start, first_end = (int(x) for x in first_range.split(","))
    second_start, second_end = (int(x) for x in second_range.split(","))
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    result = first_set.intersection(second_set)
    if len(result) > len(longest):
        longest = result

print(f"Longest Intersection is [{', '.join(str(x) for x in result)}] with length {len(longest)}")

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
