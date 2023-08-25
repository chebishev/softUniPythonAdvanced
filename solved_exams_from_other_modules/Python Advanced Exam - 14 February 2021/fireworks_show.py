from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]
fireworks_dictionary = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}
enough_fireworks = False
while firework_effects and explosive_power:
    current_effect = firework_effects.popleft()
    if current_effect <= 0:
        continue
    current_power = explosive_power.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    result = current_effect + current_power
    if result % 5 == 0 and result % 3 == 0:
        fireworks_dictionary["Crossette Fireworks"] += 1
    elif result % 5 == 0:
        fireworks_dictionary["Willow Fireworks"] += 1
    elif result % 3 == 0:
        fireworks_dictionary["Palm Fireworks"] += 1
    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        explosive_power.append(current_power)
    for v in fireworks_dictionary.values():
        if v < 3:
            break
    else:
        enough_fireworks = True
        break

if enough_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for k, v in fireworks_dictionary.items():
    print(f"{k}: {v}")

# test inputs:

# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

# -15, -8, 0, -16, 0, -22
# 10, 5
