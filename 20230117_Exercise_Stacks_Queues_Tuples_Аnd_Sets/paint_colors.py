from collections import deque


initial_string = deque(input().split())

colors = {'yellow', 'red', 'blue', 'green', 'orange', 'purple'}
mixed_colors = {
    'orange': {'yellow', 'red'},
    'purple': {'red', 'blue'},
    'green': {'blue', 'yellow'}
}

found_colors = []

while initial_string:
    first_part = initial_string.popleft()
    second_part = initial_string.pop() if initial_string else ''

    for color in (first_part + second_part, second_part + first_part):
        if color in colors:
            found_colors.append(color)
            break
    else:
        for part in (first_part[:-1], second_part[:-1]):
            if part:
                initial_string.insert(len(initial_string) // 2, part)

for color in set(mixed_colors.keys()).intersection(found_colors):
    if not mixed_colors[color].issubset(found_colors):
        found_colors.remove(color)

print(found_colors)

# test inputs:

# d yel blu e low redd

# r ue nge ora bl ed

# re ple blu pop e pur d
