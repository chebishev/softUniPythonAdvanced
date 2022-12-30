expression = input()
stack = []
for index in range(len(expression)):
    current_char = expression[index]
    if current_char == "(":
        stack.append(index)
    elif current_char == ")":
        start_index = stack.pop()
        current_expression = expression[start_index:index+1]
        print(current_expression)


# test inputs:

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

# (2 + 3) - (2 + 3)
