from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches_count = 0

while males and females:
    male = males.pop()
    if male <= 0:
        continue
    elif male % 25 == 0:
        if males:
            males.pop()
            continue
    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    elif female % 25 == 0:
        if females:
            females.popleft()
            males.append(male)
            continue
    if male == female:
        matches_count += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {matches_count}")
print(f"Males left:", (', '.join(str(x) for x in males[::-1]) if males else 'none'))
print(f"Females left:", (', '.join(str(x) for x in females) if females else 'none'))

# test inputs:

# 4 5 7 3 6 9 12
# 12 9 6 1

# 4 5 7 3 6 9 12
# 12 9 6 1
