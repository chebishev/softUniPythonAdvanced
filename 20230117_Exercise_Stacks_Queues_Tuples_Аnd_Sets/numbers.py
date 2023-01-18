first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}
operations_count = int(input())
operations = {
    "Add": {
        "First": lambda x: [first_set.add(number) for number in x],
        "Second": lambda x: [second_set.add(number) for number in x]
    },
    "Remove": {
        "First": lambda x: [first_set.discard(number) for number in x],
        "Second": lambda x: [second_set.discard(number) for number in x],
    },
    "Check Subset": lambda: True if first_set.issubset(second_set) or second_set.issubset(first_set) else False
}

for operation in range(operations_count):

    current_operation = input()

    if current_operation == "Check Subset":
        print(operations[current_operation]())

    else:
        action, choice, *data = current_operation.split()
        operations[action][choice](int(x) for x in data)

for current_set in (first_set, second_set):
    print(*sorted(current_set), sep=", ")

# test inputs:

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
