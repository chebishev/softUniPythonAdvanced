print(*set(input() for name in range(int(input()))), sep="\n")

# variant 2:
# print("\n".join(set(input() for name in range(int(input())))))

# variant 3:
# number_of_names = int(input())
# output = {input() for name in range(number_of_names)}
# print(*output, sep="\n")

# test inputs:

# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234

# 10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George
