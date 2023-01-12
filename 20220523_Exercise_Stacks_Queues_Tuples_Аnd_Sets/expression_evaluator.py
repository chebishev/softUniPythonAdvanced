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
            current_numbers.append(result)

    if ch.isdigit():
        current_numbers.append(int(ch))

print(current_numbers.pop())
