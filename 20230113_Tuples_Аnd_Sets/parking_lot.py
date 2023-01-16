number_of_cars = int(input())
cars_set = set()
cars = {
    "IN": lambda x: cars_set.add(x),
    "OUT": lambda x: cars_set.remove(x) if x in cars_set else None,
}
for car in range(number_of_cars):
    status, license_plate = input().split(", ")
    cars[status](license_plate)

print(*cars_set, sep="\n") if cars_set else print("Parking Lot is Empty")
###########################################################################
# Another solution:
# cars = int(input())
# cars_set = set()
# for car in range(cars):
#     current_car_info = input().split(", ")
#     operation = current_car_info[0]
#     license_plate = current_car_info[1]
#     if operation == "IN":
#         cars_set.add(license_plate)
#     else:
#         cars_set.remove(license_plate)
#
# if cars_set:
#     print('\n'.join(cars_set))
# else:
#     print("Parking Lot is Empty")
###########################################################################

# test inputs:

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA
