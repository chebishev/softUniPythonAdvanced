lines = int(input())
even_set = set()
odd_set = set()
for row in range(1, lines + 1):
    current_name = input()
    current_sum = int(sum(ord(x) for x in current_name) / row)
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

sum_odd = sum(odd_set)
sum_even = sum(even_set)
result = ""
if sum_odd > sum_even:
    result = odd_set.difference(even_set)
elif sum_even > sum_odd:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.union(even_set)
print(*result, sep=", ")

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
