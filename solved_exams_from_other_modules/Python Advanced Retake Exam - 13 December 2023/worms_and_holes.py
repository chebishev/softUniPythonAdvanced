from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
removed_worms = False

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_hole != current_worm:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)
        else:
            removed_worms = True
    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if not worms and not removed_worms:
    print("Every worm found a suitable hole!")
elif not worms and removed_worms:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")

# test input
# 9 5 8 13
# 13 8 5 6

# 17 20 25 25 30
# 9 8 7 21 5 4 3 2 1

# 9 8 7 6
# 6 7 8 9

# 10 10 10 10
# 5
