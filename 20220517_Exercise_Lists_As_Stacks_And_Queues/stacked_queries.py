number_of_queries = int(input())
stack = []
for _ in range(number_of_queries):
    current_query = input()
    if stack:
        if current_query == "2":
            stack.pop()
        elif current_query == "3":
            print(max(stack))
        elif current_query == "4":
            print(min(stack))
        else:
            current_query = current_query.split()
            stack.append(int(current_query[1]))
    else:
        current_query = current_query.split()
        if current_query[0] == "1":
            stack.append(int(current_query[1]))

while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")

# test inputs:

# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
