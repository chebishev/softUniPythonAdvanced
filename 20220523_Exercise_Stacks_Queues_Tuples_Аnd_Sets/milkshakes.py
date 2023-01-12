from collections import deque

chocolates_stack = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))
chocolate_milkshakes = 0
milkshakes_needed = False
while chocolates_stack and cups_of_milk:
    current_chocolate = chocolates_stack.pop()
    current_cup_of_milk = cups_of_milk.popleft()
    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue
    elif current_cup_of_milk <= 0:
        chocolates_stack.append(current_chocolate)
        continue

    if current_chocolate == current_cup_of_milk:
        chocolate_milkshakes += 1
        if chocolate_milkshakes == 5:
            milkshakes_needed = True
            break
    else:
        cups_of_milk.append(current_cup_of_milk)
        current_chocolate -= 5
        chocolates_stack.append(current_chocolate)

if milkshakes_needed:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print("Chocolate: ", end="")
if chocolates_stack:
    print(*chocolates_stack, sep=", ")
else:
    print("empty")

print("Milk: ", end="")
if cups_of_milk:
    print(*cups_of_milk, sep=", ")
else:
    print("empty")

# test inputs:

# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55

# -10, -2, -30, 10
# -5

# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
