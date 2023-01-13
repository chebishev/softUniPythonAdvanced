from collections import deque


working_bees = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())
honey_made = 0
loop_interupted = False
operations_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while working_bees and nectar_stack:
    current_bee = working_bees.popleft()
    current_nectar = nectar_stack.pop()
    while current_nectar < current_bee:
        if nectar_stack:
            current_nectar = nectar_stack.pop()
        else:
            loop_interupted = True
            working_bees.appendleft(current_bee)
            break
    if loop_interupted:
        break
    current_symbol = symbols.popleft()
    if current_symbol == "/":
        if current_nectar == 0:
            continue
    honey_made += abs(operations_dict[current_symbol](current_bee, current_nectar))
    
print(f"Total honey made: {honey_made}")
if working_bees:
    print(f"Bees left: ", end="")
    print(*working_bees, sep=", ")
if nectar_stack:
    print(f"Nectar left: ", end="")
    print(*nectar_stack, sep=", ")

# test inputs:

# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /

# 30
# 15 9 5 150 8
# * + + * -
