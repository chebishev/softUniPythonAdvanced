# The first sequence represents the armor of the monsters.
# Each integer value represents the armor of a different monster.
from collections import deque

monsters_armor = deque([int(x) for x in input().split(",")])

# The second sequence represents the soldier's striking impact.
# Each integer value represents the strength of a strike performed by the soldier.
striking_impact = [int(x) for x in input().split(",")]

total_monsters_killed = 0

while monsters_armor and striking_impact:
    current_armor = monsters_armor.popleft()
    current_strike = striking_impact.pop()
    if current_strike >= current_armor:
        current_strike -= current_armor
        total_monsters_killed += 1
        if current_strike > 0:
            if striking_impact:
                next_strike = striking_impact.pop()
                next_strike += current_strike
                striking_impact.append(next_strike)
            else:
                striking_impact.append(current_strike)
        else:
            continue
    else:
        current_armor -= current_strike
        monsters_armor.append(current_armor)

if not monsters_armor:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {total_monsters_killed}")

# test inputs:

# 20,15,10
# 5,15,10,25

# 30,25,40,35
# 15,20,10,30
