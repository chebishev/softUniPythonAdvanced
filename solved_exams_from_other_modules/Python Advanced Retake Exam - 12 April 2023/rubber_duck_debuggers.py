from collections import deque

time_for_task = deque([int(x) for x in input().split(" ")])
number_of_tasks = [int(x) for x in input().split(" ")]

ducks = {
    "Darth Vader Ducky": {
        'time': range(0, 61),
        'count': 0
    },
    "Thor Ducky": {
      'time': range(61, 121),
      'count': 0
    },
    "Big Blue Rubber Ducky": {
      'time': range(121, 181),
      'count': 0
    },
    "Small Yellow Rubber Ducky": {
      'time': range(181, 241),
      'count': 0
    }
}
while time_for_task and number_of_tasks:
    current_time = time_for_task.popleft()
    current_number = number_of_tasks.pop()
    result = current_time * current_number

    for duck in ducks:
        if result in ducks[duck]['time']:
            ducks[duck]['count'] += 1
            break
    else:
        current_number -= 2
        time_for_task.append(current_time)
        number_of_tasks.append(current_number)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck in ducks:
    print(f'{duck}: {ducks[duck]["count"]}')

# test inputs:

# 10 15 12 18 22 6
# 12 16 5 6 9 1
#
# 2 55 17 31 23
# 7 5 17 4 27
