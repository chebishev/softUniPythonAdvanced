def operate(*args):
    operator = args[0]
    numbers = list(args[1:])

    def sum_numbers():
        return sum(numbers)

    def subtract_numbers():
        result = numbers.pop(0)
        for number in numbers:
            result -= number
        return result

    def multiply_numbers():
        result = 1
        for number in numbers:
            result *= number
        return result

    def divide_numbers():
        first_number = numbers.pop(0)
        for number in numbers:
            first_number /= number
        return first_number

    if operator == "+":
        return sum_numbers()
    elif operator == "-":
        return subtract_numbers()
    elif operator == "*":
        return multiply_numbers()
    elif operator == "/":
        return divide_numbers()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
