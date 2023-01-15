from collections import deque

food_quantity = int(input())
food_queue = deque(int(x) for x in input().split())
print(max(food_queue))

while food_queue:
    current_order = food_queue.popleft()
    if food_quantity - current_order < 0:
        food_queue.appendleft(current_order)
        break
    elif food_quantity - current_order == 0:
        food_quantity -= current_order
        break
    else:
        food_quantity -= current_order

if food_queue:
    print("Orders left:", *food_queue, sep=" ")
else:
    print("Orders complete")

# test inputs:

# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76 100 50
