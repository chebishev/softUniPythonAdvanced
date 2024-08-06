# stack
from collections import deque
# queue
worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
all_worms_fit = True

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches += 1
    else:
        all_worms_fit = False
        current_worm -= 3

        if current_worm <= 0:
            continue
        else:
            worms.append(current_worm)
if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if all_worms_fit and not worms:
    output = "Every worm found a suitable hole!"
else:
    output = f"Worms left: {'none' if not worms else ', '.join(str(x) for x in worms)}"
print(output)
print(f"Holes left: {'none' if not holes else ', '.join(str(x) for x in holes)}")

# test inputs:

# 9 5 8 13
# 13 8 5 6

# 17 20 25 25 30
# 9 8 7 21 5 4 3 2 1

# 9 8 7 6
# 6 7 8 9

# 10 10 10 10
# 5
