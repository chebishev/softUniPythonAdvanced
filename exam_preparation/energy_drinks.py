from collections import deque

caffeine_milligrams = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))
initial_caffeine = 0
max_caffeine = 300

while caffeine_milligrams and energy_drinks:
    current_milligrams = caffeine_milligrams.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_energy_drink * current_milligrams
    if result + initial_caffeine > 300:
        energy_drinks.append(current_energy_drink)
        initial_caffeine -= 30
        if initial_caffeine < 0:
            initial_caffeine = 0
    else:
        initial_caffeine += result

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")

# test inputs:

# 34, 2, 3
# 40, 100, 250

# 1, 16, 8, 14, 5 
# 27, 23

# 1, 23, 2, 1, 42, 22, 7, 14
# 51, 100, 3, 7