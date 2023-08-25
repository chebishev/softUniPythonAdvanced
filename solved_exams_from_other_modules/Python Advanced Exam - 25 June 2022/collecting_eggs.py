from collections import deque

egg_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = [int(x) for x in input().split(", ")]
box_size = 50
filled_boxes = 0

while egg_sizes and paper_sizes:
    egg = egg_sizes.popleft()
    if egg == 13:
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue
    elif egg <= 0:
        continue

    paper = paper_sizes.pop()
    if egg + paper <= box_size:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if egg_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in egg_sizes)}")
elif paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")

# test inputs:

# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

# 2, 4, 7, 8, 0
# 5, 6, 2

# 12, 23
# 28, 40
