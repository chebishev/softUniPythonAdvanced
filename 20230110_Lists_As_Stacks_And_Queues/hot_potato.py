from collections import deque


class HotPotato:
    def __init__(self):
        self.queue = deque(x for x in input().split())
        self.step = int(input())

    def remove_people(self):
        self.queue.rotate(-self.step)
        name = self.queue.pop()
        return name


hot_potato = HotPotato()
while len(hot_potato.queue) > 1:
    print(f"Removed {hot_potato.remove_people()}")

print(f"Last is {hot_potato.queue.pop()}")

# test inputs:

# Tracy Emily Daniel
# 2

# George Peter Michael William Thomas
# 10

# George Peter Michael William Thomas
# 1


