from collections import deque

expression = input().split()

current_numbers = deque()
operations_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for ch in expression:
    if ch in "*/+-":
        while len(current_numbers) > 1:
            first_number = current_numbers.popleft()
            second_number = current_numbers.popleft()
            result = operations_dict[ch](first_number, second_number)
            current_numbers.appendleft(result)

    else:
        current_numbers.append(int(ch))

print(abs(current_numbers.pop()))

# test inputs:

# 6 3 - 2 1 * 5 /

# 2 2 - 1 *

# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
