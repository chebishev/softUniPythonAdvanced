field_size = int(input())
steps = tuple(x for x in input().split(", "))
field = []
position = ()
hazelnuts = 0

for row in range(field_size):
    field.append([])
    for ch in input():
        field[row].append(ch)
        if ch == 's':
            position = (row, field[row].index(ch))
            field[position[0]][position[1]] = '*'


directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for step in steps:
    current_row, current_col = position
    new_row, new_col = current_row + directions[step][0], current_col + directions[step][1]
    if new_row not in range(field_size) or new_col not in range(field_size):
        print("The squirrel is out of the field.")
        break
    if field[new_row][new_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if field[new_row][new_col] == 'h':
        hazelnuts += 1
        field[new_row][new_col] = '*'
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    position = (new_row, new_col)
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")

# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# ****

# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***

# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
