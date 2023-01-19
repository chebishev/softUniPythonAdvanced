import functools
from collections import deque

initial_expression = deque(input().split(" "))
current_numbers = []
operations = {
    "+": lambda x: (functools.reduce(lambda a, b: a + b, x)),
    "-": lambda x: (functools.reduce(lambda a, b: a - b, x)),
    "*": lambda x: (functools.reduce(lambda a, b: a * b, x)),
    "/": lambda x: (functools.reduce(lambda a, b: a // b, x))
}
while True:

    current_element = initial_expression.popleft()
    if current_element not in "+-*/":
        current_numbers.append(int(current_element))
        if not initial_expression:
            print(current_numbers.pop())
            break
    else:
        initial_expression.appendleft(str(operations[current_element](current_numbers)))
        current_numbers = []

# variant 2:
# from collections import deque

# expression = input().split()

# current_numbers = deque()
# operations_dict = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a // b
# }

# for ch in expression:
#     if ch in "*/+-":
#         while len(current_numbers) > 1:
#             first_number = current_numbers.popleft()
#             second_number = current_numbers.popleft()
#             result = operations_dict[ch](first_number, second_number)
#             current_numbers.appendleft(result)

#     else:
#         current_numbers.append(int(ch))

# print(abs(current_numbers.pop()))

# test inputs:

# 6 3 - 2 1 * 5 /

# 2 2 - 1 *

# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
