territory_size = int(input())
snake_position = ()
snake_territory = []
burrows = set()
food_eaten = 0
for row in range(territory_size):
    current_row = input()
    snake_territory.append([ch for ch in current_row])
    for col in range(territory_size):
        current_position = snake_territory[row][col]
        if current_position == "S":
            snake_position = (row, col)
            snake_territory[row][col] = "."
        elif current_position == "B":
            burrows.add((row, col))


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    line = input()
    new_row = snake_position[0] + directions[line][0]
    new_col = snake_position[1] + directions[line][1]
    if 0 <= new_row < territory_size and 0 <= new_col < territory_size:
        current_element = snake_territory[new_row][new_col]
        if current_element == "*":
            food_eaten += 1
            if food_eaten == 10:
                snake_territory[new_row][new_col] = "S"
                print("You won! You fed the snake.")
                break
        elif current_element == "B":
            burrows.remove((new_row, new_col))
            new_position = burrows.pop()
            snake_territory[new_row][new_col] = "."
            snake_territory[new_position[0]][new_position[1]] = "."
            new_row, new_col = new_position

        snake_territory[new_row][new_col] = "."
    else:
        print("Game over!")
        break

    snake_position = (new_row, new_col)

print(f"Food eaten: {food_eaten}")
for row in snake_territory:
    print(''.join(row))

# 6
# -----S
# ----B-
# ------
# ------
# --B---
# --*---
# left
# down
# down
# down
# left

# 7
# --***S-
# --*----
# --***--
# ---**--
# ---*---
# ---*---
# ---*---
# left
# left
# left
# down
# down
# right
# right
# down
# left
# down
