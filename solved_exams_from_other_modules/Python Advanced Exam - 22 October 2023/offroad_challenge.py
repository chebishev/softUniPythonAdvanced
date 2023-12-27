from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
needed_quantities = deque([int(x) for x in input().split()])

reached_altitudes = []
current_index = 1
while initial_fuel and additional_consumption_index and needed_quantities:
    current_fuel = initial_fuel[-1]
    current_consumption_index = additional_consumption_index[0]
    current_quantity = needed_quantities[0]
    if current_fuel - current_consumption_index >= current_quantity:
        print(f"John has reached: Altitude {current_index}")
        reached_altitudes.append(f"Altitude {current_index}")
        needed_quantities.popleft()
    else:
        break
    current_index += 1
    initial_fuel.pop()
    additional_consumption_index.popleft()

if len(reached_altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
elif not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print(f"John did not reach: Altitude {current_index}")
    print("John failed to reach the top.\nReached altitudes:", ", ".join(reached_altitudes))

# 200 90 40 100
# 20 40 30 50
# 50 60 80 90

# 40 66 123 100
# 10 30 70 33
# 40 55 77 100

# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
