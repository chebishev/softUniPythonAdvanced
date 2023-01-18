import functools
from collections import deque

initial_expression = deque(input().split(" "))
current_numbers = []
operations = {
    "+": lambda x: (functools.reduce(lambda a, b: a + b, current_numbers)),
    "-": lambda x: (functools.reduce(lambda a, b: a - b, current_numbers)),
    "*": lambda x: (functools.reduce(lambda a, b: a * b, current_numbers)),
    "/": lambda x: (functools.reduce(lambda a, b: a // b, current_numbers))
}
while len(initial_expression) > 1:

    current_element = initial_expression.popleft()
    current_numbers.append(int(current_element)) if current_element not in "+-*/" else operations[current_element]()
    initial_expression.appendleft(str(current_numbers.pop()))

print(initial_expression)