from collections import deque

number_of_pumps = int(input())
gas_stations = deque(input() for x in range(number_of_pumps))
liters = 0

current_index = 0
for index in range(len(gas_stations)):
    for station in gas_stations:
        station = station.split()
        liters += int(station[0])
        distance = int(station[1])
        if liters - distance >= 0:
            liters -= distance
            continue
        else:
            gas_stations.rotate(-1)
            liters = 0
            break
    else:
        current_index = index
        break

print(current_index)

# test inputs:

# 3
# 1 5
# 10 3
# 3 4

# 5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9


