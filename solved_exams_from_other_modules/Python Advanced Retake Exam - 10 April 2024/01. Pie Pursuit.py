from collections import deque

contestants_pies_capacity = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants_pies_capacity and pies:
    current_contestant = contestants_pies_capacity.popleft()
    current_pie = pies.pop()
    if current_contestant >= current_pie:
        current_contestant -= current_pie
        if current_contestant > 0:
            contestants_pies_capacity.append(current_contestant)
    else:
        current_pie -= current_contestant
        if current_pie == 1:
            if pies:
                pies[-1] += 1
            else:
                pies.append(current_pie)
        else:
            pies.append(current_pie)

if not pies and not contestants_pies_capacity:
    print("We have a champion!")
elif contestants_pies_capacity:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(x) for x in contestants_pies_capacity])}")
else:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(x) for x in pies])}")

# test inputs:

# 5 8 4 6
# 3 7 2 9

# 4 6 8 10 12 16
# 16 12 10 8 6 4

# 3 3 3 3 3
# 4 4 4 4
