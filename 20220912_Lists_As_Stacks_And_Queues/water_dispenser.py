from collections import deque

initial_litters = int(input())
names = deque()

while True:
    line = input()
    if line == "Start":
        break

    names.append(line)

while True:

    command = input()
    if command == "End":
        print(f"{initial_litters} liters left")
        break

    command = command.split()
    if command[0] == "refill":
        initial_litters += int(command[1])
    else:
        current_litters = int(command[0])
        current_name = names.popleft()
        if initial_litters - current_litters >= 0:
            initial_litters -= current_litters
            print(f"{current_name} got water")
        else:
            print(f"{current_name} must wait")

# test inputs:

# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End

# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End

