from collections import deque

seats = input().split(", ")
numbers_left = deque(int(x) for x in input().split(", "))
numbers_right = [int(x) for x in input().split(", ")]
matches = []
rotations = 0

while len(matches) < 3 and rotations < 10:
    left_number = numbers_left.popleft()
    right_number = numbers_right.pop()
    current_letter = chr(left_number + right_number)
    first_combination = str(left_number) + current_letter
    second_combination = str(right_number) + current_letter

    if first_combination in seats:
        seats.remove(first_combination)
        matches.append(first_combination)

    elif second_combination in seats:
        seats.remove(second_combination)
        matches.append(second_combination)

    else:
        numbers_left.append(left_number)
        numbers_right.insert(0, right_number)

    rotations += 1

print(f"Seat matches: {', '.join(matches)}")
print(f'Rotations count: {rotations}')

# test inputs:

# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46

# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40

# 15C, 25C, 36C, 43P, 40E, 38G
# 15, 25, 80, 40, 15, 99, 52
# 15, 42, 29
