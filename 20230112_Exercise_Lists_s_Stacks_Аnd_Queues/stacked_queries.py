lines = int(input())
stack = []
operations = {
    "2": lambda x: x.pop() if x else None,
    "3": lambda x: print(max(x)) if x else None,
    "4": lambda x: print(min(x)) if x else None
}
for _ in range(lines):
    current_line = input().split()
    if current_line[0] == "1":
        stack.append(int(current_line[1]))
    else:
        operations[current_line[0]](stack)
stack.reverse()
print(*stack, sep=", ")
