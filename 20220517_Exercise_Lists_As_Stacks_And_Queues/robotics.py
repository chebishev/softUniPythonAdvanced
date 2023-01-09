from collections import deque

list_robots = input().split(";")
robots = {}
products = deque()
start_time = [int(x) for x in input().split(":")]
timer = 0  # an alternate time to check if the robot is available. It can be removed if it isn't necessary
for robot in list_robots:
    current_robot = robot.split("-")
    name = current_robot[0]
    process_time = int(current_robot[1])
    timer = process_time
    robots[name] = [process_time, timer, True]

while True:
    command = input()
    if command == "End":
        break
    else:
        products.append(command)

while products:
    start_time[2] += 1
    if start_time[2] == 60:
        start_time[2] = 0
        start_time[1] += 1
        if start_time[1] == 60:
            start_time[1] = 0
            start_time[0] += 1
            if start_time[0] == 24:
                start_time[0] = 0
    # Content in the "robots" dictionary:
    # robots[robot] - the name of the robot as key. The values are in list with 3 elements:
    # robots[robot][0] = processing time
    # robots[robot[1] = timer
    # robots[robot[2] = availability True/False
    for robot in robots.keys():
        if not robots[robot][2]:
            robots[robot][1] -= 1
            if robots[robot][1] <= 0:  # judge has a test case with 0 processing time so this "<" solves the problem
                robots[robot][2] = True
                robots[robot][1] = robots[robot][0]
    for robot in robots.keys():
        if robots[robot][2]:
            print(f"{robot} - {products.popleft()} [{start_time[0]:02d}:{start_time[1]:02d}:{start_time[2]:02d}]")
            robots[robot][2] = False
            break
    else:
        products.rotate(-1)

# test inputs:

# ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End

# ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End
