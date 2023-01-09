from collections import deque

food_for_the_day = int(input())
orders = list(map(int, input().split()))
print(max(orders))
queue = deque()
for order in orders:
    queue.append(order)

while queue:
    current_order = queue.popleft()
    if current_order <= food_for_the_day:
        food_for_the_day -= current_order
    else:
        queue.appendleft(current_order)
        break

if queue:
    print(f"Orders left: ", end="")
    while queue:
        print(queue.popleft(), end=" ")
else:
    print("Orders complete")

# test inputs:

# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76 100 50
