from collections import deque

cups_capacity = deque(int(x) for x in input().split())
filled_bottles = [int(x) for x in input().split()]
water_wasted = 0

while cups_capacity and filled_bottles:
    current_cup = cups_capacity.popleft()
    current_bottle = filled_bottles.pop()

    while current_cup > current_bottle:
        current_cup -= current_bottle
        if filled_bottles:
            current_bottle = filled_bottles.pop()
        else:
            break
    if current_cup <= current_bottle:
        current_bottle -= current_cup
        water_wasted += current_bottle

if filled_bottles:
    print(f"Bottles: {' '.join(str(x) for x in filled_bottles)}")
if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
print(f"Wasted litters of water: {water_wasted}")

# variant 2:
# from collections import deque
#
# cups = deque([int(x) for x in input().split()])
# bottles_stack = [int(x) for x in input().split()]
# wasted_watter = 0
# while cups and bottles_stack:
#     current_cup = cups.popleft()
#     while bottles_stack:
#         current_bottle = bottles_stack.pop()
#         if current_bottle - current_cup < 0:
#             current_cup -= current_bottle
#             continue
#         elif current_bottle - current_cup > 0:
#             current_bottle -= current_cup
#             wasted_watter += current_bottle
#             break
#         else:
#             break
# if cups:
#     print(f"Cups:", *cups, sep=' ')
# elif bottles_stack:
#     print(f"Bottles:", *bottles_stack, sep=" ")
# print(f"Wasted litters of water: {wasted_watter}")

# test inputs:

# 4 2 10 5
# 3 15 15 11 6

# 1 5 28 1 4
# 3 18 1 9 30 4 5

# 10 20 30 40 50
# 20 11
