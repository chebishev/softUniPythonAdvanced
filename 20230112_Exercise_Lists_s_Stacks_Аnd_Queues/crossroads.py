from collections import deque

green_light_duration = int(input())
additional_time_to_leave_the_crossroad = int(input())
total_cars_passed = []
cars_queue = deque()
crash = False

while True:

    if crash:
        break
    command = input()

    if command == "END":
        print(f"Everyone is safe.\n{len(total_cars_passed)} total cars passed the crossroads.")
        break
    elif command == "green":
        current_green = green_light_duration

        while cars_queue:

            if current_green <= 0:
                break
            current_car = cars_queue.popleft()

            if len(current_car) <= current_green:
                current_green -= len(current_car)
                total_cars_passed.append(current_car)
                continue

            elif current_green < len(current_car):
                crash_index = current_green + additional_time_to_leave_the_crossroad

                if len(current_car) > crash_index:
                    print(f"A crash happened!\n{current_car} was hit at {current_car[crash_index]}.")
                    crash = True
                    break

                else:
                    current_green -= len(current_car)
                    total_cars_passed.append(current_car)
                    continue
    else:
        cars_queue.append(command)

# second solution:
# from collections import deque
#
# green_light_duration = int(input())
# free_window_duration = int(input())
# current_car = ""
# cars_queue = deque()
# cars_passed = []
# crash = False
# while True:
#     if crash:
#         break
#     command = input()
#     if command == "END":
#         print("Everyone is safe.")
#         print(f"{len(cars_passed)} total cars passed the crossroads.")
#         break
#
#     elif command == "green":
#         time = green_light_duration
#         while time:
#             if cars_queue:
#                 current_car = cars_queue.popleft()
#                 cars_passed.append(current_car)
#                 if len(current_car) > time:
#                     current_car = current_car[time:]
#                     time = 0
#                 else:
#                     time -= len(current_car)
#                     if time > 0:
#                         continue
#                     else:
#                         break
#             else:
#                 break
#
#             if current_car:
#                 if len(current_car) > free_window_duration:
#                     current_car = current_car[free_window_duration:]
#                     print("A crash happened!")
#                     print(f"{cars_passed.pop()} was hit at {current_car[0]}.")
#                     crash = True
#                     break
#
#     else:
#         cars_queue.append(command)

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
