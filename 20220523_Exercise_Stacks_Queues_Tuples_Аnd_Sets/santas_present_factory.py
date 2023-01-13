from collections import deque


boxes_with_materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
magic_dictionary = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while boxes_with_materials and magic_levels:
    current_box = boxes_with_materials.pop()
    current_level = magic_levels.popleft()
    current_magic_level = current_box * current_level
    if current_magic_level < 0:
        sum = current_box + current_level
        boxes_with_materials.append(sum)
    elif current_magic_level > 0:
        if current_magic_level in magic_dictionary:
            crafted_toys[magic_dictionary[current_magic_level]] += 1
        else:
            current_box += 15
            boxes_with_materials.append(current_box)
    else:
        if current_box == 0 and current_level == 0:
            continue
        elif current_box == 0:
            magic_levels.appendleft(current_level)
            continue
        elif current_level == 0:
            boxes_with_materials.append(current_box)
            continue

if (crafted_toys["Doll"] and crafted_toys["Wooden train"]) or (crafted_toys["Teddy bear"] and crafted_toys["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: ", end="")
    boxes_with_materials.reverse()
    print(*boxes_with_materials, sep=", ")
if magic_levels:
    print(f"Magic left: ", end="")
    print(*magic_levels, sep=", ")
for key in sorted(crafted_toys):
    if crafted_toys[key] > 0:
        print(f"{key}: {crafted_toys[key]}")

# test inputs:

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0

# 30 5 15 60 0 30
# -15 10 5 -15 25

# 30 10
# 15 10 5 0 10
