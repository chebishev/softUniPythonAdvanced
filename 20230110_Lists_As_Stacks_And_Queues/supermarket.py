from collections import deque


class Supermarket:
    def __init__(self):
        self.queue = deque()

    def remaining_people(self):
        return len(self.queue)

    def paying_people(self):
        return self.queue.popleft()

    def add_people(self, name):
        self.queue.append(name)


COMMAND_PAID = "Paid"
COMMAND_END = "End"
supermarket = Supermarket()
while True:
    command = input()

    if command == COMMAND_END:
        print(f"{supermarket.remaining_people()} people remaining.")
        break

    elif command == COMMAND_PAID:
        while supermarket.queue:
            print(supermarket.paying_people())

    else:
        supermarket.add_people(command)

# test inputs:

# George
# Peter
# William
# Paid
# Michael
# Oscar
# Olivia
# Linda
# End

# Anna
# Emma
# Alexander
# End
