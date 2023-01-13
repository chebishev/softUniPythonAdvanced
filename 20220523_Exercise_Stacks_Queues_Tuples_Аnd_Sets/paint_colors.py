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


main_colors = tuple(["red", "yellow", "blue"])
secondary_colors = {
    "orange": ["yellow", "red"],
    "purple": ["blue", "red"],
    "green": ["blue", "yellow"]
}
initial_string = deque(x for x in input().split())
output_list = []

while initial_string:
    if len(initial_string) == 1:
            current_color = initial_string.pop()
            if check_color(current_color):
                output_list.append(current_color)
            else:
                break
    first_substring = initial_string.popleft()
    second_substring = initial_string.pop()
    left_first = first_substring + second_substring
    right_first = second_substring + first_substring
    if check_color(left_first):
        output_list.append(left_first)
        continue
    elif check_color(right_first):
        output_list.append(right_first)
        continue
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]
        if len(first_substring) == 0 and len(second_substring) == 0:
            break
        if len(initial_string) > 0 and len(initial_string) % 2 != 0:
            index = (len(initial_string) // 2)  + 1
        else:
            index = len(initial_string) // 2
        initial_string.insert(index, first_substring)
        initial_string.insert(index, second_substring)

for key in secondary_colors:
    check_main(key)
print(output_list)

# test inputs:

# d yel blu e low redd

# r ue nge ora bl ed

# re ple blu pop e pur d
