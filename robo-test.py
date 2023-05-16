from collections import deque


# convert passed_seconds to time after adding them to the initial time
def get_time(added_seconds):
    hours, minutes, seconds = int(time[0]), int(time[1]), int(time[2])
    seconds += added_seconds
    if seconds > 59:
        seconds -= 60
        minutes += 1
    if minutes > 59:
        minutes -= 60
        hours += 1
    if hours > 23:
        hours -= 24
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# getting the robots raw list
robots_list = input().split(";")
# empty dictionary that will become nested one, containing time, timer and status of each robot
# the timer will be used to check when the robot is free
robots_dict = {}

for robot in robots_list:

    robot_name, robot_time = robot.split("-")

    robots_dict[robot_name] = {
        "processing_time": int(robot_time),
        "timer": int(robot_time),
        "status": True
    }

# getting the time as string
# it will be used in a function in the printing
time = input().split(":")

# This will be the queue of the products
products = deque()

# getting the products from the input
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

# here we will store all the seconds that the robots need to process the products
seconds_passed = 0

while products:
    seconds_passed += 1
    # getting the first product in the queue
    current_product = products.popleft()

    # checking for free robot to process the product
    for robot in robots_dict:

        if robots_dict[robot]["status"]:
            # mark that robot as busy until the timer hits 0 or below
            robots_dict[robot]["status"] = False
            # printing the message on the console
            print(f"{robot} - {current_product} [{get_time(seconds_passed)}]")
            break
    else:
        # if the loop has no breaks we return the product at the end of the queue
        products.append(current_product)

    # each second(each iteration of the while loop) we are decreasing the timers of the busy robots with one
    # and check if they became 0 or less in order to change their status to "free" (True)
    for robot in robots_dict:
        if not robots_dict[robot]["status"]:
            robots_dict[robot]["timer"] -= 1
        if robots_dict[robot]["timer"] <= 0:
            robots_dict[robot]["status"] = True
            robots_dict[robot]["timer"] = robots_dict[robot]["processing_time"]

# test_input:

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
