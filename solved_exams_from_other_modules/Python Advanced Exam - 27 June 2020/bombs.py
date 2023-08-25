from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]
bombs = {
    60: "Cherry Bombs",
    40: "Datura Bombs",
    120: "Smoke Decoy Bombs"
}
created_bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bombs_quota = set()

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    matching_sum = current_effect + current_casing

    for k in bombs:
        if matching_sum == k:
            created_bombs[bombs[k]] += 1
            if created_bombs[bombs[k]] == 3:
                bombs_quota.add(bombs[k])
            break
    else:
        current_casing -= 5
        bomb_casings.append(current_casing)
        bomb_effects.appendleft(current_effect)
    if len(bombs_quota) == 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if len(bomb_effects) else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if len(bomb_casings) else 'empty'}")
for k, v in created_bombs.items():
    print(f"{k}: {v}")

# test inputs:

# 5, 25, 25, 115
# 5, 15, 25, 35
