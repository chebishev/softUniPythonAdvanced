from collections import deque


def check_color(color):
    if color in main_colors or color in secondary_colors:
        return True


def check_main(color):
    counter = 0
    for main in secondary_colors[color]:
        if main in output_list:
            counter += 1
    if counter < 2:
        if color in output_list:
            output_list.remove(color)
        return output_list


main_colors = ("red", "yellow", "blue")
secondary_colors = {
    "orange": ["yellow", "red"],
    "purple": ["blue", "red"],
    "green": ["blue", "yellow"]
}
initial_string = deque(x for x in input().split())
output_list = []

while initial_string:
    first_substring = initial_string.popleft()
    if not initial_string:
        second_substring = ""
    else:
        second_substring = initial_string.pop()
    left_first = first_substring + second_substring
    right_first = second_substring + first_substring
    if check_color(left_first):
        output_list.append(left_first)
    elif check_color(right_first):
        output_list.append(right_first)
    else:
        first_substring = first_substring[:-1]
        if first_substring:
            initial_string.insert(len(initial_string) // 2, first_substring)
        second_substring = second_substring[:-1]
        if second_substring:
            initial_string.insert(len(initial_string) // 2, second_substring)

[check_main(color) for color in output_list if color in secondary_colors]
print(output_list)

# test inputs:

# d yel blu e low redd

# r ue nge ora bl ed

# re ple blu pop e pur d
