from collections import deque

cups = deque([int(x) for x in input().split()])
bottles_stack = [int(x) for x in input().split()]
wasted_watter = 0
while cups and bottles_stack:
    current_cup = cups.popleft()
    while bottles_stack:
        current_bottle = bottles_stack.pop()
        if current_bottle - current_cup < 0:
            current_cup -= current_bottle
            wasted_watter += current_bottle
            continue
        elif current_bottle - current_cup > 0:
            current_bottle -= current_cup
            wasted_watter += current_cup
            if cups:
                current_cup = cups.popleft()
print(cups)
print(bottles_stack)