first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
sets_of_numbers = {
    "First": first_set,
    "Second": second_set
}
number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    next_step = current_command[1]

    if action == "Add":
        if current_command[2:]:
            for number in current_command[2:]:
                sets_of_numbers[next_step].add(int(number))

    elif action == "Remove":
        if current_command[2:]:
            for number in current_command[2:]:
                current_number = int(number)
                if current_number in sets_of_numbers[next_step]:
                    sets_of_numbers[next_step].remove(current_number)

    elif action == "Check":
        if sets_of_numbers["First"].issubset(sets_of_numbers["Second"]) \
                or sets_of_numbers["Second"].issubset(sets_of_numbers["First"]):
            print("True")
        else:
            print("False")

for key in sets_of_numbers:
    print(*(sorted(sets_of_numbers[key])), sep=", ")

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
