def numbers_searching(*numbers):
    smallest_number = min(numbers)
    biggest_number = max(numbers)
    output = []
    repeated_numbers = set()
    for number in range(smallest_number, biggest_number + 1):
        if number not in numbers:
            output.append(number)
        if numbers.count(number) > 1:
            repeated_numbers.add(number)
    output.append(sorted(repeated_numbers))
    return output


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
