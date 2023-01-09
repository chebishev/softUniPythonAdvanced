numbers = [int(x) for x in input().split()]
print(numbers)
target_number = int(input())
pair_found = False
while numbers:
    for index in range(len(numbers)):
        first_number = numbers[index]
        for second_number in range(index + 1, len(numbers)):
            current_number = numbers[second_number]
            if first_number + current_number == target_number:
                print(f"{first_number} + {current_number} = {target_number}")
                numbers.pop(second_number)
                numbers.pop(index)
                pair_found = True
                break
        else:
            numbers.pop(index)
            break
        if pair_found:
            break

# No judge for this problem, so
# test inputs:

# 1 5 4 2 2 3 1 3 2
# 4

# 11 8 5 6 9 2 9 7 3 4
# 11
