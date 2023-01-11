from collections import deque


class WaterDispenser:
    def __init__(self):
        self.initial_quantity = int(input())
        self.water_queue = deque()

    def add_people_to_queue(self, name):
        self.water_queue.append(name)

    def want_water(self):
        if self.water_queue:
            return self.water_queue.popleft()


dispenser = WaterDispenser()
COMMAND_START = "Start"
COMMAND_END = "End"
loop_ended = False
while True:
    if loop_ended:
        break
    command = input()

    if command == COMMAND_START:
        while True:
            command = input()
            if command == COMMAND_END:
                print(f"{dispenser.initial_quantity} liters left")
                loop_ended = True
                break
            if command.isdigit():
                wanted_liters = int(command)
                current_name = dispenser.want_water()
                if dispenser.initial_quantity - wanted_liters >= 0:
                    print(f"{current_name} got water")
                    dispenser.initial_quantity -= wanted_liters
                else:
                    print(f"{current_name} must wait")

            else:
                command = command.split()
                dispenser.initial_quantity += int(command[1])

    else:
        dispenser.add_people_to_queue(command)

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
