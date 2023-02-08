from collections import deque


def check_gift_table(gift):
    for k in gifts:
        if gifts[k](gift_attempt) is not None:
            if k not in crafted_gifts:
                crafted_gifts[k] = 0
            crafted_gifts[k] += 1
            return True
    else:
        return False


materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": lambda x: x if 100 <= x < 200 else None,
    "Porcelain Sculpture": lambda x: x if 200 <= x < 300 else None,
    "Gold": lambda x: x if 300 <= x < 400 else None,
    "Diamond Jewellery": lambda x: x if 400 <= x < 500 else None,
}
crafted_gifts = {

}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    gift_attempt = current_material + current_magic

    if 100 <= gift_attempt < 500:
        if check_gift_table(gift_attempt):
            continue

    elif gift_attempt < 100:

        if gift_attempt % 2 == 0:
            gift_attempt = (current_material * 2) + (current_magic * 3)
        else:
            gift_attempt *= 2

    elif gift_attempt > 499:
        gift_attempt //= 2

    check_gift_table(gift_attempt)

if {"Gemstone", "Porcelain Sculpture"}.issubset(set(crafted_gifts.keys())) or \
        {"Gold", "Diamond Jewellery"}.issubset(set(crafted_gifts.keys())):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for k in sorted(crafted_gifts):
    print(f"{k}: {crafted_gifts[k]}")

# test inputs:

# 105 20 30 25
# 120 60 11 400 10 1

# 30 5 21 6 0 91
# 15 9 5 15 8

# 200
# 5 15 32 20 10 5
