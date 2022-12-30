from collections import deque

queue = deque()

while True:
    line = input()
    if line == "End":
        print(f"{len(queue)} people remaining.")
        break
    if line == "Paid":
        print("\n".join(queue))
        queue.clear()
    else:
        queue.append(line)

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
