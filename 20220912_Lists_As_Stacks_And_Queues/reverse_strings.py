string_to_reverse = input()
stack = []
# adding to stack char by char
for char in string_to_reverse:
    stack.append(char)

# printing the reversed string:
while stack:
    print(stack.pop(), end="")

# test inputs:

# I Love Python

# Stacks and Queues
