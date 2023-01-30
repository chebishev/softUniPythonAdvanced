class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative

# test input:

# 1
# 4
# -5
# 3
# 10
