# Solution 1: tuple to set
# initial_numbers = tuple(map(float, input().split()))
# counted_numbers = set()
# for number in initial_numbers:
#     if number not in counted_numbers:
#         print(f"{number} - {initial_numbers.count(number)} times")
#         counted_numbers.add(number)
############################################################

# Solution 2: list to list with tuples
# numbers_list = [float(x) for x in input().split()]
# output_list = []
#
# for number in numbers_list:
#     current_count = numbers_list.count(number)
#     current_tuple = (number, current_count)
#     if current_tuple not in output_list:
#         output_list.append(current_tuple)
#
# for row in output_list:
#     print(f"{row[0]} - {row[1]} times")
###########################################################

# Solution 3: tuple to dictionary:
numbers_row = tuple(float(x) for x in input().split())
output_dict = {k: numbers_row.count(k) for k in numbers_row}
for number in output_dict:
    print(f"{number} - {output_dict[number]} times" for number in output_dict)

# test inputs:

# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
