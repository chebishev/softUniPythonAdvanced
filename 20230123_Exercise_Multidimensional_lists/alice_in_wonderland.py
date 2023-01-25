territory_size = int(input())
alice_position = []
territory = []
tea_bags = 0
party = False
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(territory_size):
    current_row = input().split()
    territory.append(current_row)
    if "A" in current_row:
        alice_position = [row, current_row.index("A")]
        territory[row][alice_position[1]] = "*"

while tea_bags < 10:
    row, col = directions[input()]
    next_row = row + alice_position[0]
    next_col = col + alice_position[1]
    if 0 <= next_row < territory_size and 0 <= next_col < territory_size:
        current_step = territory[next_row][next_col]
        territory[next_row][next_col] = "*"
        if current_step == "R":
            break
        if current_step.isdigit():
            tea_bags += int(current_step)
        alice_position = [next_row, next_col]
        if tea_bags >= 10:
            party = True
            break
    else:
        break

if party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in territory:
    print(' '.join(str(x) for x in row))

# test inputs:

# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
