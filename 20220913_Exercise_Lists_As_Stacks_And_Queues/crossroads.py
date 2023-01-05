from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_queue = deque()
cars_passed = []
while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{len(cars_passed)} total cars passed the crossroads.")
        break
    elif command == "green":
        if cars_queue:
            current_car = cars_queue.popleft()
            cars_passed.append(current_car)
            for second in range(green_light_duration):
                current_car = current_car[1:]
                if not current_car:
                    if cars_queue:
                        current_car = cars_queue.popleft()
                        cars_passed.append(current_car)
                    else:
                        break
            else:
                if current_car:
                    for second in range(free_window_duration):
                        current_car = current_car[1:]
                        if not current_car:
                            break
                    else:
                        if current_car:
                            print("A crash happened!")
                            print(f"{cars_passed.pop()} was hit at {current_car[0]}.")
                            break
    else:
        cars_queue.append(command)

# test inputs:

# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END

# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END
