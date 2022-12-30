from collections import deque

players = input().split()
number_to_remove = int(input())
players_queue = deque()

for player in players:
    players_queue.append(player)

counter = 1
while len(players_queue) > 1:
    if counter == number_to_remove:
        removed_player = players_queue.popleft()
        print(f"Removed {removed_player}")
        counter = 1
    else:
        players_queue.append(players_queue.popleft())
        counter += 1

print(f"Last is {players_queue.popleft()}")

# test inputs:

# Tracy Emily Daniel
# 2

# George Peter Michael William Thomas
# 10

# George Peter Michael William Thomas
# 1
