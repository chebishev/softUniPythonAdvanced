from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance
    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance == 0:
            continue
        else:
            substances.append(current_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

output = {
    "Tools": tools,
    "Substances": substances,
    "Challenges": challenges
}
for k, v in output.items():
    if v:
        print(f"{k}: {', '.join(str(x) for x in v)}")

# test inputs:

# 2 4 6 8
# 11 3 5 7 9
# 24 28 18 30

# 13 7 4 22 11 15 20
# 3 2 1
# 12 10 5
