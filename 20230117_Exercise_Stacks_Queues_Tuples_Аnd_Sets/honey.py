from collections import deque


working_bees_queue = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total_honey = 0
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while working_bees_queue and nectar_stack:
    
    current_bee = working_bees_queue.popleft()
    current_nectar = nectar_stack.pop()
    
    if current_nectar < current_bee:
        working_bees_queue.appendleft(current_bee)
        continue
    
    else:
        current_symbol = symbols.popleft()
        if current_symbol == "/" and current_nectar == 0:
            continue
        total_honey += abs(operations[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")
if working_bees_queue:
    print(f"Bees left: {', '.join(str(x) for x in working_bees_queue)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_stack)}")

# test inputs:

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /

# 30
# 15 9 5 150 8
# * + + * -
