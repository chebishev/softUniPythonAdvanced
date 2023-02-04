from collections import deque

directions_dictionary = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
deposit_dictionary = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete"
}
deposits = set()
# Rover E; Water W; Metal M; Concrete C; Rock R
field = []
rover_position = []
for row in range(6):
    current_row = input().split()
    field.append(current_row)
    if "E" in current_row:
        rover_position = [row, current_row.index("E")]
        field[rover_position[0]][rover_position[1]] = "-"

directions = deque(x for x in input().split(", "))
while directions:
    row, col = directions_dictionary[directions.popleft()]
    new_row = rover_position[0] + row
    new_col = rover_position[1] + col

    if new_row < 0:
        new_row = 5
    elif new_row > 5:
        new_row = 0

    if new_col < 0:
        new_col = 5
    elif new_col > 5:
        new_col = 0

    current_position = field[new_row][new_col]
    if current_position == "R":
        print(f"Rover got broken at ({new_row}, {new_col})")
        break
    elif current_position in deposit_dictionary:
        deposits.add(deposit_dictionary[current_position])
        print(f"{deposit_dictionary[current_position]} deposit found at ({new_row}, {new_col})")
    rover_position = [new_row, new_col]

if len(deposits) < 3:
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")

# test inputs:

# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left

# R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right

# R - - - - -
# - - C - - -
# - - - - M -
# C - M - R M
# - E - W - -
# - - - - - -
# right, right, up, left, left, left, left, left
