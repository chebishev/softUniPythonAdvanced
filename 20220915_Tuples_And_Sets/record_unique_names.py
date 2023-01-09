names = int(input())
names_set = set()
for name in range(names):
    names_set.add(input())

print("\n".join(names_set))

# test inputs:

# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey

# 7
# Lyle
# Bruce
# Alice
# Easton
# Shawn
# Alice
# Shawn

# 6
# Adam
# Adam
# Adam
# Adam
# Adam
# Adam
