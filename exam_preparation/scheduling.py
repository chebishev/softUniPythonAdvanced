from collections import deque

jobs = deque(int(x) for x in input().split(", "))
index = int(input())
clock_cycles = 0
final_number = jobs[index]

for number in range(1, final_number + 1):
    if number not in jobs:
        continue
    found_index = jobs.count(number)
    for _ in range(found_index):
        while jobs[index] != number:
            jobs.rotate(-1)
        clock_cycles += number

print(clock_cycles)

# test inputs:

# 3, 1, 10, 1, 2
# 0

# 4, 10, 10, 6, 2, 99
# 2
