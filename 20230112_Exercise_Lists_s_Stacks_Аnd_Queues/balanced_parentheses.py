parentheses = input()
stack = []
dictionary = {
    ")": "(",
    "]": "[",
    "}": "{"
}
for ch in parentheses:
    if ch in "{[(":
        stack.append(ch)
    else:
        if stack:
            current_open = stack.pop()
            if current_open == dictionary[ch]:
                continue
            else:
                print("NO")
                break
        else:
            print("NO")
            break
else:
    print("YES")

# test inputs:

# {[()]}

# {[(])}

# {{[[(())]]}}

