periodic_table = list((input().split()) for line in range(int(input())))
print(*set(item for sublist in periodic_table for item in sublist), sep="\n")

# variant 2:
# elements_set = set()
# for _ in range(int(input())):
#     for element in input().split():
#         elements_set.add(element)
# print(*elements_set, sep="\n")

# test inputs:

# 4
# Ce O
# Mo O Ce
# Ee
# Mo

# 3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne
