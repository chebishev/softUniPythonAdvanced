file = open("numbers.txt", 'r')
numbers_sum = 0

for element in file.read():
    if element.isdigit():
        numbers_sum += int(element)

print(numbers_sum)