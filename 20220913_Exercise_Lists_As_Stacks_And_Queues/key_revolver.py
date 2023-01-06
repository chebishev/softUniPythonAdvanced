from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_stack = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
temp_barrel = gun_barrel_size
no_bullets = False
locks_destroyed = False
current_lock = None
while locks and bullets_stack:
    current_lock = locks.popleft()
    while bullets_stack:
        current_bullet = bullets_stack.pop()
        if not bullets_stack:
            no_bullets = True
        temp_barrel -= 1
        intelligence_value -= bullet_price
        if current_bullet > current_lock:
            print("Ping!")
            if no_bullets:
                locks.append(current_lock)
                break
            if not temp_barrel:
                print("Reloading!")
                temp_barrel = gun_barrel_size
        else:
            print("Bang!")
            if not locks:
                locks_destroyed = True
            if no_bullets:

                break
            if not temp_barrel:
                print("Reloading!")
                temp_barrel = gun_barrel_size
                break
            else:
                break

if locks_destroyed:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value}")
elif no_bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")

# test inputs:

# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500

# 20
# 6
# 14 13 12 11 10 5
# 13 3 11 10
# 800

# 33
# 1
# 12 11 10
# 10 20 30
# 100
