import datetime
from collections import deque


def convert_seconds(seconds):
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_dict = {}
robots_info = input().split(";")

# filling the robots in dictionary with name, processing time, timer
for index in range(len(robots_info)):
    robot, processing_time = robots_info[index].split("-")
    robots_dict[robot] = [int(processing_time), 0, True]

start_time = [int(x) for x in input().split(":")]
converted_time = datetime.timedelta(hours=start_time[0], minutes=start_time[1], seconds=start_time[2])
details = deque()

# Filling the details in queue
while True:

    command = input()
    if command == "End":
        break
    details.append(command)

# managing details on every second
while details:
    current_detail = details.popleft()
    converted_time += datetime.timedelta(seconds=1)
    for robot in robots_dict:
        if robots_dict[robot][2]:
            print(f"{robot} - {current_detail} [{convert_seconds(converted_time.seconds)}]")
            robots_dict[robot][2] = False
            break
    else:
        details.append(current_detail)

    # free robot is a robot which robot[2] parameter is True in any other case: timer += 1 sec and the flag is False
    for robot in robots_dict:
        if not robots_dict[robot][2]:
            robots_dict[robot][1] += 1
        if robots_dict[robot][1] >= robots_dict[robot][0]:  # this >= is for robots with processing time 0
            robots_dict[robot][1] = 0
            robots_dict[robot][2] = True

# variant 2: without importing of datetime:
# from collections import deque
#
# list_robots = input().split(";")
# robots = {}
# products = deque()
# start_time = [int(x) for x in input().split(":")]
# timer = 0  # an alternate time to check if the robot is available. It can be removed if it isn't necessary
# for robot in list_robots:
#     current_robot = robot.split("-")
#     name = current_robot[0]
#     process_time = int(current_robot[1])
#     timer = process_time
#     robots[name] = [process_time, timer, True]
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         products.append(command)
#
# while products:
#     start_time[2] += 1
#     if start_time[2] == 60:
#         start_time[2] = 0
#         start_time[1] += 1
#         if start_time[1] == 60:
#             start_time[1] = 0
#             start_time[0] += 1
#             if start_time[0] == 24:
#                 start_time[0] = 0
#     # Content in the "robots" dictionary:
#     # robots[robot] - the name of the robot as key. The values are in list with 3 elements:
#     # robots[robot][0] = processing time
#     # robots[robot[1] = timer
#     # robots[robot[2] = availability True/False
#     for robot in robots.keys():
#         if not robots[robot][2]:
#             robots[robot][1] -= 1
#             if robots[robot][1] <= 0:  # judge has a test case with 0 processing time so this "<" solves the problem
#                 robots[robot][2] = True
#                 robots[robot][1] = robots[robot][0]
#     for robot in robots.keys():
#         if robots[robot][2]:
#             print(f"{robot} - {products.popleft()} [{start_time[0]:02d}:{start_time[1]:02d}:{start_time[2]:02d}]")
#             robots[robot][2] = False
#             break
#     else:
#         products.rotate(-1)

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
