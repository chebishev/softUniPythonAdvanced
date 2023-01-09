parentheses = input()
stack = []
dictionary = {"[": "]", "{": "}", "(": ")"}
match = False
for item in parentheses:
    if item in "[({":
        stack.append(item)
    else:
        if stack:
            current_key = stack.pop()
            if dictionary[current_key] == item:
                match = True
            else:
                match = False
                break
        else:
            match = False

if not match or stack:
    print("NO")
elif match:
    print("YES")

# test inputs:

# {[()]}

# {[(])}

# {{[[(())]]}}
