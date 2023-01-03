from collections import deque

number_of_petrol_pumps = int(input())
petrol_pumps = deque()
for pump in range(number_of_petrol_pumps):
    information = input().split()
    amount_of_petrol = int(information[0])
    distance_to_next = int(information[1])
    petrol_pumps.append({"petrol": amount_of_petrol, "distance": distance_to_next})

for index in range(len(petrol_pumps)):
    next_is_possible = True
    fuel = 0
    distance = 0
    for pump in range(len(petrol_pumps)):
        fuel += petrol_pumps[pump]["petrol"]
        distance = petrol_pumps[pump]["distance"]
        if fuel < distance:
            next_is_possible = False
            break
        else:
            fuel -= distance
    if next_is_possible:
        print(index)
        break
    else:
        petrol_pumps.rotate(-1)

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
