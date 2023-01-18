initial_string = input().split()
main_colors = {"yellow", "red", "blue"}
mixed_colors = {
    "orange": {"yellow, red"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}
found_colors = []
while initial_string:
    first_part = initial_string.pop(0)
    second_part = initial_string.pop() if initial_string else ""
    left_first = first_part + second_part
    right_first = second_part + first_part
    if left_first in main_colors or left_first in mixed_colors:
        found_colors.append(left_first)
    elif right_first in main_colors or right_first in mixed_colors:
        found_colors.append(right_first)
    else:
        if left_first:
            initial_string.insert(len(initial_string) // 2, first_part[:-1])
        if right_first:
            initial_string.insert(len(initial_string) // 2, second_part[:-1])

for color in mixed_colors:
    if mixed_colors[color] not in found_colors:
        if color in found_colors:
            found_colors.remove(color)

print(found_colors)

# test inputs:

# d yel blu e low redd

# r ue nge ora bl ed

# re ple blu pop e pur d
