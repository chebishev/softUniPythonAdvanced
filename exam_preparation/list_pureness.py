import sys
from collections import deque


def best_list_pureness(*args):
    lst = deque(args[0])
    if lst:
        rotations = 0
        pure_rotation = 0
        max_pureness = -sys.maxsize
        if args[1]:
            for _ in range(args[1]):
                current_pureness = sum(index * value for index, value in enumerate(lst))
                if current_pureness > max_pureness:
                    max_pureness = current_pureness
                    pure_rotation = rotations
                lst.rotate()
                rotations += 1
            return f"Best pureness {max_pureness} after {pure_rotation} rotations"
        else:
            return f"Best pureness {sum(index * value for index, value in enumerate(lst))} after {0} rotations"
    else:
        return f"Best pureness {0} after {0} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
