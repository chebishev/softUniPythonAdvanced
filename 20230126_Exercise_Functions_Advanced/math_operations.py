from collections import deque


def math_operations(*numbers, **operations):
    operations_queue = deque(x for x in operations)  # to get only the letters and to rotate them
    operators = {
        "a": lambda x, y: x + y,
        "s": lambda x, y: x - y,
        "d": lambda x, y: x / y,
        "m": lambda x, y: x * y
    }

    for number in numbers:
        operation = operations_queue[0]  # getting the first letter in the queue
        first_number = operations[operation]   # getting the number corresponding to that letter in the dictionary
        if number == 0 and operation == "d":   # check for zero division
            operations_queue.rotate(-1)     # rotating the que
            continue   # skipping this step
        second_number = number  # this is just for more readability
        # getting the dict value       calling the lambda with the given numbers
        operations[operation] = operators[operation](first_number, second_number)
        operations_queue.rotate(-1)  # rotating the queue

    sorted_operations = dict(sorted(operations.items(), key=lambda x: (-x[1], x[0])))
    output_list = []
    for k, v in sorted_operations.items():
        output_list.append(f"{k}: {v:.1f}")
    return '\n'.join(output_list)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
