from collections import deque

initial_fuel = [int(x) for x in input().split()]
# additional consumption index
adi = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])
reached_altitudes = []
reached_altitude = True  # ?

for altitude in range(1, 4+1):
    current_altitude = f"Altitude {altitude}"
    current_fuel = initial_fuel.pop()
    current_adi = adi.popleft()
    current_needed_fuel = fuel_needed.popleft()
    result = current_fuel - current_adi
    if result >= current_needed_fuel:
        reached_altitudes.append(current_altitude)
        print(f"John has reached: {current_altitude}")
    else:
        print(f"John did not reach: {current_altitude}")
        print(f"John failed to reach the top.")
        if reached_altitudes:
            print(f"Reached altitudes: {', '.join(reached_altitudes)}")
        else:
            print("John didn't reach any altitude.")
        break
else:
    print(f"John has reached all the altitudes and managed to reach the top!")

# 200 90 40 100
# 20 40 30 50
# 50 60 80 90

# 40 66 123 100
# 10 30 70 33
# 40 55 77 100

# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
