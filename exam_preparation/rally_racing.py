matrix_size = int(input())
racing_number = input()
start_coordinates = (0, 0)
last_position = ()
distance_covered = 0
# + 10 kilometers on each direction
# + 30 kilometers when Tunnel is reached
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0), 
    "down": (1, 0)
}
tunnels = set()
matrix = []
finish_reached= False
for row in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    for ch in current_row:
        if ch == "T":
            tunnels.add((row, current_row.index(ch)))

while True:

    direction = input()
    
    if direction == "End":
        matrix[start_coordinates[0]][start_coordinates[1]] = "C"
        if finish_reached:
            print(f"Racing car {racing_number} finished the stage!")
        else:
            print(f"Racing car {racing_number} DNF.")
        break

    next_row = start_coordinates[0] + directions[direction][0]
    next_col = start_coordinates[1] + directions[direction][1]
    current_move = matrix[next_row][next_col]
    last_position = (next_row, next_col)
    
    if current_move == "F":
        finish_reached = True
        distance_covered += 10
    
    elif current_move == "T":
        current_tunnel = {(next_row, next_col)}
        second_tunnel = tunnels.difference(current_tunnel)
        matrix[next_row][next_col] = "."
        last_position = (second_tunnel[0], second_tunnel[1])
        distance_covered += 30
    
    matrix[last_position[0]][last_position[1]] = "."
    start_coordinates = last_position

# test inputs:
# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End	

# 10
# 45
# . . . . . . . . . . 
# . . T . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . F . . .
# . . . . . . . . . .
# . . . . . . . . . . 
# . . . . . . . T . .
# right
# down
# down
# right
# up
# left
# up
# up
# End