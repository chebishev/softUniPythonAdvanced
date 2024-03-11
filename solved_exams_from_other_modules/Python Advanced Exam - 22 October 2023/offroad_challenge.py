from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
needed_quantities = deque([int(x) for x in input().split()])

reached_altitudes = []

for index in range(1, 5):
    current_fuel = initial_fuel.pop()
    current_consumption_index = additional_consumption_index.popleft()
    current_quantity = needed_quantities.popleft()
    if current_fuel - current_consumption_index >= current_quantity:
        print(f"John has reached: Altitude {index}")
        reached_altitudes.append(f"Altitude {index}")
    else:
        print(f"John did not reach: Altitude {index}")
        if not reached_altitudes:
            print("John failed to reach the top.\nJohn didn't reach any altitude.")
            break
        else:
            print("John failed to reach the top.\nReached altitudes:", ", ".join(reached_altitudes))
            break
else:
    print("John has reached all the altitudes and managed to reach the top!")

# 200 90 40 100
# 20 40 30 50
# 50 60 80 90

# 40 66 123 100
# 10 30 70 33
# 40 55 77 100

# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
