numbers_list = [float(x) for x in input().split()]
output_list = []

for number in numbers_list:
    current_count = numbers_list.count(number)
    current_tuple = (number, current_count)
    if current_tuple not in output_list:
        output_list.append(current_tuple)

for row in output_list:
    print(f"{row[0]} - {row[1]} times")

# test inputs:

# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
