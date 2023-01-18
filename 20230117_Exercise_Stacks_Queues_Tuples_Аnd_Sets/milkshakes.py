from collections import deque


chocolates_stack = [int(x) for x in input().split(", ")]
cups_of_milk_queue = deque(int(x) for x in input().split(", ")) 
chocolate_milkshakes = 0

while chocolate_milkshakes < 5 and chocolates_stack and cups_of_milk_queue:
    current_chocolate = chocolates_stack.pop()
    current_cup_of_milk = cups_of_milk_queue.popleft()
    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk_queue.appendleft(current_cup_of_milk)
        continue
    elif current_cup_of_milk <= 0:
        chocolates_stack.append(current_chocolate)
        continue

    if current_chocolate == current_cup_of_milk:
        chocolate_milkshakes += 1
    else:
        cups_of_milk_queue.append(current_cup_of_milk)
        chocolates_stack.append(current_chocolate - 5)

if chocolate_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates_stack) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk_queue) or 'empty'}")

# test inputs:

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# -10, -2, -30, 10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
