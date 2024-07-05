from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])
delivered_kgs = 0

while packages and couriers:
    current_package = packages.pop()
    current_courier = couriers.popleft()

    if current_courier < current_package:
        current_package -= current_courier
        packages.append(current_package)
        delivered_kgs += current_courier

    elif current_courier > current_package:
        current_courier -= current_package * 2
        if current_courier > 0:
            couriers.append(current_courier)

        delivered_kgs += current_package
    else:
        delivered_kgs += current_package

print(f"Total weight: {delivered_kgs} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(x) for x in packages)}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} "
          f"but there are no more packages to deliver.")

# test inputs:

# 2 4 6 8
# 8 6 4 2

# 13 11 5
# 5 11

# 3 7 14
# 2 2 2 1 7
