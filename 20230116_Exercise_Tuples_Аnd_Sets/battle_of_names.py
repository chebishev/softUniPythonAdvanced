number_of_names = int(input())
odd_set = set()
even_set = set()

for row in range(1, number_of_names + 1):
    name = input()
    sum_ascii = sum(ord(ch) for ch in name) // row
    even_set.add(sum_ascii) if sum_ascii % 2 == 0 else odd_set.add(sum_ascii)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

# variant 2:
# lines = int(input())
# even_set = set()
# odd_set = set()
# for row in range(1, lines + 1):
#     current_name = input()
#     current_sum = int(sum(ord(x) for x in current_name) / row)
#     if current_sum % 2 == 0:
#         even_set.add(current_sum)
#     else:
#         odd_set.add(current_sum)
#
# sum_odd = sum(odd_set)
# sum_even = sum(even_set)
# result = ""
# if sum_odd > sum_even:
#     result = odd_set.difference(even_set)
# elif sum_even > sum_odd:
#     result = odd_set.symmetric_difference(even_set)
# else:
#     result = odd_set.union(even_set)
# print(*result, sep=", ")

# test inputs:

# 4
# Pesho
# Stefan
# Stamat
# Gosho

# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
