from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
current_car = ""
cars_queue = deque()
cars_passed = []
crash = False
while True:
    if crash:
        break
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{len(cars_passed)} total cars passed the crossroads.")
        break

    elif command == "green":
        time = green_light_duration
        while time:
            if cars_queue:
                current_car = cars_queue.popleft()
                cars_passed.append(current_car)
                if len(current_car) > time:
                    current_car = current_car[time:]
                    time = 0
                else:
                    time -= len(current_car)
                    if time > 0:
                        continue
                    else:
                        break
            else:
                break

            if current_car:
                if len(current_car) > free_window_duration:
                    current_car = current_car[free_window_duration:]
                    print("A crash happened!")
                    print(f"{cars_passed.pop()} was hit at {current_car[0]}.")
                    crash = True
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
