from collections import deque


materials_boxes = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted_toys = []
target_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}


while materials_boxes and magic_levels:
    current_box = materials_boxes.pop() if magic_levels[0] or not materials_boxes[0] else 0
    current_magic = magic_levels.popleft() if current_box or not magic_levels[0] else 0
    
    if not current_magic:
        continue

    result = current_box * current_magic

    if target_presents.get(result):
        crafted_toys.append(target_presents[result])
    elif result < 0:
        materials_boxes.append(current_box + current_magic)
    elif result > 0:
        materials_boxes.append(current_box + 15)
        
if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_boxes:
    print(f"Materials left: {', '.join([str(x) for x in materials_boxes][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for toy in sorted(set(crafted_toys)):
    print(f"{toy}: {crafted_toys.count(toy)}")

# test inputs:

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0

# 30 5 15 60 0 30
# -15 10 5 -15 25

# 30 10
# 15 10 5 0 10
