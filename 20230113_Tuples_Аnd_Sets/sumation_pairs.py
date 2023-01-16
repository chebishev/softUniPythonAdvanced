integers_list = [int(x) for x in input().split()]
target_sum = int(input())

while integers_list:
    current_number = integers_list.pop(0)
    for number in integers_list:
        if current_number + number == target_sum:
            print(f"{current_number} + {number} = {target_sum}")
            integers_list.pop(integers_list.index(number))
            break
    if not integers_list:
        break

# test inputs:

# 1 5 4 2 2 3 1 3 2
# 4

# 11 8 5 6 9 2 9 7 3 4
# 11
